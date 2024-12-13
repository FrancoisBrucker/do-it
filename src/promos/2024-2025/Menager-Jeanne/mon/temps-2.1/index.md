---
layout: layout/mon.njk

title: "Projet Numérologie"
authors:
  - Ménager Jeanne

date: 1970-11-01
tags: 
  - "temps 2"

résumé: "Je vais suivre le projet numérologie afin de découvrir les bases du développement de serveur web"
---

{% prerequis %}

Avoir quelques notions de html et javascript 

{% endprerequis %}
{% lien %}

[Projet numérologie](https://francoisbrucker.github.io/cours_informatique/cours/web/projet-numérologie/) \
[GitHub](https://github.com/jeanne-mngr/MON_2.1)

{% endlien %}

## Contenu

Ce MON a pour but de revoir les différentes étapes nécessaires à la réalisation d'un site web. 
Pour cela, j'ai suivi le projet numérologie disponible sur le site de François Brucker. 

Le but du projet est de faire un site sur lequel, l'utilisateur rentre son prénom et découvre ainsi le nombre qui lui est associé ainsi qu'une petite phrase du style horoscope liée à son numéro

Ce projet se décompose en 5 partie :
1. [Le front](https://francoisbrucker.github.io/cours_informatique/cours/web/projet-numérologie/partie-1-front/)
2. [Le back](https://francoisbrucker.github.io/cours_informatique/cours/web/projet-numérologie/partie-2-serveur/)
3. [La gestion de données](https://francoisbrucker.github.io/cours_informatique/cours/web/projet-numérologie/partie-3-données/)
4. [Rendre le code propre](https://francoisbrucker.github.io/cours_informatique/cours/web/projet-numérologie/partie-4-jardinage/)
5. [La maintenace et les tests](https://francoisbrucker.github.io/cours_informatique/cours/web/projet-numérologie/partie-5-maintenance/)

### Partie 1 : Le front
  Dans cette partie, nous avons définit l'algorithme qui nous permet d'associer à chaque chaine de caractère un chiffre. 
  On y apprend notamment à écrire **des fonctions en JS** et faire des log dans la console grâce à **console.log()**
  On crée ensuite une page en **html**, sur laquelle on rajoute du **css**.
  Enfin, on intègre la fonction en JS à la page html pour calculer le chiffre lorsque l'utilisateur clique sur 'entrée'

  Dans le niveau 2, de la gestion de projet est ajoutée mais c'est peu naturel de faire le niveau 2 après le niveau car on y définit des objectifs, déjà remplit dans le niveau 1. Si la partie gestion de projet vous intéresse je conseillerai de faire le niveau 2 directement n s'aidant du niveau 1 lorsque qu'il est nécessaire de coder

### Partie 2 : Le back

  L'objectif est de faire les calculs dans le **backend**. Pour cela on apprend dans cette partie notemment à créer une **route** en JS dans le backend puis à l'appeler dans le frontend 

### Partie 3 : La gestion de données

  Dans cette partie, nous créons une **base de données** dans laquelle nous allons associer à chaque chiffre un message.
  Nous avons ensuite créé une route **get** et plus précisement une méthode **findOne** afin de récupérer dans la base de données le message correspondant à un chiffre en particulier. 
  Nous avons ensuite apporté les modifications nécessaires au frontend pour récupérer ces informations. 

  Enfin, nous avons créé un autre modèle afin d'enregister en base les prénoms déjà demandés par l'utilisateur grâce à une méthode **create** pous pouvoir ensuite tous les afficher grâce à une méthode **getAll**

### Partie 4 : Rendre le code propre 

  Pour savoir comment rendre son **code plus propre et plus facile à maintenir**, il faut s'intéresser à cette partie du projet. 
  On a notamment séparer les routes et les modèles et différents fichiers afin de les regrouper par thème.
  Ceci permet de ne pas avoir des fichiers trop long dans lesquels il est difficile de trouver l'information que l'on cherche

### Partie 5 : La maintenace et les tests

  On y apprend la mise en place de log afin de rendre plus facile les corrections d'erreur

  Tester son projet est important aussi pour ne pas avoir de problèmes, mais le tester uniquement à la main n'est pas suffisant : en effet, on peut tester la feature que l'on rajoute et ne pas se rendre compte que sans faire exprès, on a cassé une feature qui existait déjà.

  Il existe des [tests unitaires](https://francoisbrucker.github.io/cours_informatique/cours/web/projet-numérologie/partie-5-maintenance/4-tests-unitaires/) qui vérifient (en isolation) le bon fonctionnement d'une méthode, d'un algorithme mais aussi des [tests utilisateurs](https://francoisbrucker.github.io/cours_informatique/cours/web/projet-numérologie/partie-5-maintenance/6-tests-utilisateurs/) qui sont des enchaînements de tests fonctionnels qui racontent une histoire d'un utilisateur voulant réaliser une tache sur notre application/site.

### Remarque

Le projet est un mélange d'anglais et de français, ce qui n'est pas très aggréable, j'ai essayé au fur et à mesure d'enlever les accents des mots mais je me suis retrouvée avec des erreurs car je n'étais pas consistante. Je recommande néanmoins d'essayer de passer le mots français en anglais, notamment prénom qui par son accent peut poser des problèmes.