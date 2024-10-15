---
layout: layout/pok.njk

title: "Dark Kitchen - FrontEnd"
authors:
  - Sofiane Ouadda

date: 2024-09-16

tags: 
  - 'temps 1'
  - 'FrontEnd'
  - 'HTML'
  - 'CSS'
  - 'JavaScript'
  - 'Vue.js'
  - 'Dark Kitchen'

résumé: "Codage du FrontEnd du site de ma Dark Kitchen avec HTML/CSS/JavaScript et transition vers Vue.js pour une structure dynamique."
---

{% prerequis %}
**Niveau :** Basique à Intermédiaire  
**Pré-requis :**
- Connaissances de base en HTML/CSS.
- Connaissance des concepts fondamentaux de JavaScript (variables, fonctions, DOM).
- Une première expérience avec un éditeur de code.
- Familiarité avec le concept des frameworks FrontEnd (Vue.js sera introduit).

{% endprerequis %}
{% lien %}

- [GitHub Projet Dark Kitchen v1](https://github.com/SofianeOuadda/dark-kitchen)
- [GitHub Projet Dark Kitchen v2](https://github.com/SofianeOuadda/dark-kitchen-v2)

{% endlien %}

# POK 1 - Dark Kitchen - FrontEnd

Ce POK décrit les étapes du développement du site web de ma Dark Kitchen. Il s'agit de la création du FrontEnd à l'aide de HTML, CSS et JavaScript. Le projet évoluera vers une structure dynamique en utilisant Vue.js. Le site aura une page d'accueil, un menu, un panier et d'autres composants nécessaires pour une boutique en ligne.

## Objectifs principaux

1. Mettre en pratique les connaissances acquises en HTML/CSS lors du **MON1**.
2. Appliquer les fondamentaux de JavaScript appris dans le **MON2** pour dynamiser le FrontEnd.
3. Migrer le site d'une architecture statique vers une structure plus dynamique avec **Vue.js**.
4. Déployer une interface utilisateur fluide et réactive pour un site web de Dark Kitchen.

## Plan d'action

### 1. Conception initiale avec HTML/CSS
- Définir la structure du site avec HTML : création de l'index, page de menu, et panier.
- Designer l'interface utilisateur à l'aide de CSS : structure de la navigation, sections, boutons et visuels.
- Développement du layout général et de l'identité visuelle (typographie, couleurs, design des boutons).

### 2. Dynamisation du FrontEnd avec JavaScript
- Intégrer des fonctionnalités JavaScript pour dynamiser l'interface utilisateur (par exemple, le panier).
- Manipulation du DOM pour interagir avec les éléments HTML.
- Ajouter des transitions et animations légères via CSS et JavaScript.

### 3. Migration vers Vue.js
- Refactoriser le code HTML/CSS/JavaScript en composants Vue.js.
- Introduction de la réactivité : rendre le site plus dynamique en fonction des interactions utilisateurs.
- Gestion des événements utilisateurs (ex. : ajout de produits au panier, mise à jour du contenu).

## Sprints de développement

### Sprint 1 : Développement initial avec HTML/CSS
- **Objectif :** Structurer le site web avec les pages principales et concevoir l'interface de base.
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

 #### [CE SPRINT N'A PAS ÉTÉ RÉALISER] (Pas utile pour la migration vers Vue)
### Sprint 2 : Dynamisation avec JavaScript 
- ~~**Objectif :** Intégrer des fonctionnalités JavaScript pour interagir avec le contenu.~~
  - ~~[ ] Utiliser JavaScript pour ajouter des produits au panier et mettre à jour dynamiquement le contenu.~~
  - ~~[ ] Gestion des événements DOM (ex. : clics sur les boutons "Ajouter au panier").~~
  - ~~[ ] Implémentation de transitions visuelles avec CSS et JavaScript.~~

### Sprint 3 : Migration vers Vue.js

- **Objectif :** Migrer l'application existante vers Vue.js et implémenter les fonctionnalités permettant d'ajouter des éléments au panier, tout en calculant dynamiquement le total.

##### 1. Configuration du Projet Vue.js
- **Tâches** :
  - Initialiser un nouveau projet Vue.js avec Vue CLI.
  - Créer la structure des dossiers du projet (`components`, `views`, `router`, etc.).
  - Valider que le projet démarre correctement avec un serveur local.

##### 2. Migration des Composants Visuels (Header, Footer, Hero)
- **Tâches** :
  - Migrer les éléments statiques du header et footer dans des composants Vue (`AppHeader`, `AppFooter`).
  - Créer un composant `AppHero` pour l'image de fond et le texte d'introduction.
  - Valider l'affichage statique sans logique métier.

##### 3. Migration des Pages (Home, Menu, Panier)
- **Tâches** :
  - Migrer la page d'accueil dans `HomePage.vue` en utilisant les composants `AppHero`, `AppHeader`, et `AppFooter`.
  - Créer la structure de la page Menu dans `MenuPage.vue` en affichant une liste statique d'items de menu.
  - Créer la page `CartPage.vue` pour afficher le panier avec les articles ajoutés.

##### 4. Ajout des Composants Dynamiques (MenuItem, CartItem)
- **Tâches** :
  - Créer le composant `AppMenuItem.vue` pour chaque item du menu, avec les props `name`, `description`, `price`, et `image`.
  - Créer le composant `AppCartItem.vue` pour chaque article dans le panier, avec les props `name`, `price`, et `quantity`.
  - Valider que chaque composant affiche correctement les données transmises.

##### 5. Gestion Globale du Panier dans `App.vue`
- **Tâches** :
  - Implémenter la gestion globale du panier dans `App.vue` avec une méthode `addToCart(item)` pour ajouter des articles et une méthode `removeFromCart(item)` pour les retirer.
  - Utiliser un tableau d'articles dans l'état global (`data`) pour stocker les articles du panier.
  - Passer les méthodes `addToCart` et `removeFromCart` en tant que props aux composants enfants (`MenuPage.vue` et `CartPage.vue`).
  - S'assurer que les pages Menu et Panier interagissent avec le panier global dans `App.vue`.


##### 6. Calcul Dynamique du Total du Panier
- **Tâches** :
  - Ajouter une méthode dans `CartPage.vue` pour calculer le total du panier en fonction des quantités et des prix.
  - Mettre à jour dynamiquement le total lorsque des articles sont ajoutés ou supprimés.
  - Afficher le total à la fin de la page Panier.

#### Démo du site après la migration vers Vue

<div style="display: flex; justify-content: center; align-items: center; height: 480;">
  <video style="max-width: 100%; height: auto;" controls>
    <source src="./video/Demo_Website_Vue.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
</div>

### Horodateur

| Date       | Heures passées | Indications                                    |
|------------|----------------|------------------------------------------------|
| 13/09      | 1H             | Création du projet GitHub                      |
| 13/09      | 1H             | Création de la structure du code Html          |
| 14/09      | 2H             | Conception primitive des pages du sites        |
| 15/09      | 3H             | Design de la page principal avec CSS           |
| 16/09      | 3H             | Design des pages menu et panier                |
| 25/09      | 1H             | Configuration du projet Vue.js et initialisation avec Vue CLI     |
| 09/10      | 2H             | Migration des composants statiques (Header, Footer, Hero)         |
| 09/10      | 3H             | Migration des pages Menu et Panier                                |
| 10/10      | 2H             | Création des composants dynamiques `AppMenuItem` et `AppCartItem` |
| 11/10      | 2H             | Gestion globale du panier dans `App.vue`                          |
| 11/10      | 2H             | Implémentation du calcul dynamique du total dans le panier        |
