# Spellcast Overflow

## Tl;Dr
**Use-after-free with type confusion to call `win`.**

## Contexte

On interagit avec un service permettant de gérer des "personnages" disposant de différentes actions. L’objectif est d’exploiter une faille de type *Use after free* et une confusion de type afin de rediriger l’exécution vers une fonction cachée (`win`) qui affiche le flag.

Le service présente une interface avec :
- La création de personnages parmi plusieurs types (humain, sorcier, alchimiste, etc.).
- 4 slots accueillant des personnages
- une suppression (pas ouf) d'un slot
- des actions en fonction du type

---

## Fonctionnement global

Le programme permet de créer et manipuler des personnages avec des actions spécifiques. Cependant, la suppression d’un personnage libère la mémoire associée (dans la heap) sans effacer son type dans une liste séparée ni le pointeur vers cette zone (heap). 

**Cela entraîne une confusion possible entre types de personnages.**

Les slots ne sont jamais réelement libérés, cependant les zones mémoires le sont. Vu que la taille d'une structure `Sorcerer` ou `Alchemist` est la même que celle d'un `Human`, il est possible de les faire s'overlapper.

L'exploit se déroule en deux phases :
1. Une fuite de l'adresse de `spell` (en utilisant l'affichage de l'age d'un humain).
2. Le changement du pointeur `cast_spell` (qui pointe vers `spell`) vers `win` à l'aide de l'écriture de l'age d'un humain.

Voici un schéma de la heap après exploitation:

---------------------------------------------------------------------------------
| Slot 0: Human                           | Slot 1: Sorcerer                    |
|-----------------------------------------|--------------------------------------
| Name: "Harry"                           | Name: "Harry"                       |
| Age: 0x12345678                         | cast_spell: 0x12345678              |
---------------------------------------------------------------------------------
| Slot 2: Sorcerer                        | Slot 3: Human                       |
|-----------------------------------------|--------------------------------------
| Name: "Alice"                           | Name: "Alice"                       |
| Age: 0xdeadbeef (win func)              | cast_spell: 0xdeadbeef (win func)   |
---------------------------------------------------------------------------------


---

## Exploit

### Étapes :

1. **(slot 0)** Créer un humain :  
   On crée un humain qui sera utilisé plus tard pour obtenir une fuite d’adresse.

   ```python
   create_human(p, slot=1, name="John", age=30)
   ```

2. **(slot 0)** Supprimer l’humain :  
   Le slot est libéré, mais son type reste enregistré.

   ```python
   delete_character(p, slot=1)
   ```

3. **(slot 1)** Créer un sorcier :  
   Un sorcier est créé dans un autre slot mais overlap la zone mémoire de "John".

   ```python
   create_sorcerer(p, slot=2, name="Harry")
   ```

4. **(slot 1)** Lire l’age (fuite d’adresse) :  
   En accédant à l’action humaine "lire l’âge" dans le **slot 1**, on récupère une adresse mémoire. Cet âge correspond à l’adresse de la fonction `spell`.

   ```python
   leaked_address = read_human_age(p, slot=1)
   print(f"Leaked address: {hex(leaked_address)}")
   ```

5. **Calculer l’offset vers `win`** :  
   À partir du binaire fourni, on calcule l’offset entre `spell` et `win` :

   ```python
   offset = win_address - spell_address
   ```

6. **(slot 2)** Créer un nouveau sorcier :  
   On prépare un nouveau sorcier dans un autre slot pour le réutiliser plus tard.

   ```python
   create_sorcerer(p, slot=3, name="Hermione")
   ```

7. **(slot 2)** Supprimer le personnage :  
   Libération du slot pour permettre une future réutilisation.

   ```python
   delete_character(p, slot=3)
   ```

8. **(slot 3)** Créer un humain avec un âge "spécial" :  
   L’âge de ce nouvel humain est l’adresse calculée de la fonction `win`.

   ```python
   create_human(p, slot=4, name="Alice", age=win_address)
   ```

9. **(slot 2)** Appeler l’action "cast_spell" :  
    On a réécrit le pointeur `cast_spell` par `win`.
   ```python
   perform_sorcerer_action(p, slot=3)
   ```

---

### Résultat

L’appel détourné vers `win` permet d’afficher le flag !

---

## Flag

> **NBCTF{If_Pwn_Is_Magic_Heap_Is_SORCERY!}**