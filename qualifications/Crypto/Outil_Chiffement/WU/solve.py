"""
AES Oracle Padding Attack
"""

from pwn import *

alphabet = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN1234567890_{}-!?"

r = remote("127.0.0.1", 1337)

def get_cipher(plain):
    r.recvuntil(b"chiffrer : ")
    r.sendline(plain)
    r.recvuntil(b"chiffrees : ")
    ciphertext = r.recvuntil(b"\n").strip().decode()

    return ciphertext

def get_flag():
    length = 32 - 1 # 2 blocs nécessaires pour récupérer un flag de 25 caractères
    FLAG = ''

    while True:
        payload = 'A' * (length - len(FLAG))
        cipher_org = get_cipher(payload.encode())

        for letter in alphabet:
            cipher_test = get_cipher((payload + FLAG + letter).encode())
            if cipher_test[32:64] == cipher_org[32:64]:
                FLAG += letter
                print(FLAG)
                break

get_flag()