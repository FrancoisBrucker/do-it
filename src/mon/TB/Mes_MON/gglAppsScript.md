---
layout: layout/post.njk

title: "Working with Excel Spreadsheets"
authors:
  - Timothée Bermond
---

<!-- début résumé -->
Automate the boring stuff with python : Working with Excel spreadsheets (chapter 13)
<!-- fin résumé -->

## Introduction

J'ai suivi la formation du livre [Automate the boring stuff with python](https://automatetheboringstuff.com/) et plus particulièrement le chapitre 13 [Working with Excel Spreadsheets](https://automatetheboringstuff.com/2e/chapter13/) car on est forcément amené à utiliser des tableurs dans notre vie professionelle. Savoir automatiser son utilisation afin de gagner du temps et limiter les erreurs me paraît pertinent.

## Lire un document Excel

Une méthode pour travailler sur les documents Excel est l'utilisation du module OpenPyXL (version 2.6.2 dans cette formation).

Il est ensuite possible d'importer un document excel avec la fonction *openpyxl.load_workbook()*. Ce qui permet d'accéder aux différents feuilles (sheet) du tableur ainsi qu'aux cellules de chaque feuille.

Chaque cellule a comme attribut :
- sa valeur (*value*)
- sa ligne (*row*)
- sa colonne (*column*)
- ses coordonnées (*coordinate*)

Il est donc possible de lire les données, de calculer l'occurence d'un mot, comparer les données entre différents tableurs, vérifier la présence de lignes vides ou de données invalides...

**Petit résumé** 
- Importer le module openpyxl
- Utiliser la fonction openpyxl.load_workbook()
- Choisir les feuilles qu'on veut modifier en utilisant son nom ou en choisissant la feuille active
- Utiliser les coordonnées ou la méthode *cell()* avec les lignes et les colonnes en arguments
- Lire la valeur de la cellule

## Modifier un document Excel

Il est également possible de modifier un document Excel :
- Créer un nouveau tableur vide
- Créer ou supprimer une nouvelle feuille
- Modifier le nom d'une feuille
- Créer ou modifier la valeur d'une cellule

**Idées de programmes**
- Modifier un tableur
- Écrire des parties d'un tableur dans un autre
- Lire des données sur des sites, des textes ou sur le presse papier et les écrire dans un tableur
- Automatiquement "clean up" des données dans un tableur. (réécrire différents formats de numéros de téléphones en un seul)

