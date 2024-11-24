from Crypto.Util.number import long_to_bytes, bytes_to_long
from sage.all import Matrix, vector, identity_matrix
from Crypto.Util.Padding import pad, unpad
from more_itertools import divide
from Crypto.Hash import SHAKE256
from pwn import process, remote
from Crypto.Cipher import AES
from time import time, sleep

LOG_MAX = 256
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
conn = process(['python', '../dist/chall.py'])
# conn = remote("127.0.0.1", 1338)

# Reception du prompt
_ = conn.recvuntil(b"> ")

# Reception du nombre et du flag
_ = conn.sendline(b"f")
x = int(conn.recvline().strip())
f = bytes.fromhex(eval(conn.recvline().strip().decode().split("= ")[1]))

# On close la connexion
conn.close()

# Construction de la lattice
u = expand_time(int(time()))
u.append(-x)

M = identity_matrix(DIM+1)
M = M.augment(vector(u))
llled = M.LLL()

# On extrait la seed de la lattice
s = [int(ss) for ss in llled.rows()[0][:DIM]]

# Déchiffre et print le flag :)
flag = decrypt_flag(list(s), f)
print(flag.decode('utf-8'))