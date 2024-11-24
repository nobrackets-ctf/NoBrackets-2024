from Crypto.Util.number import long_to_bytes, bytes_to_long
from Crypto.Util.Padding import pad, unpad
from sage.all import Matrix, vector
from more_itertools import divide
from Crypto.Hash import SHAKE256
from pwn import process, remote
from Crypto.Cipher import AES
from time import time, sleep

LOG_MAX = 128
MAX = 2**LOG_MAX
DIM = 8

def decrypt_flag(s, ct):
	shake = SHAKE256.new()
	shake.update(str(s).encode('utf-8'))

	key = shake.read(AES.block_size)
	iv  = b"."*AES.block_size

	cipher = AES.new(key, AES.MODE_CBC, iv=iv)
	return unpad(cipher.decrypt(ct), AES.block_size)

def expand_time(n):
	shake = SHAKE256.new()
	shake.update(long_to_bytes(n))

	res = shake.read((LOG_MAX//DIM)*DIM)
	return [bytes_to_long(bytes(uu)) for uu in divide(DIM, res)]

# Setup du remote (ici, c'est 'process' car le CTF est fini)
conn = process(['python', '../infra/chall.py'])
# conn = remote("127.0.0.1", 1337)

_ = conn.recvuntil(b"> ")

# M*s = t
M = []
t = []

# Reception de DIM nombre 'random'
for _ in range(DIM):
	_ = conn.sendline(b"a")

	u = expand_time(int(time()))
	M.append(u)

	t.append(int(conn.recvline().strip()))

	_ = conn.recvuntil(b"> ")
	sleep(1)

# Reception du flag chiffré
conn.sendline(b"f")
f = bytes.fromhex(eval(conn.recvline().strip().decode().split("= ")[1]))

# Fermeture de la connexion
conn.close()

# Résoudre le système linéire pour 's'
M = Matrix(M)
t = vector(t)
s = M.solve_right(t)

# Déchiffrer le flag et l'afficher :)
flag = decrypt_flag(list(s), f)
print(flag.decode('utf-8'))