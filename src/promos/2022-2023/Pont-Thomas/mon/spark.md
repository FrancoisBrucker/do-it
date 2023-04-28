---
layout: layout/mon.njk


title: "MON 5 : Spark et Big Data"
authors:
 - Thomas Pont

date: 2023-03-23

tags:
  - 'temps 3'
  - 'spark'
  - 'data'
  - 'calcul distribué'
---


<!-- Début Résumé -->

Spark et Big Data
<!-- Début Résumé -->

## Introduction

J'ai réalisé ce MON pour préparer mon stage dans lequel je vais devoir faire de l'architecture de données et notamment devoir **récolter et traiter un grand nombre d'information**. Un des prérequis du stage est de comprendre les bases du **principe de traitement de mégadonnées** et de **Spark**. Il s'agit "d'un framework open source de calcul distribué". Il est utile pour traiter des mégadonnées et pour faire des analyses complexes à grande échelle.

Afin d'apprendre tout ceci, j'ai suivi le cours Openclassrooms [Réalisez des calculs distribués sur des données massives](https://openclassrooms.com/fr/courses/4297166-realisez-des-calculs-distribues-sur-des-donnees-massives).

Le cours est divisé en plusieurs parties :

- Introduction au Big Data et au calcul distribué
- Le principe de MapReduce
- Découvrir Spark

Ce MON nécessite de nombreux prérequis en **algorithmie**, **programmation** (maîtrise de Java ou Python) et **ingénierie informatique** (connaissance de l'environnement UNIX, ...) et est d'un niveau **avancé**.

## Introduction au Big Data et au calcul distribué

Aujourd'hui, de plus en plus de données sont collectées. Elles peuvent toucher tous les secteurs (consommation, environnement, santé,...). L'enjeu actuel est de pouvoir les stocker, les filtrer et les analyser. Mais ceci posent de nombreuses questions notamment sur la manière de stocker et d'architecturer les données. Un des points clés est la mise à l'échelle, lorsque l'on multiplie par un grand facteur le nombre de données que l'on possède. En effet, il faut alors faire attention à trois facteurs clés : le **Volume**, la **Vélocité** et la **Variété** (des formats).

Pour traiter des données, une des manières de pallier à leur multiplication est d'effectuer du **calcul distribué** au lieu de **calcul parallélisé**. Dans le calcul parallélisé, les calculs sont effectués **simultanément** en utilisant une **mémoire** et des **ressources communes**. Au contraire, dans le calcul distribué, les calculs sont faits dans des **nœuds indépendants**. La communication s'effectue à l'aide de messages dans des clusters. Cette méthode de calcul permet de **simplifier le passage à l'échelle** lorsqu'on rajoute des données. Il n'est plus nécessaire d'augmenter la puissance des processeurs (limitée par la loi de Moore) : il suffit dès lors d'ajouter des nœuds au cluster. Mais, cela permet aussi d'être plus **résistant aux pannes**. Dans des calculs parallélisés, si un nœud tombe en panne, le calcul ne peut plus être effectué alors que dans le cadre d'un calcul distribué, le calcul peut juste être donné à faire à un autre nœud.

## MapReduce

### Principe

MapReduce est une manière de résoudre un problème pour s'adapter aux contraintes du Big Data. L'objectif est de découper les données afin de pouvoir paralléliser les tâches et réunir les résultats ensuite. Deux opérations sont nécessaires pour cela : une opération **map** et une opération **reduce**.

Les différentes étapes sont les suivantes :

- **Découpage** des données en plusieurs sous-ensembles.
- Etape **Map** : l'opération map, qui dépend du problème qu'on souhaite résoudre, est appliquée à chaque sous-ensemble. Elle transforme la paire(clé, valeur) représentant le sous-ensemble en une liste de nouvelles paires (clé, valeur)
- Etape **Shuffle and Sort** : les résultats obtenus sont regroupés et triés par clé
- Etape **Reduce** : l'opération reduce, qui dépend du problème notre problème, est appliqué à chaque clé. Elle permet d'obtenir le résultat final.

Tout ceci peut être résumé par le schéma suivant :

![Schéma du MapReduce](../image/Schéma.jpg "Schéma explicatif MapReduce")
*Source : Openclassrooms*

### Exemples

#### Word count

Un des exemples basiques du MapReduce est le problème **"Word Count"**. Il permet de compter le nombre d'itération de chaque mot dans un texte. Afin de vérifier que j'avais bien compris le principe, j'ai recodé cette fonction.

On suppose que le texte a été découpé en différentes parties. La fonction Map associe à chaque mot d'une partie du texte la couple (clé, valeur), **(mot, 1)**.

```python
def compte_mot_map(ligne):
    mots = ligne.split()


    liste_paire = [(mot, 1) for mot in mots]
   
    return liste_paire
```

La fonction Shuffle permet de créer un dictionnaire de tous les mots présents et d'ajouter des 1 à chaque apparition d'un mot.

```python
def compte_mot_shuffle(liste_paire):
    dictionnaire_paire = {}
   
    for élément in liste_paire:
        clé = élément[0]
        valeur = élément[1]
        if clé in dictionnaire_paire :
            dictionnaire_paire[clé].append(valeur)
        else:
            dictionnaire_paire[clé] = [valeur]
   
    return dictionnaire_paire
```

Enfin la fonction Reduce somme tous les 1 pour un mot présent dans le dictionnaire et permet donc de connaître son nombre d'itération.

```python
def compte_mot_reduce(dictionnaire):
    result_liste=[]
    for mot in dictionnaire :
        result_list.append(compte_mot_indiv(mot, dictionnaire))
    return (result_liste)
```

En réunissant ces trois fonctions, on obtient la fonction *compte_mot* :

```python
def compte_mot(texte):
    return (compte_mot_reduce(compte_mot_shuffle(compte_mot_map(texte))))
```

#### Autres exemples

Cette méthode peut paraître simple mais, elle peut également s'appliquer à d'autres problèmes beaucoup plus complexes tel que la multiplication de matrice par un vecteur. C'est notamment à partir de ceci que Google a mis au point son algorithme de **Page Ranking**.

### Hadoop

Pour effectuer du MapReduce dans un contexte de Big Data, il faut une **infrastructure logicielle**. Cette dernière permettra de faire tourner des fonctions de manière **massivement développée** en s'assurant qu'il n'y ait pas de problèmes liés à la localité des données, à la puissance et aux pannes.
Le framework **Hadoop** permet ceci. Celui-ci est composé d'un **système de fichiers** où ceux-ci sont distribués, répliqués et optimisés et d'une **architecture pour faire tourner MapReduce**. Vous pouvez trouver plus d'informations sur Hadoop [ici](https://hadoop.apache.org/).

Globalement, l'utilisateur peut déposer des fichiers qui sont découpés sur des Datas Node. Toutes les informations sont dupliqués pour faire face aux potentielles pannes. Il peut ensuite donner le travail à effectuer au job tracker. Celui-ci communique avec le name node pour savoir où sont les données et pouvoir lancer les calculs de la manière la plus efficace possible. Tous les résultats sont sauvegardés au fur et à mesure.

![Schéma de Hadoop](../image/Schéma2.jpg "Schéma explicatif Hadoop")
*Source : Openclassrooms*

Ainsi l'utilisateur a juste à déposer ses données et à écrire les fonctions Map et Reduce.

En suivant ce lien, on peut télécharger et tester une [machine virtuelle Hadoop](https://www.cloudera.com/downloads/cdp-private-cloud-trial.html). Il est donc possible de tester la fonction *Count Word* sur Hadoop.

## Spark

### Présentation et exemple

**Spark** permet de s'affranchir de quelques problèmes causés car Hadoop. En effet, Hadoop stocke à chaque étape les données et résultats sur le **disque** et ne les gardent pas sur la RAM. De plus, les opérations possibles sont **limitées**.

Les programmes de Spark peuvent être écrits en Python ou en Java.

Voici le lien d'un tutoriel pour [télécharger Spark sous Windows](http://www.xavierdupre.fr/app/sparkouille/helpsphinx/lectures/spark_install.html).

Voici un exemple de réécriture d'une fonction permettant de faire Word Count via Spark :

``` python
import sys
from pyspark import SparkContext

sc = SparkContext()
texte_rdd = spark.sparkContext.textFile(file_path)
ligne = sc.texte_rdd(sys.argv[1])
compte_mot = ligne.flatMap(lambda ligne: ligne.split(' ')) \
                   .map(lambda mot: (mot, 1)) \
                   .reduceByKey(lambda c1, c2: c1 + c2) \
                   .collect()

for (mot, compteur) in compte_mot:
    print(mot, compteur)
```

Les premières lignes du code permettent d'importer les bons modules. Notre fichier est ensuite mis en RDD (cf lien dans les sources pour plus d'informations). Enfin, on définit les méthodes *Map* et *Reduce* qui sont ensuite directement gérées par Spark.
Ici Spark tourne en **local** sur notre ordinateur mais il prévoit déjà une architecture si on possède **plusieurs machines connectées**.

### Compléments

Spark permet également d'aller plus loin notamment pour les Data Scientists. Un module Spark SQL est ainsi disponible pour faire "un modèle de requête SQL distribué" via des Data Frame. Il existe également un module de Machine Learning Spark ML.

## Conclusion

Le cours est noté pour durer 20h mais la dernière partie est peu pertinente et peut être lue rapidement. Il est surtout important de s'attarder sur les premiers concepts présentés pour bien comprendre la logique de Spark et son fonctionnement.

## Sources

- [Page Wikipédia de Spark](https://fr.wikipedia.org/wiki/Apache_Spark)
- [RDD (Resilient Distributed Datasets) en Spark](https://sparkbyexamples.com/spark-rdd-tutorial/)
- [Fonction parallelize](https://sparkbyexamples.com/spark/how-to-create-an-rdd-using-parallelize/?utm_content=cmp-true)
- [Spark SQL](https://spark.apache.org/sql/)
