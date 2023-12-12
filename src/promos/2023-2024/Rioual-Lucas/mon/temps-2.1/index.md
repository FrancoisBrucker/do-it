---
layout: layout/mon.njk

title: "React.js et Tailwind CSS"
authors:
  - Lucas Rioual

date: 1970-09-01

tags: 
  - "temps 2"

résumé: "React.js"
---

Ce MON a pour objectif de me rendre plus à l’aise avec le développement frontend. J’ai donc décidé d’apprendre React.js et Tailwind CSS.

{% prerequis %}
**Notions abordées** : React.js, Tailwind CSS
**Niveau** : Intermédiaire
{% endprerequis %}



## Introduction

**React.js** est un Framework Javascript qui permet de développer des interfaces utilisateurs.
Ce Framework propose une architecture différente du HTML/CSS/Javascript utilisé dans la conception de site internet traditionnel. Développer une interface réactive et dynamique peut s’avérer compliquer en HTML/CSS/Javascript. **React** facilite la création de ce genre d’interface grâce à des mécanismes que nous verrons plus tard. 
Il existe d’autres Framework Javascript qui permettent plus ou moins la même chose comme **Vue.js** ou **Angular**.
J’ai choisi d’étudier React.js car il j’avais déjà quelques bases en **React Native** qui utilise à peu près les mêmes notions.

Je me suis fixer comme objectif de refaire le site web que j’ai crée pendant le POK 1 avec **React**. 


Malheureusement, j’ai récemment perdu toutes les données de mon disque dur externe (y compris le code que j’ai fait durant ce MON). Je sais, cela ressemble à une excuse bidon, mais c’est malheureusement vrai. Je vais quand même expliquer tout mon processus d’apprentissage et certaines notions importante de **React** que j’ai découvert.


## Commencer avec React

Pour l’apprentissage de React, j’ai utilisé la documentation de React et Chat GPT.

Pour commencer, je vous conseille vraiment de lire la [documentation](https://react.dev/learn/).
Attention, il faut aller l'ancienne documentation est obsolète et plus valable.

Je trouve cette documentation très claire et efficace. Il y a un tutoriel pour faire un morpion. C'est un bon exercice pour comprendre les notions fondamentales de React : 

- **Les Components**
- **Les props**
- **Le state**

### Les components

Les components sont essentiels dans le fonctionnement de React. Ce sont des éléments réutilisables qui encapsulent du code et les fonctionnalités. Un component peut être aussi simple qu'un bouton ou aussi complexe qu'une section entière. 

Voici un exemple d’un component représentant le header d’un site web (généré par Chat GPT) :

```jsx
// Header.js
import React from 'react';

const Header = () => {
  return (
    <header>
      <h1>Mon App</h1>
      <nav>
        <ul>
          <li>Accueil</li>
          <li>À propos</li>
          <li>Contact</li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;
```

On peut maintenant utiliser ce component n’importe où dans le projet :

```jsx
import React from 'react';
import Header from './Header';

const App = () => {
  return (
    <div>
      <Header />
      <main>
        {/* Contenu principal de l'application */}
      </main>
    </div>
  );
};

export default App;
```

### Les props

Les composants peuvent accepter des propriétés (props) pour paramétrer leur comportement. Les props sont des passées de parent à enfant. Par exemple, nous pouvons rendre le titre de notre header dynamique en utilisant une prop : 

```jsx
const Header = (props) => {
  return (
    <header>
      <h1>{props.titre}</h1>
      <nav>
        <ul>
          <li>Accueil</li>
          <li>À propos</li>
          <li>Contact</li>
        </ul>
      </nav>
    </header>
  );
};
```

```jsx
const App = () => {
  const titreHeader = "Mon App";
  return (
    <div>
      <Header titre={titreHeader} />
			<main>
        {/* Contenu principal de l'application */}
      </main>
    </div>
  );
};
```

 

### Le state

En plus des props, React propose le concept d'état (state) pour gérer les données qui changent au fil du temps à l'intérieur d'un composant. Pour illustrer cette notion, nous pouvons ajouter un bouton qui incrémente un compteur :

```jsx
const App = () => {
  const titreHeader = "Mon App";

	const [count, setCount] = useState(0);

  const incrementer = () => {
    setCount(count + 1);
  };

	
  return (
    <div>
      <Header titre={titreHeader} />
			<main>
        <p>Compteur : {count}</p>
	      <button onClick={incrementer}>Incrémenter</button>
      </main>
    </div>
  );
};
```

La fonction **`useState`** permet de déclarer et d'initialiser le state **`count`**

**`setCount`** est une fonction qui permet de modifier la valeur de cette variable d'état.

## Tailwind CSS

