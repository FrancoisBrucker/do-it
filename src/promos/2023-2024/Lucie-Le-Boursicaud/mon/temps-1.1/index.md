---
layout: layout/mon.njk

title: "MON 1 : Initiation à C++"
authors:
  - Lucie Le Boursicaud

date: 1970-09-01

tags: 
  - "temps 1"

résumé: "Dans ce MON l'objectif est de découvrir un nouveau langage informatique dans lequel je n'ai aucune base. A la fin des 10h de cours j'espère savoir coder de petits algorithmes simples en C++."
---

## Sommaire

1. Présentation du langage
2. Syntaxe du C++
3. Premiers algorithmes

## 1.Présentation du langage
Le langage C++ est apparu dans les années 90 et il est aujourd'hui devenu un langage très utilisés et indispensable pour certains programmeur. Son grand atout est sa fonctionalité de classe permettant d'utiliser la programmation object comme en JAVA. 

## 2. Syntaxe du C++
#### Type de variable 
Comme d'autres langages le C++ possède plusieurs type de variables :  
+ vide : void  - aucune voriable ne peut être de ce type
+ enter : char - petit entier de -128 à 127 
          short - grand entier de -32768  à 32767
          long - très grand entier 
          int - coïncide avec short ou long en fonction de l'initiation 
+ réels : float - précision de 7 chiffres
          double - précision de 15 chiffres 
          long double - précision de 18 chiffres

Parfois on pourra rencontré le type ***unsigned*** , il s'agit d'un entier dit "non signé".

#### Déclarer une variable 
Il est nécessaire de déclarer une variable avant de devoir l'utiliser en C++.
Pour déclarer une variable on utilise la syntaxe suivante : *type liste_de_variables*.
Exemples :
```html
 int a, b, c;    // déclare trois entiers a,b et c
 const float Taille = 1.67;  // déclare une constante de type float
 const Nom = 'Lucie'; // déclare une constante littérale
```
#### Les différents opérateurs
+ "+" : addition
+ "-" : soustraction
+ "*" : multiplication
+ "/" : donne le quotient (entier si il s'agit de deux entiers)
+ "%" : donne le reste modulo entre deux entiers
Exemples :
```html
 20.0 / 3.2    donnera  6.25
 15 / 8       donnera 1
 15 % 8       donnera 7
```
