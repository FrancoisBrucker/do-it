---
layout: layout/mon.njk

title: "MON 4 : Sass"
authors:
 - Thomas Pont

date: 2023-01-25

tags:
  - 'temps 2'
  - 'sass'
  - 'front'

---

<!-- Début Résumé -->

Sass : amélioration et optimisation du CSS
<!-- Début Résumé -->

## Introduction

Ce MON est destiné à des personnes de niveau **intermédiaire** en connaissance de style pour réaliser un site Web. En effet, il est nécessaire d'avoir des **bases en CSS** et dans un langage de programmation.

{%prerequis%}
Les différents MONs suivants parlent des bases en CSS :

- [MON de Louise](https://francoisbrucker.github.io/do-it/mon/LG/MON2/)
- [MON de Nathan](https://francoisbrucker.github.io/do-it/mon/NG/mon-1-1/)

{%endprerequis%}

**Sass** (Syntactically awesome stylesheets) est un **langage de script préprocesseur** qui est **compilé ou interprété** en CSS.

Il offre de **nouvelles fonctionnalités** par rapport à du simple CSS à l'aide notamment de variables, de fonctions, de mixins, d'imbrications, ... Il **facilite** également le code et sa **maintenabilité**.

**Deux syntaxes** sont possibles en Sass, une indentée et une reprenant la même structure que CSS. Les extensions de fichier respectivement associées sont *.sass* et *.scss*.

Dans la suite de ce MON, je parlerai de la syntaxe en *.scss* soit un code reprenant la même structure qu'un fichier CSS standard.

## Comment faire du Sass ?

Afin d'utiliser Sass, il est nécessaire de l'installer. En effet, les navigateurs ne comprennent pas les fichiers Sass. Il faut donc un compilateur qui traduira le fichier en CSS ce qui le rendra compréhensible par les navigateurs.

Pour cela, il y a plusieurs méthodes possibles qui sont détaillées dans ce [tutorial](https://openclassrooms.com/fr/courses/6106181-simplifiez-vous-le-css-avec-sass/6599386-installez-sass-sur-votre-machine#:~:text=Installation%20de%20Sass%20avec%20VsCode&text=Cette%20extension%20s'appelle%20Live,onglet%20%E2%80%9Cextension%E2%80%9D%20de%20VsCode.&text=Puis%20recherchez%20l'extension%20Live%20Sass%20Compiler%20et%20installez%2Dl%C3%A0.&text=Vous%20pourrez%20maintenant%20lancer%20facilement%20la%20compilation%20de%20fichiers%20Sass.)

Afin d’apprendre les bases de Sass, j’ai suivi le cours suivant : [Apprendre à utiliser Sass](https://www.pierre-giraud.com/sass-apprendre-cours-complet/) et la deuxième partie du cours [Simplifiez-vous le CSS avec Sass](https://openclassrooms.com/fr/courses/6106181-simplifiez-vous-le-css-avec-sass).

## Les principales fonctionnalités

### Les variables

Un des premiers avantages de Sass est que ce langage permet de **déclarer des variables** qui permettent **maintenir et modifier un site**. Ces variables ne peuvent prendre qu'**une seule valeur** contrairement au CSS et sont **impératives** (si on utilise puis change la valeur d'une variable, les usages précédents ne seront pas impactés par cette modification). Les deux types de variables (Sass et CCS) n'ont pas le même objectif. Les variables CSS vont dans le DOM et peuvent être utilisées dans des fonctions JS par exemple.

Pour déclarer une variable, on utilise le **symbole $**.

Il est possible de déclarer des **variables globales**. Celles-ci doivent être déclarées en haut du document et font effet sur tout le document. Mais, on peut également créer des **variables locales**. Celles-ci sont déclarées dans les accolades d'un bloc et sont à application dans celui-ci.

On peut notamment utiliser les variables pour définir une charte de couleurs. Si celle-ci change, il sera facile de la modifier partout sur le site. Par exemple, le code qui suit définit une charte graphique globale à tout le site.

```css
$main-color: #0000FF;
$secondary-color: #FF0000;
```

Il est également possible de laisser le choix à l'utilisateur de personnaliser le site. Cela est faisable grâce à la balise **!default**. Si la valeur n'est pas définie c'est cette valeur pas défaut qui est utilisé, sinon c'est celle définie par l'utilisateur qui l'est.

Les variables peuvent être des couleurs, des chaînes de caractères, des nombres, des listes, des maps, des booléens, des nulls ou des fonctions.

Une liste permet de stocker plusieurs variables, comme par exemple plusieurs couleurs.

```css
$fonts-family: ['Roboto', 'Source Code Pro', 'Fira Code'];
```

Pour se servir de la 3ème police pour les titres, on peut procéder de cette manière :

```css
h1{
    font-family: nth($fonts-family, 3)
}
```

{% attention "**Attention** à la numérotation" %}
Contrairement à la plupart des langages informatiques, la numération des éléments d'une liste commence à 1 en Sass.

{% endattention %}

### Les mixins

Une **mixin** définit un **ensemble de règles** qui pourra être réutilisé pour **stylisé** un ensemble d'élément sur une page Web. Cela permet d'alléger le code en évitant les répétitions si ces paramètres sont utilisés à plusieurs endroits. Et, tout comme précédemment, cela facilite la maintenabilité du site. Pour déclarer une mixin, on utilise **@mixin**.

On peut également avoir des mixins qui prennent des **paramètres**.

On peut définir une mixin pour les titres de notre page. On la définit en haut de notre fichier Sass grâce au code suivant :

```css
@mixin title-shadow($color){
    font-family: $fontGeorgia, serif;
    text-shadow: .15rem .15rem $color;
}
```

Pour l'utiliser, on l'intègre de cette manière dans le code :

```css
h1{
    text-decoration-line:underline;
    text-decoration-style: solid;
    text-decoration-color: $secondary-color;
    @include title-shadow(#a5a3a3);
}
```

### Les fonctions

Sass a également des **fonctions préprogrammées** qui permettent de simplifier la gestion du style de notre page. Par exemple, il existe des [fonctions](https://sass-lang.com/documentation/modules/color) pour les couleurs. Des fonctions permettant de **désaturer**, d'**assombrir**, d'**éclaircir** ou encore de **griser** une couleur sont ainsi disponible. Cela peut s'avérer très pratique pour garder une cohérence dans un visuel et faciliter la maintenabilité en cas de changement de couleur.

Pour exemple, si l'on souhaite faire un cadre de couleur légèrement plus foncé que la couleur du texte qu'il contient, on peut procéder de cette manière :

```css
#p_encadre{
    color:$main-color;
    border:1px solid darken($main-color, 20%);
}
```

Il est également possible de **créer ses propres fonctions** en utilisant **@function**. On peut alors utiliser des **conditions** tel que *if ... then ... else ...*, des variables,... Cela permet plus de liberté et un code simple. Ainsi, pour que la différence de couleur entre le cadre et le texte soit bien marquée, on peut faire en sorte d'assombrir le trait du cadre quand la couleur du texte est clair et inversement quand elle est foncée. Pour cela, on crée une mixin qu'on utilise ensuite.

```css
@function encadre($color){
    @if ( lightness($color) < 25% ) {
        @return lighten($color, 20%);
    }@else{
        @return darken($color, 20%);
    }
}

@mixin p_encadre($color: encadre($main-color)){
    border: 1px solid encadre($color);
}

#p_encadre{
    color:$main-color;
    @include p_encadre()
}
```

Il est également possible d'utiliser d'autres boucles comme *for* grâce au bloc **@for**. Cela permet par exemple de faire varier une valeur comme par exemple la taille d'un composant.

```css
@for $i from 1 through 6 {
    .grid-#{$i} {
        width: 100px*$i;
    }
}
```

D'autres boucles sont disponibles :

- **@while** : pour faire varier une valeur tant qu'une condition est vérifiée;
- **@each** : pour par exemple prendre les éléments d'une liste.

## Tutoriel

Dans la suite de ce MON, j'ai principalement regardé des vidéos sur YouTube de manière à trouver des conseils sur la Sass et des idées principalement sur cette [playlist](https://www.youtube.com/playlist?list=PL4-IK0AVhVjMYRhK9vRPatSlb-9r0aKgh).

## Autres ressources utilisées

- [Informations sur Sass](https://fr.wikipedia.org/wiki/Sass_(langage))
- [Documentation Sass](https://sass-lang.com/documentation/)
