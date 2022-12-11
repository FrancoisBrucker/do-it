---
layout: layout/post.njk

title: "Coté Web"
authors:
  - Gabriel BARBE
tags: ['Server']
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
Nous avons pour le moment les dossiers suivants dans notre environnement de programmation : <img src="../../Images/Dossiers.PNG">
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
Nous avons commencé par créer un compte sur hhtp://cloud.mongodb.com/ puis le tout est de connecter notre application ou site avec la database présente sur le cloud. Pour se faire, nous utilisons le lien que nous donne mangodb : 'mongodb+srv://username:password!@cluster0.kngjtje.mongodb.net/?retryWrites=true&w=majority' que nous lions avec notre projet dans le fichier app.js : 

```bash
var mongoose = require('mongoose');
var dev_db_url = 'mongodb+srv://username:password!@cluster0.kngjtje.mongodb.net/?retryWrites=true&w=majority';
var mongoDB = process.env.MONGODB_URI || dev_db_url;
mongoose.connect(mongoDB, {useNewUrlParser: true, useUnifiedTopology: true});
mongoose.Promise = global.Promise;
var db = mongoose.connection;
db.on('error', console.error.bind(console, 'MongoDB connection error:'));
```
Nous crééons ensuite une base de donnée comprenant des livres, des auteurs etc. par l'intermédiaire d'un nouveau fichier "populatedb.js" qui nous sert à peupler la base de données. Ce fichier contient par exemple des fonctions telles que :
```bash
function authorCreate(first_name, family_name, d_birth, d_death, cb) {
  authordetail = {first_name:first_name , family_name: family_name }
  if (d_birth != false) authordetail.date_of_birth = d_birth
  if (d_death != false) authordetail.date_of_death = d_death
  
  var author = new Author(authordetail);
       
  author.save(function (err) {
    if (err) {
      cb(err, null)
      return
    }
    console.log('New Author: ' + author);
    authors.push(author)
    cb(null, author)
  }  );
}
function createGenreAuthors(cb) {
    async.series([
        function(callback) {
          authorCreate('Patrick', 'Rothfuss', '1973-06-06', false, callback);
        },
        function(callback) {
          authorCreate('Ben', 'Bova', '1932-11-8', false, callback);
        },
    ]);
}
```
Cette fonction renvoi à un autre fichier, "author.js", stocké dans "models" définissant l'objet "auteur". 
```bash
const mongoose = require("mongoose");

const Schema = mongoose.Schema;

const AuthorSchema = new Schema({
  first_name: { type: String, required: true, maxLength: 100 },
  family_name: { type: String, required: true, maxLength: 100 },
  date_of_birth: { type: Date },
  date_of_death: { type: Date },
});

AuthorSchema.virtual("name").get(function () {
  // To avoid errors in cases where an author does not have either a family name or first name
  // We want to make sure we handle the exception by returning an empty string for that case
  let fullname = "";
  if (this.first_name && this.family_name) {
    fullname = `${this.family_name}, ${this.first_name}`;
  }
  if (!this.first_name || !this.family_name) {
    fullname = "";
  }
  return fullname;
});

AuthorSchema.virtual("url").get(function () {
  return `/catalog/author/${this._id}`;
});

// Export model
module.exports = mongoose.model("Author", AuthorSchema);
```

Nous pouvons retrouver cette base de données à tout moment sur mangodb : <img src='../../Images/database.PNG'>

### Routes 
Définition : Une route est une section de code qui associe un HTTP, un chemin URL et une fonction qui les associe sur le site. <br>
Express possède un middleware permettant de créer des routes directement. Ce middleware permet de créer des routes pour les requêtes : "get", "post", "delete", "copy", "subscribe"... et bien d'autres. Ainsi, pour chaque filtre de notre base de données, nous crééons un fichier où l'on code toutes les requêtes souhaitées. Nous plaçons ces fonctions dans un dossier.<br>
Un exemple de fichier "listController" peut-être : 
```bash
const Element = require("../models/element");

//Liste tous les éléments
exports.list = (req, res) => {
  res.send("NOT IMPLEMENTED: Element list");
};
```
Ce code crée un URL où l'on listera tous les éléments de notre base de données. Nous verrons plus tard comment l'associer réellement à notre BDD. 
Le code suivant permet ensuite de créer la route en tant que tel, nous le plaçons donc dans le dossier express "routes"
```bash
const list_controller = require("../controllers/listController");

//Page principale du site
router.get("/", list_controller.index);
```
Les routes "index" et "users" sont automatiquement implantées dans le fichier "app.js" mais on peut rajoutés des fichiers dans "Routes" et es reliées dans "app.js". <br>
En l'état actuel, notre page affiche le message : "Not implemented : Element list"
Il nous suffit simplement de remplacer la fonction "export.list" dans "listController" et elle pourra ensuite afficher notre base de donnée : 
```bash
exports.list = function (req, res, next) {
  Element.find({}, "Information 1")
    .sort({ title: 1 })
    .exec(function (err, list) {
      if (err) {
        return next(err);
      }
      res.render("list", { title: "List", list: books });
    });
};
```
Que l'on associe avec un fichier "list.pug" dans notre dossier "View" : 
```bash
extends layout

block content
  h1= title

  ul
    each element in list
      li
        a(href=element.url) #{element.title}
    else
      li There are no books.
```
### 