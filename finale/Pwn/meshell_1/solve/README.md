La fonction `check` vérifie que l'utilisateur n'a pas entré les caractères
suivants : `$`, `,` ou ` `.

Les espaces sont ainsi interdits, les virgules ou les dollars égalemement.
Il n'est donc pas possible d'afficher le flag avec un simple `cat /app/flag.txt`.

On ne peut pas non plus tenter de contourner la restriction sur les espaces
grâce aux techniques suivantes : `{cat,/app/flag.txt}` ou
`cat$IFS/app/flag.txt`.

Plusieurs de solutions permettent tout de même d'afficher le flag, parmi elles :
- `sh` puis `cat /app/flag.txt`
- `\`</app/flag.txt\``
