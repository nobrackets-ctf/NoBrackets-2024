#!/usr/bin/env python3
import subprocess
import re

# Regex qui détermine les sites légaux
pattern = r'https?://[a-zA-Z0-9.-]+\.nobrackets\.fr(/[a-zA-Z0-9./?%_-]*)?'

# Fonction de vérification de la légalité d'une url
def is_legal_url(url):
    return re.match(pattern, url) is not None

# Bannière
print("----------------------------")
print("~~ Ce site est-il légal ? ~~")
print("----------------------------")

# Entrée utilisateur
value = input("Entrez un site (eg: https://wiki.nobrackets.fr/) >>> ")

# Vérification que l'entrée utilisateur ne soit pas vide
if not value:
    print("Erreur. Veuillez entrer une URL.")
    exit(-1)

# Vérification de la légalité de l'URL entrée
if not is_legal_url(value):
    print("Erreur. Votre URL est soit mal formatée soit illégale !")
    exit(-1)

# Test de l'existence du site

process = subprocess.run("curl -I "+value, capture_output=True, shell=True)
res = process.stdout
if not res:
    print("Erreur. Le site ne semble pas exister.")
    exit(-1)

# Affichage de l'échange
print("Succès ! Le site est légal et fonctionnel ! Voici ses informations : \n\n")
print(res.decode())
exit(0)
