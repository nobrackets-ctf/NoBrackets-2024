# VIP-Only

L'application permet de créer un utilisateur, se connecter et accéder à son profil.

Si notre utilisateur est VIP, alors le flag s'affiche.

Le but est donc d'avoir accès à un compte VIP.


## Le modèle des données

Les données sont stockées dans une bdd mongo. La connexion entre node et mongo s'effectue via l'ODM mongoose.
```js
const UserSchema = new mongoose.Schema({
  username: { type: String, unique: true, required: true },
  password: { type: String, required: true },
  is_vip: { type: Boolean, required: true, default: false },
});
```

Tous les champs sont nécéssaires (required: true) et le champ `is_vip` est à false par défaut. Ça aurait été un peu trop facile si l'utilisateur était VIP par défaut...

## La faille

La connexion de l'utilisateur ne semble pas poser de problème. Cependant pour la création d'un utilisateur, ce n'est pas la même histoire !

```js
// Route d'inscription
app.post('/register', async (req, res) => {
  try {
    const user = new User(req.body); // Création de l'utilisateur
    await user.save();
    res.redirect('/');
  } catch (error) {
    res.send('Erreur lors de la création du compte.'); // Gestion des erreurs
  }
});
```

La création de l'utilisateur récupère la liste des arguments de la requête `POST` vers `/register` en utilisant `req.body`. Ces arguments sont ensuite **directement** passés au constructeur de mongoose afin de créer un nouvel utilisateur.

Par défaut, l'application envoie deux variables via cette requête `POST` :

```
username=SomeUser&password=SomePassword
```

Cependant nous avons vu auparavant qu'un utilisateur était défini par 3 champs :
- username
- password
- is_vip

Ce dernier n'est pas renseigné et ainsi tombe dans le cas par défaut, c'est à dire `is_vip=false`.

C'est là où la faille intervient ! Dans la façon dont les arguments sont envoyés au constructeur, rien ne nous empêche d'envoyer des arguments supplémentaires, comme par exemple... `is_vip` !

## Exploit

L'exploit est relativement simple, nous allons renseigner le champ `is_vip` à `true`.

Pour ce faire, à l'aide de *firefox* (ou autre), nous allons envoyer une requête `POST` du type :

```
username=SomeUser&password=SomePassword&is_vip=true
```

Dans *firefox* :
1. Clique droit, *inspect*, menu *Network*
2. Création d'un utilisateur via le formulaire
3. Dans le menu *Network*, Clique droit sur la requête vers `/register`, *Edit and Resend*
4. Modification du *Body* (il faut changer le username à minima & ajouter `&is_vip=true`)
5. Clique sur *Send*
6. Connexion au compte fraichement créé
7. Enjoy!


~ Keep pwning
Drahoxx
