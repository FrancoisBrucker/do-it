---
layout: layout/mon.njk

title: "Titre du second MON du temps 2"
authors:
  - Lola Bourdon

date: 2023-12-15
tags: 
  - "temps 2"
  - "power BI"

résumé: "Analyse des résultats d'un google form en utilisant Power BI"
---
{%prerequis 'Bases de POwer BI'%}  
{%endprerequis%}

Ce second MON du temps 2 sera consacré à l'apprentissage de power BI en analysant les données fournies par un google form.
Pour ce mon, j'ai décidé de suivre la formation proposéé par learn.microsoft.com complémentée par le visionnage de plusieurs vidéos sur youtube.com. 


## Sommaire 

1. Introduction
2. Généralités sur PowerBI
3. Analyse de données
4. Conclusion

### Introduction

Avec la filière Entrepreneuriat, je participe aux entrep', un programme d’entraînement à l'entrepreneuriat. Dans ce cadre, je travaille sur un projet de restauration rapide. Afin de trouver notre public et définir nos personas, nous avons réalisé un google form de 32 questions qui a obtenu plus de 140 réponses. Le problème? traiter toutes les données obtenues : l'occasion idéale d'utiliser Power BI.

## Généralités sur Power BI

Power BI est une suite d'outils logiciels de Microsoft dédiée à l'analyse et à la visualisation de données. Elle permet de transformer des sources de données variées en analyses visuelles interactives. Que les données proviennent d'Excel ou d'entrepôts hybrides, Power BI offre une interface pour explorer, analyser et partager des insights de manière sélective ou publique.

méthodologie de l'exercice : 

1. Collecter
2. Transformer
3. modéliser
4. Analyser
5. Visualiser

## Analyse de données 

Afin de traiter le google form, la première étape est de récupérer les données au format csv en allant dans les réponses>télécharger au format csv.

Maintenant démarrons Power BI.

### Collecter 

Afin de collecter les données sur Power BI nous utilisons POwer Query.
Power Query est un outil d'EAI (Enterprise Application Integration) de Microsoft utilisé pour collecter, transformer et charger (ETL) des données à partir de différentes sources. Il est souvent intégré à Microsoft Excel et Power BI, mais peut également être utilisé de manière indépendante.

J'utilise Power Query pour la :

- Collecte de Données : Power Query permet de se connecter à diverses sources de données, qu'elles soient locales ou dans le cloud, telles que des bases de données, des fichiers Excel, des services en ligne, etc.
- Transformation de Données : Il offre des outils conviviaux pour nettoyer, filtrer, remodeler et transformer les données selon les besoins. Cela permet d'obtenir des données prêtes à l'emploi pour l'analyse.

collecte de donnée> sélection du fichier csv 