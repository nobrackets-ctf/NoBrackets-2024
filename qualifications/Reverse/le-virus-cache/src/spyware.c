#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void hiddenFunction(void) {
    char encStr[] = { 0x7D, 0x71, 0x70, 0x67, 0x75, 0x48, 0x40, 0x63, 0x4A, 0x44, 
                      0x73, 0x61, 0x76, 0x6C, 0x02, 0x5D, 0x06, 0x47, 0x72, 0x02, 
                      0x02, 0x56, 0x57, 0x4E, '\0' };

    for (int i = 0; i < strlen(encStr); i++) {
        encStr[i] ^= 0x23; 
        encStr[i] ^= 0x10;  
    }
    printf("%s\n", encStr);
    exit(0);
}

int main(void) {
    printf("You will own nothing and you will be happy...\n");
    return 0;
}
