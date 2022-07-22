---
layout: base-layout.njk 
title: Markdown possibilités
date: 2019-06-01
tags: ['post']
---

Les possibilités d'édition en markdown

## liens

* [post 2 chemin relatif](../post-2)
* [post 2 chemin absolu]({{ "/blog/post-2" | url }})
* [post 2 chemin relatif avec une ancre](../post-2#images)
* [post 2 chemin absolu avec une ancre]({{ "/blog/post-2" | url }}#images)


## algorithmes

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

```python
permutations(T):
l = [1, 3, 2, 6, 4, 5]
print(l.max())
```

## images {#images}

![WTFs/minute](../wtfm.jpg){style="margin: auto;display: block"}

> Notez le `..` qui est important dans tous les liens.
{.note}

## équations

$$
2+2 = \frac{1}{2}
$$

Et un $\log(3)^2$ dans une phrase.

## details

{% details "spoiler" %}
Quelque chose de caché.
{% enddetails %}