---
layout: layout/pok.njk

title: "Mon sheet c'est moi : suite et déploiement"
authors:
  - Léonard Barbotteau
  - Nathan Gissler

tags:
  - 'temps 2'
  - web
---

<!-- début résumé -->

Mon sheet c'est moi, suite du développement du site et déploiement sur un serveur distant (POK-Temps 2)

<!-- fin résumé -->

## 1.1 Objectifs primordiaux du POK

- Déploiement sur le serveur du site développé au temps 1

- Ecrire le back du site en node. Cette étape nécessitera une documentation approfondie en raison de nos connaissances précaires en la matière

- Faire une base de données en SQLite

- Faire le lien entre le back, le site et la base de données

## 1.2 Objectifs optionnels du POK

Ces objectifs seront réalisés si nous avons le temps après avoir fini les objectifs précédents.

- Améliorer le front du site, notamment son apparence et réaliser des finitions

- Rajouter des fonctionnalités à la partition de musique

## 2.1 Tâches du premier sprint à réaliser d'ici le mercredi 07/12.

- Déployer le site sur ovh

- Commencer l'écriture du back après avoir pris en main les outils (node / express a priori)

- Commencer la base de données (avec SQLite a priori)

## 2.2 Réalisations du premier sprint.

Nous avons pu à l'aide des premières connaissances acquises par nos MON commencé à améliorer le site et le pousser sur un serveur distant. Nous avons comme prévu déployé le site sur le serveur et commencé à travailler avec Express et SQLite, mais le temps nécessaire pour acquérir des connaissances au fur et à mesure a fait que nous n'avons pas encore pu beaucoup avancer.

### Déploiement du site sur le serveur ovh

Le site est déployé sur l'herbe de Provence de Nathan (Thym), on peut y accéder à cette adresse : [http://thym.ovh1.ec-m.fr/mon-sheet-cest-moi/static/index.html](http://thym.ovh1.ec-m.fr/mon-sheet-cest-moi/static/index.html), sans express pour le moment.

Nous avons rencontré quelques difficultés avec l'installation de xz (qui permet de compresser des archives avec la méthode Lzma), nous avons donc pour l'instant envoyé sur le serveur l'archive contenant le site directement.

### Express

Nous avons commencé à utiliser Express : gestion des routes et accès au site en local. Les fichiers du site sont mieux structurés (notamment avec le dossier static) et un fichier index.js nous permet de controler le back-end.

### Base de données

En ce qui concerne la base de données, nous avons un tableau pour les utilisateurs et un tableau pour les partitions enregistrées. Chaque partition appartient à un utilisateur (que l'on retrouve avec son ID) et possède un élément JSON qui correspond aux notes de la partition. Il reste à pouvoir alimenter la base de données en utilisant le back-end.

## Tâches du deuxième sprint

- Faire fonctionner Express sur ovh

- Faire fonctionner la base de données

- Gérer l'édition de partition en temps réel avec Meteor

## 2.2 Réalisations du second sprint.

A l'aide de nos MON mais également des cours nous avons pu continuer à travailler et faire avancer le site. Nous avons bien avancé mais ne sommes pas au bout de nos peines, si tant est que nous soyions amenés à poursuivre le projet.

### La base de données

Nous étions parti pour réaliser la base de données avec le modules sqlite3, cependant sur avis de M.Brucker nous avons décidé de partir sur l'utilisation de sequelize, avec MySQL.
Nous avons mieux organisé les fichiers du site afin de créer des routes claires pour associer le front, le back et la BDD de la meilleure manière possible.
Nous nous sommes inspiré d'une architecture déjà existante, d'un utlisateur github utilisant sequelize et Express, dont le projet est ici : [Un exemple Github utilisant Sequelize avec Express](https://github.com/FaisonsLePoint/api_rest_express).
Nous avons également apprécié les explications de Hugo Guillaume, ingénieur diplomé de Centrale Marseille.
Le site ne fonctionne pas encore à cause d'erreurs sur la base de données lorsque l'on tente d'envoyer des requêtes au back depuis le front, mais on peut voir la lumière au bout du tunnel. 

### Meteor

J'ai trouvé un [exemple d'utilisation de Meteor](https://blog.jscrambler.com/meteor-framework-hardest-part-coming-app-name-2) pour créer un éditeur de texte collaboratif. Le cas de l'éditeur de texte est beaucoup plus classique que le nôtre mais j'ai décidé de commencer par reproduire cet exemple pour comprendre le fonctionnement du framework.

Cependant, j'ai été confronté à des difficultés lors de l'installation de Meteor. Une version de Node inférieure à 14 est requise alors que la version 16 est installée chez moi. J'ai donc entrepris d'installer nvm (Node version manager) afin de pouvoir changer de version de Node plus facilement. J'ai réussi à l'installer mais je ne suis pas parvenu à changer la version de Node, ce qui m'a bloqué pour l'utilisation de Meteor.

### Express sur ovh

En parallèle, j'avais comme objectif de faire fonctionner la gestion des routes sur ovh avec Express (ce qui fonctionnait déjà en local). J'ai également été bloqué, cette fois par le transfert de fichiers sur ovh. Le désarchivage du fichier `tar` avec la commande `tar -xvf mon-sheet-cest-moi.tar` ne faisait plus apparaître le dossier désarchivé, que ce soit localement ou sur ovh.