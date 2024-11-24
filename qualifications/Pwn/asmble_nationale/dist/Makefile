all: asmble_nationale

asmble_nationale: asmble_nationale.asm
	nasm -f elf64 asmble_nationale.asm -o asmble_nationale.o
	ld -m elf_x86_64 -z execstack -o asmble_nationale asmble_nationale.o
	rm -f asmble_nationale.o

clean:
	rm -f asmble_nationale
