section .text
global _start

_start:
    ; Allocate 200 bytes on the stack for the buffer
    sub rsp, 200

    ; Ask for the law to execute
    mov rax, 1              ; syscall number for write
    mov rdi, 1              ; file descriptor 1 is stdout
    mov rsi, prompt         ; pointer to the prompt string
    mov rdx, prompt_len     ; length of the prompt
    syscall                 ; make syscall

    ; Read the law (up to 200 bytes)
    mov rax, 0              ; syscall number for read
    mov rdi, 0              ; file descriptor 0 is stdin
    mov rsi, rsp            ; pointer to the buffer (now on stack)
    mov rdx, 200            ; maximum number of bytes to read
    syscall                 ; make syscall

    ; Jump to the buffer to execute the law
    jmp rsp

section .data
    prompt db "Enter the law to execute (in raw bytes format -- max 200 bytes): ", 0
    prompt_len equ $ - prompt
