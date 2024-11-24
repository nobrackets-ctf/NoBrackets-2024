from pwn import *

reponses = {"Allemagne":"Berlin", "Italie":"Rome", "Espagne":"Madrid", "Japon":"Tokyo", "Canada":"Ottawa"}

r = remote("localhost", 1337)

question = r.recvuntil(b">>>").decode()

print(question)
pays = question.split(" ")[-3].split("'")[-1]
print(reponses[pays])
r.sendline(reponses[pays].encode())
print(r.recv())
