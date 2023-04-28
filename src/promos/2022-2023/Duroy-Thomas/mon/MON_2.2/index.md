---
layout: layout/mon.njk

title: "MON 2.2 : Back-end avec Node.js et Express"
authors:
  - Thomas Duroy 

date: 2023-01-25

tags:
  - 'temps 2'
  - 'back'
  - 'Express'
---

Durant ce MON, j'ai pu en apprendre davantage sur le back-end. Dans un premier temps, j'ai appris ce qu'était Node.js, son architecture et son fonctionnement.

Puis je me suis initié au codage d'une API RESTful basique en suivant les tutoriels de [Programming with Mosh](https://www.youtube.com/@programmingwithmosh).

Enfin, j'ai complété une [openclassroom](https://openclassrooms.com/fr/courses/6390246-passez-au-full-stack-avec-node-js-express-et-mongodb/6466206-configurez-votre-environnement-de-developpement) où le but était de développer un middleware plus complexe en y connectant une base de données.

## Qu'est ce que le back-end ?

Le back-end est la partie invisible de l'iceberg. Concrètement, il s'agit de l'ensemble des rouages côté serveur permettant de faire fonctionner un site web quand le client envoie une requête.

![Back-end illustration](./back-end%20illustration.jpg)

Pour s'occuper de toute ces taches, il nous faut donc un serveur. Ce sera le rôle de Node.js que d'utiliser notre machine comme support pour lancer un serveur local.

## Qu'est ce que Node.js ?

### Description et utilisation de Node.js

Node.js est un environnement d'exécution basé sur le même moteur javascript que Google à savoir "V8".

Il fonctionne de manière asynchrone. C'est-à-dire qu'il envoie au moteur les commandes à exécuter  en permanence sans attendre que ce dernier ait terminé la commande précédente pour s'attaquer à la suivante. Cela lui permet de fonctionner de manière fluide et d'enchaîner les commandes peu voraces, parfait pour du dev web.

{% attention %} Attention, il est nécessaire de [télécharger](https://nodejs.org/en/download/) Node.js pour pouvoir l'utiliser ! {% endattention %}

Pour utiliser Node.js, il faut d'abord initialiser un projet node. Pour ce faire, avec un powershell/une interface de commande, il faut se rendre dans le dossier de votre projet puis lancer la commande:

```powershell
npm init
```

De nombreux paramètres seront réglables. Faîtes simplement attention à nommer (server.js par exemple) comme vous le désirez votre point d'accès serveur (entry pont).

Puis vous pouvez démarrer votre serveur avec la commande suivante (on conserve le nom server.js pour l'exemple mais il faudra prendre le nom de votre point d'accès).

```powershell
nodejs server.js
```

Bon, on n'a pas vraiment créé de serveur, parce que Node.js se contente de lire le contenu de "server.js". Cette fonctionnalité se trouve dans le module http.

{% info %}
Un outil précieux: [Nodemon](https://www.npmjs.com/package/nodemon) permet aux changements apportés à votre fichier js de s'afficher directement, sans avoir à redémarrer votre serveur à chaque fois.
{% endinfo %}

Pour une explication plus détaillée : [l'avis de l'expert](https://www.youtube.com/watch?v=TlB_eWDSMt4&ab_channel=ProgrammingwithMosh).

### Les modules de Node.js

À l'instar des librairies python, les modules sont des éléments js avec de nombreuses fonctionnalités que l'on peut importer avec la commande require:

```js
const http = require("http");
```

Les [basiques](https://www.w3schools.com/nodejs/nodejs_modules.asp) sont: "http" pour s'occuper de tout ce qui est création et communication avec un serveur, "File System" pour manipuler fichier et dossiers, "URL" pour manipuler des URL ou bien "Event" pour ajouter de l'intéractivité à son js.

Mais les modules peuvent très bien être votre propre fichier js. C'est d'ailleurs la base des API. Dans ce cas, dans "require" on remplacera le nom du module par sa localisation sur votre machine.

À des niveaux plus complexes, nous avons les package et les framework (dont Express fait partie) qui sont installés et géré par le "Node Package Manager" (npm). L'installation se fait dans le powershell comme suit:

```powershell
npm i nom_package
```

Pour revenir à l'histoire du serveur, en utilisant le package http, il suffit d'écrire dans notre fichier js la chose suivante :

```js
const http = require("http");

const server = http.createServer((req,res)=>{
    res.writeHead(200);
    res.end("Hello World!");
})

server.listen(3000);
```

3 choses à retenir ici :

- Un serveur prend en charge deux éléments: la requête (req) et la réponse (res).
- Des messages et des status (ex: erreur code 404) sont usuellements intégrés à la réponse pour des soucis de compréhension.
- On définit un port d'écoute pour le serveur. Ici le port 3000. Pour y accéder, il suffit de taper "http://localhost:3000" dans son navigateur.

Cette structure étant simpliste. Elle n'est jamais réellement utilisée. On préférera créer le serveur à partir d'un autre fichier js qui sera l'application s'occupant du routage et des requêtes.

Une implémentation plus complexe que l'on verra est celle de l'API RESTful. On la mettra en place grâce au framework "Express"

## Express et RESTful API

Express est un framework de Node.js donnant accès à de nombreuses fonctionnalités pour développer une appli web. Un avantage majeur est qu'il permet de structurer le routage et donc de s'affranchir des inconvénients de tester les routes.

Pour l'utiliser:

```js
const express = require('express');

const app = express();
```

Où "app" sera notre application à laquelle on va ajouter des fonctionnalités REST.

Une API RESTful (REpresentative State Transfer) est une application mettant en pratique la logique CRUD (Create Read Updata Delete) d'une base de donnée à travers 4 méthodes fondamentales: get/post/put/delete.

Un outil intéressant pour tester si les fonctions marchents correctement est l'application google "Postman" permettant de créer des requêtes HTTP à destination de son serveur.

Par la suite, je vais vous montrer une API "répertoire" qui s'occuper de données avec le schéma suivant:

```js
const répertoire = [
    {id:1,prénom: 'Thomas', nom: 'Duroy'},
    {id:2,prénom: 'Joe', nom: 'Mama'},
    {id:3,prénom: 'Dize', nom: 'Nutse'},
];
```

### Fonction GET et exemple

La fonction GET est la plus basique. Elle permet d'avoir accès à n'importe quel URL définit dans le routage et d'y consulter les éléments.

Ici, deux exemples:

```js
app.get('/api/repertoire', (req,res) =>{
    res.send(répertoire);
});

app.get('/api/repertoire/:id',(req,res) => {
    //Vérifier que la personne existe
    const personne = répertoire.find(p => p.id === parseInt(req.params.id));
    if (!personne) res.status(404).send("La personne n'existe pas");
    res.send(personne);
});
```

Remarques:
    - Une fonction REST prend 2 arguments, la route et le binôme requête/réponse.
    - Si dans la route, un élément est précédé de ":" alors il est utilisable dans la fonction avec l'appel "params.élément".

### Fonction POST et exemple

POST permet de créer une nouvelle entité, qui sera réutilisable pour le routage.

```js
app.post('/api/repertoire',(req,res) =>{
    //checker si la requête est valide
    if (!req.body.prénom || !req.body.nom) {
        res.status(400).send('Incomplete input');
    }
    //ajouter la nouvelle personne
    const personne = {
        id: répertoire.length + 1,
        prénom: req.body.prénom,
        nom: req.body.nom
    };

    répertoire.push(personne);
    res.send(personne);
});
```

### Fonction PUT et exemple

La fonction PUT permet de mettre à jour un item (à condition qu'il soit présent) ou de le créer s'il est absent. Ici j'ai voulu faire la distinction entre post et put en testant l'existance.

```js
const répertoire = [
    {id:1,prénom: 'Thomas', nom: 'Duroy'},
    {id:2,prénom: 'Joe', nom: 'Mama'},
    {id:3,prénom: 'Dize', nom: 'Nutse'},
];
```

```js
app.put('/api/répertoire/:id', (req,res)=>{
    //Vérifier que la personne existe
    const personne = répertoire.find(p => p.id === parseInt(req.params.id));
    if (!personne) res.status(404).send("La personne n'existe pas");

    //checker si la requête est valide
    if (!req.body.prénom || !req.body.nom) {
        res.status(400).send('Incomplete input');
    }

    personne.prénom = req.body.prénom;
    personne.nom = req.body.nom;
    res.send(personne);
});
```

### Fonction DELETE et exemple

DELETE est assez évocateur comme nom.

```js
app.delete('/api/repertoire/:id', (req,res) => {
    //Vérifier que la personne existe
    const personne = répertoire.find(p => p.id === parseInt(req.params.id));
    if (!personne) res.status(404).send("La personne n'existe pas");

    //Supprimer la personne
    const index = répertoire.indexOf(personne);
    répertoire.splice(index,1);

    res.send(personne);
});
```

### Créer un serveur avec Express

L'avantage d'Express est qu'il utilise les fonctionnalités de HTTP d'où le fait de pouvoir créer le server directement:

```js
const port = 3000 ;
app.listen(3000,() => console.log(`listening on port 3000`));
```

Il suffit alors de lire avec Node.js le fichier de l'application directement.
