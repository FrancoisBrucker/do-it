---
layout: layout/mon.njk

title: "Web Front 1 (HTML, CSS, Bootstrap)"

authors:
  - Jeffrey Edisah

date: 2022-10-07

tags:
  - 'temps 1'
  - 'info'
  - 'web'
  - 'front'
  - 'html'
  - 'css'

---
<!-- début résumé -->

Voir ou revoir les technologies pour la conception du front d'un site (HTML, CSS, Frameworks CSS, JavaScript)

<!-- fin résumé -->

Au cours de ce MON, j'ai revu HTML 5, CSS 3 et Bootstrap afin de pouvoir travailler sur mon POK.
J'ai utilisé Mozilla Developer Network  pour revoir l'HTML, le CSS et les utiliser dans mon POK ( le lien est [ici](https://github.com/JeffreyEdisah/Jekwed-Portfolio))

Mes souvenirs en HTML étant plutôt frais, ce MON se concentrera plus sur le CSS et les Frameworks associés

## HTML

L'**HTML**(HyperText Markup Language) est le langage permettant l'écriture des pages web en complément du **CSS** (Cascading Style Sheets). Tandis que l'HTML sert à créer le contenu à proprement parler, c'est à dire le texte, les liens, les images, les vidéos, les tableaux, et les formulaires; le CSS sert lui à styliser les différents éléments HTML, organiser la page et son contenu, rendre le tout attrayant visuellement.

L'HTML se construit à l'aide de balises ouvrantes et fermantes, de la forme `<element> contenu </element>`, ces balises pouvant s'imbriquer les unes dans les autres. Une liste plus détaillée des éléments et de comment les utiliser est présente sur ce [tutoriel de Mozilla Developer Network](https://developer.mozilla.org/fr/docs/Learn/HTML)

### Structure générale du fichier

Chaque fichier HTML se structure avec tout d'abord un élément principal `<html></html>`, qui est nécessaire. 

Il est possible ensuite d'écrire un en-tête `<head></head>` qui contient des métadonnées sur la page telle que son titre, son type de caractères, sa langue, ou bien les liens vers les fichiers CSS et JavaScript, ou même les codes CSS et JavaScript directement dans les éléments `<style></style>`et `<script></script>`respectivement. Le contenu de cette élément n'est pas visible sur la page.

Ce qui est visible dans la page est écrit dans l'élément **body**, c'est ici que sera écrit ce qui est visible sur la page, et tout cela sera détaillé juste en dessous.

### Structure de la page

Les pages Web se construisent généralement comme ceci, un **header**, un **main** et un **footer**. Aucun de ces éléments n'est obligatoire bien entendu mais ils permettent de mieux structurer la page, le header contenant généralement une **navbar** (barre de navigation ou menu) tandis que le footer porte des informations de contact. Le main lui correspond au reste de la page

### Contenu

Le gros du contenu produit en HTML est surtout textuel, que ce soit les titres par exemple de la forme`<h1> </h1>`, les paragraphes `<p></p>`.
Il existe aussi un élément `<img>`, avec une balise qui est seulement ouvrante pour tout ce qui est images, le contenant `<iframe>` pour les contenus multimédia, et des éléments audio et vidéo que je n'ai pas encore été amené à utiliser.

Au delà de ça il existe des éléments appelés universels `<div>`et `<span>` qui servent ensuite dans la stylisation de la pag en CSS à l'aide des attribut classes.

## CSS

De la même manière que pour l'HTML, ma ressource principale pour le CSS était [Mozilla](https://developer.mozilla.org/fr/docs/Learn/CSS) qui nous permet une introduction au langage et référence les éléments CSS et leurs valeurs possibles

### Sélecteurs

Le CSS fonctionne à l'aide de sélecteurs, c'est à dire des moyens de sélectionner les éléments auxquelles on ajoute le style. On peut les sélectionner par ordre de spécificité soit par leur élément, soit par leur classe, soit par leur id. La spécificité, concept important en CSS, est décrite de manière plus exhaustive [ici](https://developer.mozilla.org/fr/docs/Learn/CSS/Building_blocks/Cascade_and_inheritance)

### Stylisation des éléments HTML

Le CSS permet de changer différentes propriétés des éléments, que ce soit leur taille, leur position, leur couleur, la couleur de l'arrière plan, etc...

### Mise en page

La mise en page apparait comme la grande force de CSS, et aussi la partie la plus compliquée de la chose. Il y a plusieurs layout disponibles : la grille, les multicolonnes, et plus récemment la flexbox. La flexbox a l'avantage d'être plus responsive nativement que les autres layouts, ce qui permet d'éviter la multiplication des medias queries. Le lien suivant d'[OpenClassrooms](https://openclassrooms.com/fr/courses/1603881-apprenez-a-creer-votre-site-web-avec-html5-et-css3/3298561-faites-votre-mise-en-page-avec-flexbox) m'a permis de comprendre beaucoup mieux la puissance du layout flex, notamment avec la fonction wrap.  Ce [lien](https://css-tricks.com/snippets/css/a-guide-to-flexbox/#aa-background) m' a aussi permis de voir beaucoup plus de choses sur flex.

## Bootstrap

J'ai manqué de temps pour voir Bootstrap de manière exhaustive et organiser mes pensées mais je suis toujours en train de regarder ces liens actuellement, la [documentation Bootstrap](https://getbootstrap.com/docs/5.2/getting-started/introduction/) ainsi que le [cours OpenClassrooms](https://openclassrooms.com/fr/courses/7542506-creez-des-sites-web-responsives-avec-bootstrap-5). je prendrais sûrement un peu de temps pour mieux organiser cette partie plus tard.

Bootstrap est un framework qui facilite la mise en place de pages aux layouts agréables et responsives. Bootstrap construit ses propres classes à rajouter aux différents éléments HTML afin de leur appliquer les propriétés Bootstrap.

Un exemple de structure d'un élément bootstrap se construit comme ceci :

  <div class='container'>
    <div class='row'>
      <div class='col-xs-12 col-md-4'>
        ...
      </div>
    </div>
  </div>

Concrètement, la page Bootstrap se construit sur un concept de grille, à 12 colonnes. On accède à la grille tout d'abord à l'aide d'une classe container. Cette classe met en place la grille, à laquelle les autres éléments peuvent accéder, tout d'abord par les rows, c'est-à-dire les lignes de la grille, et les colonnes, avec différents agencements pour différentes tailles d'écran ou **breakpoints**. Il est également assez simple de rajouter des marges, avec des tailles prédéfinies.

AU delà de la mise en page, Bootstrap facilite grandement le design des pages avec des composants déjà faits et facile à implémenter (encore une fois à l'aide de classes) telle que la navbar, les carousels, les boutons, etc...

Un des problèmes que j'ai cependant rencontré avec l'utilisation de Bootstrap est la difficulté de personnalisation des différents composants, avec des ambiguïtés parfois au niveau des classes choisis, ou même au niveau de la spécificité, ce qui rend la personnalisation tatillonne. Apparemment, la personnalisation est plus simple avec des fichiers SCSS mais je ne suis pas encore au point sur les préprocesseurs CSS (peut-être un futur MON).