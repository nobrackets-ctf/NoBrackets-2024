from flask import Flask, request, make_response
import sqlite3
from hashlib import sha256

#############################
# MENU D'ADMINISTRATION     #
# DES COMPTES UTILISATEURS  #
#############################

# Initialiser l'application Flask
app = Flask(__name__)


# Fonction pour obtenir une connexion à la base de données
def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/login', methods=['GET'])
def login():
    # Récupérer les données des paramètres de requête
    username = request.args.get('username')
    password = request.args.get('password')
    
    # Vérifier si le nom d'utilisateur et le mot de passe sont fournis
    if not username or not password:
        return make_response({'error': 'Missing username or password'}, 400)
    
    # Établir une connexion à la base de données
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Hacher le mot de passe
    hashed_password = sha256(password.encode()).hexdigest()
    
    # Vérifier les identifiants dans la base de données
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_password))
    user = cursor.fetchone()
    
    # Fermer la connexion à la base de données
    conn.close()
    
    # Renvoyer la réponse appropriée
    if user:
        return make_response({'message': 'Login successful'}, 200)
    else:
        return make_response({'error': 'Invalid credentials'}, 401)

@app.route('/reset-password', methods=['GET'])
def reset_password():
    # Récupérer les données des paramètres de requête
    username     = request.args.get('username')
    new_password = request.args.get('new_password')
    
    # Vérifier si le nom d'utilisateur et le nouveau mot de passe sont fournis
    if not username or not new_password:
        return make_response({'error': 'Missing username or new password'}, 400)
    
    # Établir une connexion à la base de données
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Hacher le nouveau mot de passe
    hashed_password = sha256(new_password.encode()).hexdigest()
    
    # Mettre à jour le mot de passe dans la base de données
    cursor.execute("UPDATE users SET password = ? WHERE username = ?", (hashed_password, username))
    conn.commit()
    
    # Vérifier si l'utilisateur existe
    if cursor.rowcount == 0:
        conn.close()
        return make_response({'error': 'User not found'}, 404)
    
    # Fermer la connexion à la base de données
    conn.close()
    return make_response({'message': 'Password reset successful'}, 200)


@app.route('/create-account', methods=['GET'])
def create_account():
    # Récupérer les données des paramètres de requête
    username = request.args.get('username')
    password = request.args.get('password')
    
    # Vérifier si le nom d'utilisateur et le mot de passe sont fournis
    if not username or not password:
        return make_response({'error': 'Missing username or password'}, 400)
    
    # Établir une connexion à la base de données
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Vérifier si le nom d'utilisateur existe déjà
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        conn.close()
        return make_response({'error': 'Username already exists'}, 409)
    
    # Hacher le mot de passe
    hashed_password = sha256(password.encode()).hexdigest()
    
    # Insérer le nouvel utilisateur dans la base de données
    cursor.execute("INSERT INTO users (username, password, voted) VALUES (?, ?, 0)", (username, hashed_password))
    conn.commit()
    conn.close()
    
    return make_response({'message': 'Account created successfully'}, 201)

@app.route('/vote', methods=['GET'])
def vote():
    # Récupérer les données des paramètres de requête
    username = request.args.get('username')
    
    # Vérifier si le nom d'utilisateur est fourni
    if not username:
        return make_response({'error': 'Missing username'}, 400)
    
    # Établir une connexion à la base de données
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Vérifier si l'utilisateur existe
    cursor.execute("SELECT voted FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    
    if not user:
        conn.close()
        return make_response({'error': 'User not found'}, 404)
    
    # Vérifier si l'utilisateur a déjà voté
    if user[0] == 1:
        conn.close()
        return make_response({'error': 'User has already voted'}, 403)
    
    # Mettre à jour le statut de vote de l'utilisateur
    cursor.execute("UPDATE users SET voted = 1 WHERE username = ?", (username,))
    conn.commit()
    conn.close()
    
    return make_response({'message': 'Vote recorded successfully'}, 200)


@app.route('/has-voted', methods=['GET'])
def has_voted():
    # Récupérer le nom d'utilisateur des paramètres de requête
    username = request.args.get('username')
    
    # Vérifier si le nom d'utilisateur est fourni
    if not username:
        return make_response({'error': 'Missing username'}, 400)
    
    # Établir une connexion à la base de données
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Vérifier si l'utilisateur existe et récupérer son statut de vote
    cursor.execute("SELECT voted FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    
    conn.close()
    
    if not user:
        return make_response({'error': 'User not found'}, 404)
    
    # Renvoyer le statut de vote de l'utilisateur
    has_voted = user[0] == 1
    return make_response({'has_voted': has_voted}, 200)


if __name__ == '__main__':
    # Exécuter l'application Flask
    app.run(host='0.0.0.0', port=8080, debug=False)