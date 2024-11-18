---
layout: layout/mon.njk

title: "Web Front 1"
authors:
  - Antoine Varnerot
tags:
  - 'temps 1'

date: 2022-10-07
---

<head>
  <link rel="stylesheet" href="../assets/style.css">
</head>

## Description

Pour ce MON, étant donné que j’ai fait un stage en développement web, j’ai décidé d’utiliser les 10h de temps en autonomie pour reprendre les quelques connaissances que j’avais du framework Angular et de les approfondir. J’ai choisi ce framework car il fait partie de la stack utilisé dans mon alternance.
L'objectif de ce MON est d'expliquer comment j'ai fait mon POK et notamment comment Angular m'a aidé. Je me suis aidé du tuto : https://openclassrooms.com/fr/courses/7471261-debutez-avec-angular (10h selon eux, moins si on a déjà des bases en Javascript) et du tuto (en anglais) Getting Started disponible sur le site https://angular.io/docs.

Pour avoir quelques informations sur ce framework avant de commencer, j'ai d'ailleurs lu :

https://webojob.ch/technologies/javascript/angular
https://www.codeur.com/blog/choisir-framework-javascript/


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
  <img src="../assets/Angular-init.png">
  <figcaption>Application Angular basique</figcaption>
</figure>
C'est la page qu'Angular génère de base quand on crée un projet.


### 3. Components

Angular, comme plusieurs autres framework JS, fonctionne grâce à des <i>components</i> (composants en français). Ce sont des blocs qui vont constituer une page web. Par exemple sur le site https://francoisbrucker.github.io/cours_informatique/cours/ on pourrait identifier plusieurs components :

<figure> 
  <img src="../assets/ComponentsExplication.png">
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
On peut alors essayer de l'implémenter dans notre MON. Pour cela, on place cette balise à la place de tout ce qu'il y a dans app.component.html. Sur notre page locale, on peut ainsi voir ceci : 

<figure> 
  <img src="../assets/navbarWorks.png">
  <figcaption>Implémentation d'un componenent</figcaption>
</figure>

Le composant de la barre de navigation s'affiche bien ! On peut maintenant de créer une vraie navbar et lui donner un peu de style.


### 4. Navbar

J'aime bien travailler avec Bootstrap pour avoir des beaux éléments sans faire trop de CSS. On va donc prendre une navbar de Bootstrap pour travailler avec. 

Pour implémenter Bootstrap sur un projet Angular, il faut l'installer avec npm et le rajouter dans le fichier angular.json (tuto : https://stackoverflow.com/questions/43557321/angular-4-how-to-include-bootstrap).

J'ai choisi une navbar simple pour commencer : 

```html
<nav class="navbar navbar-expand-lg navbar-light fixed-top">
    <div class="container">
        <a class="navbar-brand" href="#">Antoine Varnerot</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ml-auto">
                <li class="nav-item">
                    <a class="nav-link" href="#parcours">Parcours</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#projets">Projets</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#contact">Contact</a>
                </li>
            </ul>
        </div>
    </div>
</nav>
```

Après avoir copié ce code dans le fichier navbar.component.html, on devrait avoir une navbar qui s'affiche en haut de la page.
Pour les différentes parties du site (parcours, projets, contact), on va aussi créer un component. Je créé ainsi un component <i>accueil</i> qui se placera sous la navbar qui faira office de page d'accueil, un component <i>overview</i> qui contiendra une brève présentation de moi et un component <i>skills</i> qui contiendra mon parcours et mes compétences.

### 5. Interactions HTML/TS

Un des grands intérêts d'avoir de travailler avec un framework est qu'on va gagner du temps. Par exemple, on peut utiliser des variables du fichier Typescript dans le HTML, on peut écouter des événements et indiquer quelle fonction appeler si l'événement se produit ...
Je vais présenter la syntaxe pour effectuer des actions de ce type et expliquer en quoi cela peut servir dans le projet de port-folio.

- Pour afficher une variable TS dans le fichier HTML du même component on écrit :

```html 
<img [src]="imageUrl" [alt]="title">
```
Avec bien sur imageUrl et title des variables définies dans le fichier Typescript. Par exemple :
```typescript 
imageUrl!: string;
title: string;
ngOnInit(){
  this.imageUrl = "https://www.nature-isere.fr/sites/default/files/styles/natureisere_large/public/images/temoignages/principale/iceland-2111810_1920.jpg?itok=PMXb-dCB";
  this.title = "paysage";
}

```
On parle alors de <strong>attribute binding</strong>.

- Pour écouter un événement et appeler une function s'il se produit : 
```html
<button (click)="myFunction()">Cliquez ici!</button>
```
```typescript
myFunction(){
  //Actions
}
```
On parle alors d'<strong>event binding</strong>.


Note : On peut bien sur combiner les différentes syntaxes. Pour compter le nombre de fois qu'on appuie sur un bouton on peut écrire :
 ```html
<button (click)="addOne()">{{counter}}</button>
```
```typescript

ngOnInit(){
  counter: number = 0;
}


addOne(){
  this.counter++
}
```

<!-- Pour le MON, j'ai décidé de mettre dans le component <i>accueil</i>, des boutons  -->

### 6. Conditionnement et Boucles

Dans la même idée que la partie précédente, il est possible d'utiliser des conditions et des boucles Typescript directement dans le HTML pour par exemple afficher ou non des éléments. Cela pourrait nous aider dans le MON pour l'affichage des projets. On va supposer que l'on dispose d'une classe Project qui dispose des attributs title (string), techs (string[]), description (string), keyword (string[]) et image (string) qui est optionnelle. 

Pour rendre le code plus lisible, on va créer un fichier dont le seul but sera de créer la classe Project. 

```typescript
export class Project {
  public title!: string,
  public techs!: string[],
  public description!: string,
  public keyword!: string[],
  public image?: string
}
```
Note : Le point d'interrogation à coté de l'attribut image permet de dire que cet attribut est optionnel.

Avec ce que l'on a vu précédemment, on pourrait afficher des projets :

```typescript

import { Project } from '../models/project.model';

project1!: Project;
project2!: Project;

ngOnInit(): void {

  this.project1 = 
  {
    title: "Projet 1",
    techs: ["Angular", "PHP"],
    description: "Un petit projet avec Angular",
    keyword: [""],
    image: "monImage.png"
  } 
  this.project2 = 
  {
    title: "Projet 2",
    techs: ["Javascript", "Scss"],
    description: "Projet pour découvrir un framework css",
    keyword: ["style","scss"],
  }

}
```
Et dans le code HTML : 

```html {% raw %}
<p>{{ project1.title }}</p>
<p>{{ project1.description }}</p>
<p>{{ project1.techs[0] }}</p>
<p>{{ project2.title }}</p>
<p>{{ project2.description }}</p>
<p>{{ project2.techs[0] }}</p>
{% endraw %}
```

Mais il existe des méthodes plus faciles pour faire cela !


#### A. *ngFor

*ngFor permet d'itérer sur un tableau dans le code HTML. Reprenons l'exemple précédent. Organisons plutôt nos projets dans un tableau : 
```typescript
projects!: Project[];

ngOnInit(): void {
  this.projects = [
    {
      title: "Projet 1",
      techs: ["Angular", "PHP"],
      description: "Un petit projet avec Angular",
      keyword: [""],
      image: "monImage.png",
    },
    {
      title: "Projet 2",
      techs: ["Javascript", "Scss"],
      description: "Projet pour découvrir un framework css",
      keyword: ["style","scss"],
    }

  ]
}
```
Pour afficher tous nos projets on va écrire :
```html{% raw %}
<div *ngFor="let project of projects">
    <p>{{project.title}}</p>
    <p>{{project.description}}</p>
</div>{% endraw %}
```
#### B. *ngIf

De manière similaire, on peut imposer des conditions aux projets. Par exemple, on peut avoir envie d'afficher que les projets qui ont une image.
```html{% raw %}
<div *ngFor="let project of projects" >
   <div *ngIf="project.image"> 
        <p>{{project.title}}</p>
        <p>{{project.description}}</p>
    </div>
</div>{% endraw %}
```