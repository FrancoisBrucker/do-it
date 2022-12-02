---
layout: layout/post.njk

title: "Coté Web"
authors:
  - Gabriel BARBE

---
<!-- Début Résumé -->
MON sur le developpement côté serveur suivi sur le site de M. Brucker puis sur mdn developper. 
<!-- Fin Résumé -->
Il n'est pas question de paraphraser ici l'entièreté du cours, néanmoins j'incluerai un résumé sous chaque partie. <br/>
Etant complètement débutant j'ai trouvé que le cours dispensé en anglais sur [mdn.developper](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/development_environment) détaillait plus toute la démarche de création de serveur, c'est pourquoi après les deux premiers modules, j'ai continué mon apprentissage sur ce site.
## Coté serveur 
### Lire des données 
Afin de lire des données sur un site web et les réutiliser ensuite, on utilise la fonction javascript "fetch". Cette dernière est fondamentale dans l'utilisation des bases de données. La fonction fetch peut être utilisé sur des fichiers textes, des images ou du json ([voir Devweb 1](Devweb1)) à condition que ces dernières soient sur un serveur web !
### Serveur web minimal
On peut créer un "serveur minimal" grâce à node simplement avec la commande shhell : 
```bash
node index.js
```
Cette commande crée un serveur minimal en local. 
Ce serveur suit le protocole http c'est à dire une suite de requête de l'utilsateur et de réponse de la machine. 

### Création du premier projet grâce à Node/Express 
Express est un framework de node, lui-même environnement de développement, permettant de coder des sites côtés serveurs. Tout l'intéret de l'apprentissage de ce MON est de basculer le site créer avec le premier POK : "Mon site chez moi" coté serveur.<br>
Le framework Express crée tout le "squelette" de notre site web et l'importe sur un serveur local. Ce serveur est localisé à http://localhost:3000/.
Nous obtenons donc notre premier site web sur serveur : <img src="../../Images/Express.png">
Nous avons pour le moment les dossiers suivants dans notre environnement de programmation : <img src="../../Images/Dossiers.png">
- le dossier "bin" contient un fichier "www" qui représente l'hébergement de notre site
- les dossiers "models" ainsi que "public" sont vides pour le moment : "models" nous servira pour la base de données et "public" pour les images et les styles. 
- "routes" indique les routes 
- "views" montre les messages que l'on voit affiché en fonction des réponses de notre serveur
- les fichiers ".json" sont l'identité de notre projet et le fichier app.js est l'endroit où l'on programme notre site et ressemble pour le moment à ceci : 

```bash
var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');

var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);
app.use('/users', usersRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
```

### Utiliser une base de donnée
Dans cette troisième partie nous apprenons à insérer une base de données sur notre site express via mongoose et mangodb. Cette partie fondamentale est surement la plus compliqué que j'ai effectuée en informatique depuis cette année. <br>
Nous avons commencé par créer un compte sur <a href=hhtp://cloud.mongodb.com/> puis le tout est de connecter notre application ou site avec la database présente sur le cloud. Pour se faire, nous utilisons le lien que nous donne mangodb : 'mongodb+srv://username:password!@cluster0.kngjtje.mongodb.net/?retryWrites=true&w=majority' que nous lions avec notre projet dans le fichier app.js : 

```bash
var mongoose = require('mongoose');
var dev_db_url = 'mongodb+srv://username:password!@cluster0.kngjtje.mongodb.net/?retryWrites=true&w=majority';
var mongoDB = process.env.MONGODB_URI || dev_db_url;
mongoose.connect(mongoDB, {useNewUrlParser: true, useUnifiedTopology: true});
mongoose.Promise = global.Promise;
var db = mongoose.connection;
db.on('error', console.error.bind(console, 'MongoDB connection error:'));
```