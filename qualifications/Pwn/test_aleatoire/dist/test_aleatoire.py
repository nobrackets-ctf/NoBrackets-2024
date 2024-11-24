#!/usr/bin/env python3
import os
import random
# Lire le fichier flag.txt
if os.path.exists("flag.txt"):
    with open("flag.txt", "r") as f:
        FLAG = f.read().strip()
else:
    print("Vous devez mettre un fichier flag.txt dans le dossier du challenge.")
    exit(1)

print("------------------------------------------------------------")
print("Bienvenue dans le programme de recrutement de la rebellion !")
print(" ~ Made with\t❤️\tby Drahoxx ~")
print("------------------------------------------------------------\n\n")

print("Quel est votre pseudonyme ?")
username = input("> ")

print("Bonjour " + username + ", vous allez pouvoir commencer le test !\n\n")

print("------------------------------------------------------------")
print("Q1. Quel est le plus grand nombre premier inférieur à 100 ?")
print("------------------------------------------------------------")

answer = input("> ")

if answer == "97":
    print("Bonne réponse !")
else:
    print("Mauvaise réponse !")
    exit(1)

print("------------------------------------------------------------")
print("Q2. Comment s'appelle le nom de notre ennemi ?")
print("------------------------------------------------------------")

answer = input("> ")

if answer == "Cybort":
    print("Bonne réponse !")
else:
    print("Mauvaise réponse !")
    exit(1)

print("------------------------------------------------------------")
print("Q3. Trouvez un nombre aléatoire entre 1 et 3000")
print("------------------------------------------------------------")

answer = input("> ")

if str(random.randint(1, 3000)).startswith(answer):
    print("Bonne réponse !")
else:
    print("Mauvaise réponse !")
    exit(1)

print("------------------------------------------------------------")
print("Bravo, vous avez réussi le test !")
print("Vous allez pouvoir rejoindre la rebellion !")
print("------------------------------------------------------------\n")
print("...Vérification des vos informations...")
if len(username) < 3:
    print("Votre pseudonyme est trop court !")
    exit(1)
elif len(username) > 32:
    print("Votre pseudonyme est trop long !")
    exit(1)


print("Vous avez réussi le test " + username + "!")
print("Voici votre flag :")
print("------------------------------------------------------------")
print(FLAG)