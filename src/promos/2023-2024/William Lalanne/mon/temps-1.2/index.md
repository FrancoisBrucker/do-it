---
layout: layout/mon.njk

title: "Un peu de JavaScript"
authors:
  - William Lalanne

date: 2023-18-10
tags: 
  - "temps 1"

résumé: "JavaScript"
---

{% prerequis %}
**Niveau :** Facile
**Prérequis :** Bases en JavaScript
{% endprerequis %}

## Sommaire

1. Switch 
2. Objets
3. Fonctions anonymes
4. Classes
5. Pour le développement web

## Switch
En JavaScript, comme dans de nombreux langages de programmation, lorsqu'on a une variable qui prend des valeurs différentes et que pour chacune de ses valeurs on veut afficher un message différent, on peut utiliser un switch. Pour mieux comprendre, prenons un exemple.
Imaginons que j'ai une fonction qui prend un paramètre un prénom et qui renvoie en sortie un chanteur qui possède le même prénom cela donnerait : 
```javascript 
function famousSinger(firstName) {
  let familyName = "";

  if (firstName=="Bob") {
    familyName = "Marley";
  } 
  else if (firstName=="Micheal") {
    familyName = "Jackson";
  }
  else if (firstName=="Kurt") {
    familyName = "Cobain";
  }
  else if (firstName=="Elvis") {
    familyName = "Presley";
  }
  else if (firstName=="Rey") {
    familyName = "Charles";
  }
  else if (firstName=="Freddy") {
    familyName = "Mercury";
  }
  else {
    familyName = "no singer";
  }

  return familyName;
}
```
On voit que si on a de nombreuses conditions, il est très long d'écrire à chaque fois le else if et cela manque de clarté. C'est pourquoi les switch ont été inventés, voilà ce que ça donne : 
```javascript 
function famousSinger(firstName) {
  let familyName = "";
  switch(firstName) {
    case "Bob":
      familyName = "Marley";
      break;
    case "Micheal":
      familyName = "Jackson";
      break;
    case "Kurt":
      familyName = "Cobain";
      break;
    case "Elvis":
      familyName = "Presley";
      break;
    case "Rey":
      familyName = "Charles";
      break;
    case "Freddy":
      familyName = "Mercury";
      break;
    default:
      familyName = "no singer";
      break;
  }
  return familyName;
}
```
On gagne en clarté avec le switch.


## Objets 
Il est possible de créer des objets en JavaScript et d'accéder aux différentes propriétés qui constituent l'objet. Prenons un exemple pour mieux comprendre :
```javascript 
const dog = {
  "name": "Nicolas",
  "legs": 4,
  "tails number": 1,
  "enemies": ["Water", "Cats"]
};
```
Ici, nous avons créé l'objet **cat** qui possède 4 propriétés :
- *name*
- *legs*
- *tails number* 
- *enemies* 

On peut accéder aux propriétés de l'objet et même les modifier, pour cela on peut faire :
```javascript 
const enemiesValue = cat.enemies;
enemiesValue = ["Mouses"];
```
si on connait le nom de la propriété à laquelle on veut accéder. 

Ou alors si le nom de la propriété possède un espace : 
```javascript 
const tailsNumberValue = cat["tails number"];
tailsNumberValue = 2;
```
Il est également possible de supprimer des propriétés, par exemple avec notre objet *dog* :
```javascript 
delete dog.enemies;
delete dog["tails number"];
```

Pour savoir si un objet possède une certaine propriété, la méthode ***.hasOwnProperty(proprietes)*** existe. Si l'object possède la propriété, la fonction retourne true, sinon elle retourne false :

```javascript 
dog.hasOwnProperty("name");
dog.hasOwnProperty("gender");
```

## Fonctions anonymes

Parfois en JavaScript il n'y pas besoin de nommer des fonctions, surtout lorsqu'elles sont utilisés comme argument par d'autres fonctions. On dit alors que c'est une fonction anonymé.
Par exemple au lieu d'écrire ça : 
```javascript 
const myFunc = function() {
  const myVar = "value";
  return myVar;
} 
```
On écrira plutôt : 
```javascript 
const myFunc = () => {
  const myVar = "value";
  return myVar;
}
```

## Les classes

Il est possible de créer des objets plus facilement qu'avec la méthode que nous avons utilisé précedemment, ce qui peut être très pratique quand on crée de nombreux objets. Pour cela on utilise des classes qui agissent en quelques sortes comme des plans pour les objets. 
Par exemple pour créer une classe livre :
```javascript 
class Book {

}
```
Pour cette classe, on voudra que tous les livres aient certaines propriétés comme un titre, un auteur, un nombre de pages. Pour cela on utilise un constructeur :
```javascript 
class Book {
  constructor(title, author, pages) {
    this.title = title;
    this.author = author;
    this.pages = pages;
  }
}
```

Une fois que cela est fait on peut facilement créer des livres :

```javascript 
let harryPotter = new Book("Chamber of secrets", "J.K Rowling", 1200);
```

On peut aussi ajouter après le constructeur des méthodes, ce sont des fonctions qui seront applicables à tous les objets appartenant à la classe dans laquelle la méthode est écrite :
```javascript 
class BankAccount {
    constructor(owner, balance) {
        this.owner = owner;
        this.balance = balance;
    }
    showBalance() {
        console.log('Balance: ' + this.balance + ' EUR');
    }
}
```

Ainsi si on crée un bankAccount on peut lui appliquer la méthode.

## Pour le développement web

JavaScript est très utilisé pour le développement web, notamment pour modifer la strucuture et le style des pages web par l'intermédiraire du DOM (Document Object Model).

Nous allons voir comment intéragir avec le DOM avec JavaScript.

### Trouver des éléments dans la page
Pour trouver les éléments du DOM avec lesquels on souhaite intéragir, il existe de nombreuse méthodes :
- .getElementsByTagName() ---> permet de sélectionner tous les éléments d'une même famille (body, h3, div...). 
- .getElementsByClassName() ---> permet de sélectionner les éléments d'une même classe.
- .getElementById() ---> permet de sélectionner l'élément ayant l'Id demandé.
- .querySelector() ---> un mélange de toutes les autres méthodes, on peut même combiner les sélecteurs (classe, Id, tag).

```javascript 
document.getElementById("myID");
```



### Modifier les éléments
Pour modifier le contenu d'un élément, il y a deux méthodes principales à connaître : 
- innerHTML ---> permet d'avoir accès au contenu de l'élément HTML sélectionné.
- textContent ---> permet d'avoir accès au texte du noeud choisi mais aussi celui de tous ses descendants

```javascript 
var htmlElement = document.getElementById("myID");
htmlElement.innerHTML = ("je remplace l'élément");
```

Après avoir modifier le contenu de l'élément, on peut aussi modifier son style notamment en changeant sa classe : 
- .style.color
- classList.add()
- classList.remove()

```javascript 
var htmlElement = document.getElementById("myID");
htmlElement.innerHTML = ("je remplace l'élément");
htmlElement.style.color=('red');
```

### Ajouter des éléments 
On peut ajouter de nouveaux éléments au DOM grâce à plusieurs méthodes : 

- .createElement()

```javascript 
let newDiv = document.createElement('div');
```

### Les event listeners 

Pouvoir modifier les éléments de la page web par l'intermédiaire du DOM c'est bien, mais comment faire pour que ces modifications se fassent à la suite d'une action d'un utilisateur ? 
C'est là qu'intervienne les event listeners.
Des évènements peuvent avoir lieu sur la page web :
- Des cliques sur des éléments
- Des mouvements de souris 
- Appuis sur le clavier
...
On peut savoir à quel moment ont lieux ces évènements. 
Pour cela on place des event listeners sur les éléments qui avec lesquels l'utilisateur est susceptible d'intéragir. 

Prenons l'exemple d'un bouton, l'utilisateur peut cliquer dessus, cela déclenchera une action. Pour cela :

```javascript 
var button = document.getElementById("button");
button.addEventListener('click', do an action);
```
L'action peut être un changement de page ou une modification, il faut préciser à l'event listener quel action on attend (clique, mouvement de souris...)

### Conclusion 
De nombreuses autres choses peuvent être faites avec JavaScript en web, mais pour l'instant nous nous limiterons à ce que nous avons déjà vu. La suite viendra éventuellement dans un autre MON. 


## Conclusion 
Dans ce MON nous avons vu comment JavaScript pouvait être utilisé comment langage orienté objet, notamment avec les classes. Mais nous avons également vu l'apport de JavaScript d'un point de vue web. 

## Bibliographie 
[OpenClassRoom](https://openclassrooms.com/fr/courses/5493201-write-javascript-for-the-web) : vraiment très bien fait pour l'aspect web, il faut néanmoins quelques connaissances en JavaScript pour se lancer. 

[freeCodeCamp](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/) : pas mal pour revoir les bases.


