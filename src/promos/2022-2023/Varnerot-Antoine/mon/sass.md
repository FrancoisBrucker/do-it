---
layout: layout/mon.njk

title: "Sass"
authors:
  - Antoine Varnerot
tags:
  - 'temps 2'

date: 2023-01-25

---
<head>
  <link rel="stylesheet" href="../assets/style.css">
</head>

## Description du MON

Pendant les 10h consacrées à ce MON, je veux :
- apprendre à utiliser sass
- savoir utiliser les animations css/scss


## Réalisation

1. 
Afin de pouvoir réaliser des transitions sur un site web, j'ai vite compris que c'était beaucoup plus facile de passer par un autre language que css: le sass. C'est un language très proche qui est compilé en css et qui permet l'utilisation de variables css, de fonctions, qui utilise une synthaxe plus simple à comprendre ... Timothée a d'ailleurs réalisé un MON qui traite de sass et de ces fonctionnalités (https://francoisbrucker.github.io/do-it/mon/TB/Mes_MON/CSS/). J'ai pu l'utiliser pour apréhender l'éventail des fonctionnalités de sass.
J'ai néanmoins suivi en plus le même tuto que lui pour connaître tous les détails de ce language (https://openclassrooms.com/fr/courses/6106181-simplifiez-vous-le-css-avec-sass). 

Prérequis :
- bases de HTML/CSS
- utilisation de Git/Github
Temps estimé : 5h (si on a de bonnes bases en css)

2. 
Pour apprendre comment les transitions fonctionnent en css, j'ai suivi une formation en ligne (https://openclassrooms.com/fr/courses/5919246-creez-des-animations-css-modernes).J'ai fais les deux tiers de la formation car la fin me parraissait trop complexe pour ce que je voulais faire. Cela m'a pris environ 4h.


Prérequis :
- bases de HTML/CSS
- le premier tuto ci dessus

En plus d'apprendre à coder ces transitions, on apprend des concepts très interessant d'UI :

-  les “12 principes de l’animation”.
- les timings de transitions (linear,  ease-in-out, ease-in, ease-out, cubic-bezier)
...

## Petit projet 

Pour mettre en pratique, ce que j'ai pu apprendre j'ai décidé de créer une page très simple HTML/CSS qui utilise un maximum d'animations. Même si, l'utilité de la page peut être discutable, elle me servira à m'entrainer et à créer de "belles animations"

Pour utiliser sass sans trop me casser la tête, j'ai utilisé l'extension VSCode **Live Sass Compiler** qui permet de compiler notre code sass en css sans.
L'animation consiste à afficher le texte "Do It" un peu comme le texte "Netflix" s'affiche au lancement de l'application. Cette animation se répète à l'infini.

Remarque : On voit très bien que le code est beaucoup plus long dans le fichier css que dans le fichier scss. 

Le lien vers le code est là : https://github.com/AntwanV/animCSS

