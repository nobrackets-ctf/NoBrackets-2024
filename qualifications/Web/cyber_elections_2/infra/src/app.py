from flask import Flask, request, render_template, redirect, url_for, session, flash, jsonify, make_response
import random
import string
import sqlite3
from base64 import b64encode, b64decode

# Initialiser l'application Flask
app = Flask(__name__)
# Générer une clé secrète aléatoire pour la gestion des sessions
app.secret_key = ''.join(random.choices(string.ascii_letters + string.digits, k=32))

# Définir les candidats pour l'élection
CANDIDATES = {
    'government': 'Kael Syntar',
    'opposition': 'Zarya Velkyn'
}

# Initialiser le décompte des votes
#   Les deux cent membres du gouvernement ont déjà voté :)
VOTES = {
    'government': 200,
    'opposition': 0
}

@app.route('/')
def index():
    # Afficher la page principale avec la liste des candidats
    return render_template('index.html', candidates=CANDIDATES)

def get_random_captcha():
    # Établir une connexion à la base de données SQLite
    conn = sqlite3.connect('captcha.db')
    cursor = conn.cursor()
    # Sélectionner une question et sa réponse au hasard dans la table 'captchas'
    cursor.execute("SELECT question, answer FROM captchas ORDER BY RANDOM() LIMIT 1")
    # Récupérer le résultat de la requête
    res = cursor.fetchone()
    # Fermer la connexion à la base de données
    conn.close()
    # Retourner la question et la réponse sélectionnées
    return res

@app.route('/captcha', methods=['GET', 'POST'])
def captcha():
    # Gestion de la requête GET
    if request.method == 'GET':
        # Obtenir une question de captcha aléatoire
        captcha_question, captcha_answer = get_random_captcha()
        # Stocker la question dans la session
        resp = make_response(render_template('captcha.html', question=captcha_question))
        # Stocker la question et la réponse dans les cookies
        resp.set_cookie('captcha_question', b64encode(captcha_question.encode()).decode())
        resp.set_cookie('captcha_answer', b64encode(captcha_answer.encode()).decode())
        return resp

    # Gestion de la requête POST
    elif request.method == 'POST':
        # Récupérer la réponse de l'utilisateur depuis le formulaire
        user_answer = request.form.get('answer')
        # Récupérer la question et la réponse stockées dans les cookies
        preprocess_stored_question = request.cookies.get('captcha_question')
        preprocess_stored_answer = request.cookies.get('captcha_answer')

        # Vérifier s'il y a une question et une réponse stockées
        if not preprocess_stored_question or not preprocess_stored_answer:
            flash("Pas de captcha trouvé. Rendez-vous sur /captcha pour en obtenir un nouveau.", "error")
            return redirect(url_for('index'))

        try:
            stored_question = b64decode(preprocess_stored_question).decode()
            stored_answer = b64decode(preprocess_stored_answer).decode()
        except Exception as e:
            flash("Erreur lors du décodage du captcha.", "error")
            return redirect(url_for('index'))

        # Vérifier si l'utilisateur a fourni une réponse
        if not user_answer:
            flash("Vous devez fournir une réponse au captcha.", "error")
            return redirect(url_for('index'))

        # Requête SQL pour vérifier si la réponse est correcte
        conn = sqlite3.connect('captcha.db')
        cursor = conn.cursor()
        cursor.execute("SELECT answer FROM captchas WHERE question = ?", (stored_question,))
        result = cursor.fetchone()
        conn.close()

        # Si la requête SQL ne retourne pas de réponse, afficher une erreur et rediriger vers la page d'index
        if not result:
            flash("Erreur lors de la récupération du captcha.", "error")
            return redirect(url_for('index'))

        # Vérifier si la réponse de l'utilisateur est correcte
        if stored_answer and user_answer.lower() == stored_answer.lower() and result[0].lower() == user_answer.lower():
            # Marquer le captcha comme résolu dans la session
            session['captcha_solved'] = True
            flash("Bonne réponse au captcha, vous pouvez voter !", "success")
            return redirect(url_for('index'))
        else:
            # Réponse incorrecte
            flash("Mauvaise réponse au captcha.", "error")
            return redirect(url_for('index'))

    # Gestion des méthodes de requête invalides
    return jsonify({'error': 'Méthode de requête invalide'}), 405

@app.route('/vote', methods=['POST'])
def vote():
    # Obtenir le candidat sélectionné depuis le formulaire
    candidate = request.form.get('candidate')
    if candidate not in CANDIDATES:
        # Si un candidat invalide est sélectionné, afficher une erreur
        flash("Candidat invalide.", "error")
        return redirect(url_for('index'))

    if session.get('voted'):
        # Si l'utilisateur a déjà voté, afficher une erreur et rediriger vers la page de vote
        flash("Vous avez déjà voté.", "error")
        return redirect(url_for('index'))

    if not session.get('captcha_solved'):
        flash("Vous devez résoudre le captcha pour voter.", "error")
        return redirect(url_for('captcha'))

    # Incrémenter le nombre de votes pour le candidat sélectionné
    VOTES[candidate] += 1
    # Marquer l'utilisateur comme ayant voté
    session['voted'] = True
    # Rediriger vers la page des résultats
    return redirect(url_for('results'))

@app.route('/results')
def results():
    # Vérifier si l'utilisateur a voté
    if not session.get('voted'):
        # Si non, afficher une erreur et rediriger vers la page de vote
        flash("Vous devez voter avant de voir les résultats.", "error")
        return redirect(url_for('index'))

    # Déterminer le gagnant en fonction du nombre de votes
    winner = max(VOTES, key=VOTES.get)

    # Afficher le flag si le nombre de vote de l'opposition est supérieur à celui du gouvernement
    flag = ""
    if VOTES['opposition'] > VOTES['government']:
        with open('flag.txt','r') as f:
            flag = f.read().strip()

    # Afficher la page des résultats
    return render_template('results.html', votes=VOTES, winner=CANDIDATES[winner], candidates=CANDIDATES, flag=flag)

@app.route('/source')
def view_source():
    # Définit une route pour afficher le code source de l'application

    # Ouvre le fichier actuel en mode lecture
    with open(__file__, 'r') as file:
        # Lit tout le contenu du fichier
        code = file.read()

    # Renvoie le template 'source.html' avec le code source comme variable
    return render_template('source.html', code=code)


if __name__ == '__main__':
    # Exécuter l'application Flask
    app.run(host='0.0.0.0', port=5000, debug=False)
