---
title: 'Inattention fatale'
disqus: hackmd
authors: '6e 61 74 68'
---

# Inattention fatale
NBCTF 2024 - OSINT Challenge - Auteur **6e 61 74 68**

En réutilisant les informations que l'on avait déjà. On va essayer de retrouver la publication de notre suspect. 

Pour cela nous savons d'où la photo a été prise. 
Il existe peu d'endroit où l'on poste régulièrement des photos. Nous commençons alors avec le plus connu: Instagram

Sur téléphone, nous pouvons aller rechercher les photos postées proche d'un même lieu. Nous pouvions également utilisé InstaHunt pour retrouver le lieu et faire une recherche grâce à des requêtes API.

Nous trouvons que le lieu le plus proche est "Ponte Pietra". 
Dessus on retrouve l'image que nous avions avec la description indiquée dans l'énoncée de la Fuite en touriste. Nous savons que nous sommes sur la bonne piste!

On remonte sur le compte Instagram de notre suspect. Il s'appelle "Patrick Bekod" et son speudo est "patbekod". 
En faisant une recherche sur ces deux informations, on se rend compte qu'on ne trouve rien grâce au pseudo mais le nom prénom semble plus intéressant. En effet, on retrouve un compte Twitter (https://x.com/BekodP) en effectuant la recherche de son prénom Nom dans la recherche de twitter. 

En fouillant ses tweets, nous retrouvons un post sur une image de son bureau de travail avec un graphique légèrement flouté. Dans les réponses de ce tweet, une personne semble lui dire qu'il ne faut pas poster des dossiers internes sur internet (une lettre fait toute la différence 😉). Le ton formel et l'avertissement nous indique qu'il s'agit d'un supérieur de son entreprise. 

Nous avons donc le nom prénom de son supèrieur.