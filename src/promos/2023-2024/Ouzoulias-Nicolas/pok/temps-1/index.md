---
layout: layout/pok.njk

title: "Découverte du développement Web"
authors:
  - Nicolas Ouzoulias

date: 2023-09-17

tags: 
  - "temps 1"

résumé: Le premier POK de l'année pour apprendre à programmer un petit site Web.
---

Je n'ai jamais pratiqué le developpement Web je cherche donc à travers ce POK à : 
- Apprendre les bases du HTML
- Apprendre les base du CSS
- Les mettre en pratique en codant mon premier site

## Sommaire

I. Le développement Web pour les nuls

II. Mon petit site Web à moi

## I. Le développement Web pour les nuls

Tout d'abord pourquoi deux langages séparés et pas un seul ? 
Les deux fonctionnent de paire, le HTML permet de créer et de structurer le contenu tandis que le CSS s'occupe de la mise en forme visuelle. 

Le développement Web est divisé en 2 parties : 
- Le **front** : c'est la partie apparente du site (l'interface, les boutons, les menus, ...), c'est le lien direct avec l'utilisateur
- Le **back** : c'est les composantes cachées du site (les bases de données, les serveurs, l'infrastructure,...)

### Le HTML 

**Exemple de code HTML** 
```html 
<!DOCTYPE html>  <!--Indispensable en début de code car indique qu'il s'agit d'une page HTML-->
<html lang="fr">

<head>
    <meta charset="utf-8"> <!--Pour afficher les caractères spéciaux-->
    <title> Ceci est un titre </title>
</head>

<body>
    <!-- Le corps du site -->
    <img> <!-- Balise orpheline -->
</body>

</html>
```
Il existe ensuite de multiples **balises** pour organiser le texte et insérer des éléments comme par exemple : 
- `<p> </p>`  pour les paragraphes
- `<br>` pour les sauts de ligne
- `<h1> </h1>` jusqu'à 6 pour les niveaux de titres
- `<img>` pour insérer une image
- `<a>` pour les liens web

### Le CSS

 Le CSS étant un complément au HTML, il faut demander à ce dernier de l'appeler, pour cela on rentre la commande :
``` html
<head> <!-- Cela doit obligatoirement dans <head> -->
  <link href="style.css" rel="stylesheet">
</head>
```




## II. Mon petit site Web à moi

à definir ...