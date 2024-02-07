---
layout: layout/mon.njk

title: "Faire du clean code"
authors:
  - TAING Henri

date: 2024-02-07

tags:
  - "temps 3"
  - Bonnes pratiques
  - HTML
  - CSS
  - JS
  - Python

résumé: "Quoi ? Il y a des conventions pour la manière d'écrire le code ? Une convention par langage en plus ?! Mon dieu, il est temps de nettoyer tout ce code sale et de rénover le site du projet 3A !"
---

{%prerequis 'MON débutant'%}
Savoir lire du code
{%endprerequis%}

---

## Table des matières

1. [Introduction](#section-1)
2. [PEP 8 pour Python et Google HTML/CSS Style Guide et Google JavaScript Style Guide](#section-2)
3. [Nettoyage du code et Rénovation du site](#section-3)
4. [Conclusion](#section-4)
5. [Sources](#section-5) 

## 1. Introduction <a id="section-1"></a>

Cherchant un poste à l'étranger en IT pour mon premier, mes choix sont assez restreints au vu de mes compétences techniques limitées. 
Pour autant, ce n'est pas une raison de ne pas les valoriser en mettant en avant les projets effectués à l'école et sur mon temps libre, avec un lien github par exemple qui donne sur du clean code.
Dans ce MON, nous verrons les principales conventions utilisées pour rédiger du code et vous aurez un avant-après du site du projet 3A. Le but étant pour moi, aussi, d'intégrer tout le code que j'ai écrit.

## 2. PEP 8 pour Python et Google HTML/CSS Style Guide et Google JavaScript Style Guide <a id="section-2"></a>

Le but de ses conventions est définir des règles de format et de style pour le code afin de promouvoir la collaboration et la compréhension. L'idée est d'écrire du code qui soit lisible et consistent pour faire en sorte que sa lecture ne soit pas une souffrance visuelle en plus d'intellectuelle. 
Ces guides sont mis à jour régulièrement pour suivre l'évolution de la programmation. 

Les principaux points relèvent de :
- l'indentation, par exemple, en Python, il faut faire en sorte soit de s'aligner sur le délimiteur ouvert (parenthèse, strophe, crochet) ou d'ajouter 4 espaces pour séparer les arguments du reste ou en alignant les autres lignes par rapport à la première. Et on va préférer les espaces (avec la touche espace) que les "tabs",

{% details "Exemple calqué sur celui du guide" %}

```
#  Aligné avec le délimiteur ouvert.
f = drole(v1, v2,
          v3, v4)

#  Ajout de 4 espaces (crée un autre niveau d'indentation) pour dinstinguer les arguments du reste.
def fonction(
        a1, a2, a3,
        a4):
    print(a1)

#  "S'aligner sur la première ligne" ou encore s'aligner sur "hanging indent"".
fonction = f(
         b1, b2,
         b3, b4)

```

{% enddetails %}

- le nombre de caractères par ligne, en Python, on conseillera 79 caractères, pour JavaScript 80, 
- les espaces dans le code, on évitera les espaces inutiles du genre, 

{% details "Un autre exemple calqué sur celui du guide" %}

```
#  Ok.
petitdej(jambon[1], {fromage: 2})

#  Ah nan.
petitdej( jambon[ 1 ], { fromage: 2 } )
```

{% enddetails %}

- les commentaires dans le code, il faut que ce soient des phrases complètes, explicites et compréhensibles avec une majuscule au début et utilisés si et seulement si ils aident à la compréhension du code
- les noms des variables, fonctions, etc, par exemple, ne jamais utiliser "l", "O", qui peuvent être confondus avec "1" et "0", écrire le nom des variables en miniscules, etc. 
- des recommandations générales du type : 
{% details "Autres exemples calqués sur celui du guide" %}

```
#  Ok:
def f(x): return 2*x

#  Ah nan, on évite lambda !:
f = lambda x: 2*x

#  Ok:
if booleen:

# Ah nan, le booleen donne déjà l'information du True ou False:
if booleen == True:

```

{% enddetails %}


## 3. Nettoyage du code et Rénovation du site <a id="section-3"></a>


## 4. Conclusion <a id="section-4"></a>

J'ai passé un peu plus que 10h sur le MON, mais c'était un pur plaisir. Les graphes parlent d'eux-mêmes. Ce n'est pas tous les jours qu'on a une démonstration empirique de la superficialité de notre espèce en quelques graphes super jolis. 

## 5. Sources <a id="section-5"></a>

[PEP 8 - Style pour Python](https://peps.python.org/pep-0008/#fn-hi)
[Google JavaScript Style Guide](https://google.github.io/styleguide/jsguide.html)
[Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html)
