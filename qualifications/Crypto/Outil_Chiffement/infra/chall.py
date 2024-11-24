"""
Outil de chiffrement sécurisé
"""
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

key = os.urandom(16)
FLAG = b'NBCTF{0Racl3_Sup3R_P0w3r}'

assert len(FLAG) == 25

def encrypt(plaintext):
	padded = pad(plaintext + FLAG, 16)
	cipher = AES.new(key, AES.MODE_ECB)

	ciphertext = cipher.encrypt(padded)
	return ciphertext.hex()

print("=======Bienvenue sur votre plateforme de chiffrement sécurisé=======")
while True:
	plaintext = input("Entrez le texte que vous souhaitez chiffrer : ").encode()

	ciphertext = encrypt(plaintext)

	print(f"Voici vos données chiffrees : {ciphertext}")
