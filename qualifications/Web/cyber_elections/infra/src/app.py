from flask import Flask, request, render_template, redirect, url_for, session, flash
import random
import string

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
    with open(__file__, 'r') as file:
        code = file.read()

    return render_template('source.html', code=code)


if __name__ == '__main__':
    # Exécuter l'application Flask
    app.run(host='0.0.0.0', port=5000, debug=False)
