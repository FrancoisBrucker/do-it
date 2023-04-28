---
layout: layout/mon.njk

title: "[MON] Créez des pages web dynamiques avec JavaScript"
authors:
  - Killian ROYANT
date: 2022-10-19

tags:
  - 'temps 1'
  - DevWeb
  - JavaScript
  - API
  - DOM
  - JSON
---

<!-- début résumé -->

Ce MON a pour objectif d'apprendre à utiliser le DOM et les données (API, JSON, etc.) à l'aide de JavaScript afin de créer des pages web dynamiques. Ce DOM nous permettra de générer automatiquement des éléments HTML à partir de données stockées dans des fichiers, des bases de données ou sur des serveurs distants.

<!-- fin résumé -->

[<-- Retour](../)

{% prerequis "Prérequis :"  %}

Ce MON est destiné aux personnes **ayant déjà des bases en JavaScript et en HTML/CSS**.

Si vous souhaitez vous initier à JavaScript, je vous invite à consulter cette formation OpenClassrooms : [Apprenez à programmer avec JavaScript](https://openclassrooms.com/fr/courses/6175841-apprenez-a-programmer-avec-javascript)

{% endprerequis %}

## Introduction

Afin d'obtenir les connaissances nécessaires à la réalisation de mon POK, je souhaite me former au **développement Web Full Stack**. Pour y parvenir, il m'a semblé nécessaire de choisir deux MON proposés par la plateforme de formation [Openclassrooms](https://openclassrooms.com/fr). Ce premier MON explique comment utiliser le language Javascript pour parvenir à développer des pages web dynamiques, en apprenant notamment à utiliser les fichiers JSON, les API ou encore des librairies.

![Capture Openclassrooms](https://i.vimeocdn.com/video/1499265044-2cd83363e9cf92fe02a6ef5aeedd9396fa7269195555af32b9be92fef6ad9583-d_640)

## Sommaire

- [Introduction](#introduction)
- [Sommaire](#sommaire)
- [Présentation](#présentation)
  - [Ressources](#ressources)
- [Résumé du MON](#résumé-du-mon)
  - [Présentation du JSON](#présentation-du-json)
  - [Utilisation du DOM](#utilisation-du-dom)
  - [Présentation des API](#présentation-des-api)
  - [Présentation de la programmation asynchrone](#présentation-de-la-programmation-asynchrone)
  - [Présentation de Fetch](#présentation-de-fetch)
  - [Présentation du Local Storage](#présentation-du-local-storage)
  - [Présentation des librairies](#présentation-des-librairies)
  - [Présentation de jQuery](#présentation-de-jquery)

## Présentation

Ce MON a pour objectif d'**apprendre à utiliser le DOM et les données (API, JSON, etc.) à l'aide de JavaScript** afin de créer des **pages web dynamiques**. À l'aide du DOM, on pourra générer automatiquement des éléments HTML à partir de données stockées dans des fichiers, des bases de données ou sur des serveurs distants.

Ce MON repose en grande partie sur une formation proposée par **Openclassrooms** accessible ci-dessous. Des compléments à cette formation peuvent également être trouvés sur YouTube. J'ai fournis quelques liens ci-dessous.

![Exemple](./exemple.png)

La formation est **très claire et très simple à suivre**, comme la plupart des formations proposées par Openclassrooms. Le formateur propose différents **exemples concrets** repris tout au long de la formation. La formation est composée de *vidéos, de cours écrits, d'exemples et d'exercices à chaque étape*. À la fin de chaque chapitre, un **quiz** est proposé afin d'évaluer notre compréhension des différents acquis du chapitre.

### Ressources

{% chemin %}

**Ressources utilisées**

- [Créez des pages web dynamiques avec JavaScript (Openclassrooms)](https://openclassrooms.com/fr/courses/7697016-creez-des-pages-web-dynamiques-avec-javascript)
- [Learn DOM Manipulation In 18 Minutes (YouTube)](https://youtu.be/y17RuWkWdn8)
- [Introduction à jQuery](https://openclassrooms.com/fr/courses/3504441-introduction-a-jquery)

{% endchemin %}

## Résumé du MON

J'ai utilisé **GitHub Copilot** pour rédiger ce résumé. Il s'agit d'un outil proposé par GitHub qui permet de générer du code à partir de commentaires. Il est encore en phase de test et ne fonctionne pas parfaitement. Il est tout de même intéressant de voir comment il peut être utilisé pour rédiger des résumés.

### Présentation du JSON

Le **JSON** est un format de données très utilisé pour échanger des informations entre un serveur et un site web. Il est très simple à utiliser et à comprendre. Il est composé de **paires clé/valeur**. Les clés sont des **chaînes de caractères** et les valeurs peuvent être de différents types : **chaînes de caractères, nombres, booléens, tableaux, objets ou null**.

Exemple :

```json
{
  "nom": "Dupont",
  "prenom": "Jean",
  "age": 42,
  "majeur": true,
  "adresse": {
    "rue": "1 rue de la paix",
    "ville": "Paris",
    "codePostal": "75000"
  },
  "enfants": ["Marc", "Marie", "Julie"]
}
```

Pour importer un fichier JSON dans un fichier JavaScript, on utilise la méthode `fetch()` que l'on verra plus loin.

### Utilisation du DOM

Le **DOM** est un **modèle de données** qui représente les **éléments HTML** d'une page web. Il est composé de **noeuds** qui sont des **éléments HTML**. Ces éléments sont **hiérarchisés** et peuvent être **sélectionnés** à l'aide de **sélecteurs**. Le DOM est très utilisé pour **modifier le contenu** d'une page web, **ajouter** ou **supprimer** des éléments HTML.

Afin d'interagir avec le DOM, il faut utiliser **JavaScript**. Il est possible d'**ajouter** ou de **supprimer** des éléments HTML à l'aide de **propriétés** ou de **méthodes**. Il est également possible de **modifier** le contenu d'un élément HTML existant. Parmi les propriétés et méthodes les plus utilisées, on peut citer :

- `document.getElementById()` : permet de sélectionner un élément HTML à l'aide de son identifiant.
- `document.createElement()` : permet de créer un élément HTML.
- `element.appendChild()` : permet d'ajouter un élément HTML à un autre élément HTML.
- `element.removeChild()` : permet de supprimer un élément HTML.
- etc...

Exemple :

```javascript
// Création d'un élément HTML
const p = document.createElement('p');
// Ajout d'un texte à l'élément HTML
p.textContent = 'Bonjour !';
// Ajout de l'élément HTML à la page web
document.body.appendChild(p);
```

### Présentation des API

Les **API** sont des **interfaces** qui permettent de **récupérer des données** depuis un serveur. Ces données peuvent être des **données brutes** ou des **données structurées**. Les API sont très utilisées pour **récupérer des données** depuis un serveur et les **afficher** sur une page web. Il existe de nombreuses API open source auxquelles ont peut accéder librement, par exemple : **OpenWeatherMap**, **OpenFoodFacts**, **OpenStreetMap**, **OpenDataSoft**, **OpenDataFrance**, **OpenDataParis**, etc.

Pour accéder à une API, on peut également utiliser **JavaScript**. Il est possible d'utiliser **XMLHttpRequest** ou **Fetch**. Les deux méthodes sont très similaires. La méthode **Fetch** est plus récente et plus simple à utiliser. Elle est donc préférée.

### Présentation de la programmation asynchrone

La **programmation asynchrone** est un **concept** qui permet d'exécuter du code **en parallèle**. Elle est très utilisée dans le développement web. Elle permet d'exécuter du code **sans bloquer** l'exécution du reste du code. En effet, le code asynchrone est exécuté **en arrière-plan**. Il est donc possible d'exécuter du code **pendant** que le code asynchrone est en cours d'exécution.

La **programmation asynchrone** a recours à des **promesses**. Une **promesse** est un **objet** qui représente une **opération asynchrone**. Elle peut être dans un des **trois états** suivants :

- **En attente** : l'opération asynchrone n'a pas encore été exécutée.
- **Résolue** : l'opération asynchrone a été exécutée avec succès.
- **Rejetée** : l'opération asynchrone a été exécutée avec erreur.
  
Une **promesse** est composée de **deux méthodes** :

- `then()` : permet de **traiter** la réponse de la promesse.
- `catch()` : permet de **traiter** les erreurs de la promesse.

Exemple :

```javascript
let promise = new Promise(function (resolve, reject) {
  setTimeout(function () {
    resolve("Promesse résolue");
  }, 1000);
});
```

### Présentation de Fetch

La méthode **Fetch** permet de **récupérer des données** depuis un serveur. Elle est très simple à utiliser et à comprendre. Elle est composée de **deux étapes** :

1. On **configure** la requête à l'aide de la méthode `fetch()`. En paramètre, on passe l'**URL** de l'API à laquelle on souhaite accéder. Cette méthode retourne une **promesse**. On peut donc utiliser la méthode `then()` pour **traiter** la réponse. On peut également utiliser la méthode `catch()` pour **traiter** les erreurs. On peut également utiliser la méthode `finally()` pour **exécuter** du code à la fin de la requête.
2. On **traite** la réponse à l'aide de la méthode `json()`. Cette méthode retourne une **promesse**. On peut donc également utiliser la méthode `then()` pour **traiter** la réponse.

Exemple :

```javascript
fetch("https://api.openweathermap.org/data/2.5/weather?q=Paris&appid=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    console.log(data);
  })
  .catch(function (error) {
    console.log(error);
  })
  .finally(function () {
    console.log("Requête terminée");
  });
```

La méthode `fetch()` utilise la méthode `GET` par défaut. Il est possible de **modifier** la méthode à l'aide de la propriété `method`. Il est également possible de **modifier** les **en-têtes** de la requête à l'aide de la propriété `headers`. Il est possible de **modifier** les **paramètres** de la requête à l'aide de la propriété `body`.

Exemple :

```javascript
fetch("https://api.openweathermap.org/data/2.5/weather", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    q: "Paris",
    appid: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  }),
})
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    console.log(data);
  })
  .catch(function (error) {
    console.log(error);
  })
  .finally(function () {
    console.log("Requête terminée");
  });
```

### Présentation du Local Storage

Le **Local Storage** est un **espace de stockage** qui permet de **stocker des données** sur le **navigateur** de l'utilisateur. Il est possible de **stocker des données** sous forme de **chaîne de caractères**. Il est possible de **stocker des données** de manière **permanente** ou **temporaire**. Il est possible de **stocker des données** de manière **sécurisée** ou **non sécurisée**. Il est possible de **stocker des données** de manière **synchronisée** ou **non synchronisée**.

Il est possible de **stocker des données** dans le **Local Storage** à l'aide de la méthode `setItem()`. En paramètre, on passe la **clé** et la **valeur** de la donnée à stocker. Il est possible de **récupérer des données** dans le **Local Storage** à l'aide de la méthode `getItem()`. En paramètre, on passe la **clé** de la donnée à récupérer. Il est possible de **supprimer des données** dans le **Local Storage** à l'aide de la méthode `removeItem()`. En paramètre, on passe la **clé** de la donnée à supprimer. Il est possible de **supprimer toutes les données** dans le **Local Storage** à l'aide de la méthode `clear()`.

Exemple :

```javascript
localStorage.setItem("key", "value");
localStorage.getItem("key");
localStorage.removeItem("key");
localStorage.clear();
```

### Présentation des librairies

Les **librairies** sont des **bibliothèques** qui contiennent des **fonctions** et des **méthodes** qui permettent de **réaliser des tâches** plus rapidement. Il existe de nombreuses librairies, par exemple : **jQuery**, **Bootstrap**, **React**, **Vue**, **Angular**, **Lodash**, **Moment**, **Chart.js**, **Leaflet**, **D3**, etc.

Pour utiliser une librairie, il faut la **télécharger** et la **inclure** dans notre page web. Il est également possible d'utiliser des **CDN** (Content Delivery Network) qui permettent d'inclure une librairie dans notre page web sans avoir à la télécharger. Les librairies sont très utiles pour, par exemple, **réaliser des animations** ou pour **générer des graphiques**.

### Présentation de jQuery

{% chemin %}

Une formation complète sur jQuery est disponible sur **OpenClassrooms** :

- [Introduction à jQuery](https://openclassrooms.com/fr/courses/3504441-introduction-a-jquery)

{% endchemin %}

![Introduction à jQuery](https://i.vimeocdn.com/video/822498516-042feb94146f0232cf0caa3c3d498aee6056890e327b1093b3eb3d838dbd686e-d_640)

Un exemple de librairie est **jQuery** qui permet de **sélectionner** des éléments dans le **DOM** à l'aide de la méthode `$(selector)`. En paramètre, on passe le **sélecteur** de l'élément à sélectionner, qui peut être un **sélecteur CSS** ou un **sélecteur jQuery**. Cette méthode retourne un **objet jQuery** qui contient des **méthodes** qui permettent de **modifier** les éléments sélectionnés.

Pour utiliser jQuery, il faut inclure le fichier `jquery.min.js` dans notre page web comme ceci :

```html
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
```

On pourra ensuite utiliser les méthodes de jQuery comme ceci :

```javascript
// Sans jQuery
document.querySelector("h1").style.color = "red";
// Avec jQuery
$("h1").css("color", "red");
```

[<-- Retour](../)
