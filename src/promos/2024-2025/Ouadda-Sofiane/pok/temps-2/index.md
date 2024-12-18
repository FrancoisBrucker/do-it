---
layout: layout/pok.njk

title: "Dark Kitchen - BackEnd"
authors:
  - Sofiane Ouadda
date: 2024-10-20

tags:
  - 'temps 2'
  - 'BackEnd'
  - 'Node.js'
  - 'Express.js'
  - 'MongoDB'
  - 'API REST'
  - 'Dark Kitchen'
résumé: "Développement du BackEnd pour le site de ma Dark Kitchen en utilisant Node.js, Express.js, MongoDB et des API REST pour gérer les produits, le panier et les commandes."
---

{% prerequis %}
**Pré-requis :**
- Connaissances de base en JavaScript.
- Familiarité avec Node.js et npm.
- Notions d’API REST et de bases de données comme MongoDB.
{% endprerequis %}

{% lien %}
[GitHub Backend Dark Kitchen](https://github.com/SofianeOuadda/dark-kitchen-backend)
{% endlien %}

# POK 2 - Dark Kitchen - BackEnd

Ce POK détaille le développement du backend pour le site **Dark Kitchen**. Il comprend la mise en place d'une **API REST**, la connexion à une base de données **MongoDB** et des fonctionnalités essentielles côté serveur.

## Objectifs principaux

1. Construire une API REST avec **Node.js** et **Express.js** pour gérer les produits, commandes et le panier.
2. Intégrer **MongoDB** comme base de données pour stocker les informations de manière persistante.
3. Refactoriser et structurer le code pour une meilleure maintenabilité.
4. Rendre le backend fonctionnel pour intégration avec le frontend.

## Plan d'action

### 1. Initialisation du projet
- **Tâches :**
  - Initialiser un projet Node.js avec `npm init`.
  - Installer les dépendances principales : `express`, `mongoose`, `dotenv`.
  - Configurer un fichier `.env` pour stocker les variables sensibles comme le port et l’URI MongoDB.
  - Créer un serveur Express.js fonctionnel qui écoute sur un port donné.

### 2. Connexion à MongoDB
- **Tâches :**
  - Créer un cluster MongoDB sur MongoDB Atlas.
  - Configurer la connexion entre le serveur Node.js et MongoDB à l’aide de `mongoose`.
  - Définir les schémas et modèles pour :
    - **Produits** (nom, description, prix, image).
    - **Users** (nom, eamil, passwords).
  - Ajouter des données de test pour les produits.

  ### 3. Création des routes API REST
- **Tâches :**
  - Implémenter les routes suivantes :
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
  - Organiser le projet en modules :
    - `routes/` : Fichiers pour les routes (`products.js`, `auth.js`).
    - `controllers/` : Logique métier séparée des routes.
    - `models/` : Définition des schémas **Mongoose**.
  - Ajouter un fichier `utils/` pour des fonctions utilitaires (exemple : formatage des données).

### 5. Ajout des données et validation simple
- **Tâches :**
  - Ajouter des produits par défaut via un script ou directement dans MongoDB.
  - Vérifier que les produits sont bien récupérés via les routes `GET /api/products` et `GET /api/products/:id`.

### 6. Intégration du Backend avec le Frontend
- **Tâches :**
  - Connecter le frontend en **Vue.js** avec l'API backend en utilisant **Axios** ou **Fetch** pour effectuer des appels API.
  - Tester les appels aux différentes routes API (produits, users) depuis le frontend pour vérifier que les données sont correctement affichées et manipulées.
  - Implémenter des actions sur le frontend comme l'ajout de produits au panier via l'API `POST /api/cart` et l'affichage des produits depuis `GET /api/products`.
  - Vérifier que les pages du frontend, comme le panier et le menu, interagissent correctement avec le backend pour mettre à jour les données de manière dynamique.

## Sprints de développement

### Sprint 1 : Initialisation et serveur Express
- **Objectif :** Créer un serveur **Express.js** fonctionnel.
- **Tâches** :
  - [x] Initialisation du projet et installation des dépendances.
  - [x] Configuration du serveur avec **express**.

## Sprint 2 : Connexion à MongoDB et création des modèles
- **Objectif :** Configurer MongoDB et définir les schémas des données.
- **Tâches** :
  - [x] Création du cluster MongoDB.
  - [x] Connexion avec **mongoose**.
  - [x] Création des modèles **Product** et **Users**.
  - [x] Ajout de données de test pour les produits.

### Sprint 3 : Développement des routes API
- **Objectif :** Implémenter les fonctionnalités principales de l’API.
- **Tâches** :
  - [x] Routes pour les produits (`GET`, `POST`, `PUT`, `DELETE`).
  - [x] Routes pour les commandes (`POST`).
  - [x] Validation basique des données entrantes.

### Sprint 4 : Refactorisation et modularisation
- **Objectif :** Organiser le projet pour faciliter la maintenance et les futures évolutions.
- **Tâches** :
  - [x] Séparation des routes, modèles dans des dossiers dédiés.
  - [x] Structuration du code en modules clairs (`routes/`, `models/`).

### Sprint 5 : Ajout des données et validation simple
- **Objectif :** Ajouter des données de test et vérifier le fonctionnement des routes API.
- **Tâches** :
  - [x] Ajout manuel ou via script des produits par défaut.
  - [ ] Validation des données récupérées avec **Postman**.

### Sprint 6 : Intégration du Backend avec le Frontend
- **Objectif :** Assurer la communication entre le frontend **Vue.js** et le backend **Node.js** via des API.
- **Tâches** :
  - [x] Implémentation des appels API pour récupérer les produits.
  - [x] Vérification de l'affichage dynamique des produits dans le frontend.
  - [x] Tester connexion/l'enregistrement d'un user et ajout à la base de donnée.

# Horodateur

| Date   | Heures passées | Indications                                         |
|--------|----------------|-----------------------------------------------------|
| 01/11  | 1H             | Initialisation du projet et configuration Node.js   |
| 01/11  | 3H             | Mise en place de MongoDB et connexion               |
| 02/11  | 2H             | Création des modèles de données (User, Product)     |
| 07/11  | 2H             | Développement des routes API pour l'authentification |
| 07/12  | 3H             | Création du middleware d'authentification JWT       |
| 08/12  | 3H             | Tests manuels des routes et ajustements |
| 12/11  | 4H             | Intégration des produits dynamiques au backend      |
| 14/11  | 4H             | Connexion du frontend au backend (authentification et produits) |