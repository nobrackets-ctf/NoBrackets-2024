#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define BUFFER_SIZE 64

void setup() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
}

void win() {
    system("cat /flag.txt");
}

void vulnerable_function() {
    char buffer[BUFFER_SIZE];
    printf("Bienvenue au bureau des plaintes. Veuillez entrer votre message:\n");
    gets(buffer);
    printf("Merci pour votre message. Il sera examiné par nos services.\n");
}

int main() {
    setup();
    printf("Système de gestion des plaintes citoyennes\n");
    printf("==========================================\n\n");
    vulnerable_function();
    return 0;
}
