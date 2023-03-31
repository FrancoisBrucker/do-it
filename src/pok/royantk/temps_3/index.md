---
layout: layout/post.njk

title: "[POK] E-commerce avec React (temps 3)"
authors:
  - Killian ROYANT
tags:
  - JavaScript
  - React
  - MUI
  - TailwindCSS
---

<!-- début résumé -->

Ce POK présente le développement d’une plateforme simple de e-commerce à l’aide de différentes technologies web (React, MUI, TailwindCSS…)

<!-- fin résumé -->

{% chemin "**Ressources**" %}

- [Le Github du POK](https://github.com/royantk/FindTheKey)
- [[Documentation] React](https://fr.reactjs.org/docs/getting-started.html)
- [[Documentation] React-Redux](https://react-redux.js.org/introduction/getting-started)
- [[Documentation] Material Design UI (MUI)](https://mui.com/material-ui/getting-started/overview/)
- [Documentation] Parcel
- [[MON] Débutez avec React](https://francoisbrucker.github.io/do-it/mon/royantk/temps_2/react/)
- [Chat GPT](https://chat.openai.com/chat)
- [https://parceljs.org/getting-started/webapp/](https://parceljs.org/getting-started/webapp/)
- [https://create-react-app.dev/](https://create-react-app.dev/)
- [https://webpack.js.org/](https://webpack.js.org/)

{% endchemin %}

## Introduction

L’objectif de ce POK est de **concevoir une boutique en ligne simple** utilisant des **technologies de développement web modernes**, notamment React. Pour cela, j’ai décidé de reprendre une maquette Figma que j’ai réalisé à lors de la création d’une formation afin d’avoir une vue claire de l’endroit où amener ce POK.

![Untitled](images/Untitled.png)

{% chemin "**Choix des technologies**" %}

Afin d’identifier les différentes technologies que j’allais pouvoir utiliser, j’ai fais des recherches. J’en ai constitué un **MON** que vous pouvez consulter ici : [[MON] Technologies web](../../../mon/royantk/temps_3/tech_web)

{% endchemin %}

### Organisation et to-do

Afin de réaliser ce POK, j’ai identifié les tâches nécessaires suivantes. Ces tâches sont susceptibles d'évoluer.

#### **~~🌳 Général~~ *(fait)***

- ~~Comprendre le fonctionnement des bibliothèques (React, MUI, TailwindCSS, Parcel)~~
- ~~Mettre en place l’environnement du projet~~

#### **📑 Page catalogue**

- ~~Récupérer une liste de produits depuis un fichier JSON ou une API~~
- ~~Afficher la liste de produits sur la page~~
- ~~Pour chaque produit, afficher son nom, sa description, son prix et une image~~
- ~~Ajouter un bouton "Ajouter au panier" pour chaque produit~~
- Ajouter le header du tableau

#### **📄 Page produit**

- Créer une page pour afficher les détails d'un produit sélectionné
- Afficher le nom, la description, le prix et l'image du produit
- Ajouter un bouton "Ajouter au panier"
- Associer la page produit à la page catalogue

#### **🛒 Panier**

- Créer un composant pour afficher le contenu du panier
- Afficher les produits ajoutés au panier (nom, prix, quantité)
- Afficher le prix total du panier
- Ajouter la possibilité de modifier la quantité de chaque produit dans le panier
- Ajouter la possibilité de supprimer un produit du panier

## Structure de l’application

### Composants nécessaires

J’ai repris ma maquette Figma pour définir les différents composants React nécessaires pour réaliser le prototype, ainsi que leurs designs respectifs. Voici ci-dessous les composants Figma.

![Untitled](images/Untitled%201.png)

## Arborescence des fichiers

Voici l’organisation de mes fichiers sources. J’ai divisé mon application en composants React, appelés dans une application globale App.js. Il n’y a qu’un seul fichier de style car le style des composant est directement écrit en Tailwind dans les fichiers React.

```bash
src/
├── components/
│   ├── AddToCart.js
│   ├── Catalogue.js
│   ├── CatalogueItem.js
│   └── Header.js
├── styles/
│   └── App.css
├── App.js
├── index.html
└── index.js
```

## Le prototype (V1)

Le code ci-dessous représente la version 1 du prototype d'application React développée dans le cadre d'un POK sur la création d'une boutique en ligne. Cette version contient la page du catalogue, qui permet d'afficher les produits disponibles à l'achat. Le code utilise TailwindCSS pour appliquer des styles au composant et des composants Material-UI pour ajouter des fonctionnalités supplémentaires tels que les boutons d'ajout au panier.

![Untitled](images/Untitled%202.png)

### App.js

Chemin : `./App.js`

Le code suivant est un extrait de l'application React développée dans le cadre d'un POK sur la création d'une boutique en ligne. Il s'agit du code de la fonction `App`, qui est le composant principal de l'application. Cette fonction retourne du JSX (JavaScript avec des balises XML), qui permet de décrire l'interface utilisateur de l'application.

```jsx
const products = ['...']  // Contient des produits

export function App() {

  const [cart, setCart] = useState([]);

  const addToCart = (product) => {
    setCart([...cart, product]);
  };

  return (
    <StyledEngineProvider injectFirst>
      <div className="app">
        <div className="app-head">
          <h1>Lorem Ipsum</h1>
          <p>Lorem Ipsum Dolor Sit Amet</p>
        </div>
        <Catalogue products={products} addToCart={addToCart} />
      </div>
    </StyledEngineProvider>

  );
}
```

Dans ce code, la fonction `useState` est utilisée pour stocker les produits ajoutés au panier par l'utilisateur. La fonction `addToCart` permet d'ajouter un produit au panier en mettant à jour l'état `cart` avec la fonction `setCart`.

Le JSX retourné par la fonction `App` contient un `StyledEngineProvider`, qui enveloppe un `div` avec une classe `app`. Ce div contient un titre (`h1`) et un paragraphe (`p`) qui ne sont pas pertinents pour la compréhension du code. Enfin, il y a un composant `Catalogue` qui prend deux props (`products` et `addToCart`). Cela signifie que le composant `Catalogue` est appelé avec ces deux props.

Le composant `StyledEngineProvider` est utilisé pour faire fonctionner TailwindCSS avec Material-UI. Concrètement, il permet d'injecter les styles dans l'application et de les rendre compatibles avec les composants Material-UI. Il s'agit donc d'un élément important pour utiliser les deux bibliothèques de manière conjointe dans une application React.

### Catalogue

Chemin : `./components/Catalogue.js`

```jsx
import { CatalogueItem } from './CatalogueItem';

const addToCart = (product) => {
    console.log('Adding to cart:', product);
};

export function Catalogue(props) {
    return (
        <div className="flex flex-col space-y-4">
            {props.products.map((product) => (
                <CatalogueItem product={product} addToCart={addToCart} key={product.id} />
            ))}
        </div>
    );
}
```

Le code représente le composant `Catalogue` de l'application React. Ce composant est appelé dans le composant principal `App`. Le composant `Catalogue` prend une seule prop appelée `products`, qui est un tableau d'objets représentant les produits à afficher. Le composant `Catalogue` utilise la méthode `.map()` pour itérer sur le tableau des produits et afficher chaque produit à l'aide du composant `CatalogueItem`.

Le composant `CatalogueItem` prend deux props, `product` et `addToCart`. Le composant `addToCart` est une fonction qui sera appelée lorsqu'un utilisateur clique sur le bouton "Add to cart" dans le composant `CatalogueItem`.

Le code utilise également TailwindCSS pour appliquer des styles au composant `Catalogue`. Le conteneur principal est un div avec une classe `flex` qui utilise la direction verticale (`flex-col`) et ajoute un espacement vertical (`space-y-4`) entre chaque élément dans le conteneur. Le composant `CatalogueItem` est appelé pour chaque produit et est rendu à l'intérieur du conteneur principal.

### CatalogueItem

Chemin : `./components/CatalogueItem.js`

```jsx
import { AddToCart } from './AddToCart';

export function CatalogueItem(props) {
    return (
        <div className="bg-white rounded-lg flex flex-row items-center space-x-16 pr-12">
            <img className="object-cover h-40 aspect-square" src={props.product.image} alt={props.product.name} />
            <h3 className="my-2 text-lg font-medium max-h-28 w-40 overflow-hidden">{props.product.name}</h3>
            <p className="break-words text-gray-500 max-h-28 w-60 overflow-hidden">{props.product.description}</p>
            <p className="break-words text-gray-500 max-h-28 w-28 overflow-hidden">{props.product.price} €</p>
            <AddToCart product={props.product} addToCart={props.addToCart} />
        </div>
    );
}
```

Le composant `CatalogueItem` est utilisé pour afficher les détails d'un produit dans le catalogue. Il prend deux props: `product` et `addToCart`. La prop `product` est un objet qui contient les informations du produit telles que l'image, le nom, la description et le prix. La prop `addToCart` est une fonction qui sera appelée lorsque l'utilisateur cliquera sur le bouton "Add to cart".

Le code utilise TailwindCSS pour appliquer des styles au composant `CatalogueItem`. Le conteneur principal est un div avec une classe `bg-white` qui ajoute une couleur de fond blanche au composant. Il utilise également la classe `rounded-lg` pour arrondir les coins du composant et `flex` pour afficher les éléments à l'intérieur du conteneur en ligne. `items-center` est utilisé pour aligner les éléments verticalement et `space-x-16` ajoute un espacement horizontal de 16 pixels entre chaque élément.

Le code utilise également l'objet `props.product` pour afficher l'image, le nom, la description et le prix du produit. `props.product.image` est utilisé pour afficher l'image du produit. `props.product.name` est utilisé pour afficher le nom du produit, et `props.product.description` est utilisé pour afficher la description du produit. `props.product.price` est utilisé pour afficher le prix du produit, avec le symbole de l'euro.

Le composant `AddToCart` est également appelé à la fin du composant `CatalogueItem`. Cette fonctionnalité permet à l'utilisateur d'ajouter le produit au panier en cliquant sur le bouton "Add to cart". La prop `product` est passée à `AddToCart` pour que la fonction `addToCart` sache quel produit ajouter au panier.

### AddToCart

Chemin : `./components/AddToCart.js`

```jsx
import Button from '@mui/material/Button';
import Add from '@mui/icons-material/Add';

export function AddToCart(props) {
    return (
        <Button
            startIcon={<Add />}
            variant="contained"
            className='bg-black hover:bg-white hover:text-black text-white font-bold py-2 px-6 rounded-full'
            onClick={() => props.addToCart(props.product)}
        >
            Add to cart
        </Button>
    );
}
```

Le composant `AddToCart` est appelé à partir du composant `CatalogueItem` et contient un bouton "Add to cart" qui permet à l'utilisateur d'ajouter un produit au panier.

Le composant `AddToCart` utilise les composants `Button` et `Add` de la bibliothèque MUI pour créer le bouton, et utilise TailwindCSS pour appliquer des styles supplémentaires au bouton. Le bouton est configuré pour avoir une icône "Add" à gauche du texte "Add to cart", et le texte du bouton est centré.

Lorsque l'utilisateur clique sur le bouton "Add to cart", la fonction `props.addToCart` est appelée avec l'objet `props.product` en tant que paramètre. Cela permet à la fonction `addToCart` de savoir quel produit ajouter au panier.

[<-- Retour](../)
