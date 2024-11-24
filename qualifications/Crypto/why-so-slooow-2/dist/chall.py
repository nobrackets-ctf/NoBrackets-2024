# Tu auras besoin de ça : https://pycryptodome.readthedocs.io/en/latest/src/installation.html
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import random

# Fonctions utilitaires
def safe_encrypt(flag, u):
	# Dérive une clef AES à partir d'un int
	random.seed(u)
	key = random.randbytes(AES.block_size)
	iv  = b"."*AES.block_size

	# Chiffre le flag
	cipher = AES.new(key, AES.MODE_CBC, iv=iv)
	return cipher.encrypt(pad(flag, AES.block_size))

def safe_decrypt(ct, u):
	# Dérive une clef AES à partir d'un int
	random.seed(u)
	key = random.randbytes(AES.block_size)
	iv  = b"."*AES.block_size

	# Déchiffre le ciphertext
	cipher = AES.new(key, AES.MODE_CBC, iv=iv)
	return unpad(cipher.decrypt(ct), AES.block_size)

# Définitions de mes paramètres magiques
GROS_INDEX = (1 << 123) + (1 << 78) + (1 << 56)
# MODULO est premier, tu peux inverser ce que tu veux :)
MODULO = 1229894983634972312797718042580418393679633615251177958057988339965550336867464103010048241

# Calcul du secret
s = 1
for k in range(1, GROS_INDEX+1):
	s *= pow(1337, k**2 + k, MODULO)
	s %= MODULO

# Chiffrement du flag
flag = "NBCTF{CENSURÉ}".encode("utf-8")
ct = safe_encrypt(flag, s)

# Écriture dans output.txt des {resultats,informations publiques}
out = ""
out += f"GROS_INDEX = {GROS_INDEX}\n"
out += f"MODULO = {MODULO}\n"
out += f'ct = bytes.fromhex("{ct.hex()}")'

open("output.txt", "w").write(out)
