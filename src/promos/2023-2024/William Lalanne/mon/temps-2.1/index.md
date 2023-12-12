---
layout: layout/mon.njk

title: "Backend avec Node.js et express"
authors:
  - William Lalanne

date: 2023-09-27

tags: 
  - "temps 2"

résumé: "Dans ce MON je souhaite me former au backend avec Node.js et express"
---

{% prerequis %}
**Niveau :** Moyen
**Prérequis :** Avoir fait un peu de JavaScript avant
{% endprerequis %}

## Sommaire

1. Création du serveur 
2. Création de l'application express
3. Les Middlewares


## Création du serveur 
Pour démarrer un serveur basique, il faut d'abord commencer par importer le package HTTP indispensable pour créer un serveur :
```js
const http = require('http'); 
```

Une fois le package HTTP importé, on peut créer notre serveur à l'aide des commandes suivantes: 
```js
const server = http.createServer((req, res) => {
    res.end('Voilà la réponse du serveur !');
});
```

Le serveur est créé simplement grâce à la fonction ***createServer*** du package HTTP à qui on donne deux arguments:
- ***req*** qui correspond à la requête faîte au serveur.
- ***res*** qui correspond à la réponse.

Ensuite, à chaque requête faite au serveur la fonction après le **(req, res)** est jouée. Dans notre cas, à chaque requête faite au serveur on reçoit la réponse : 'Voilà la réponse du serveur'. 
On améliorera plus tard dans ce MON le serveur pour qu'il fasse ce que l'on veut. 


## Création de l'application express

Après avoir créé notre serveur, il faut maintenant créer l'application express. Express est un framework de Node.js très utile car il facilite grandement l'écriture des requêtes au serveur. D'abord, il faut créer un fichier **app.js** dans lequel nous allons créer l'application avec la commande suivante: 
```js
const express = require('express');

const app = express();

module.exports = app;
```
D'abord on importe le package express, puis on crée l'application grâce à la méthode ***express()*** et enfin on exporte l'application pour l'utiliser dans d'autres fichiers. 

Il faut ensuite exécuter l'application Express que l'on vient de créer dans le serveur Node. 
On revient sur le fichier de départ où l'on écrit les commandes suivantes :
```js
const http = require('http');
const app = require('./app');

app.set('port', process.env.PORT || 3000);
const server = http.createServer(app);

server.listen(process.env.PORT || 3000);
```

Par rapport à avant, on a ajouté plusieurs lignes :
- ***const app = require('./app');*** on importe l'application Express sur le serveur pour pouvoir l'utiliser
- ***app.set('port', process.env.PORT || 3000);*** avec cette ligne on précise sur quel port doit être lancé l'application, soit sur le port en cours soit sur le port 3000. 
- ***const server = http.createServer(app);*** commande qui permet de créer le serveur et qui prenc comme argument l'application créé, mais comme notre application ne fait rien pour l'instant, chaque requête faite au serveur renverra une erreur 404. 

Pour que le serveur réponde quelque chose il faut que l'on ajoute des commandes dans notre application.

```js
app.use((req, res) => {
   res.json({ message: 'Votre requête a bien été reçue !' }); 
});
```
Grâce à cette commande, à chaque requête faite au serveur, il renvoie la réponse **"Votre queête a bien été reçue"**. 


## Les Middlewares. 
La commande ci-dessus est ce qu'on appelle un middleware, les application express sont éssentiellements composées d'une suite de middlewares. Ce sont des fonctions qui reçoivent en entrée une requête (req) et une réponse (res). Ils peuvent lire ces objets, les analyser et les manipuler. On peut aussi leur donner en entrée la méthode next qui permet à un middleware de passer l'exécution du code au middleware suivant. 
Pour mieux comprendre, prenons un exemple :
```js
const express = require('express');

const app = express();

app.use((req, res, next) => {
  console.log('Requête reçue !');
  next();
});

app.use((req, res, next) => {
  res.status(201);
  next();
});

app.use((req, res, next) => {
  res.json({ message: 'Votre requête a bien été reçue !' });
  next();
});

app.use((req, res, next) => {
  console.log('Réponse envoyée avec succès !');
});

module.exports = app;
```

Pour faire simple, le premier middleware renvoie "requête reçue" lorsque qu'il y a une requête faite au serveur. Ensuite, il passe l'exécution au middleware suivant qui lui, renvoie un statut 201 puis passe l'éxecution. Le troisième middleware renvoie une réponse sous format JSON puis passe l'exécution. Le dernier renvoie "Réponse envoyée avec succès" dans la console. 


## Les différentes méthodes HTTP et les routes

Pour faire des requêtes au serveur, on utilise des méthodes HTTP :
- GET est une méthode qui permet de recevoir des informations du serveur. 
- POST permet d'envoyer des informations au serveur. 
- DELETE permet de supprimer des données du serveur. 

Les routes permettent de définir comment l'application doit répondre à une requête HTTP spécifique. Par exemple, si on veut mettre en place un sytème d'authentification sur un site, il y aura une route pour l'inscription, une pour la connexion et une pour la deconnexion. 

Pour faire une requête POST, on s'inspire de ce qu'on a fait pour les middlewares mais au lieu d'utiliser la méthode ***use*** on utilise la méthode ***post*** :

```js
app.post('/api/stuff', (req, res, next) => {
  res.status(201).json({
    message: 'Objet créé !'
  });
});
```
On voit que contrairement à la requête ***use***, ici il y a le chemin ***'/api/stuff'***. Cela permet de préciser comment notre route doit être utilisé. Le préfixe 'api' laisse imaginer que notre requête concerne une api à laquelle on va vouloir ajouter un objet. 







