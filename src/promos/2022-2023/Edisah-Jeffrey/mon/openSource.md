---
layout: layout/mon.njk

title: "Découverte d'une communauté Open Source avec Blender"

authors:
  - Jeffrey Edisah

date: 2023-04-05

tags:
  - 'temps 3'
  - 'info'
  - 'orga'
  - 'open-source'
---

<!-- début résumé -->

Ce dernier MON est fait pour voir l'organisation d'une communauté open source, Blender, et comment participer effectivement à cette communauté.

<!-- fin résumé -->

## Présentation de Blender 

Blender est un logiciel de création 3D open-source qui donne accès à de nombreux outils de modélisation, de sculpture, d'animation, de texturing, des moteurs de rendu graphique et plus encore. Le logiciel de par sa gratuité gagne de plus en plus en popularité actuellement chez les artistes amateurs et professionnels.

Le logiciel est également personnalisable grâce à son interface utilisateur modifiable. Les utilisateurs peuvent créer des espaces de travail spécifiques à leurs besoins et préférences et peuvent personnaliser les raccourcis clavier et les menus pour accélérer leur workflow. Il est également possible d'étendre les fonctionnalités de Blender en utilisant des add-ons créés par la communauté.

De fait, le logiciel a en plus de sa communauté d'artistes une grande communauté de développeurs qui participe au développement continu du produit, et une association, la Blender Foundation, créée par le créateur du logiciel Ton Roosendaal, qui gère les dites releases.

## Point d'entrée

Pour pouvoir participer au développement d'un projet open source, il faut avoir accès à 2 choses :

- [Le repository du projet](https://github.com/blender/blender)
- [Un forum de développeurs participant au projet](https://developer.blender.org/)
  
Le repository est nécessaire pour pouvoir effectivement coder sur le projet, run ses propres builds sur sa machine, personnaliser l'application pour un usage personnel (ou professionnel pour les Technical Directors des studios).

Le forum de développeurs est lui nécessaire pour effectivement contribuer à la communauté Blender, et travailler au développement du logiciel. Le forum donne le point d'entrée, comment run le code sur notre machine, les dépendances qu'il est nécessaire d'installer et les tickets et issues sur lesquelles il faut travailler.

J'ai essayé de run un build du code sur ma machine afin de faire des tests mais le logiciel prend beaucoup d'espace mémoire et le build a eu des bugs que je n'ai pas pu régler.

Néanmoins je peux tout de même détailler dans ce MON comment la communauté s'organise, et la démarche à suivre pour effectivement participer au développement de ce logiciel open source.

## Organisation de la communauté

La communauté de développeurs de Blender (à différencier de la communauté d'artistes Blender même si elles se rejoignent) s'organise sur un site en lien avec celui que j'ai mis précédemment. C'est sur ce site que l'on retrouve les ("issues")[https://projects.blender.org/], c'est à dire les bugs reportés, les fonctionnalités à développer, etc...

Mais comment les développeurs Blender se décident sur la suite du développement ? Avec le modèle du Benevolent Dictator.

Le modèle du Benevolent Dictator est une approche de gestion de projet open-source où un développeur unique dirige le projet. Ce développeur a le dernier mot sur les décisions concernant le projet, mais il est également attentif aux opinions de la communauté open-source qui contribue au projet. Le rôle du Benevolent Dictator est de maintenir la cohérence et la direction du projet, tout en étant ouvert aux contributions et aux idées de la communauté.

Ce modèle de gouvernance a été popularisé par des projets open-source tels que Python, où Guido van Rossum a été le "Benevolent Dictator" pendant de nombreuses années. C'est une figure importante au sein de la communauté Python et il a réussi à maintenir une direction claire pour le projet tout en étant ouvert aux contributions et aux idées des autres.

Dans le cas de Blender, Ton Roosendaal est le Benevolent Dictator en question. Ce modèle ne veut pas dire que les autres ne peuvent pas proposer d'idées, seulement que le Dictator a le dernier mot, afin de pouvoir trancher en cas de conflit. Ainsi lorsque des pulls requests, c'est à dire des demandes de modifications sont faites sur le logiciel, c'est lui qui a le dernier mot. Il ne les traite pas toutes, d'autres membres de la communauté le font aussi

Il existe d'autres types de communauté open source, Audacity par exemple, logiciel de traitement audio, fonctionnait (en tout cas jusqu'à l'année dernière avant son rachat par une entreprise) par exemple par consensus d'un groupe de devs.

## Conclusion

Au delà des considérations techniques, ce MON montre que, comme dans les entreprises, l'aspect organisationnel est primordial dans la conduite de ces projets, et il permet également de mettre en lumière d'autres types d'organisations possibles, avec des structures associatives, des développeurs bénévoles, etc...
Je pense que c'est une expérience intéressante en tant que dev de participer au développement d'un tel projet, que ce soit pour les compétences acquises, découvrir de nouvelles technologies, devenir un meilleur développeur, ou bien mettre à profit ses compétences dans des domaines qui nous intéressent.