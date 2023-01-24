---
layout: layout/post.njk

title: "POK2 Cartographie d'un SI"
authors:
  - Eugénie Giraud-Telme
  - Sarah Honoré

---
<!-- début résumé -->

- Ce POK est destiné à être repris et complété. Le but est de faire un état des lieux de certaines pratiques de plusieurs organisations en termes de cartographies de Systèmes d'Information et d'essayer de cartographier une partie du SI d'une organisation.
- Niveau : intermédiaire
- Il faut avoir suivi le cours "Architecture des SI" au moins.

<!-- fin résumé -->

## Préparation du premier point POK

[Guide de cartographie des SI](./../guide-cartographie-systeme-information-anssi-pa-046.pdf)

La méthode présentée se décline en 5 étapes. Tout d'abord, il faut identifier les enjeux et les parties prenantes de la cartographie, définir le périmètre à cartographier, la cartographie cible et la trajectoire de construction. En deuxième étape, il est important de collecter et d'analyser les éléments de cartographie existants, puis définir le modèle de cartographie à partir de ces éléments existants. Ensuite, il est nécessaire de trouver un logiciel adapté de cartographie. En quatrième étape, il faut commencer par réaliser l'inventaire du SI, puis construire les vues de la cartographie. Enfin, il est important de communiquer sur la cartographie et de la maintenir à jour pour pouvoir la pérenniser.

Pour ce POK, il ne nous semble pas logique d'aller jusqu'à l'étape 5 de la pérennisation. Notre objectif est de réussir à construire une cartographie complète d'un système d'informations qui permettra de comprendre le SI.

Notre principale interrogation concerne le côté très confidentiel de la cartographie du SI d'une entreprise : les entreprises ne conservent même pas leur cartographie sur leur serveur, uniquement en format papier. Nous nous demandions donc sur quel organisme nous allions pouvoir travailler.

Nous envisageons deux scénarios pour ce POK :

- si le système à cartographier est très complexe, nous nous restreindrons à quelques vues : vue métier et vue application par exemple.
- Si le système est plus simple, nous pourrons enrichir cette cartographie avec d'autres vues et augmenter la précision des premières.

## To-do list du premier sprint
- [X] Contacter la région Sud pour savoir comment ils cartographient leur SI
- [X] Contacter la DSI de Centrale Marseille pour savoir comment ils cartographient leur SI et savoir s'il y a une partie que l'on pourrait cartographier pour eux
- [~] Chercher si il y a des anciens de Centrale qui bossent dans une DSI
- [~] Chercher les différentes méthodes de cartographie d'un SI
- [X] Définir le périmètre que l'on souhaite donner à ce POK en fonction des réponses précédentes et définir la to-do list de la deuxième partie du POK

## Détail du premier sprint
Comme notre objectif principal du premier sprint était de faire un tour d'horizon du sujet et de définir le périmètre de notre POK, nous avons surtout contacté des personnes pouvant nous aider dans notre projet. 
- Nous avons cherché les contacts d'anciens de Centrale sans les contacter pour le moment. 
- M. Bouilloux, la personne que nous avons contacté de la DSI de la Région Sud, nous a offert son aide sans problème. Eugénie pourra discuter plus précisément du sujet lors du deuxième sprint, lorsqu'elle sera en alternance. 
- Nous avons eu une réunion avec M. Pagé de la DSI le 06/12. Cette réunion nous a appris beaucoup de choses. Nous savons désormais que Centrale n'a pas de cartographie complète : seule la vue applicative a été cartographiée pour répondre aux exigences du cabinet, il s'agit d'une figure imposée d'un rapport. Le DSI pense qu'il leur serait utile d'avoir une cartographie complète pour pouvoir anticiper certains problèmes et savoir quelles parties du SI sont liées entre les différentes vues. Par exemple, elle servirait à connaître, lorsqu'un serveur est coupé, les impacts sur le SI. La raison de l'absence d'une cartographie est tout simplement le manque de ressources humaines : la DSI est composée de 8 personnes qui sont déjà très chargées. Comme les outils de cartographie sont souvent de "grosses usines à gaz", il est nécessaire d'avoir au moins une personne (un architecte ou un urbaniste) assignée à ce travail, ce qui est impossible dans le cas de Centrale.

Ce que nous nous proposons de faire dans ce POK est de mettre en place une collaboration entre la DSI de l'École et les élèves de l'option DO-IT sur plusieurs années. Comme a dit M. Pagé, si nous avions 40h mais avec déjà de l'expérience, peut-être qu'alors nous aurions pu avancer de manière significative sur la cartographie du SI de Centrale. Ainsi, nous allons regrouper les témoignages de DSIs et les différentes méthodes de cartographies au même endroit pour que, à défaut d'avoir de l'expérience, la théorie et un peu de pratique soient regroupés. Nous allons ensuite préparer la collaboration entre les parties pour la cartographie puisse être faite, améliorée et mise à jour au fil des années. Dans ce projet, il va falloir prendre en compte le fait que la DSI ne pourra pas participer au projet autrement que par des points ponctuels.

## To-do list du second sprint :
- [~] Chercher et restituer les différentes méthodes théoriques de cartographie d'un SI
- [X] Rencontrer la Région Sud
- [~] Chercher si il y a des anciens de Centrale qui bossent dans une DSI et discuter avec eux des méthodes
- [X] Restituer proprement les entretiens obtenus avec les DSI
- [X] Préparer la collaboration avec la DSI de Centrale et mettre en forme le projet pour l'année prochaine

## Compte-rendus des discussions avec les DSI de différentes entreprises
# La Région SUD
La Région Sud a environ 150 applications dans son SI. La DSI est composée de 60 ressources qui peuvent toutes être amenées à mettre à jour la cartographie. Actuellement, la Région n’a pas de schéma récapitulatif de l’ensemble du SI mais possède une application qui permet de cartographier les serveurs et une application qui correspond plus à un inventaire des applications. Un projet est en cours pour changer la manière de cartographier le SI. Le logiciel d’inventaire actuel s’appelle CASIRE et est une liste des applications, des composants du SI, des serveurs, des bases de données, etc. Dans ce logiciel, on précise les serveurs utilisés par chaque application, son hébergement, sa description et d’autres informations utiles. Il est en place à la Région depuis 10 ans et représente un travail du quotidien de mise à jour des informations. Il n’y a pas de schéma récapitulatif et les processus ne sont pas cartographiés non plus. 
Pour effectuer une bonne cartographie, M. Anigo explique qu’il faut commencer par identifier les couches, d’abord les réseaux, puis les serveurs, puis les applications, les applications métiers et enfin les processus. L’idéal est d’avoir un logiciel qui présente la cartographie au niveau applicatif service, de pouvoir dézoomer dans son contexte, et encore dézoomer pour avoir les relations avec les SI des autres services. Il faut voir les interfaces entre les applications. 

# Naver (équivalent de Google coréen)
Pour faire la cartographie, Naver (équivalent de Google coréen) utilise un logiciel de dessin gratuit : draw.io. A chaque fois qu’ils veulent remettre à jour la cartographie, c’est une seule personne qui s’en charge sur une journée. Il leur est arrivé de faire une mise à jour dans le cadre du passage à un nouvel opérateur pour les routeurs (Orange à Bouygues). Le but de leur cartographie est de savoir ce qu’il se passe lorsqu’il y a un problème, avoir un visuel pour les nouveaux arrivants et pour faciliter les changements : en somme c’est pour montrer et comprendre le SI. Leur démarche commence toujours par le niveau Internet et box, puis ils remontent les couches. Ils vont jusqu’aux adresses IP qui utilisent les applications mais ils ne cartographient pas les processus

# IMA (Institut du Monde Arabe)
Le DSI de l’IMA (Institut du Monde Arabe) nous a expliqué qu’ils réalisent la cartographie du SI globale dans le cadre de l’étude d’un schéma directeur, c’est-à-dire un plan pour engager des actions sur 3 à 5 ans. Le SI est un ensemble d’informations sur tous les acteurs de l’Institut, il est très complexe à L’IMA.
Ce schéma directeur contient les objectifs à atteindre, la démarche générale, des informations sur le champ d’actions et sur les enjeux des projets et des détails sur l’organisation de l’IMA. Ces informations permettent de mettre un contexte autour des différents projets qui vont se dérouler et d’introduire la suite. Il y a ensuite une première cartographie des SI, en effet, le SI global est divisé en plusieurs SI par type d’activité, des sous-activités sont ensuite détaillées par SI. Puis, il y a une cartographie des flux entre ces différents SI et avec l’extérieur. Cela permet de bien comprendre comment ces SI sont imbriqués et cela donne une vision générale. Une dernière cartographie est la cartographie applicative actuelle (avant le début de l’application du schéma directeur). Dans la suite du document, on peut voir détaillé tous les projets avec leurs objectifs et leurs enjeux, ainsi qu’un planning qui les place dans le temps. Le document est conclu avec une cartographie applicative cible.


## Ebauche de fiche projet
Ce projet de 3A a été construit au cours d'un POK par Eugénie Giraud-Telme et Sarah Honoré. Le projet consiste à réaliser la cartographie du système d'informations de l'Ecole, avec la collaboration ponctuelle de la DSI. Ce projet s'adresse aussi bien à des personnes intéressées par la compréhension de la structure du système d'informations de l'Ecole, qu'à des personnes intéressées par les serveurs ou la cybersécurité. Nous vous conseillons de construire une équipe avec plusieurs profils différents afin de pouvoir approfondir au maximum le sujet. 

Pour rentrer dans le sujet et comprendre quel sera l'objectif du projet, nous vous recommandons de commencer par lire le guide de la cartographie des systèmes d'informations de l'ANSSI (Agence Nationale de la Sécurité des Systèmes d'Information) pour avoir une première idée de comment se construit une cartographie. Il faudra bien évidemment chercher d'autres méthodologies de cartographie, les comparer et choisir celle qui convient le mieux à votre projet. 

To do list pour le début de ce projet :
- [ ] Trouver un organigramme à jour de l'Ecole
- [ ] Contacter chaque responsable de l'organigramme pour trouver leurs liens avec le SI et les fonctions auxquelles ils répondent. Ces entretiens sont à préparer en amont avec la DSI afin d'être sûr de poser les bonnes questions pour obtenir les informations dont vous avez besoin. Dans l'idéal, il faudrait faire les premiers entretiens avec une personne de la DSI.
- [ ] Réaliser la cartographie avec la vision métier
- [ ] Reprendre une ancienne cartographie avec la vision applicative et la mettre à jour 

La suite du projet dépend des profils des membres de l'équipe. 
Il est possible de faire une cartographie avec une vue des processus. Auquel cas nous vous recommandons d'avoir fait précédemment le MON "Diagnostic organisationnel et modélisation des processus" avec l'étude de cas CPF pour être familier avec le concept de processus et une manière de les représenter. 

