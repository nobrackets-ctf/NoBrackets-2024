## Intended

Vous pouvez utiliser [Cheat Engine](https://www.cheatengine.org) pour trouver les coordonnées x,y et pouvoir les modifiers par celles souhaités.

Bien sûr ce n'est pas si simple. GMS a des variables qui bouge en même temps que celles du joueur: la position de l'image du joueur ; les 4 coins de la boite de collision du joueur ; les positions de la camera et là où elle regarde (vers le joueur)

Certains auront peut-être modifié la """vie""" du joueur contre le froid. Relié à l'objet de camera. Permettant de marcher sans problème dans le froid. Ajouter avec un speedhack pour rejoindre les coordonnées rapidement.

## Unintended

En traquant où se trouve l'affichage du flag et d'où il vient grâce à [UndertaleModTool](https://github.com/UnderminersTeam/UndertaleModTool) (plus de détails dans la partie 3/4 sur l'outil), on trouve que ``oController.Draw`` affiche ``surfaceText()`` à des coordonnées proches. Le code de ``surfaceText()`` utilise une variable nommée ``variable_name``, en regardant sa valeur on trouve le flag.