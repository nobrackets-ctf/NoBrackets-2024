La fonction `check` interdit les lettres minuscules et majuscules.

Les solutions présentées dans la première version du challenge ne marchent
donc pas.

Une subtilité de bash permet d'encoder des chaînes de caractères sans faire
appel à des commandes externes avec la syntaxe suivante :
`echo $'\x41\x42\x43'` ce qui affiche `ABC`

En revanche, les `x` sont interdits. Il est possible d'encoder notre commande
en octal pour n'utiliser que des chiffres. Voici donc une solution pour ce
challenge :
- `$'\163\150'`

Une autre solution, en exploitant la manipulation des chaînes de caractères permise par bash :
- `${0: -2}` (`$0` correspond au script courant, soit `/app/meshell.sh` ;  le
`: -2` récupère les 2 derniers caractères, soit `sh`)
