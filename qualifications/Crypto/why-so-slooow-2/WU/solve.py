# Tu auras besoin de ça : https://pycryptodome.readthedocs.io/en/latest/src/installation.html
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import random

# Chargement des données du `output.txt`
exec(open("output.txt", "r").read())

# Pour déchiffrer le flag
def safe_decrypt(ct, u):
	# Dérive une clef AES à partir d'un int
	random.seed(u)
	key = random.randbytes(AES.block_size)
	iv  = b"."*AES.block_size

	# Déchiffre le ciphertext
	cipher = AES.new(key, AES.MODE_CBC, iv=iv)
	return unpad(cipher.decrypt(ct), AES.block_size)

# Cette fonction calcul la somme des n premiers entiers naturels non nuls
def somme_des_n_premiers_entiers(n):
	return (n * (n + 1)) // 2

# Cette fonction calcul la somme des carrés des n premiers entiers naturels non nuls
def somme_des_n_premiers_carres(n):
	return (n*(n+1)*(2*n+1)) // 6

# Calcul l'exposant modulo l'ordre du groupe mutliplicatif ...
s1 = somme_des_n_premiers_entiers(GROS_INDEX)
s2 = somme_des_n_premiers_carres(GROS_INDEX)
t = (s1 + s2) % (MODULO-1)
# .. puis le secret ...
s = pow(1337, t, MODULO)

# ... enfin, affiche le flag déchiffré
print(safe_decrypt(ct, s))