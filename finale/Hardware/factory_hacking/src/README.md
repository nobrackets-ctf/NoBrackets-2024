Pour recréer ce chall:

- Créer une VM Windows 10 avec un utilisateur *user* administrateur local. Prendre au moins 2 CPU et 2 Go de RAM.
- Faire toutes les mises à jour WIndows et redémarrer.
- Installer TightVNC, FactoryIO et Python.
- Configurer TightVNC en autorisant les connexion en localhost en en mettant `readonly` en mot de passe pour un accès en lecture seule.
- Mettre le contenu de [Desktop](./Desktop) sur le Bureau de *user*.
- Ajouter le contenu de [Documents](./Documents) aux Documents de *user*.
- Ouvrir un explorateur de fichier, entrer l'adresse `shell:startup` et copier les fichiers du dossier [StartupFolder](./StartupFolder).
- Dans les paramètres Windows, mettre la résolution de l'écran à 800x600.
- Placer le dossier [config.cfg](./config.cfg) dans le dossier `%localappdata%\Real Games\Factory IO\`.

Les ports TCP 80, 502 et 5901 doivent être accessibles depuis l'extérieur et éventuellement le port 5900 pour déboguer.

Pour la VM de la finale, le mot de passe de *user* est `StrongPassword123` et il est possible de contrôler la machine via VNC en mettant `GCC>H2G2` en mot de passe.