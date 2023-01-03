---
layout: layout/post.njk

title: "BDD non relationnelles"
authors:
  - Antoine Varnerot

---
<head>
  <link rel="stylesheet" href="../../assets/style.css">
</head>


## Description du MON

Pendant les 10h consacrées à ce MON, je veux apprendre à utiliser une système de base de données non relationnnelle et l'intégrer à un projet existant.

## Préambule

1. Bases de données relationnelles

En général, les systèmes de bases de données vus jusqu'à présent sont des bases de données relationnelles. Ces dernières sont caractérisées comme ayant des schémas stricts et des relations entre les différentes tables importantes. Cela permet d'éviter de faire des erreurs dans l'écriture ou le récupérage de donnée.
MySQL et PostgreSQL sont des bons exemples de bdd relationnelles.

2. Bases de données non relationnelles

Les bdd non relationnelles ou NoSQL sont des bdd beaucoup plus libres : il n'y a pas de structure de tables stricts et pas de relations entre les tables. On travaille plutot avec des "documents" qui correspondent à des collections d’objets. Cela permet donc de regrouper des données ayant des structures différentes.
Exemples :  MongoDB, Cassandra, HBase, GraphQL ...

https://getc.com.tn/sql-vs-nosql-quelles-differences/

## Réalisation

Pour mon apprentissage d'un systeme de base de données non relationnelles, j'ai choisi MongoDb car c'est une technologie que j'ai déjà vu sur des offres de stage et elle m'a l'air très populaire. J'ai d'abord suivi le tuto : https://openclassrooms.com/fr/courses/6390246-passez-au-full-stack-avec-node-js-express-et-mongodb
Prérequis :
- Connaissances de base de Javascript
- Connaissances de l'architecture du web (client/serveur)
- Avoir envie d'apprendre Express et NodeJs aussi
Temps estimé : 5h

https://www.mongodb.com/atlas/database

Le site a un peu changé de design depuis que le tuto a été fait mais on s'y retrouve assez bien.

## Petit projet

Pour utiliser les connnaisances que je viens d'acquérir, j'ai décidé de faire un petit projet : une to-do list où l'on peut ajouter des taches, les supprimer et bien-sûr les afficher. 
(Le code est disponible ici: https://github.com/AntwanV/Little-Todo-app/tree/master)
Explication des grandes lignes:

<figure>
  <img src="../../assets/todoapp.png">
  <figcaption>To-do list</figcaption>
</figure>

Pour ajouter des tâches on écrit dans le champs "Add new item ..." et pour en supprimer on clique simplement dessus.

Pour comprendre le code, il faut s'intéresser au fichier todoController.js :

```javascript
const mongoose = require('mongoose');
var psw = require('./psw.js'); 

//Connect to Mongoose
mongoose.connect('mongodb+srv://antoine:'+psw+'@cluster0.qh9so.mongodb.net/?retryWrites=true&w=majority',
  { useNewUrlParser: true,
    useUnifiedTopology: true })
  .then(() => console.log('Connexion à MongoDB réussie !'))
  .catch(() => console.log('Connexion à MongoDB échouée !'));
```

Ici on importe mongoose (Doc: https://mongoosejs.com/) qui permet un dialogue plus facile entre MongoDb et NodeJs et la possibilité de créer des schémas de données.
Ensuite on se connecte à la bdd avec un identifiant (antoine) et un mot de passe (que j'ai mis dans un autre fichier qui n'est pas mis sur GitHub).

```javascript
//Models
const itemSchema = mongoose.Schema({
  name: {
  type: String,
  required: true
  }
});

const Item = mongoose.model('Item', itemSchema);
```