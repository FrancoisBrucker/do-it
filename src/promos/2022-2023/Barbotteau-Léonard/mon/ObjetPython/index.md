---
layout: layout/mon.njk

title: "Le MON-2 de Léonard"
authors:
  - Léonard Barbotteau

date: 2022-10-19

tags:
  - 'temps 1'
---

<!-- début résumé -->
Python programmation orientée objet
<!-- fin résumé -->

## Description

Dans ce MON, je vais m'intéresser aux objets dans Python. Ayant déjà une certaine aisance avec Python et aimant bien ce langage, je vais pouvoir développer mes connaissances.

## Développement de mes connaissances en Python
Il est intéressant ans la vie de s'ouvrir à de nouvelles connaissances. Mais il est tout aussi important de les approfondir là où on les aime. Ce cours va m'y aider pour Python. Une fois n'est pas coutume, je vais réaliser ce cours à l'aide d'[openclassroom](https://openclassrooms.com/fr/courses/7150616-apprenez-la-programmation-orientee-objet-avec-python)

# Connaissances de base

## Présentation de la classe
Une <strong>classe</strong> contient d'une part un <strong>état</strong> (les variables/ données qu'elle contient) et d'autre part un <strong>comportement</strong> qui correspond à ce que la classe peut faire. Ce comportement est inclu dans les <strong>méthodes</strong> qui sont comme des fonctions associées à une classe spécifique.

Des <strong>objets</strong> sont donc créés en correspondance avec une classe. Le type d'un objet associé à une classe est la classe elle même.

## Syntaxe d'une classe
Voici l'exemple de l'écriture d'une classe:
~~~
class Epargne:
    capitalinitial = 1500
    interets = 0.05

    def calculate_income_first_month(self):
        return self.capitalinitial * self.interets
~~~
On peut voir au début deux variables qui lui sont associées, avec des données. Ensuite il y a une méthode qui est également associée à la classe.

## Construire une classe dynamique avec le constructeur __ init __
~~~
class Epargne:
    def __init__(self, capitalinitial, interets):
        self.capitalinitial = capitalinitial
        self.interets = interets
~~~

Ici on voit que les variables de la classe sont <strong>dynamiques</strong>, et on peut associer un objet à la classe épargne en remplaçant les attributs capitalinitial et interets par ce que l'on veut.

Dans l'exemple suivant:
~~~
class Epargne:
    def __init__(self, capitalinitial, interets=0.05):
        self.capitalinitial = capitalinitial
        self.interets = interets
~~~
Les intérêts sont de base à 0.05, on peut choisir en créant un objet de changer la valeur de cet attribut ou de la garder si on ne met rien.

## Créer ds objets grâce aux classes
Pour le premier exemple d'epargne, si on veut créer un objet on fait comme ceci:
~~~
    epargnetest = Epargne(10000, 0.02):
~~~

On peut bien évidemment le modifier par la suite:
~~~
    epargnetest.capitalinitial = 5000
~~~

Maintenant, regardons le premier exemple. On peut assigner le résultat de la méthode à une variable:
~~~
income_first_month = epargne.calculate_income_first_month:
~~~

## Différents types d'attributs

### Les attributs d'instance
Il sont définis à l'aide de <strong>self</strong>. Pour y accéder on doit faire une instanciation:

~~~
class Epargne:

    def __init__(self):
        self.interets = 0.05

    def argent(self):
        print("J'aime l'argent")
~~~
On doit donc faire une instanciation:
~~~
epargnetest = Epargne()

epargnetest.interets

epargnetest.argent()
~~~

### Les attributs de classe
Il sont définis dans le corps de la classe, et on utilise <strong>@classmethod</strong> avec un premier paramètre <strong>cls</strong>

~~~
class Epargne:

    banque = ("bnp", "creditagricole")

    @classmethod
    def argent(cls, monnaie):
        return("J'aime l'argent et surtout les", monnaie)
~~~
On peut récupérer les variables de classe sans instanciation
~~~
Epargne.banque
print(Epargne.argent(euros))
~~~

### Les attributs statiques
Ils n'ont quasiment pas de lien avec la classe, il faut éviter de les utiliser.

## Différentes fonctions utiles 
### Les propriétés
Les <strong>setters</strong> et <strong>getters</strong> permettent de récuperer ou changer la valeur d'un attribut en gardant une cohérence pour le programmeur, donner l'information. 
~~~
class Epargne:

    def __init__(self):
        self.interets = 0.05

    def _get_interets(self):
        print "Récupération des interets"
        return self.interets

    def _set_interets(self, change):
        print "Les interets ont changé"
        self.interets  =  change

    interets=property(_get_interets, _set_interets)
~~~
Si interets change, on aura un message.
Ce n'est pas obligatoire mais ça apporte de la clarté.

### La fonction dir, l'attribut __ dict __
La fonction <strong>dir</strong> permet de trouver les méthodes de l'objet, l'attribut <strong>__ dict __<strong> ses attributs.


## L'héritage
En gros, l'héritage permet de faire une <strong>sous-classe</strong> qui possède les mêmes attributs plus d'autres attributs spécifiques et d'autres méthodes, ou à l'inverse une super-classe qui en possède moins.
Cette méthode permet de simplifier le code.

### Syntaxe de l'héritage

~~~
class Epargne:

    def __init__(self, interets, capitalinitial):
        self.interets = interets
        self.capitalinitial = capitalinitial
~~~
On peut à partir de cette classe créer une sous-classe qui va rajouter des éléments
~~~
class SousEpargne(Epargne):
    def argent(self):
        print("J'aime l'argent")
~~~
On peut également remplacer les fonctions compléter les attributs:
~~~
class SousEpargne(Epargne):
    def __init__(self, interets, capitalinitial, banque):
        self.interets = interets
        self.capitalinitial = capitalinitial
        self.banque = banque
~~~

### Surcharge des méthodes
Lorsqu'une méthode a la même signature dans la classe <strong>enfant</strong>, elle prédomine sur la méthode de la classe <strong>parent</strong>.

En revanche il est possible d'accéder aux méthodes des parents depuis les classes enfants. (en utilisant la méthode super()).

### Classes abstraites
On peut créer une classe abstraite qui ne peut être instanciée et ne peut servir que pour des sous-classes. On utilise ABC:
~~~
from abc import ABC

class abstraite(ABC):
    def area(self):
        return 0
~~~

### Autres fonctionnalités de l'héritage
- On peut faire des hiérarchies d'héritage
- On peut faire un héritage multiple mais c'est assez compliqué à mettre en place

# Mise en application
Pour bien comprendre la programmation orientée objet, j'ai simplement fait des exercices sur internet sur un [site en anglais](https://www.my-courses.net/2020/02/exercises-with-solutions-on-oop-object.html), pour me familiariser avec les objets python.

