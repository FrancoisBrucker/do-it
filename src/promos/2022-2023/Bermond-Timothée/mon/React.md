---
layout: layout/mon.njk

title: "React"
authors:
  - Timothée Bermond

date: 2023-04-05

tags:
  - 'temps 3'
  - 'react'
  - 'front'
  - 'librairie'
  - 'framework'
---

<!-- début résumé -->
Durant ce MON, je me suis formé aux bases de React.
<!-- fin résumé -->

## Qu'est-ce que react ?

React est une bibliothèque JavaScript open-source utilisée pour la construction d'interfaces utilisateur pour les applications web. Elle permet de construire des composants réutilisables et modulaires, qui peuvent être facilement assemblés pour créer des interfaces utilisateur complexes. React utilise également une approche de virtual DOM, où les changements d'état de l'interface utilisateur sont enregistrés dans une représentation virtuelle de l'arbre DOM, ce qui permet de minimiser les changements effectués sur le DOM réel, améliorant ainsi les performances de l'application.


## La formation que j'ai suivie

Pour ce MON j'ai suivi la [formation openclassroom](https://openclassrooms.com/fr/courses/7008001-debutez-avec-react).

Elle est très intéressante et complète pour apprendre les bases de react. De plus, elle permet de développer un projet tout au long de la formation ce qui permet de mieux assimiler toutes les informations.

Elle demande par contre d'avoir des bases en javascript, html et css.

Je conseille de passer très rapidement sur (voire de sauter) la 1ère partie (jusqu'à [Prenez en main create-react-app](https://openclassrooms.com/fr/courses/7008001-debutez-avec-react/7135204-prenez-en-main-create-react-app))

Voici un apperçu global de ce que vous pourrez apprendre dans cette formation :

## La logique de React

Quand on code en React on créé des composants que l'on va afficher dans notre application. L'avantage des composants c'est qu'ils peuvent facilement être réutiliser plusieurs fois. Par exemple, si l'on veut afficher le nom, le prix ainsi que l'année de parution d'une liste de livre, on créé un composant livre, comprenant le nom, le prix et l'année de parution que l'on va réutiliser autant de fois qu'il y a de livres.

## Créer un projet avec Create React App

Pour se faire il suffit de taper dans le terminal la commande :

```
npx create-react-app le nom de votre projet
```

Ce qui permet de générer un squelette de code (dossiers et fichiers importants) ainsi qu'un certain nombre d'outils préconfigurés afin de faciliter le développement de l'application.

## Styliser son application

Cette formation apprend également à utiliser l'attribut *className* qui permet d'ajouter un style à nos éléments dans un fichier css.

Elle montre également comment ajouter des images.

## Gagner en temps et en efficacité grâce aux listes et aux conditions

La méthode *map()* permet de traiter tous les éléments d'un tableau. Ce qui est très pratique avec react car cela offre la possibilité de transformer une liste de données en liste de composants. 

Les méthodes *forEach()*, *filter()* et *reduce()* qui permettent de manipuler des tableaux vont elles aussi nous être très utiles.

On peut également gérer des conditions afin d'afficher certaines parties du site que sous certaines conditions. Par exemple afficher le texte en rouge si une valeur est inférieure à une valeur seuil.

## Réutiliser des composants avec des props

Les props sont des objets JavaScript passés de parent à enfant via les composants. Les props permettent de passer des données statiques ou dynamiques d'un composant parent à un composant enfant.

Les props permettent de rendre les composants plus génériques et réutilisables. En passant des props différentes, le même composant peut être utilisé pour afficher des données différentes ou pour un contexte différent.

## Rendre son application interactive grâce aux événements

Un événement est une réaction à une action de l'utilisateur (clic, saisie de texte,...)

En React les événements ont une syntaxe un peu différente qu'en javascript : 
- l'événement s'écrit dans une balise en camelCase
- vous déclarez l'événement à capter, et lui passez entre accolades la fonction à appeler
- contrairement au JS, dans la quasi totalité des cas, vous n'avez pas besoin d'utiliser addEventListener.

## UseState

Il est également possible de contrôler les formulaires (accéder à la valeur de l'input). Cela permet d'interagir directement avec les données renseignées par l'utilisateur pour, par exemple, filtrer certaines données ou vérifier leur validité. Pour cela on utilise la fonction *useState* qui contient la valeur de l'input ainsi que la fonction qui permet de la modifier.

Il est également possible de transmettre ces données dans les *props* (vus plus haut). Ce qui permet permet de changer le comportement d'un composant en fonction du state d'un autre composant.

## UseEffet

Il permet d'effectuer une action à un moment donné du cycle de vie de nos composants. Par exemple, envoyer un message à chaque fois qu'un composant est modifié. Il prend deux arguments : 
- le 1er est l'action à effectuer
- le 2ème permet de décider précisement quand on veut déclencher l'effet.
