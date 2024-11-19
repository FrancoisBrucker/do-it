---
layout: layout/pok.njk

title: "Dark Kitchen - FrontEnd"
authors:
  - Thomas Merle

date: 2024-09-05

tags: 
  - 'temps 1'
  - 'vert'
  - 'FrontEnd'
  - 'CSS'
  - 'HTML'
  - 'JavaScript'
  - 'Dark Kitchen'

résumé: "Codage du FrontEnd du site de ma Dark Kitchen avec HTML/CSS/JavaScript et transition vers Vue.js pour une structure dynamique."
---
{% prerequis %}
**Niveau :** Basique
**Pré-requis:**
- Développement FrontEnd en HTML/CSS/JavaScript.
- Méthode d'analyse du besoin client : définir l'expérience utilisateur.
- Développement UI/UX.
- Connaissance des concepts fondamentaux de JavaScript (variables, fonctions, DOM).
- Une première expérience avec un éditeur de code.
- Familiarité avec le concept des frameworks FrontEnd (Vue.js sera introduit).

{% endprerequis %}
{% lien %}

- [`W3School`](https://www.w3schools.com/js/default.asp)
- [`MON1: HTML/CSS`](https://francoisbrucker.github.io/do-it/promos/2024-2025/Merle-Thomas/mon/temps-1.1/)
- [`MON2: JavaScript`](https://francoisbrucker.github.io/do-it/promos/2024-2025/Merle-Thomas/mon/temps-1.2/)

- [`GitHub Projet Dark Kitchen v1`](https://github.com/SofianeOuadda/dark-kitchen)
- [`GitHub Projet Dark Kitchen v2`](https://github.com/SofianeOuadda/dark-kitchen-v2)

{% endlien %}

Quelques phrases permettant de connaître, sans jargon ni blabla, le contenu de ce POK. On oubliera pas de donner :

- le niveau et les prérequis nécessaires en utilisant la balise [`prerequis`](/cs/contribuer-au-site/#prerequis)
- les autres POK & MON en rapport en utilisant la balise [`lien`](/cs/contribuer-au-site/#lien)

# <span style="color: green">POK 1 - Asian Fried Rice - FrontEnd
Codage en HTML/CSS/JavaScript. 

Ce POK décrit les étapes du développement du site web de notre Dark Kitchen de Fried Rice et de Noodles. Il s'agit de la création du FrontEnd à l'aide de HTML, CSS et JavaScript. Le projet évoluera vers une structure dynamique en utilisant **Vue.js**. Le site aura une page d'accueil, un menu, un panier et d'autres composants nécessaires pour faire des commandes en ligne.

## Objectifs principaux

1. Mise en oeuvre des connaissances acquises durant les **MON1** et **MON2**.
2. Mise en pratique de l'apprentissage des languages **HTML/CSS** et **JavaScript**.
3. Migrer le site d'une architecture statique vers une structure plus dynamique avec **Vue.js**.
4. Déployer une interface utilisateur fluide et réactive pour un site web de Dark Kitchen.
5. Mettre en place une gestion de porjet de type **Pair Programming**, dan sl'objectif d'apprendre à développer un site from scratch en utilisant JavaScript. 


## Plan d'action
### 1. Conception initiale avec HTML/CSS
- Définir la structure du site avec HTML : création de l'**index** (page d'accueil), **page de menu**, et **panier**.
- Designer l'interface utilisateur à l'aide de **CSS** : structure de la navigation, sections, boutons et visuels.
- Développement du layout général et de l'identité visuelle (typographie, couleurs, design des boutons).


### 2. Dynamisation du FrontEnd avec JavaScript 
[NON RÉALISÉ] (Pas utile pour la migration vers Vue.js)
- ~~Intégrer des fonctionnalités **JavaScript** pour dynamiser l'interface utilisateur (par exemple, le panier).~~
- ~~Manipulation du **DOM** pour interagir avec les éléments HTML.~~
- ~~Ajouter des transitions et animations légères via **CSS** et **JavaScript**.~~

### 3. Migration vers Vue.js
- Refactoriser le code **HTML/CSS/JavaScript** en composants **Vue.js**.
- Introduction de la réactivité : rendre le site plus dynamique en fonction des interactions utilisateurs.
- Gestion des événements utilisateurs (ex. : ajout de produits au panier, mise à jour du contenu).

### 4. Méthode de développement : le *Pair Programming*
Mon niveau en développement web et mes connaissances des languages et framework utilisés n'étant pas assez développé, nous avons décidé d'utiliser la méthode de Pair Programming à une seule machine. 

Travailler en binôme favorise l’émulation et donc la créativité puisque l’échange fait émerger de nouvelles idées. De plus, cette méthode m'a permis de montée en compétences rapidement. Le transfert de connaissances est plus fluide en pair programming et permet en effet de faire l’économie de l’auto-formation. Nous avons utiliser une méthode classique, sur un même poste de travail avec chacun un rôle bien précis, l’un code et l’autre effectue la revue de code en simultané en alternant les rôles, notamment lorsque je commençais à mieux maîtriser le projet.

## <span style="color: green">Sprint 1
- **Objectif :** Structurer le site web avec les pages principales (accueil, menu et panier) et concevoir l'interface de base.
  - [x] Création du fichier `index.html` avec les sections : header, hero, featured dish, footer.
  - [x] Conception de la page `menu.html` avec un système de grille pour afficher les menus.
  - [x] Création de la page `panier.html` pour gérer les articles du panier.
  - [x] Définition du style de la navigation (menus, boutons, couleurs) dans le fichier `style.css`.


#### Démo du site après la première phase

<div style="display: flex; justify-content: center; align-items: center; height: 480;">
  <video style="max-width: 100%; height: auto;" controls>
    <source src="./video/Demo_Website_HTML.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
</div>

## <span style="color: orange">Sprint 2
### [CE SPRINT N'A PAS ÉTÉ RÉALISÉ] (Pas utile pour la migration vers Vue.js)
- ~~**Objectif :** Intégrer des fonctionnalités JavaScript pour interagir avec le contenu.~~
  - ~~[ ] Utiliser JavaScript pour ajouter des produits au panier et mettre à jour dynamiquement le contenu.~~
  - ~~[ ] Gestion des événements DOM (ex. : clics sur les boutons "Ajouter au panier)~~

## <span style="color: green">Sprint 3 :
- **Objectif :** Transformer le site en une application plus interactive avec Vue.js.
  - [x] Diviser les pages en composants Vue.js (ex. : ``MenuComponent``, ``CartComponent``).
  - [x] Mettre en place la réactivité avec Vue pour gérer les états du panier.
  - [x] Utiliser des directives Vue (``v-for``, ``v-if``, etc.) pour dynamiser l'affichage du contenu.
  - [x] Intégration de formulaires réactifs pour la commande.

- [x]**Objectif :** Migrer l'application existante vers **Vue.js** et implémenter les fonctionnalités permettant d'ajouter des éléments au panier, tout en calculant dynamiquement le total.

### 1. Configuration du Projet Vue.js
- **Tâches** :
  - [Sofiane](#)&[Thomas](#): Initialiser un nouveau projet Vue.js avec Vue CLI. 
  - [Sofiane](#)&[Thomas](#) : Créer la structure des dossiers du projet (``components``, ``views``, ``router``, etc.).
  - [Sofiane](#)&[Thomas](#) : Valider que le projet démarre correctement avec un serveur local.

### 2. Migration des Composants Visuels (Header, Footer, Hero)
- **Tâches** :
  - [Sofiane](#) : Migrer les éléments statiques du header et footer dans des composants Vue (``AppHeader``, ``AppFooter``).
  - [Sofiane](#) : Créer un composant ``AppHero`` pour l'image de fond et le texte d'introduction.
  - [Sofiane](#) : Valider l'affichage statique sans logique métier.

### 3. Migration des Pages (Home, Menu, Panier)
- **Tâches** :
  - [Sofiane](#) : Migrer la page d'accueil dans `HomePage.vue` en utilisant les composants ``AppHero``, ``AppHeader``, et ``AppFooter``.
  - [Sofiane](#)&[Thomas](#) : Créer la structure de la page Menu dans `MenuPage.vue` en affichant une liste statique d'items de menu.
  - [Sofiane](#)&[Thomas](#) : Créer la page `CartPage.vue` pour afficher le panier avec les articles ajoutés.

### 4. Ajout des Composants Dynamiques (MenuItem, CartItem)
- **Tâches** :
  - [Sofiane](#)&[Thomas](#) : Créer le composant `AppMenuItem.vue` pour chaque item du menu, avec les props ``name``, ``description``, ``price``, et ``image``.
  - [Sofiane](#)&[Thomas](#) : Créer le composant `AppCartItem.vue` pour chaque article dans le panier, avec les props ``name``, ``price``, et ``quantity``.
  - [Sofiane](#)&[Thomas](#) : Valider que chaque composant affiche correctement les données transmises.

### 5. Gestion Globale du Panier dans `App.vue`
- **Tâches** :
  - [Sofiane](#)&[Thomas](#) : Implémenter la gestion globale du panier dans `App.vue` avec une méthode ``addToCart(item)`` pour ajouter des articles et une méthode `removeFromCart(item)` pour les retirer.
  - [Sofiane](#)&[Thomas](#) : Utiliser un tableau d'articles dans l'état global (``data``) pour stocker les articles du panier.
  - [Sofiane](#)&[Thomas](#) : Passer les méthodes ``addToCart`` et ``removeFromCart`` en tant que props aux composants enfants (`MenuPage.vue` et `CartPage.vue`).
  - [Sofiane](#) : S'assurer que les pages Menu et Panier interagissent avec le panier global dans `App.vue`.


### 6. Calcul Dynamique du Total du Panier
- **Tâches** :
  - [Sofiane](#)&[Thomas](#) : Ajouter une méthode dans `CartPage.vue` pour calculer le total du panier en fonction des quantités et des prix.
  - [Sofiane](#)&[Thomas](#) : Mettre à jour dynamiquement le total lorsque des articles sont ajoutés ou supprimés.
  - [Sofiane](#)&[Thomas](#) : Afficher le total à la fin de la page Panier.

#### Démo du site après la migration vers Vue
<div style="display: flex; justify-content: center; align-items: center; height: 480;">
  <video style="max-width: 100%; height: auto;" controls>
    <source src="./video/Demo_website_vue.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
</div>

## Horodateur

Toutes les séances et le nombre d'heure que l'on y a passé.

| Date       | Heures passées | Indications                                    |
|------------|----------------|------------------------------------------------|
| 13/09      | 1H             | Création du projet GitHub                      |
| 13/09      | 1H             | Création de la structure du code HTML          |
| 14/09      | 2H             | Conception primitive des pages du sites        |
| 15/09      | 3H             | Design de la page principal avec CSS           |
| 16/09      | 3H             | Design des pages **menu** et **panier**        |
| 09/10      | 2H             | Migration des composants statiques (Header, Footer, Hero)         |
| 09/10      | 3H             | Migration des pages Menu et Panier                                |
| 10/10      | 2H             | Création des composants dynamiques ``AppMenuItem`` et ``AppCartItem`` |
| 11/10      | 2H             | Gestion globale du panier dans `App.vue`                          |
| 11/10      | 2H             | Implémentation du calcul dynamique du total dans le panier        |
| 14/10      | 1H             | Derniers updates comme ajouter le plat du jour à la CartPage depuis la Home Page |