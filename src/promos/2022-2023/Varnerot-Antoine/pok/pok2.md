---
layout: layout/pok.njk

title: "POK 2"
authors:
  - Antoine Varnerot

date: 2023-01-04

tags:
  - 'temps 2'
---
<head>
  <link rel="stylesheet" href="../assets/style.css">
</head>
<p style="text-align: center; font-size: 1.5rem;"><strong>Mon site distant</strong></p>

Pour ce deuxième POK, j'ai choisi de me concentrer un peu plus sur le <strong>backend</strong> et sur "comment mettre un site <strong>en ligne.</strong>"
Déployer un site sur un serveur ovh a été partiellement vue dans le cours de "serveur distant".

L'idée du site à créer est d'avoir un feed de musiques partagées par des utilisateurs et que toute la communauté puisse voter +1/-1 pour les musiques partagées. Je vais donc me concentrer sur la partie backend et les différentes requêtes HTTP. L'objectif est aussi d'utiliser une base de données afin d'avoir un site complet en ligne.

<figure>
  <img src="../assets/wireframe2.png">
  <figcaption>Wireframe de l'app</figcaption>
</figure>

Pendant le premier sprint, j'ai créé un mono-repo pour le front et la back de mon app :

- <https://github.com/AntwanV/POK2-fullstack>
Pour visualiser le site :
<http://origan.ovh1.ec-m.fr/>
(Pas forcément avec toutes les dernières fonctionnalités)

J'ai ensuite choisi les technologies que j'allais utilisé. J'ai pris une stack très classique, la stack MEAN (MongoDb, Express, Angular, Node)
<figure>
  <img src="https://static.packt-cdn.com/products/9781789808735/graphics/C11069_01_02.jpg">
  <figcaption>Stack</figcaption>
</figure>

Plus d'informations : <https://subscription.packtpub.com/book/web-development/9781789808735/1/ch01lvl1sec03/mean-architecture-demystification>

J'ai ensuite rempli ces repos, d'abord avec un front assez simple :

<figure>
  <img src="../../assets/basic-front.png">
  <figcaption>Wireframe de l'app</figcaption>
</figure>

J'ai ensuite créé le back (avec un peu plus de difficultés). Le front est sur le port 4200 et le back sur le port 3000. Il existe à la fin de ce premier sprint qu'une seule route (/api/musics) qui permet de récupérer toutes les musiques et de les afficher dans le front. Plus précisément, comme il n'y a pas de bdd encore, je stock les musiques dans mon serveur et quand un utilisateur arrive sur la page du feed (celle de l'image ci-dessus), on fait une requête GET sur le port 3000 pour et on affiche la réponse sur la page. A l'avenir, il ne faudrait pas stocker les données sur l'API mais dans une base de données.

A la fin du sprint 1, je n'ai pas fini tout ce que j'avais listé. Peut-être parce que j'ai surestimé le temps que j'avais pour ce premier sprint. En effet, la durée de ce dernier était très réduite (environ 10 j). J'ai aussi remarqué que certaines étapes étaient plus dures que prévu : j'ai notamment eu beaucoup de problèmes pour passer mon API de Javascript à Typescript (pas encore réussi d'ailleurs)
Il y avait aussi des taches qui n'en étaient pas vraiment comme "définir l'architecture de la bdd". En fait, quand j'ai construit les objets dans mon code, les colonnes de la bdd se sont révélées toutes seules. Il en manquait bien-sur comme id mais je ne pense pas que ca méritait un tiret dans le Sprint Backlog.

TODO :
**Sprint 1**

- ~~repo github~~
- ~~choix techno~~
- ~~creer un front end simple Angular (libs : Bootstrap, Angular Materials, google fonts). Pages : feed, profile~~
- ~~creer un backend dissocié du front (2 dossiers différents)~~
- ~~creer les classes/interfaces (User, Music) et definir les différentes fonctions (sans implementation)~~
- <span style="color:orange">définir l'architecture de la bdd </span>
- <span style="color:red">connexion bdd (mongoDb ou postgreSQL), ORM ? </span>
- <span style="color:orange">pouvoir ajouter de nouvelles musiques </span>

**Sprint 2**

- discuter avec l'api de Youtube par exemple pour intégrer la miniature de la musique ou même intégrer un lecteur
- pouvoir noter les musiques (j'aime ou j'aime pas)
- systeme de login avec token si possible sso (single sign-on) avec des guards (ie limiter l'accès quand on est pas connecté). Cela comprend la création de nouvelles pages (inscription/connexion)
- deployer en ligne
- tests

Pour le second sprint, j'ai décidé de terminer d'abord les taches du premier sprint car elles étaient indispensables. Voici l aliste des taches après ce second sprint :

- ~~définir l'architecture de la bdd~~
- ~~connexion bdd (mongoDb ou postgreSQL), ORM ?~~
- ~~pouvoir ajouter de nouvelles musiques~~
- ~~discuter avec l'api de Youtube par exemple pour intégrer la miniature de la musique ou même intégrer un lecteur~~
- <span style="color:orange">pouvoir noter les musiques (j'aime ou j'aime pas)</span>
- systeme de login. Cela comprend la création de nouvelles pages (inscription/connexion)
- ~~deployer en ligne~~
- tests

Implementer l'API de Youtube pour pouvoir rechercher directement les musiques sur Youtube plutot que d'entrer toutes les informations manuellement a été une tâche qui nous a pris plus de temps que prévu. En effet, on avait mal estimé le temps nécessaire à créer un compte sur la partie "dev" de Google et de comprendre comment se servir de l'API.
Tuto qui m'a aidé : <https://blog.logrocket.com/build-a-youtube-video-search-app-with-angular-and-rxjs/>
Très complet !

Liens utils :
<https://developers.google.com/youtube>
<https://console.cloud.google.com/>
