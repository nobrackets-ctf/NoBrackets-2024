# [Cryptanalyse] Time to flag (1/2) - Write up

Le PRNG est initialisé avec un vecteur secret de dimension DIM=8, que nous allons noté $s$, avec :
```math
s = \begin{pmatrix}
s_0\\
s_1\\
s_2\\
\vdots\\
s_7
\end{pmatrix} \in \mathbb{Z}^8
```
Nous remarquons rapidement que l'objectif du challenge est de retrouver ce vecteur afin de pouvoir déchiffrer le FLAG. En effet, la clef AES est dérivée du vecteur $s$ (cf. extrait ci-dessous).
```py
def get_encrypted_flag(s):
	shake = SHAKE256.new()
	shake.update(str(s).encode('utf-8'))

	key = shake.read(AES.block_size)
	iv  = b"."*AES.block_size

	cipher = AES.new(key, AES.MODE_CBC, iv=iv)
	return cipher.encrypt(pad(FLAG, AES.block_size)).hex()
```

À chaque fois que nous demandons un nombre aléatoire, un tableau `u` de taille `DIM` est créé grâce a la fonction `expand_time`. Nous notons également que cette fonction est *déterministe* (i.e. pour une entrée donné la sortie sera toujours la même). Ici, cette entrée est le temps actuel. Si nous le connaissons, alors, nous pouvons recréer les vecteurs `u` ! Notons ces vecteurs `t_i`, avec :
```math
t_i = \begin{pmatrix}
a_i\\
b_i\\
c_i\\
\vdots\\
h_i
\end{pmatrix} \in \mathbb{Z}^8
```

Le nombre généré a un instant $i$, notons le $x_i$, est le résultat du produit scalaire entre la seed secrète et le vecteur $t_i$, i.e. 
```math
x_i = a_i s_0 + b_i s_1 + \ldots + h_i s_7
```
Si nous arrivons a obtenir DIM (i.e. 8) nombres différents et générés par le `PRNG` (i.e. générés à 1 seconde d'intervalle), alors nous obtenons le système linéaire suivant :
```math
 \quad (*) \quad \begin{cases}
x_{i+0} = a_{i+0} s_0 + b_{i+0} s_1 + \ldots + h_{i+0} s_7 \\
x_{i+1} = a_{i+1} s_0 + b_{i+1} s_1 + \ldots + h_{i+1} s_7 \\
x_{i+2} = a_{i+2} s_0 + b_{i+2} s_1 + \ldots + h_{i+2} s_7 \\
\vdots \\
x_{i+7} = a_{i+7} s_0 + b_{i+7} s_1 + \ldots + h_{i+7} s_7
\end{cases}
```
> ⚠️ **Attention**: Il est essentiel de les générer a 1 seconde d'intervalle, sinon nous n'aurons pas `DIM` equations différentes, et il existera une infinité de solutions.

C'est maintenant trivial de retrouver le vecteur $s$ (i.e. la seed). En effet, il suffit de résoudre le système linéaire $(*)$ ; l'implémentation de cette solution est disponible en python dans le fichier `solve.py`.
