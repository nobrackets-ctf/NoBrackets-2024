# [Cryptanalyse] RSAdd

L'implémentation du RSA dans `chall.py` calcul le chiffré de la manière suivante :
$$c = m \times e \pmod N$$

au lieu de faire : 
$$c = m^e \pmod N$$

Le problème de factorisation est ainsi transformé en un problème d'inversion modulaire, dont la complexité est de O(log(n)), ce qui le rend résoluble en un temps raisonnable. Par exemple, la fonction `pow()` de Python permet de le résoudre. Voir `solve.py` pour une solution complète.