# [Cryptanalyse] Why so sloooww?? 2/2 - Write up

## Contenu du challenge

L'objectif du challenge est le même que celui de la première partie (i.e. il faut trouver un secret afin de le dériver en clef AES pour déchiffrer le flag). De même que dans la première partie, il faut simplifier l'expression d'une boucle afin de la rendre calculable en un temps raisonnable.

## Résolution du challenge

Nous pouvons réécrire la boucle `for` sous forme d'un produit (avec `n = GROS_INDEX`) :

$$\text{u =}\prod_{k=0}^{n} 1337^{k^2 + k}$$

En utilisant les opérations sur les puissances, nous pouvons réécrire cette somme :

$$\text{u =}1337^{\sum_{k=0}^n k^2 + \sum_{k=0}^n k}$$

Posons $s_1 = \sum_{k=0}^n k^2$ et $s_2 = \sum_{k=0}^n k$, nous pouvons alors calculer en un temps raisonnable:

$$t = s_1 + s_2 \pmod{\text{MODULO}-1}$$

Il ne nous reste plus qu'a calculer $s$, en effet : $s = 1337^{t} \pmod{\text{MODULO}}$, cette opération aussi se fait en un temps raisonnable.

Tu peux retrouver l'implémentation de la solution dans le fichier `solve.py`