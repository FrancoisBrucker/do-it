---
layout: layout/mon.njk

title: "[MON] Passez au Full Stack avec Node.js, Express et MongoDB"
authors:
  - Killian ROYANT
date: 2023-01-04

tags:
  - 'temps 2'
  - DevWeb
  - BackEnd
  - JavaScript
  - API
  - NoSQL
  - MongoDB
  - Node.js
  - Express
  - FullStack
---

<!-- début résumé -->

Présentation du premier MON de mon temps 2 : une introduction au développement Full Stack avec Node.js, Express et MongoDB basée sur une formation proposée par Openclassrooms.

<!-- fin résumé -->

[<-- Retour](../)

{% prerequis "**Prérequis**" %}

Une connaissance de la relation client-serveur, ainsi qu'une connaissance pratique de JavaScript, HTTP/AJAX (asynchronous JavaScript and XML), et Git. Si vous n'avez pas ces prérequis, nous vous recommandons de commencer par les formations [Openclassroom](https://openclassrooms.com) suivants :  

- [Apprenez la programmation à l'aide de JavaScript](https://openclassrooms.com/fr/courses/6175841-apprenez-a-programmer-avec-javascript)
- [Écrivez JavaScript pour le Web](https://openclassrooms.com/fr/courses/5543061-ecrivez-du-javascript-pour-le-web)
- [Utilisez Git et GitHub pour vos projets de développement](https://openclassrooms.com/fr/courses/5641721-utilisez-git-et-github-pour-vos-projets-de-developpement)

Vous pouvez jetter un œil à des MON précédents pour vous aider à vous familiariser avec ces notions :

- [Louise GARCOIN - Web Front 1](../../../LG/MON2/)
- [Savinien LAEUFFFER - Web Front 1](../../../SL/webfront/web-front-1/)
- [Gabriel BARBE - Dev Web 2](../../../GB/Mons/Devweb2/)
- [Killian ROYANT - Créez des pages web dynamiques avec JavaScript](../js/)

Outils nécessaires :

- un éditeur de code ;
- Node.

{% endprerequis %}

## Introduction

Afin d'obtenir les connaissances nécessaires à la réalisation de mon POK, je souhaite me former au **développement Web Full Stack**. Après avoir réalisé mon [MON JS](../js/) au temps 1 qui expliquait comment créer des pages web dynamiques avec JavaScript, j'ai décidé de suivre une formation proposée par [Openclassrooms](https://openclassrooms.com/fr) présentant comment passer au développement Full stack à l'aide d'outils comme Node.js, Express et MongoDB.

![Passez au Full Stack avec Node.js, Express et MongoDB](https://i.vimeocdn.com/video/831167886-a5fc36e3ebad0faa112367f30c68d4f32ae1f759bee515b454169908dc55db2f-d_640)

Le lien de la formation est disponible : [Passez au Full Stack avec Node.js, Express et MongoDB (Openclassrooms)](https://openclassrooms.com/fr/courses/6390246-passez-au-full-stack-avec-node-js-express-et-mongodb)

Cette formation est composée de **4 parties** qui mettent en place un **projet concret** de développement d'une API. Chacune de ces parties est composé de **plusieurs leçons** et d'un **quiz**. Dans ces leçons, vous retrouverez du **cours** écrit, les lignes de **code** qui permettent de créer l'API ainsi que des **vidéos** qui expliquent pas à pas comment y arriver.

{% info "**Objectifs**" %}

À la fin de ce cours, vous serez capable de :

- créer un serveur web simple avec Express ;
- créer une API REST avec Node, Express et MongoDB ;
- mettre en place un système d'authentification sur une application Express ;
- gérer des fichiers utilisateur sur une application Express.

{% endinfo %}

{% chemin "**Ressources utiles**" %}

- [Passez au Full Stack avec Node.js, Express et MongoDB (Openclassrooms)](https://openclassrooms.com/fr/courses/6390246-passez-au-full-stack-avec-node-js-express-et-mongodb)
- [Getting Started Guide (Node.js)](https://nodejs.org/en/docs/guides/getting-started-guide/)
- [Getting started (Express)](https://expressjs.com/en/starter/installing.html)

{% endchemin %}

### Table des matières

Vous trouverez ci-dessous la table des matières de la formation :

{% prerequis %}

#### Partie 1 - Créez un serveur Express simple

Cette partie vous permettra de **créer un serveur web simple** avec Express avec laquelle vous pourrez communiquer via des requêtes HTTP. Vous pourrez ainsi **envoyer et recevoir** des données au format JSON via différentes **routes** (adresses web) et différents types de requêtes (GET, POST).

--

1. Tirez le maximum de ce cours
2. Configurez votre environnement de développement
3. Démarrez votre serveur Node
4. Créez une application Express
5. Créez une route GET
6. Créez une route POST

--

#### Partie 2 - Créez une API RESTful

Cette partie vous présentera comment **créer une API REST fonctionnelle** comportant une base de données non-relationnelle. Vous apprendrez à créer une base de données avec **MongoDB**, à communiquer avec elle ainsi qu'à créer toutes les routes nécessaires pour gérer les données de votre API.

--

1. Configurez votre base de données
2. Créez un schéma de données
3. Enregistrez et récupérez des données
4. Modifiez et supprimez des données

--

#### Partie 3 - Mettez en place un système d'authentification sur votre application

Cette partie vous permettra de **mettre en place un système d'authentification** sur votre application. Vous apprendrez à **crypter** les mots de passe des utilisateurs, à **générer des jetons d'authentification** et à **protéger les routes** de votre API.

--

1. Optimisez la structure du back-end
2. Préparez la base de données pour les informations d'authentification
3. Créez des utilisateurs
4. Vérifiez les informations d'identification d'un utilisateur
5. Créez des tokens d'authentification
6. Configurez le middleware d'authentification

--

#### Partie 4 - Ajoutez une gestion des fichiers utilisateur sur l'application

Enfin, cette partie vous permettra de **gérer les fichiers** des utilisateurs de votre application. Vous apprendrez à **stocker les images** des utilisateurs sur votre serveur, à **générer des liens uniques** pour accéder à ces images et à les **supprimer**.

--

1. Acceptez les fichiers entrants avec multer
2. Modifiez les routes pour prendre en compte les fichiers
3. Développez la fonction delete du back-end

--

{% endprerequis %}

Bonne formation !

## Pour commencer

Si vous ne souhaitez pas suivre la formation, voici **quelques pistes pour vous aider à commencer** à développer votre API.

Tout d'abord, **nous allons voir comment créer un serveur Express simple**.

Pour **installer Node.js**, il suffit de **télécharger** le fichier d'installation sur le site officiel : [Node.js](https://nodejs.org/en/). Une fois l'installation terminée, vous pouvez **vérifier que Node.js est bien installé** en ouvrant un terminal et en tapant la commande suivante :

```bash
node -v
```

Vous devriez obtenir la version de Node.js installée sur votre ordinateur.

Pour **installer Express**, il suffit de taper la commande suivante dans un terminal :

```bash
npm install express --save
```

Cette commande va installer Express et l'ajouter dans la liste des dépendances de votre projet.

Vous pouvez maintenant **créer un fichier** `server.js` dans lequel vous allez **créer votre serveur Express**. Voici un exemple de code pour un serveur Express simple qui renvoie le texte "Hello World!" à l'adresse [http://localhost:3000](http://localhost:3000/) :

```javascript
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(3000, () => {
  console.log('Example app listening on port 3000!');
});
```

Pour **lancer votre serveur**, il suffit de taper la commande suivante dans un terminal :

```bash
node server.js
```

Vous pouvez maintenant **accéder** à votre serveur en tapant l'adresse suivante dans votre navigateur : [http://localhost:3000](http://localhost:3000/)

Vous pourrez maintenant **créer des routes GET et POST pour votre API**. Pour cela, vous pouvez vous référer à la partie 1 de la formation ou consulter la documentation officielle de Node.js et d'Express fournie dans les ressources utiles.

[<-- Retour](../)
