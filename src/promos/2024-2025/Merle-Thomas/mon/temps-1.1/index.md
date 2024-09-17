---
layout: layout/mon.njk

title: "Apprendre HTML/CSS pour un débutant en Dev Web"
authors:
  - Thomas Merle
date: 2024-09-08

tags: 
  - "temps 1"
  - "Developpement FrontEnd"
  - "HTML"
  - "CSS"

résumé: "Grâce à ce MON, je souhaite apprendre les languages HTML et CSS dans l'objectif de me lancer dans le codage de mon 1er site web de Dark Kitchen.
Pour réaliser ce MON et débuter mon apprentissage, j'ai décidé de suivre les cours du site de Mr Brucker, ainsi que de suivre un tutoriel disponible en ligne et recommandé par le site do-it. Il s'agit du tutoriel [`W3School`](https://www.w3schools.com/html/default.asp). Ce tutoriel permet d'apprendre les notions de bases de HTML/CSS et est accompagné d'exercices de codes sur un éditeur en ligne."
---

{% prerequis %}

Aucun prérequis nécessaires.

{% endprerequis %}
{% lien %}

[`W3School`](https://www.w3schools.com/html/default.asp)
[`POK1: Asian Fried Rice - FrontEnd`](https://francoisbrucker.github.io/do-it/promos/2024-2025/Merle-Thomas/pok/temps-1/)

{% endlien %}

Quelques phrases permettant de connaître, sans jargon ni blabla, le contenu de ce MON. On oubliera pas de donner :

- le niveau et les prérequis nécessaires en utilisant la balise [`prerequis`](/cs/contribuer-au-site/#prerequis)
- les autres POK & MON en rapport en utilisant la balise [`lien`](/cs/contribuer-au-site/#lien)

## Contenu

## 1.HTML

#### <span style="color: #26B260">Généralités
Les sigles « HTML » sont l’abréviation de **« HyperText Markup Language »**. Le HTML est donc un langage de **balisage**, c’est-à-dire un langage qui va nous permettre de définir les différents contenus d’une page.

Tout d’abord, qu’est-ce qu’un site internet ? Un site internet est un ensemble de fichiers de code et de medias (images, videos, etc.) liés entre eux et disponibles à tout moment via le web. Pour que les différentes ressources constituant un site internet soient toujours accessibles, on les héberge généralement sur un **serveur** d’un hébergeur.

Comment accède-t-on à une page d’un site internet ? Notre navigateur va contacter le serveur sur lequel est hébergée la page à laquelle on souhaite accéder et lui demander de renvoyer les différents éléments de la page : la page sous forme de **code HTML** et potentiellement les différents médias intégrés dans la page. Le navigateur va donc recevoir ces différents éléments et les afficher en utilisant le code HTML.

Voici ci-dessous le code minimum pour créer une page HTML valide :
```
<!DOCTYPE html>
<HTML>
<HEAD>
    <title>Titre du document<title>
    <meta charset="utf-8">
    en-tête du document
</HEAD>
<BODY>
    corps du document
</BODY>
</HTML>
```
Comme son nom l’indique, le **doctype** sert à indiquer le type du document.
L’élément meta sert lui à transmettre des meta informations sur la page au navigateur. La valeur *utf-8* est la valeur de référence pour tous les alphabets latins.

#### <span style="color: #26B260">Les éléments HTML
Le langage HTML tout entier repose sur l’utilisation d’**éléments**. Dans une page, nous allons utiliser les éléments en HTML pour marquer du contenu, c’est-à-dire pour lui donner du sens aux yeux des navigateurs et des moteurs de recherche.

**<span style="color: purple">1. Les balises HTML**
   
Une balise peut prendre trois formes. La première, la plus simple, un simple nom d'élément encadré par les signes inférieur et supérieur. Dans un deuxième temps, la balise peut porter sur une partie précise du document, auquel cas, elle doit s'ouvrir et se refermer. Enfin, il peut être nécessaire de préciser le comportement de la balise, cela se fait avec des **attributs**.

| Elément de base  | Definition |
| :--------------- |-----|
| html | root of an HTML document |
| body  | document's body |
| p | paragraph |
| h1 to h6 | HTML headings |
| br  | line break |
| a | hyperlink |
| img | used to embed an image |
| b | Bold text |
| strong | Important text |
| i | Italic text |
| em | Emphasized text |
| mark | Marked text |
| small | Smaller text |
| del | Deleted text |
| ins | Inserted text |
| sub | Subscript text |
| sup | Superscript text |
| blockquote | section that is quoted from another source |
| abbr | abbreviation or acronym |

**<span style="color: purple">2. Les attributs HTML**

Les éléments vont également pouvoir contenir des **attributs** qu’on va alors placer au sein de la balise ouvrante de ceux-ci. Pour certains éléments, les attributs vont être facultatifs tandis que pour d’autres ils vont être obligatoires pour garantir le bon fonctionnement du code.

| Attribut | Definition |
| :--------------- |-----|
| style | add styles to an element |
| href  | link's destnation |
| target | where to open the linked document |
| src | path to the image |
| alt  | specifies an alternate text for an image |
| lang | to declare the language of the Web page |
| title | defines some extra information about an element |
| width and height | provides size information for images |


**<span style="color: purple">3. Focus sur l'indentation et les commentaires**

Indenter va nous permettre d’avoir un code plus propre et plus lisible, donc plus compréhensible. Indenter permet également de plus facilement **détecter les erreurs** potentielles dans un code.
Note : Les retours à la ligne et l’indentation créés dans l’éditeur n’affectent pas le résultat final dans le navigateur.

Les commentaires ne seront pas affichés par le navigateur lorsque celui-ci va afficher la page : ils ne vont servir qu’aux développeurs créant ou lisant le code. Les commentaires en HTML vont prendre la forme d’une **balise orpheline** très particulière : 
```
<!--Commentaire-->
```

**<span style="color: purple">4. Les listes**

Il est possible en HTML de définir différents types de listes :
* des **listes non ordonnées** (élément ul, l'élément li permet de définir chaque item) ;
* des **listes ordonnées** (élément ol, l'élément li permet de définir chaque item) ;
* des **listes de définition** (dl, lh, dt et dd).

**<span style="color: purple">5. Les entités**

Une **entité HTML** est une suite de caractère qui est utilisée pour afficher un caractère réservé ou un caractère invisible.
* "&nbsp" : ajouter une espace simple dit espace « insécable » ;
* "&ensp" : créer une espace double ;
* "&emsp" : créer une espace quadruple ;
* "&thinsp" : créer un espace très fin (demi-espace).

**<span style="color: purple">6. Les tables**

| Attribut | Definition |
| :--------------- |-----|
| table |	Defines a table|
| th |	Defines a header cell in a table|
| tr |	Defines a row in a table|
| td |	Defines a cell in a table|
| caption | Defines a table caption|
| colgroup |	Specifies a group of one or more columns in a table for formattingv|
| col |	Specifies column properties for each column within an element|
| thead |	Groups the header content in a table|
| tbody |	Groups the body content in a table|
| tfoot |	Groups the footer content in a table|

**<span style="color: purple">7. Block/Inline Elemnent**
* Un **élément de niveau bloc** commence toujours sur une nouvelle ligne et occupe toute la largeur disponible;
* Un élément en ligne ne démarre pas sur une nouvelle ligne et prend uniquement la largeur nécessaire; 
* L'**élément div** est au niveau bloc et est souvent utilisé comme conteneur pour d'autres éléments HTML.
* L'**élément span** est un conteneur en ligne utilisé pour baliser une partie d'un texte ou une partie d'un document.


## 2.CSS


## Horodateur

Toutes les séances et le nombre d'heure que l'on y a passé.

| Date | Heures passées | Indications |
| -------- | -------- |-------- |
| Vendredi 06/09  | 1H  | Lecture du cours do-it dév Web et recherche d'un tutoriel |
| Mardi 10/09  | 2H  | HTML : Structure de base en HTML, balises et attributs|
| Vendredi 13/09  | 2H  | HTML : En-tête, paragraphes, commentaires, styles et couleurs |
| Samedi 14/09  | 1H  | HTML : Listes et tables |
| Dimanche 15/09  | 1H  | HTML : début du codage du FrontEnd du site de Dark Kitchen |