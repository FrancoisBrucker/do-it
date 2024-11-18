---
layout: layout/mon.njk

title: "Les Design Patterns pour les Sites Internet"
authors:
  - "Sofiane Ouadda"
date: 2024-10-20

tags: 
  - "Développement Web"
  - "Design Patterns"
  - "Refactoring"
  - "JavaScript"
  - "Node.js"

résumé: "Ce cours explore les principaux design patterns utilisés dans le développement de sites internet. À travers des exemples pratiques en JavaScript et Node.js, vous apprendrez comment améliorer la maintenabilité, la scalabilité et la lisibilité de votre code."

---

{% prerequis %}

Bases en JavaScript et Node.js. Une connaissance des concepts fondamentaux de la programmation orientée objet est recommandée.

{% endprerequis %}

{% lien %}

- [Refactoring Guru - Design Patterns](https://refactoring.guru/design-patterns)
- [MDN - JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [YouTube - Traversy Media: JavaScript Design Patterns](https://www.youtube.com/watch?v=kuirGzhB1U4)
- [Patterns.dev](https://patterns.dev/)

{% endlien %}

---

## Objectifs

À la fin de ce cours, vous serez capable de :
1. Comprendre l’importance des design patterns dans le développement de sites internet.
2. Identifier et implémenter les patterns les plus courants : Singleton, Factory, Observer, etc.
3. Appliquer ces patterns en JavaScript et Node.js.
4. Reconnaître les situations où chaque pattern est le plus adapté.

---

## 1. Introduction aux Design Patterns

Les **design patterns** sont des solutions génériques à des problèmes récurrents dans le développement logiciel. Ils ne sont pas des morceaux de code prêt à l'emploi, mais des "templates" qui peuvent être adaptés à des situations spécifiques.

### Pourquoi utiliser des Design Patterns ?

- **Réduction de la complexité** : Structurent le code pour le rendre plus compréhensible.
- **Réutilisabilité** : Encouragent la création de composants modulaires.
- **Collaboration facilitée** : Fournissent un langage commun pour les développeurs.
- **Anticipation des évolutions** : Préparent le code à être étendu ou modifié facilement.

---

## 2. Le Singleton Pattern

### Description

Le **Singleton** garantit qu'une classe n'a qu'une seule instance tout en fournissant un point d'accès global à cette instance.

### Quand l'utiliser ?

- Pour gérer une connexion unique (ex. : base de données).
- Pour centraliser une configuration partagée.

### Exemple en Node.js : Gestion d’une connexion MongoDB

  ```
  class Database {
    constructor() {
      if (Database.instance) {
        return Database.instance;
      }
      this.connection = this.connect();
      Database.instance = this;
    }

    connect() {
      console.log('Connexion à la base de données...');
      return {}; // Simuler une connexion.
    }

    getConnection() {
      return this.connection;
    }
  }

  // Utilisation
  const db1 = new Database();
  const db2 = new Database();

  console.log(db1 === db2); // true
  ```

## 3. Le Factory Pattern

### Description

Le Factory Pattern permet de créer des objets sans spécifier leur classe exacte. Il délègue la logique d'instanciation à une "fabrique".

### Quand l'utiliser ?
   
- Pour éviter d'exposer la logique complexe de création.
- Pour instancier différents types d'objets en fonction des paramètres.

### Exemple : Création d'utilisateurs avec rôles

```
class User {
  constructor(name) {
    this.name = name;
    this.role = 'User';
  }
}

class Admin {
  constructor(name) {
    this.name = name;
    this.role = 'Admin';
  }
}

class UserFactory {
  static createUser(name, type) {
    if (type === 'admin') {
      return new Admin(name);
    }
    return new User(name);
  }
}

// Utilisation
const user1 = UserFactory.createUser('Sofiane', 'user');
const admin1 = UserFactory.createUser('Soso', 'admin');

console.log(user1); // { name: 'Sofiane', role: 'User' }
console.log(admin1); // { name: 'Soso', role: 'Admin' }
```
## 4. L'Observer Pattern

### Description

L’Observer Pattern permet à un objet (le sujet) de notifier automatiquement plusieurs autres objets (les observateurs) lorsque son état change.

### Quand l'utiliser ?
   
- Pour mettre en œuvre une communication entre objets sans couplage fort.
- Pour réagir aux événements dans une application (ex. : interfaces utilisateur ou événements système).

### Exemple : Implémentation d'un système de notifications
```
class Subject {
  constructor() {
    this.observers = [];
  }

  attach(observer) {
    this.observers.push(observer);
  }

  detach(observer) {
    this.observers = this.observers.filter(obs => obs !== observer);
  }

  notify(data) {
    this.observers.forEach(observer => observer.update(data));
  }
}

class Observer {
  constructor(name) {
    this.name = name;
  }

  update(data) {
    console.log(`${this.name} a reçu les données :`, data);
  }
}

// Utilisation
const subject = new Subject();

const observer1 = new Observer('Observer 1');
const observer2 = new Observer('Observer 2');

subject.attach(observer1);
subject.attach(observer2);

subject.notify({ message: 'Hello, Observers!' });

subject.detach(observer1);

subject.notify({ message: 'Second notification' });
```


## 5. Le Decoratot Pattern

### Description

Le Decorator Pattern permet d’ajouter dynamiquement des fonctionnalités à un objet sans modifier sa structure originale.

### Quand l'utiliser ?
   
- Pour étendre les fonctionnalités d’un objet existant sans hériter de celui-ci.
- Pour appliquer des fonctionnalités optionnelles sans multiplier les sous-classes.

### Exemple : Ajout de fonctionnalités à une fonction

```
function basicFunctionality() {
  console.log('Fonctionnalité de base');
}

function withExtraFeature(func) {
  return function () {
    func();
    console.log('Fonctionnalité supplémentaire ajoutée');
  };
}

// Utilisation
const enhancedFunctionality = withExtraFeature(basicFunctionality);

basicFunctionality(); // "Fonctionnalité de base"
enhancedFunctionality(); // "Fonctionnalité supplémentaire ajoutée"
```

## Horodateur

| Date       | Heures passées | Indications                                                                  | 
|------------|----------------|------------------------------------------------------------------------------|
| 06/11      | 2H30           | Lecture sur le Singleton et implémentation d’exemples pratiques en Node.js  | 
| 06/11      | 2H30             | Étude approfondie et pratique sur le Factory Pattern                        |
| 09/11      | 1H45             | Apprentissage du Observer Pattern et implémentation d’une maquette          |
| 09/11      | 1H45           | Pratique sur le Decorator Pattern                                            |
| 10/11      | 2H             | Retranscription du cours en markdown                                         |

