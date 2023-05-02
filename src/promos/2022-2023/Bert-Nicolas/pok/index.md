---
layout: layout/pok-index.njk

title: "Jeu Mots croisés"
authors:
  - Nicolas BERT
  - Jean-Baptiste DURAND
---

<!-- début résumé -->
Jeu de mots croisés (Svelte, NestJS, PostgreSQL)
<!-- fin résumé -->

{% info "**Liens GitHub**" %}

* Front-end : [https://github.com/nbert71/mots-croises-front](https://github.com/nbert71/mots-croises-front)
* Back-end : [https://github.com/nbert71/mots-croises-back](https://github.com/nbert71/mots-croises-back)
* Microservice: [https://github.com/Jean-Baptiste-DP/mots-croises-generateur](https://github.com/Jean-Baptiste-DP/mots-croises-generateur)

{% endinfo %}

<a href="http://balsamite.ovh1.ec-m.fr" class="imageContainer">
  <img src="./images/gamePage.png" alt="Page de jeu" class="viewPage">
  <div class="infoTitles">
    <p class="title">Mots croisés</p>
    <p class="link">http://balsamite.ovh1.ec-m.fr</p>
  </div>
</a>

<br>

## Gestion de projet

<div class="allButtonGestionProjet">
  <a href="./temps1" class="buttonGestionProjet">
    <span><b class="hoverUnderline">Temps 1 :</b> Un site chez moi</span>
  </a>

  <a href="./temps2" class="buttonGestionProjet">
    <span><b class="hoverUnderline">Temps 2 :</b> Serveur distant</span>
  </a>

  <a href="./temps3" class="buttonGestionProjet">
    <span><b class="hoverUnderline">Temps 3 :</b> Amélioration continue</span>
  </a>
</div>

## Idée de ce POK

L'idée de ce POK est de créer une site contenant une partie frontend, une partie backend qui va communiquer avec le frontend via une API. On ajoutera également une base de données afin de pouvoir stocker les informations.

Dans ce POK nous allons recrée un jeu de ticket à gratter : le jeu de mots croisés. Voici une photo du ticket en question :

<img src="./images/mots-croises.jpg" alt="Image jeu de mots croisés" style="width: 350px; margin: 0 auto;" />
<br>

{% info "**Règles du jeu**" %}

Nous disposons de 14 cases **?** et d’une grille de mots. Derrière chaque case se trouve une lettre qui apparaît dans la grille. A chaque lettre révélée il faut gratter les occurrences de cette lettre dans la grille. Une fois toutes les cases **?** grattées, on remporte de l’argent suivant le nombre de mots entièrement reconstitués.
{% endinfo %}

## Technologies utilisées

<img src="./images/choix_techno.jpg" alt="Technologies utilisées" style="width: 700px; margin: 0 auto; border: 0" />

* **Front-end** : Svelte + TailwindCSS
* **Back-end** : NestJS
* **API** : REST
* **Moyen d'authentification** : JWT (*JSON Web Token*)
* **Base de données** : PostgreSQL

## Schéma d'entités

<div style="display: grid; place-items: center;">
  <img src="./images/UML-POK-1.png" alt="Schéma d'entités" style="border: 0;" />
</div>

On a une relation OneToMany entre User et Game ==> un user peut avoir plusieurs parties alors qu'une partie ne peu avoir qu'un seul player.

## Fonctionnalités

Par la suite, le back-end fera appelle à un service externe qui à l'aide d'un algorithme s'occupera de générer la grille de mots croisés à partir d'une liste de mots.

Gestion des utilisateurs, avec connexion et gestion de solde.

<style>
  a.imageContainer{
    margin: 50px auto;
    width: 550px;
    display: block;
    border: 4px solid rgb(22,163,74);
    border-radius: 25px;
    --opacity:0.2;
    transition: all 1s;
    background-color : rgba(22,163,74,var(--opacity));
    text-decoration:none;
  }
  a.imageContainer:hover{
    --opacity:0.6;
  }
  img.viewPage{
    width:500px;
    margin: 25px 25px 15px 25px;
    border-width:0;
  }
  div.infoTitles .title{
    font-size:32px;
    margin: 0 0 10px 0;
    text-align: center;
    font-weight: bolder;
  }
  div.infoTitles .link{
    margin: 0 0 25px 0;
    text-align: center;
    font-weight: 350;
  }
  a.buttonGestionProjet{
    display: flex;
    position: relative;
    height: 50px;
    width: 280px;
    background-color: rgb(22,163,74);
    border-radius: 15px;
    text-align: center;
    justify-content: center;
    align-items:center;
    border: 4px white solid;
    outline: 4px rgb(22,163,74) solid;
    text-decoration: none;
    transition: transform 0.3s cubic-bezier(.12,-0.91,.85,1.86);
  }
  a.buttonGestionProjet:hover{
    transform: scale(1.1);
  }
  a.buttonGestionProjet span{
    display: block;
    color: white;
  }
  div.allButtonGestionProjet{
    display:flex;
    flex-direction:row;
    justify-content: space-around;
  }
  .hoverUnderline{
    position:relative;
  }
  a.buttonGestionProjet .hoverUnderline::after{
    content:"";
    position: absolute;
    bottom:0;
    left:0;
    height: 0.125em;
    width: 0;
    background-color:white;
    transition: all 0.6s;
  }
  a.buttonGestionProjet:hover .hoverUnderline::after{
    width:100%;
  }
</style>
