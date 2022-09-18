---
layout: layout/post.njk

title: "MON de Tuncay : POO"
authors:
  - Tuncay Bilgi

tags: ['mon']
---

<!-- début résumé -->
MON: POO python.
But : Possedant les bases de la POO , le but du MON est d'étudier et mettre en oeuvre son implémentation en python.
Resultat : [Mon Repo GitHub.](https://github.com/TuncayBilgi/heelo-dev/tree/main/Python/POO)
<!-- fin résumé -->
Le MON balaie les notions suivantes :

 - POO en python:
	 - Base de POO :Classe, Constructeurs, getter, setter, héritage
	 -  Design patterns
 - Spécificités avancées de Python :
	 - @decorateurs
	 - @staticmethod et @classmethod
	 - @property
	 - Metaclasses
	
 - TDD :
	 - La philosophie
	 - pytest

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

Chaque classe est accompagné d'un fichier test.py qu l'on evoquera à la fin et d'un fichier main.py qui permet de montrer quelques fonctionnalités de la classe et des spécificités de son implémentation.

A retenir :
En python tout se fait a travers des fonctions et il existe plusieurs methodes d'implementer la meme chose.
Les getter et les setters semblent inutiles au début en python puisque les attributs ne sont pas réellement privés (_attributprivé n'est qu'une convention) mais ils sont très important car ils permettent de respecter le principe Open/Closed er que quand l'on doit modifier le comportement d'un getter, on est heureux de n'avoir à le faire qu'une fois dans la classe plutôt que partout dans le code.

### Les Design Patterns

Les design Patterns sont des schémas d'implémentation de systèmes qui permettent de répondre à des problèmes bien spécfiques.
En effet, si la structure des classes de votre projet se détériore trop et devient plus compliqué que complexe, il est probable qu'un design pattern mettre de l'odre dans le projet.
Cependant les designs en tant que tels sont assez obscurs et dur à comprendre sans implémentation concrete quand le probleme se pose dans un projet.
Vous pouvez retrouver ces designs [ici](https://refactoring.guru/design-patterns) avec des exemples en python.

## Les Spécificités de Python.

Python est un language où tout est un objet. Chaque fonction et chaque variable est un objet qui appartient à une classe (et oui cette classe est elle meme un objet.)
Grâce à cela, on peut modifier des fonctionnements très profond de python grâce à la POO.

### Les Getters et Setters façon python.
Comme dit précédement, les getters et setters sont dans une position assez particulière en python.
D'un coté, ils sont indispensable pour avoir un code maintable mais de l'autre, ils vont a l'encontre de la philosophie de python. En effet, ils rajoutent de la complexitée dans le code et ils perdent un de leur role qui est d'assurer le coté privé d'un attribut.
Ainsi `dé.position='lol'` peut etre utilisé malgré le fait que l'on a définit `def set_compteur(self,value): assert isinstance(value,int)`, comme on peut le voir avec la classe Dice et son fichier main.
Pour eviter se comortement, on créer des @property, qui permettent d'appeller les setters que l'on a implémenté, même avec `dé.position=`