---
layout: layout/pok.njk

title: "Fiche projet 3A Cartographie d'un SI"
authors:
  - Eugénie Giraud-Telme
  - Sarah Honoré

date: 2023-01-04

tags:
  - 'temps 2'
  - 'systeme information'
  - 'cartographie'
---
<!-- début résumé -->

- Ceci est la fiche sujet d'un projet 3A pour l'année 2023-2024. Nous avons regroupé des témoignages et quelques indications en termes de cartographies de Systèmes d'Information pour permettre à des 3As d'essayer de cartographier au moins une partie du SI de l'École.
- Niveau : intermédiaire

<!-- fin résumé -->

## Fiche projet
Ce projet de 3A a été construit au cours d'un POK par Eugénie Giraud-Telme et Sarah Honoré. Le projet consiste à réaliser la cartographie du système d'informations de l'Ecole, avec la collaboration ponctuelle de la DSI. Ce projet s'adresse aussi bien à des personnes intéressées par la compréhension de la structure du système d'informations de l'Ecole, qu'à des personnes intéressées par les serveurs ou la cybersécurité. Nous vous conseillons de construire une équipe avec plusieurs profils différents afin de pouvoir approfondir au maximum le sujet. 

Pour comprendre comment s'est déroulé notre POK, cliquez ici : [Préparation POK](../pok_2_prep).

Pour entrer dans le sujet et comprendre quel sera l'objectif du projet, nous vous recommandons de commencer par lire le [guide de la cartographie des systèmes d'informations de l'ANSSI](./../guide-cartographie-systeme-information-anssi-pa-046.pdf) (Agence Nationale de la Sécurité des Systèmes d'Information) pour avoir une première idée de comment se construit une cartographie. Il faudra bien évidemment chercher d'autres méthodologies de cartographie, les comparer et choisir celle qui convient le mieux à votre projet. Nous avons pu interviewer des personnes travaillant dans des DSI d'entreprise pour connaître la démarche qu'ils adoptent lorsqu'ils font une cartographie, quels outils ils utilisent, combien de temps et de ressources ils y allouent, à quoi leur sert cette cartographie, quelle est sa nature (applicative, des flux, des processus, infrastructure, etc.). Toutes ces informations sont regroupées dans les comptes-rendus de discussions plus bas.

*To do list très large pour le début de ce projet* :
- [ ] Trouver un organigramme à jour de l'École
- [ ] Contacter chaque responsable de l'organigramme pour trouver leurs liens avec le SI et les fonctions auxquelles ils répondent. Ces entretiens sont à préparer en amont avec la DSI afin d'être sûr de poser les bonnes questions pour obtenir les informations dont vous avez besoin. Dans l'idéal, il faudrait faire les premiers entretiens avec une personne de la DSI.
- [ ] Réaliser la cartographie avec la vision métier
- [ ] Reprendre une ancienne cartographie avec la vision applicative et la mettre à jour 

La suite du projet dépend des profils des membres de l'équipe, en effet, chacun peut avoir un intérêt différent pour chaque aspect d'une cartographie. 
Pour mener à bien ce projet, vous serez évidemment amenés à travailler avec M. Pagé, le directeur de la DSI de Centrale. Il n'aura pas le temps de vous accompagner hebdomadairement mais saura vous éclairer quant aux besoins de la DSI.
Il est possible de faire une cartographie avec une vue des processus. Auquel cas nous vous recommandons d'avoir fait précédemment le MON "Diagnostic organisationnel et modélisation des processus" avec l'étude de cas CPF pour être familier avec le concept de processus et une manière de les représenter. Nous sommes trois à l'avoir réalisé l'année dernière, vous trouverez nos MON [ici](../../../mon/SH/MON1-1/), [ici](../../../mon/EGT/MON_1_2) et [là](../../../mon/KR/MON1-2). La vue des processus s'adresse à des personnes qui cherchent à comprendre comment une information transite à travers différentes personnes et ce qu'une décision peut impliquer. 
Si certains étudiants sont intéressés par le réseau et les serveurs ou la cybersécurité, il est intéressant de réaliser une vue des infrastructures logiques ou physiques.  

Suivant l'intérêt porté à chaque vue, il est possible de rentrer plus ou moins dans le détail. Le projet pourra donc être repris l'année d'après pour être poursuivi et complété avec un niveau de détails plus important.

## Compte-rendus des discussions avec les DSI de différentes entreprises
# Centrale Marseille
Nous avons eu une réunion avec M. Pagé de la DSI le 06/12. Cette réunion nous a appris beaucoup de choses. Nous savons désormais que Centrale n'a pas de cartographie complète : seule la vue applicative a été cartographiée pour répondre aux exigences du cabinet, il s'agit d'une figure imposée d'un rapport. Le DSI pense qu'il leur serait utile d'avoir une cartographie complète pour pouvoir anticiper certains problèmes et savoir quelles parties du SI sont liées entre les différentes vues. Par exemple, elle servirait à connaître, lorsqu'un serveur est coupé, les impacts sur le SI. La raison de l'absence d'une cartographie est tout simplement le manque de ressources humaines : la DSI est composée de 8 personnes qui sont déjà très chargées. Comme les outils de cartographie sont souvent de "grosses usines à gaz", il est nécessaire d'avoir au moins une personne (un architecte ou un urbaniste) assignée à ce travail, ce qui est impossible dans le cas de Centrale.

# La Région SUD
La Région Sud a environ 150 applications dans son SI. La DSI est composée de 60 ressources qui peuvent toutes être amenées à mettre à jour la cartographie. Actuellement, la Région n’a pas de schéma récapitulatif de l’ensemble du SI mais possède une application qui permet de cartographier les serveurs et une application qui correspond plus à un inventaire des applications. Un projet est en cours pour changer la manière de cartographier le SI. Le logiciel d’inventaire actuel s’appelle CASIRE et est une liste des applications, des composants du SI, des serveurs, des bases de données, etc. Dans ce logiciel, on précise les serveurs utilisés par chaque application, son hébergement, sa description et d’autres informations utiles. Il est en place à la Région depuis 10 ans et représente un travail du quotidien de mise à jour des informations. Il n’y a pas de schéma récapitulatif et les processus ne sont pas cartographiés non plus. 
Pour effectuer une bonne cartographie, M. Anigo explique qu’il faut commencer par identifier les couches, d’abord les réseaux, puis les serveurs, puis les applications, les applications métiers et enfin les processus. L’idéal est d’avoir un logiciel qui présente la cartographie au niveau applicatif service, de pouvoir dézoomer dans son contexte, et encore dézoomer pour avoir les relations avec les SI des autres services. Il faut voir les interfaces entre les applications. 

# Naver (équivalent de Google coréen)
Pour faire la cartographie, Naver (équivalent de Google coréen) utilise un logiciel de dessin gratuit : draw.io. A chaque fois qu’ils veulent remettre à jour la cartographie, c’est une seule personne qui s’en charge sur une journée. Il leur est arrivé de faire une mise à jour dans le cadre du passage à un nouvel opérateur pour les routeurs (Orange à Bouygues). Le but de leur cartographie est de savoir ce qu’il se passe lorsqu’il y a un problème, avoir un visuel pour les nouveaux arrivants et pour faciliter les changements : en somme c’est pour montrer et comprendre le SI. Leur démarche commence toujours par le niveau Internet et box, puis ils remontent les couches. Ils vont jusqu’aux adresses IP qui utilisent les applications mais ils ne cartographient pas les processus

# IMA (Institut du Monde Arabe)
Le DSI de l’IMA (Institut du Monde Arabe, institut public financé par l'État) nous a expliqué qu’ils réalisent la cartographie du SI globale dans le cadre de l’étude d’un schéma directeur, c’est-à-dire un plan pour engager des actions sur 3 à 5 ans. Le SI est un ensemble d’informations sur tous les acteurs de l’Institut, il est très complexe à L’IMA.
Ce schéma directeur contient les objectifs à atteindre, la démarche générale, des informations sur le champ d’actions et sur les enjeux des projets et des détails sur l’organisation de l’IMA. Ces informations permettent de mettre un contexte autour des différents projets qui vont se dérouler et d’introduire la suite. Il y a ensuite une première cartographie des SI, en effet, le SI global est divisé en plusieurs SI par type d’activité, des sous-activités sont ensuite détaillées par SI. Puis, il y a une cartographie des flux entre ces différents SI et avec l’extérieur. Cela permet de bien comprendre comment ces SI sont imbriqués et cela donne une vision générale. Une dernière cartographie est la cartographie applicative actuelle (avant le début de l’application du schéma directeur). Dans la suite du document, on peut voir détaillé tous les projets avec leurs objectifs et leurs enjeux, ainsi qu’un planning qui les place dans le temps. Le document est conclu avec une cartographie applicative cible.


