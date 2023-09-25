---
layout: layout/mon.njk

title: "Analyse des données sans galèR"
authors:
  - Benoit BEGUIER

date: 2023-09-17

tags: 
  - "temps 1"
  - "R"
  - "Analyse des données"
  - "RStudio"

résumé: "Initiation au langage R et application dans l'analyse et la visualisation des données."
---

{% prerequis %}
**Niveau :** débutant
**Prérequis :**
- Bases de programmation
{% endprerequis %}

## Sommaire

1. Introduction
2. Bases

## 1. Introduction
Pour la réalisation de ce cours, j'aurais deux sources principales : 
- Initiez-vous au langage R pour analyser vos données, cours dispensé sur le site openclassrooms que vous pouvez trouvez [ici](https://openclassrooms.com/fr/courses/4525256-initiez-vous-au-langage-r-pour-analyser-vos-donnees).
- La documentation officielle R pour aller plus loin accessible [ici] (https://cran.r-project.org/other-docs.html).

R est un logiciel de la famille GNU (GNU signifie "GNU's Not Unix"). Le projet GNU a été lancé en 1984 afin de développer un système d’exploitation complet, semblable à Unix, et qui soit un logiciel libre.
Je vais utiliser l'environnement de travail RStudio tout au long de cette formation puis des approfondissements. Mon but à la fin de ce MON est de pouvoir analyser et visualiser des jeux de données divers. J'espère approfondir suffisamment le langage pour analyser des données d'un sujet que je connais assez bien, le sport automobile.

## 2. Bases
#### Répertoire
Comme dans beaucoup d'environnements, il faut spécifier à RStudio le répertoire de travail avec la commande 
```shell
setwd("C:Users...")
```

#### Types d'objets
S'en suivent ensuite d'autres explications basiques sur les trois manières d'attribuer des variables, ou *objets* comme ils sont appelés dans la formation ; ainsi que la suppression des objets et l'explication sur les différents types d'objets en R. 

J'ai trouvé très intéressante la partie sur la conversion entre les types. R permet de convertir un objet en n'importe quel type, et ce même quand cela n'a pas de sens (par exemple : un nombre en type *numeric* que l'on peut convertir en booléen de type *logical*). Cette liberté peut permettre, à mon sens, des facilités de programmation utiles dans certains cas.

#### Les dataframes
Les dataframes sont des listes d'objets (appelés *composantes*), dont chaques composantes ont la même longueur. Ils sont particulièrement utiles dans l'analyse des données. J'ai appris à en créer à partir de deux listes, à partir d'une matrice et à en importer depuis un fixhier (.csv ou .txt par exemple) et aussi à les visualiser grâce à la fonction View.

## L'import de données à partir de fichiers externes
#### A partir d'un fichier texte (.txt ou .csv)
Pour lire les données d'un fichier texte externe avec R, il faut utiliser la commande
```shell
maVariable <- read.table("monFichier.txt", sep=";", row.names=1, header=TRUE)
#header indique si la première ligne contient ou non les intitulés des variables. Il est FALSE par défaut.
```

#### A partir d'un fichier quelconque
Il est aussi possible avec RStudio d'importer tous les types de fichiers en utilisant le bouton Import Dataset.

#### Gérer les erreurs d'importations
J'ai appris dans ce MOOC à détecter les erreurs d'importation (provenant du fichier source généralement), notamment avec la bonne pratique d'utiliser la fonction
```shell
summary
```
Celle-ci permet de visualiser un résumé de chaque donnée, ainsi que le nombre de type *NA*, en l'occurrence des erreurs de données.