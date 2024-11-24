// Importations
const express = require('express');
const mongoose = require('mongoose');
const session = require('express-session');
const bcrypt = require('bcryptjs');
const fs = require('fs');
const crypto = require('crypto');

// Modèle Base de Données
const User = require('./models/User');

// Config
const app = express();
app.set('view engine', 'ejs');
app.use(express.urlencoded({ extended: true }));
app.use(express.static('public'));

const sessionSecret = process.env.SESSION_SECRET || crypto.randomBytes(32).toString('hex');
const mongoUri = process.env.MONGO_URI;

// Configuration de la session
app.use(
  session({
    secret: sessionSecret,
    resave: false,
    saveUninitialized: true,
  })
);

// Connexion à MongoDB
mongoose.connect(mongoUri, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});



// Middleware pour vérifier si un utilisateur est connecté
function isAuthenticated(req, res, next) {
  if (req.session.userId) {
    return next();
  }
  res.redirect('/'); // Rediriger vers la page d'accueil si non authentifié
}

// Route de la page d'accueil
app.get('/', (req, res) => {
  res.render('index'); // Rendre la vue d'index
});

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

// Route de connexion
app.post('/login', async (req, res) => {
  const { username, password } = req.body;
  const user = await User.findOne({ username });
  if (user && (await bcrypt.compare(password, user.password))) {
    req.session.userId = user._id;
    req.session.is_vip = user.is_vip;
    res.redirect('/profile');
  } else {
    res.send('Identifiants invalides'); // Message d'erreur pour identifiants incorrects
  }
});

// Route de déconnexion
app.get('/logout', (req, res) => {
  req.session.destroy(err => {
    if (err) {
      return res.status(500).send('Impossible de se déconnecter.'); // Gestion des erreurs
    }
    res.clearCookie('connect.sid');
    res.redirect("/"); // Rediriger vers la page d'accueil
  });
});

// Route de profil
app.get('/profile', isAuthenticated, async (req, res) => {
  const user = await User.findById(req.session.userId);
  res.render('profile', { user }); // Rendre la vue de profil avec les données de l'utilisateur
});

// Route pour accéder au flag
app.get('/flag', isAuthenticated, (req, res) => {
  if (req.session.is_vip) {
    const flag = fs.readFileSync('flag.txt', 'utf8');
    res.send(`Flag: ${flag}`); // Win :)
  } else {
    res.send('Le flag est réservé aux VIPs 😊');
  }
});

// Démarrer le serveur
app.listen(3000, () => console.log('Serveur en cours d\'exécution sur http://localhost:3000'));

