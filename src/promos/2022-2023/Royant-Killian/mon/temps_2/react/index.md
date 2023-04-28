---
layout: layout/mon.njk

title: "[MON] Débutez avec React"
authors:
  - Killian ROYANT
date: 2023-01-25

tags:
  - 'temps 2'
  - DevWeb
  - FrontEnd
  - React
  - JavaScript
---

<!-- début résumé -->

Présentation du deuxième MON de mon temps 2 : une introduction au développement FrontEnd avec React basée sur une formation proposée par Openclassrooms.

<!-- fin résumé -->

[<-- Retour](../)

{% prerequis "**Prérequis**" %}

Pour réussir à suivre ce cours, vous devez avoir une certaine connaissance de HTML, CSS et JavaScript (ES2015+), npm, les commandes de base du terminal, et Git. Vous pouvez acquérir ces connaissances de JavaScript en suivant cette formation proposée par Openclassrooms :

- [Écrivez du JavaScript pour le Web](https://openclassrooms.com/fr/courses/5543061-ecrivez-du-javascript-pour-le-web)

Vous pouvez jetter un œil à des MON précédents pour vous aider à vous familiariser avec ces notions :

- [Louise GARCOIN - Web Front 1](../../../LG/MON2/)
- [Savinien LAEUFFFER - Web Front 1](../../../SL/webfront/web-front-1/)
- [Gabriel BARBE - Dev Web 2](../../../GB/Mons/Devweb2/)
- [Killian ROYANT - Créez des pages web dynamiques avec JavaScript](../js/)

Outils nécessaires :

- Un IDE, tel que VSCode
- npm
- GitHub

{% endprerequis %}

## Introduction

En parcourant les offres de stage proposées dans le domaine du développement, je me suis rapidement rendu compte de la **demande des employeurs** vis à vis des **frameworks de développement** (React, Vue, Angular...). Ayant déjà abordé React en cours très rapidement, j'ai décidé de suivre une formation proposée par [Openclassrooms](https://openclassrooms.com/fr) afin de solidifier mes bases sur le sujet.

![Débutez avec React](https://i.vimeocdn.com/video/1043590546-d1dea1f9d9290343e0214d2f7495428c8db29ca375a135c7957a1d95b63afb9d-d_640)

Le lien de la formation est disponible : [Débutez avec React (Openclassrooms)](https://openclassrooms.com/fr/courses/7008001-debutez-avec-react)

Cette formation est composée de **4 parties** qui mettent en place un **projet concret** de développement d'une interface FrontEnd. Chacune de ces parties est composé de **plusieurs leçons** et d'un **quiz**. Dans ces leçons, vous retrouverez du **cours** écrit, les lignes de **code** qui permettent de créer l'interface web ainsi que des **vidéos** qui expliquent pas à pas comment y arriver.

![Le site La maison jungle découpé en composants](https://user.oc-static.com/upload/2021/01/18/16109867335116_P1C3-2.png)

{% info "**Objectifs**" %}

À la fin de ce cours, vous serez capable de :

- comprendre le fonctionnement de React ;
- créer une application React complète avec Create React App ;
- stocker et récupérer des données avec le state et les effets.

{% endinfo %}

### Table des matières

Vous trouverez ci-dessous la table des matières de la formation :

{% prerequis %}

#### Partie 1 - Initiez-vous aux principes de React

Cette partie vous permettra de **comprendre les bases** de React en vous familiarisant avec sa logique et en écrivant du code modulaire avec les composants en JSX.

--

1. Tirez le maximum de ce cours
2. Appréhendez la logique de React
3. Écrivez du code modulaire avec les composants en JSX

--

#### Partie 2 - Créez votre première application complète avec Create React App

Cette partie vous permettra de **créer votre première application** en utilisant Create React App. Vous apprendrez à incorporer du style et des assets à votre projet, à utiliser les listes et les conditions pour gagner en temps et en efficacité, et à réutiliser vos composants avec les props.

--

1. Prenez en main Create React App
2. Incorporez du style et des assets à votre projet
3. Gagnez en temps et en efficacité grâce aux listes et aux conditions
4. Réutilisez vos composants avec les props
5. Interagissez avec vos composants grâce aux événements

--

#### Partie 3 - Stockez et récupérez des données avec le state et les effets

Cette partie vous permettra de **stocker et récupérer des données** en utilisant le state et les effets de React. Vous apprendrez à mettre en place votre state local avec useState, à partager votre state entre différents composants, et à déclencher des effets avec useEffect.

--

1. Mettez en place votre state local avec useState
2. Partagez votre state entre différents composants
3. Déclenchez des effets avec useEffect

--

#### Partie 4 - Conclusion

1. Revenez sur vos acquis

{% endprerequis %}

Bonne formation !

## Pour commencer

Si vous ne souhaitez pas suivre la formation, voici **quelques pistes pour vous aider à commencer** à développer en React.

### Créer un projet React avec Create React App

Pour créer un projet React, vous pouvez utiliser [Create React App](https://create-react-app.dev/). C'est un outil qui permet de créer un projet React en quelques secondes. Pour l'utiliser, vous devez installer Node.js et npm, puis lancer la commande suivante :

```bash
npx create-react-app nom-du-projet
```

{% info "**C'est quoi npx ?**" %}
npx est un outil qui permet d'exécuter des commandes npm sans avoir à installer le package.
{% endinfo %}

### Lancer un projet React

Pour lancer un projet React, vous devez vous rendre dans le dossier du projet et lancer la commande suivante :

```bash
yarn start
```

### Créer un composant React

Un composant React est un élément de l'interface qui peut être réutilisé. On peut par exemple créer un composant `Header` qui contient le titre et le logo de notre site, et l'utiliser sur toutes les pages de notre site.

Pour créer un composant React, vous devez créer un fichier `.js` ou `.jsx` dans le dossier `src/components` et y écrire le code suivant :

```jsx
import React from 'react';

const NomDuComposant = () => {
  return (
    <div>
      <h1>Titre</h1>
      <p>Paragraphe</p>
    </div>
  );
};

export default NomDuComposant;
```

{% info " **Explication de la syntaxe des composants React**" %}
Pour créer un composant React, j'ai utilisé une fonction fléchée. Vous pouvez également utiliser une fonction classique, mais je vous conseille d'utiliser les fonctions fléchées car elles sont plus courtes et plus lisibles.

La fonction fléchée `NomDuComposant` retourne un élément JSX. Cet élément JSX est un composant React qui contient un titre et un paragraphe.

Pour finir, j'ai exporté le composant `NomDuComposant` pour pouvoir l'utiliser dans d'autres fichiers.
{% endinfo %}

{% info "**C'est quoi JSX ?**" %}
JSX est une extension de JavaScript qui permet d'écrire du code HTML dans un fichier JavaScript. C'est une syntaxe qui permet de rendre le code plus lisible.

Pour plus d'informations, vous pouvez consulter la [documentation officielle](https://fr.reactjs.org/docs/introducing-jsx.html).

Il est important de noter que Create React App utilise un compilateur tel que Babel pour convertir le code JSX en JavaScript standard avant de l'exécuter dans un navigateur, donc il est transparent pour vous de utiliser JS ou JSX.
{% endinfo %}

### Utiliser un composant React

Pour utiliser un composant React, vous devez l'importer dans le fichier où vous souhaitez l'utiliser et l'insérer dans le code JSX du fichier. Par exemple, si vous souhaitez utiliser le composant `NomDuComposant` dans le fichier `App.js`, vous devez écrire le code suivant:

```jsx
import React from 'react';

import NomDuComposant from './NomDuComposant';

const App = () => {
  return (
    <div>
      <h1>Titre</h1>
      <p>Paragraphe</p>
      <NomDuComposant />
    </div>
  );
};

export default App;
```

Vous pourrez ensuite lancer l'application avec la commande `yarn start` et voir le composant s'afficher.

{% info "**C'est quoi le fichier App.js ?**" %}
Le fichier `App.js` est le fichier principal de votre application. Il est utilisé pour afficher le composant principal de votre application. Il est possible de créer plusieurs composants principaux et de les afficher dans le fichier `App.js` en fonction de la page sur laquelle l'utilisateur se trouve.
{% endinfo %}

### Utiliser le state

Le state est un objet qui contient des données. Il est utilisé pour stocker des données et les mettre à jour. Le state est préférable à la variable car il permet de mettre à jour le composant à chaque fois que le state est modifié.

Pour utiliser le state, vous devez importer `useState` depuis la bibliothèque `react` et utiliser la fonction `useState` dans votre composant :

```jsx
import React, { useState } from 'react';

const App = () => {
  const [state, setState] = useState('valeur initiale');

  return (
    <div>
      <h1>Titre</h1>
      <p>Paragraphe</p>
      <p>{state}</p>
    </div>
  );
};

export default App;
```

### Utiliser les effets

Les effets sont des fonctions qui sont exécutées à chaque fois que le composant est mis à jour. Elles sont utiles pour récupérer des données, mettre à jour le DOM, etc.

Pour utiliser les effets, vous devez importer `useEffect` depuis la bibliothèque `react` et utiliser la fonction `useEffect` dans votre composant :

```jsx
import React, { useEffect } from 'react';

const App = () => {
  useEffect(() => {
    console.log('Ceci est un effet');
  }, []);

  return (
    <div>
      <h1>Titre</h1>
      <p>Paragraphe</p>
    </div>
  );
};

export default App;
```

### Utiliser les props

Les props sont des données que vous pouvez passer à un composant React. Elles sont utiles pour réutiliser un composant avec des données différentes. 

Pour utiliser les props, vous devez passer des données à votre composant :

```jsx
import React from 'react';

import NomDuComposant from './NomDuComposant';

const App = () => {
  return (
    <div>
      <h1>Titre</h1>
      <p>Paragraphe</p>
      <NomDuComposant nom="John Doe" />
    </div>
  );
};

export default App;
```

Et vous devez récupérer ces données dans votre composant :

```jsx
import React from 'react';

const NomDuComposant = (props) => {
  return (
    <div>
      <h1>Titre</h1>
      <p>Paragraphe</p>
      <p>{props.nom}</p>
    </div>
  );
};

export default NomDuComposant;
```

### Compiler un projet React

Afin de pouvoir déployer votre projet React, vous devez le compiler.

Pour compiler un projet React, vous devez vous rendre dans le dossier du projet et lancer la commande suivante :

```bash
yarn build
```

Vous pouvez ensuite déployer le dossier `build` sur votre serveur.

[<-- Retour](../)
