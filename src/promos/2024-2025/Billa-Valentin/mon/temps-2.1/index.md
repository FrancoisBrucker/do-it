---
layout: layout/mon.njk

title: "Haskell"
authors:
  - Valentin Billa

date: 2024-09-17

tags:
  - 'temps 2'
  - 'vert'  
  - 'débutant'
  - 'back'
  - 'programmation-fonctionnelle'
  - 'haskell'

résumé: Introduction à la programmation fonctionnelle
---

{% prerequis %}
Ce MON s’adresse à des lecteurs ayant une intérêt pour la programmation et une curiosité envers les paradigmes
alternatifs comme la programmation fonctionnelle. Aucune expérience préalable avec Haskell n’est nécessaire,
mais une compréhension de base des langages de programmation (comme Python ou Java) facilitera la lecture.
{% endprerequis %}

## Objectifs du MON

L’objectif de ce MON est de découvrir la programmation fonctionnelle à travers Haskell et d’évaluer son potentiel
dans des environnements de production. Nous chercherons à répondre à la question :
**peut-on utiliser un langage fonctionnel comme Haskell pour des applications concrètes en production ?**

Mon parcours d’apprentissage suivra les étapes suivantes :

1. Introduction aux concepts de la programmation fonctionnelle.
2. Exploration et apprentissage des bases d'Haskell.
3. Recherche de retours d’expérience sur l’utilisation d'Haskell dans des projets concrets.
4. Synthèse et réflexion critique sur les domaines d’application possibles.

## Découverte de la programmation fonctionnelle

La programmation fonctionnelle repose sur plusieurs concepts clés :

- **Fonctions pures** : des fonctions sans effets de bord, ce qui signifie que leur résultat dépend uniquement de leurs entrées.
- **Immutabilité** : une approche où les variables sont immuables, ce qui facilite le raisonnement sur le code.
- **Expressions** : tout est une expression, ce qui rend le code plus prévisible et composable.

### Exploration initiale

Pour comprendre ces idées, j’ai consulté plusieurs ressources introductives sur la programmation fonctionnelle,
notamment des articles techniques et des vidéos explicatives. Ces études m’ont permis de saisir les avantages potentiels,
comme la facilité de parallélisation et la réduction des bugs grâce à l’absence d’état mutable.

Cependant, une question persistait : pourquoi la programmation fonctionnelle, bien qu’élégante,
reste-t-elle sous-utilisée dans de nombreux environnements de production ?

## Introduction à Haskell

### Choix d’une ressource d’apprentissage

Pour trouver des ressources, [une discussion Reddit](https://www.reddit.com/r/haskell/comments/xlemih/best_resources_to_learn_haskell/)
(initiée par un utilisateur visiblement désespéré !) m'a permis de me constituer une petite bibliographie introductive.

### Premiers pas

Haskell est un langage statiquement typé, avec une syntaxe concise et un système de types très puissant.
Voici quelques concepts que j’ai découverts :

- **Les types et fonctions** : tout en Haskell est typé, et les fonctions peuvent être composées facilement.
- **Les listes** : un outil puissant pour manipuler des collections de données.

Dans l'article [What Makes Haskell Unique](https://www.snoyman.com/blog/2017/12/what-makes-haskell-unique/)
j'ai découvert quelques super concepts qui auraient été une vraie aubaine dans certains projets de dev que j'ai eu l'occassion de développer :

- **Le parallélisme avec `race`** : une fonction qui exécute deux tâches en parallèle et retourne la première à se terminer.
- **Utilisation de types** pour créer facilement des parsers.

### Installation Haskell

J'ai perdu pas mal de temps, car j'ai initialement voulu suivre un tutoriel Haskell qui ne devait pas vraiment
être prévu pour des utilisateurs sur Linux donc j'ai adapté comme je pouvais et j'ai installé des trucs qui
sont rentrés en conflit quand j'ai finalement essayé de simplement suivre la 
[documentation d'Haskell](https://www.haskell.org/get-started/) pour télécharger ce qu'il faut pour
développer en Haskell...

Ce point de ralentissement a pas mal stoppé mon élan, mais j'ai finalement suivi en partie la trame d'un MOOC
[https://haskell.mooc.fi/material/](https://haskell.mooc.fi/material/) qui était plutôt bien organisé avec pas mal
de petits exercices que j'ai résolus au fur et à mesure.

## Recherche de retours d’expérience (REX)

Après pas mal de temps passé sur le language, je me suis rendu compte que sans projet concret, il va être difficile
pour moi de répondre à ma question, j'ai donc décidé par manque de temps de plutôt partir à la
recherche de retours d'expériences.

### Applications concrètes

Pour comprendre l’utilisation d'Haskell en production,
j’ai exploré des cas d’usage concrets et analysé les avantages ainsi que les inconvénients cités dans les retours d’expérience.

### Secteurs

Haskell est utilisé dans divers secteurs où la fiabilité, la performance, et la robustesse du code sont essentielles.
Voici quelques cas d’usage notables :

- **Blockchain et crypto-monnaies** :
    - *Cardano* : une blockchain de troisième génération qui repose fortement sur Haskell pour garantir la sécurité et la robustesse de son protocole.
    - *IOHK* (Input Output Hong Kong) : développe des solutions blockchain et utilise Haskell pour concevoir des systèmes distribués fiables.

- **Finance et trading** :
    - *Standard Chartered* : cette banque internationale utilise Haskell pour concevoir des systèmes de gestion des risques et d’automatisation des calculs financiers.
    - *Tsuru Capital* : un fonds d’investissement japonais qui adopte Haskell pour ses algorithmes de trading à haute fréquence.

- **Cloud et infrastructures** :
    - *Facebook* : le langage Haskell est utilisé dans certains outils internes pour gérer la configuration et la maintenance des datacenters.
    - *GitHub* : l’outil de migration *Semantic* utilise Haskell pour analyser et transformer le code source de manière sûre et rapide.

- **Avantages** : sa sécurité typographique réduit les bugs en production, et son parallélisme natif est idéal pour traiter des charges de travail intensives.
- **Inconvénients** : la communauté est restreinte et l’écosystème moins développé que celui des langages mainstream comme Python ou JavaScript.

### Domaines d’application

En analysant ces retours, il est clair qu'Haskell excelle dans les niches où la robustesse et la précision sont prioritaires.
Cependant, son adoption reste limitée à ces cas particuliers, souvent en raison de la courbe d’apprentissage et du manque de développeurs expérimentés.

## Mise en pratique et conclusion

Malgré mes efforts, le temps consacré à ce MON n’a pas suffi pour développer un projet significatif en Haskell.
Mes programmes se sont limités à des exercices simples pour assimiler les bases.

Cependant, cet apprentissage m’a permis de répondre partiellement à ma question initiale :
**oui, Haskell peut être utilisé en production, mais principalement dans des contextes spécifiques et avec une équipe compétente dans ce paradigme.**

Pour aller plus loin, je serais tenté de réaliser un projet complet en Haskell, comme je l’ai fait précédemment avec Go.
Cela permettrait d’avoir une vision plus claire de sa robustesse et de ses limites en conditions réelles.

## Bibliographie

[1] [Learn You a Haskell for Great Good! | Miran Lipovača](https://learnyouahaskell.com/chapters)

[2] [Why Functional Programming Matters | John Hughes](https://www.cse.chalmers.se/~rjmh/Papers/whyfp.pdf)

[3] [11 Companies that use Haskell in production | Serokell](https://serokell.io/blog/top-software-written-in-haskell)

[4] Haskell Documentation [https://www.haskell.org/documentation/](https://www.haskell.org/documentation/)
