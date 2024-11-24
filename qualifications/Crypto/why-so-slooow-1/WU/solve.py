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

## Retrouvons la valeur finale de `u`
# Calcul de `r`, r = B*(1 - A)^{-1} (mod MODULO)
r = (B * pow(1-A, -1, MODULO)) % MODULO

# Calcul de `u_{GROS_INDEX}`
u = (pow(A, GROS_INDEX, MODULO) * (17 - r) + r) % MODULO

# Done!
print(safe_decrypt(ct, u).decode())