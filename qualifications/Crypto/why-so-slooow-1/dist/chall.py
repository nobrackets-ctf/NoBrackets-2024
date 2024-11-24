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

# Définition de mes paramètres magiques
GROS_INDEX = (1 << 123) + (1 << 78) + (1 << 56)
# MODULO est premier, tu peux inverser ce que tu veux :)
MODULO = 1229894983634972312797718042580418393679633615251177958057988339965550336867464103010048241

A = random.randint(1, MODULO-1)
B = random.randint(1, MODULO-1)

# Calcul du secret
u = 17
for _ in range(GROS_INDEX):
	u *= A
	u += B
	u %= MODULO

# Chiffrement du FLAG
FLAG = "NBCTF{CENSURÉ}".encode("utf-8")
ct = safe_encrypt(FLAG, u)

# Écriture dans output.txt des {résultats,informations publiques}
out = ""
out += f"A = {A}\n"
out += f"B = {B}\n"
out += f"GROS_INDEX = {GROS_INDEX}\n"
out += f"MODULO = {MODULO}\n"
out += f'ct = bytes.fromhex("{ct.hex()}")'

open("output.txt", "w").write(out)