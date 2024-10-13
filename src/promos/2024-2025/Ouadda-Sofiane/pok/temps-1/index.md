---
layout: layout/pok.njk

title: "Dark Kitchen - FrontEnd"
authors:
  - Sofiane Ouadda

date: 2024-09-16

tags: 
  - 'temps 1'
  - 'temps 2'
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

- [MON1 : Développement FrontEnd - HTML/CSS](/promos/2024-2025/Ouadda-Sofiane/mon/temps-1.1/index.md)
- [MON2 : Développement FrontEnd en JavaScript](/promos/2024-2025/Ouadda-Sofiane/mon/temps-1.2/index.md)
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

![demo](./Demo_Website_HTML.mov)

#### [CE SPRINT N'A PAS ÉTÉ RÉALISER] (Pas utile pour la migration vers Vue)
### Sprint 2 : Dynamisation avec JavaScript 
- **Objectif :** Intégrer des fonctionnalités JavaScript pour interagir avec le contenu.
  - [ ] Utiliser JavaScript pour ajouter des produits au panier et mettre à jour dynamiquement le contenu.
  - [ ] Gestion des événements DOM (ex. : clics sur les boutons "Ajouter au panier").
  - [ ] Implémentation de transitions visuelles avec CSS et JavaScript.

### Sprint 3 : Migration vers Vue.js
- **Objectif :** Transformer le site en une application plus interactive avec Vue.js.
  - [x] Diviser les pages en composants Vue.js (ex. : `MenuComponent`, `CartComponent`).
  - [x] Mettre en place la réactivité avec Vue pour gérer les états du panier.
  - [x] Utiliser des directives Vue pour dynamiser l'affichage du contenu.
  - [ ] Intégration de formulaires réactifs pour la commande.

### Horodateur

| Date       | Heures passées | Indications                                    |
|------------|----------------|------------------------------------------------|
| 13/09      | 1H             | Création du projet GitHub                      |
| 13/09      | 1H             | Création de la structure du code Html          |
| 14/09      | 2H             | Conception primitive des pages du sites        |
| 15/09      | 3H             | Design de la page principal avec CSS           |
| 16/09      | 3H             | Design des pages menu et panier                |
