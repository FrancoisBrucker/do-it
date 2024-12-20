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
Pour réaliser ce MON et débuter mon apprentissage, j'ai décidé de suivre les cours du site de Mr Brucker, ainsi que de suivre un tutoriel disponible en ligne et recommandé par le site do-it. Il s'agit du tutoriel W3School. Ce tutoriel permet d'apprendre les notions de bases de HTML/CSS et est accompagné d'exercices de codes sur un éditeur en ligne."
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

## Table des matières<a name="table-des-matières"></a>

- [Table des matières](#table-des-matières)
- [Contenu](#contenu)
- [1.HTML](#1html)
    - [Généralités](#généralités)
    - [Les éléments HTML](#les-éléments-html)
- [2.CSS](#2css)
- [3.Bilan](#3bilan)
- [Horodateur](#horodateur)

## Contenu

## 1.HTML<a name="1htmlL"></a>

#### <span style="color: #26B260">Généralités<a name="généralités"></a>
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

#### <span style="color: #26B260">Les éléments HTML<a name="les-éléments-html"></a>

Le langage HTML tout entier repose sur l’utilisation d’**éléments**. Dans une page, nous allons utiliser les éléments en HTML pour marquer du contenu, c’est-à-dire pour lui donner du sens aux yeux des navigateurs et des moteurs de recherche.

**<span style="color: purple">1. Les balises HTML**<a name="balises"></a>
   
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

**<span style="color: purple">2. Les attributs HTML**<a name="attributs"></a>

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
| class | used to point to a class name in a style sheet, used by a JavaScript to access and manipulate elements with the specific class name |
| div |	Container for other HTML elements|
| id | Specifies a unique id for an HTML element|

**Focus sur certains attributs importants**
* L'attribut **class** est souvent utilisé pour pointer vers un nom de classe dans une feuille définissant le style. Il peut également être utilisé par un JavaScript pour accéder et manipuler des éléments portant le nom de classe spécifique. Pour définir plusieurs classes, séparez les noms de classe par un espace. L'élément sera stylisé selon toutes les classes spécifiées.
* L'attribut **id** spécifie un identifiant unique pour un élément HTML. La valeur de l'attribut id doit être unique dans le document HTML. Il est utilisé pour spécifier une caractéristique de style spécifique dans le code. Il est également utilisé par JavaScript.

Pourquoi les attributs **div** et **id** sont-ils différents ? 
L'attribut **class** peut être utilisé par plusieurs éléments HTML, tandis que **div** ne doit être utilisé que par un seul élément HTML dans la page :

```
<!-- An element with a unique id -->
<h1 id="myHeader">My Cities</h1>

<!-- Multiple elements with same class -->
<h2 class="city">London</h2>
<p>London is the capital of England.</p>

<h2 class="city">Paris</h2>
<p>Paris is the capital of France.</p>

<h2 class="city">Tokyo</h2>
<p>Tokyo is the capital of Japan.</p>
```

**<span style="color: purple">3. Focus sur l'indentation et les commentaires**<a name="ind_comm"></a>

Indenter va nous permettre d’avoir un code plus propre et plus lisible, donc plus compréhensible. Indenter permet également de plus facilement **détecter les erreurs** potentielles dans un code.
Note : Les retours à la ligne et l’indentation créés dans l’éditeur n’affectent pas le résultat final dans le navigateur.

Les commentaires ne seront pas affichés par le navigateur lorsque celui-ci va afficher la page : ils ne vont servir qu’aux développeurs créant ou lisant le code. Les commentaires en HTML vont prendre la forme d’une **balise orpheline** très particulière : 
```
<!--Commentaire-->
```

**<span style="color: purple">4. Les listes**<a name="listes"></a>

Il est possible en HTML de définir différents types de listes :
* des **listes non ordonnées** (élément ul, l'élément li permet de définir chaque item) ;
* des **listes ordonnées** (élément ol, l'élément li permet de définir chaque item) ;
* des **listes de définition** (dl, lh, dt et dd).

**<span style="color: purple">5. Les entités**<a name="entités"></a>

Une **entité HTML** est une suite de caractère qui est utilisée pour afficher un caractère réservé ou un caractère invisible.
* "&nbsp" : ajouter une espace simple dit espace « insécable » ;
* "&ensp" : créer une espace double ;
* "&emsp" : créer une espace quadruple ;
* "&thinsp" : créer un espace très fin (demi-espace).

**<span style="color: purple">6. Les tables**<a name="tables"></a>

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

**<span style="color: purple">7. Block/Inline Elemnent**<a name="B/I_element"></a>

* Un **élément de niveau bloc** commence toujours sur une nouvelle ligne et occupe toute la largeur disponible;
* Un élément en ligne ne démarre pas sur une nouvelle ligne et prend uniquement la largeur nécessaire; 
* L'**élément div** est au niveau bloc et est souvent utilisé comme conteneur pour d'autres éléments HTML.
* L'**élément span** est un conteneur en ligne utilisé pour baliser une partie d'un texte ou une partie d'un document.


## 2.CSS<a name="2css"></a>

**<span style="color: purple">1. Généralités**<a name="CSS-Généralités"></a>

* Le code CSS est contenu dans une feuille de style construite en cascade.
* Il décrit comment les éléments HTML doivent être affichés à l'écran, en définissant le style de chaque éléments.
* Il peut contrôler la mise en page de plusieurs pages Web à la fois.
* Les feuilles de style externes sont stockées dans des fichiers CSS.

Il permet de résoudre un gros problème, puisque le language HTML n'a jamais été conçu pour formater une page Web. Il permet un gain de temps significatif car on peut modifier l’apparence d’un site Web entier en modifiant un seul fichier au format CSS externe.

Il existe trois manières d'insérer une feuille de style, en interne, en externe ou en ligne. On se concentre ici sur les fichiers externes, ce que nous souhaitons utiliser pour la création de notre site de Dark Kitchen.

**La syntaxe CSS :**

![Syntaxe_CSS](./syntaxe_CSS.webp)

Le sélecteur pointe vers l’élément HTML que vous souhaitez styliser. Chaque déclaration comprend un nom de propriété CSS et une valeur.

**<span style="color: purple">2. Les sélecteurs**<a name="sélecteurs"></a>

Les sélecteurs CSS sont utilisés pour « trouver » (ou sélectionner) les éléments HTML que vous souhaitez styliser. Il en existe 5 catégories : 
* Sélecteurs simples (sélectionnez des éléments en fonction du nom, de l'identifiant, de la classe)
* Sélecteurs combinatoires (sélectionnez des éléments en fonction d'une relation spécifique entre eux)
* Sélecteurs de pseudo-classes (sélectionnez des éléments en fonction d'un certain état)
* Sélecteurs de pseudo-éléments (sélectionnez et stylisez une partie d'un élément)
* Sélecteurs d'attributs (sélectionnez des éléments en fonction d'un attribut ou d'une valeur d'attribut)*

**<span style="color: purple">3. En pratique**<a name="pratique"></a>

Tous les styles d'une page seront « mis en cascade » dans une nouvelle feuille de style « virtuelle » selon les règles suivantes, où le numéro un a la priorité la plus élevée :

1. Style en ligne (à l'intérieur d'un élément HTML)
2. Feuilles de style externes et internes (dans la section head)
3. Navigateur par défaut
   
Ainsi, un style en ligne a la priorité la plus élevée et remplacera les styles externes et internes ainsi que les valeurs par défaut du navigateur. 

Exemple : 
```
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" type="text/css" href="mystyle.css">
<style>
body {background-color: linen;}
</style>
</head>
<body style="background-color: lavender">

<h1>Hello</h1>
<p>Here, the background color of the page is set with inline CSS, and also with an internal CSS, and also with an external CSS.</p>

</body>
</html>
```

On se limitera ici à une brève présentation du language CSS, puisque nous allons rapidement le pratiquer à l'aide de notre POK1, puisque nous allons écrire un fichier externe qui définira le style de notre site web.


Voici un exemple d'un code que nous avons écris pour définir le design de la page menu de notre site web : 
```
body {
    font-family: 'Raleway', sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f7f7f7;
    color: #333;
}

header {
    background-color: #333;
    padding: 20px;
    text-align: center;
}

nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: white;
    text-decoration: none;
    font-weight: 600;
}

.menu-section {
    padding: 50px 0;
}

.menu-section h1 {
    text-align: center;
    font-size: 2.5rem;
    margin-bottom: 50px;
}

.menu-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 30px;
    max-width: 1200px;
    margin: 0 auto;
}

.menu-item {
    background-color: white;
    border-radius: 10px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.menu-item:hover {
    transform: translateY(-10px);
    box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
}

.menu-item img {
    max-width: 100%;
    border-radius: 10px;
    margin-bottom: 20px;
}

.menu-item h3 {
    font-size: 1.5rem;
    margin-bottom: 10px;
}

.menu-item p {
    font-size: 1.1rem;
    margin-bottom: 20px;
}

.btn-primary {
    background-color: #ff6347;
    color: white;
    padding: 10px 20px;
    text-decoration: none;
    border-radius: 5px;
    font-weight: bold;
    transition: background-color 0.3s ease;
}

.btn-primary:hover {
    background-color: #e55340;
}
```

Et voici ensuite la code HTML permettant de faire appel à notre fichier CSS externe : 
```
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dark Kitchen - Menus</title>
    <link rel="stylesheet" href="../css/menu.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;600&display=swap" rel="stylesheet">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="../index.html">Accueil</a></li>
                <li><a href="menu.html">Menus</a></li>
                <li><a href="panier.html">Panier</a></li>
            </ul>
        </nav>
    </header>

    <section class="menu-section">
        <div class="container">
            <h1>Nos Menus</h1>
            <div class="menu-grid">
                <div class="menu-item">
                    <img src="../images/nazi_goreng.webp" alt="Menu 1">
                    <h3>Menu Savoureux</h3>
                    <h4>Nazi Goreng</h4>
                    <p>Un délicieux menu composé d'ingrédients ultra proteine.</p>
                    <a href="panier.html" class="btn-primary">Ajouter au panier</a>
                </div>
                <div class="menu-item">
                    <img src="../images/mie_goreng.webp" alt="Menu 2">
                    <h3>Menu Gourmand</h3>
                    <h4>Mie Goreng</h4>
                    <p>Un menu généreux pour les afters salle.</p>
                    <a href="panier.html" class="btn-primary">Ajouter au panier</a>
                </div>
    
            </div>
        </div>
    </section>
</body>
</html>
```

L'exécution de ce code sur le serveur web nous permet d'afficher ce rendu visuel : 
![Page-Menu-Dark-Kitchen](./page-menu.webp)

## 3.Bilan<a name="3bilan"></a>
Lors de ce MON, j'ai réalisé 2 tutoriels complets sur W3School qui m'ont permis de découvrir et d'apprendre la mécanique du FrontEnd avec l'utilisation des languages HTML et CSS. L'objectif de ce MON était de bien assimilé ces 2 languages afin de les utiliserr pour le codage de mon propre site web qui fait l'objet de mon POK1. Je suis donc satisfait du travail réalisé puisque le rendu des premières pages de mon site est satisfaisant. Reste maintenant à acquérir des connaissance complémentaires en JavaScript et sur l'utilisation du framework Vue pour ajouter de l'interactivité aux pages de mon site internet. 

## Horodateur

Toutes les séances et le nombre d'heures que l'on y a passé.

| Date | Heures passées | Indications |
| -------- | -------- |-------- |
| 06/09  | 1H  | Lecture du cours do-it dev Web et recherche d'un tutoriel |
| 10/09  | 1H  | HTML : Structure de base en HTML, balises et attributs|
| 13/09  | 1.5H  | HTML : En-tête, paragraphes, commentaires, styles et couleurs |
| 14/09  | 1.5H  | HTML : Listes et tables |
| 13/09  | 1H  | HTML : Les attributs class, div et id |
| 20/09  | 2H  | CSS : Tutoriel W3schools, introduction au language |
| 22/09  | 2H  | CSS : Codage des pages 'Menu' et 'Panier' Dark Kitchen |

