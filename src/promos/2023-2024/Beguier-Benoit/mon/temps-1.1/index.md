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
  - "mon"

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
Pour la réalisation de ce cours, j'aurais une source principale : 
- Initiez-vous au langage R pour analyser vos données, cours dispensé sur le site openclassrooms que vous pouvez trouvez [ici](https://openclassrooms.com/fr/courses/4525256-initiez-vous-au-langage-r-pour-analyser-vos-donnees).

R est un logiciel de la famille GNU (GNU signifie "GNU's Not Unix"). Le projet GNU a été lancé en 1984 afin de développer un système d’exploitation complet, semblable à Unix, et qui soit un logiciel libre.
Je vais utiliser l'environnement de travail RStudio tout au long de cette formation puis des approfondissements. Mon but à la fin de ce MON est de pouvoir analyser et visualiser des jeux de données divers. J'espère approfondir suffisamment pour analyser des données d'un sujet que je connais assez bien, le spor automobile.

## 2. Bases
#### Répertoire
Comme dans beaucoup d'environnements, il faut spécifier le répertoire de travail avec la commande 
```html
setwd("C:Users...")
```