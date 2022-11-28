---
layout: layout/post.njk

title: "POK d'Antoine Varnerot"
authors:
  - Antoine Varnerot

tags: ['pok']
---
<head>
  <link rel="stylesheet" href="../../un-site-chez-moi/AV/assets/style.css">
</head>

<!-- Début Résumé -->
MONs d'Antoine Varnerot

<!-- fin Résumé -->

## Temps 1

<p style="text-align: center; font-size: 1.5rem;"><strong>Mon site chez moi</strong></p>

L'objectif de ce POK est de créer un portfolio.

Lien vers le repo Github : https://github.com/AntwanV/POKcv

Voici le wireframe : 

<figure>
  <img src="../../un-site-chez-moi/AV/assets/wireframe.png">
  <figcaption>Wireframe du portfolio</figcaption>
</figure>

J'ai ensuite choisi de réaliser mon site avec Angular car j'avais fait mon premier MON sur cette technologie. Je l'ai complété avec SASS qui est un framework CSS mais que j'ai clairement pas utilisé à son plein potentiel. C'était plus pour essayer une techno.

Dans le projet j'ai aussi eu besoin de quelques librairies :
- bootstrap
- ngx-vertical : timeline verticale (https://github.com/aleckendall/ngx-timeline-vertical)
- locomotive-scroll : smooth scroll (https://github.com/locomotivemtl/locomotive-scroll)
- ...

Toutes ces librairies sont disponibles dans le fichier package.json

TODO :
- ~~Trouver une idée de site~~
- ~~Choix des technologies~~ 
- ~~Créer l’arborescence du site~~
- ~~Faire un schéma du positionnement des éléments d’une page pour chaque page (wireframe)~~
- ~~Créer repo Github pour le projet~~
- Développer le front-end :
    1. Création des éléments HTML
    2. Fonctionnalités (JS)
    3. Intégration du style CSS
- Rédiger les contenus


## Temps 2 (5,5 semaines)

<p style="text-align: center; font-size: 1.5rem;"><strong>Mon site distant</strong></p>

Pour ce deuxième POK, j'ai choisi de mon concentrer un peu plus sur le <strong>backend</strong> et sur comment mettre un site <strong>en ligne.</strong>
Déployer un site sur un serveur ovh a été partiellement vue dans le cours de "serveur distant".

L'idée du site à créer est d'avoir un feed de musiques partagées par des utilisateurs et que toute la communauté puisse voter +1/-1 pour les musiques partagées. Je vais donc me concentrer sur la partie backend et les différentes requêtes HTTP. L'objectif est aussi d'utiliser une base de données afin d'avior un site complet en ligne. 

<figure>
  <img src="../../un-site-chez-moi/AV/assets/wireframe2.png">
  <figcaption>Wireframe de l'app</figcaption>
</figure>


TODO : 
**Sprint 1**
- repo github 
- creer un front end simple Angular (libs : Bootstrap, Angular Materials, google fonts). Pages : feed, profile
- creer un backend dissocié du front (2 dossiers différents)
- creer les classes/interfaces (User, Music) et definir les différentes fonctions (sans implementation)
- définir l'architecture de la bdd
- connexion bdd (mongoDb ou postgreSQL), ORM ?
- pouvoir ajouter de nouvelles musiques

**Sprint 2**
- discuter avec l'api de Youtube par exemple pour intégrer la miniature de la musique ou même intégrer un lecteur
- pouvoir noter les musiques (j'aime ou j'aime pas)
- pouvoir ajouter aux favoris
- systeme de login avec token si possible sso (single sign-on) avec des guards (ie limiter l'accès quand on est pas connecté). Cela comprend la création de nouvelles pages (inscription/connexion)
- deployer en ligne 
- tests 



## Temps 3
