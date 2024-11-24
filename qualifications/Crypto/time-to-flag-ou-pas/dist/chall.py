"""
Ce challenge nécessite de parler avec un serveur faisant tourner le code python ci-dessous.

Je te conseil de d'abord flag "en local", c'est à dire de flag directement avec ce fichier.
(et pas en communiquant avec le serveur)

Pour ce faire, install la lib python pwntools (ici: https://docs.pwntools.com/en/stable/)
et fais :
```
conn = process(["python", "chall.py"])
```
puis lorsque tu auras une solution prête tu pourras utiliser l'exact même code en
changant `conn` par :
```
conn = remote("host", port) # remplace host (une string) et le port (int)
```
Et tu auras le flag du remote ! Pour apprendre a utiliser pwntools je te conseille
la cheatsheet suivante : https://xavierholt.github.io/cheatsheets/pwntools.html

N'hésites pas a demander de l'aide sur discord !
"""

from Crypto.Util.number import long_to_bytes, bytes_to_long
from Crypto.Util.Padding import pad
from more_itertools import divide
from Crypto.Hash import SHAKE256
from Crypto.Cipher import AES
from random import randint
from time import time

FLAG = "NBCTF{CENSURÉ}".encode('utf-8')
SECRET_MAX = 2**24
LOG_MAX = 256
MAX = 2**LOG_MAX
DIM = 8

def get_encrypted_flag(s):
	shake = SHAKE256.new()
	shake.update(str(s).encode('utf-8'))

	key = shake.read(AES.block_size)
	iv  = b"."*AES.block_size

	cipher = AES.new(key, AES.MODE_CBC, iv=iv)
	return cipher.encrypt(pad(FLAG, AES.block_size)).hex()

def ps(u, v):
	return sum(uu*vv for uu,vv in zip(u, v))

def expand_time(n):
	"""
	Si tu ne comprends pas cette fonction, tu peux la voir comme une boîte noire qui
	prends le timestamp actuel en seconde (nb de secondes ecoulées depuis le 01/01/1970)
	et le convertit de manière déterministe en vecteur de dimension 8 avec des entrées de
	128 bits.
	"""
	shake = SHAKE256.new()
	shake.update(long_to_bytes(n))

	res = shake.read((LOG_MAX//DIM)*DIM)
	return [bytes_to_long(bytes(uu)) for uu in divide(DIM, res)]

class PRNG:
	def __init__(self):
		self.secret = [randint(1, SECRET_MAX) for _ in range(DIM)]

	def get_secret(self):
		return self.secret

	def random(self):
		now = int(time())
		u = expand_time(now)

		return ps(u, self.secret)

mon_prng = PRNG()

print("Hello ! Bienvenue sur mon PRNG suuuper sécurisé :)")
print("J'ai eu des petits problèmes avec la v1, maintenant, tu ne peux recevoir qu'un \
seul nombre aléatoire ...")
print("Commandes disponibles :")
print("`f`: recevoir un nombre aléatoire + le flag chiffré")
print("`q`: quitter")

while True:
	choice = input("> ")

	if choice == 'f':
		r = mon_prng.random()
		print(r)
		ct = get_encrypted_flag(mon_prng.secret)
		print(f"{ct = }")
		exit()

	elif choice == 'q':
		exit()

	else:
		print('invalid choice')
		continue
