---
layout: layout/mon.njk

title: "Angular"
authors:
  - Arthur Louradou

date: 2024-02-28

tags: 
  - "temps 3"
  - "front-end"
  - "JavaScript"
  - "TypeScript"
  - "Angular"
  - "framework"  

résumé: "Angular est un framework TypeScript basé sur une architecture très uilisée dans le milieu professionnel. Il est très complet et permet de créer des applications web de grande envergure."
---

## Prérequis

Des bases en développement Front-End et en Javascript. La connaissance d’un framework javascript en particulier n’est pas nécessaire, même si je pars avec des bases d’Angular et une connaissance de React.

## Autres MONs

Killian avait en 2023 présenté [un MON sur les différents frameworks Front-End](/promos/2022-2023/Royant-Killian/mon/temps_3/technologies/) et en particulier y a consacré une section sur Angular.

## Objectifs du MON

Dans le passé, j'ai utilisé Angular dans un contexte professionnel sans avoir une connaissance approfondie. Mon objectif est de combler cette lacune en acquérant une compréhension approfondie d'Angular. Je prévois d'explorer ses fonctionnalités, d'établir des bonnes pratiques et de l'appliquer dans des projets concrets.

J’ai par exemple eu besoin de comprendre l’architecture des projets pour lesquels j’ai travaillé (séparation en modules, services et composants), de maîtriser les concepts de base (composants, directives, pipes, services) et de comprendre le fonctionnement de la détection de changements pour optimiser les performances de ce que j’ai développé. C’est le sujet sur lequel nous allons principalement nous concentrer pour ce MON.

## Angular - Histoire et contexte

JavaScript a été créé en 1995. Il a été conçu comme un langage de script pour rendre les pages web plus interactives. Par la suite, JavaScript a évolué avec l'introduction de nombreuses mises à jour et standards, notamment ECMAScript, qui est devenu un standard de langage pour JavaScript. TypeScript, introduit par Microsoft en 2012, est un sur-ensemble de JavaScript qui ajoute des types statiques et d'autres fonctionnalités pour rendre le code JavaScript plus robuste et plus facile à maintenir. Angular, développé par Google, est un framework open-source basé sur TypeScript qui permet de créer des applications web dynamiques. Il a été initialement lancé en 2010 sous le nom d'AngularJS et a subi une refonte majeure en 2016 pour devenir Angular. [[1]](#bibliographie)

Dans cette optique, nous allons mettre l’accent sur les bonnes pratiques sur l’utilisation d’Angular, apprendre à l'utiliser efficacement avec TypeScript et comprendre comment il se compare à d'autres Frameworks comme React.

## Les bases de Javascript appliquées à Angular

### Fonctions asynchrones

L’avantage des fonctions asynchrones est la possibilité de lancer plusieurs traitements en parallèle sans avoir à attendre la fin de l’un pour commencer l’autre. Cela évite de bloquer l’application durant l’exécution d’une longue tâche. C'est un concept clé en programmation qui facilite la gestion des opérations qui prennent du temps, comme les requêtes API par exemple.

### Event Loop

Dans cette partie, nous allons expliciter des fondamentaux de l’ordre d’exécution des fonctions en JavaScript, dont l’ignorance provoque beaucoup d’erreurs inexplicables.

Voici un exemple assez parlant :

```javascript
var value;

setTimeout(function () {
    value = 'VALUE';
}, 0 /* 0 ms. */);

console.log(value); // 1 - undefined

setTimeout(function () {
    console.log(value); // 3 - VALUE
}, 0);

console.log(value); // 2 - undefined
```

Ici, nous inscrivons des **fonctions de callback**  `function() {}` après l’exécution des **événements** `setTimeout, addEventListener, ...`. Le **thread** garde en mémoire la file d’exécution et joue les événements asynchrones dans l’ordre.

### Programmation orientée objet

En JavaScript, tout est objet. Cependant, c’est un langage très peu typé, ce que TypeScript vient corriger à sa manière. Nous allons voir ce qui le caractérise.

La norme ECMAScript 2015 (ES6) caractérise les objets de cette manière [[2]](#bibliographie) :

```javascript
class ClassName {
  constructor() { ... }
}
```

### var, let, const

Petit point sur ces mots clés avant les variables [[4]](#bibliographie) : `let` ne permet l’accès aux variables que dans leur scope et après leur déclaration. On ne peut pas déclarer deux fois avec `let`. `const` permet quant à lui de ne pas réinitialiser une constante par erreur. `var` peut être redéclaré et causer des erreurs.

On préfèrera utiliser `let` et délaisser `var` pour des raisons de clareté et de lisibilité.

{% info %}
Une convention de nommage définit le préfixe `_` devant une variable comme la visibilité `private` dans des languages plus typés. Cela donne des fonctions comme `_function()` et des variables sous forme `this._variable`.
{% endinfo %}

### Binding dans les classes et les callbacks

Le binding dans les callbacks en JavaScript est une méthode pour s'assurer que la valeur de "this" dans une fonction de rappel correspond à l'objet attendu, et non à l'objet global.

### Exemple de Binding dans les classes et les callbacks

Supposons que vous avez une classe `Person` avec une méthode que vous voulez utiliser cette méthode comme un callback.

```javascript
class Person {
  constructor(name) {
    this.name = name;
  }

	const timeout = setTimeout(function () {
	    console.log(this === timeout); // true
	});
}
```

Ici, le contexte d’exécution de la fonction dans un callback (ici `setTimeout`) amène le `this` à avoir la valeur de la fonction elle-même. Ce n’est pas ce que l’on souhaite et il existe des méthodes pour l’éviter. La première consiste à ajouter à la fin de la fonction un `.bind(this)` correspondant au bon contexte d’exécution.

```javascript
const timeout = setTimeout(function () {
	    console.log(this === timeout); // true
	}.bind(this));
```

### Bonne pratique : les fonctions fléchées !

On lit qu’à partir de ES6, nous pouvons utiliser des fonctions fléchées pour préserver le contexte d'exécution sans avoir à recourir à `.bind(this)`. Dans l'exemple précédent, cela donnerait :

```javascript
const timeout = setTimeout(() => {
  console.log(this === timeout); // false
});

```

En effet, `this` fait référence au contexte dans lequel la fonction fléchée a été définie, et non à l'objet `timeout`. C'est une manière plus concise et souvent plus claire de gérer le contexte `this` dans les fonctions de rappel.

Pour résumer, il existe de nombreuses manières de définir des fonctions en Javascript mais la fonction fléchée nous sera très utile pour éviter les ambigüités liées au contexte d’exécution.

## TypeScript

Une petite mise au point s’impose à quiconque veut passer de JavaScript à TypeScript. On peut résumer rapidement l’essentiel, mais rien ne vaut la lecture de la documentation associée.

Parmi les point à retenir :

- Importance de déclarer ces variables dans une classe avant de les appeler avec `this.variable`
- Par défaut, visibilité publique des propriétés dans la classe
- Importance du typing des variables (par défaut, type `any`) dans la déclaration ET dans les paramètres des fonctions
- Types courants : `boolean`, `number`, `string`, array (`string[]`, `number[]`, …) et pas avec des majuscules qui correspondent aux types primitifs
- Paramètres optionnels dans les fonctions doivent être indiqués par un `?` pour que le code compile, ou en spécifiant une valeur par défaut
- Il existe des interfaces comme en Java pour spécifier la signature (le contrat) que doit remplir une classe (ou une fonction !)
- L’inférence permet à TypeScript de déterminer à l’avance les types de sortie des fonctions à la compilation (et de les traduire en erreur, le cas échéant)

> “Toute la puissance de TypeScript repose sur cet art de typer le moins possible mais au bon endroit pour en profiter au maximum.” [[1]](https://guide-angular.wishtack.io/typescript/inference)
> 
- Par exemple, les fonctions de callback sont importantes à typer puisque le type de retour est déterminé après un certain temps dans les fonctions asynchrones. Après, l’IDE peut autocompléter et c’est chouette.
- Certains décorateurs permettent d’étendre des fonctions TypeScript [[5]](#bibliographie)

## Angular

Une application Angular = Une arborescence de composants hiérarchisée. Au sommet de cette hiérarchie, le composant “root component”.

En particulier, on peut citer différentes fonctionnalités à maitriser pour s’intégrer à un pipeline de développement professionnel :

- Les composants et la logique MVC
- Les services
- L’injection de dépendance [[6]](#bibliographie)
- Les directives
- Les pipes

J’invite vivement les lecteurs à poursuivre la lecture de la partie Angular de la référence [[1]](#bibliographie), très instructive sur la structure des projets Angular et des points mentionnés ici.

### Conclusion

Angular est un framework puissant pour le développement d'applications web. Grâce à ses fonctionnalités telles que les composants, les services, les directives et les pipes, Angular permet de créer des applications modulaires, réutilisables et maintenables. L'apprentissage d'Angular nécessite une compréhension approfondie de ces concepts, ainsi qu'une bonne maîtrise de JavaScript et de TypeScript. Cependant, une fois ces compétences acquises, Angular offre un environnement de développement robuste et flexible pour créer des applications web dynamiques.


## Regard critique et ouverture

À partir de ce que j'ai appris, je peux dire qu'Angular est un outil puissant avec un ensemble de fonctionnalités robustes. Cependant, son adoption nécessite un investissement significatif en temps d'apprentissage et de maîtrise. Il est essentiel de comprendre les nuances de TypeScript et les spécificités d'Angular, comme l'injection de dépendances et le cycle de vie des composants.

Je ne pense pas maitriser tous ces concepts à l’issue de ces dix heures d’autoformation, c’est pourquoi je continuerai à me documenter sur le framework Angular qui sera utile pour les contextes professionnels évoqués en introduction.

## Ce que j’ai appris durant ce MON

Cependant, ce MON a permis une révision des concepts basiques de JavaScript que je pensais maîtriser, notamment parce que j'ai beaucoup pratiqué le framework React récemment. En revisitant ces bases, j'ai pris conscience de certaines pratiques risquées qui pourraient se glisser dans mes projets.

En particulier, le traitement asynchrone des données était un point bloquant de plusieurs de mes projets et ce MON a offert un recul plus important sur ce point, entre autre.

Pour résumer, j’ai désormais une meilleure maitrise des concepts clés de JavaScript et je suis convaincu de l'importance de comprendre en profondeur le fonctionnement des frameworks que j'utilise. Enfin, j'ai vu une approche de TypeScript et de son utilisation en conjonction avec Angular et je mesure l’intérêt de ces derniers dans les cas d’usages trouvés dans les différentes lectures.

## Bibliographie { #bibliographie }

[1] Le guide de Angular par Marmicode :
[https://guide-angular.wishtack.io](https://guide-angular.wishtack.io/)

[2] Javascript ES6
https://www.w3schools.com/Js/js_es6.asp

[3] Différence var let const
https://www.freecodecamp.org/news/var-let-and-const-whats-the-difference/

[4] Documentation TypeScript
[https://www.typescriptlang.org](https://www.typescriptlang.org/)

[5] Decorators
https://www.typescriptlang.org/docs/handbook/decorators.html

[6] Guide for Dependency Injection
https://blog.angular-university.io/angular-dependency-injection/

[7] Angular official style guide
https://angular.io/guide/styleguide
