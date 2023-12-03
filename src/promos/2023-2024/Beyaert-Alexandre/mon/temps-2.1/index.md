---
layout: layout/mon.njk

title: "Bibliothèques Python pour la Data Science : NumPy, Matplotlib et Pandas"
authors:
  - Alexandre Beyaert

date: 1970-11-01
tags: 
  - "temps 2"

résumé: "Un MON traitant de l'utilisation des bibliothèques Python pour la Data Science."
---

{% prerequis %}
**Niveau :** Facile
**Prérequis :** Bases en Python
{% endprerequis %}

## Sommaire

1. Introduction
2. Bibliothèque NumPy 
3. Bibliothèque Matplotlib
4. Bibliothèque Pandas
5. Combinaison des bibliothèques
6. Conclusion
7. Bibliographie

## 1. Introduction

quid sklearn et seaborn

## 2. Bibliothèque NumPy
```python
import numpy as np
```

La bibliothèque NumPy permet de faciliter l'application de calculs numériques en Python en introduisant aux tableaux.

Ces tableaux à N dimensions s'avèrent être bien plus utiles que les listes en Data Science dans la mesure où :
- leur coût mémoire est moins important que celui des séquences
- ils présentent beaucoup plus de méthodes que ces dernières et permettent une plus grande flexibilité et facilité dans les calculs.

### Construire un tableau NumPy
Commençons alors par regarder comment créer ces tableaux.

Il est dans un premier temps possible de créer un tableau "à la main", en retrant nous même chacune des valeurs grâce à la fonction array.

```python
>>>A = np.array([1, 2, 3])
array([1, 2, 3])
>>>B = np.array([[0, 2 ,4], [1, 2, 3]])
array([[0, 2, 4],
       [1, 2, 3]])
```
On peut également préremplir le tableau de zéros ou de 1 :
```python
>>>C = np.zeros((3,2))
>>>C
array([[0., 0.],
       [0., 0.],
       [0., 0.]])

>>>D = np.ones((3,4))
array([[1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.]])
```
Enfin, il est également très utile de pouvoir remplir les tableaux avec des nombres aléatoires grâce aux fonctions du modules random.
En particulier :
- la fonction rand qui génère des valeurs aléatoires provenant d'une distribution uniforme sur l'intervalle [0,1]
- la fonction randn qui génère des valeurs aléatoires issus de la distribution normale centrée en 0
- la fonction randint qui génère des valeurs entières aléatoires de façon uniforme dans un intervalle donné


```python
>>>E = np.random.randn(3,4)
>>>E
array([[ 0.32146014, -1.38563513,  0.346344  , -1.60361699],
       [-0.26914238,  0.156633  , -0.16439682, -0.96573034],
       [ 0.27903539,  0.69972398, -0.73055932,  0.47816189]])

>>>F = np.random.rand(4,2)
>>>F
array([[0.55901839, 0.33178598],
       [0.534862  , 0.93134297],
       [0.52179033, 0.51332815],
       [0.13075336, 0.31464172]])

>>>G = np.random.randint(101, size=(2,4))
>>>G
array([[49, 43, 33, 27],
       [78, 27, 11, 95]])
```
### Quelques attributs utiles
- ndim : dimension du tableau
- shape : forme du tableau (tuple). Cette fonctionnalité est particulièrement utile lorsque nous faisons du Machine Learning avec Python. Elle permet d'éviter de nombreuses étourderies lorsque l'algorithme effectue des opérations sur les matrices. Dans le cas d'une matrice à 2 dimensions; shape renvoie le nombre de lignes puis de colonnes.
- size : nombre d'éléments dans le tableau

```python
>>>A = np.array([[1,2],[2,3],[4,5]])
>>>A.ndim
2
>>>A.shape
(3, 2)
>>>A.size
6
```

## 3. Bibliothèque Matplotlib
## 4. Bibliothèque Pandas
## 5. Combinaison des bibliothèques
## 6. Conclusion
## 7. Bibliographie

https://numpy.org/doc/stable/user/absolute_beginners.html
https://courspython.com/apprendre-numpy.html
https://www.youtube.com/playlist?list=PLO_fdPEVlfKqMDNmCFzQISI2H_nJcEDJq

