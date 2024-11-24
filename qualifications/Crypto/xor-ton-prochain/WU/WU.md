# [Cryptanalyse] XOR ton prochain 1/2 - Write up

## Description

Le challenge fournit un fichier `chall.py` effectuant des opérations utilisant le XOR sur le flag puis l'exporte dans `output.txt`.

## Solution

Nous pouvons observer deux choses :
- Nous connaissons le début du flag (et la fin): `NBCTF{` (et `}`)
- Chaque caractère est XORé avec le suivant, puis le dernier avec le premier

Par exemple, si l'output de `xor_ton_prochain(b"abcd")` sera `out = b"(a^b)(b^c)(c^d)(d^a))"`, sachant que nous connaissons `a`, on peut connaitre `b` en XORant `out[0]` avec `a`, on peut trouver `c` en XORant `out[1]` avec `b` et enfin `d`, de la même manière.

Il suffit de réappliquer cette méthode sur la variable `ct` du `output.txt` pour retrouver le flag ! Tu peux trouver un script complet dans `solve.py`.