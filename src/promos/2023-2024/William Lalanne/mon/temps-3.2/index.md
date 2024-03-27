---
layout: layout/mon.njk

title: "Bases de développement mobile"
authors:
  - William Lalanne

date: 2023-09-27

tags: 
  - "temps 3"

résumé: "Dans ce MON je souhaite apprendre les bases de TypeScript"
---

{%prerequis%}

Pré-requis :
**Niveau :** Moyen
**Prérequis :** Pour ce MON, il est nécessaire d'avoir certaines bases de JavaScript pour comprendre les concepts avec plus de facilité mais il est possible de s'en passer. 

{%endprerequis%}

## Liens utiles 

[Site TypeScript](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html)
[Autre site très bien](https://kinsta.com/fr/base-de-connaissances/guide-complet-typescript/)

## Sommaire 
1. TypeScript, qu'est-ce que c'est 
2. Pourquoi ce MON
4. Lancer un projet TypeScript
5. Les types en TypeScript
6. Les fonctions et les classes
7. TypeScript dans le développement web
8. Conclusion


## TypeScript, qu'est-ce que c'est 

TypeScript est un langage de programmation développé par Microsoft, qui s'appuie sur JavaScript. La différence entre les deux est que TypeScript est un langage typé, il prend les fonctionnalités de bases de JS et en ajoute des nouvelles dans lesquels le type des variables, des fonctions doit être précisé. Cela apporte une meilleure stabilité et sécurité au code et permet de limiter grandement les erreurs ou en tout cas de les détecter plus tôt. 


## Pourquoi ce MON

J'ai voulu en apprendre plus sur TypeScript pour plusieurs raisons. D'abord car ce langage est en plein essort, de nombreuses entreprises l'utilisent et c'est le cas de celle dans laquelle je vais effectuer mon stage. C'est donc aussi pour ça que je souhaite connaître ce langage. 


## Lancer un projet TypeScript

Pour lancer un projet TypeScript, rien de très compliqué. Il faut ouvrir un nouvel onglet sur VSCode avec un terminal et taper les commandes suivantes : 

```shell
npm install -D typescript
``` 

Cette commande permet d'installer le compilateur. 

Ensuite on crée un projet node avec la commande : 
```shell
npm init -y
```
```shell
npx tsc .ts
```

## Les types en TypeScript
L'un des points forts de TypeScript est son système de typage statique. Cela signifie qu'on peut spécifier le type de chaque variable ou de chaque paramètre de fonction et même le type de retour des fonctions. Le code sera alors bien plus clair et plus prévisible, et cela évite les erreurs de typage comme il en arrive souvent. 
Voici un exemple de code TypeScript avec des types pour se rendre mieux compte de comment cela fonctionne :

```js
// Déclaration d'une variable avec son type
let message: string;
message = "Hello, TypeScript!";

// Déclaration d'une fonction avec des types pour les paramètres et le retour
function add(a: number, b: number): number {
    return a + b;
}

// Utilisation de la fonction
const result = add(10, 20);
console.log(result);
```

On voit ici que la variable message est un String, ou ne pourra donc pas lui attribuer la valeur d'un nombre par exemple. 
Ensuite la fonction possède deux paramètres, des nombres et le retour doit lui aussi être un nombre. 


## Les fonctions et les classes
En TypeScript, on peut créer des classes comme en JavaScript, la seule différence étant que l'on doit préciser le type des propriétés que l'on utilise. 

Voici comment on écrirait une classe en JavaScript : 
```js
class Person {
    // Constructeur pour initialiser les propriétés
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    // Méthode de la classe
    greet() {
        return `Hello, my name is ${this.name} and I am ${this.age} years old.`;
    }
}
```

Et voici comment on l'écrirait en TypeScript : 

```js
class Person {
    // Propriétés de la classe avec des types
    name: string;
    age: number;

    // Constructeur pour initialiser les propriétés
    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }

    // Méthode de la classe
    greet(): string {
        return `Hello, my name is ${this.name} and I am ${this.age} years old.`;
    }
}
```


## Conclusion 
Grâce à ce MON j'ai pu découvir sommairement ce qu'était TypeScript. Malheuresement en seulement 10h je n'ai pas pu manipuler assez pour vraiment m'habituer à l'utiliser, mais je vais gagner du temps d'apprentissage quand je serai en stage car je saurai à quoi m'attendre. 


## Horodatage
Lecture des différentes informations sur TypeScript: 4h
Ecriture du code et mise en place d'un projet TS : 4h
