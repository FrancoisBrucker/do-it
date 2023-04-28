---
layout: layout/mon.njk

title: "Programmation objet en Python"
authors:
  - Nicolas BERT

date: 2022-10-19

tags:
  - 'temps 1'
---

<!-- début résumé -->
POO en Python (Temps 1)
<!-- fin résumé -->

## La programmation orientée objet

La programmation orientée objet, également abrégée POO, est un paradigme de programmation et une manière de penser différente de celle que l'on connait habituellement qui est la programmation procédurale.

L'idée de la programmation objet est d'encapsuler les données(i.e. les attributs) et les fonctions (i.e. les méthodes) dans des objets et ainsi les rendre disponibles uniquement aux objets qui en ont besoin.

| **Programmation procédurale**                                                   | **Programmation orientée objet**                                                   |
|---------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| Le programme est découpé en petites parties appelées **fonctions**.             | Le programme est découpé en petites parties appellées **objets**                   |
| Il n'y a pas de spécificateur d'accès.                                          | L'accès aux données est réglémenté : public, private, protected ...                |
| Les fonctions utilisent des **données globales**.                                   | Les objets utilisent ses **propres données**.                                          |
| La logique est pensée de **manière globale** et le code est difficilement scalable. | La logique est pensée à **petite échelle** (objet) et le code est facilement scalable. |

<div style="display: flex; align-items: center;">
  <div style="width: 50%; display: flex; flex-direction: column; align-items: center;">
    <img src="./../images/procedurale.png" style="border: 0;" />
    <p>La programmation procédrale</p>
  </div>
  <div style="width: 50%; display: flex; flex-direction: column; align-items: center;">
    <img src="./../images/orientee-objet.png" style="border: 0;" />
    <p>La programmation orientée objet</p>
  </div>
</div>

### Ressources

Ce petit MON se base sur le [cours de François Brucker](https://francoisbrucker.github.io/cours_informatique/cours/algorithme-code-th%C3%A9orie/code/programmation-objet/).

## Un jeu de bataille

Dans ce cours j'ai réalisé comme il est suggéré dans le cours de François de Brucker à la section 7 un petit jeu en ligne de commande permettant de faire combatter deux personnages. Je fais ici combattre un magicien contre un nain. Vous pourrez retrouver mon code sur [GitHub](https://github.com/nbert71/POO-Python).

<div style="display: grid; place-items: center;">
  <img src="./../images/gandalf-gimli.png" style="width: 50%;" />
</div>

### La classe Character

J'ai d'abord commencé par créer une classe Character représentant un personnage avec un nom et nombre de points de vie. Je définis également des méthodes pour récupérer le nom ou le nombre de points de vie et les modifier : ce sont respectivement les getters et les setters. Je crée également une fonction visant à afficher les informations du personnage.

```python
class Character:
    
    def __init__(self, name, hp):
        self.__name = name;
        self.__hp = hp;

    def getName(self):
        return self.__name
    
    def getHp(self):
        return self.__hp

    def loseHp(self, damage):
        self.__hp -= damage
    
    def gainHp(self, heal):
        self.__hp += heal

    def display(self):
        print(type(self).__name__  + " " + self.getName())
        print('- HP : ' + str(self.getHp()))   
```

La notation `__attribut` "permet" de gérer des attributs privés mais ce n'est qu'une facette puisqu'en réalité ces attributs ne sont pas privés. On garde tout de même cette syntaxe et les getters/setters pour respecter le principe Open/Closed (cf [MON de Tuncay](https://francoisbrucker.github.io/do-it/mon/TBi/MON/POO/))

### La classe Dwarf

J'ai ensuite créé la classe Dwarf qui hérite de la classe Character qui représente un nain. Le nain possède une méthode *attack* qui enlève 20 points de vie à l'adversaire.

```python
from Character import *

class Dwarf(Character):
    
    def __init__(self, name, hp=80):
        super().__init__(name, hp)  # on appelle le constructeur de la classe parente
        self.__damage = 20

    def display(self):
        super().display()   # on appelle la méthode display de la classe parente
        print("- Damage : " + str(self.__damage))

    def attack(self, player):
        player.loseHp(self.__damage)

```

### La classe Magician

J'ai enfin crée la classe Magician qui hérite elle aussi de la classe Character. Le magicien possède en plus une barre de mana qui lui permet de lancer des sorts. Il possède une méthode attack pour attaquer une autre joueur tout en consommant un peu de sa mana, attention cette méthode ne peut se lancer que si le magicien à encore de la mana. Il dispose aussi d'une méthode pour régénérer ses points de vie.

```python
from Character import *

def checkMana(self, cost):
    if self.getMana() >= cost:
        return True
    else:
        print("Vous n'avez pas assez de mana pour lancer ce sort !")
        return False

class Magician(Character):

    __spellCost = 10

    def __init__(self, name, hp=100):
        super().__init__(name, hp)
        self.__mana = 50
        self.__damage = 10

    def display(self):
        super().display()
        print("- Mana : " + str(self.getMana()))
        print("- Spell cost : " + str(self.__spellCost))
        print("- Damage : " + str(self.__damage))
    
    def getMana(self):
        return self.__mana

    def attack(self, player):
        if checkMana(self, self.__spellCost):
            player.loseHp(self.__damage)
            self.__mana -= self.__spellCost
        else:
            print('Vous gagner 30 points de mana')
            self.__mana += 30
        
    def heal(self):
        if checkMana(self, self.__spellCost):
            self.gainHp(40)
            self.__mana -= self.__spellCost
      
```

Les relations entre les classes sont résumées dans le diagramme UML suivant.

<div style="display: grid; place-items: center;">
  <img src="./../images/uml-poo.png" style="border: 0;">
</div>

## La mécanique de jeu

J'ai ensuite programmé la logique de jeu. Tout d'abord le jeu nous demande de créer nos deux personnages et de leur donner un nom chacun. Ensuite tour à tour, chaque personnage joue. Le combat continue tant que les deux personnages sont encore en vie.

```python
def play(player1, player2):
    while player1.getHp() > 0 and player2.getHp() > 0:
        turn(player1, player2)
        if player2.getHp() > 0:
            turn(player2, player1

    if player1.getHp() <= 0:
        winner = player2
    else:
        winner = player1
    print(winner.getName() + ' a gagné !')
```

## Conclusion

Durant ce MON j'ai appris comment faire de la programmation orientée objet en python de manière assez simple. Je vois également et cela se ressent à la pratique, que Python n'est pas un langage très adapté pour l'orienté objet. En effet, il n'y a pas de notions de public ou privé, tout est public ce qui va un peu à l'encontre des principes de la POO. De plus, le fait qu'il ne soit pas un langage typé ne facilte pas les choses. J'ai cependant pu expérimenter la POO en Python.





