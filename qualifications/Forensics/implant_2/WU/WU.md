# Implant 2/3

Rappel du challenge : 

> L'informateur vous a envoyé les `logs` de l'ordinateur de `noclick`. Ce sont des fichiers qui répertorient les actions qui se sont déroulées sur le système (plus d'informations sur le [wiki](https://wiki.nobrackets.fr/docs/intro)). Quand le virus a-t-il été lancé ? Quel est le **processus père** (*parent process*) qui a lancé le malware ? Le flag est au format NBCTF{<date et heure du lancement du virus>-<nom processus père>}.

## Logs Windows

De la même manière que pour la partie 1, les logs Windows ont été traduits dans un format textuel. On a donc un fichier CSV que vous pouvez ouvrir avec votre bloc note, LibreOffice Calc, Excel ou encore Google Sheet. Je déconseille le bloc note car il n'est pas adapté pour les CSV. L'analyse sera bien plus simple si vous prenez un tableur.

### Quelques informations sur les logs

On peut voir les logs comme un journal de bord du système. Windows garde trace des différentes actions telles que la connexion à un réseau, les programmes lancés, leurs actions sur le système, l'ouverture de fichier etc... Windows fournit également un outil graphique qui permet de les consulter, les trier, effectuer des recherches... 

> On peut même ajouter des sources de logs à Windows. Dans ce challenge, j'ai ajouté [Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon) qui permet d'avoir des logs plus précis. En particulier, il permet de voir davantage d'actions que réalisent un programme. Il **n'est pas** installé de base sous Windows mais il s'agit d'un *must have* lorsqu'on souhaite monitorer des machines. Pour les intéressé(e)s, je vous invite à vous renseigner sur cet outil.

Les logs sont très riches, il n'est pas facile de s'y reprérer pour un débutant. Néanmoins, les noms des colonnes peuvent aider à comprendre. Ici, nous allons nous intéresser aux colonnes suivantes : 

- `TimeCreated` : horodatage du log en question.

- `EventID` : il s'agit d'un identifiant qui permet... d'identifier un événement particulier. Par exemple, `4624` signifie *an account was successfully loged on*. C'est une donnée très utile mais qui ne sera pas utilisée dans ce challenge. *Nota* : le champ `MapDescription` est la description associée à l'eventID.

- `UserName` : quel *utilisateur* est à l'origine de l'action (du log). On peut retrouver l'utilisateur "humain" qui utilisait l'ordinateur, auquel cas il sera noté comme suit : `WINDOWS10\<username>` (dans notre cas l'*username* sera `noclick`).

> On peut également voir des utilisateurs comme `AUTHORITE NT\Système`, `AUTHORITE NT\SERVICE RESEAU`. Dans ce cas, cela signifie que ce sont des actions que le système effectue automatiquement. Une action effectuée par `AUTHORITE NT\Système` ne signifie **pas forcément** qu'il s'agit d'une activité malveillante. Dans ce challenge, on n'ira pas dans le détail.

- `PayloadData4` : contient parfois des informations, en l'occurrence le *parent process* (processus père) qui a lancé le processus dont il est question dans le log.

- `ExecutableInfo` : le fichier `exe` à l'origine du log.

- `Payload` : contient la majorité des informations croustillantes qu'on détaillera dans la partie "*Bonus : résolvez la partie 3 grâce au payload*". **N'est pas obligatoire pour ce challenge.**

### Processus père et fils

Un processus est un programme lancé. Quand vous double-cliquez sur un programme il est chargé en mémoire (RAM) et Windows créé un processus. Souvent, un programme est lancé par un autre programme. Si `programme1.exe` lance `programme2.exe`, alors `programme1.exe` est le processus **père** de `programme2.exe`. Inversement, `programme2.exe` est le processus **fils** de `programme1.exe`.

On serait tenté de dire que, si je lance un programme, alors il n'a pas de processus père. En réalité, Windows a un fonctionnement bien précis et chaque programme possède un processus père (pour faire simple). Si vous voulez comprendre en détail le fonctionnement de Windows sur cette partie, je vous invite à consulter ce poster du SANS : [Find Evil - Know Normal - SANS](https://share.ialab.dsu.edu/cae_workshops/2019/Incident%20Response/Supplementary%20Material/SANS_Poster_2018_Hunt_Evil_FINAL.pdf).

## Investiguons !

Armé de toutes ces connaissances, nous pouvons commencer l'investigation. A ce stade, nous savons que le programme malveillant s'appelle `important_nouvel_exploit_drone_a_tester.exe`. Une recherche de ce programme dans les logs nous sort ces informations : 

- `TimeCreated` : 2024-09-08 15:20:39.3203769

- `EventID` associé à `MapDescription` pour rendre le tout compréhensible : 1 (*Process creation*).

- `UserName` : `WINDOWS10\noclick` cela indique que c'est l'utilisateur de la machine qui est à l'origine de cette action.

- `ParrentProcess` : `C:\Windows\System32\cmd.exe` le processus qui a lancé `important_nouvel_exploit_drone_a_tester.exe`.

- `ExecutableInfo` : `important_nouvel_exploit_drone_a_tester.exe` le programme à l'origine du log.

(On s'intéressera au champ `Payload` dans la partie suivante, en bonus)

D'après ces informations, on peut en tirer la conclusion suivante : 

> Le **2024-09-08** à **15:20:39**, l'utilisateur **noclick** a exécuté le programme `important_nouvel_exploit_drone_a_tester.exe` (`EventID` 1 (*Process creation*)) **depuis un invite de commande** (`ParrentProcess` `cmd.exe`).

Ici, il s'agit uniquement de la première occurence, donc le log **le plus vieux**. Pas besoin de s'intéresser aux autres pour ce challenge car ce sont les actions qu'effectue le programme ensuite. Ce qui nous intéresse ici est de savoir quand le malware a été exécuté pour la première fois et par quel programme.

## Bonus : résolvez la partie 3 grâce au payload

Cette partie est pour les participant(e)s déjà un peu expérimenté(e)s. Si vous voulez comprendre plus en détail, vous êtes au bon endroit. Les plus curieux(ses) auront peut-être remarqué des actions étranges... En particulier dans la colonne `Payload`. Cette dernière contient beaucoup d'informations au format `JSON`. C'est assez difficile à lire mais on peut utiliser un [JSON formatter en ligne](https://jsonformatter.org/) qui va effectuer des sauts de lignes ainsi que des indentations pour rendre la lecture plus simple (j'ai enlevé ce qui ne nous intéresse pas) : 

```json
{
  "EventData": {
    "Data": [
      {
        "@Name": "UtcTime",
        "#text": "2024-09-08 15:20:39.216"
      },
      {
        "@Name": "Image",
        "#text": "C:\\Users\\noclick\\Downloads\\IMPORTANT_nouvel_exploit_drone_a_tester\\IMPORTANT_nouvel_exploit_drone_a_tester.exe"
      },
      {
        "@Name": "CommandLine",
        "#text": "IMPORTANT_nouvel_exploit_drone_a_tester.exe"
      },
      {
        "@Name": "CurrentDirectory",
        "#text": "C:\\Users\\noclick\\Downloads\\IMPORTANT_nouvel_exploit_drone_a_tester\\"
      },
      {
        "@Name": "User",
        "#text": "WINDOWS10\\noclick"
      },
      {
        "@Name": "ParentImage",
        "#text": "C:\\Windows\\System32\\cmd.exe"
      },
      {
        "@Name": "ParentCommandLine",
        "#text": "\"C:\\Windows\\system32\\cmd.exe\" "
      },
      {
        "@Name": "ParentUser",
        "#text": "WINDOWS10\\noclick"
      }
    ]
  }
}
```

On se rend compte ici que cette colonne a elle toute seule nous permet d'avoir toutes les informations nécessaires à la résolution du challenge. Et si on regarde d'autres occurences de notre malware, on tombe sur un *payload* intriguant :

```json
{
  "EventData": {
    "Data": [
      {
        "@Name": "UtcTime",
        "#text": "2024-09-08 15:20:47.704"
      },
      {
        "@Name": "OriginalFileName",
        "#text": "Cmd.Exe"
      },
      {
        "@Name": "CommandLine",
        "#text": "C:\\Windows\\system32\\cmd.exe /c \"dir\""
      },
      {
        "@Name": "CurrentDirectory",
        "#text": "C:\\Users\\noclick\\Downloads\\IMPORTANT_nouvel_exploit_drone_a_tester\\"
      },
      {
        "@Name": "User",
        "#text": "WINDOWS10\\noclick"
      },
      {
        "@Name": "ParentImage",
        "#text": "C:\\Users\\noclick\\Downloads\\IMPORTANT_nouvel_exploit_drone_a_tester\\IMPORTANT_nouvel_exploit_drone_a_tester.exe"
      },
      {
        "@Name": "ParentCommandLine",
        "#text": "IMPORTANT_nouvel_exploit_drone_a_tester.exe"
      }
    ]
  }
}
```

Ne trouvez-vous pas le champ `CommandLine` étrange ? Ce que nous dit ce log c'est que `cmd.exe` a un processus père qui est `IMPORTANT_nouvel_exploit_drone_a_tester.exe`. De plus, `cmd.exe` exécute une commande qui est `dir`, qui sert à lister les éléments dans le dossier courant. Pour le dire autrement, le soit-disant programme qui servirait à exploiter une vulnérabilité dans les drones exécute des commandes afin de savoir ce qui se trouve dans un dossier. Plus étrange encore, lorsqu'on continue de chercher un peu, on tombe sur les commandes suivantes : 

- `cd C:\` (`cd` sert à se déplacer dans les dossiers)

- `type "C:\Users\noclick\Desktop\message du collectif\drone exploit.py"` (`type` sert aficher le contenu d'un fichier)

Moi je trouve que ça ressemble fortement à un programme qui permet à une personne de se balader sur l'ordinateur de `noclick` et de voir le contenu des fichiers... bref, un **implant** !

## Références

- [Cours TryHackMe (malheureusement payant) sur les logs Windows](https://tryhackme.com/room/windowseventlogs)

- [Wiki du NoBracketsCTF](https://wiki.nobrackets.fr/docs/intro)

- [Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)

- [Find Evil - Know Normal - SANS](https://share.ialab.dsu.edu/cae_workshops/2019/Incident%20Response/Supplementary%20Material/SANS_Poster_2018_Hunt_Evil_FINAL.pdf)