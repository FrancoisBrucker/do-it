---
layout: layout/pok.njk

title: "Mon sheet c'est moi, interactions avec le serveur et la base de données"
authors:
  - Léonard Barbotteau
  

date: 2023-01-25

tags:
  - 'temps 3'
  - 'base de données'
  - 'sequelize'
  - 'back-end'
---

<!-- début résumé -->

Mon sheet c'est moi, interactions avec le serveur et la base de données en rectifiant les erreurs du front. La fonctionnalité de pouvoir enregistrer les partitions a été la plus chronophage. (POK-Temps 3)
voici le lien pour le github du site : [mon-sheet-cest-moi](https://github.com/nathan-gissler/mon-sheet-cest-moi)

<!-- fin résumé -->

## 1.1 Objectifs primordiaux du POK
Les objectifs n'ont pas beaucoup changé depuis le temps 2 car ils étaient très compliqué à mettre en place.

- Ecrire le back du site en node.

- Faire une base de données en MySQL

- Faire le lien entre le back, le site et la base de données

- Déploiement sur le serveur du site développé au temps 1

## 1.2 Objectifs optionnels du POK

Ces objectifs seront réalisés si j'ai le temps après avoir fini les objectifs précédents. 

- Améliorer le front du site, notamment son apparence et réaliser des finitions

- Rajouter des fonctionnalités à la partition de musique

### Base de données

En ce qui concerne la base de données, nous avons une table pour les utilisateurs et une table pour les partitions enregistrées. Chaque partition appartient à un utilisateur (que l'on retrouve avec son ID) et possède un élément JSON qui correspond aux notes de la partition. L'élément JSON est en fait transformé en TEXT dans la partie serveur pour pouvoir être traitée, et c'est côté client qu'on passe de TEXT à JSON. Il reste à pouvoir alimenter la base de données en utilisant le back-end.

J'ai repris les fichiers du site afin de créer des routes claires pour associer le front, le back et la BDD de la meilleure manière possible. On a un dossier pour les routes, un dossier pour les modèles des utilisateurs et des partitions et un dossier pour les controlleurs.

### Affichage côté client

Grande partie du travail : récupérer les infos de la base de données avec les fetch et les afficher sur le site. Pour les partitions, il faut qu'un utilisateur puisse accéder à ses partitions, donc une fois qu'il est connecté, on prend son Id dans l'url et ensuite on la récupère sur la page suivante, affichant pour chaque partition un bloc avec les données de la partition. Ensuite, quand on clique sur un bloc d'une partition, on accède à la partition sur la page après.

Pour l'affichage de la partition, on utilise les fonctions de frontend qui permettent de récupérer un JSON et d'en faire une partition, travail réalisé au préalable par Nathan.

### Problèmes rencontrés

Mon POK a été marqué de beugs, de problèmes etc... Je vais parler de ceux que vous pourrez recontrer si vous importez le projet depuis github ou même si vous réalisez un projet similaire.

#### Mysql
Déjà, vous pouvez avoir des problèmes avec MySQL. Le premier que j'ai rencontré consistait en le fait que je n'avais pas le mot de passe pour me connecter. Réinstaller Mysql permet de palier au problème. Ensuite, j'ai fait face à un autre problème : le serveur contenant la base de données que j'utilisais était arrêté, et pas moyen de le redémarrer avec la ligne de commande Mysql ou même Mysql Workbench : et pour cause, le service s'était arrêté tout seul sur mon PC. Donc dans ce cas de figure, attention de bien regarder dans les "services" de votre ordinateur si vous n'avez pas eu de problème : le service Mysql doit se démarrer automatiquement. J'ai rencontré d'autres problèmes. Réinstaller Mysql est radical mais est une méthode qui fonctionne toujours.

#### Ordre d'appel des fonctions dans la base de données
Une erreur simple mais qui m'a pris beaucoup de temps à résoudre est la suivante : dans mon fichier javascript principal, j'avais appelé la base de données et éxécuté des fonctions test qui devaient créer un utilisateur et une partition. Et là, plein d'erreur de base de données : en fait trop habitué au python, je pensais qu'éxécuter les fonctions interagissant avec la base de données à la fin du script était safe, mais en fait la fonction qui connectait à la base de données étaient asynchrone. Il fallait donc juste appeler les fonctions de test dans la fonction de connexion à la base de données, une fois qu'on a bien vérifié qu'elle existe.
En résumé : **attention aux fonctions asynchrones**

#### Plein d'erreurs sur ce qu'on a pas le droit de faire dans le back, ce qu'on a pas le droit de faire dans le front
Franchement là des fois ça manque de logique. Pourquoi je pourrais pas remplir le localStorage depuis le back? Bon des fois c'est quand même plus logique, comme les fetch depuis le client. Mais bon il faut s'y habituer.

### Ce qu'il reste à faire
- Déjà, corriger toutes les erreurs qu'il peut y avoir
- Synchroniser la page de la partition avec les infos sur l'utilisateur et la partition
- Pouvoir partager la partition à d'autres utilisateurs
- Améliorer le visuel
- Mettre en place la possiblité de jouer la partition directement sur le site