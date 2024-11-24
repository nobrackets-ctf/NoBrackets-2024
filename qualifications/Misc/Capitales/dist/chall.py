import time
from random import randint
from flag import FLAG

chrono = time.time()

questions = [
    "Quelle est la capitale de l'Allemagne ?",
    "Quelle est la capitale de l'Italie ?",
    "Quelle est la capitale de l'Espagne ?",
    "Quelle est la capitale du Japon ?",
    "Quelle est la capitale du Canada ?"
]

reponses = [
    "Berlin",
    "Rome",
    "Madrid",
    "Tokyo",
    "Ottawa"
]

numero_question = randint(0,5)

reponse_utilisateur = input(questions[numero_question] + " >>>")

fin_chrono = time.time()

if fin_chrono - chrono > 1:
    print("Il faut être plus rapide !")
    exit()

if reponse_utilisateur == reponses[numero_question]:
    print(f"Bravo !! Voici le flag : {FLAG}")
else:
    print("Dommage, ce n'est pas la bonne réponse")
