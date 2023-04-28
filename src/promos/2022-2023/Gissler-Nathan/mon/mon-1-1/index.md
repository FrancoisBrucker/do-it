---
layout: layout/mon.njk

title: "Web Front 1 HTML/CSS/JS"
authors:
    - Nathan Gissler

date: 2022-10-07

tags:
  - 'temps 1'
  - 'web'
  - 'front'
  - 'html'
  - 'css'
  - 'canvas'
---

<!-- début résumé -->

Avec ce MON, je vais apprendre à utiliser les outils de front qui me permettront de réaliser le POK "Mon site chez moi"

<!-- fin résumé -->

## 1. Prise en main de HTML et CSS

### 1.1 Cours Openclassrooms

J'étais au départ assez peu familier avec HTML, CSS, JavaScript et le front en général. J'ai choisi de suivre le [cours HTML et CSS d'Openclassrooms][cours openclassrooms] car il m'a paru assez complet.

Le cours est assez facile à suivre, chaque partie apparaît sous la forme d'une vidéo et de manière détaillée sous forme de texte, il y a des exercices réguliers si on veut s'entraîner et des ouvertures sont proposées à la fin pour aller plus loin ainsi qu'un récapitulatif des balises et fonctionnalités.

### 1.2 Site

En parallèle du cours, j'ai réalisé un [site][site sur github] en HTML et CSS qui m'a simplement servi à tester la plupart des fonctionnalités au fur et à mesure. Ce site de test me servira également à retrouver les différentes balises et autres propriétés lors de la réalisation du POK.

### 1.3 Principales fonctionnalités de HTML

#### Bases

Le langage HTML sert à définir le contenu d'une page web. Il fonctionne avec des balises qui peuvent être seules : `<img />`, ou par deux : `<title> </title>`.

Le code de base d'un fichier HTML est le suivant :

    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8" />
            <title>Titre de la page</title>
        </head>

        <body>
        
        </body>
    </html>

On place ensuite le contenu de la page entre les balises `<body> </body>`.

On peut insérer des commentaires sous la forme `<!-- commentaire -->`.

#### Quelques balises

Il existe de nombreuses balises, notamment :

- `<p> </p>` pour les paragraphes
- `<h1> </h1>` à `<h6> </h6>` pour les titres du plus au moins important
- `</ br>` pour les sauts de ligne
- `<em> </em>`, `<strong> </strong>` et `<mark> </mark>` pour faire ressortir certaines parties du texte
- `<ul> </ul>` pour une liste (`<ol> </ol>` pour une liste ordonnée) et `<li> </li>` pour chaque élément de liste
- `<a href="https://adressedulien.com>Nom affiché</a>` pour un lien, `title="titre"` permet d'afficher un texte lorsque l'on survole le lien et `target="_blank"` d'ouvrir le lien dans un nouvel onglet/fenêtre. Le lien peut aussi être une image par exemple
- il est aussi possible de créer un lien relatif vers une autre page du site ou un fichier à télécharger avec `href="chemin/autrepage.html"` / `href="chemin/fichier.zip"` ou vers une ancre dans la même page avec `href="#ancre` et avec `id=ancre` dans la balise correspondant à l'ancre
- `<img src="chemin/image.jpg" alt="texte alternatif" />` pour une image
- `<div> </div>` et `<span> </span>` sont des balises génériques (qui n'ont pas de sens particulier)
- `<audio src="chemin/fichier.mp3"> </audio>` pour des fichiers audios (fonctionne avec différents formats)
- `<video src="chemin/fichier.mp4"> </video>` pour des vidéos

#### Balises pour structurer la pages

Certaines balises peuvent servir à identifier les différentes sections de la page.

![Balises pour identifier les sections de la page](sections_page_web.png)

#### Tableaux

La structure des tableaux HTML est la suivante :

    <table>
        <tr>
            <td>
                ligne 1 colonne 1
                ligne 1 colonne 2
            </td>
        </tr>
        <tr>
            <td>
                ligne 2 colonne 1
                ligne 2 colonne 2
            </td>
        </tr>
    </table>

Il est possible de fusionner des cellules avec `colspan` et `rowsspan`.

#### Formulaires

Il est possible d'insérer des formulaires avec la balise `<form> </form>`, dans laquelle on peut placer la balise `<input type="text" />` par exemple, où l'attribut `type` peut prendre un certain nombre de valeurs pour demander à l'utilisateur une date, une couleur, un numéro de téléphone, etc.

La récupération des informations doit se faire en php.

### 1.4 Principales fonctionnalité de CSS

#### Bases

On écrit le code CSS dans un fichier .css qu'on relie au(x) fichier(s) HTML au(x)quel(s) il s'applique en insérant cette ligne dans la balise `<head> </head>` du fichier HTML :

    <link rel="stylesheet" href="style.css" />

Où `style.css` est le nom du fichier CSS.

On peut écrire des commentaires sous la forme `/* commentaire */`

#### Appliquer un style à des balises HTML spécifiques

Grâce aux sélecteurs, il est possible d'appliquer un style :

- à un type de balise :

        p
        {
            color: blue;
        }

- à la balise ayant l'attribut `id="unebalise"` :

        #unebalise
        {
            color: blue;
        }

- à toutes les balises ayant l'attribut `class="certainesbalises` :

        .certainesbalises
        {
            color: blue;
        }

- aux balises h1 et h2 :

        h1, h2
        {
            color: blue;
        }

- aux balises p contenues dans des balises h1 :

        h1 p
        {
            color: blue;
        }

- aux balises h2 qui suivent une balise h1 :

        h1 + h2
        {
            color: blue;
        }

- à toutes les balises :

        *
        {
            color: blue;
        }

- et beaucoup d'autres...

#### Propriétés CSS

Il existe de nombreuses propriétés pour le texte :

- `color` pour la couleur
- `font-size` pour la taille
- `font-family` pour la police
- `font-style` pour l'italique
- `font-weight` pour le gras
- `font-decoration` pour souligner
- `text-align` pour l'alignement (gauche / droite / centré / justifié)
- `float` peut s'appliquer aux images pour gérer leur position par rapport aux paragraphes de texte

Quelques propriétés pour le fond (de toute la page ou de n'importe quelle balise) :

- `background-color`
- `background-image`
- `background-repeat`
- `background-attachment`
- `background-position`
- `background` qui peut combiner ces propriétés

Quelques propriétés pour les éléments de type block (contrairement aux éléments de type inline) :

- `height` et `width` pour la hauteur et la largeur du block
- on peut également définir des `min-width`, `max-width`, etc.
- `padding` et `margin` pour les marges intérieures et extérieures du block
- `overflow` ou encore `word-wrap` pour gérer le débordement du texte

Autres propriétés :

- `border` permet de paramétrer les bordures d'un élément. Les bordures peuvent paramétrées ensemble ou séparément
- `box-shadow` pour mettre une ombre sur un bloc ou `text-shadow` sur un texte (l'ombre est alors sur le contour des lettres)

Il est possible de définir un style pour un élément seulement lorsqu'il est survolé (pour un lien par exemple) avec `:hover`

    a:hover
    {
        color: blue;
    }

Il existe également `:active` pour un élément cliqué (lors du clic), `:focus` pour un élément sélectionné, ou encore `:visited` pour un élément déjà visité.

Il est possible d'ajouter la propriété `display: flex` à un conteneur pour gérer la disposition de ses éléments assez simplement avec Flexbox (disposition verticale ou horizontale, ordre, espacement...).

#### Responsive

Les Medias Queries permettent de paramétrer les propriétés CSS à appliquer en fonction de différents paramètre de l'appareil sur lequel on affiche le site (type d'appareil, taille de la page, etc.).

## 2. Canvas HTML

### 2.1 Tutoriel

J'ai également regardé une partie de ce [ tutoriel][tutoriel canvas html] sur les Canvas HTML qui pourraient être utiles pour créer une partition intéractive pour le POK "Mon site chez moi".

Les canvas se placent dans des balises HTML et permettent de dessiner au sein de la page (placer des formes, du texte, des images, les faire se déplacer, intéragir avec...), ils peuvent être utilisés grâce à JavaScript.

### 2.2 Quelques fonctionnalités

#### Bases

Insertion du canvas dans le fichier HTML :

    <body>
        <canvas id="canvas"></canvas>
    </body>
    <script src="main.js"></script>

Paramétrage de la taille et du fond du canvas dans le fichier `main.js` :

    let canvas = document.getElementById("canvas");

    let context = canvas.getContext("2d");

    var window_height = window.innerHeight;
    var window_width = window.innerWidth;

    canvas.style.background = "#fff";

#### Création d'objets

On se place pour la suite dans `main.js`

Rectangle (la couleur est facultative) :

    context.fillStyle = "colorName";
    context.fillRect(xpos, ypos, width, height);

Cercle :

    context.beginPath();
    context.strokeStyle = "colorName";
    context.lineWidth = lineWidth;
    context.arc(x, y, radius, startAngle, endAngle, anticlockwise?);
    context.stroke();
    context.closePath();

Texte (la police est également facultative) :

    context.fillText(text, xpos, ypos);
    context.font = "20px Arial";

Image :

    let image = document.createElement("img");
    image.src = imagePath;
    image.onload = function() {
        context.drawImage(image, xpos, ypos, width, height);
    }

#### Création de classes

Classe permettant de créer des cercles :

    class Circle {
        constructor(xpos, ypos, radius, color) {
            this.xpos = xpos;
            this.ypos = ypos;
            this.radius = radius;
            this.color = color;
        }

        draw(context) {
            context.beginPath();
            context.strokeStyle = color;
            context.arc(xpos, ypos, radius, 0, Math.PI * 2, false);
            context.stroke();
            context.closePath();
        }
    }

Création d'un cercle grâce à cette classe :

    let circle = new Circle(100, 200, 50, "red");

    circle.draw(context);

#### Animation d'un objet

Une fonction de ce type permet d'avoir un objet en mouvement (la méthode update modifie légèrement la position du cercle) :

    let updateCircle = function() {
        requestAnimationFrame(updateCircle);
        circle.update();
    }

#### Intéractions avec le canvas (clic)

Pour exécuter une action en cas de clic sur le canvas :

    canvas.addEventListener('click', (event) => {
        const rect = canvas.getBoundingClientRect();
        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;
        // action à effectuer en utilisant la position x, y du clic
    })

## 3. Liens

- [Cours HTML / CSS d'Openclassrooms][cours openclassrooms]
- [Mon site de test sur GitHub][site sur github]
- [Tutoriel Canvas HTML sur Youtube][tutoriel canvas html]

[cours openclassrooms]: https://openclassrooms.com/fr/courses/1603881-apprenez-a-creer-votre-site-web-avec-html5-et-css3
[site sur github]: https://github.com/nathan-gissler/cours-html-css
[tutoriel canvas html]: https://www.youtube.com/watch?v=p88rNckccmg&list=PLN0tvDAN1yvSNbkHAwPzJ5O4pP_e2vyme