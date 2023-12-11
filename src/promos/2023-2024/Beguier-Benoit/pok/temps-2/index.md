---
layout: layout/pok.njk

title: "Ouais Benoît fait son site Internet"
authors:
  - Benoit BEGUIER

date: 2023-12-13

tags: 
  - "temps 2"
  - "Spotify"
  - "Playlist"
  - "HTML"
  - "CSS"
  - "API"

résumé: Je vais dans ce POK créer mon site Internet permettant à l'utilisateur d'analyser ses goûts musicaux, en utilisant l'API de Spotify.
---

{% prerequis %}
**Niveau :** débutant
**Prérequis :**

- Bases de développement Web (HTML et CSS)
- Des prérequis en utilisation d'API peuvent être un plus mais ne sont pas indispensables
{% endprerequis %}

Pour la réalisation de ce cours, je me réfèrerais aux sources listées ci-dessous :

- *Créez votre site web avec HTML5 et CSS3.* OpenClassrooms. Accessible [ici](https://openclassrooms.com/fr/courses/1603881-creez-votre-site-web-avec-html5-et-css3).
- Developer Mozilla. Accessible [ici](https://developer.mozilla.org/fr/)

## Sommaire

1. Objectifs du Sprint 1
2. Objectifs du Sprint 2
3. Maquette Figma
4. Création des pages du site en HTML
5. Mise en page V1 en CSS
6. Retour d'expérience du Sprint 1

Le but de ce POK est de mettre en pratique mon MON1.2 sur le développement web. Je souhaite créer un site web fonctionnel, qui utilise l'API de Spotify. Ce site permettrait à l'utilisateur de connecter son compte Spotify personnel, et en retour afficher une analyse de ses goûts musicaux.

{% exercice %}
"Analyser les goûts musicaux de l'utilisateur" : ça veut dire quoi concrètement ?
{% endexercice %}

Il y a une multitude d'analyses possibles à partir d'un compte Spotify.
Concrètement j'aimerais proposer les fonctionnalités suivantes :

- Afficher une liste des principaux genres de musique que l'utilisateur écoute
  - Si possible, afficher un graphique des genres écoutés en fonction de l'heure de la journée. Cela pourrait (et je dis bien pourrait) potentiellement mettre en avant une tendance de l'utilisateur : par exemple des musiques mouvementées à haut *bpm* (*beats per minute*) en fin d'après-midi lors de sa séance de sport.

- Afficher le Top 5 des musiques écoutées depuis le début de l'année par l'utilisateur

- Afficher des graphiques décomposant les musiques écoutées par l'utilisateur selon des paramètres définis dans la suite du POK.

![features](Music-features.jpg)
Ces graphiques prennent en ordonnée des paramètres tels que le tempo, la dançabilité

- En bonus, effectuer une analyse en composantes principales (ACP, *PCA* en anglais) des musiques écoutées par l'utilisateur, et afficher le spectre d'écoute (*cf.* image ci-dessous). Vous pourrez trouver [ici](https://fr.wikipedia.org/wiki/Analyse_en_composantes_principales) la documentation sur l'ACP.

![spectre](spectre.jpg)
Illustration du type de graphique que je souhaite afficher.

## Objectifs du Sprint 1

Voici les objectifs que je me suis fixé :

- Première maquette sur Figma (★☆☆☆☆, 2 heures estimées)
- Création des pages et de leur contenu primaire en HTML (★☆☆☆☆, 4 heures estimées)
- Mise en page V1 en CSS (★★☆☆☆, 4 heures estimées)

Les étoiles correspondent au niveau de difficulté de l'objectif dans mon référentiel de débutant en DevWeb.

## Objectifs du Sprint 2

Voici les objectifs que je me suis fixé :

- Lier l'API de Spotify avec mon site
- Travailler sur les différentes fonctionnalités d'affichage de données de l'utlisateur en lien avec son compte Spotify

## Maquette Figma

Avant de partir dans tous les sens, il est nécessaire de cadrer le projet en amont. Mon but est d'offrir à l'utilisateur une expérience simple et personnalisée.

Je choisis en premier lieu une interface simple et épurée. Afin de rappeler la proximité de mon service avec Spotify, je conserve en couleur secondaire la couleur du logo Spotify : #1ED760.

Je crée aussi un logo se basant sur la forme ronde du logo Spotify, mais en y incluant un rappel de statistiques au travers des courbes de tendances. Je choisis ainsi le nom de mon service : **Spotistats**.

![Logo](Allonge.png)

Je choisis ensuite le type de boutons de ma page Web. Je télécharge les icones sur le site [Flaticon](https://www.flaticon.com/). J'utilise le pack d'icônes [*Outline*](https://www.flaticon.com/authors/icongeek26/outline?author_id=296&type=standard) créé par Icongeek26.

Je définis les composantes de mes pages :

- les boutons seront des rectangles de 330px*65px, avec des bords arrondis de 38px.

![bouton](Group-1.png)

- le header fait 1440px*120px, de couleur #25242F, avec une ombre portée grise.

![Header](Header.png)

- la page fait 1440px*1024px (dimension Desktop), de couleur #25242F qui rappelle le mode sombre sur Spotify. Les titres de section sont écrits avec la police Gotham de couleur #1ED760, tandis que le corps de texte est blanc en Roboto Light de 25px.

![Accueil](Accueil.png)

Ma maquette Figma est accessible [ici](https://www.figma.com/file/Rx2sAj4SSzLNnZjNFwKq6O/Spotistats?type=design&node-id=0%3A1&mode=design&t=T7OGaQuYW9phVxnz-1).

## Création des pages du site en HTML

Rien de très intéressant à ajouter dans cette partie, si ce n'est que je vais transformer la maquette Figma en HTML et en CSS.

Voici le résultat pour la page d'accueil :
![Accueil](AccueilHtml.png)

{% details "Cliquez pour afficher le **code HTML** de la page d'accueil%}

```html
<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Accueil - Spotistats 📈</title>
        <link href="styles.css" rel="stylesheet">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
    </head>
    <body>
        <header>
            <img src="Allonge.png" class="logo" width="15%" height="60%" >
            <a class="FAQ" href="FAQ.html">FAQ</a>
            <button class="Connexion">
                <img src="Spotify_black.png" width="38" height="39">
                <span class="ButtonText">S’identifier avec Spotify</span>
            </button>
        </header>

        <div class="container">
            <img src="chart-up 1.png" class="arrow">
            <div class="column">
                <h1> Toutes vos statistiques.</h1>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
                    Sit amet dictum sit amet justo donec. Dolor sed viverra ipsum nunc aliquet 
                    bibendum enim facilisis. Erat imperdiet sed euismod nisi porta. Viverra 
                    accumsan in nisl nisi scelerisque eu ultrices. In vitae turpis massa sed elementum. 
                    Pretium aenean pharetra magna ac placerat vestibulum. Quis vel eros donec ac odio tempor. 
                    Felis donec et odio pellentesque diam volutpat commodo. Et tortor consequat id porta nibh
                    venenatis.
                </p>
            </div>
        </div>

        <div class="container2">
            <div class="column2">
                <h1> Analysez vos goûts musicaux.</h1>
                <p class="parap2">Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
                    Sit amet dictum sit amet justo donec. Dolor sed viverra ipsum nunc aliquet 
                    bibendum enim facilisis. Erat imperdiet sed euismod nisi porta. Viverra 
                    accumsan in nisl nisi scelerisque eu ultrices. In vitae turpis massa sed elementum. 
                    Pretium aenean pharetra magna ac placerat vestibulum. Quis vel eros donec ac odio tempor. 
                    Felis donec et odio pellentesque diam volutpat commodo. Et tortor consequat id porta nibh
                    venenatis.
                </p>
            </div>
            <img src="sound 1.png" class="sound">
        </div>
        
    </body>
</html>
```

{% enddetails %}

{% details "Cliquez pour afficher le **code CSS** de la page d'accueil%}

```css
body {
    margin: 0;
    padding: 0;
    background-color: #25242F;
    display: flex;
    flex-direction: column;
}

header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #25242F;
    height: 90px;
    padding: 0 30px;
    box-shadow: 0 4px 17px rgba(81, 95, 95, 0.25);
}

.logo {
    margin-right: 30px;
}

.FAQ {
    order: 1;
    font-size: 25px;
    font-weight: bolder;
    font-family: 'Roboto', sans-serif;
    color: #FFFFFF;
    text-decoration: none;
    justify-content: center;
    margin-left: 520px;
}

button.Connexion {
    order: 2;
    display: flex;
    align-items: center;
    justify-content: flex-end;
    text-align: right;
    font-size: 25px;
    font-weight: bolder;
    background-color: #1ed760;
    font-family: 'Roboto', sans-serif;
    border: none;
    border-radius: 38px;
    width: 360px;
    height: 55px;
    margin-left: 30px;
}

.ButtonText {
    margin-right: 18px;
    margin-left: 10px;
    font-weight: bold;
}

button.Connexion img {
    margin-right: 10px;
}

button:hover {
    box-shadow: 6px 6px 10px rgba(0, 0, 0, 0.5);
}

@font-face {
    font-family: 'Gotham-Bold';
    src: url('Spotify-Font/Gotham-Bold.otf') format('opentype');
    font-weight: normal;
    font-style: normal;
}

.container {
    display: flex;
    flex-direction: row;
    justify-content:flex-start;
    align-self: center;
}

.column {
    display: flex;
    flex-direction: column;
    margin-top: 40px;
    margin-left: 70px;
    width: 650px;
    margin-right: 50px;
}

h1 {
    font-family: 'Gotham-Bold', sans-serif;
    font-size: 40px;
    color: #1ed760;
    margin-bottom: 10px;
}

p {
    font-family: 'Roboto', sans-serif;
    color: #FFFFFF;
    font-size: large;
    width: 600px;
    text-align: justify;
}

.arrow {
    width: 41.6%;
    height: 41.4%;
    margin-top: 70px;
}

.sound {
    width: 55%;
    height: 55%;
    margin-top: 30px;
}

.container2 {
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-self: center;
}

.column2 {
    display: flex;
    flex-direction: column;
    margin-top: 0px;
    margin-left: 50px;
    margin-right: 30px;
    width: 950px;
}

.parap2{
    width:950px;
}

```

{% enddetails %}