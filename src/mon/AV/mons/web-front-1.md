---
layout: layout/post.njk

title: "Web Front 1"
authors:
  - Antoine Varnerot

---
<head>
  <link rel="stylesheet" href="../../assets/style.css">
</head>

## Description

Pour ce MON, étant donné que j’ai fait un stage en développement web, j’ai décidé d’utiliser les 10h de temps en autonomie pour reprendre les quelques connaissances que j’avais du framework Angular et de les approfondir. J’ai choisi ce framework car il fait partie de la stack utilisé dans mon alternance.


## Premiers pas

### 1. Installations

Sur un terminal, installer le CLI d'Angular (Command Line Interface) à l'aide de npm. 

`npm install -g @angular/cli`

<mark>Note : -g signifie qu'on installe Angular "globalement" sur l'ordinateur et qu'on aura pas à le réinstaller pour chaque projet</mark>

### 2. Créer un projet

Pour créer un projet, on écrit dans le terminal et à l'endroit voulu :
`ng new mon-projet`

<mark>Note : ng fait référence à Angular et sera l'abréviation à utiliser pour toutes les autres commandes que l'on va utiliser.</mark>

Cette commande va créer un dossier avec plusieurs fichiers mais celui qui va le plus nous intéresser est le dossier src (source). C'est ce dossier que l'on va modifier et où on va coder notre site. Voici l'arborescence de ce dossier :

```bash
src
    ├── app
    ├── assets
    ├── environnements
    ├── index
    ├── main
    ├── styles
    .
    .
    .

```

Pour visualiser son site, il faut le lancer sur un serveur. Dans un terminal ouvert au dossier du projet, lancez la commande :
`ng new mon-projet`
Ensuite rendez-vous à l'adresse http://localhost:4200/ et ceci devrait s'afficher :
<figure>
  <img src="../../assets/Angular-init.png">
  <figcaption>Application Angular basique</figcaption>
</figure>
C'est la page qu'Angular génère de base quand on crée un projet.


### 3. Components

Angular, comme plusieurs autres framework JS, fonctionne grâce à des <i>components</i> (composants en français). Ce sont des blocs qui vont constituer une page web. Par exemple sur le site https://francoisbrucker.github.io/cours_informatique/cours/ on pourrait identifier plusieurs components :

<figure> 
  <img src="../../assets/ComponentsExplication.png">
  <figcaption>Exemple de découpage d'une page web en composant</figcaption>
</figure>
Ces composants permettent d'organiser le code et de gagner du temps. En effet, en découpant le code en petits morceaux qui s'occupent seulement d'une fonction, on s'y retrouve plus facilement. De plus, les composants sont réutilisables.

Pour créer un composant, on se place dans le terminale et on tape :
`ng generate component navbar`
(Si on veut l'appeler navbar)

Notre component est maintenant créé ! Il est constitué de 4 fichiers :

```bash
navbar
    ├── navbar.component.html
    ├── navbar.component.css
    ├── navbar.component.spec.ts
    ├── navbar.component.ts

```
<mark>Note : Le fichier app.module.ts a aussi été mis-à-jour pour afin de bien importer ce component.</mark>

En se baladant dans le fichier Typescript, on remarque que pour faire appel à la balise html de ce composant on va devoir taper :
```html
<app-navbar></app-navbar>
```
On peut alors essayer de l'implémenter dans notre MON :

IMAGE AVEC "navbarworks" 

Le composant de la barre de navigation s'affiche bien ! J'aime bien travailler avec Bootstrap pour avoir des beaux éléments sans faire trop de CSS. On va donc prendre une navbar de Bootstrap pour travailler avec. 

<mark>Note : Pour implémenter Bootstrap sur un projet Angular, il faut l'installer avec npm et le rajouter dans le document angular.json (tuto : https://stackoverflow.com/questions/43557321/angular-4-how-to-include-bootstrap)</mark>