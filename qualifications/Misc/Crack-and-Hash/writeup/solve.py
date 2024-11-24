#!/usr/bin/nv python3

import subprocess
from pwn import *


# On commence par identifier que les hash sont en SHA256
# Des mots de passe simples désignent certainement rockyou.txt


def parse_out(output, hashToCrack):
    indexHash = output.find(hashToCrack)
    output = output[indexHash+len(hashToCrack)+1:]
    indexNewL = output.find('\n')
    passwordCracked = output[:indexNewL]
    print("Cracked : " + passwordCracked + "\n")
    return passwordCracked


def main():
    # On se connecte à l'instance
    r = remote("localhost",1337)
    
    # Boucle infinie car on ne sait pas le nombre de mots de passe à cracker
    while True:
        # Message d'intro
        msg = r.recvuntil(b': ')
        # Si le message est le flag, on le print
        if "NBCTF" in msg.decode():
            print(msg)
        # On récupère le hash
        hashToCrack = r.recv(64).decode().strip()
        print("Hash : ", hashToCrack)
        # Création de la commande hashcat, 1400 désigne le SHA256
        hashcatCmd = f"hashcat -m 1400 {hashToCrack} -a 0 rockyou.txt"

        try:
            # On exécute la commande
            output = subprocess.check_output(hashcatCmd, shell=True, stderr=subprocess.STDOUT).decode().strip()
            # On parse le résultat
            passwordCracked = parse_out(output,hashToCrack)
            # On renvoie le mot de passe
            r.sendline(passwordCracked.encode())
        except subprocess.CalledProcessError as e:
            print(f"Error executing hashcat command: {e}")


if __name__=="__main__":
    main()