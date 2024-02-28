---
layout: layout/pok.njk

title: "Génération procédurale de mondes"
authors:
  - Paul Vietor

date: 2024-02-14

tags: 
  - "temps 3"
  - "génération procédurale"

résumé: Dans ce POK, je m'intéresse à la génération procédurale de mondes.
---

## Objectif du projet

Pour ce projet je souhaite faire un programme permettant de générer de façon procédurale la carte d'un monde avec de multiples environnements ainsi que de l'afficher, et éventuellement de l'exporter pour l'utiliser plus tard dans d'autres programmes.

Le code source sera disponible sur [Github](https://github.com/lauravietor/WorldGen)

## Objectifs du premier sprint

- ~~Affichage d'une carte prédéfinie (3h)~~ -> Sprint 2
- Recherche, choix et implémentation des algorithmes de base : (2h)
  - Wave function collapse (3h)
  - Fonctions de bruits (Bruit simplexe, 1h)
  - Autre chose ? -> Sprint 2

## Résultats du premier sprint

Pour ce premier sprint, j'ai grandement manqué de temps dans les deux semaines allouées, donc je n'ai finalement pas eu le temps de faire l'affichage et je me suis restreint à deux algorithmes, mais j'espère continuer un peu les recherches et implémenter d'autres algorithmes pour avoir par exemple des cours d'eau.

## Objectifs pour le second sprint

- Affichage de la carte (4h)
- Changement entre vue globale et vue locale (1h)
- Génération de la hauteur du terrain et de biomes avec le bruit simplexe (2h)
- Génération de cours d'eau (3h)
- Chargement d'un ensemble de tuiles pour l'algorithme WFC (1h)
- Génération au niveau local avec WFC (2h)

Et je me garde à priori 1h pour d'éventuelles difficultés imprévues, que je compte utiliser pour implémenter un export de monde si je ne l'utilise finalement pas pour autre chose.

## Ressources

Un tutoriel pour la génération de cartes de planète avec Unity : http://www.jgallant.com/procedurally-generating-wrapping-world-maps-in-unity-csharp-part-1/
La page Wikipédia sur le bruit simplexe (en anglais) : https://en.wikipedia.org/wiki/Simplex_noise
Une vidéo Youtube sur l'algorithme Wave Function Collapse : https://youtu.be/2SuvO4Gi7uY
Une présentation par un des développeurs de Minecraft sur la génération du monde de Minecraft : https://youtu.be/ob3VwY4JyzE
Dépôt Github de WaveFunctionCollapse : https://github.com/mxgmn/WaveFunctionCollapse

