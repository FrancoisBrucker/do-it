---
layout: layout/mon.njk

title: "Programmation orientée objet"
authors:
  - Agathe Rabachou

date: 2023-10-18

tags: 
  - "temps 1"
  - "POO"
  - "Python"
  - "débutant"

résumé: "Ce MON a pour but de m'initier aux bases de la programmation orientée objet et de l'appliquer à des exemples simples en Python"
---
## 1. Introduction

La programmation orientée objet (abrégée POO) est un modèle qui a pour but de simplifier l'écriture, la lecture et la modification d'un code. Pour cela, l'idée est de segmenter et de factoriser au maximum le code en regroupant ce qui se répète dans des entités que l'on peut réutiliser et faire interagir entre elles au besoin.

Dans ce MON, mon objectif est de m'approprier les notions de bases de la programmation orientée objet, et de l'utiliser sur des applications simples en Python.
Contrairement à ce que je pensais, je me suis rendu compte que j'avais très peu de restes de mes connaissances du langage Python, et j'ai donc dû passer plus de temps que prévu à revoir la syntaxe et les fonctionnalités de base. J'ai utilisé pour cela les 8 premiers chapitres du livre [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) en ligne. Cela m'a permis de me remettre en mémoire les principaux types de données, leur écriture et les opérations possibles sur chacune d'entre elles.
Ensuite, j'ai suivi la première moitié du cours [Programmation Objet](https://francoisbrucker.github.io/cours_informatique/cours/algorithme-code-th%C3%A9orie/code/programmation-objet/) de François Brucker et j'ai aussi regardé en détail l'exemple traité dans le MON [Programmation objet en Python](https://francoisbrucker.github.io/do-it/promos/2022-2023/Bert-Nicolas/mon/poo-python/) de Nicolas Bert.

## 2. Principes et définitions

Lorsque l'on fait de la programmation orientée objet, on manipule des objets et des classes. Voici quelques définitions du vocabulaire courant :

- Un **objet** est une structure de données précise qui prend en paramètres des valeurs appelées **attributs** qui lui sont propres. Sur cet objet, on peut effectuer différentes opérations que l'on nomme aussi **méthodes**.
Les chaînes de caractères, les entiers ou encore les listes sont des objets simples inclus dans le langage Python.

- Une **classe** est un ensemble d'objets qui possèdent la même structure de données et auxquels on peut appliquer les mêmes **méthodes**. Ces objets sont donc uniquement différenciés par leurs **attributs**. A partir d'une classe existante, on peut donc créer un **objet** qui a d'office une certaine structure et des opérations associées, il ne reste alors qu'à attribuer des valeurs à ses champs.
Pour reprendre un des exemples précédents, on pourrait imaginer une classe qui contient toutes les listes d'entiers de taille 4 (ce sont bien des objets, leurs attributs sont les valeurs des éléments de la liste), et lui associer une méthode qui remplace la dernière valeur de la liste par 7.

- Pour appeler une méthode et l'appliquer à un objet issu d'une classe associée, on utilise ce que l'on appelle la **notation pointée**. On note alors : **objet.méthode(a, b, c...)** où a, b et c sont les paramètres de la méthode.

- Enfin, on décrit parfois les classes et les objets que l'on utilise grâce à une représentation synthétique issue du langage **UML**, pour *Unified Modeling Language*. Elle se traduit dans ce cas par le diagramme ci-dessous :
|Nom de la classe|
|:--------------:|
|Liste des attributs, propres à chaque objet, avec leur type|
|Liste des méthodes, avec leurs nom et paramètres, que l'on peut appliquer aux objets de la classe|

## 3. Applications simples

Après avoir assimilé ces différents concepts et leur utilité dans la programmation de certains modèles, j'ai pu les mettre en application dans des exemples simples issus du [cours](https://francoisbrucker.github.io/cours_informatique/cours/algorithme-code-th%C3%A9orie/code/programmation-objet/) de François Brucker :

1. Le premier exemple simule un dé que l'on peut lancer, dont on peut lire la valeur, et également que l'on peut lancer jusqu'à obtenir une certaine valeur choisie, on peut dans ce cas récupérer le nombre de lancers qui ont été nécessaires pour atteindre cette valeur.

Voici la modélisation du dé : 
```py
import random

class Dé:
    def __init__(self, position_initiale=1):
        self.position = position_initiale

    def lancer(self):
        self.position = random.randint(1, 6)
```

Les tests associés :
```py
from dé import Dé

def test_init():
    d = Dé()
    assert isinstance(d, Dé)

def test_position():
    d = Dé()
    assert d.position == 1

def test_position():
    d = Dé(4)
    assert d.position == 4

def test_lancer():
    d=Dé()
    assert 1 <= d.position <= 6
```

Et le code principal du jeu :
```py
from dé import Dé

position_initiale = int(input("Position initiale :"))
valeur_arrêt = int(input("Valeur pour laquelle arrêter les lancers :"))

d = Dé(position_initiale)
i = 0
while d.position != valeur_arrêt:
    d.lancer()
    i+=1
print(i)
```

2. Dans un deuxième temps, j'ai modélisé un jeu de cartes que l'on mélange et dans lequel on tire trois cartes:

```py
SEPT = "sept"
HUIT = "huit"
NEUF = "neuf"
DIX = "dix"
VALET = "valet"
DAME = "dame"
ROI = "roi"
AS = "as"

PIQUE ="pique"
COEUR = "coeur"
CARREAU = "carreau"
TREFLE = "trefle"

VALEURS = [SEPT, HUIT, NEUF, DIX, VALET, DAME, ROI, AS]
COULEURS = [TREFLE, CARREAU, COEUR, PIQUE]

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        v = self.valeur
        c = self.couleur
        print(v + " de " + c)

#opérations de comparaison pour une potentielle suite du MON où l'on crée un jeu avec les cartes

    def __eq__(self, carte2):
        print (self.valeur == carte2.valeur and self.couleur == carte2.couleur)

    def __ne__(self, carte2):
        print (self.valeur != carte2.valeur or self.couleur != carte2.couleur)

    def __lt__(self, carte2):
        if self.valeur < carte2.valeur :
            return True
        elif self.valeur == carte2.valeur :
            return COULEURS.index(self.couleur) < COULEURS.index(carte2.couleur)
        else :
            return False
        
    def __gt__(self, carte2) :
        if self.valeur > carte2.valeur :
            return True
        elif self.valeur == carte2.valeur :
            return COULEURS.index(self.couleur) > COULEURS.index(carte2.couleur)
        else :
            return False
        
    def __le__(self, carte2) :
        if self.valeur <= carte2.valeur :
            return True
        elif self.valeur == carte2.valeur :
            return COULEURS.index(self.couleur) <= COULEURS.index(carte2.couleur)
        else :
            return False
        
    def __ge__(self, carte2) :
        if self.valeur >= carte2.valeur :
            return True
        elif self.valeur == carte2.valeur :
            return COULEURS.index(self.couleur) >= COULEURS.index(carte2.couleur)
        else :
            return False
```

Avec les tests associés :
```py
from carte import *
import random

def test_init():
    c = Carte(SEPT, PIQUE)
    assert c.valeur == SEPT
    assert c.couleur == PIQUE

def test__str__():
    c = Carte(SEPT, PIQUE)
    assert c.__str__ == "sept de pique"

```

Et le jeu en lui même :
```py
import random
from carte import *

PAQUET = [Carte(SEPT, TREFLE), Carte(HUIT, TREFLE), Carte(NEUF, TREFLE), Carte(DIX, TREFLE), Carte (VALET, TREFLE), Carte(DAME, TREFLE), Carte (ROI, TREFLE), Carte(AS, TREFLE),
          Carte(SEPT, CARREAU), Carte(HUIT, CARREAU), Carte(NEUF, CARREAU), Carte(DIX, CARREAU), Carte (VALET, CARREAU), Carte(DAME, CARREAU), Carte (ROI, CARREAU), Carte(AS, CARREAU),
          Carte(SEPT, COEUR), Carte(HUIT, COEUR), Carte(NEUF, COEUR), Carte(DIX, COEUR), Carte (VALET, COEUR), Carte(DAME, COEUR), Carte (ROI, COEUR), Carte(AS, COEUR),
          Carte(SEPT, PIQUE), Carte(HUIT, PIQUE), Carte(NEUF, PIQUE), Carte(DIX, PIQUE), Carte (VALET, PIQUE), Carte(DAME, PIQUE), Carte (ROI, PIQUE), Carte(AS, PIQUE)]

#userstory => tirer 3 cartes dans un paquet mélangé

random.shuffle(PAQUET)

cartes_tirees = random.sample(PAQUET, 3)

for i in range (len(cartes_tirees)):
    carte = cartes_tirees[i]
    print(carte)
```

J'ai ensuite réfléchi à la suite de ce TD qui a pour but de créer une sorte de bataille avec ce jeu de cartes et les fonctions de comparaison, mais je n'ai pas eu le temps de l'implémenter proprement.

## 4. Pour approfondir

Enfin, pour aller un peu plus loin dans la prise en main de ce modèle de programmation et de ses applications, j'ai parcouru le chapitre [Héritage](https://francoisbrucker.github.io/cours_informatique/cours/algorithme-code-th%C3%A9orie/code/programmation-objet/h%C3%A9ritage/) du cours, les exemples associés, ainsi que la suite des chapitres de [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/), mais je n'ai pas eu le temps de les mettre en pratique par moi-même.