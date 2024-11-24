Un outil super utile pour analyser le code d'un jeu fait sur GameMaker, c'est [UndertaleModTool](https://github.com/UnderminersTeam/UndertaleModTool) !

> [!NOTE]
> Pour trouver ce tool il suffit juste de chercher un décompilateur pour GMS.
>
> Comment savoir que c'est un jeu fait avec GMS vous me direz ? Il suffit de regarder les *strings* ou de regarder à quoi correspond l'*icone du .exe* 

Grâce à UndertaleModTool nous avons un jolie GUI et un accès complet aux données du jeux: sprites (images) ; code ; sons ; cartes (rooms) ; ...

Le tout sans aucunes restrictions et sans obfuscation ! (Pour les curieux, c'est parce que le jeu n'a pas été compilé en C++ avec le Yoyo C++ Compiler mais est en bytecode avec son executable pour le jouer)

Vous pouvez analyser le code et solve facilement tous les challs, 1/4 ; 2/4 si vous êtes curieux ; 3/4 bien sûr ; 4/4 facilement car vous savez comment obtenir le flag et comment se jouer de l'API

## Et le flag alors

Il suffit de regarder dans les images, parmis elles se trouvent une non utilisé avec un jolie flag écrit dessus.