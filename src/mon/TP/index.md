---
layout: layout/post.njk

title: "MON 1 : React"
authors:
 - Thomas Pont

tags: ['mon']
---

<!-- Début Résumé -->

React : un framework front-end
<!-- Début Résumé -->

## Objectif de ce MON

Dans ce MON, l'objectif sera de découvrir le React et d'en voir les principales fonctionnalités.


## Qu'est-ce que React ?

React est un framework front-end. C’est donc un ensemble de classes, fonctions et utilitaires qui facilite la création de la partie visuelle d’un site Internet. On peut retrouver au même titre Vue ou Angular.

Le principal objectif de React est de créer des sites Web à partir de composants. Un composant est un ensemble de HTML, CSS et JavaScript. Tous les composants pourront ensuite interagir ensemble afin de donner le site que l’on souhaite.

## Fonctionnement de React

### Création d'un projet

Tout d’abord, pour créer un projet en React il faut ouvrir un terminal, se placer dans le dossier que l’on souhaite et entrer la commande suivante:

**npx create-react-app mon-site-chez-moi**

Un projet avec des dossiers et des fichiers de code va alors se créer.


### Les composants

Comme expliqué précédemment, la logique de React est basée sur les composants. Chaque partie du site que l’on souhaite avoir sera défini par un composant. Par exemple, un site peut avoir un header, un footer,...

Pour créer et organiser nos composants, on peut créer un dossier les regroupant tous. Chaque composant sera ensuite créé à l’aide d’un fichier en .js.

Par exemple le fichier Banner.js suivant :

```javascript
function Banner() {
    return <h1>Mon site chez moi</h1>
}

export default Banner
```

créera un composant Banner qui pourra être mis sur notre site.
Dans ce fichier en .js, on peut ajouter tous les éléments que l’on souhaite avec les balises de HTML (\<h1> pour un titre, \<ul> pour une liste, \<p> pour un paragraphe, \<img> pour une image,...).

On peut associer un fichier en CSS pour donner du style au texte ou aux éléments présents sur un composant.

Mais comment afficher notre site ensuite ?
Pour cela, à la création de notre projet, un fichier App.js a été créé. On peut lui ajouter les composants que l’on a créer.

Ainsi :

```javascript
import Banner from './Banner'

function App() {
    return <Banner />
}

export default App

```

permettra d’avoir un site avec la Banner précédemment défini.

En lançant la commande suivante dans la console, notre site s’affiche sur un serveur local:

**npm start**

On peut progressivement ajouter des composants et du style pour que notre site ressemble à ce que l’on souhaite.


### Contextualiser ces composants

On a vu que React permet de créer des composants mais il permet également de les contextualiser. En effet, lors de la définition d’un composant, on peut ajouter du javascript afin de savoir comment afficher un élément.

Par exemple, si l’on souhaite réaliser un site affichant tous les partants à un marathon et qu’on souhaite afficher une flamme à côté de ceux qui ont déjà gagné un marathon, on peut automatiser cela.
En effet, on peut créer un document avec la liste des participants (Participant.txt) et pour chacun attribut avec leur nom et un avec True si le participant a déjà gagné un marathon et False sinon .

Le script suivant affichera cela:

```javascript
import participant-list from ../Donnees/Participants.txt

function Participant() {
    return (
        <ul>
            {participant-list.map((name) => (
            <li>
                {name}
                {name.winMarathon && <span>🔥</span>}
            </li>
            ))}
        </ul>
    )
}

export default Participant

```


On a vu jusque là qu’on pouvait créer et afficher des composants, qu’on pouvait eux-mêmes contextualiser. Cependant pour le moment, notre site reste statique et ne prend pas en compte les intéractions que l’utilisateur peut avoir avec les composants.

### Les props et les interactions
