---
layout: layout/mon.njk

title: "MON 2 : Utilisation d'Excel dans l'analyse de données"
authors:
  - Lucie Le Boursicaud

date: 1970-10-01
tags: 
  - "temps 1"
  - "Excel"
  - "Analyse des données"

résumé: "Dans ce MON l'objectif est d'apprendre à utiliser Excel dans le but d'analyser des données."
---
{%prerequis 'Niveau débutant'%} 
Aucun prérequis
{%endprerequis%}

## Introduction
Au sein de mon entreprise d'alternance beaucoup de fichiers Excel sont utilisés dans tous les services afin de faire du suivi de tâches, de réaliser des processus de relevé de prix ou encore d'analyser des données... Mon rôle en tant qu'alternante en digitalisation est de minimiser au maximum l'utilisation d'Excel en utilisant des applications collaboratives, nottament [Power BI](https://powerbi.microsoft.com/fr-fr/what-is-power-bi/) issus de la suite de Microsoft pour l'analyse des données. Je trouve donc pertinent de comprendre comment Excel fonctionne dans l'analyse de données afin de mieux comprendre l'utilisation d'Excel par les utilisateurs pour lesquels il m'arrive de créer des Power BI.

## Sommaire

1. Qu'est-ce qu'Excel ?
2. Création d'une base de données sur Excel
3. Nettoyage de données sur Excel
4. Analyse de données sur Excel
5. Visualisation de données

#### Ressources et Outils utilisés
+ [Découvrir Microsoft Excel](https://www.blogdumoderateur.com/tools/microsoft-excel/)
+ [Les bases de l'analyse de données sur Excel](https://cartong.pages.gitlab.cartong.org/learning-corner/assets/pdfs/trainings/220908-Module-formation-analyse-donnees-Excel_CartONG.pdf)


## 1. Qu'est-ce qu'Excel ?
<strong>Microsoft Excel</strong>, un logiciel de tableur faisant partie de la suite bureautique Office 365, présente des tableaux organisés en lignes et colonnes dans des onglets distincts appelés feuilles de calcul. Cette application intègre des fonctionnalités de calcul numérique, de représentation graphique, d'analyse de données, ainsi qu'une capacité de programmation grâce à son propre langage.

En tant qu'élément considéré comme le plus complexe au sein de la suite Office, Microsoft Excel offre une gamme variée de fonctionnalités, notamment :

+ Calculs à partir de formules mathématiques : Vous pouvez entrer des formules dans une cellule en utilisant le symbole « = » suivi de l'opération à effectuer.

+ Calculs à partir de fonctions Excel : Vous avez également la possibilité d'utiliser des fonctions prédéfinies telles que « SOMME », « MOYENNE », ou encore « MAINTENANT » pour afficher la date et l'heure actuelles dans une cellule désignée.

+ Formules matricielles : Certaines formules ont la particularité de générer des calculs pour une matrice entière.

+ Graphiques : Excel permet de créer des graphiques à partir de données contenues dans un tableau. Ces graphiques se mettent automatiquement à jour si les données sont modifiées.

+ Tableaux croisés dynamiques : Cet outil permet de regrouper des données selon un ou plusieurs critères et de les présenter sous forme de sommes, moyennes ou comptages.

+ Macros : Les macros Excel sont des séquences d'actions qui automatisent des tâches. Elles sont enregistrées en utilisant le langage de programmation Visual Basic pour applications.

Une autre caractéristique importante de Microsoft Excel est la possibilité de protéger une feuille de calcul avec <strong>un mot de passe</strong>, limitant ainsi l'accès non autorisé et les modifications indésirables.

Les fichiers générés par Excel sont généralement enregistrés aux formats .xls ou .xlsx pour les feuilles de calcul, et .csv ou .txt pour les fichiers contenant du texte.

## 2. Création d'une base de données sur Excel
Le plus souvent la base de données est <strong>le fichier Excel</strong> que les équipes utilisent pour <strong>suivre leurs données de programme</strong> mais elle peut aussi être sur papier, sous un format texte ou un format plus complexe. 
Une base de donnée est un élément indispensable pour trouver facilement et rapidement les données que l'on souhaite.

#### Comment créer une BDD sur Excel ?
Pour créer une BDD sur Excel on a besoin de 3 étapes :
+ Définir les lignes
+ Définir les colonnes
+ Designer les colonnes

<strong>Définir les lignes</strong>
Chaque ligne correspond à un enregistrement.
Le plus souvent cela correspond à un ensemble de réponses d'une collecte de données. Il est <strong>PRIMORDIALE</strong> que chaque enregistrement est un identifiant unique qui permette de remonter à la ligne en question. Le plus souvent on utilise une suite de nombre (1, 2, 3, 4,...).

<strong>Définir les colonnes</strong>
Chaque colonne correspond à une information. On indique en haut de chaque colonne de cellule le nom de la variable informative par exemple *auteur* , *date* , *durée* , *taille de la toile* , *type*,...

<strong>Designer les colonnes</strong>
La première colonne sera toujours l'ID de l'enregistrement. Les en-tête de colonnes sont uniques, courts et clairs. On peux rajouter si on le souhaite des en-tête supplémentaire pour définir des parties afin d'améliorer la lisibilité de la BDD.

Exemple : mini-BDD de peintures
<div style="display:flex"><img src="bdd.png"></div>
Grace à la fonctionnalité de filtre il sera plus simple de naviguer dans des BDD plus imposantes.

#### Principes de bases
+ <strong>La référence absolue</strong>
Lors de l'utilisation d'Excel on fait souvent référence à des cellules. Si l'on désire que la référence ne soit pas modifier lorsqu'on recopie sa formule il faut penser à rajouter le symbole <strong>$</strong>.

+ <strong>Nommer une plage de cellules</strong>
Nommer une plage de cellules permet de <strong>gagner du temps sur l'entrée et la lisibilité des formules</strong>.
Pour ce faire il suffit de sélectionner la plage des cellules à nommer et d'entrer le nom voulu dans la plage associée.
<div stype="display:flex"><img src="plage.png"></div>

## 3. Nettoyage de données sur Excel
Maintenant que l'on sait créer une BDD sous Excel nous allons voir comment nettoyer des données c'est à dire à <strong>analyser la cohérence des données</strong> et à effectuer une <strong>triangulation</strong> avec d'autres informations.
Le nettoyage de données permet d'avoir une base de données à jour sans risquer des erreurs d'analyse.

Il y a trois grand principes aux nettoyages des données :
+ Vérification de la cohérence logique
+ Vérification de la fiabilité 
+ Correction des erreurs 
Alors, le but est de déceler : *les valeurs manquantes* , *celulles vides* , *fautes de frappes* , *doublons* , *valeurs extrêmes* , *textes en chiffres et inversement* , ...

<strong>Erreurs courantes faciles à rectifier</strong>
+ Nombres enregistrés sous forme de texte : 
  Il faut sélectionner toute la plage de données concernée faire un clic droit et choisir "Convertir en nombre"
+ Trouver un point au lieu d"une virgule pour les nombres :
  Il faut utiliser la fonction "Rechercher et remplacer" pour modifier les points par des virgules.
+ Les espaces inutiles :
  On utilise la formule <strong>SUPPRESPACE()</strong> qui permet de supprimeer les espaces du texte à l'exception des espaces simples entre les mots.
+ Doublons et valeurs extrêmes : 
Une valeur extrême est une valeur <strong>aberrante</strong> anormalement différente de la distribution d'une variable. Comme les doublons il est important de trouver ce type d'anomalie afin de ne pas induire d'erreur dans l'analyse.
Pour cela on peut utiliser l'outil de <strong>Mise en forme conditionelle</strong> dans l'onglet *Acceuil*.
On trouve alors facilement les valeur extrême en utilisant *Supérieur à ...* ou *Inférieur à...* et les doublons à l'aide de *Valeurs en double...*. 

Exemples : Nettoyage de la mini-BDD peintures avec des erreurs et des doublons intégrés exprès
<div stype="display:flex"><img src="nettoyage.png"></div>
Sur cet exemple, pour toute la colonne durée j'ai demandé à ce que les cellules inférieures à 6à soit mis en rouge et pour toute la colonne représentation que les cellule en doublons soit mise en rouge.

Ces méthodes mettent en exerbe des comportements étrange sur les données néanmoins cela ne veut pas focément signifier qu'il y a une erreure. Il est tout à fait possible que deux peinture représente la même chose ou qu'une peinture soit bien plus longue à réaliser que la moyenne, il est important de <strong>garder un esprit critique</strong> lors du nettoyage des données.

Pour en savoir plus sur les outils disponibles pour le nettoyage des données : [Nettoyer ses données](https://cartong.pages.gitlab.cartong.org/learning-corner/fr/3_nettoyage_page).

## 4. Analyse de données sur Excel
#### Introduction 
L'analyse des données permet de donner une interprétation aux données que l'on a relevé.
Beaucoup de calculs sont possibles pour les variables de type nombre (*effectif*, *minimum et maximum*, *moyenne et médiane*, *écartype et variance*, *somme*,...) mais il faut choisir celles qui auront le plus de sens en fonction du cas que l'on étudie.

#### Statistique descriptives
On peut s'y pencher selon 3 axes : 
+ La *distribution* qui concerne la <strong>fréquence</strong> de chaque valeur.
+ La *tendance centrale* qui concerne les valeurs <strong>moyennes</strong>.
+ La *variabilité* qui concerne la <strong>distribution</strong> des valeurs.

### Horodateur 
| Date | Heures passées | Indications | 
| -------- | -------- |-------- |
| Mercredi 27/09  | 1H  | Choix des sources/cours à suivre et début de l'apprentissage |
| Jeudi 28/09  | 2H  | Création d'une BDD et nettoyage |
