---
layout: layout/mon.njk

title: "Développement d'une Application avec Node.js"
authors:
  - "Sofiane Ouadda"
date: 2024-10-20

tags: 
  - "temps 2"
  - "Dévelopement Web"
  - "BackEnd"
  - "Node.js"

résumé: "Ce cours détaille comment créer une application complète avec Node.js, de la configuration initiale à la mise en place d’une API REST."

---

{% prerequis %}

Bases en JavaScript (ES6) sont nécessaires. Une connaissance des concepts d'API REST et de gestion des dépendances est recommandée.

{% endprerequis %}
{% lien %}

[`Node.js Documentation Officielle`](https://nodejs.org/en/docs/)

[`Express.js Guide`](https://expressjs.com/)

[`MDN Web Docs - Using Fetch`](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)

[`Node.js Crash Course - Traversy Media`](https://www.youtube.com/watch?v=fBNz5xF-Kx4)

[`Learn Node.js for Beginners`](https://www.youtube.com/watch?v=RLtyhwFtXQA)

{% endlien %}

## Objectifs

À la fin de ce cours, vous serez capable de :
1. Comprendre les bases de Node.js et son modèle d'exécution.
2. Installer et configurer un projet Node.js avec npm.
3. Créer un serveur HTTP avec Node.js.
4. Construire une API REST avec Express.js.
5. Interagir avec une base de données.

---

## 1. Introduction à Node.js

Node.js est un environnement d'exécution JavaScript basé sur le moteur V8 de Chrome. Il permet d'exécuter JavaScript côté serveur et de construire des applications backend performantes et évolutives.

### Points Clés :
- **Non-bloquant** : Node.js utilise un modèle d'E/S non bloquant basé sur des événements, ce qui le rend idéal pour des applications temps réel.
- **Écosystème** : Node.js s'appuie sur npm, qui offre un large choix de bibliothèques et outils.

### Avantages de Node.js
- Applications scalables et performantes.
- API REST faciles à mettre en œuvre.
- Large communauté et nombreux modules prêts à l’emploi.

---

## 2. Installation et Configuration

### Installation de Node.js

1. Téléchargez et installez [Node.js](https://nodejs.org).
2. Vérifiez l'installation : `node -v npm -v`

### Initialisation d'un projet Node.js

1. Créez un nouveau dossier pour votre projet :
  - `mkdir my-project`
  - `cd my-project`

2. Initialisez le projet avec npm :
  - `npm init -y`

Cela crée un fichier `package.json` contenant les informations sur votre projet et ses dépendances.

---

## 3. Création d’un Serveur HTTP

Node.js inclut un module natif pour créer des serveurs HTTP : le module `http`.

### Exemple de Serveur HTTP

Créez un fichier `server.js` :

```
const http = require('http');

const server = http.createServer((req, res) => {
res.writeHead(200, { 'Content-Type': 'text/plain' });
res.end('Hello, World!');
});

server.listen(3000, () => {
console.log('Serveur en écoute sur le port 3000');
});
```

### Exécution
  - ***Lancez le serveur:*** `node server.js`

Ouvrez http://localhost:3000 dans un navigateur pour voir votre serveur en action.


## 4. Utilisation de Express.js

Express.js est un framework minimaliste pour Node.js qui simplifie la création d’API et la gestion des routes.

### Installation de Express.js

  -`npm install express`

#### Exemple d'API REST avec Express

  * Dans le fichier server.js :

  ```
  const express = require('express');
  const app = express();

  // Middleware pour parser les requêtes JSON
  app.use(express.json());

  // Route de base
  app.get('/', (req, res) => {
    res.send('Bienvenue dans notre API!');
  });

  // Endpoint GET
  app.get('/api/users', (req, res) => {
    res.json([{ id: 1, name: 'Sofiane' }, { id: 2, name: 'Soso' }]);
  });

  // Endpoint POST
  app.post('/api/users', (req, res) => {
    const user = req.body;
    console.log('Utilisateur ajouté :', user);
    res.status(201).send(user);
  });

  app.listen(3000, () => {
    console.log('API en écoute sur le port 3000');
  });
  ```

## 5. Interaction avec une Base de Données

Pour interagir avec une base de données, vous pouvez utiliser des bibliothèques comme mongoose (MongoDB) ou pg (PostgreSQL).

### IExemple avec MongoDB et Mongoose

1. Installez MongoDB et Mongoose :

  -`npm install mongoose`

2. Configurez la connexion dans server.js :

```

  const mongoose = require('mongoose');

  mongoose.connect('mongodb://localhost:27017/monprojet', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connexion à MongoDB réussie'))
    .catch(err => console.error('Erreur de connexion à MongoDB :', err));

  const userSchema = new mongoose.Schema({
    name: String,
    email: String,
  });

  const User = mongoose.model('User', userSchema);

  app.post('/api/users', async (req, res) => {
    const user = new User(req.body);
    await user.save();
    res.status(201).send(user);
  });
  ```

  ## Ressources pour aller plus loin

- [Node.js Documentation Officielle](https://nodejs.org/en/docs/)
- [Express.js Guide](https://expressjs.com/)
- [MDN - Guide JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Traversy Media - Node.js Crash Course](https://www.youtube.com/watch?v=fBNz5xF-Kx4)

---

## Horodateur

| Date       | Heures passées | Indications                                                                  | 
|------------|----------------|------------------------------------------------------------------------------|
| 25/10      | 1H30           | Lecture de la documentation officielle Node.js et installation d’un projet   | 
| 26/10      | 2H             | Pratique sur la création d’un serveur HTTP simple avec Node.js               |
| 27/10      | 1H30           | Apprentissage d’Express.js et construction d’une API REST                   |
| 27/10      | 1H30           | Manipulation de fichiers avec le module `fs`                                |
| 28/10      | 2H             | Utilisation de Mongoose pour interagir avec une base MongoDB                 |
| 29/10      | 2H             | Mise en œuvre des connaissances dans un projet pratique                     |
| 30/10      | 2H             | Retranscription du cours en markdown                                         |

