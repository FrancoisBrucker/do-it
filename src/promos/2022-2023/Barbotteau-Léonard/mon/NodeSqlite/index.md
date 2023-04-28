---
layout: layout/mon.njk

title: "Le MON-3 de Léonard"
authors:
  - Léonard Barbotteau

date: 2023-01-04

tags:
  - 'temps 2'
---

<!-- début résumé -->
Le Back-end avec Node.js, puis la base de données Sqlite
<!-- fin résumé -->

## Sources
[Un tuto youtube sur Node.js](https://www.youtube.com/watch?v=09tWCISVU70)
[Un tuto youtube sur la programmation asynchrone en Javascript](https://www.youtube.com/watch?v=nf0FvGwAQBg)
[De la documentation sur Sqlite](https://www.linuxtricks.fr/wiki/sqlite-l-essentiel-sur-cette-base-de-donnees-cli-sql-php)
[La documentation sur express](https://expressjs.com/fr)
[Une IA qui répond aux questions sépcifiques sur l'informatique avec une justesse étonnante](https://openai.com/api/)

### Introduction avec la programmation synchrone vs la programmation asynchrone.
D'après mes recherches, pour bien comprendre l'objet de ce MON il faut d'abord bien comprendre les notions de programmation synchrone/asynchrone.

Dans la programmation synchrone, on éxécute ligne par ligne, à chaque ligne on éxecute le code, et la ligne d'après on est certains que les lignes d'avant on été éxécutées.

Dans la programmation asynchrone, les conditions se font sur des événements qui peuvent intervenir à tout moment, et donc une ligne de code plus bas qu'une autre peut s'éxécuter avant la ligne plus haute, si la condition qui permet son éxécution est validée avant. 

Imaginons on utilise readLine qui permet d'interagir avec un utilisateur :

```
const readLine = require('readline')

const r1 = readLine.createInterface({
  input: process.stdin,
  output: process.stdout
})
```

On va alors créer une fonction qui demande le prénom de quelqu'un. En asynchrone, on va poser la question et faire en sorte qu'une fonction s'éxécute lorsqu'on a donné la réponse à la question, avec un callback:

```
const demarrerProgramme = () => {
  r1.question('Quel est ton prénom?', reponse => {
    console.log('Ton prénom est ' + reponse)
    r1.close()
  })
}
```
Tant que la réponse n'est pas donnée, le programme éxécute les lignes suivantes. 

## Le back-end.
Je n'ai très peu de notions sur la question et je vais donc commencer par les bases de Node.js.

### Qu'est ce que Node.js?
Node.js est un environnement d'exécution JavaScript qui permet de faire des applications web côté serveur. On peut utiliser JavaScript non seulement dans son navigateur, mais aussi sur son serveur web.

### A quoi sert Node.js?
Node.js est très populaire pour la création de serveurs web et de services en temps réel en raison de sa performance et de sa flexibilité.
Node.js permet également de construire des applications full-stack (c'est-à-dire avec une interface utilisateur côté client et un serveur côté serveur) en utilisant le même langage de programmation (JavaScript) sur les deux côtés.

### Comment utiliser Node.js ?
Pour utiliser Node.js, on peut écrire des scripts Node.js dans un éditeur de texte et les exécuter à l'aide de la commande "node" dans son terminal.
On peut également utiliser Node.js avec des frameworks tels que Express pour créer des applications web plus complexes. Ce sera le cas dans mon cours et pour la réalisation du POK.

### Les fonctionnalités qu'Express peut fournir
Explorant ce qu'est le back-end, les premières questions qui me viennent à l'esprit sont : à quoi cela sert de faire le lien entre le serveur et le client et comment le faire grâce à Express?
Nous allons le voir ici en listant les fonctionnalités d'Express

  - #### Le routage
    La définition de route s'écrit de cette manière:
    ```
    app.METHOD(PATH, HANDLER)
    ```
    Avec **app** une instance d'express, **METHOD** une méthode de demande HTTP, **PATH** un chemin sur le serveur et **HANDLER** la fonction exécutée lorsque la route est mise en correspondance.
    Express nous permet de créer des routes pour notre serveur, qui sont des URL spécifiques que votre serveur peut gérer. Par exemple, on peut créer une route "/" qui gère les requêtes à la racine de son site, ou une route "/api/users" qui gère les requêtes à une API utilisateur.

    On va prendre un exemple avec le code suivant:
    ```
    app.get('/partitions/:userId', (req, res) => {
      const userId = req.params.userId;

    // Récupérer les partitions de l'utilisateur à partir de la base de données ou d'une autre source de données
      const partitions = getPartitionsForUser(userId);

      res.send(partitions);
    });
    ```
    Grâce à cette route on peut répondre à une demande GET à l'URL **/partitions/:userId** où **:userId** est un paramètre de route qui peut être remplacé par l'Id de l'utilisateur. On extrait l'Id de l'utilisateur à partir des paramètres de route **req.params.userId** et la fonction utilise une fonction fictive **getPartitionsForUser** pour récupérer les partitions de l'utilisateur.

  - #### Middleware
    Express utilise des "middlewares" pour traiter les requêtes et les réponses. Un middleware est une fonction qui est exécutée avant que la requête ne soit envoyée à la route finale. Vous pouvez utiliser des middlewares pour faire toutes sortes de choses, comme vérifier l'authentification de l'utilisateur, enregistrer des données dans une base de données ou gérer les erreurs.

    ```
    app.get('/partitions/:userId', validateUser, (req, res) => {
      const userId = req.params.userId;

      // Récupérer les partitions de l'utilisateur à partir de la base de données ou d'une autre source de données
      const partitions = getPartitionsForUser(userId);

      res.send(partitions);
    });

    function validateUser(req, res, next) {
      const userId = req.params.userId;

      // Valider l'ID de l'utilisateur
      if (isValidUserId(userId)) {
        // Appeler le gestionnaire de route suivant si l'ID de l'utilisateur est valide
        next();
      } else {
        // Renvoyer une erreur si l'ID de l'utilisateur n'est pas valide
        res.status(400).send({ error: 'Invalid user ID' });
      }
    }
    ```

    Ici on a rajouté la fonction validateUser, un middleware qui vérifie l'ID de l'utilisateur et passe à la fonction **next()** si elle est valide. Sinon, la fonction renvoie une erreur au client.


  - #### Template engine
    Express prend en charge plusieurs "template engines", qui sont des outils qui vous permettent de générer du HTML ou d'autres types de contenu à partir de modèles. Cela peut être utile pour créer des sites Web dynamiques qui affichent des données provenant de votre serveur.

  - #### Gestion des erreurs
    Express vous permet de gérer facilement les erreurs qui se produisent sur votre serveur. Vous pouvez définir des gestionnaires d'erreur pour traiter les erreurs de différentes manières, par exemple en renvoyant une page d'erreur ou en envoyant un message à un service de surveillance.

  - #### Gestion de la session
    Express prend en charge la gestion de la session côté serveur, ce qui vous permet de stocker des informations sur les utilisateurs entre les requêtes. Vous pouvez utiliser cela pour créer des sites Web qui se souviennent de l'état de l'utilisateur, comme un panier d'achat ou un formulaire d'inscription.

    Une des solutions pour cela est de s'aider de cookies. Pour cela il faut d'abord installer la bibliothèque **cookie-parser**, ensuite on ajoute le middleware à l'application Express:

    ```
    const cookieParser = require('cookie-parser');
    app.use(cookieParser());
    ```
    Ensuite on définit le cookie dans la réponse HTTP :

    ```
    app.post('/preferences', (req, res) => {
      // Récupérer les préférences de l'utilisateur à partir de la demande
    const preferences = req.body.preferences;

      // Définir le cookie avec les préférences de l'utilisateur
      res.cookie('preferences', preferences, { maxAge: 900000, httpOnly: true });

      res.send({ message: 'Preferences saved' });
    });
    ```

    Les options du cookies contiennent **maxAge** qui définit la durée de vie du cookie en millisecondes, et **httpOnly** qui précise que le cookie ne peut être accédé que par le serveur ce qui peut prévenir des attaques.
    Quand l'utilisateur enverra une demande au serveur, le cookie sera envoyé simultanément et on pourra accéder aux préférences de l'utilisateur à l'aide de la propriété **req.cookies**:
    ```
    app.get('/preferences', (req, res) => {
      // Récupérer les préférences de l'utilisateur à partir du cookie
      const preferences = req.cookies.preferences;

      res.send({ preferences });
    });
    ```
## La base de données
### La base de données SQLite fonctionnant sous Express
Je vais désormais expliquer comment développer une base de données Sqlite et la faire fontionner sous Express
Pour ceci suivez ces étapes:

1. Installez SQLite et le module Sqlite pour Node.js avec npm:

  ```
  npm install sqlite3
  ```
2. Créez un fichier comme **BDD.sqlite** dans le projet et utilisez le module **sqlite3**

  ```
  const sqlite3 = require('sqlite3').verbose();
  const db = new sqlite3.Database('BDD.sqlite');
  ```

3. Créez une table dans la base de données en exécutant une requête SQL:

  ```
  db.serialize(() => {
    db.run("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, pseudo TEXT, password TEXT)");
  });
  ```

4. Insérez des données dans la table en exécutant une autre requête SQL :

  ```
  db.serialize(() => {
    const stmt = db.prepare("INSERT INTO users (pseudo, password) VALUES (?, ?)");
    stmt.run("Leonard", "draneol");
    stmt.run("Nathan", "nahtan");
    stmt.finalize();
  });
  ```
5. Créez un serveur Express et configurez-le pour pouvoir récupérer les informations de la base de données lors de requêtes HTTP :

  ```
  const express = require('express');
  const app = express();

  app.get('/users', (req, res) => {
    db.all("SELECT * FROM users", (err, rows) => {
      res.send(rows);
    });
  });

  app.listen(3000, () => {
    console.log('Server listening on port 3000');
  });
  ```

Voilà, l'application a bien été construite

Pour ajouter un nouvel enregistrement dans la table users avec les valeurs **Vincent** et **tnecniv** pour les colonnes **name** et **password**, vous pouvez utiliser une requête INSERT SQL comme ceci :

  ```
  db.run("INSERT INTO users (name, password) VALUES (?, ?)", "Vincent", "tnecniv");
  ```

On peut également utiliser la méthode **run** d'une fonction préparée:

  ```
  const stmt = db.prepare("INSERT INTO users (name, password) VALUES (?, ?)");
  stmt.run("Vincent", "tnecnit");
  stmt.finalize();
  ```
Cette méthode est efficace si on veut insérer plusieurs enregistrements.