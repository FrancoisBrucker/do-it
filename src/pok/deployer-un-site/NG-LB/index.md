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

- Déploiement du site sur le serveur

- Ecrire le back du site en node. Cette étape nécessitera une documentation approfondie en raison de nos connaissances précaires en la matière

- Faire une base du données en SQLite

- Faire le lien entre le back, le site et la base de données

## 1.2 Objectifs optionnels du POK

Ces objectifs seront réalisés si nous avons le temps après avoir fini les objectifs précédents. 

- Améliorer le front du site, notamment son apparence et réaliser des finitions

- Rajouter des fonctionnalités à la partition de musique

## 1.3 Tâches du premier sprint à réaliser d'ici le mercredi 07/12.

- Déployer le site sur ovh

- Commencer l'écriture du back après avoir pris en main les outils (node / express a priori)

- Commencer la base de données (avec SQLite a priori)

## 2.1 Réalisations du premier sprint.
Nous avons pu à l'aide des premières connaissances acquises par nos MON commencer à améliorer le site et le pousser sur un serveur distant.

Le site est déployé sur l'herbe de Provence de Nathan (Thym), les fichiers utiles sont mieux structurés (notamment avec le fichier static) et un fichier index.js nous permet de controler le back-end.

En ce qui concerne la base de données, on a un tableau pour les utilisateurs et un tableau pour les partitions enregistrées. Chaque partition appartient à un utilisateur (que l'on retrouve avec son ID) et possède un élément JSON qui correspond aux notes de la partition. Il reste à pouvoir alimenter la base de données en utilisant le back-end.

