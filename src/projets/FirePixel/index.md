---
layout: layout/post.njk

title: "FirePixel"
authors:
  - Nicolas BERT
  - Tuncay BILGI
  - Jean-Baptiste DURAND
  - Thomas PONT

tags: ['projet']
---

<!-- début résumé -->
La pixel war centralienne organisé autour d'un écran avec comme interface d'entrée .
<!-- fin résumé -->

# [FirePixel]()

Le projet a pour but de recréer la [pixel war]() de reddit.

## Le Principe :

Un tableau de $n \times m$ pixels est partagé entre plusieurs utilisateurs. Ceux-ci peuvent modifier les couleurs des cases en chissiant parmis une sélection limitée de couleur. Le but est que plusieur utilisateurs se coordonent pour dessiner une image, ou remplacer celles des autres.

Il n'y a pas de modération automatique, mais les administrateurs se réservent le droit de supprimer des sections d'images jugées innapropriées.

## En Pratique :

Le projet sera déployé sur un écran qui pourra être posé n'importe où dans centrale, par exemple dans un lieu de pause comme à coté des distributeurs de café.

Les centraliens pourront s'approcher de l'écran et scanner un QRcode pour s'enregistrer sur l'application. Sur leur téléphone, ils peuvent chosir un pixel, une couleur, et appliquer la modification qui sera affiché en temps réel sur l'écran principal.
Le télephone devra  être connecté sur le réseau centralien.

Un compte admninistrateur permet de sélectionner des zones à effacer pour modérer l'usage de l'application.

## Stack technologique :

L'application nécéssite un Front, un Back et une base de données.
Pour la réaliser on utilise le stack suivant :

- Front-end : React.js
- Back-end : Express.js
- Base de données : MongoDB ?
- Carte RaspberryPi + écran de télé%

