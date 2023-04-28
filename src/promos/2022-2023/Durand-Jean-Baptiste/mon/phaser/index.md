---
layout: layout/mon.njk

title: "Phaser et CI sur Github"
authors:
  - Jean-Baptiste Durand

date: 2023-04-05

tags:
    - 'temps 3'
    - Phaser
    - Game Engine
    - Github Actions
    - Github Pages
    - Javascript
---

<!-- début résumé -->
Phaser - Game Engine + Github CI
<!-- fin résumé -->

[Lien du jeu](https://jean-baptiste-dp.github.io/PhaserEscapeRoom/)
[Lien du github](https://github.com/Jean-Baptiste-DP/PhaserEscapeRoom)

<h2 id="toc"> Table des matières </h2>

- [Table des matières](#toc)
- [Choix de la technologie](#h1)
- [Hébergement sur Github](#h2)
  - [Actions](#h2-1)
  - [Clé de déploiement](#h2-2)
    - [Access Token](#h2-2-1)
    - [Secrets](#h2-2-2)
- [Présentation de Phaser](#h3)
  - [Physique (*Physics*)](#h3-1)
    - [Arcade](#h3-1-1)
    - [Matter](#h3-1-1)
  - [Scène (*Scene*)](#h3-2)
  - [Joueur (*Sprite*)](#h3-3)
  - [Carte (*Tilemap*)](#h3-4)
- [Liens Utiles](#liens)

<h2 id="h1">Choix de la technologie</h2>

Je me suis renseigné sur 4 différents moteurs de jeu : 
- [Unity](https://unity.com/) : 
  - Code en C# et UnityScript (JS)
  - Fait tourner des jeux pour Desktop, mobile et console
- [Unreal Engine](https://www.unrealengine.com/en-US) : 
  - Code en C++ et Blueprint
  - Fait tourner des jeux pour Desktop, mobile et console
- [Godot](https://godotengine.org/) : 
  - Code en GDScript (Python) et C++
  - Fait tourner des jeux pour Desktop, mobile et console
- [Phaser](https://phaser.io/) :
  - Code en Javascript
  - Fait tourner des jeux pour web (HTML5)

Je me suis tourné vers Phaser car il permettait d'être disponible en static sur un navigateur. Ce qui, combiné avec [Github Pages](https://pages.github.com/), permet d'avoir mon jeu hébergé directement par Github sans trop de difficultés.

<h2 id="h2"> Hébergement sur Github</h2>

<h3 id="h2-1">Actions</h3>

Github propose d'**héberger gratuitement un site static** (comportant seulement des pages HTML, avec CSS et JS, mais sans serveur), c'est ce qui permet notamment d'héberger le **site de Do_It**. Pour cela, Github a besoin d'une branche sur laquelle est toute l'infrastructure statique du site.

Pour éviter d'avoir à chaque fois à mettre le site static sur une branche, on peut utiliser les [Github Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions#:~:text=GitHub%20Actions%20is%20a%20continuous,merged%20pull%20requests%20to%20production.) qui est une routine, exécutée sur une machine de Github.

Voici l'action github que j'ai mis en place, avec en dessous les informations sur les différentes fonctionnalités : 

```text
name: Build
on:
  push:
    branches:
      - main
  workflow_dispatch:
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        with:
          publish_dir: ./static
          github_token: ${% raw %}{{ secrets.DEPLOY_KEY }}{% endraw %}
```

- **Name** permet de facilement retrouver l'action si on en a plusieurs
- **on** est l'élément déclencheur de l'action, ici l'action est effectuée quand des commits sont push sur la branche *main*
- **workflow_dispatch** permet de lancer l'action manuellement depuis l'onglet **Actions** de github
- **jobs** est l'ensemble des actions à effectuer
- **runs-on** le code étant exécuté sur une machine de Github, on a la possibilité de choisir sur quelle OS va faire tourner notre code
- **actions/checkout** est une action permettant à la machine de Github, de pouvoir accéder à notre code (permet aussi d'avoir accès à d'autres repo Github si nécessaire)
- **peaceiris/actions-gh-pages** est une action permettant de publier sur la branche **gh-pages** le contenu d'un dossier (ici le dossier *static*). La machine de Github n'ayant pas les droit de modifier notre projet, il faut lui fournir un mot de passe d'accès en écriture de notre projet, d'où le *${% raw %}{{ secrets.DEPLOY_KEY }}{% endraw %}*

<h3 id="h2-2">Clé de déploiement</h3>

Bien évidement, nous n'allons pas donner aux machines de Github notre mot de passe de connexion à notre compte Github. Il faut donc trouver un moyen de donner l'accès à notre projet en évitant de se faire voler notre mot de passe.

<h4 id="h2-2-1">Access token</h4>

Github nous permet d'avoir des mots de passes ayant des accès restreints sur notre compte. On peut choisir d'avoir un accès en écriture seulement sur un projet ou autre.

Pour cela :

Settings (celui de votre compte, pas du repo) -> Developer Settings -> Personal Access Token


Vous pouvez ensuite choisir les droits de votre clé.
Il faut faire attention à ne pas donner plus de droits que nécessaire.
Donner une date d'expiration de la clé et supprimer les clés inutiles.

[Documentation officielle](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

<h4 id="h2-2-2">Secrets</h4>

Un secret est une variable qui est stockée de manière sécurisée par Github et qui peut être transmise lors de l'exécution d'actions. Un secret peut être un token d'accès (comme dans ce projet), ou par exemple l'url d'un serveur distant sur lequel déployer notre code (comme on a pu le faire sur Gitlab dans le cours AWS/Docker).

[Documentation officielle](https://docs.github.com/en/actions/security-guides/encrypted-secrets)

<h2 id="h3">Présentation de Phaser</h2>

Phaser est un moteur de jeu open source, dont le code source se trouve [ici](https://github.com/photonstorm/phaser/tree/v3.55.2).

Pour installer Phaser, il faut mettre, dans un fichier html, la balise :

```html
<script src="//cdn.jsdelivr.net/npm/phaser@3.55.2/dist/phaser.min.js"></script>
```

Le reste du code sera dans un fichier js, ou dans une autre balise *script*.

Phaser a une énorme bibliothèque d'exemples, pour voir une mise en application de chaque fonctionnalités, et un fichier API complet. Il est important de s'y référer pour voir comment implémenter une des fonctionnalités.

[exemples](https://labs.phaser.io/index.html?dir=&q=)

[API](https://photonstorm.github.io/phaser3-docs/index.html)

<h3 id="h3-1">Physique (<i>Physics</i>)</h3>

Phaser a 2 models de physique implémentée **Arcade** et **Matter**

Le choix de la physique est quelque chose de primordial car il influencera les fonctionnalités de votre application.

Les méthodes des objets ne sont pas les mêmes dans différents cas.

<h4 id="h3-1-1">Arcade</h4>

La physique **Arcade** est une physique plus simple, qui est faite pour mettre en place un projet rapidement.

C'est plus simple de le prendre en main. Par contre la détections des éléments extérieurs (blocks) n'est pas implémentée ce qui peut-être limitant.

<div class="allButtonGestionProjet">
  <a href="./phaser-build/?id=arcade" class="buttonGestionProjet">
    <span><b class="hoverUnderline">Exemple</b></span>
  </a>
</div>

<h4 id="h3-1-2">Matter</h4>

La physique **Matter** essai de se rapprocher au plus proche de la réalité, en ayant une implémentation de mécanique : il y a des frottements, il est possible de pousser des objets etc.

Il y a une variété plus importante d'objet qu'on peut créer.


<div class="allButtonGestionProjet">
  <a href="./phaser-build/?id=matter" class="buttonGestionProjet">
    <span><b class="hoverUnderline">Exemple</b></span>
  </a>
</div>

<h3 id="h3-2">Scène (<i>Scene</i>)</h3>

La scène est l'élément principal de Phaser, c'est lui qui va s'occuper de précharger les images d'initier les components et de faire tourner le jeu.

On doit créer une classe qui hérite de *Phaser.Scene*.

On peut créer 3 méthodes :
- *preload*
- *create*
- *update*

Méthodes utilisées pour charger les images (*preload*), initialiser les éléments du jeu (*create*), et effectuer des actions à chaque tick du jeu (*update*).

<h3 id="h3-3">Joueur (<i>Sprite</i>)</h3>

Un Sprite est un objet animé du jeu, il peut être contrôlé par le joueur ou par d'autres éléments du jeu. Il est créé à partir d'une image.

<div class="allButtonGestionProjet">
  <a href="./phaser-build/?id=sprite" class="buttonGestionProjet">
    <span><b class="hoverUnderline">Exemple</b></span>
  </a>
</div>

<h3 id="h3-4">Carte (<i>Tilemap</i>)</h3>

La carte du jeu peut-être générée en plaçant des bloques un par un ou en utilisant une Tilemap qui va contenir toutes les informations pour créer la map.

La carte peut être composée de plusieurs couches, dont des touches qui créent des collisions ou non. C'est pratique pour générer des décors de fond, et les blocks avec lesquels notre personnage va interagir.

<div class="allButtonGestionProjet">
  <a href="./phaser-build/?id=map" class="buttonGestionProjet">
    <span><b class="hoverUnderline">Exemple</b></span>
  </a>
</div>

<h2 id="h4">Mon point de vue</h2>

**Points positifs** 👍

- Phaser est très bien documenté avec un très grand nombre d'exemples différents.
- Il n'y a pas besoin d'installer de logiciel ou autre.

**Points négatifs** 👎

- Il vaut mieux s'adapter à Phaser que essayer que suivre à la lettre ce qu'on a comme idée (contrôle limité sur les détails de bas niveau).
- Il n'est pas aisé d'avoir un projet organisé en différents fichier. J'ai fait en sorte de séparer le code du joueur du code global, mais ce n'a pas été facile. Donc il n'est pas trop possible de faire des gros projets.
- Il n'y a pas de réel cours, il y a une explication du "Hello World!", puis l'utilisateur est encouragé à aller voir les différents exemples.

<h2 id="liens">Liens Utiles </h2>

**Mon projet**
- [Lien du jeu](https://jean-baptiste-dp.github.io/PhaserEscapeRoom/)
- [Lien du github](https://github.com/Jean-Baptiste-DP/PhaserEscapeRoom)

**Github**
- [Github Pages](https://pages.github.com/)
- [Github Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions#:~:text=GitHub%20Actions%20is%20a%20continuous,merged%20pull%20requests%20to%20production.)
- [Github Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- [Github Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets)

**Phaser**
- [Site Web](https://phaser.io/)
- [Bibliothèque d'exemples](https://labs.phaser.io/)
- [API](https://photonstorm.github.io/phaser3-docs/index.html)

<style>
  a.buttonGestionProjet{
    display: flex;
    position: relative;
    height: 40px;
    width: 150px;
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
