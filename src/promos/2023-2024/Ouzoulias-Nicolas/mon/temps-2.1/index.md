---
layout: layout/mon.njk

title: "Faire les backs : partie 1 "
authors:
  - Nicolas Ouzoulias

date: 2023-09-17
tags: 
  - "temps 2"

résumé: "Un MON pour découvrir le back d'un site web : partie 1"
---

## Objectifs


Ce premier MON du temps 2 a pour objectif de m'initiner à la partie back d'un site Web pour m'aider dans la réalisation des sites web de mon POK et du projet 3A. 

Pour cela je vais suivre les cours de monsieur Brucker sur son site internet. 

## I. Initiation à JavaScript

Pour bien utiliser Node.js je dois me mettre à niveau en JavaScript. Grâce au projet 3A et aux cours d'info de Do-It j'ai pu expérimenté quelques fois ce langage mais j'ai encore beaucoup trop de lacunes et trop peu de connaissances. Je vais donc tout d'abord revoir les bases de ce langage pour mieux comprendre Node.js et tout le back. 

JavaScript peut être utilisé en *front* et en *back* : 
- *front* : c'est le côté **client**, JS permet de rendre la page plus dynamique et de permettre à ce dernière d'intéragir plus profondément avec le site
- *back* : c'est le côté **serveur**, JS permet de travailler avec des environnements comme Node.js afin de gérer tout ce qui est base de données par exemple. 

Tout comme Python, JS est un langage interprété et le code va donc s'éxecuter de haut en bas en renvoyant le résultat immédiatement. Contrairement par exemple au C et au C++ qui sont compilés en langage assembleur pour  ensuite être exécuté par l'ordinateur.

Le script JS se lie avec le code HTML grâce à cette ligne de code : 
``` html
<script src="script.js"></script>
```

Le fonctionnement et la syntaxe de JS sont globalement assez sembables à Python et c'est donc assez facile de prendre en main ces aspects du langage. On y retrouve de multiples similitudes : 

- l'utilisation de variables
```js 
let myVariable = 12 //déclaration de la variable
my variable = 14 //modification de la variable

const myConst = "Daniel" //déclaration d'une constante
```
- la programmation orientée objet
``` js
let monPC = {
  marque: "Dell",
  gamme: "XPS",
  couleur: "gris",
  annee: "2021"
}

let maMarque = monPC.marque //appel à une propriété
```

- les conditions et boucles
```js
if (condition){
  ...
}else{
  ...
}

for (let i = 0; i<5; i++){
  ...}

let i = 0
while(i<5){
  ...}
```

Le grand intérêt du JS est le lien avec les langages HTML et CSS. Il permet : 
- **d'ajouter des balises**
- **d'en supprimer**
- **de les modifier**

Pour cela il faut tout d'abord récupérer les éléments d'une page Web grâce aux diverses méthodes 

``` js
let baliseZone = document.getElementById("zone"); //pour récupérer un élément particulier

let baliseZoneSpan = document.querySelector("#zone span"); //pour récupérer seulement un type parmi un groupe parent (comme un div par exemple)

let listeInputRadio = document.querySelectorAll(".zoneChoix input"); //pour récupérer tous les inputs du groupe parent zoneChoix
```

Afin d'avoir une page plus dynamique il faut programmer de **manière événementielle**. Les événements peuvent être : un clic de la souris, une frappe d'une clavier, un bouton coché, ... 
Ces derniers sont écoutés grâce à *addEventListener* puis utilisés à l'aide d'une fonction *=>*

```js
monBouton.addEventListener("click", () => {
    console.log("Vous avez cliqué sur le bouton")
});
```

