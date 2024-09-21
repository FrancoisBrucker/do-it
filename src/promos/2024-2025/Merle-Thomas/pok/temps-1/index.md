---
layout: layout/pok.njk

title: "Asian Fried Rice - FrontEnd"
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

résumé: "Codage du FrontEnd du site de notre Dark Kitchen de Fried Rice"
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

[`W3School`](https://www.w3schools.com/js/default.asp)
[`MON1: HTML/CSS`](https://francoisbrucker.github.io/do-it/promos/2024-2025/Merle-Thomas/mon/temps-1.1/)
[`MON2: JavaScript`](https://francoisbrucker.github.io/do-it/promos/2024-2025/Merle-Thomas/mon/temps-1.2/)

{% endlien %}

Quelques phrases permettant de connaître, sans jargon ni blabla, le contenu de ce POK. On oubliera pas de donner :

- le niveau et les prérequis nécessaires en utilisant la balise [`prerequis`](/cs/contribuer-au-site/#prerequis)
- les autres POK & MON en rapport en utilisant la balise [`lien`](/cs/contribuer-au-site/#lien)

# <span style="color: #26B260">POK 1 - Asian Fried Rice - FrontEnd
Codage en HTML/CSS/JavaScript. 

Ce POK décrit les étapes du développement du site web de notre Dark Kitchen de Fried Rice. Il s'agit de la création du FrontEnd à l'aide de HTML, CSS et JavaScript. Le projet évoluera vers une structure dynamique en utilisant Vue.js. Le site aura une page d'accueil, un menu, un panier et d'autres composants nécessaires pour faire des commandes en ligne.

## <span style="color: #26B260">Objectifs principaux

1. Mise en oeuvre des connaissances acquises durant les **MON** et **MON2**.
2. Mise en pratique de l'apprentissage des languages **HTML/CSS** et **JavaScript**.
3. Migrer le site d'une architecture statique vers une structure plus dynamique avec **Vue.js**.
4. Déployer une interface utilisateur fluide et réactive pour un site web de Dark Kitchen.


## <span style="color: #26B260">Plan d'action
### 1. Conception initiale avec HTML/CSS
- Définir la structure du site avec HTML : création de l'**index** (page d'accueil), **page de menu**, et **panier**.
- Designer l'interface utilisateur à l'aide de **CSS** : structure de la navigation, sections, boutons et visuels.
- Développement du layout général et de l'identité visuelle (typographie, couleurs, design des boutons).

### 2. Dynamisation du FrontEnd avec JavaScript
- Intégrer des fonctionnalités **JavaScript** pour dynamiser l'interface utilisateur (par exemple, le panier).
- Manipulation du **DOM** pour interagir avec les éléments HTML.
- Ajouter des transitions et animations légères via **CSS** et **JavaScript**.

### 3. Migration vers Vue.js
- Refactoriser le code **HTML/CSS/JavaScript** en composants **Vue.js**.
- Introduction de la réactivité : rendre le site plus dynamique en fonction des interactions utilisateurs.
- Gestion des événements utilisateurs (ex. : ajout de produits au panier, mise à jour du contenu).

### <span style="color: purple">Sprint 1
- **Objectif :** Structurer le site web avec les pages principales (accueil, menu et panier) et concevoir l'interface de base.
  - [x] Création du fichier `index.html` avec les sections : header, hero, featured dish, footer.
  - [x] Conception de la page `menu.html` avec un système de grille pour afficher les menus.
  - [x] Création de la page `panier.html` pour gérer les articles du panier.
  - [x] Définition du style de la navigation (menus, boutons, couleurs) dans le fichier `style.css`.


### <span style="color: purple">Sprint 2
- **Objectif :** Intégrer des fonctionnalités JavaScript pour interagir avec le contenu.
  - [ ] Utiliser JavaScript pour ajouter des produits au panier et mettre à jour dynamiquement le contenu.
  - [ ] Gestion des événements DOM (ex. : clics sur les boutons "Ajouter au panier").
  - [ ] Implémentation de transitions visuelles avec CSS et JavaScript.

### <span style="color: purple">Sprint 3 :
- **Objectif :** Transformer le site en une application plus interactive avec Vue.js.
  - [ ] Diviser les pages en composants Vue.js (ex. : `MenuComponent`, `CartComponent`).
  - [ ] Mettre en place la réactivité avec Vue pour gérer les états du panier.
  - [ ] Utiliser des directives Vue (`v-for`, `v-if`, etc.) pour dynamiser l'affichage du contenu.
  - [ ] Intégration de formulaires réactifs pour la commande.

### Horodateur

Toutes les séances et le nombre d'heure que l'on y a passé.

| Date       | Heures passées | Indications                                    |
|------------|----------------|------------------------------------------------|
| 13/09      | 1H             | Création du projet GitHub                      |
| 13/09      | 1H             | Création de la structure du code HTML          |
| 14/09      | 2H             | Conception primitive des pages du sites        |
| 15/09      | 3H             | Design de la page principal avec CSS           |
| 16/09      | 3H             | Design des pages **menu** et **panier**        |