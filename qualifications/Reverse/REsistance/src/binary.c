#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define INPUT_SIZE 100
#define CHUNK_SIZE 8
#define NUM_CHUNKS 4

int main(void) {
    // Définition des 4 sous-chaînes de 8 caractères
    const char *chunk4 = "he_W1N!}";
    const char *chunk1 = "NBCTF{S7";
    const char *chunk3 = "eP_for_7";
    const char *chunk2 = "R1NGs_GR";

    // Tableau des sous-chaînes
    const char *chunks[NUM_CHUNKS] = {chunk1, chunk2, chunk3, chunk4};

    // Ordre de vérification : 4, 2, 3, 1 (indices 3, 1, 2, 0)
    const int order[NUM_CHUNKS] = {3, 1, 2, 0};

    char input[INPUT_SIZE];

    // Lecture sécurisée de l'entrée utilisateur
    printf("Entrez le flag : ");
    if (!fgets(input, sizeof(input), stdin)) {
        fprintf(stderr, "Erreur de lecture.\n");
        return EXIT_FAILURE;
    }

    // Suppression du caractère de nouvelle ligne si présent
    input[strcspn(input, "\n")] = '\0';

    // Vérification de la longueur de l'entrée
    if (strlen(input) != CHUNK_SIZE * NUM_CHUNKS) {
        printf("Flag incorrect.\n");
        return EXIT_FAILURE;
    }

    // Vérification de chaque sous-chaîne dans l'ordre spécifié
    for (int i = 0; i < NUM_CHUNKS; i++) {
        int idx = order[i];
        if (strncmp(input + idx * CHUNK_SIZE, chunks[idx], CHUNK_SIZE) != 0) {
            printf("Flag incorrect.\n");
            return EXIT_FAILURE;
        }
    }

    // Si toutes les vérifications réussissent
    printf("Flag correct ! Bien joué.\n");
    return EXIT_SUCCESS;
}
