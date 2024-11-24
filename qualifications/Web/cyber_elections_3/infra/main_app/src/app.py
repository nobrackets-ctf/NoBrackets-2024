from flask import Flask, request, render_template, redirect, url_for, session, flash, jsonify, make_response
import random
import string
import sqlite3
from hashlib import sha256
import requests
from functools import wraps

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
VOTES = {
    'government': 200,
    'opposition': 0
}

TRACKER = {}

# Décorateur pour tracker le "Referer header" (source)
def check_referer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Récupère le "Referer" header de la requête
        referer = request.headers.get('Referer')
        if referer:
            try:
                # Tente d'effectuer une requête GET vers l'URL du referer
                response = requests.get(referer, timeout=1)
                if response.status_code == 200:
                    # Si la requête réussit, enregistre les informations dans TRACKER
                    ip_address = request.remote_addr
                    if 'username' in session:
                        # Si l'utilisateur est connecté, enregistre son nom d'utilisateur
                        TRACKER[ip_address] = {'referer': referer, 'username': session['username']}
                    else:
                        # Sinon, enregistre seulement le referer
                        TRACKER[ip_address] = {'referer': referer}

            except requests.RequestException as e:
                # Si la requête échoue, ne fait rien et continue l'exécution
                pass
        # Appelle la fonction décorée
        return func(*args, **kwargs)
    return wrapper

# Décorateur pour vérifier si l'utilisateur est connecté
def check_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'username' not in session:
            flash("Vous devez être connecté pour accéder à cette page.", "error")
            return redirect(url_for('login'))
        return func(*args, **kwargs)
    return wrapper

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Gère la route de connexion, accepte les méthodes GET et POST
    if request.method == 'POST':
        # Si la méthode est POST, on traite le formulaire de connexion
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Envoie une requête à l'API accounts-app pour vérifier les identifiants
        response = requests.get('http://accounts-app:8080/login', params={'username': username, 'password': password})
        
        if response.status_code == 200:
            # Si la réponse est 200 (OK), la connexion est réussie
            session['username'] = username  # Stocke le nom d'utilisateur dans la session
            flash('Connexion réussie!', 'success')  # Affiche un message de succès
            return redirect(url_for('index'))  # Redirige vers la page d'accueil
        else:
            # Si la réponse n'est pas 200, la connexion a échoué
            flash('Nom d\'utilisateur ou mot de passe incorrect.', 'error')  # Affiche un message d'erreur
    
    # Si la méthode est GET ou si la connexion a échoué, affiche le formulaire de connexion
    return render_template('login.html')



@app.route('/logout')
def logout():
    # Gère la déconnexion des utilisateurs
    # Supprime la session de l'utilisateur
    session.pop('username', None)
    flash('Vous avez été déconnecté.', 'info')
    # Redirige vers la page de connexion
    return redirect(url_for('login'))



@app.route('/reset-password', methods=['GET', 'POST'])
@check_login
def reset_password():
    if request.method == 'POST':
        new_password = request.form.get('new_password')
        username = session['username']
        
        # Make a request to the accounts-app API for password reset
        response = requests.get('http://accounts-app:8080/reset-password', params={'username': username, 'new_password': new_password})
        
        if response.status_code == 200:
            flash('Mot de passe réinitialisé avec succès.', 'success')
            return redirect(url_for('index'))
        else:
            flash('Erreur lors de la réinitialisation du mot de passe.', 'error')
    
    return render_template('reset_password.html')


@app.route('/')
@check_login
@check_referer
def index():
    # Afficher la page principale avec la liste des candidats
    return render_template('index.html', candidates=CANDIDATES)



@app.route('/vote', methods=['POST'])
@check_login
@check_referer
def vote():
    # Vérifier si l'utilisateur a déjà voté en utilisant l'API accounts-app
    username = session['username']
    # Vérifier si l'utilisateur a déjà voté en utilisant l'API accounts-app
    response = requests.get('http://accounts-app:8080/has-voted', params={'username': username})
    if response.status_code == 200:
        if response.json()['has_voted']:
            flash("Vous avez déjà voté.", "error")
            return redirect(url_for('index'))
    else:
        flash("Erreur lors de la vérification du statut de vote.", "error")
        return redirect(url_for('index'))
    
    # Récupérer le candidat choisi depuis le formulaire
    candidate = request.form.get('candidate')
    # Vérifier si le candidat est valide
    if candidate not in CANDIDATES:
        flash("Candidat invalide.", "error")
        return redirect(url_for('index'))
    
    # Enregistrer le vote en utilisant l'API accounts-app
    response = requests.get('http://accounts-app:8080/vote', params={'username': username})
    if response.status_code == 200:
        # Incrémenter le nombre de votes pour le candidat choisi
        VOTES[candidate] += 1
        # Rediriger vers la page des résultats
        return redirect(url_for('results'))
    else:
        flash("Erreur lors de l'enregistrement du vote.", "error")
        return redirect(url_for('index'))



@app.route('/results')
@check_login
@check_referer
def results():
    if 'username' not in session:
        flash("Vous devez être connecté pour voir les résultats.", "error")
        return redirect(url_for('login'))
    
    username = session['username']
    
    # Vérifier si l'utilisateur a voté en utilisant l'API accounts-app
    response = requests.get('http://accounts-app:8080/has-voted', params={'username': username})
    if response.status_code == 200:
        if not response.json()['has_voted']:
            flash("Vous devez voter avant de voir les résultats.", "error")
            return redirect(url_for('index'))
    else:
        flash("Erreur lors de la vérification du statut de vote.", "error")
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


if __name__ == '__main__':
    # Exécuter l'application Flask
    app.run(host='0.0.0.0', port=5000, debug=False)