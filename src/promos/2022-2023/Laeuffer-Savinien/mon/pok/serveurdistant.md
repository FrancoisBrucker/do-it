---
layout: layout/pok.njk

title: "Backend & Serveur distant"
authors:
  - Savinien Laeuffer

date: 2023-01-04

tags:
  - 'temps 2'
---

<!-- début résumé -->
Backend & déploiement sur un serveur distant
<!-- fin résumé -->

## Description du projet

Ce projet vise à remplacer mon groupe messenger avec mes amis sur lequel on envoie des musiques peu connues chaque jour, par une application web avec des fonctionnalités supplémentaires qui répertorie tous les envois plus facilement.

Ce temps 2 va donc être consacré à la création de cette application web de gestion de musiques en ligne. L'utilisateur peut ajouter des musiques à l'application à partir de liens YouTube ou Soundcloud, il en rentre les informations nécessaire à la bonne identification de la musique (Artiste, titre, lien, album, label, genre), celle-ci s'ajoute à sa collection et apparait dans le feed général que tout le monde peut consulter.
Chaque utilisateur peut ajouter une musique à ses favoris et voter pour une musique si il le juge nécessaire.

## Plan du POK

1. **Front-End**

La première partie de ce POK est évidemment de mettre en place le côté front-end de l'application.
Pour cela nous utiliserons le framework Angular (HTML/CSS/JS et la librarie Bootstrap) que nous avons étudié au temps 1.

Les composants principaux à implémenter seront:
- Le feed principal avec les musiques les plus récentes en premier
- Sur chaque musique, afficher un player YouTube ou Soundcloud, la possibilité de voter pour la musique et de l'ajouter aux favoris.
- Une navbar avec des boutons de connexion et d'inscription
- Une page d'inscription et de connexion
- Une page "Mon Profil" avec la liste des musiques likées

Voici un aperçu de ce que l'on souhaite pour l'UI:

<div style="width:100%;">
  <figure style="text-align:center">
    <img style="height:600px; margin-left: auto; margin-right: auto" src="../uiwireframe.png">
    <figcaption>Wireframe de l'application</figcaption>
  </figure>
</div>

Le but est de ne pas trop tarder sur cette partie afin de passer la majorité du temps disponible sur les parties suivantes. D'où l'utilisation de Bootstrap qui nous permettra d'être rapide et efficace pour l'UI.

Ressources pour cette partie:
- [POK1](./monsite.md)
- [Documentation Angular](https://angular.io/docs)
- [W3School](https://www.w3schools.com/)
- [Documentation Bootstrap](https://getbootstrap.com/docs/4.1/getting-started/introduction/)

2. **Back-End**

La seconde partie va être de créer tout ce qui est back-end et de l'associer au front-end. Il va donc falloir créer les différentes classes/interfaces dont on aura besoin (Users et Music) et définir les fonctions "voter", "aimer" etc.

Ensuite, il va falloir définir l'architecture de la base de données, quels attributs et méthodes chaque classe va contenir puis installer une base de données et établir les premières connexions entre celle-ci et l'application.

Nous nous foncaliseront d'abord sur le système de login/sign-in avec token, si possible SSO (Single Sign-on) avec des guards (ie. limiter l'accès aux URL quand on est pas connecté). Cela comprend aussi un peu de front-end, notamment pour les fenêtres de connection, les routing entre les différentes pages, les erreurs à afficher etc.

Une fois la gestion d'utilisateur terminée, il faudra s'occuper de la gestion des musiques. Il faut implémenter la possibilité d'ajouter des musiques, de les supprimer pour l'utilisateur qui l'a publiée, de voter, de l'ajouter à sa collection de titres aimés, et que tout cela se répercute dans la base de donnée.

Une des dernières étapes est de gérer le système de feed de la page principale. Discuter avec les API YouTube et Soundcloud afin d'incorporer les players ou les miniatures.

Ressources pour cette partie:
- [Documentation MongoDB](https://www.mongodb.com/docs/)
- [Documentation Express](https://expressjs.com/fr/starter/installing.html)

3. **Déploiement**

Finalement, il faudra déployer notre application sur un serveur distant.

## Découpage en sprints


TODO : 


**Sprint 1**
- repo github 
- creer un front end simple Angular (libs : Bootstrap, Angular Materials, google fonts). Pages : feed, profile
- creer un backend dissocié du front (2 dossiers différents)
- creer les classes/interfaces (User, Music) et definir les différentes fonctions (sans implementation)
- définir l'architecture de la bdd
- connexion bdd (mongoDb ou postgreSQL)
- pouvoir ajouter de nouvelles musiques

**Sprint 2**
- discuter avec l'api de Youtube par exemple pour intégrer la miniature de la musique ou même intégrer un lecteur
- pouvoir noter les musiques (j'aime ou j'aime pas)
- pouvoir ajouter aux favoris
- systeme de login avec token si possible sso (single sign-on) avec des guards (ie limiter l'accès quand on est pas connecté). Cela comprend la création de nouvelles pages (inscription/connexion)
- deployer en ligne 
- tests
