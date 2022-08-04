---
layout: layout/post.njk 
title: Les possibilités d'édition en markdown
date: 2019-06-01
tags: ['post', 'markdown']
---

Comparer le résultat au [code source](https://raw.githubusercontent.com/FrancoisBrucker/do-it/main/src/blog/possibilite-markdown.md).

## titre `##`

### titre `###`

#### titre `####`

##### titre `#####`

## liens

* [post 2 chemin relatif](../post-2)
* [post 2 chemin absolu]({{ "/blog/post-2" | url }})
* [post 2 chemin relatif avec une ancre](../post-2#images)
* [post 2 chemin absolu avec une ancre]({{ "/blog/post-2" | url }}#images)

## listes

### non ordonnées 

* un
* deux
* trois

### ordonnées

1. un
2. deux
3. trois

## quotes

> Une quote normale
> sur deux lignes.


> Une mise en garde.
{.attention}


> Une note à retenir.
{.note}

> Un chemin/vers/un article
{.chemin}


## algorithmes

### programme

```python
permutations(T):
l = [1, 3, 2, 6, 4, 5]
print(l.max())
```

### avec lignes numérotées

```text#
si T est vide:
    rendre [T] # la liste contenant toutes les permutation de de T, c'est à dire T
L = []  # va contenir les permutations de T
pour chaque i allant de 0 à len(T) - 1:
    soit a = T[i]
    soit T' la liste contenant tous les éléments de T sauf T[i]
    soit L' = permutations(T')
    pour chaque P' de L':
        P = concaténation de [a] et de P'
        ajoute P à la fin de L
rendre L
```

### dans le texte 

* par défaut : `l = [1, 3, 2, 6, 4, 5]`
* on dit que c'est un langage : `l = [1, 3, 2, 6, 4, 5]`{.language-python}.

## images {#images}

![WTFs/minute](../wtfm.jpg)

> Notez le `..` qui est important dans tous les liens.

## équations

$$2+2 = \frac{1}{2}$$

Et un $\log(3)^2$ dans une phrase.

## details

### dans le texte

{% details "spoiler" %}
Quelque chose de caché. Que l'on peut *écrire* en `Markdown` 
{% enddetails %}

### dans un exercice

{% exercice %}
Un exercice à faire.

{% details "corrigé" %}
Le corrigé de l'exercice.
{% enddetails %}

{% endexercice %}

## tables

On utilise les possibilités de [multimardown](https://fletcher.github.io/MultiMarkdown-6/syntax/tables.html)

### de base 

| titre colonne 1  | titre colonne 2 |
| ---------------- | --------------- |
| Content Cell     | Content Cell  |
| Content Cell     | Content Cell  |


### sans titre



| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |


### multi-colonne


| ------------- | ------------- |
|     Content Cell             ||
| Content Cell  | Content Cell  |


### multi-ligne

| ------------- | ------------- |
| Content Cell  | Content Cell  |
| ^^            | Content Cell  |

### plusieurs ligne dans une cellule

| ------------- | ------------- |
| Content Cell  | * Content Cell  | \
| Content Cell  | * Content Cell  |
| Content Cell  | Content Cell  |


### alignement horizontal

| :- | :-: | -: |
| Content Cell  | Content Cell  | Content Cell |
| Content Cell  | Content Cell  |Content Cell  |
| Content Cell  | Content Cell  |Content Cell  |


### alignement vertical

On ajoute un style, mais il ne faut pas que ce soit la dernière colonne. 

| ------------- | ------------- |
| Content Cell  {style="vertical-align:middle"}| Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eleifend, orci nec pharetra lacinia, lacus dolor euismod ipsum, quis pulvinar ipsum urna non purus. Cras accumsan ex ligula, eu pellentesque mauris congue ac. Integer venenatis elementum est ac imperdiet. Etiam lectus purus, imperdiet gravida commodo non, faucibus at metus. Maecenas elit nibh, venenatis a efficitur vitae, placerat vitae nulla. Fusce volutpat nisl sem, vel iaculis risus sagittis vel. Nunc felis tellus, sollicitudin eu felis vel, cursus egestas arcu. Sed laoreet ex a nisl vestibulum, id placerat leo pellentesque. Praesent nec ultrices purus, ut congue elit. Pellentesque in diam ultrices purus volutpat lacinia. | 
| Content Cell  | Content Cell  |

Pour la dernière colonne, il faut ajouter une colonne vide : 

| ------------- | ------------- | - |
| Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eleifend, orci nec pharetra lacinia, lacus dolor euismod ipsum, quis pulvinar ipsum urna non purus. Cras accumsan ex ligula, eu pellentesque mauris congue ac. Integer venenatis elementum est ac imperdiet. Etiam lectus purus, imperdiet gravida commodo non, faucibus at metus. Maecenas elit nibh, venenatis a efficitur vitae, placerat vitae nulla. Fusce volutpat nisl sem, vel iaculis risus sagittis vel. Nunc felis tellus, sollicitudin eu felis vel, cursus egestas arcu. Sed laoreet ex a nisl vestibulum, id placerat leo pellentesque. Praesent nec ultrices purus, ut congue elit. Pellentesque in diam ultrices purus volutpat lacinia. | Content Cell  {style="vertical-align:middle"}| | 
| Content Cell  | Content Cell  | |

