---
layout: layout/post.njk

title: "Mon sheet c'est moi : suite et déploiement"
authors:
  - Léonard Barbotteau
  - Nathan Gissler

tags: ['web']
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