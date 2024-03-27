---
layout: layout/projet.njk

title: "Tu tires ou tu pointes? La version mobile du jeu Chiche ou Pois Chiche"
authors:
  - Duc DANG VU
  - Sarah SEBASTIEN
  - Samy DIAFAT
---

### Sommaire

- [Contexte et objectifs du projet](#contexte)
- [Comparaison avec le jeu papier](#papier)
- ["Tech stack" ou stack technique](#stacktechnique)
- [Organisation](#organisation)
- [Résultats et livrables](#resultat)
- [Apprentissage et retour d'expérience](#apprentissage)
- [Capitalisation et suite à donner](#capitalisation)

<h2 id=contexte> Contexte et objectifs du projet</h2>

<h2 id=papier> Comparaison avec le jeu papier</h2>

<h2 id=stacktechnique> "Tech stack" ou stack technique</h2>

<h2 id=organisation> Organisation</h2>

<h2 id=resultat> Résultats et livrables</h2>

### Maquette Figma

Comme la réussite de notre jeu résidait en grande partie à la réussite de **l'expérience utilisateur** de nos joueurs, il nous fallait nous appliquer particulièrement dans le design de notre interface.

Nous avions obtenu une première version à la fin des **cours d'UX design**, qui ressemblait à ceci : 

<img width=500 src=maquette1.png>


Mais lors du cours d'**UI**, plus centré sur le **design visuel**, il nous a été reproché que notre design ne faisait pas assez *jeu*. En voulant nous adresser à un public *large*, plutôt que de choisir un *persona*, nous n'arrivions pas à nous décider sur des choix visuels précis.

Nous avons alors décidé de refaire toute la démarche, de définir un persona précis qui soit un jeune de notre âge, et de créer un *Moodboard*. Nous avons choisi de nous inspirer d'un jeu mobile sur le même principe que nous (ie qui se jouait sur un seul téléphone), et s'adressant aux jeunes : **l’imposteur**.

<img width=500 src=imposteur.png>

Nous avons alors analysé ce qu'il manquait à notre maquette essentiellement : des **images/icônes**, des **couleurs**, et un **logo** qui correspondait à l'univers du jeu. 

Alors on a tenté de retravailler : 
- notre logo

|---|---|
|<img width=300 src=logo1_1.png> | <img width=300 src=logo1_2.png>|
|<img width=300 src=logo2_1.png> | <img width=300 src=logo2_2.png>|

- notre maquette

<img width=500 src=maquette2.png>

Mais c'était très dur pour nous de nous défaire de notre idée de départ. Alors on s'est finalement dirigé vers une alternative de notre première idée :

<img width=500 src=maquette3.png>

{%faire%}
**[Lien vers le preview Figma](https://www.figma.com/proto/qpd6RRPLzQF2yXglJ3bFc3/Interface-application?type=design&node-id=42-93&t=i522PIOTavWnt3Og-1&scaling=scale-down&page-id=0%3A1&starting-point-node-id=71%3A561&show-proto-sidebar=1&mode=design)**
{%endfaire%}


### Poster 

Nous avons également présenté notre application lors de l'après- midi de présentation des projets 3A aux anciens de Do-It ainsi qu’aux élèves intéressés. Voici le poster que nous avons réalisé pour expliquer le concept, la planification et l’avancement du projet : 

<img width=500 src=poster.png>

### Application Bubble

Malheureusement l'option de déployer une application avec Bubble est *payante*. Mais vous trouverez ici une courte vidéo de présentation de l'application :



<video width="400" height="200" controls> <source src="demo.mp4" type="video/mp4"></video> 


Et voici le lien vers un preview de notre application [ici](https://duc15dangvu.bubbleapps.io/version-test/page_de_connexion), avec lequel vous pourrez jouer !

### Base de données Airtable

Pour la base de données, comme expliqué plus tôt, nous l'avons gérée avec Airtable.
Elle contient donc les informations complémentaires à Bubble, c'est-à-dire l’ensemble des données liées aux questions. Il y  **234 questions différentes aujourd'hui** dans la table. Au total, **200** proviennent des questions du jeu de cartes initial, et nous en avons ajouté **34** que nous avons créés sur les thèmes **Histoire** et **Sciences**.

<h2 id=apprentissage> Apprentissage et retour d'expérience</h2>

<h2 id=capitalisation> Capitalisation et suite à donner</h2>







## Introduction

Ce projet a pour but de créer une version mobile du jeu de cartes “Chiche ou Pois Chiche”. Après plusieurs parties, on retombe rapidement sur les mêmes questions et le jeu devient vite obsolète pour un joueur une fois qu’il a rencontré toutes les questions et connaît toutes les réponses. Notre idée serait donc de créer une version mobile du jeu pour pouvoir alimenter la base de données et ainsi offrir aux fervents joueurs de “Chiche ou pois Chiche”, de pouvoir y jouer indéfiniment. De plus, une application mobile serait un moyen d'accroître la visibilité du jeu.

![Image jeu](Image1.jpg)

Le but du jeu est de gagner le plus de points en posant les bonnes questions à son ou ses partenaire de jeu. On forme plusieurs équipes de 2 minimum. Pour chaque question le joueur lit l'indice à son partenaire puis lui demande "Chiche ou Pois Chiche ?". Il répond "Chiche" s'il pense pouvoir répondre à la question sans proposition de réponse ou "Pois Chiche" s'il souhaite les 4 propositions. Si la réponse donnée est correcte l'équipe récupère une "Carte Chiche" (3 points) ou une "Carte Pois Chiche" (1 point) selon l'annonce faite précédemment.
Le jeu possède 8 catégories de questions pour permettre à tout le monde d’avoir des points forts et des faiblesses. ("Sport", "Culture G", "Petits écrans", "Grand écran", "Voyage", “Musique", "Bouffe")

## Fonctionnalités

Voici une première liste de fonctionnalités que nous voulons implémenter sur l'application:

- La gestion d'un compte utilisateur
- Lancer un dé pour déterminer le type de tour
- Pouvoir rejoindre un salon avec les autres participants (mode en ligne? bluetooth?)
- Tirer aléatoirement une question
- Comptage de points
- Afficher la réponse à une question sur demande de l'utilisateur

## Planification du projet

Nous avons réalisé une feuille de route pour notre projet, qui consiste en quelques étapes que nous devrons réaliser au fur et à mesure de notre avancement:

- Faire des maquettes de l'apparence graphique générale du jeu (sur Canva ou autres)
  - Quelle charte graphique pour l'application?
  - Quelle expérience utilisateur?
- Réfléchir sur les fonctionnalités de l’application
  - Quelles règles établir? Ajout de règles?
- Elaboration d’un premier prototype sur Figma
  - Apprentissage et prise en main de l'outil
- Première version en no code sur Bubble.io
  - Création d'une première base de donnée de questions sur Bubble (ou autre) avec les questions du jeu
  - Création de l'interface utilisateur
- Recueil d’un grand nombre de questions et de réponses
- Test et retours d’expérience auprès de plusieurs utilisateurs
- Améliorations sur le jeu suite aux remarques soulevées
- Possible migration (NiceGui sur Python)?
