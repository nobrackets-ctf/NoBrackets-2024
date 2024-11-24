# [Cryptanalyse] Time to flag (ou pas ?) (2/2) - Write up

Comme pour la partie 1, le PRNG est initialisé avec une seed secrète de dimension DIM=8, nous allons la noter $s$, tel que :
```math
s = \begin{pmatrix}
s_0\\
s_1\\
s_2\\
\vdots\\
s_7
\end{pmatrix} \in \mathbb{Z}^8
```
le but de cette seconde partie est également de retrouver ce vecteur $s$.

Nous remarquons que les seules différences avec le premier challenge, sont :
- Nous pouvons obtenir un seul nombre aléatoire ;
- Le vecteur $s$ est composé de valeur bien plus petite que les vecteurs $t_i$ (24 bits contre 256 bits).

Contrairement au premier challenge, nous ne pouvons donc pas créer de système linéaire avec 8 équations. En effet, le PRNG ne nous fournit qu'un seul nombre ! Le challenge parait alors impossible, MAIS, il existe une règle en crypto, lorsqu'un problème d'algèbre linéaire parait impossible et qu'il y a des petites valeurs quelque part (ici les entrées de $s$), la solution, c'est .... `LLL` !!

Si tu ne connais pas les lattices ni l'algo de reduction de base `LLL` ; ce qui est trèèèès probable sachant que tu n'es qu'au lycée ... je t'invite a aller voir les ressources suivantes :
- https://theblupper.github.io/blog/posts/lattices/
- https://link.springer.com/book/10.1007/978-1-4939-1711-2
- https://www.youtube.com/watch?v=QDdOoYdb748

Nous pouvons écrire le problème de ce challenge sous forme d'équation, 
```math
x = s_0 * a + s_1 * b + \cdots + s_7 * h 
```
avec $x$ le nombre aléatoire et $a$, $b$, ..., $h$ les composantes du vecteur temps. Nous pouvons la réécrire sous la forme :
```math
s_0 *
\begin{pmatrix}
1\\0\\0\\\vdots\\0\\a
\end{pmatrix}
+ s_1*
\begin{pmatrix}
0\\1\\0\\\vdots\\0 \\b
\end{pmatrix}
+ s_2*
\begin{pmatrix}
0\\0\\1\\\vdots\\0 \\c
\end{pmatrix}
+ \cdots + s_7 *
\begin{pmatrix}
0\\0\\0\\\vdots\\1\\h
\end{pmatrix}
=
\begin{pmatrix}
s_1\\s_2\\s_3\\\vdots\\s_4\\x
\end{pmatrix}
```
Mais encore :
```math
s_0 *
\begin{pmatrix}
1\\0\\0\\\vdots\\0\\a
\end{pmatrix}
+ s_1*
\begin{pmatrix}
0\\1\\0\\\vdots\\0 \\b
\end{pmatrix}
+ s_2*
\begin{pmatrix}
0\\0\\1\\\vdots\\0 \\c
\end{pmatrix}
+ \cdots + s_7 *
\begin{pmatrix}
0\\0\\0\\\vdots\\1\\h
\end{pmatrix}
+ (-1) *
\begin{pmatrix}
0\\0\\0\\\vdots\\0\\x
\end{pmatrix}
=
\begin{pmatrix}
s_1\\s_2\\s_3\\\vdots\\s_4\\0
\end{pmatrix}
```
nous remarquons que le vecteur a droite du signe $=$ est très petits (i.e. chacun de ces coefficients fait $\approx$ 32 bits), nous pouvons donc construire la lattice avec tous les vecteurs colonnes de la partie gauche de l'égalité et appliquer l'algorithme de reduction de base, si le vecteur $s$ est suffisément petit, alors il apparaitra dans la base réduite.

Tu peux retrouver une implémentation de cette solution dans le `solve.py`. Il y a beaucoup de nouvelles notions dans ce challenge pour un lycéen, donc si tu n'as pas tout compris, n'hésites pas à venir nous parler en DM :)
