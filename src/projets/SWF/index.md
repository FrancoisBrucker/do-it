---
layout: layout/post.njk

title: "Street Workout Finder"
authors:
  - Thibault Adelain
  - Thomas Duroy
  - Jeffrey Edisah
  - Kasimir Romer

tags: [projet]
---
<!-- début résumé -->
Le projet pour trouver des installations sportives en plein air près de chez vous !
<!-- fin résumé -->

## Objectif

L'objectif du projet est le développement d'une application de géolocalisation d'installations sportives en extérieur (barres de tractions, barres parallèles, etc..) dans la ville de Marseille. La conception de l'application se fait dans une démarche Design Thinking.

## Déroulé 

<<<<<<< HEAD
### Octobre-Novembre

Le but de cette période est d'arriver à un **Minimum Viable Product (MVP)** à travers le maquettage sur Figma et les interviews des potentiels utilisateurs. Ce temps est aussi dédié à l'établissement de l'état de l'art, et à la délimitation d'un business model. Une fois ces objectifs atteints, nous nous lancerons dans le développement.

### Décembre-Janvier

Nous sommes actuellement en train de nous décider sur l'archtecture de notre application, et hésitons entre une application classique avec un front, un back et une base de données et des micros services.
Une fois cette décision prise, nous commencerons à développer l'application.

## Planning des sprint

=======
>>>>>>> 2d95b9b06edadc41bd8019c8d2acdeb49597282b
### Phase de réflection, Design Thinking

**19/09/2022 - 05/12/2022**
<<<<<<< HEAD
Dans la phase de réflexion, nous allons nous concentrer sur les étapes suivantes :

=======
Dans la phase de réflexion, nous nous sommes concentrés sur les étapes suivantes :
>>>>>>> 2d95b9b06edadc41bd8019c8d2acdeb49597282b
- Recherche des besoins utilisateurs (avec des entretiens)
- Recherche de l'état de l'art
- Création du design dans Figma
- Création de l'architecture de l'application (on a décidé d'utiliser une architecture en microservices)

### Sprint 1

**06/12/2022 - 03/01/2023**

Dans le premier sprint, nous avons réalisé les étapes suivantes :
[x] Création du repo GitHub : https://github.com/JeffreyEdisah/Street-Workout-Finder
[x] Création microservice utilisateur et authentification
[x] Début du développement du microservice lieux

Nous avons crée un projet sur GitHub: 

### Sprint 2
<<<<<<< HEAD
=======
**03/01/2023 - 07/02/2023**
>>>>>>> 2d95b9b06edadc41bd8019c8d2acdeb49597282b

**04/01/2023 - x**
Dans le deuxième sprint, nous avons réalisé les étapes suivantes :
[x] Finir le microservice lieux
[x] Déploiement du microservice lieux sur AWS Lambda

### Sprint 3
**07/02/2023 - 28/02/2023**

Dans le troisième sprint, nous avons réalisé les étapes suivantes :
[x] Début du travail sur le front en React
[x] Création de la carte avec Leaflet
[x] Ajout des pages Login et Register
[x] Ajout de la page de description d'un lieu

### Sprint 4
**28/02/2023 - 21/03/2023**

Dans le quatrième sprint, nous avons réalisé les étapes suivantes :
[x] Refactoring du microservice lieux
[x] Ajout du menu à la carte
[x] Liaison du front avec les différents microservices
[x] Ajout d'une gateway entre le microservice lieu et le microservice utilisateurs

### Sprint 5
**28/02/2023 - 21/03/2023**

Dans le quatrième sprint, nous avons réalisé les étapes suivantes :
[x] Divers ajustements CSS
[x] Création d'un docker compose avec 3 services : le front, le microservice lieu et le microservice utilisateurs

## Poster

![SWF_Poster](SWF_Poster.png)

### X-Bilan et futures fonctionnalités

#### X.1-Bilan

Le développement d'une application web est un projet qui peut être très enrichissant d'un point de vue professionnel et personnel. Dans ce projet, nousa avons eu l'opportunité de travailler sur différentes technologies et outils, ce qui nous a permis d'acquérir une expérience précieuse en développement web. Nous avons également développé des compétences en gestion de projet, en résolution de problèmes et en communication. Au-delà de ces compétences techniques, le projet a également permis aux membres de l'équipe de développer leur créativité et leur capacité à collaborer avec des personnes ayant des compétences différentes.

Dans l'ensemble, le projet a permis à tous, à notre échelle personnelle de progresser en développement web. Que ce soit dans la façon de structurer une application ou dans la prise en main de nouveau outils et framework nécessaires à la progression du projet. Nous avons tous éprouvé et amélioré nos capacités.

#### X.2-Futures fonctionnalités

Bien que nous soyons fiers de ce que nous avons accompli avec l'application web, il y a certaines fonctionnalités que nous aurions aimé pouvoir ajouter si le temps et les ressources nous avaient permis. Ces améliorations pourraient inclure :

- Recherche par équipement présents sur le lieu : Nous pourrions intégrer une fonctionnalité de recherche qui permettrait aux utilisateurs de trouver des lieux en fonction des équipements qu'ils offrent..

- Aspect communauté avec ajout de commentaires : Il serait intéressant d'ajouter une section commentaires à l'application pour permettre aux utilisateurs de partager leur expérience, poser des questions et interagir entre eux.

- Ajout d'équipements sur les lieux avec des tags : Nous pourrions permettre aux utilisateurs de suggérer de nouveaux équipements pour les lieux et de les taguer, afin que les autres utilisateurs puissent les trouver plus facilement.

- Mise en place d'utilisateurs clés pour vérifier la véracité des ajouts : Pour assurer la qualité des informations de notre application, nous pourrions mettre en place un système de vérification pour les ajouts suggérés par les utilisateurs. Ces utilisateurs clés pourraient être responsables de valider ou de rejeter les ajouts proposés.

- Déploiement sur le cloud : Il serait bénéfique de déployer notre application sur le cloud, car cela permettrait d'assurer une disponibilité en ligne 24/7 et une meilleure performance pour les utilisateurs.

- Remplacement des images "placeholder" par des images correspondant au lieu : Nous pourrions remplacer les images par défaut par des images réelles des différents lieux, pour une expérience utilisateur plus personnalisée et plus engageante.

- Ajout d'un bouton itinéraire : Il serait utile d'ajouter un bouton itinéraire pour que les utilisateurs puissent trouver facilement leur chemin vers les différents lieux répertoriés sur notre application.
  
En somme, nous sommes conscients qu'il y a encore des améliorations à apporter à notre application, et les intégrer à l'avenir afin permettrait de garantir la satisfaction de nos utilisateurs.
