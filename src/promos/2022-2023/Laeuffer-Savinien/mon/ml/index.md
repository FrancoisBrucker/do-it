---
layout: layout/mon.njk

title: "Machine learning"
authors:
  - Savinien Laeuffer
date: 2023-04-05

tags:
  - 'temps 3'
---

<!-- début résumé -->
Apprentissage supervisé et non supervisé (Machine Learning)
<!-- fin résumé -->

## Description

Avec l'apparition de nombreuses intelligences artificielles comme ChatGPT, Dall-e, etc que j'ai pu beaucoup utiliser, je me suis dit qu'il était intéressant de s'intéresser au Machine Learning tout d'abord avant de rentrer dans ces concepts plus complexes. Puisque je serai aussi amené lors de mon stage à traiter des données, il est intéressant de voir cette facette de l'intelligence artificielle et c'est pourquoi je me suis penché sur la théorie concernant le machine learning (et non la pratique cette fois-ci).

Le Machine learning est un modèle d'intelligence artificielle qui est capable d'apprendre seul à partir de jeux de données en utilisant des algorithmes basés sur les statistiques et les probabilités.
Grâce à cela il est possible de traiter, d'analyser de très grand jeux de données qu'un humain ne peut faire à la main, et pouvoir en tirer des conclusions.

On distingue en Machine Learning, deux types d'algorithmes: l'apprentissage supervisé et l'apprentissage non supervisé.

## Apprentissage supervisé

Partons d'un large jeu de données sous forme de tableau CSV par exemple. Une base de données comportant des messages textuels, et une colonne indiquant si ce message est d'humeur positive ou négative.
Dans le cadre de l'apprentissage supervisé, l'algorithme va essayer de prédire une certaine donnée du tableau (ici l'humeur du message) tout en connaissant déjà les réponses que l'on attend d'elle. Ainsi une fois que notre IA sera entraînée sur un large set de données, elle sera capable d'évaluer l'humeur d'un message qui ne fait pas parti de ce jeu de données.

<div style="width:100%;">
  <figure style="text-align:center">
    <img style="height:400px; margin-left: auto; margin-right: auto" src="../supervised.png">
    <figcaption>Schéma de modèle supervisé</figcaption>
  </figure>
</div>

A partir des données on établit un set d'apprentissage et un set de validation. A partir de ces sets, on entraine l'IA à l'aide d'un certain modèle de machine learning pour qu'elle prédise des résultats recherchés.


##### Classification

Ce type d'apprentissage est utile pour exécuter des tâches de classification, c'est à dire, attribuer une classe à un objet. Par exemple si un mail est un spam ou non, si un message est d'humeur positive ou négative. On définit nous mêmes les différentes classes qui vont permettre à la machine de classifier les éléments.

##### Régression

On peut aussi exécuter des tâches de regression à partir de l'apprentissage supervisé. Au lieu d'attribuer une classe et leur appartenance ou non à cette classe, on attribut une valeur mathématique comme un pourcentage. Pqr exemple, on peut essayer de déterminer à combien de pourcent un e-mail est considéré comme un spam.

##### Exemple: Classification Naïve bayésienne (Naive Bayes)

Le classifieur Naive Bayes est un type de classifieur probabiliste basé sur la formule de Bayes.
Dans le cadre de la classification de texte, on essaie par exemple de terminer à quelle catégorie est associée un certain texte. Ces catégories peuvent être des opinions (positive, neutre, négatif), des domaines binaires spécifiques (spam ou pas spam, à conseiller à l'utilisateur ou non), ou bien des sujets/thèmes divers et variés (Business, art, sports...)

La formule de Bayes est la suivante:

<div style="width:100%;">
  <figure style="text-align:center">
    <img style="height:100px; margin-left: auto; margin-right: auto" src="../prob1.png">
    <figcaption>Formule de Bayes</figcaption>
  </figure>
</div>

C est une des variables de classe dépendante, tandis que X représente une suite de variables caractéristiques.

Dans ce cas ici on va supposer que C correspond à l'ensemble des variables thèmes C1 = "business", C2 = "art", C3 = "sport".
X = (x1, x2, ..., xn) correspond aux différents mots du texte qu'on cherche à classifier.

On cherche à déterminer quel catégorie est la plus probable d'être associée au texte sachant que le texte X a été utilisé.
Le calcul est donc le suivant:

<div style="width:100%;">
  <figure style="text-align:center">
    <img style="height:100px; margin-left: auto; margin-right: auto" src="../prob2.png">
    <figcaption>Calcul d'appartenance à une catégorie</figcaption>
  </figure>
</div>

Or grâce à la formule de Bayes, sachant que la probabilté d'avoir les mots (x1, ..., xn) est égale à 1, on peut simplifier le calcul comme suit:

<div style="width:100%;">
  <figure style="text-align:center">
    <img style="height:300px; margin-left: auto; margin-right: auto" src="../prob3.png">
    <figcaption>Simplification du calcul</figcaption>
  </figure>
</div>

En supposant que la présente des différents mots du texte sont indépendants (ce qui est quand même une forte hypothèse), on peut établir un produit de probabilités. En effet P(Cj) peut être établit à partir de la fréquence des classes dans le dataset d'entrainement. La probalité d'avoir le mot X1 lorsque la catégorie est Cj, est une valeur qui peut être estimée si le dataset d'entrainement est très grand.
On estime donc quelle catégorie est la plus représentative, mais on a aussi une pourcentage d'appartenance à ces catégories.

On appelle ce classifieur Naïf puisqu'il repose sur une hypothèse d'indépendante assez forte, cependant il n'est pas si naïf que ça puisqu'il est encore utilisé pour déterminer si des mails sont des spams ou non.

Pour rendre cet algorithme efficace, il faut pratiquer ue sélection de caractéristique. C'est à dire qu'au lieu de traiter tous les mots même inutiles des textes, on va garder ceux qui sont le plus déterministes et pertinentes afin de réduire la dimensionnalité du problème.

## Apprentissage non supervisé

Dans le cadre d'apprentissage non supervisé, les catégories ne sont pas indiquées dans le dataset et on cherche donc à fractionner ce jeu de données en parties définies que l'on appelle clusters. On réalise donc ici un clustering.

La machine va par elle même grouper les objets dans des classes qu'elle invente elle même, en se basant sur les similitudes entre les objets et créer un ensemble le plus homongène possible.

<div style="width:100%;">
  <figure style="text-align:center">
    <img style="height:400px; margin-left: auto; margin-right: auto" src="../unsupervised.png">
    <figcaption>Schéma de modèle non supervisé</figcaption>
  </figure>
</div>

##### Exemple: K-moyennes

La méthode des K-moyennes est un algorithme qui permet le partitionnement d'un set de données. K étant un entier, on cherche à diviser le jeu de données en K clusters. Il fonctionne comme suit:

K est un entier

1. On crée k clusters initiaux. Pour chacun on calcule les coordonnées du centre de masse C_i à partir de moyennes numériques des attributs des objets.

2. On prend un objet X et on calcule sa distance à tous les centres de masse des clusters, on note j l'index du centre de masse le plus proche.

3. Si cet objet X se trouve déjà dans le cluster j, on ne fait rien, sinon on change X de cluster afin qu'il se trouve dans C_j. On recalcule alors tous les centres de masse

4. Tant qu'un point d'arrêt n'est pas rencontré (tous les objets se trouvent dans le cluster le plus proche), on répète les 2 dernières étapes.

Sur un schéma en une dimension, voici un exemple:

<div style="width:100%;">
  <figure style="text-align:center">
    <img style="height:500px; margin-left: auto; margin-right: auto" src="../cluster.png">
    <figcaption>Exemple - K-moyennes</figcaption>
  </figure>
</div>

## Logiciels de datamining et d'apprentissage (Orange, Weka...)

##### Orange

Orange est un logiciel open source basé sur Python, qui est utile pour l'analyse de données et le machine learning. Il est possible de visualer, modéliser et évaluer des données à l'aide d'une interface graphique ergonomique.

Il est possible de réaliser des schéma/algorithme comme suit:

<div style="width:100%;">
  <figure style="text-align:center">
    <img style="height:600px; margin-left: auto; margin-right: auto" src="../orangeschema.png">
    <figcaption>Orange</figcaption>
  </figure>
</div>

1. On met en entrée un jeu de données dans un format adéquat (xlsx, csv par exemple) qui va d'abord subir une étape de pre-processing (supprimer les valeurs manquantes, discrétiser des variables continues, pratiquer une selection de caractéristiques, ...)

2. On relie ces données à un modèle de notre choix afin de faire des prédictions. De nombreuses méthodes sont disponibles parmi lesquelles on trouve k-plus proches voisins, Naive Bayes, régression logistique, réseaux neuronaux et bien d'autres.

3. On peut finalement évaluer ces données grâce à différents outils, notamment l'affichage d'une matrice de confusion qui repertorie les vrais positifs, faux négatifs, vrais négatifs et faux positifs classés par le modèle afin de déterminer sa fiabilité.

<div style="width:100%;">
  <figure style="text-align:center">
    <img style="height:200px; margin-left: auto; margin-right: auto" src="../confusion.png">
    <figcaption>Matrice de confusion</figcaption>
  </figure>
</div>

##### Weka

Weka lui, est basé sur Java et est un outil similaire mais beaucoup plus complet, plus dur à utiliser et à l'interface moins ergonomique que celle d'Orange.

Voici un exemple de mise en place d'un algorithme K-Moyennes.

<div style="width:100%;">
  <figure style="text-align:center">
    <img style="height:700px; margin-left: auto; margin-right: auto" src="../weka.png">
    <figcaption>Weka</figcaption>
  </figure>
</div>

1. ArffLoader permet d'importer un data set au format reconnu par Weka

2. Training SetMaker permet de transformer ce jeu en jeu d'entrainement.

3. Simple KMeans correspond à l'algorithme des K-moyennes.

4. Les deux dernières étapes évaluent les clusters formés et d'afficher les résultats.

Voici dans ce cas là le résultat de la pipeline que nous avons fait, sur un dataset qui répertorie des patients anonymes ayant été atteint de crise cardiaque et des valeurs médicales. La valeur de K pour la méthode des k-moyennes ici est égale à 2

[Dataset en question](https://archive.ics.uci.edu/ml/datasets/Heart+failure+clinical+records)

<div style="width:100%;">
  <figure style="text-align:center">
    <img style="height:700px; margin-left: auto; margin-right: auto" src="../wekaresults.png">
    <figcaption>Résultats weka</figcaption>
  </figure>
</div>

Les deux clusters créés sont affichés et la principale caractéristique qui les différents est la variable "mort ou vivant" nommée "DEATH_EVENT" avec 0 pour vivant, et 1 pour mort.
On obtient une colonne avec les moyennes de chaque variable, et les moyennes de chaque variables pour les différents clusters

## Ressources

- [Orange](https://orangedatamining.com/download/#windows)
- [Weka](https://sourceforge.net/projects/weka/)
- [Schémas](https://www.researchgate.net/figure/Machine-Learning-Unsupervised-Schema_fig2_331473456)
- [Lecture 12, Stanford.edu](https://web.stanford.edu/class/cs276/)
- Introduction to Machine Learning & Desicion Trees, Maciej Piasecki
- [Apprentissage supervisé et non supervisé : quelles différences ?](https://experiences.microsoft.fr/articles/intelligence-artificielle/apprentissage-supervise-et-non-supervise-quelles-differences/)
