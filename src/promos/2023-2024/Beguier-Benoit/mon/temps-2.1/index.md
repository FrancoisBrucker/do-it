---
layout: layout/mon.njk

title: "Reprise des bases de Python + Petite exploration de Seaborn"
authors:
  - Benoit BEGUIER

date: 2023-12-13
tags: 
  - "temps 2"
  - "python"
  - "piton"
  - "pyton"
  - "Seaborn"
  - "visualisation"
  - "plot"

résumé: "Le but de ce MON est de reprendre les bases d'algorithmique en Python, puis de s'initier au package Seaborn permettant de plot des jolis graphiques"
---

{% prerequis %}

**Niveau :** Intermédiaire
**Prérequis :**
- Bases de Python

{% endprerequis %}


## Sommaire
1. Introduction
2. Remise au niveau intermédiaire sur Python
3. pprentissage de la bibliothèque Seaborn
4. Mise en pratique en reprenant l'exemple du MON 1.1

## Introduction

Pour la réalisation de ce cours, je me réfèrerais aux sources listées ci-dessous : 
- *Python Tutorial*, W3 Schools. Accessible [ici](https://www.w3schools.com/python/).
- *Coder en Python*, François Brucker. Accessible [ici](https://francoisbrucker.github.io/cours_informatique/cours/coder-en-python/)
- *Le tutoriel Python*. Accessible[ici](https://docs.python.org/fr/3/tutorial/index.html)

## Remise au niveau intermédiaire sur Python

#### Exercices de décrassage (2 heures)

J'ai débuté ce MON en effectuant un grand nombre d'exercices Python sur le site W3 Schools, cité dans mes références. Ce site propose un peu moins de 5 exercices sur les différents aspect essentiels du langage, tels que :
- la syntaxe
- les variables
- les data types : string, boolean, number, integer, dictionnaries, ...
- les opérateurs
- les listes
- les tuples
- les boucles
- les fonctions
- les classes

Ces exercices représentaient selon moi le meilleur moyen de me remettre dans la syntaxe Python. Bien que Python soit assez intutif, certains mots-clés m'échappaient (*dir*, *break*, *continue*, ...). Les exercices sont d'abord très simples ce qui permet de se refaire la main, puis ils se corsent (très légèrement) pour aborder quelques détails, commandes et méthodes. J'ai aussi consulté en profondeur la documentation sur les listes car j'utilise fréquemment ce type d'objets.
Je recommande à tous de faire ces exercices. Ils m'ont pris deux heures, car j'ai systématiquement survolé la documentation des types et des commandes que je maîtrisais mal.

![W3](W3.png)


#### Échauffement (2 heures 30)

J'ai ensuite effectué le cours de Python de M. Brucker accessible [ici](https://francoisbrucker.github.io/cours_informatique/cours/coder-en-python/). Je me suis attardé sur les parties Variables, Fonctions, Listes et Notebook.
Je retiens notamment la partie sur les listes en compréhension (dont la documentation est disponible [ici](https://docs.python.org/fr/3/tutorial/datastructures.html#list-comprehensions)), les arrays (dont la documentation est disponible [ici](https://numpy.org/doc/stable/reference/generated/numpy.array.html)), les Notebook et la partie *Pour aller plus loin*.
J'ai effectué l'ensemble des exercices proposés par M. Brucker sur les pages que j'ai consulté, afin de reprendre rapidement la main sur tous les types.

J'ai ensuite suivi le tutoriel Python (encore recommandé par Brucker) qui est disponible [ici](https://docs.python.org/fr/3/tutorial/index.html). Celui-ci étant très long, j'ai sélectionné uniquement les parties qui m'intéressaient : 
- [10.6. Mathématiques](https://docs.python.org/fr/3/tutorial/stdlib.html#mathematics)
- [12.2. Création d'environnements virtuels](https://docs.python.org/fr/3/tutorial/venv.html#creating-virtual-environments)
- [12.3. Gestion des paquets avec pip](https://docs.python.org/fr/3/tutorial/venv.html#managing-packages-with-pip) histoire de consolider le cours de DevWeb du temps 2.

Enfin, j'ai lu la documentation du mot-clé *case* accessible [ici](https://docs.python.org/fr/dev/reference/compound_stmts.html) car je n'étais plus certain de son utilisation.

## Apprentissage de la bibliothèque Seaborn
