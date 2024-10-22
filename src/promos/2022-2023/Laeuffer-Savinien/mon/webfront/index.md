---
layout: layout/mon.njk

title: "Web Front 1"
authors:
  - Savinien Laeuffer
date: 2022-10-07

tags:
  - 'temps 1'
---

<!-- début résumé -->
HTML, CSS et BOOTSTRAP
<!-- fin résumé -->

## Description

Dans ce MON, nous reverrons tout d'abord les bases d'HTML et CSS, puis nous introduiront Bootstrap qui est un framework.

Je me suis servi du site W3school que j'apprécie beaucoup pour la première partie sur HTML et CSS, mais aussi Bootstrap. Ensuite je me suis renseigné sur le site Openclassroom afin d'approfondir Bootstrap car je ne l'ai jamais réellement utilisé. Cela apporte un gain de temps considérable mais comme j'aime créer de A à Z, je m'étais d'abord plutôt penché sur le CSS pour pouvoir faire ce que je voulais.


## Rappels d'HTML

Cette partie consiste particulièrement à revoir HTML et CSS. Si on débute vraiment le HTML, je conseillerais plutôt de commencer par un autre site tel que OpenClassroom.

Personnellement, je trouve W3School vraiment très utile et assez fourni pour la programmation HTML et CSS. Il répertorie les différentes composants, balises, et objets que l'ont peut créer avec du CSS. c'est particulièrement utile lorsque qu'on a déjà des bases et que l'on cherche des composants précis à ajouter (un bouton, faire des transitions/animations, ...).

#####  1. Création du projet (HTML)

Pour commencer un projet HTML/CSS, il faut tout d'abord créer un fichier ```index.html``` que l'on ouvrira et modifiera avec un éditeur de texte. Pour ma part Visual Studio Code fera l'affaire.


Le fichier doit contenir ce code pour démarrer une page web:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Savinien LAEUFFER</title>
  </head>
  <body>
    Hello world
  </body>
</html> 
```


Maintenant réfléchissons à ce que l'on veut sur notre page. Pour ma part je souhaiterais faire un site portfolio qui regroupera mes compétences, mon contact, mes projets, un peu comme un CV en ligne de développeur web. Voici un schéma de ce que je veux faire:

<figure>
  <img src="../schema.png">
  <figcaption>Schema du site</figcaption>
</figure>

Pour la barre de navigation, c'est simple:
On ajoute la balise ```<nav>``` avec nos différents textes dans des balises ```<div>``` séparées, tout cela dans le ```<body>``` de la page HTML à la place du texte Hello world. On associe nos ```<div>``` à des classes qui serviront pour implémenter le CSS plus tard. Une classe navtitle pour le titre de la page, et une classe navelt pour les futurs textes cliquables. (les liens sont à l'envers mais cela aura son importance dans le CSS plus tard...)
Chez moi ça donne cela:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Savinien LAEUFFER</title>
  </head>
  <body>
    <!-- NAVBAR -->
    <nav id="header">
        <div class="navtitle">SAVINIEN LAEUFFER</div>
        <div class="navelt">CONTACT</div>
        <div class="navelt">PROJETS</div>
        <div class="navelt">PARCOURS</div>
        <div class="navelt">BIENVENUE</div>
    </nav>
  </body>
</html> 
```


On passe désormais à la page principale qui compote un fond d'écran et du texte par dessus. On utilise toujours les balises ```<div>``` qui s'imbriquent dans le code: d'abord le background, puis les textes. Le mot "Bienvenue" est dans un div distinct, car on voudra lui appliquer une autre couleur que l'autre phrase. La classes "background" servira à construire l'image de fond et la positionner. La classe "bigtext" nous servira à formater le texte.
On se retrouve avec ce code html:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Savinien LAEUFFER</title>
  </head>
  <body>
    <!-- NAVBAR -->
    <nav id="header">
        <div class="navtitle">SAVINIEN LAEUFFER</div>
        <div class="navelt">CONTACT</div>
        <div class="navelt">PROJETS</div>
        <div class="navelt">PARCOURS</div>
        <div class="navelt">BIENVENUE</div>
    </nav>
    <!-- PAGE PRINCIPALE -->
    <div class="background">
      <div class ="bigtext">
          <div>
              BIENVENUE
          </div>
          JE SUIS SAVINIEN LAEUFFER
      </div>
    </div>
  </body>
</html> 
```

Pour ma dernière partie de la page, il nous fond un fond d'écran blanc, on y affichera un texte de présentation (que je n'ai pas encore) et pourquoi pas une photo.
On obtient cela:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Savinien LAEUFFER</title>
  </head>
  <body>
    <!-- NAVBAR -->
    <nav id="header">
        <div class="navtitle">SAVINIEN LAEUFFER</div>
        <div class="navelt">CONTACT</div>
        <div class="navelt">PROJETS</div>
        <div class="navelt">PARCOURS</div>
        <div class="navelt">BIENVENUE</div>
    </nav>
    <!-- PAGE PRINCIPALE -->
    <div class="background">
      <div class ="bigtext">
          <div>
              BIENVENUE
          </div>
          JE SUIS SAVINIEN LAEUFFER
      </div>
    </div>
    <!-- PRESENTATION -->
    <div class="whitebackground">
      <div class="normaltext">     
        Hello ! Je m’appelle SAVINIEN, ceci est mon prenom, on me l'a donné quand je suis né et maintenant je dois faire avec. 
      </div>
    </div>
  </body>
</html> 
```

En lançant notre fichier html dans un navigateur internet, cela s'affiche:

<figure>
  <img src="../justehtml.png">
  <figcaption>index.html</figcaption>
</figure>


##### 2. Ajout de CSS

Notre site n'est pas très beau pour le moment, on a écrit le contenu textuel mais nous n'avons pas de mise en forme, pas d'image, il faut donc s'en occuper. Pour cela on va créer une feuille de style ```styles.css``` que l'on va placer au même endroit que le fichier ```index.html```.

Pour faire le lien entre le fichier html et le fichier css, on ajoute la balise suivante dans le ```<head>``` de notre fichier html:
```html
<link rel="stylesheet" href="styles.css">
```


a. La barre de navigation.

Tout d'abord on va formater l'apparence de la navbar, puis l'apparence des textes. Dans notre fichier css on va overrider la balise nav afin de lui donner certaines propriétés:
Marges: 0, Couleur: bleu foncé et assez transparent, position fixe à l'écran, largeur maximale. Le site W3School répertorie bien tout cela et c'est dans ces moments qu'il est très utile.

On ajoute donc au fichier CSS le code suivant:

```css
nav {
    margin: 0;
    overflow: hidden;
    padding: 0;
    background-color: rgba(14, 108, 170, 0.7);
    position: fixed;
    width: 100%;
}
```

Pour le texte, on formate la police d'écriture, la position des élements avec ```float```, la couleur du texte, et le padding. Si on a inversé les éléments précédemment c'est parce que ```float; right``` va placer les élément le plus à droite à la suite, il faut donc être vigilant.

On ajoute les lignes suivantes au CSS:

```css
.navtitle {
    float: left;
    font-size: large;
    font-family:   'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    color: white;
    text-align: center;
    padding: 25px 22px;
    display: block;
}

.navelt {
    float: right;
    font-size: large;
    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    color: white;
    text-align: center;
    padding: 25px 22px;
    display: block;
}
```

Petit plus (pour le fun et l'esthétique), on cherche à changer la couleur d'un des 4 liens dès qu'on l'on passe le curseur dessus, et on veut que cette couleur se change progressivement (1 demi seconde). C'est possible de faire cela avec uniquement du CSS avec ```:hover```. Ne pas oublier d'ajouter ```transition: 0.3s``` dans notre classe navelt.

```css
.navelt {
    float: right;
    font-size: large;
    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    color: white;
    text-align: center;
    padding: 25px 22px;
    display: block;
    transition: 0.3s;
}

.navelt:hover {
    background-color: black;
}
```


b. Notre page principale

Maintenant que la barre de navigation est en place, nous pouvons attaquer le corps principal de la page, ce que l'on va voir en attérissant sur le site. D'abord on applique la première image en background. On colle notre image dans le dossier avec les fichier HTML et CSS puis on ajoute le CSS suivant afin d'avoir une image fixe, qui prend tout l'espace en largeur, et qui s'adapte à la longueur de la page:

```css
.background {
    background-size: 100%;
    width: 100%;
    background-image: url(homescreen.jpg);
    min-height: 93vh;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
```
La valeur en "vh" est un pourcentage selon la taille du navigateur de l'utilisateur, cela peut être utile et appronfondi lorsque l'on tente de créer un site responsive qui s'adapte à la taille du navigateur et aux mobiles.

Pour le texte, comme précédemment, on ajoute le CSS suivant:

```css
.bigtext {
    font-size: 48px;
    font-family: Roboto;
    font-weight: bold;
    color: white;
    text-align: center;
    padding: 30vh;
}
```

c. La présentation

Pour le background blanc, on ajoute le CSS suivant: 

```css
.whitebackground {
    background-size: 100%;
    width: 100%;
    background-color: white;
}
```

Pour le texte, on recrée une classe qui reprendra les mêmes éléments que .bigtext mais avec des valeurs différentes:

```css
.normaltext{
    font-size: 24px;
    font-family: Roboto;
    font-weight: bold;
    color: black;
    text-align: center;
    padding: 20vh;
}
```

Comme dit précédemment dans la partie HTML, on souhaiterait que le "BIENVENUE" ne soit pas de la même couleur que le reste du texte. Pour cela on ne va pas recréer toute une classe. On peut aller changer directement notre style dans la balise ```<div>``` comme ceci:

```html
<div style="color: rgb(65, 163, 209)">
  BIENVENUE
</div>
```

d. Une autre image fixe (pour accentuer le "balayage" réalisé par le bloc de présentation)

J'ai passé pas mal de temps à réfléchir à comment faire cet effet de balayage de l'écran par le bloc blanc qui permet de changer le background. Je pensais d'abord qu'il fallait utiliser du JavaScript mais j'ai réussi à me débrouiller avec uniquement du CSS.

Pour cela, il a fallu fixer ma toute première image avec ```background-repeat: no-repeat;``` et ```background-attachment: fixed;```, puis faire en sorte que la page soit scrollable en rajoutant du contenu, c'est à dire le bloc de présentation sur fond blanc ainsi qu'une autre image en dessous qui est aussi fixée par les même paramètres:

```html
<div class="autrebackground">
</div>
```

```css
.autrebackground {
    background-size: 100%;
    width: 100%;
    background-image: url(background.png);
    min-height: 93vh;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
```

On obtient cet effet assez esthétique:


##  Installation de Bootstrap

Bootstrap est un framework gratuit et open source de développement front-end pour la création de sites web et d'applications web orienté mobile. Il fournit des outils aidant au developpement responsive grâce à un système de grilles qui détecte l'orientation et la taille de l'écran de l'utilisateur et adapte automatiquement l'affichage de la page web. Cela est particulièrement utile lorsque l'on veut créer un site web qui doit s'adapter au web mais aussi aux smartphones et aux tablettes.
Bootstrap fournit de plus de nombreux templates pour différents éléments de design.


Pour installer Bootstrap 4.6, il faut d'abord commencer par ajouter la feuille de style ```<link>``` suivante dans la partie ```<head>``` avant toutes les autres feuilles de style:

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
```


De nombreux composants Bootstrap (Alertes, boutons, barre de navigation déroulante) requièrent l'utilisation de JavaScript, plus particulièrement jQuery et Popper. Pour les installer il suffit d'ajouter les lignes ```<script>``` suivantes vers la fin de la page:

```html
<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>
```


Maintenant que Bootstrap est installé, votre code devrait ressembler à ceci si vous êtes parti d'un site Hello World:

```html
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <h1>Hello, world!</h1>

    <!-- jQuery et Bootstrap Bundle (Popper inclus) -->
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>

  </body>
</html>
```


##  Utilisation de Bootstrap


##### 1. Navbar


On veut tout d'abord essayer de remplacer la navbar précédente avec Bootstrap. Une navbar est déjà fournit dans leur documentation. Elle est modulable, on peut en changer les couleurs, polices et autres paramètres en ajoutant dans les balises "style=" suivi du CSS que l'on ajouter.

Pour une navbar classique on colle le code ci-dessous:

```html
<nav class="navbar navbar-expand-lg bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Savinien Laeuffer</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link" href="#">Bienvenue</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Parcours</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Projets</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Contact</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
```

et en ajoutant un peu de CSS pour les couleurs:

```html
    <nav class="navbar navbar-expand-lg bg-light">
      <div
        class="container-fluid"
        style="background-color: rgba(14, 108, 170, 0.7)"
      >
        <a class="navbar-brand" style="color: white" href="#">Savinien Laeuffer</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" 
        aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavDropdown">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link" style="color:white"href="#">Bienvenue</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" style="color: white" href="#">Parcours</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" style="color: white" href="#">Projets</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" style="color: white" href="#">Contact</a>
          </li>
          </ul>
        </div>
      </div>
    </nav>
```

L'avantage de cette navbar c'est qu'elle est prête à l'usage et ressemble à ceci:

<figure> 
  <img src="../navbar1.png">
  <figcaption>Navbar Bootstrap</figcaption>
</figure>

Mais elle est aussi adaptative à la taille de l'écran, et lorsque que la largeur diminue, par exemple sur mobile, les liens se déplacent dans un menu déroulant:

<figure> 
  <img src="../navbar2.png">
  <figcaption>Navbar Bootstrap</figcaption>
</figure>


##### 3. Composants

Grids, images reponsive, caroussels, buttons, alerts, forms (checkboxes, radio buttons,), toasts

##### 3. Imbriquer des composants

L'utilité de Bootstrap est d'avoir des composants tout fait qui peuvent s'imbriquer pour créer ce que l'on veut avec l'utilisation que l'on souhaite. Par exemple faisons un toast qui permet de contacter le propriétaire du site.

Il nous faut tout d'abord le toast

```html
<div class="toast fade show" role="alert" aria-live="assertive" aria-atomic="true">
  <div class="toast-header">
    <svg class="bd-placeholder-img rounded me-2" width="20" height="20" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" preserveAspectRatio="xMidYMid slice" focusable="false"><rect width="100%" height="100%" fill="#007aff"></rect></svg>

    <strong class="me-auto">Contact</strong>
    <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Fermer"></button>
  </div>
  <div class="toast-body">
    Toast
  </div>
</div>
```

Il nous faut aussi des champs textuels:
```html
<div class="mb-3">
  <label class="form-label">Email</label>
  <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
</div>
<div class="mb-3">
  <label class="form-label">Message</label>
  <textarea class="form-control" aria-label="With textarea"></textarea>
</div>
```

Et pour finir un bouton "Envoyer":

```html
<button type="button" class="btn btn-primary">Envoyer</button>
```

On imbrique tout cela pour obtenir:

```html
<div class="toast fade show" role="alert" aria-live="assertive" aria-atomic="true">
  <div class="toast-header">
    <svg class="bd-placeholder-img rounded me-2" width="20" height="20" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" preserveAspectRatio="xMidYMid slice" focusable="false"><rect width="100%" height="100%" fill="#007aff"></rect></svg>

    <strong class="me-auto">Contact</strong>
    <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Fermer"></button>
  </div>
  <div class="toast-body">
    <div class="mb-3">
    <label class="form-label">Email</label>
    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
  </div>
  <div class="mb-3">
    <label class="form-label">Message</label>
    <textarea class="form-control" aria-label="With textarea"></textarea>
  </div>
  <button type="button" class="btn btn-primary">Envoyer</button>
</div>
```

Il manque biensûr du backend pour que le message puisse s'envoyer, mais le résultat front-end est le suivant:

<figure> 
  <img src="../contacttoast.png">
  <figcaption>Toast de contact</figcaption>
</figure>