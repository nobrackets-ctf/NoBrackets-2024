#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    int eax = 0;

    if (eax == 109) {
        char encStr[] = { 
            0x1B, 0x17, 0x16, 0x01, 0x13, 0x2E, 0x1E, 0x34, 0x37, 0x65, 
            0x65, 0x38, 0x0A, 0x64, 0x06, 0x0A, 0x64, 0x38, 0x38, 0x3C, 
            0x3B, 0x66, 0x3B, 0x01, 0x28, '\0'
        };

        for (int i = 0; i < strlen(encStr); i++) {
            encStr[i] ^= 0x55;
        }
        printf("Good job! You win !\n");
        printf("%s\n", encStr);
    } else {
        printf("Fatal error. Incorrect ignition code\n");
    }

    return 0;
}
