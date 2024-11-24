L'objectif de ce défi est de mmodifier le contenu d'un registre lorsque le programme est en exécution.
Pour ce faire il faut voir, en utilisant GDB par exemple, que le contenu du registre EAX est comparé à une valeur. Les deux valeurs ne sont pas égales, ce qui affiche le message d'erreur.

Dans GDB:
```bash
$b main
$run
$si
$i r
$set $eax=0x6D
$c 
```
