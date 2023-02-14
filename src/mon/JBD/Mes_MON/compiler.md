---
layout: layout/post.njk

title: "Compilateurs"
authors:
  - Jean-Baptiste Durand

tags :
  - 'Compilateur'
  - 'Yacc et Lex'
  - 'C'
  - 'Structures de données'
---

<!-- début résumé -->
Terminer le compilateur en ajoutant des fonctionnalités complexes (variables, boucles, fonctions)
<!-- fin résumé -->

{% prerequis "" %}
La lecture de mon [premier MON](https://francoisbrucker.github.io/do-it/mon/JBD/Mes_MON/yaccLex/) sur le sujet n'est pas nécessaire pour la compréhension de ce MON mais est important pour la compréhension du projet.
{% endprerequis %}

<h2 id="toc"> Table des matières </h2>

- [Table des matières](#toc)
- [Évolution du projet](#h1)
  - [Avant](#h1-1)
  - [Après](#h1-2)
- [Liens Utiles](#liens)

<h2 id="h1">Évolution du projet</h2>

Le résultat obtenu après le premier MON n'était pas satisfaisant, et avait une utilité limité. C'est pourquoi j'ai décidé de reprendre le projet pour ce MON.

<h3 id="h1-1">Avant</h3>

```python
print(-(7+1)*3);
print(2>=1 && 6!=5+1);
```

<h3 id="h1-2">Après</h3>

<div class="codeContainer">
<div>

```python
if
```

</div>
<div>

```python
while
```

</div>
<div>

```python
function
```

</div>
</div>

<h2 id="liens">Liens Utiles </h2>


<style>
    .codeContainer{
        display: flex;
        flex-direction: row;
        width:100%;
        justify-content: space-evenly;
    }
</style>
