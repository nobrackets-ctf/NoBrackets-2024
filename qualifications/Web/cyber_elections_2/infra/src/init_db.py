#!/usr/bin/env python3

import sqlite3

def init_db():
    conn = sqlite3.connect('captcha.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS captchas (id INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT, answer TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('Quelle est la capitale de : France ?', 'Paris')''')
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('Quelle est la capitale de : Allemagne ?', 'Berlin')''')
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('Quelle est la capitale de : Italie ?', 'Rome')''')
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('Quelle est la capitale de : Espagne ?', 'Madrid')''')
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('Quelle est la capitale de : Portugal ?', 'Lisbon')''')
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('Quelle est la capitale de : Suisse ?', 'Berne')''')
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('Quelle est la capitale de : Autriche ?', 'Vienne')''')
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('Quelle est la capitale de : Belgique ?', 'Bruxelles')''')
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('Quelle est la capitale de : Danemark ?', 'Copenhague')''')
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('Quelle est la capitale de : Luxembourg ?', 'Luxembourg')''')
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('Quelle est la capitale de : Pays-Bas ?', 'Amsterdam')''')
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('Quelle est la capitale de : Suède ?', 'Stockholm')''')
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('Quelle est la capitale de : Norvège ?', 'Oslo')''')
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('Quelle est la capitale de : Finlande ?', 'Helsinki')''')
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('Quelle est la capitale de : Islande ?', 'Reykjavik')''')
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('Quelle est la capitale de : Lettonie ?', 'Riga')''')
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('Quelle est la capitale de : Lituanie ?', 'Vilnius')''')
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('Quelle est la capitale de : Pologne ?', 'Varsovie')''')
    
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('En quelle année est né Léonard De Vinci ?', '1452')''')
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('En quelle année est né Napoléon Bonaparte ?', '1769')''')
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('En quelle année est né Charles de Gaulle ?', '1890')''')
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('En quelle année est né François Mitterrand ?', '1916')''')
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('En quelle année est né Jacques Chirac ?', '1926')''')
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('En quelle année est né Nicolas Sarkozy ?', '1955')''')
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('En quelle année est né François Hollande ?', '1954')''')
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('En quelle année est né Emmanuel Macron ?', '1977')''')

    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('Combien fait 2x3 ?', '6')''')
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('Combien fait 3x3 ?', '9')''')
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('Combien fait 4x4 ?', '16')''')
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('Combien fait 5x5 ?', '25')''')
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('Combien fait 6x6 ?', '36')''')
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('Combien fait 7x7 ?', '49')''')
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('Combien fait 8x8 ?', '64')''')
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('Combien fait 9x9 ?', '81')''')
    cursor.execute('''INSERT INTO captchas (question, answer) VALUES ('Combien fait 10x10 ?', '100')''')

    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()