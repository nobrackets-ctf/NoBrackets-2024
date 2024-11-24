Une fonction est déclarée mais n'est kamais appelée. L'objectif du défi est de modifier l'adresse du pointeur EIP pour exécuter la fonction cachée

```bash
$info functions
$b main
$run
$disas hiddenFunction
$set $eip=0x565561ad
$c
```
