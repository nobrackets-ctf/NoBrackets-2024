#!/usr/bin/env python3

import hashlib
import random
from inputimeout import inputimeout, TimeoutOccurred
from pwn import *


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def get_rockyou_passwords(file_path, limit=500):
    passwords = []
    with open(file_path, 'r') as f:
        for i in range(limit):
            password = f.readline().strip()
            if password:
                passwords.append(password)
    return passwords


def choose_random_passwords(passwords, count=30):
    return random.sample(passwords, count)


def chall(passwords):
    log.info(f"Bonjour ô grand Hacker ! J'ai perdu tous les mots de passe de mon gestionnaire mais j'ai encore les hash, peut-être pourrais-tu m'aider ?\nJ'ai un peu honte tu vas les trouver très génériques...\n")
    for i, password in enumerate(passwords):
        hashed_password = hash_password(password)
        log.info(f"Hash #{i+1}: {hashed_password}")
        solved = False

        try:
            response = inputimeout(prompt="Entrez le mot de passe en clair > ", timeout=30).strip()
            if response == password:
                log.success(f"Bravo ! Le mot de passe {i+1} est correct.")
                solved = True
            else:
                log.failure("Mot de passe incorrect, essayez encore.")
                solved = False
                break
        except TimeoutOccurred:
            log.failure("Vous mettez trop longtemps...ça ne devrait pas être si compliqué !")
            solved = False
            break

    if solved:
        log.success("Félicitations ! Vous avez retrouvé tous mes mots de passe ! Pour vous récompenser, c'est cadeau : NBCTF{D0n7_cr4ck_7h1ng5_f0r_p30pl3}")
    else:
        log.failure("Vous avez échoué. Veuillez réessayer.")


if __name__ == "__main__":
    rockyouPath = "./rockyou.txt"
    rockyouPwds = get_rockyou_passwords(rockyouPath)
    selectedPwds = choose_random_passwords(rockyouPwds)
    chall(selectedPwds)
