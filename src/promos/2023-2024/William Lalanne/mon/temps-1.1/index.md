---
layout: layout/mon.njk

title: "Titre du premier MON du temps 1"
authors:
  - William Lalanne

date: 2023-09-01

tags: 
  - "temps 1"

résumé: "Dans ce MON je souhaite approfondir mes connaissances en CSS"
---

{% prerequis %}
**Niveau :** Moyen
**Prérequis :** Bases en HTML et CSS
{% endprerequis %}

## Sommaire

1. Introduction
2. Comment bien organiser sa page avec CSS ? 


## 1. Introduction
Pour ce premier MON, je me suis servi de plusieurs ressources afin de tirer le meilleur de chaque document. Voici les sites que j'ai utilisé : 
- [Openclassroom](https://openclassrooms.com/fr/courses/5295881-create-web-page-layouts-with-css/5341491-set-media-queries-for-different-devices)
- [CSS-Tricks](https://css-tricks.com/snippets/css/complete-guide-grid/)

Dans ce MON, je voulais approfondir mes connaissances en CSS et particulièrement sur les *Grid*, les *Flex-box* qui sont des éléments très importants.



## 2. Les Grid
### Qu'est ce que c'est et à quoi ça sert ? 
Lorsque l'on veut coder une page web, il faut que chaque élément de la page soit à la bonne place. Pour cela, il peut être utile d'utiliser une grid, ou un tableau en français. Un tableau est un ensemble de lignes et de colonnes de différentes tailles dans lequel on peut mettre des éléments de la page. 
Le plus simple pour comprendre est de prendre un exemple :
![exemple de gridd]

Dans l'image précédente, on peut voir que la page web est constituée d'un tableau qui permet de disposer de manière simple les différents éléments voulus. 


### Créé un tableau
Pour créer un tableau, il faut d'abord créer un *container* c'est un élément HTML qui va contenir d'autres éléments, comme c'est le cas dans l'exemple suivant : 
`<div class="container">`
    `<div>Premier élément</div>`
    `<div>Deuxième élément</div>`
    `<div>Troisième élément</div>`
    `<div>Quatrième élément</div>`
`</div>`


Pour l'instant on a simplement créé un élément avec d'autres à l'intérieur, il faut ensuite préciser que cet élément est un tableau. Pour cela, dans le fichier CSS il suffit d'une simple ligne de code : 
`.container {
    display: grid;
}
`
Cette ligne permet simplement de dire que l'élément de class "container" doit être considéré comme un tableau. 


## Modifier les propriétés du tableau
Une fois le tableau créé, on peut préciser combien de lignes on souhaite avoir et combien de colonnes. 


