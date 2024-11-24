# SuperCat

## Tl;Dr
*"Race condition" sur le fichier pour le transformer en symlink.**

## Contexte

On a un service qui permet de sélectionner un fichier puis d'afficher son contenu dans un second temps.
Ce service a un bit de suid d'activé, ce qui permet donc de se faire passer pour `user-cracked`.

Le service est plutôt bien fait, car :
- codé en rust (donc à priori, pas de problème de mémoire)
- pas de bloc `unsafe` (donc normalement vraiment pas de problème de mémoire)
- il vérifie si le fichier n'est pas un symlink ou si son nom est flag.txt

## Fonctionnement global

En analysant le code (car on ne va pas reverse, du rust strippé c'est pas cool), on comprend le fonctionnement suivant :
1. Selection d'un fichier en variable globale
    - Vérification si c'est un symlink & si le path ne finit pas par flag.txt
2. Affichage des informations et du contenu du fichier
    - Aucunes vérifications

## Exploit
L'exploit est donc simple :

1. Ouvrir deux sessions ssh (sess 1 et sess 2)
2. Créer un fichier `abc.txt` (ou autre) : `touch abc.txt`
3. (sess 1) Lancer le programme : `./super_cat`
4. (sess 1) Selectionner le fichier `abc.txt`
5. (sess 2) Supprimer le fichier `abc.txt` : `rm abc.txt`
6. (sess 2) Créer un lien symbolique entre `abc.txt` et `flag.txt` : `ln -s flag.txt abc.txt`
7. (sess 1) Afficher le contenu du fichier `abc.txt`

Le flag apparait car le fichier abc.txt pointe vers flag.txt et nous avons les droits pour le lire (grace au suid).

> NBCTF{Race_1n_Rust_a1nt_rusty_4t_4ll!}
