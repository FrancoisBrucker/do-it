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
2. Variables Globales/Locales
3. Objets
4. Fonctions anonymes

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

Ainsi si on crée un bankAccount on peut lui appliquer la méthode 