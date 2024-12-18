---
layout: layout/pok.njk

title: "Dark Kitchen - BackEnd"
authors:
  - Thomas Merle

date: 2024-10-16

tags:
  - 'temps 2'
  - 'BackEnd'
  - 'Node.js'
  - 'Express.js'
  - 'MongoDB'
  - 'API REST'
  - 'Dark Kitchen'

résumé: "Codage du BackEnd du site de ma Dark Kitchen avec NodeJS."
---
{% prerequis %}
**Niveau :** Technique
**Pré-requis:**
- Connaissances de base en JavaScript.
- Familiarité avec Node.js et npm.
- Familiarités avec les bases de données et leur gestion avec MangoDB.
- Notions d’API REST et endpoints.

{% endprerequis %}
{% lien %}

- [`MON2.1: Initiation au BackEnd : go to learn Go!`](https://francoisbrucker.github.io/do-it/promos/2024-2025/Merle-Thomas/mon/temps-2.1/)
- [`GitHub Projet Dark Kitchen v2`](https://github.com/SofianeOuadda/dark-kitchen-v2)
- [GitHub Backend Dark Kitchen](https://github.com/SofianeOuadda/dark-kitchen-v2)


{% endlien %}

Quelques phrases permettant de connaître, sans jargon ni blabla, le contenu de ce POK. On oubliera pas de donner :

- le niveau et les prérequis nécessaires en utilisant la balise [`prerequis`](/cs/contribuer-au-site/#prerequis)
- les autres POK & MON en rapport en utilisant la balise [`lien`](/cs/contribuer-au-site/#lien)

# <span style="color: green">POK2 - Dark Kitchen - BackEnd
Codage en JS (NodeJS). 

Ce POK décrit les étapes du développement du site web de notre Dark Kitchen de Fried Rice et de Noodles **S&T Goreng**. Il comprend la mise en place d'une **API REST**, la connexion à une base de données **MongoDB** et des fonctionnalités essentielles côté serveur.

---

## Objectifs principaux

1. Conception des API: construire une API REST avec **Node.js** et **Express.js** pour gérer les produits, commandes et le panier. Création des endpoints et de l'architecture API.
2. Modéliser les données : définir les modèles nécessaires avec **MongoDB** comme base de données pour stocker les informations de manière persistante.
3. Refactoriser et structurer le code pour une meilleure maintenabilité.
4. Rendre le backend fonctionnel pour intégration avec le frontend.

### 1. Initialisation du projet
- **Tâches :**
  - [Sofiane](#)&[Thomas](#) Initialiser un projet Node.js avec `npm init`.
  - [Sofiane](#)&[Thomas](#) Installer les dépendances principales : `express`, `mongoose`, `dotenv`.
  - [Sofiane](#)&[Thomas](#) Configurer un fichier `.env` pour stocker les variables sensibles comme le port et l’URI **MongoDB**.
  - [Sofiane](#)&[Thomas](#) Créer un serveur Express.js fonctionnel qui écoute sur un port donné.

### 2. Connexion à MongoDB
- **Tâches :**
  - [Thomas](#) Créer un cluster MongoDB sur **MongoDB Atlas**.
  - [[Thomas](#) Configurer la connexion entre le serveur Node.js et MongoDB à l’aide de `mongoose`.
  - [Thomas](#) Définir les schémas et modèles pour :
    - **Produits** (nom, description, prix, image).
    - **Users** (nom, eamil, passwords).
  - [Thomas](#) Ajouter des données de test pour les produits.

  ### 3. Création des routes API REST
- **Tâches :**
  - [Sofiane](#) Implémenter les routes suivantes :
    - `GET /api/products` : Liste tous les produits.
    - `GET /api/products/:id` : Détaille un produit spécifique.
    - `POST /api/products/` : Création un produit spécifique.
    - `PUT /api/products/:id` : Update un produit spécifique.
    - `DELETE /api/products/:id` : Suprimer un produit spécifique.
    - `POST /api/login` : Se connecter
    - `POST /api/register` : Créaction d'un nouveau compte
  - Structurer les routes pour qu'elles utilisent les méthodes **CRUD** associées.

### 4. Refactorisation et modularisation du code
- **Tâches :**
  - [Sofiane](#)&[Thomas](#) Organiser le projet en modules :
    - `routes/` : Fichiers pour les routes (`products.js`, `orders.js`).
    - `controllers/` : Logique métier séparée des routes.
    - `models/` : Définition des schémas **Mongoose**.
  - Ajouter un fichier `utils/` pour des fonctions utilitaires (exemple : formatage des données).

### 5. Ajout des données et validation simple
- **Tâches :**
  - [Sofiane](#)&[Thomas](#) Ajouter des produits par défaut directement dans MongoDB: données **Product** notamment.
  - [Sofiane](#)&[Thomas](#) Vérifier que les produits sont bien récupérés via les routes `GET /api/products` et `GET /api/products/:id`.

### 6. Intégration du Backend avec le Frontend
- **Tâches :**
  - [Sofiane](#)&[Thomas](#) Connecter le frontend en **Vue.js** avec l'API backend en utilisant **Axios** ou **Fetch** pour effectuer des appels API.
  - [Sofiane](#)&[Thomas](#) Tester les appels aux différentes routes API (produits, panier, commandes) depuis le frontend pour vérifier que les données sont correctement affichées et manipulées.
  - [Sofiane](#)&[Thomas](#) Implémenter des actions sur le frontend comme l'ajout de produits au panier via l'API `POST /api/cart` et l'affichage des produits depuis `GET /api/products`.
  - [Sofiane](#)&[Thomas](#) Vérifier que les pages du frontend, comme le panier et le menu, interagissent correctement avec le backend pour mettre à jour les données de manière dynamique.

---

## Sprints de développement

--

### Sprint 1 : Initialisation et serveur Express
- **Objectif :** Créer un serveur **Express.js** fonctionnel.
- **Tâches** :
  - [x] [Sofiane](#)&[Thomas](#) Initialisation du projet et installation des dépendances.
  - [x] [Sofiane](#)&[Thomas](#) Configuration du serveur avec **express**.

## Sprint 2 : Connexion à MongoDB et création des modèles
- **Objectif :** Configurer MongoDB et définir les schémas des données.
- **Tâches** :
  - [x] [Thomas](#) Création du cluster **MongoDB Atlas**.
  - [x] [Thomas](#) Connexion avec **mongoose**.
  - [x] [Thomas](#) Création des modèles **Product**, **Order** et **User**.
  - [x] [Thomas](#) Ajout de données de test pour les **Product**.
  - [x] [Sofiane](#) Connexion à MongoDB pour l'authentification : création des données **Users** via script.

### Sprint 3 : Développement des routes API
- **Objectif :** Implémenter les fonctionnalités principales de l’API.
- **Tâches** :
  - [x] [Thomas](#) Création route pour les produits (`GET`, `POST`, `PUT`, `DELETE`)..
  - [x] [Sofiane](#) Création routes pour l'authentification.
  - [x] [Sofiane](#)&[Thomas](#) Validation basique des données entrantes.

--

### Sprint 4 : Refactorisation et modularisation
- **Objectif :** Organiser le projet pour faciliter la maintenance et les futures évolutions.
- **Tâches** :
  - [x] [Sofiane](#)&[Thomas](#) Séparation des routes, contrôleurs et modèles dans des dossiers dédiés.
  - [x] [Sofiane](#)&[Thomas](#) Structuration du code en modules clairs (`routes/`, `models/`).

### Sprint 5 : Ajout des données et validation simple
- **Objectif :** Ajouter des données de test et vérifier le fonctionnement des routes API.
- **Tâches** :
  - [x] [Sofiane](#)&[Thomas](#) Ajout manuel des produits par défaut dans la base de données MongoDB.
  - [ ] Validation des données récupérées avec **Postman**.

### Sprint 6 : Intégration du Backend avec le Frontend
- **Objectif :** Assurer la communication entre le frontend **Vue.js** et le backend **Node.js** via des API.
- **Tâches** :
  - [x] [Sofiane](#)&[Thomas](#) Implémentation des appels API pour récupérer les produits et gérer le panier.
  - [x] [Sofiane](#) Implémentation des appels API pour enregistrer des **User**.
  - [x] [Sofiane](#) Mise à jour du FrontEnd avec les popups **LogIn** et **SignIn**.
  - [x] [Sofiane](#)&[Thomas](#) Vérification de l'affichage dynamique des produits dans le frontend.
  - [x] [Sofiane](#)&[Thomas](#) Tester connexion/l'enregistrement d'un user et ajout à la base de donnée.

--

## Horodateur

Toutes les séances et le nombre d'heure que l'on y a passé.

| Date       | Heures passées | Indications                                    |
|------------|----------------|------------------------------------------------|
| 01/11  | 1H             | Formation à Node.js à l'aide des MONs et de la documentation |
| 01/11  | 1H             | Initialisation du projet et configuration Node.js à partir du projet frontend|
| 01/11  | 1H             | Structuration du nouveau projet avec intégration du backend et configuration des servers|
| 01/11  | 3H             | Mise en place de MongoDB et connexion|
| 02/11  | 2H             | Création des modèles pour les données : **Product**, **Order** et **User** |
| 07/11  | 2H             | Développement des routes API authentification et products|
| 07/12  | 3H             | Création du middleware d'authentification JWT |
| 08/12  | 3H             | Tests manuels des routes et ajustements |
| 12/11  | 4H             | Intégration des produits dynamiques au backend |
| 14/11  | 4H             | Connexion du frontend au backend (authentification et produits) |
