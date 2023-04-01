---
layout: layout/post.njk

title: "Phaser et CI sur Github"
authors:
  - Jean-Baptiste Durand

tags:
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

<h2 id="liens">Liens Utiles </h2>

**Mon projet**
- [Lien du jeu](https://jean-baptiste-dp.github.io/PhaserEscapeRoom/)
- [Lien du github](https://github.com/Jean-Baptiste-DP/PhaserEscapeRoom)

**Github**
- [Github Pages](https://pages.github.com/)
- [Github Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions#:~:text=GitHub%20Actions%20is%20a%20continuous,merged%20pull%20requests%20to%20production.)
- [Github Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- [Github Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
