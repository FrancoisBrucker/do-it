---
layout: layout/mon.njk

title: "Python pour l’Analyse de Données Textuelles - Partie 2 : Analyser"
authors:
  - Esther Henry

date: 1970-10-01
tags: 
  - "temps 1"
  - “vert”
  - ”python”

résumé: "Ce MON fait suite au MON1.1, son objectif est donc de continuer l’apprentissage de python pour les SHS et de passer cette fois à l’étape de manipulation de données, et de traiter un exemple simple d’analyse de données textuelles avec python."
---

{% prerequis %}

Maîtriser les bases de python et l’utilisation des bibliothèques (ou lire mon MON 1.1).

{% endprerequis %}
{% lien %}

[Mon MON 1.1](https://francoisbrucker.github.io/do-it/promos/2024-2025/Esther-Henry/mon/temps-1.1/)

{% endlien %}

## Objectifs

1. Apprendre les bases de l’analyse de données sous Python  
2. Apprendre les fonctions de base spécifiques à l’analyse de données textuelles  
3. Réaliser une analyse de données textuelles pour pratiquer sur un exemple

## Introduction

Python est de plus en plus utilisé en sciences humaines et sociales pour son efficacité dans le traitement et l'analyse de données massives et variées. Grâce à ses nombreuses bibliothèques dédiées à l'analyse textuelle, il permet d'extraire des informations pertinentes de grands corpus de textes, d'automatiser des tâches répétitives, et de visualiser des données de manière claire et compréhensible. Sa simplicité de syntaxe et sa large communauté d'utilisateurs en font un outil accessible, même pour les chercheurs n'ayant pas de formation technique poussée, tout en offrant une grande flexibilité pour mener des analyses complexes. C'est donc un langage idéal pour se former à l'analyse de données textuelles, ce qui sera à terme le but de ces MON.

## Manipuler des données

### Manipuler des données : pourquoi ?

L’objectif est d’être capable de créer un script afin de passer de données brutes (que l’on a, par exemple, appris à récupérer en ligne dans le MON1.1) à des données utilisables. Il s’agit donc de pouvoir **ouvrir** un fichier, **lire** les informations qu’il contient, les mettre dans un **format** adapté à la **visualisation** et à la **modification**, puis de les **sauvegarder** dans un fichier plus facile à utiliser.

### Catégories de données

Il existe deux catégories de données dans un programme :

- **Données externes** : celles qui nous intéressent et que nous voulons traiter
- **Données internes** : celles nécessaires au bon fonctionnement du programme

{% attention %}
Lorsque l’on manipule des données, il peut être tentant d’effectuer des modifications à la main sur les données brutes. Cependant, cela est fortement déconseillé ; il est préférable de le faire directement dans le code, car cela permet :  

- De garder une trace des modifications effectuées  
- Si les données d’entrée changent, il n’y aura pas besoin de tout refaire
{% endattention %}

### Charger et sauvegarder un fichier

Avant de pouvoir manipuler les données, il est essentiel de savoir accéder aux fichiers contenus dans votre ordinateur, afin que votre code puisse ensuite lire les informations et stocker les résultats correspondants. Ainsi, nous allons voir comment lire l’information puis la stocker, selon l’organisation d’un fichier : son format.

Le format d’un fichier est défini par la manière dont est organisée l’information à l’intérieur de celui-ci, et il est essentiel de savoir reconnaître le format d’un fichier afin de pouvoir récupérer ses informations.

#### Les formats de fichier

Il est en effet nécessaire de connaître le format d’un fichier afin de passer d’un fichier binaire (composé de 0 et de 1) à un fichier lisible. On reconnaît généralement le format à l’extension du fichier :

- **.txt** : informations textuelles de base  
- **.csv** : tableaux de données brutes  
- **.webp** : images  
- **.docx** : textes mis en forme par Word ou LibreOffice  
- **.xlsx** : tableur Excel ou LibreOffice  
- **.html** : pages internet  
- **.md** : textes en format markdown

{% info %}
Le format de fichier **.pdf** est très compliqué à utiliser pour le traitement des données, car ce n’est pas un format conçu pour l’ordinateur afin de stocker des informations temporairement. Il s’agit d’un format plutôt destiné à l’homme pour réaliser une présentation finale des informations.
{% endinfo %}

#### Ouvrir un fichier

Lorsque les fichiers sont directement contenus dans l’ordinateur, le programme doit aller récupérer ce contenu afin de pouvoir l’utiliser, c’est ce que l’on appelle **lire** le fichier.

Par ailleurs, **écrire** dans un fichier permet de conserver l’information. Si l’information n’est pas écrite, elle disparaît après l'exécution du code.

Pour ouvrir un fichier, il faut alors :

- Créer un lien vers le fichier correspondant à l’aide de la fonction **open( )**. Cette fonction indique que le fichier est actuellement utilisé et interdit son utilisation par d'autres programmes.  
- Réaliser les actions de lecture et d’écriture détaillées par la suite.  
- Une fois nos actions terminées, il faut fermer le fichier avec la fonction **close( )**.

##### Lire un fichier

{% faire %}
Afin de pouvoir reproduire les exercices qui vont être présentés tout au long de ce NOM, je vous conseille de télécharger une base de données. Il en existe énormément en libre accès, notamment sur le site de l’Insee, mais il existe aussi plein d'autres sites avec des bases de données en tout genre.

Ici, je vais travailler avec une base de données fictive que je vais nommer **ma-base-de-donnees**, qui devra être située dans un dossier appelé **data** et qui est stockée dans le même dossier que mon fichier Python sur lequel j’exécute mon script.
{% endfaire %}

Ainsi, pour lire notre fichier, nous allons utiliser :

- La fonction **open** en donnant le chemin du fichier ainsi que le mode de lecture **“r”**, que nous stockerons dans la variable `fichier`.  
- La méthode **.read( )** nous permet de lire tout le contenu du fichier, que nous allons stocker dans la variable `contenu`.  
- La méthode **close** nous permet de fermer le fichier.  
- Nous affichons les 50 premiers éléments de `contenu` (afin de vérifier que l’opération a bien fonctionné).

```python
#Ouvrir, lire et fermer un fichier
fichier = open("./data/ma-base-de-donnees.csv","r")
contenu = fichier.read()
fichier.close()
print(contenu[0:50])
```

Pour un code plus compact, il est aussi possible d’utiliser le bloc **with** pour obtenir le même résultat et automatiser la fermeture du fichier :

```python
#Ouverture, lecture et fermeture avec le block with
##Permet la fermeture automatique du fichier en sortant de with
with open("./data/ma-base-de-donnees.csv","r") as fichier :
    contenu = fichier.read()
print(contenu[0:50])
```

{% info %}
La fonction **readlines( )** est aussi intéressante, car elle permet de lire en séparant les lignes. En théorie, les lignes sont séparées par le caractère spécial **\n**. Si l’on utilise simplement la fonction **read**, on risque de voir apparaître plein de ‘\n’ dans notre texte.

Ainsi, si l’on veut par exemple afficher les cinq premières lignes de ma base de données :

```python
#Afficher les 5 premieres lignes d'un fichier
with open("./data/ma-base-de-donnees.csv","r") as fichier :
    lignes = fichier.readlines()
print(lignes[0:5])
```

{% endinfo %}

##### Écrire dans un fichier texte

Afin d’écrire dans un fichier texte, il suffit de préciser dans la fonction **open**, le mode d’écriture **“w”** ou **“a”**.

- **“w”** (write) : pour remplacer ou créer. Le mode **“w”** crée un fichier s'il n’existe pas et supprime l’existant pour le remplacer sinon.  
- **“a”** (append) : pour ajouter. Le mode **“a”** ajoute l’information à la fin du fichier s'il existe déjà, ou le crée sinon.

De plus, la fonction **write( )** permet d’écrire dans notre fichier.

Ainsi, si l’on veut sauvegarder un fichier texte dans lequel on veut écrire le nombre d’élèves présents en Do-It, par exemple :

```python
#Faire la sauvegarde d'un résultat
with open("./eleves.txt","w") as fichier :
    fichier.write("Élèves en Do-It : 25\n")
```

{% info %}
Ajouter **“\n”** à la fin du texte permet de générer un saut de ligne à la fin (ce n’est pas fait automatiquement sinon).
{% endinfo %}

#### Bibliothèques utiles pour écrire dans un fichier

La bibliothèque **os** contient la majorité des outils permettant de manipuler des fichiers et des dossiers. On peut par exemple créer un nouveau répertoire avec la fonction **mkdir( )** :

```python
#Créer un nouveau répertoire dans lequel on crée un fichier texte
import os 
os.mkdir("Eleves")
with open("Eleves/effectif.txt","w") as fichier :
    fichier.write("L’effectif d’élèves en Do-It est : 25")
```

La fonction **glob( )** de la bibliothèque **Glob** permet de trouver tous les fichiers d’un dossier qui contiennent un motif donné, par exemple :

```python
#Rechercher tous les fichiers excel d'un dossier
import glob
fichiers_excel = glob.glob('*.xls')
print(fichiers_excel)
```

Ici **”*”** signifie “tous”.

Par ailleurs, pour des fichiers non texte, il faut utiliser des bibliothèques spécifiques pour garder une mise en forme adaptée au format (ex : Excel, image).

{% info %}
Pour information, une des bibliothèques les plus utilisées pour les fichiers Excel est **Pandas**.
{% endinfo %}

#### Un petit exercice pour pratiquer

{% exercice %}
Télécharger la page d'accueil de votre journal favori et la sauvegarder dans un fichier texte.
{% endexercice %}
{% details "corrigé" %}

```python
import requests as req
url ="https://www.lequipe.fr"
info = req.get(url)
with open("./lemonde.txt","w") as fichier :
    fichier.write(info.text)
```

{% enddetails %}

### Manipuler des ensembles d'éléments

Afin de pouvoir manipuler des données plus complexes, il est essentiel d’approfondir les notions de listes et de bibliothèques.

#### Rappel des fonctions importantes

Avant de travailler sur les listes, il est essentiel de maîtriser ces fonctions de base :

- **len(liste)** : longueur de la liste  
- **liste[x]** : valeur de l’élément de rang x  
- **liste.index(v)** : premier indice de la valeur v  
- **liste[x:y]** : valeur entre les indices x et y (y non inclus)  
- **liste[-1]** : dernier élément de la liste  

Une autre fonction un peu moins connue, mais aussi très utile, est la méthode **.sort( )** qui permet de trier une liste par ordre alphabétique ou numérique.

#### Les listes emboîtées

Maîtriser la notion de liste emboîtée est essentiel si l’on veut traiter des tableaux de données.

Une **liste emboîtée** (ou liste imbriquée) est une structure de données qui consiste en une liste contenant d'autres listes comme éléments. Cela permet de créer des structures hiérarchiques ou multidimensionnelles, par exemple :

```python
# Une liste emboîtée représentant des coordonnées (x, y)
coordonnees = [[1, 2], [3, 4], [5, 6]]

# Accéder à un élément spécifique : le premier élément de la deuxième liste
print(coordonnees[1][0])  # Affiche 3
```

Nous allons donc voir ici comment utiliser les listes emboîtées non pas comme un bloc, mais sous la forme d’un tableau qui sépare les informations :

```python
#Lire les lignes du fichier
with open("./data/ma-base-de-donnees.csv","r") as f :
    contenu = f.readlines()
print(contenu[0][0:40])
```

On commence par lire les lignes du fichier, comme vu précédemment.

{% info %}
Dans le cas d’un tableau de données classique, la première ligne du fichier va alors contenir les en-têtes des colonnes.
{% endinfo %}

Ensuite, nous allons chercher à identifier le nombre de lignes composant notre tableau :

```python
#Connaître le nombre de ligne hors entête
print("La taillle avant pop est", len(contenu))
premier_element = contenu.pop(0)
print("La taille de la liste est maintennant", len(contenu))
```

Ce script va alors nous permettre, grâce à la fonction **len**, de mesurer la longueur de notre liste avec l'en-tête. Puis, avec la méthode **pop(0)**, nous allons venir supprimer la première ligne de notre tableau (celle qui contient les en-têtes), tout en stockant cette information dans `premier_element`, afin d’avoir le nombre de lignes contenant des valeurs.

Ensuite, notre fichier étant un tableau dans lequel chaque ligne comprend des valeurs séparées par des **”;”**, nous allons séparer ces lignes afin de pouvoir récupérer nos données de manière indépendante.

```python
#Transformer chaque entrée en une liste
donnees = []
for ligne in contenu :
    ligne_decoupe = ligne.split(";")
    donnees.append(ligne_decoupe)
print(donnees[0][0:5])
```

Ici, nous avons donc séparé chaque élément grâce à la méthode **split(“;”)** qui permet de couper entre chaque point-virgule. Ensuite, nous choisissons d’afficher les 5 premiers éléments du premier élément de cette liste.

La liste que l’on a créée permet maintenant d’accéder à nos données comme dans un tableau à deux entrées. Ainsi, si l’on veut par exemple afficher le troisième élément de la septième ligne :

```python
#Afficher le 3eme élement de la 7eme ligne
print(donnees[6][2])
```

La septième ligne est à l’indice 6, et le troisième élément de notre tableau est dans la colonne 3, donc à l’indice 2.

### Manipuler du texte

#### Notion d’encodage

Nous n’allons pas beaucoup rentrer dans les détails de l’encodage ici, mais l’idée à retenir est que si, à l’ouverture de votre fichier, l’affichage comporte des caractères spéciaux un peu partout, c’est que votre fichier ne s’est pas ouvert avec le bon encodage.

Ainsi, si vous connaissez l’encodage qui a été choisi, vous pouvez ouvrir un fichier en le spécifiant (comme nous allons le voir ci-dessous). Dans le cas où, malheureusement, vous n’avez pas cette information, le mieux est de procéder par essais-erreurs avec les encodages les plus usuels.

Imaginons que l’on veuille ouvrir notre base de données et que le texte de celle-ci soit encodé en **“latin1”** (un des plus classiques) :

```python
#Encodage
with open("./data/ma-base-de-donnees.csv", "r",encoding="latin1") as fichier :
    contenu = fichier.read()
```

Ici, **encoding="latin1"** permet d’ouvrir le fichier avec le mode d’encodage choisi, le latin1.

#### Mise en forme de texte

Pour rappel, un texte est un ensemble de symboles (lettres, chiffres, ponctuations), ainsi pour accéder à une lettre d’un texte, cela revient à accéder à un élément de la liste à l’aide de son index.

**Fonctions utiles**
Il existe des méthodes permettant de mettre le texte en majuscule, minuscule, ou uniquement avec la première lettre en majuscule :

- **lower( )** : permet de mettre en minuscule  
- **upper( )** : permet de mettre en majuscule  
- **capitalize( )** : permet de mettre une majuscule uniquement à la première lettre

Par exemple :

```python
texte = [i.lower() for i in texte]
```

La méthode **replace( )** permet de remplacer un ensemble de lettres par un autre.

Par exemple, si l’on veut remplacer tous les points-virgules par des espaces :

```python
texte = [i.replace(“;”,” “) for i in texte]
```

#### Intégrer des variables au texte

On s'intéresse ici à comment intégrer une variable, par exemple un nombre, dans un texte. Une méthode est la méthode de formatage : **format( )**, que nous allons détailler ici, mais il est bon de savoir qu’il en existe d’autres.

L’intérêt de la méthode de formatage est que l’on peut insérer dans le texte une sorte d’espace vide dans lequel on pourra venir intégrer notre variable sans avoir forcément besoin de la définir au préalable :

Par exemple :

```python
#Intégrer des variables
nb_eleves_do_it = 25
print("Il y a {} élèves en Do_It".format(nb_eleves_do_it))
```

La variable que l’on va ajouter se rajoutera donc à l’endroit où nous avons mis les **{}**, et la valeur de la variable est ajoutée grâce au **.format(variable)**. On retournera donc : **Il y a 25 élèves enDo_It**
Cette fonction peut notamment être utile pour faire de la restitution de données et donc intégrer vos résultats d’analyse à du texte.

#### Traitement de données réelles

Dans cette partie, nous allons apprendre à faire une analyse sur du texte réel. Il faudra donc le formater avant de pouvoir extraire l’information recherchée.

Ici, nous allons créer un programme permettant de compter le **nombre de mots composés** dans une base de données. Si vous voulez le tester aussi assurez vous que votre base de données en comprenne (par exemple des noms de communes ou des prénoms).

Nous allons commencer par ouvrir notre base de données contenant du texte,comme précédement :

```python
#Ouvrir le fichier en séparant les lignes
with open("./data/ma-base-de-donnees.csv", "r") as file:
    contenu = file.readlines()
donnees = [ligne.split (";") for ligne in contenu]
print(donnees[1][0:10])
```

L’objectif ici est d’ouvrir notre fichier et de le séparer par ligne, puis d’afficher une partie des éléments afin d’identifier les éléments à nettoyer. Dans ce cas, nous devons nettoyer des **”** et des **\n** qui apparaîtront dans nos résultats.

{% info %}
Une infinité d’autres erreurs peut survenir selon l’encodage de votre fichier. Classiquement, il peut y avoir des signes parasites comme des guillemets ou encore des virgules, mais d’autres suites de caractères peuvent apparaître, comme par exemple :

**\u202f** : C'est le code Unicode pour le caractère d'espacement insécable (narrow no-break space). Ce caractère est souvent utilisé pour ajouter un espace entre des chiffres, en particulier dans les nombres, sans qu'il soit possible de les séparer à la fin d'une ligne.

Lorsque l’on veut faire apparaître notre chiffre en entier, il peut donc être utile de nettoyer ce code en le remplaçant, par exemple, par rien.
{% endinfo %}

Une fois le fichier ouvert, nous allons créer une fonction de nettoyage afin de remplacer les caractères indésirables identifiés par rien (c’est une façon de les supprimer).

```python
# Définir une fonction de nettoyage
def nettoyage (ligne) :
    nouvelle_ligne = ligne.replace('"','')
    nouvelle_ligne = nouvelle_ligne.replace("\n","")
    return nouvelle_ligne
```

Cette fonction nous permet donc de supprimer les guillemets et les indicateurs de saut de ligne, et nous retourne notre texte sans. Pour s’en assurer, nous pouvons l’appliquer à notre base de données et retourner la même portion que précédemment. Nous constatons donc que les caractères qui nous dérangeaient ne sont plus là.

```python
# Nettoyer et afficher
donnees = [nettoyage(ligne).split(";") for ligne in contenu]
print(donnees[1][0:10])
```

Une fois notre base de données textuelles nettoyée, nous allons pouvoir passer au comptage.

Pour ce faire, nous avons besoin d’une nouvelle fonction, la fonction **.count()**, qui permet de compter l’occurrence d’un élément.

Comme nous cherchons à compter les mots composés, nous allons compter le nombre de fois où apparaissent un tiret ou un espace (ces éléments sont caractéristiques des mots composés).

```python
# Compter le nombre de nom composé
nb_compose = 0

for ligne in donnees :
    nom = ligne[3]
    if(nom.count("-")>0 )or (nom.count(" ")>0) :
        nb_compose+=1
print("Il y a {} nom(s) composé(s)".format(nb_compose))
```

Ainsi, tout cela nous permet d’appliquer les fonctions vues jusqu'ici dans un cas concret sur des données réelles.

### Les expressions régulières

Les **expressions régulières** (ou regex) sont des séquences de caractères qui définissent un motif de recherche dans une chaîne de caractères. Elles sont largement utilisées en analyse de données textuelles pour effectuer des opérations telles que la recherche, la validation, la substitution ou le découpage de chaînes.

Les expressions régulières possèdent une syntaxe spécifique, ce qui rend leur utilisation nécessaire dès que l’on sort de cas basiques pour des cas plutôt complexes. Par exemple, elles utilisent une syntaxe particulière pour décrire des motifs, incluant des métacaractères (comme **”.”** pour n'importe quel caractère, **”*”** pour zéro ou plusieurs répétitions, ou **”^”** pour indiquer le début d'une chaîne).

Ainsi, nous ne rentrerons pas plus dans le détail ici, mais il est toutefois essentiel de savoir que cela existe afin de pouvoir chercher des fonctions spécifiques à nos besoins dans la littérature.

Aussi, la bibliothèque **re** est le module intégré de Python pour travailler avec les expressions régulières. Elle permet d'effectuer des opérations de recherche, de correspondance, de substitution et de découpage sur des chaînes de caractères en utilisant des motifs définis par des expressions régulières.

On peut notamment citer la fonction **re.findall(pattern, string)** : renvoie une liste de toutes les occurrences du motif trouvé dans la chaîne.

## Faire une analyse

L’objectif ici est de pratiquer un petit peu en autonomie sur les notions abordées, et pourquoi pas d’en découvrir d’autres. L’idée est de trouver une base de données contenant du texte que l’on va pouvoir analyser.

### Trouver une base de données à analyser

En m’inspirant du MON de Lola sur les Pokémon [Étude statistique des Pokémons avec les outils Excel](https://francoisbrucker.github.io/do-it/promos/2024-2025/Lola-Perdrix/pok/temps-1/), j’ai décidé de me rendre sur [Kaggle](https://www.kaggle.com/datasets) afin de trouver une base de données à analyser.

Afin d’avoir une base de données qui contient du texte, l’idée était de trouver une base de données contenant des avis ou des critiques, car ce seront bien des données textuelles.

J’ai alors choisi de traiter la base de données des reviews des restaurants de Lima, au Pérou : Peruvian Food Reviews. Elle contient notamment les avis des utilisateurs ainsi que d’autres critères comme la note du commentaire, un identifiant d’utilisateur et du restaurant.

### Faire l’analyse

La première étape va être d’ouvrir le fichier dans Python (comme vu précédemment) afin d’en extraire les colonnes qui nous intéressent et que l’on va nettoyer par la suite.

#### Extraction des colonnes “review” et “score”

```python
#Ouvrir le fichier en séparant les lignes
with open(".data/reviews.csv", "r") as file:
    lignes = file.readlines()

# Création de ma nouvelle base de données comprenant les colonnes de “review” et de “score”
## Récupéreration des colonnes 2 (review) et 4 (score)
colonnes_deux = []
colonnes_quatre = []

for ligne in lignes: 
    colonnes = ligne.strip().split(",")  
    if len(colonnes) > 3:  
        colonnes_deux.append(colonnes[1])  
        colonnes_quatre.append(colonnes[3])  

## Fonction pour créer une nouvelle base de données à partir de deux colonnes
def creation_bdd(c1, c2):
    bdd = [[0, 0] for _ in range(len(c1))]  
    if len(c1) == len(c2):
        for i in range(len(c1)):  
            bdd[i][0] = c1[i]  
        for l in range(len(c2)) :
            bdd[l][1] = c2[l]  
    return bdd

## Appel de la fonction pour créer la base de données
base_de_donnees = creation_bdd(colonnes_deux, colonnes_quatre)
print(base_de_donnees[0:10][0:10])
```

{% info %}
La fonction **.strip ( )** en Python est utilisée pour supprimer les espaces (ou tout autre caractère spécifié) au début et à la fin d'une chaîne de caractères. Sans argument, .strip() supprime les espaces, les tabulations (\t) et les retours à la ligne (\n) au début et à la fin de la chaîne.
{% endinfo %}

#### Nettoyage des données

Une fois nos données correctement extraites de notre base de données, nous allons les nettoyer, comme vu précédemment. Ici, après avoir affiché nos 100 premières chaînes de caractères, nous observons des guillemets au début de chaque commentaire, mais qui ne sont jamais fermés. Nous allons donc les remplacer par rien pour nettoyer nos valeurs.

```python
# Création de la fonction de nettoyage adaptée
def nettoyage(ligne):
    nouvelle_ligne = [colonne.replace('"', '') for colonne in ligne]
    return nouvelle_ligne

# Appliquer nettoyage à chaque ligne dans base_de_donnees
base_de_donnees_propre = [nettoyage(ligne) for ligne in base_de_donnees]

```

#### Créer des fichiers texte contenant les avis regroupés par score

Notre base de données regroupe maintenant une note correspondant à un avis. L’idée est donc de rassembler, pour chaque note (de 0 à 5), chaque avis correspondant dans un fichier texte. Ainsi, nous pourrons rechercher, pour chaque score, le mot qui ressort le plus et voir s'ils diffèrent.

```python
# Créer la fonction pour créer des fichiers textes contenant les avis par score
def texte_par_note(b_d_d, score, nom_fichier_texte):
    with open(nom_fichier_texte, "w") as fichier:
        for ligne in b_d_d:
            if ligne[1] == str(score):
                fichier.write(ligne[0] + "\n")

# Appliquer la fonction pour chaque score
texte_score_0 = "avis_score_0.txt"  
texte_par_note(base_de_donnees_propre, 0, texte_score_0)

texte_score_1 = "avis_score_1.txt"  
texte_par_note(base_de_donnees_propre, 1.0, texte_score_1)

texte_score_2 = "avis_score_2.txt"  
texte_par_note(base_de_donnees_propre, 2.0, texte_score_2)

texte_score_3 = "avis_score_3.txt"  
texte_par_note(base_de_donnees_propre, 3.0, texte_score_3)

texte_score_4 = "avis_score_4.txt"  
texte_par_note(base_de_donnees_propre, 4.0, texte_score_4)

texte_score_5 = "avis_score_5.txt"  
texte_par_note(base_de_donnees_propre, 5.0, texte_score_5)
```

#### Supprimer du texte les “stop words”

Une fois nos fichiers textes créés, nous allons chercher le mot le plus utilisé dans les avis d’un score donné. Cependant, si nous effectuons cette opération directement sur nos commentaires, le mot qui ressortira sera probablement ce que l’on appelle un **stop word**. Nous allons donc supprimer tous les stop words de nos textes afin de pouvoir effectuer notre comptage des mots par la suite. Étant donné que les commentaires sont en espagnol, nous allons récupérer en ligne une liste de stop words en espagnol.

{% info %}
Un **stop word** est un mot courant qui est souvent ignoré dans le traitement du langage naturel et l'analyse de texte. Ces mots, comme "et", "ou", "le", "la", et "de" en français, n'apportent généralement pas d'information significative au sens du texte et peuvent être filtrés pour simplifier l'analyse. L'élimination des stop words permet de se concentrer sur les mots qui portent plus de sens et d'améliorer l'efficacité des algorithmes d'analyse.
{% endinfo %}

Nous en profitons aussi pour venir supprimer les signes de **poncuation** car ils sont inutiles et risquent de venir perturber notre analyse.

```python
#Créer une liste de short word en espagnol à partir d'un fichier texte
with open("stop_words_spanish.txt","r") as lexique :
    stop_word = [ligne.strip().lower() for ligne in lexique.readlines()]

# Créer une fonction qui permet à partir d'un fichier texte de retirer la ponctuation, puis les stop words
def sans_stop_word(texte, mot_inutile, texte_filtre):
    with open(texte, "r") as f:
        contenu = f.read()  
    mots = contenu.lower().split()  
    ponctuation = ".,;:!¡?¿'\"()[]{}-"
    mots_sans_ponctuation = [''.join(char for char in mot if char not in ponctuation) for mot in mots]
    mots_filtres = [mot for mot in mots_sans_ponctuation if mot not in mot_inutile]
    with open(texte_filtre, "w") as fichier:
        fichier.write(" ".join(mots_filtres))  
    return texte_filtre

# Appliquer la fonction à chaque fichier
texte_ssw_score_0 = "avis_ssw_score_0.txt"
sans_stop_word(texte_score_0, stop_word, texte_ssw_score_0)

texte_ssw_score_1 = "avis_ssw_score_1.txt"
sans_stop_word(texte_score_1, stop_word, texte_ssw_score_1)

texte_ssw_score_2 = "avis_ssw_score_2.txt"
sans_stop_word(texte_score_2, stop_word, texte_ssw_score_2)

texte_ssw_score_3 = "avis_ssw_score_3.txt"
sans_stop_word(texte_score_3, stop_word, texte_ssw_score_3)

texte_ssw_score_4 = "avis_ssw_score_4.txt"
sans_stop_word(texte_score_4, stop_word, texte_ssw_score_4)

texte_ssw_score_5 = "avis_ssw_score_5.txt"
sans_stop_word(texte_score_5, stop_word, texte_ssw_score_5)
```

#### Compter les mots les plus fréquents dans le texte en fonction de la note

On va venir ici, compter pour chaque fichier texte regroupant les avis par note, les 1O mots les plus utilisés ainsi que leur occurrence dans le texte. On va ensuite venir regrouper ces résultats dans un unique fichier texte.

```python
# Créer une fonction comptant les occurrences des mots dans le texte et renvoie les 10 plus fréquents
def compter_mots(fichier):
    with open(fichier, "r") as f:
        contenu = f.read()
    mots = contenu.split()
    compteur = {}
    for mot in mots:
        compteur[mot] = compteur.get(mot, 0) + 1
    mots_frequents = sorted(compteur.items(), key=lambda x: x[1], reverse=True)[:10]
    return mots_frequents

# Créer un fichier pour enregistrer les résultats
fichier_resultats = "resultats_des_scores.txt"

def resultat(fichier_texte, score, fichier_avis):
    mots_frequents = compter_mots(fichier_avis)
    with open(fichier_texte, "a") as file:
        file.write(f"Les mots les plus utilisés dans les avis de note {score} sont : {mots_frequents}\n")

# Appeler la fonction pour chaque score
for score in range(6):
    resultat(fichier_resultats, score, f"avis_ssw_score_{score}.txt")
```

{% note %}
On utilise ici la notion de dictionnaire pour stocker les résultats de notre comptage. Cette notion est abordée plus en détail dans mon [MON 1.1](https://francoisbrucker.github.io/do-it/promos/2024-2025/Esther-Henry/mon/temps-1.1/).
{% endnote %}

{% info %}

- La fonction **sorted( )** permet de trier des itérables, comme des listes ou des tuples. Elle prend en entrée un itérable et retourne une nouvelle liste contenant les éléments triés. La syntaxe de sorted() est **sorted(iterable, key=None, reverse=False)**. Le paramètre **key** permet de spécifier une fonction qui détermine l'ordre de tri (par exemple, tri par une certaine valeur dans des tuples), tandis que le paramètre **reverse** permet de trier en ordre décroissant si défini à True.
- La fonction **lambda** est une manière de créer des fonctions anonymes, c'est-à-dire des fonctions sans nom, en une seule ligne. Elle est souvent utilisée pour des opérations simples où une fonction temporaire est requise. La syntaxe générale est **lambda arguments: expression**, où **arguments** sont les paramètres que la fonction prend et **expression** est le résultat retourné.
{% endinfo %}

Qui nous retourne :

- **Les mots les plus utilisés dans les avis de note 0 sont** : [('comida', 647), ('excelente', 436), ('lima', 262), ('servicio', 205), ('experiencia', 171), ('restaurante', 165), ('almuerzo', 126), ('atención', 112), ('rico', 112), ('delicioso', 109)]
- **Les mots les plus utilisés dans les avis de note 1 sont** : [('atención', 3523), ('comida', 2405), ('mala', 2278), ('pollo', 1293), ('mal', 1222), ('pésima', 1219), ('servicio', 1152), ('pésimo', 963), ('atencion', 917), ('sabor', 779)]
- **Les mots les plus utilisés dans les avis de note 2 sont** : [('atención', 2146), ('comida', 1831), ('mala', 829), ('pollo', 810), ('sabor', 775), ('calidad', 732), ('regular', 646), ('falta', 618), ('servicio', 549), ('atencion', 500)]
- **Les mots les plus utilisés dans les avis de note 3 sont** : [('comida', 6872), ('atención', 6500), ('rico', 3501), ('agradable', 2664), ('pollo', 2249), ('falta', 1833), ('mejorar', 1809), ('sabor', 1741), ('regular', 1738), ('platos', 1653)]
- **Les mots les plus utilisés dans les avis de note 4 sont** : [('comida', 19386), ('atención', 16686), ('rico', 12214), ('excelente', 7719), ('agradable', 7038), ('pollo', 5532), ('platos', 4694), ('ambiente', 4379), ('sabor', 3871), ('atencion', 3762)]
- **Les mots les plus utilisés dans les avis de note 5 sont** : [('excelente', 42239), ('comida', 36600), ('atención', 35102), ('rico', 25955), ('pollo', 9649), ('delicioso', 9075), ('servicio', 9035), ('agradable', 7800), ('atencion', 7617), ('platos', 7531)]

#### Conclusion

- Première conclusion : ici, nous voyons que **l’orthographe** joue un rôle important dans ce genre d’analyse, car nous avons plusieurs fois “atencion” et “atención” qui ressortent comme deux mots différents, alors qu’il s’agit du même mot mal orthographié, ce qui vient un peu fausser les résultats.
- En vue du résultat, nous pouvons présupposer que **les avis de note 0** ne sont pas réellement des avis de notes 0, car les mots qui ressortent sont plutôt très positifs, comme “excelente”, “rico” et “delicioso”.
- Pour le reste, **certains mots ressortent pour chaque note** comme “atención”, “servicio”, ou encore “comida” et “pollo” (ce qui n’est pas étonnant au Pérou, car le “pollo” fait partie des plats les plus consommés). Nous pouvons alors nous demander si, dans le cadre de notre analyse, il n’aurait pas fallu les rajouter à notre liste de stop-words afin de n’avoir que des mots faisant sens du point de vue de l’avis des consommateurs.
- Sinon, nous constatons quand même que pour **les avis de note 1**, les mots utilisés sont **plutôt négatifs**, tels que “mala”, “mal”, “pesima” et “pesimo”, alors que pour **les avis de note 5**, les mots sont plutôt connotés **positivement**, comme “excelente”, “rico”, “delicioso” et “agradable”, ce qui est ce que nous aurions pu présupposer.

![Comida Lima](./images/comida_lima.webp)

PS : Le choix de ce sujet a été motivé par mon amour pour le lomo saltado, et notamment les meilleurs que j'ai mangés à Lima.

### Horodatage

| Date | Heures passées | Indications |
| -------- | --------- | --------|
| Jeudi 19/09 | 2H | Gérer les fichiers |
| Vendredi 20/09 | 1H | Ensemble d'élément |
| Mercredi 02/10 | 2H | Manipuler du texte |
| Jeudi 03/10 | 2H | Choix base de données & Début analyse |
| Vendredi 04/10 | 2H | Analyse suite |
| Dimanche 06/10 | 2H | Analyse fin |

### Bibliographie

{% lien %}

- [Python pour les SHS](https://pur-editions.fr/product/7857/python-pour-les-shs)
- [Stop Words](https://countwordsfree.com/stopwords/french)
- [Peruvian Food Reviews](https://www.kaggle.com/datasets/lazaro97/peruvian-food-reviews)
- [Python: Trier le contenu d'un dictionnaire](https://www.quennec.fr/trucs-astuces/langages/python/python-trier-le-contenu-dun-dictionnaire-dict#:~:text=Pour%20trier%20un%20objet%20dict,valeurs%20sont%20converties%20en%20tuple.&text=On%20voit%20que%20l'ordre,n'a%20pas%20été%20conservé.)
{% endlien %}
