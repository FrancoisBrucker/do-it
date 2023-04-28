---
layout: layout/mon.njk

title: "MON 1 : React"
authors:
 - Thomas Pont

date: 2022-10-07

tags:
  - 'temps 1'
  - 'react'
---

<!-- Début Résumé -->

React : un framework front-end
<!-- Début Résumé -->

## Objectif de ce MON

Dans ce MON, l'objectif sera de découvrir React et d'en voir les principales fonctionnalités.


## Qu'est-ce que React ?

React est un framework front-end. C’est donc un ensemble de classes, fonctions et utilitaires qui facilite la création de la partie visuelle d’un site Internet. Il existe d'autres frameworks tels que Vue ou Angular.

Le principal objectif de React est de créer des sites Web à partir de composants. Un composant est un ensemble de HTML, CSS et JavaScript. Tous les composants pourront ensuite interagir ensemble afin de donner le site que l’on souhaite.

## Fonctionnement de React

Dans la suite, nous illustrerons le fonctionnement de React avec la réalisation du front d’un site de messagerie.

### Création d'un projet

Tout d’abord, pour créer un projet en React il faut ouvrir un terminal, se placer dans le dossier que l’on souhaite et entrer la commande suivante:

**npx create-react-app la-boite-aux-lettres**

Un projet avec des dossiers et des fichiers de code va alors se créer.


### Les composants

Comme expliqué précédemment, la logique de React est basée sur les composants. Chaque partie du site que l’on souhaite avoir sera défini par un composant. Par exemple, un site peut avoir un header, un footer,...

Pour créer et organiser nos composants, on peut créer un dossier les regroupant tous. Chaque composant sera ensuite créé à l’aide d’un fichier en .js.

Par exemple le fichier Banner.js suivant :

```javascript
function Banner() {
    return <h1>La boîte aux lettres</h1>
}

export default Banner
```

créera un composant Banner qui pourra être mis sur notre site.
Dans ce fichier en .js, on peut ajouter tous les éléments que l’on souhaite avec les balises de HTML (\<h1> pour un titre, \<ul> pour une liste, \<p> pour un paragraphe, \<img> pour une image,...).

On peut également associer un fichier CSS pour donner du style au texte ou aux éléments présents sur un composant.

Mais comment afficher notre site ensuite ?
Pour cela, à la création de notre projet, un fichier App.js a été créé. On peut lui ajouter les composants que l’on a créés.

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

On peut progressivement ajouter des composants et du style pour que notre site ressemble à ce que l’on souhaite. Ainsi, on ajoute des composants pour les utilisateurs, la liste des utilisateurs, les messages et la liste des messages.
On crée également un composant main qui regroupe la liste des utilisateurs et la liste des messages.

### Contextualiser ces composants

On a vu que React permet de créer des composants. Mais, il permet également de les contextualiser. En effet, lors de la définition d’un composant, on peut ajouter du javascript afin de savoir comment afficher un élément.

Par exemple, ou peut mettre en avant nos meilleurs amis en affichant une flamme à côté de leur nom.
La liste des utilisateurs est située dans datas/allUsers.txt. Pour chaque personne on peut lui attribuer un booléen isBestFriend qui indique si oui ou non on est meilleur ami avec lui.

Le script suivant affichera cela:

```javascript
import { userList } from '../datas/allUser'

function UserItem() {
    return (
        <ul>
            {userList.map((name, isBestFriend) => (
            <li>
                {name}
                {isBestFriend && <span>🔥</span>}
            </li>
            ))}
        </ul>
    )
}

export default UserItem

```


### Les interactions

On a ainsi vu jusque là que l'on pouvait créer et afficher des composants et qu’on pouvait les contextualiser. Cependant, pour le moment, notre site reste statique et ne prend pas en compte les interactions que l’utilisateur pouvait avoir avec les composants.

On souhaite pouvoir voir les messages qu'on a eu avec une personne si l'on clique sur son nom.

Pour cela on utilise les liens de parenté entre les composants. L'utilisateur va cliquer sur un UserItem. L'information va remonter à son parent Main puis redescendre jusqu'à MessageList et c'est la liste de message avec le bon utilisateur qui va s'afficher.
Pour cela on utilise la fonction useState.

```javascript
import UserList from './UserList'
import MessageList from './MessageList'
import BarreMessage from './BarreMessage'
import { allMessage } from '../datas/allMessage'
import '../styles/Main.css'
import { useState } from 'react'


function Main(){

    const [conversationwith, setconversation]=useState('Alice')


    return (

        <div>
            <div className='ecran-principal'>
                <UserList changeConversation={setconversation}/>
                <MessageList list={allMessage[conversationwith]}/>
            </div>
            <div className='barre-message'>
                <BarreMessage/>
            </div>
        </div>
    )
}

export default Main
```

La ligne **const [conversationwith, setconversation]=useState('Alice')** permet de créer une zone de stockage pour savoir ce que l'on affiche et pouvoir le modifier. La fonction useState permettra de modifier les informations de la page si l'utilisateur clique sur une autre personne.
La ligne **UserList changeConversation={setconversation}** permet de récupérer l'information de UserList de quel utilisateur a été sélectionné. La ligne **MessageList list={allMessage[conversationwith]}** permet elle de modifier ce qui va s'afficher.


## Ressources utilisées

Pour effectuer ce MON, j'ai suivi le tutoriel d'OpenClassroom sur React : https://openclassrooms.com/fr/courses/7008001-debutez-avec-react.
Par ailleurs, pour avoir plus d'informations sur certains points précis, j'ai également lu de la documentation sur le site de React : https://fr.reactjs.org/docs/getting-started.html.
