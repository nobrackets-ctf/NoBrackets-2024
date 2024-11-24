# [Cryptanalyse] Why so sloooww?? 1/2 - Write up

## Contenu du challenge

Le challenge met à disposition deux fichiers :

1. `chall.py`
2. `output.txt`

Le fichier `chall.py` contient plusieurs trucs :

- `safe_encrypt()`/`safe_decrypt()`: ces deux fonctions permettent de chiffrer/déchiffrer le FLAG a partir d'un nombre `u` (on dérive une clé AES depuis ce nombre, puis on chiffre). En gros, rien d'intéressant a ce niveau là ;
- Cette partie de code :
```python
# Définitions de mes paramètres magiques
GROS_INDEX = (1 << 123) + (1 << 78) + (1 << 56)
MODULO = 1229894983634972312797718042580418393679633615251177958057988339965550336867464103010048241

A = 105609976152967015792543303055881219028953329511948723738696995837071203045563 # nombre aléatoire
B = 101282411473189588351048224304714715012241822016646462417243766752316342481229 # nombre aléatoire

# Calcul du secret
u = 17
for _ in range(GROS_INDEX):
	u *= A
	u += B
	u %= MODULO
```
On voit que le nombre va être utilisé comme input pour la fonction `safe_encrypt()`, c'est donc ici que ça devient intéressant! En effet, on peut reconnaitre la définition sous forme récurrente d'une suite [arithmetico-géométrique](https://fr.wikipedia.org/wiki/Suite_arithmético-géométrique). Mais malheureusement, la variable `GROS_INDEX` est trop grande pour que la boucle puisse se terminer et qu'on puisse obtenir le flag.

## Résolution du challenge

Si tu te rappelles de tes cours de première sur les suites, tu sais qu'on peut définir une suite sous deux formes différentes :

1. Sous une relation de récurrence (i.e. $u_{n+1}$ en fonction de $u_{n}$, pour une récurrence simple) ;
2. Sous une forme explicite (i.e. $u_n$ en fonction de $n$).

L'avantage de (2.) par rapport à (1.) c'est que nous n'aurons pas besoin d'itérer `GROS_INDEX` fois pour trouver le terme $u_{GROS_INDEX}$. Tu peux retrouver dans le fichier `solve.py` une implémentation de cette forme (2.) afin de retrouver la flag ! A noter que la petite différence avec une suite arithmetico-géométrique classique était que tous les calculs étaient faits mod $p$, il fallait donc utiliser l'inverse modulaire au lieu de la division et bien penser à faire ses calcul mod $p$ (`% p` en python).

J'espère que tu as aimé ce challenge et n'hésites pas a poser des questions si tu as besoin d'aide.