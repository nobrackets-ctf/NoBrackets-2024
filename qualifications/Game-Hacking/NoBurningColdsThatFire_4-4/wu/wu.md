En analysant le code via [UndertaleModTool](https://github.com/UnderminersTeam/UndertaleModTool) (voir WU de la partie 3/4), on voit que le jeu fait des requêtes GET à "/cut" quand on coupe un arbre. Si on essait de faire les requêtes nous-même on voit que les requêtes ne fonctionne pas (retourne un 💀) sauf si on donne les coordonnées d'un arbre qui existe.

Pour flag il suffit juste de récupérer les coordonnées via "/tree" et on envoit 500 fois (ou plus car il y a d'autres joueurs qui font pareils 😈) les coordonnées avec "/cut" et on finit par récupérer le flag avec "/flag".
