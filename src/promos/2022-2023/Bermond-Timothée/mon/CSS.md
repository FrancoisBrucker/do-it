---
layout: layout/mon.njk

title: "CSS et introduction à SASS"
authors:
  - Timothée Bermond

date: 2022-10-19

tags:
  - 'temps 1'
  - 'CSS'
  - 'SASS'
---

<!-- début résumé -->
Les bases du CSS et introduction à SASS
<!-- fin résumé -->

## Les bases du CSS

J'ai tout d'abord commencé par suivre la partie sur le CSS de cette [formation openclassrooms](https://openclassrooms.com/fr/courses/1603881-apprenez-a-creer-votre-site-web-avec-html5-et-css3).

Le CSS permet de faire la mise en forme son site (couleur du texte, police, mise en page,...).


<img src="../Images/index_sans_css.jpg">
Mon POK sans css.


<img src="../Images/index_avec_css.jpg">
Mon POK avec css.

Le CSS peut-être écrit dans un fichier *.css* (recommandé), dans l'en-tête du fichier html à l'aide d'une balise *style* ou directement dans les balises (non recommandé). Utiliser un fichier *.css* permet de facilement généraliser les propriétés à toutes nos pages html sans avoir à faire des copié-collé.

Pour appliquer un style nous pouvons sélectionner :
- une balise
- une classe
- un id

Pour ce faire on écrit le nom de la balise / classe / id puis on ajoute entre acolades les propriétés que l'on veut appliquer.

```css
balise{
  propriété1: valeur1;
  propriété2: valeur2;
}
```
Pour chaque propriété on doit indiquer une valeur.

On peut égalemement appliquer un style à plusieurs balises en les séparant d'une virgule.

```css
balise1, balise2{
  propriété1: valeur1;
  propriété2: valeur2;
}
```

### Formater du texte

Il est possible de modifier de nombreuses caractéristiques du texte.

**La taille**

Il est possible de modifier la taille du texte avec la propriété *font-size*. On peut indiquer une taille absolue ou une taille relative.
- Taille absolue 
On indique le nombre de pixels (ou cm, mm mais plus rare) :

```css
p{
  font-size: 14px;
}
```

- Taille relative
On peut écrire la taille en mot anglais :
  - xx-small
  - x-small
  - small
  - medium
  - large
  - x-large
  - xx-large
Ou indiquer la taille en *em* :
  - *1em* : taille normale
  - '>'1em : grossi le texte
  - <1em : rétrécit le texte

```css
p{
  font-size: 1.8em;
}
```

**La police**

Pour modifier la police il faut utiliser la propriété *font-family* suivi d'au moins une police. Le mieux est d'indiquer au moins 4 polices (séparées par des virgules) au cas où l'internaute n'aurait pas la 1ère police. (le navigateur essaiera tout d'abord d'utiliser a *police1*, s'il ne l'a pas il essaiera la *police2*, etc...)

**Italique**

Pour mettre en italique on utilise la propriété *font-style* et la valeur *italic*.

**Gras**

Pour mettre en gras on utilise la propriété *font-weight* et la valeur *bold*.

**Souligné**

Pour souligner ou décorer le texte on utilise la propriété *text-decoration* et les valeurs :
- *underline* : souligné;
- *line-through* : barré;
- *overline* : ligne au-dessus.

On peut également indiquer la valeur *none* si on veut annuler une des propriétés précédentes.

**L'alignement**

Il est possible d'appliquer tous les alignements connus avec la propriété *text-align* et les valeurs :
- *left* : aligné à gauche;
- *center* : centré;
- *right* : aligné à droite;
- *justify* : justifié.

### Ajouter de la couleur et un fond

**Couleur du texte**

On peut modifier la couleur du texte avec la propriété *color*. Pour les valeurs il y a plusieurs choix possibles :
- indiquer le nom de la couleur (en anglais), problème : avec cette méthode vous n'avez accès qu'à 16 couleurs que je ne listerai pas ici;
- utiliser la notation hexadécimale qui consiste à utiliser un # suivi de 6 caractères qui se lisent 2 par deux indiquant la quantité de rouge, de vert et de bleu;
- utiliser la méthode RGB, pour cela il faut taper *rgb(Rouge, Vert, Bleu)*.

**Couleur de fond**

Pour cela on utilise la propriété *background-color* et les mêmes valeurs que précédemment.

**Image de fond**

Pour cela on utilise la propriété *background-image* et en valeur *url("nom_de_l_image.png")*.

Avec la propriété *background-attachment* on peut décider :
- de faire défiler l'image de fond avec le texte : *scroll*;
- de laisser fixe l'image de fond : *fixed*.

Il est également possible de répéter ou non l'image de fond avec la propriété *background-repeat*.

Ou encore d'indiquer la position de l'image de fond avec la propriété *background-position*.

**Transparence**

Il est possible de jouer avec les niveaux de transparence des éléments avec la propriété *opacity* qui prend une valeur entre 0 et 1 (1:opaque, 0:transparent) ou en utilisant la notation RGBa qui consiste à ajouter une valeur comprise entre 0 et 1 à la notation RGB.

### Créez des bordures et des ombres ###

**Bordures standards**

Pour modifier l'apparence de la bordure on utilise la propriété *border* qui peut prendre jusqu'à 3 valeurs :
- la largeur : valeur en pixels (2px);
- la couleur : utiliser un des choix vu plus haut pour décider de la couleur;
- type de bordure : il existe 8 types différents de bordure.
<img src="../Images/types_bordures.jpg">

Il est également possible de ne sélectionner qu'une bordure avec les propriétés : 
- *border-top*
- *border-bottom*
- *border-left*
- *border-right*

On peut aussi arrondir les bordures avec la propriété *border-radius* et on indique l'importance de l'arrondi en pixels.

**Les ombres**

Il est possible d'ajouter l'ombre des boites avec la propriété *box-shadow* qui prend 4 valeurs :
1. Le décalage horizontzal
2. Le décalage vertical
3. L'adoucissement du dégradé.
4. La couleur de l'ombre.

Il est également possible d'ajouter la valeur *inset* qui place l'ombre à l'intérieur du bloc.

On peut aussi ajouter l'ombre du texte avec la propriété *text-shadow* qui prend les mêmes valeurs que *box-shadow*.

### Apparences dynamiques

Il est possible de modifier l'apparence du texte :
- au survol avec le pseudo-formats CSS *:hoover*
- lors du clique : *:active*
- lorsque l'élément est séléctionné : *:focus*
- lorsque le lien a déjà été consulté : *:visited*

### Structurer son site

**Les balises structurantes**

Des balises ont été introduites pour structurer les pages :
- l'en-tête : balise *header*
- le pied de page : balise *footer*
- principaux liens de navigation : balise *nav*
- des sections de page : balise *section*
- des informations complémentaires : balise *aside*
- un article indépendant : balise *article*

Ce qui donne a peu près :
<img src="../Images/balises_structure.jpg">

**Flexbox**

C'est la technique que j'ai principalement utilisé pour la mise en page de mon POK.

Le principe de la mise en page est simple :
On définit un conteneur dans lequel on place des éléments.
Le conteneur est une balise HTML et les éléments sont d'autres balises HTML à l'intérieur de cette balise :
```html
<div id="conteneur">
  <div class="element 1">Element</div>
  <div class="element 2">Element</div>
  <div class="element 3">Element</div>
</div>
```
Il faut ensuite ajouter la valeur *flex* à la propriété *display* du conteneur.

On peut maintenant modifier la direction avec la propriété *flex-direction* qui peut prendre les valeurs suivantes :
- *row* : sur une ligne
- *column* : sur une colonne
- *row-reverse* : sur une ligne en ordre inversé
- *column-reverse* : sur une colonne en ordre inversé

Afin de permettre aux éléments d'aller à la ligne si il n'y a plus de place il faut utiliser la propriété *flex-wrap*.

On peut ensuite aligner les éléments selon l'axe principal avec la propriété *justify-content* qui peut prendre différentes valeurs :
<img src="../Images/alignement_axe_principal.jpg">

Mais on peut également aligner les éléments sur l'axe secondaire avec la propriété *align-items* qui peut prendre différentes valeurs :
<img src="../Images/alignement_axe_secondaire.jpg">
Il est possible d'aligner un seul élément sur l'axe secondaire avec la propriété *align-self*.

La propriété *order* permet de changer l'ordre des éléments du conteneur.

Enfin la propriété *flex* peut autoriser les éléments à occuper plus ou moins d'espace restant. 
Par exemple :
```css
.element:nth-child(1)
{
    flex: 2;
}
.element:nth-child(2)
{
    flex: 1;
}
```
permet à l'élément 1 de grossir 2 fois plus que l'élément 1.

Il existe également d'autres manières de structurer les pages que je n'ai pas étudier durant ce MON.

## Simplification du CSS avec Sass

Dans une deuxième partie j'ai suivi cette autre [formation openclassrooms](https://openclassrooms.com/fr/courses/6106181-simplifiez-vous-le-css-avec-sass).


#### Structure du CSS

Il est très facile de se retrouver avec des fichiers .css brouillons et il devient alors très difficile et surtout long pour rien de modifier l'apparence de certaines parties de son site. C'est pourquoi il est important d'avoir un fichier .css bien structuré afin de gagner en efficacité.

**Principe du DRY**

Le principe DRY, signifiant "Don't Repeat Yourself", est très important : il ne faut pas que l'on retrouve des règles qui se répètent.
Dans mon POK par exemple on peut retrouver la répétion de la même règle pour deux balises différentes.
```css
#div_choix3{
    display: none;
}

#div_choix4{
    display: none;
}
```

J'ai donc ajouté une règle *.div_choix-hide* que j'applique à mes deux *div* en ajoutant *div_choix-hide* à leur classe.
On passe donc de ceci :
```html
<div id="div_choix4" class="div_choix">
```
A ceci :
```html
<div id="div_choix4" class="div_choix div_choix-hide">
```
J'ai fusionné mes deux règles redondantes en une seule :
```css
.div_choix-hide{
    display: none;
}

```
Ce qui me permet d'avoir un codebase plus facile à maintenir.

Je l'ai appliqué à mon POK et suis passé d'un fichier .css de plus de 300 lignes à un fichier de moins de 200 lignes.

**Spécificité**

Définition de la [documentation MDN](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Cascade_and_inheritance#specificity) :

La spécificité est la manière dont le navigateur décide quelle règle s’applique si plusieurs règles ont des sélecteurs différents, mais peuvent quand même s’appliquer au même élément.

C'est super compliqué à expliquer et je vais juste vous embrouiller donc allez checker vous même sur le [cours](https://openclassrooms.com/fr/courses/6106181-simplifiez-vous-le-css-avec-sass/6595695-structurez-votre-css#/id/r-7191892) où c'est très bien expliqué.

**BEM**

BEM est une convention CSS qui permet de rapidement s'y retrouver dans son code sans avoir à chercher des heures à quoi sert tel ou tel élément.

BEM est l'acronyme de bloc, élément, modificateur.

Comment ça fonctionne?

Tout d'abord, il faut construire des **blocs**, càd un composant qui est autonome et peut fonctionner indépendamment du reste de la page.
Par exemple, dans un portfolio, si on supprimait tout sauf le titre d'un projet il ne deviendrait qu'un bout de texte isolé. Alors que si on prend l'aperçu entier du projet (titre, image, description) là ça à du sens, on a donc un bloc que l'on va nommer en décrivant sa fontion : *.apercu-proj* et auquel on va assigner les règles spécifiques à ce bloc. 
Ensuite, on va nommer tous les **éléments** de ce bloc selon une nomenclature particulière : *bloc_parent__fonction_élément*. 
Ici, pour le titre on obtiendrait : *.apercu-proj__titre*. 
Enfin, pour des modifications spécifiques à un bloc ou un élément on va ajouter un **modificateur**. Là encore, il y a une nomenclature spéciale : *bloc/élément_modifié--style_modificateur*.
Dans notre cas, si on veut mettre un fond vert ça donnerait : *apercu-projet--vert*

### Sass

Sass est un préprocesseurs css, càd un outil qui permet de rédiger son code de manière plus cohérente visuellement.
Il est possible d'écrire du Sass dans des fichiers *.sass* ou *.scss*. La syntaxe est légèrement différente mais reste quand même très proche.

Dans ce MON nous allons nous concentrer sur les fichiers *.scss*.

Grâce à Sass, il est possible d'utiliser le **nesting**, càd l'imbrication des sélécteurs.
Au lieu d'écrire : 
```css
ul {
  list-style: none;
  text-align: right;
}

ul li {
  display: inline;
  font-size: 3rem;
  color: #D6FFF5;
}
```
On écrit :
```scss
ul {
  list-style: none;
  text-align: right;
  li {
      display: inline;
      font-size: 3rem;
      color: #D6FFF5;
  }
}
```

{% attention "**Attention** à ne pas créer des sélecteurs trop spécifiques." %}
On pourrait donc être tenté de reproduire une copie conforme de la structure de notre HTML.
Cela n'est pas une bonne idée car on va se retrouver avec des sélécteurs de haute spécificité qui seront très durs à modifier.
{% endattention %}

**Utiliser des sélécteurs BEM avec Sass**

On peut fusionner la méthodologie BEM et le nesting de Sass.

Pour cela on utilise les & ce qui nous permet d'être plus clair visuellement et de ne pas avoir à répeter le nom des blocs ou des éléments : 
```scss
.block{
  background-color: #15DEA5;
  &__element {
      color: #fff;
        &--modifier {
            background-color: #001534;
  }
  }
}
```

Ce qui nous donne en CSS compilé :

```css
.block {
  background-color: #15DEA5;
}

.block__element {
  color: #fff;
}

.block__element--modifier {
  background-color: #001534;
}
```

### Améliorer la maintenabilité du code avec les variables Sass

Afin de pouvoir rapidement modifier une valeur qui apparait de nombreuses fois dans le CSS, il est possible d'utiliser les variables Sass.
Par exemple, si l'on retrouve un grand nombre de fois la couleur vert menthe dans notre fichier, il est possible d'écrire *$color-primary: #15DEA5* au début de votre fichier .scss et puis de remplacer tous les *#15DEA5* par *$color-primary* dans le reste du fichier. Comme ça si l'on décide de changer la couleur principale de notre site il suffit de changer le code hexadécimal et tous les éléments changeront de couleur plutôt que de devoir les changer 1 à 1.

{% attention "Nommer la variable en fonction de son rôle" %}
On pourrait donc être tenté de nommer la variable *#mint* (vert menthe) mais si l'on change de couleur par du bleu alors il faudrait soit changer tous *#mint* du fichier soit juste changer le *$mint: #15DEA5* au début mais cela créérait une confusion car la couleur ne serait plus vert menthe mais bleu.
{% endattention %}

Il existe 8 types de variables dans Sass:
- les couleurs;
- les chaines de caractères
- les nombres
- les listes et maps
- les booléens, les nulls et les fonctions

### Les mixins Sass

Les mixins fonctionnent un peu comme une variable sauf qu'elles stockent des blocs entiers de code. 
C'est donc très pratique pour stocker des ensembles de règles CSS que l'on utilise fréquemment.
```scss
@mixin mixin-name {
  css-property: value;
}
```

Par exemple, si l'on veut ajouter des ombres à de nombreux textes on peut créer une mixin :
```scss
@mixin heading-shadow{
  text-shadow: .55rem .55rem #15DEA5;
}
```
Et puis l'ajouter dans notre sélecteur :
```scss
.form {
  &__heading {
      @include heading-shadow;
  }
}
```

Il est également possible d'ajouter des arguments à nos mixins :
```scss
@mixin heading-shadow($colour){
  text-shadow: .55rem .55rem $colour;
}
```
Ce qui nous permet ici d'appliquer les ombres de la couleur que l'on veut.

On peut régler la valeur par défaut qui sera utilisé en écrivant :
```scss
@mixin heading-shadow($colour: $colour-primary){
  text-shadow: .55rem .55rem $colour;
}
```
Si aucune couleur n'est spécifiée alors l'ombre sera de la couleur principale (colour-primary).

### Écrire du code plus propre grâce aux extensions Sass

Attention en utilisant trop de mixins cela créer une duplication de l'ensemble de règles dans le CSS compilé. Il comporte de multiples répétitions.

Heureusement, les extensions existent. Pour cela on utilise un placeholder, càd un bloc de code qui va être réutilisé dans les à l'aide de *@extend* pour les sélecteurs voulus.
```scss
%typography {
  color: $colour-primary;
  font-size: 2rem;
  font-weight: 100;
  line-height: 1.7;
}
h1 {
@extend %typography;
}
textarea {
  @extend %typography;
}
button {
  @extend %typography;
}
input {
  @extend %typography;
}
```
Ainsi lorsque l'on regarde le CSS compilé, il n'y a plus de répétitions mais une liste des sélecteurs concernés :
```css
h1, textarea, button, input {
color: #15dea5;
font-size: 2rem;
font-weight: 100;
line-height: 1.7;
}
```

### Mixins Vs Extensions

Bien que les extensions évitent les répétions, il est préférable d'utiliser les mixins. En effet, les extensions démolissent l'ordre et la prédictibilité du codebase. De plus, les extensions n'acceptent pas d'arguments contrairement aux mixins.

### Conditions dans Sass

Il est possible d'instaurer des conditions dans Sass.
Cela s'écrit :
```scss
@if ( lightness($colour) < 25% ) {
  $colour: lighten($colour, 10%);
}@else{
  $colour: darken($colour, 10%);
}
```
On peut donc créer des mixins modulables en fonctions de certains paramètres ;
```scss
@mixin heading-shadow($colour: $colour-primary, $size: $heading-shadow-size){
  @if ( lightness($colour) < 25% ) {
      $colour: lighten($colour, 10%);
  }@else{
      $colour: darken($colour, 10%);
  }
  text-shadow: $size $size $colour;
}
```

### Créer des fonctions 

Il est possible de créer des fonctions avec le *@function Nom_de_la_fonction(Arguments)*.
Pour récupérer une valeur on utilise *@return*.
Voici un exemple de fonction qui modifie la couleur :
```scss
@function lightness-shift($colour){
  @if ( lightness($colour) < 25% ) {
      @return lighten($colour, 10%);
  }@else{
      @return darken($colour, 10%);
  }
}
```

Je n'ai pas eu le temps de finir toute la formation openclassrooms, il me reste encore la dernière partie : ["Optimisez votre code en utilisant les techniques avancées de Sass"](https://openclassrooms.com/fr/courses/6106181-simplifiez-vous-le-css-avec-sass/6599201-utilisez-le-systeme-7-1-pour-une-codebase-plus-simple-a-gerer)