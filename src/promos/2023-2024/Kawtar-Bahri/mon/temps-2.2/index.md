---
layout: layout/mon.njk

title: "Développement Back-end : Node.js, Express & MongoDB"
authors:
  - Kawtar Bahri
  
date: 1971-01-01
tags: 
  - "temps 2"
  - "Node.js" 
  - "Express"
  - "MongoDB"

résumé: " "
---

## Ressources utilisées : 
•	[Cours sur Youtube](https://www.youtube.com/watch?v=Oe421EPjeBE) (non recommendés pour les débutants comme moi)
•	[Cours de Mr François Brucker](https://francoisbrucker.github.io/cours_informatique/cours/web/) 
•	MON précedents (notamment de [William Lalanne](https://francoisbrucker.github.io/do-it/promos/2023-2024/William%20Lalanne/mon/temps-2.1/), [Lucas Rioual](https://francoisbrucker.github.io/do-it/promos/2023-2024/Rioual-Lucas/mon/temps-1.2/) et de [Royant Killian](https://francoisbrucker.github.io/do-it/promos/2022-2023/Royant-Killian/mon/temps_2/fullstack/) qui m’ont fait découvrir la [formation de OpenClassRoom](https://openclassrooms.com/fr/courses/6390246-passez-au-full-stack-avec-node-js-express-et-mongodb/6521356-tirez-le-maximum-de-ce-cours))


## Configuration de l'environnement 
Avant de commencer à coder, il est primordiale d'instalLer quelques outils : 
•	Installer [Node.js](https://nodejs.org/en)
•	***Fichier package.json*** : est un fichier de métadonnées utilisé dans les projets Node.js pour gérer les dépendances du projet, les scripts, et divers paramètres de configuration. La commande pour créer le fichier package.json : ‘npm init’, ensuite il suffit suivre les invites. Après avoir créé le fichier package.json, on utilise ‘npm install’ pour installer les dépendances répertoriées dans le fichier.
•	***Installer nodemon*** : Il surveille les fichiers dans votre application Node.js et redémarre automatiquement le serveur chaque fois qu'il détecte des changements dans ces fichiers. Commande d'installation : npm install --save-dev nodemon
•	***Ajouter l’extension ThunderClient sur VSC***. Elle permet d'envoyer des requêtes HTTP et de visualiser les réponses directement dans l'éditeur Visual Studio Code. Ce qui simplifie le développement et les tests.
•	***Installer Express*** par la commande ‘npm install express’
•	***Installer Mongoose*** par la commande‘npm install mongoose’
## Création d'un serveur 

Pour créer un serveur, on va se mettre dans le dossier configuré dans la partie précédente. On y crée un fichier serveur.js contenant : 

```js
const express = require('express');
const app = express();
const port = 3000; 

app.get('/', (req, res) => {
  res.send('Hello World'); 
});

app.listen(port, () => {
  console.log(`Serveur en cours d'exécution sur http://localhost:${port}`);
});

```
Les routes dans Node.js avec Express sont un moyen de définir comment l'application doit répondre à une demande client pour une ressource spécifique. Vous pouvez définir des routes pour différentes méthodes HTTP (GET, POST, etc.) selon la sutructure suivante :

```js
// Route pour la page d'accueil
app.get('/', (req, res) => {
  res.send('Bienvenue sur la page d\'accueil !');
});

// Route pour une page spécifique
app.get('/about', (req, res) => {
  res.send('À propos de nous.');
});

// Route avec des paramètres
app.get('/utilisateur/:id', (req, res) => {
  res.send(`Informations sur l'utilisateur avec l'ID : ${req.params.id}`);
});
```

Executer le serveur par la commande ‘node app.js’.
## Création d’une base de données 
### MongoDb Atlas 
Dans un projet backend, nous avons besoin de bases de données pour stocker les données de manière persistante, afin qu'elles ne se perdent pas lorsque le serveur est redémarré ou lorsque la session utilisateur est terminée.

MongoDB Atlas est un service de base de données cloud géré qui permet aux utilisateurs de déployer, gérer et évoluer des clusters MongoDB dans le cloud. Pour l'utiliser, on a besoin de créer un compte et de paramétrer sa base de données (Database Access, Network Access) afin d'obtenir la chaîne de connexion.
### Mongoose 
Mongoose est une bibliothèque Node.js qui fournit une couche d'abstraction sur MongoDB. Elle  facilite l'interaction avec une base de données MongoDB en permettant de définir des modèles, de créer des schémas, et d'effectuer des opérations de base de données de manière plus conviviale.

Commande d'installation : ‘npm install mongoose’
### Schéma d’une base de données

Avant de définir le schéma de la base de données, on doit une connexion à la base de données avec Mongoose.

```js
const mongoose = require('mongoose');
const uri = 'la_chaine_de_connexion'; 
mongoose.connect(uri, { useNewUrlParser: true, useUnifiedTopology: true });

const db = mongoose.connection;
db.on('error', console.error.bind(console, 'Erreur de connexion à MongoDB :'));
db.once('open', () => {
  console.log('Connecté à la base de données MongoDB');
  
});
```

Le schéma d'une base de données est une représentation structurée des différentes entités (tables), des champs (colonnes), et des relations entre ces entités dans une base de données. Dans le contexte d'une base de données NoSQL, telles que les bases de données de type document (comme MongoDB), sont souvent caractérisées par leur approche flexible du stockage de données, ce qui conduit à une gestion de schéma moins rigide.
Voici un exemple de code qui définit le schéma d'une base de données : 

```js
const mongoose = require('mongoose');

const utilisateurSchema = new mongoose.Schema({
  nom: String,
  age: Number,
  email: String
});

const Utilisateur = mongoose.model('Utilisateur', utilisateurSchema);

```