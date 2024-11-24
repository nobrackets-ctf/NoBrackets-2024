# Implan 1/3

Rappel du challenge : 

>  `noclick`, un de nos spécialiste drone n'a plus donné signe de vie depuis plusieurs jours. Il travaillait activement sur un "exploit" (programme destiné à exploiter une faille) pour neutraliser la reconnaissance faciale des drones du gouvernement. On pense qu'il aurait été arrêté ! Un informateur s'est rendu à son domicile qui était vide. Sur nos ordres, il a lancé un programme qui a collecté toutes les traces d'activité sur le poste de `noclick`. Ces traces vont vous permettre de reconstituer ce qu'il s'est passé sur sa machine. Il nous faut tout d'abord identifier le programme malveillant. L'informateur pense que le nom du virus qui a compromis l'ordinateur de `noclick` se trouve dans le fichier joint. Il s'agit d'une extraction de l'`Amcache` (plus d'information à ce propos sur le [wiki](https://wiki.nobrackets.fr/docs/intro), partie Forensic > Windows).
  
L'objectif est de trouver le **nom** du programme malveillant ainsi que son **hash** `SHA1`. Le format du flag est le suivant : NBCTF{<nom_du_programme>-<hash SHA1>}.

## Amcache

Pour reprendre les mots du [wiki](https://wiki.nobrackets.fr/docs/intro) (eux-mêmes tirés du [poster du SANS - Windows Forensic Analysis](https://cyber-ssct.com/SANS%20Digital%20Forensic%20Poster.pdf)), l'Amcache *"référence les applications installées, les programmes exécutés (ou présents sur la machine), les pilotes chargés, etc. Ce qui distingue cet artefact, c'est qu'il référence également le hash des applications et des pilotes."*. Nativement, l'Amcache est une base de données au format **binaire** (située ici `C:\Windows\AppCompat\Programs\Amcache.hve`). C'est-à-dire qu'elle n'est pas lisible tel quel (essayez de l'ouvrir avec le bloc note et vous comprendrez). Ce qu'on a ici est une **traduction de l'Amcache au format textuel**.

Dans la "vraie vie", on travaille avec des outils qui font cette traduction automatiquement. Pour information, j'ai utilisé [KAPE](https://www.kroll.com/en/services/cyber-risk/incident-response-litigation-support/kroll-artifact-parser-extractor-kape) qui est un des outils de référence en la matière. Si vous voulez apprendre à l'utiliser, [TryHackMe propose un cours gratuit pour apprendre à utiliser KAPE](https://tryhackme.com/r/room/kape), je vous le recommande lui et tous les autres cours de la plateforme.

## Analyse

Armé de ces nouvelles connaissances, comment identifier un programme malveillant ? Commençons par comprendre les données que l'Amcache contient. Chaque colonne a une signification bien précise mais je ne vais en détailler qu'une partie : 

- `FileKeyLastWriteTimestamp` : horodatage de l'écriture de la ligne (on peut raisonnablement l'interprêter comme la date de **dernière** exécution du programme/driver [en vrai c'est un peu plus compliqué mais on ne rentrera pas dans le détail ici]).

- `SHA1` : le **hash** (au format SHA1) du programme/driver. Si vous ne savez pas ce qu'est un hash, référez-vous au [wiki](https://wiki.nobrackets.fr/docs/intro). Pour faire simple, il s'agit d'une chaîne de caractère qui nous permet d'identifier de façon unique le programme/driver.

- `FullPath` : où est situé le programme/driver sur la machine.

On peut encore obtenir bien d'autres informations comme la taille du programme/driver, sa version, sa langue... mais nous n'en aurons pas besoin ici.

On sait que `noclick` travaillait sur un programme relatif à des **drones**. On peut donc commencer par là et chercher les occurences de ce mot dans le fichier CSV, que vous pouvez ouvrir avec un bloc note, Excel, LibreOffice Calc ou encore Google Sheet. On aurait pu aussi se demander si un programme situé dans le dossier téléchargement apparaissait.

On tombe sur une seule occurence dont voici les informations :

- `FileKeyLastWriteTimestamp` : `2024-08-19 18:05:56.8477053`

- `SHA1` : `89542eac72f11afb0711535d0404c79aad9c3728`

- `FullPath` : `c:\users\noclick\downloads\...important_nouvel_exploit_drone_a_tester.exe`

On s'apperçoit alors que le fichier exécutable se trouve dans le dossier `downloads` ce qui corrobore les dires de l'informateur. Les plus expérimentés d'entre-vous seraient tentés de rechercher le hash sur [VirusTotal](https://www.virustotal.com/) qui est une base de données spécialement conçue pour référencer les malwares. Malheureusement, étant donné que j'ai développé moi-même le malware et que je ne l'ai pas mis sur VirusTotal, il n'apparaît pas. Néanmoins, en fouillant un peu plus le fichier CSV, on ne trouve pas d'autres programmes exécutés depuis le dossier de téléchargement et chaque autre programme semble être cohérent avec un Windows. 

## Références

- [Wiki du NoBracketsCTF](https://wiki.nobrackets.fr/docs/intro)

- [Cours TryHackMe gratuit sur KAPE](https://www.kroll.com/en/services/cyber-risk/incident-response-litigation-support/kroll-artifact-parser-extractor-kape)

- [SANS - Windows Forensic Analysis Poster](https://cyber-ssct.com/SANS%20Digital%20Forensic%20Poster.pdf)

- [Analyse de l'AmCache - ANSSI](https://cyber.gouv.fr/publications/analyse-de-lamcache)