---
layout: layout/mon.njk

title: "POO"
authors:
  - Tuncay Bilgi

date: 2022-10-07

tags:
  - 'temps 1'
  - 'poo'
  - 'python'
---

<!-- début résumé -->
MON: POO python.
But : Possédant les bases de la POO , le but du MON est d'étudier et mettre en oeuvre son implémentation en python.
Résultat : [Mon Repo GitHub.](https://github.com/TuncayBilgi/heelo-dev/tree/main/Python/POO)
<!-- fin résumé -->

{%prerequis 'MON niveau intermédiare' %}
  - Avoir des bases en python.
{%endprerequis%}
Le MON balaie les notions suivantes :

 - POO en python:
	 - Base de POO : Classe, Constructeurs, getter, setter, héritage, interfaces
	 -  Design patterns
 - Spécificités avancées de Python :
	 - @decorateurs
	 - @staticmethod et @classmethod
	 - @property
	 - Metaclasses
	
 - TDD :
	 - La philosophie
	 - pytest

   Il a été réalisé en suivant deux ressources en particulier : 
   - [Cours de M.Brucker sur la POO en python](https://francoisbrucker.github.io/cours_informatique/cours/algorithme-code-th%C3%A9orie/code/programmation-objet/)
   - [MOOC python](https://www.youtube.com/playlist?list=PL2CXLryTKuwwV4NzULvBuchMipWgOvja-) avancé, à partir du chapitre 9.
   
   Tout cela accompagné de recherches sur StackOverflow pour répondre à des questions précises sur des concepts inconnus.

## La Programmation Orientée Objet :

La POO est une méthode de programmation suivant laquelle on manipule des objets.
Ces objets sont par exemple des instances de classes.
La POO permet de créer un code modulaire et factoriser qui respecte des principes précis que le considère être la bonne pratique à suivre si l'on veut créer un code qui pourra être utilisé et maintenu dans le temps et par des personnes différentes.

Dans ce MON  on considère comme acquis les notions de :
classes, instance, composition, agrégation, héritage, superclasse, méthode, attributs, UML

On se concentrera donc sur l'implémentation de ses concepts en python.

### La Base de la POO en python :

Pour apprendre les bases, j'ai suivi [le cours de M. Brucker.](https://francoisbrucker.github.io/cours_informatique/cours/algorithme-code-th%C3%A9orie/code/programmation-objet/)
Ce cours permet la création des classes ci-dessous :
 - [Panier](https://github.com/TuncayBilgi/heelo-dev/tree/main/Python/POO/Panier)
 - [Compteur](https://github.com/TuncayBilgi/heelo-dev/tree/main/Python/POO/Compteur)
 - [Dice (en partie)](https://github.com/TuncayBilgi/heelo-dev/tree/main/Python/POO/Dice)

Chaque classe est accompagné d'un fichier test.py qu l'on évoquera à la fin et d'un fichier main.py qui permet de montrer quelques fonctionnalités de la classe et des spécificités de son implémentation.

A retenir :
- En python tout se fait à travers des fonctions et il existe plusieurs méthodes d'implementer la meme chose.
- les fonctions `__nom__` sont des fonctions préconstruites. `__new__` et `__init__` sont des constructeurs, `__call__` permet de transformer la classe en callable etc...
- Les getter et les setters semblent inutiles au début en python puisque les attributs ne sont pas réellement privés (`_attributprivé` n'est qu'une convention) mais ils sont très important car ils permettent de respecter le principe Open/Closed er que quand l'on doit modifier le comportement d'un getter, on est heureux de n'avoir à le faire qu'une fois dans la classe plutôt que partout dans le code.
- Il faut faire en sorte que les attributs des classes soient des objets immutables, comme des int,list ou str. Cela permet d'éviter la modification involontaire des attributs par une variable intermédiaire.

### Les Design Patterns

Les design Patterns sont des schémas d'implémentation de systèmes qui permettent de répondre à des problèmes bien spécifiques.
En effet, si la structure des classes de votre projet se détériore trop et devient plus compliqué que complexe, il est probable qu'un design pattern mettre de l’ordre dans le projet.
Cependant les designs en tant que tels sont assez obscurs et dur à comprendre sans implémentation concrete quand le problème se pose dans un projet.
Vous pouvez retrouver ces designs [ici](https://refactoring.guru/design-patterns) avec des exemples en python.

## Les Spécificités de Python.

Python est un language où tout est un objet. Chaque fonction et chaque variable est un objet qui appartient à une classe (et oui cette classe est elle meme un objet.)
Grâce à cela, on peut modifier des fonctionnements très profond de python grâce à la POO.

### Les @décorateurs
Dans python, il existe la notion de callable, qui désigne tout les objets qui peuvent être appelé avec cette syntaxe : `objet()` . En pratique se sont tous les objets d'une classe qui possèdent une fonction `__call__`. Une fonction est donc un callable alors que `x=3` ne l'est pas. Ces callables peuvent prendre des paramètres,
il est très facile en python de créer callables qui prennent en paramètre d'autre callables, et qui renvoient un callable. Ainsi, on peut modifier une fonction grace à une autre fonction. Il existe une syntaxe pratique en python, celle des @decorators dont vous pouvez [voir ici un tuto vidéo](https://www.youtube.com/watch?v=hcBhtCo07EQ&list=PL2CXLryTKuwwV4NzULvBuchMipWgOvja-&index=2&ab_channel=CoursPython).

Ces décorateurs sont très pratiques, et il existe des décorateurs pré-construits dans python. Certains de ces décorateurs servent dans la POO, notamment dans la création de classe.


### Les Getters et Setters façon python.

Comme dit précédemment, les getters et setters sont dans une position assez particulière en python.
D'un coté, ils sont indispensable pour avoir un code maintenable mais de l'autre, ils vont a l'encontre de la philosophie de python. En effet, ils rajoutent de la complexité dans le code et ils perdent un de leur role qui est d'assurer le coté privé d'un attribut.
Ainsi `dé.position='lol'` peut être utilisé malgré le fait que l'on a définit :
```python
    def set_position(self,value):  #setter qui s'assure que la valeur de position reste un int
        assert isinstance(value,int)
        dé.position = value
```
	
comme on peut le voir avec la classe Dice et son fichier main.
Pour éviter se comportement, on créer des @property, qui permettent d’appeler les setters que l'on a implémenté, même avec `dé.position`. Ce sont donc des décorateurs pré-construits dans python avec une syntaxe particulière. Les créateurs de python préconisent cette manière de faire.
[Tuto vidéo disponible ici](https://www.youtube.com/watch?v=45R-gynfbnw&list=PL2CXLryTKuwwV4NzULvBuchMipWgOvja-&index=1&ab_channel=CoursPython) et un [un explication très détaillée ici](https://www.programiz.com/python-programming/property) 

### Les méthodes statiques et méthodes de Classe.

Ce sont des méthodes qui s'appliquent principalement a des classes (meme si grâce à la syntaxe des décorateurs on peut utiliser ces méthodes sur les instances).
Elles permettent d'atteindre, entre autre, les attributs de classe ( différents des attributs d'instance). En particulier, les méthodes de classe permettent de référencer la classe en paramètre, ce qui permet de mieux personnaliser la méthode selon les classes sous-classes qui en héritent. 
[Une explication claire ici](https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner) et un [Tuto vidéo la](https://www.youtube.com/watch?v=45R-gynfbnw&list=PL2CXLryTKuwwV4NzULvBuchMipWgOvja-&index=1&ab_channel=CoursPython)

### Les Métaclasses
En python,tout est un objet et tout objet est instancié par une classe. Aussi, tous les objets héritent de la superclasse "objet" et tous les classes sont elles meme un objet de la classe "type".
Type est une métaclasse, c'est une classe qui à pour but de d'instancier d'autres classes (alors qu'une classe crée des objets qui ne sont pas une classe).
Ainsi Type est une classe spéciale puisqu'elle est instancié par elle meme (type est une instance de type) et parce que c'est un objet qui hérite de "objet" qui est une classe instanciée par type aussi.

On voit donc que type et objet forment un couple important, l'origine de toutes les classes et l'origine de tous les objets. C'est eux qui vient construire toutes les classes et qui donnent a tous les objets leurs attributs et méthodes fondamentales.
En python, nous pouvons créer notre propre métaclasse et notre propre superclasse "objet" qui s'appelle plus généralement une Base. En créant ce couple, on peut créer tout un système de classe qui suivent de nouvelles règles non présente en python.
[Dans ce fichier]() on définit une métaclasse qui, quand elle instancie une classe, modifie le nom de toutes ses méthodes pour qu'elles respectent une typographie spécifique. On a aussi modifié la base de sorte à ce que les classes instanciés par la nouvelle métaclasse héritent d'une nouvelle base et non pas de "objet".

## Test Driven Développement

### La philosophie

Le TDD est une méthode de développement qui met en avant la création d'un code qui marche totalement.
Le but est de créer changer de méthode, au lieu de développer un code puis de tester si il marche, on écrit d'abord un test, et ensuite on écrit le code qui permet de réussir ce test.
Pour écrire ces tests à l'avance, on découpe les fonctions désirées en petites tâches et on associe a ses tâches des tests simples. Ensuite, on écrit le code le plus simple possible pour réussir les tests, et une fois que tous les tests sont réussis, on peut complexifier le code, tout en s'assurent que chaque modification ne fait échouer aucun test.
Pour que cela soit utile, il faut que les tests ont un bon "coverage" (idéalement 100%), c'est à dire que les tests couvrent 100% du code du programme et qu'a la fin,toutes les lignes soient testées.

Pour réaliser le TDD, on écrit tous nos tests dans un fichier à part, que l'on lance à chaque modification, et on vérifie que tout marche et que le coverage est à 100%.
C'est une tâche fastidieuse à réaliser à la main, il existe des librairies en python pour faire ça automatiquement.

### Pytest

Pytest est une librairie de test pour python, elle permet d'automatiser toutes les tâches liées au tests, et d'avoir des rapports détaillés sur le coverage et sur les erreurs rencontrées.
Pour commencer on installe la librairie :
`pip install -m pytest`
Et on créer des fichiers et des classes qui seront reconnues par pytest pour les lancer automatiquement. Les fichiers de type :
'maCLasse_test.py ou test_maClasse'
seront lancés automatiquement à l'appel de pytest.

Dans ses fichiers, on définit des fonctions test de type :
```
    def test_fonction():
        obj=maCLasse() # instance de maClasse
        ...
        assert montest #montest est une expréssion qui renvoie un booléen true ou false
```

Enfin, on appelle :
 - `pytest` pour simplement lancer la série de test est d'avoir le nombre de test passé et échouer.
 - `pytest -cov` pour en plus avoir les informations sur le coverage
 - `pytest -cov --cov:term-missing ` pour en plus avoir précisément les lignes non lues par les tests.

Des exemples peuvent être trouvés [ici](https://github.com/TuncayBilgi/heelo-dev/blob/main/Python/POO/Dice/dice_test.py), [là](https://github.com/TuncayBilgi/heelo-dev/blob/main/Python/POO/Dice/tapis_vert_test.py) et [par là](https://github.com/TuncayBilgi/heelo-dev/blob/main/Python/POO/Panier/panier_test.py).

# Conclusion :

## La POO en python :

En python, la programmation orientée objet est assez différente de celle de langages typés comme le Java. Il y a moins de règles auxquels il faut faire attention, certains concept, comme le concept d'attributs et de fonctions privés n'existent pas, et les design pattern qui font appel a des abstractions sont moins évidents à implémenter et on y voit moins l’intérêt. Par exemple, il n'y a pas le problème de dispatch comme en java.

## Les supports :

Le cours de M.Brucker est une bonne introduction. Les concepts de décorateurs, et plus particulièrement le `@property` devrait y figurer car c'est la manière actuelle et recommandée de créer des getters et setters en python.
De plus, quelques implémentations simples de design pattern seraient bienvenu, design faisant appel à des interfaces ou des classes abstraites notamment (c'est un point sur lequel j'ai encore beaucoup de mal).

Le MOOC python est bien fait et actuel avec des exemples, il reprend python depuis les bases jusqu'au fonctions avancées.


