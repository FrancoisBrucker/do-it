---
layout: layout/mon.njk

title: "Node.js : Bases"
authors:
  - Benoit BEGUIER

date: 2023-12-11
tags: 
  - "temps 2"
  - "Node.js"
  - "Backend"
  - "JavaScript"

résumé: "Apprentissage des bases de Node.js"
---

{% prerequis %}

**Niveau :** Intermédiaire
**Prérequis :**

- Bases d'HTML, CSS et de JavaScript sont un plus

{% endprerequis %}

## Sommaire

1. Introduction
2. Apprentissage de Node.js
3. Mise en application

## Introduction

Pour la réalisation de ce cours, je me réfèrerais aux sources listées ci-dessous :

- *Passez au Full Stack avec Node.js, Express et MongoDB*, cours réalisé sur OpenClassrooms*. Accessible [ici](https://openclassrooms.com/fr/courses/6390246-passez-au-full-stack-avec-node-js-express-et-mongodb)
- *Deep Dive Into Modern Web Development*. Accessible [ici](https://fullstackopen.com/en/)
- *Maîtriser le Développement Back-End Web avec Node.js, Express et MongoDB*, MON d'Omar Salame. Accessible [ici](https://francoisbrucker.github.io/do-it/promos/2023-2024/Omar-Salame/mon/temps-1.2/)
- *Introduction to Node.js*, Node.js. Accessible [ici](https://nodejs.org/en/learn/getting-started/introduction-to-nodejs)
- *Basic Routing*, ExpressJS. Accessible [ici](https://expressjs.com/en/starter/basic-routing.html).

Le développement back-end représente la colonne vertébrale souvent méconnue mais cruciale de tout système informatique. Il englobe l'ensemble des opérations côté serveur, assurant le bon déroulement, la gestion des données et la logique métier nécessaire aux applications web et systèmes informatiques pour offrir des fonctionnalités interactives et dynamiques. Les bases de données, les serveurs web, les langages de programmation côté serveur et les frameworks sont au coeur du développement back-end.

## Apprentissage de Node.js

Je prends d'abord connaissance du MON d'Omar, car il constitue une bonne base pour la direction que je souhaite prendre lors de ce MON. Son MON est complet, je vous recommande de le consulter. Je ne suis pas sûr d'aller plus loin que lui en 10 heures. J'essaierai dans mon MON d'apporter des précisions et compléments.

## Mise en application

### Initialisation du projet avec Vite

Nous allons utiliser Vite dans ce tutoriel, tout comme dans mon POK 2.

Pour créer une application :

```shell
npm create vite@latest part1 -- --template react

cd part1
npm install

npm run dev
```

NPM signifie Node Package Manager.
Vite dirige l'application sur le port 5173. Cela crée un répertoire entier avec des modules, un fichier `index.html`, un fichier .css, et un package .json. Le code de l'application est dans le dossier *src*.

![alt](dossier.png)

### Configuration du serveur Node.js

Pour ajouter un serveur Node.js, je vais utiliser Express, un framework web reposant sur Node. Express s'installe avec la commande :

```shell
npm install express
```

On crée ensuite un fichier `server.js` à la racine du projet pour configurer le serveur.

```js
const express = require('express');
const app = express();
const port = 3001;

app.get('/', (req, res) => {
  res.send('Hello from the server!');
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});

```

### Configuration du Proxy

On modifie ensuite le fichier vite.config.js pour configurer le proxy vers le serveur Node.js.

```js
export default {
  server: {
    proxy: {
      '/api': 'http://localhost:3001',
    },
  },
};
```

### Communication Client-Serveur

On peut utiliser une commande `fetch` pour communiquer avec le serveur depuis le client React. Par exemple :

```js
fetch('/api')
  .then(response => response.json())
  .then(data => console.log(data));
```

Le développement Frontend, lui, s'effectue comme d'habitude.

### Formation d'OpenClassrooms

Je ne recommande pas spécialement la formation d'OpenClassrooms. La première partie est suffisante pour créer sa propre application, et la description de la route `GET` est bien faite. Le reste manque cependant de détails. La partie de sécurisation de l'API ne m'intéressait pas, tout comme multer.

## Conclusion

Je suis maintenant à l'aise avec les termes de base du développement fullstack. Je sais comment créer et paramétrer un serveur et un proxy. 