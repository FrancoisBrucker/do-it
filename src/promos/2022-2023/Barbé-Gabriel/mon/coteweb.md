---
layout: layout/mon.njk

title: "Coté Web"
authors:
  - Gabriel BARBE
tags: 
  - 'serveur'
  - 'temps 2'

date: 2023-01-04
---
<!-- Début Résumé -->
MON sur le developpement côté serveur suivi sur le site de M. Brucker puis sur mdn developper. <br>
Nous apprendrons entre autre à créer une base de données, l'utiliser, la modifier depuis le site web mais aussi apprendre le "back-end" et l'associer au "front-end". Ce cours sera constitué de deux partie. <br>
Niveau : Intermédiaire<br>
Prérequis : [DevWeb1](Devweb1.md), [DevWeb2](./Devweb2.md)
<!-- Fin Résumé -->

## Préambule
J'ai affiché un niveau intermédiaire mais j'aurais tout aussi bien pu mettre facile, en effet le cours est relativement accessible étant donné que je suis moi-même un débutant, et qu'avec le temps alloué j'ai été capable d'effectuer les taches voulues. Néanmoins, pour les débutants, il vous faudra sortir de votre zone de confort et être motivé car il y a des passages quelques peu ardus où avoir un projet en tête aide. Pour moi ce cours a été suivi dans l'idée de réaliser mon projet [PFC](/src/pok/GB-TB/index.md) que vous pouvez aussi visiter pour mieux comprendre mes intentions. <br>
Mes sources principales sont le cours de François Brucker [Web](https://francoisbrucker.github.io/cours_informatique/cours/web/) et un cours en anglais  sur le site [MDN Developer](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/development_environment)<br/>
Bon cours !
## Coté serveur 
### Lire des données 
Afin de lire des données sur un site web et les réutiliser ensuite, on utilise la fonction javascript "fetch". Cette dernière est fondamentale dans l'utilisation des bases de données. La fonction fetch peut être utilisé sur des fichiers textes, des images ou du json ([voir Devweb 1](./Devweb1.md)) à condition que ces dernières soient sur un serveur web !
### Serveur web minimal
On peut créer un "serveur minimal" grâce à node simplement avec la commande shell : 
```bash
node index.js
```
Cette commande crée un serveur minimal en local. 
Ce serveur suit le protocole http c'est à dire une suite de requête de l'utilsateur et de réponse de la machine. 

### Création du premier projet grâce à Node/Express 
Express est un framework de node, lui-même environnement de développement, permettant de coder des sites côtés serveurs. Tout l'intéret de l'apprentissage de ce MON est de basculer le site créer avec le premier POK : "Mon site chez moi" coté serveur.<br>
Le framework Express crée tout le "squelette" de notre site web et l'importe sur un serveur local. Ce serveur est localisé à http://localhost:3000/.
Nous obtenons donc notre premier site web sur serveur : <img src="../Images/Express.png">
Nous avons pour le moment les dossiers suivants dans notre environnement de programmation : <img src="../Images/Dossiers.PNG">
- le dossier "bin" contient un fichier "www" qui représente l'hébergement de notre site
- les dossiers "models" ainsi que "public" sont vides pour le moment : "models" nous servira pour la base de données et "public" pour les images et les styles. 
- "routes" indique les routes 
- "views" est là où l'on code l'interface. 
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
Nous crééons ensuite une base de donnée comprenant des chaines de caractères, des dates, des nombres etc. Cette base est crée par l'intermédiaire d'un nouveau fichier "populatedb.js" qui nous sert à peupler la base de données. Ce fichier contient par exemple des fonctions telles que :
```bash
function personCreate(first_name, family_name, d_birth, d_death, cb) {
  persondetail = {first_name:first_name , family_name: family_name }
  if (d_birth != false) persondetail.date_of_birth = d_birth
  if (d_death != false) persondetail.date_of_death = d_death
  
  var person = new Person(authordetail);
       
  person.save(function (err) {
    if (err) {
      cb(err, null)
      return
    }
    console.log('New Player: ' + person);
    persons.push(person)
    cb(null, person)
  }  );
}
function createGenrePersons(cb) {
    async.series([
        function(callback) {
          playerCreate('Patrick', 'Rothfuss', '1973-06-06', false, callback);
        },
        function(callback) {
          playerCreate('Ben', 'Bova', '1932-11-8', false, callback);
        },
    ]);
}
```
Cette fonction renvoi à un autre fichier, "person.js", stocké dans "models" définissant l'objet "personne". 
```bash
const mongoose = require("mongoose");

const Schema = mongoose.Schema;

const PersonSchema = new Schema({
  first_name: { type: String, required: true, maxLength: 100 },
  family_name: { type: String, required: true, maxLength: 100 },
  date_of_birth: { type: Date },
  date_of_death: { type: Date },
});

PersonSchema.virtual("name").get(function () {
 
  let fullname = "";
  if (this.first_name && this.family_name) {
    fullname = `${this.family_name}, ${this.first_name}`;
  }
  if (!this.first_name || !this.family_name) {
    fullname = "";
  }
  return fullname;
});

PersonSchema.virtual("url").get(function () {
  return `/catalog/person/${this._id}`;
});

// Export model
module.exports = mongoose.model("Person", PersonSchema);
```

Nous pouvons retrouver cette base de données à tout moment sur mangodb : <img src='../Images/database.PNG'>

### Routes 

Définition : Une route est une section de code qui associe un HTTP, un chemin URL et une fonction qui les associe sur le site. <br>
Express possède un middleware (sorte de pont entre différentes applications web) permettant de créer des routes directement. Ce middleware permet de créer des routes pour les requêtes : "get", "post", "delete", "copy", "subscribe"... et bien d'autres. Ainsi, pour chaque filtre de notre base de données, nous créons un fichier où l'on code toutes les requêtes souhaitées. Nous plaçons ces fonctions dans un dossier "controller".<br>
Un exemple de fichier "listController" peut-être : 
```bash
const Element = require("../models/element");

//Liste tous les éléments
exports.list = (req, res) => {
  res.send("NOT IMPLEMENTED: Element list");
};
```
Ce code crée un URL où l'on listera tous les éléments de notre base de données. Nous verrons plus tard comment l'associer réellement à notre BDD. 
Le code suivant permet ensuite de créer la route en tant que tel, nous le plaçons donc dans le dossier express "routes" :
```bash
const list_controller = require("../controllers/listController");

//Page principale du site
router.get("/", list_controller.index);
```
Les routes "index" et "users" sont automatiquement implantées dans le fichier "app.js" mais on peut rajoutés des fichiers dans "Routes" et les relier dans "app.js". <br>

### Mis en page du site web 
Nous avons désormais nos routes et notre base de donnée prête à être utilisée. Il nous reste donc à exploiter (dans un premier temps plus simplement afficher) les données sur notre site. Pour se faire, nous allons effectuer des modifications dans 2 dossiers : controller et view. Ces deux dossiers sont reliés et on peut considérer que les fichier controllers sont le "back" alors que les fichiers views sont le "front". En effet, les dossier view sont écrit en pug, un dérivé de html, et décrira explicitement ce que "verra" l'utilisateur. <br> 
En l'état actuel, notre page affiche le message : "Not implemented : Element list". Il nous suffit simplement de remplacer la fonction "export.list" dans "listController" et elle pourra ensuite afficher notre base de donnée : 
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
Nous pouvons bien-sûr associer ce fichier à un fichier CSS et à un fichier JS comme nous l'avons vu auparavant (voir [DevWeb](../index.md))

### Forms 

Nous sommes désormais capable de créer une base de données et de l'afficher sur notre site. Afin de créer des interactions avec l'utilisateur, nous souhaiterions lui donner la possibilité de modifier la base de données. Pour ceci, nous utilisons les "forms". Ce sont des balises html qui donnent la possibilité à l'utilisateur de donner des informations et de les rentrer sur le serveur. <br/>
Après que l'utilisateur ait rentré son nouvel élément, express-validator, que nous devons installer, se chargera de vérifier que la donnée correspond bien à celle attendue et sinon, enverra un message d'erreur. 
Pour exemple, si l'on veut vérifier que notre donnée n'est pas un texte vide, il nous suffit d'insérer une ligne dans "controller : 
```bash
[
  body("name", "Empty name").trim().isLength({ min: 1 }).escape(),
];
```
Attention, il faut au préalable définir dans nos routes et nos controller si la donnée est de type "GET" ou "POST". <br/>
Nous crééons donc notre fonction de création puis nous la reportons dans un fichier view : 
```bash
exports.humain_create_post = [

  body("name")
    .trim()
    .isLength({ min: 1 })
    .escape()
    .withMessage("First name must be specified.")
    .isAlphanumeric()
    .withMessage("First name has non-alphanumeric characters."),
    (req, res, next) => {
    
    const errors = validationResult(req);

    if (!errors.isEmpty()) {
      res.render("person_form", {
        title: "Create Humain",
        person: req.body,
        errors: errors.array(),
      });
      return;
    }
    const person = new Person({
      name: req.body.name,
    });
    person.save((err) => {
      if (err) {
        return next(err);
      }
      res.redirect(person.url);
    });
  },
];
```
Nous créons finalement un fichier "person_form.pug" dans view où nous mettons : 
```bash 
form(method='POST' action='')
    div.form-group
      label(for='name') Name:
      input#name.form-control(type='text' placeholder='Name' name='name' required='true' value=(undefined===person ? '' : person.first_name) )
    button.btn.btn-primary(type='submit') Submit
  if errors
    ul
      for error in errors
        li!= error.msg
```
Nous sommes désormais capable de mettre à jour notre base de données !