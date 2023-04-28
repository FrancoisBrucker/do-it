---
layout: layout/post.njk

title: "Working with Excel Spreadsheets"
authors:
  - Timothée Bermond

date: 2022-10-07

tags:
  - 'temps 1'
  - 'google-apps-script'
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

Il ne faut pas oublier d'utiliser la fonction *save()* afin de sauvegarder les modifications. Il est aussi préférable d'enregistrer les modifications dans une copie du tableur au cas ou il y aurait une erreur.(données corrompues...)

**Idées de programmes**
- Modifier un tableur
- Écrire des parties d'un tableur dans un autre
- Lire des données sur des sites, des textes ou sur le presse papier et les écrire dans un tableur
- Automatiquement "clean up" des données dans un tableur. (réécrire différents formats de numéros de téléphones en un seul)

## Autres fonctionnalités 

**Modifier le style de police**
Pour cela on utilise la fontion *Font()* du module *openpyxl.styles*.
Il est possible:
- de changer la police avec l'attribut *name*
- ou la taille avec l'attribut *size*
- d'écrire en gras avec l'attribut *bold*
- ou en italique avec l'attribut *italic*.

**Écrire des formules**
Il est possible d'écrire des formules exactement comme dans un Excel.

**Modifier la taille des lignes et des colonnes**
Il est possible de changer la hauteur des lignes *row_dimension[].height* et la largeur des colonnes *column_dimension[].width*.

**Fusionner ou séparer des cellules**
En utilisant les fontions *merge_cells()* ou *unmerge_cells()*.

**Figer des volets**
Afin d'avoir toujours accès à certaines lignes ou colonnes, il est possible d'utiliser l'attribut *sheet.freeze.panes = ' '*. Toutes les lignes au dessus de celle indiquée ainsi que toutes les colonnes à gauche seront figer mais pas celles indiquées.

**Créer des diagrammes**
Pour créer un diagramme, il faut suivre les étapes suivantes:
- Créer un objet *Reference* à partir d'une selection de cellules : *chart.Reference(sheet, min_col= , min_row= , max_col= , max_row=)* 
- Créer un objet *Series* qui prend l'objet *Reference* en arguement :  *chart.Series(refObj, title='')*
- Créer un objet *Chart* qui peut être un diagramme en barre, en ligne, un nuage de point ou un camembert 
- Ajouter l'objet *Series* à l'objet *Chart*
- Ajouter l'objet *Chart* à la feuille : *sheet.add_chart(chartObj, 'C5')*

## Google Apps Script

Afin de compléter ma formation et de pouvoir également travailler sur les google sheets j'ai suivi le guide [Automatiser des tâches avec Apps Script](https://developers.google.com/apps-script/guides/sheets).

**Présentation**

Comme pour *openpyxl*, Apps Script permet de créer, lire et modifier des tableurs Google Sheets. La principale différence est le langage utilisé : Apps Script utilise du code JavaScript.

Les fonctionnalités essentielles :
- Lire des données : avec les fonctions *getValue()* ou *getValues()*
- Écrire des données : avec les fonctions *setValue()* ou *setValues()*

On peut ensuite créer des fonctions qui permettent de transformer les valeurs récupérés ou d'en écrire de nouvelles. 
Différentes fonctionnalités :
- Mise en forme : [Class Range](https://developers.google.com/apps-script/reference/spreadsheet/range), permet de modifier le fond, le style de police, permet de fusionner ou de diviser des cellules, définir des règles de validation,...
- Création de graphiques : 
  *var chart = sheet.newChart()* (initialisation)
    *.setChartType()* (type de graphique)
    *.addRange(sheet.getRange())* (séléction des cellules)
    *.setPosition()* (position du graphique)
    *.build();* (construction du graphique)

  *sheet.insertChart(chart);* (insère le graphique dans la feuille de calcul)
- Macros : fonctions qui s'activent à l'aide d'un raccourci clavier
- Déclencheurs : il est possible de paramétrer les scripts afin qu'ils se déclenchent à un moment précis. Par exemple, avec les fonctions *onOpen()* ou *onEdit()*.