---
layout: layout/mon.njk

title: "API REST"
authors:
  - Serigne Mbaye Sy AMAR

date: 2024-10-18
tags: 
  - "temps 2"
  - "API Rest"

résumé: "Ce MON traite les APIs REST, Une API REST permet la communication entre systèmes via HTTP."
---

{% prerequis %}

- Des connaissance de base en NestJs [Mon Mon 2.1](https://francoisbrucker.github.io/do-it/promos/2024-2025/Amar-Mbaye/mon/temps-2.1/)
- Comprendre Les bases de React [Mon Mon 1.1](https://francoisbrucker.github.io/do-it/promos/2024-2025/Amar-Mbaye/mon/temps-1.1/)
{% endprerequis %}

{% lien %}

[MON 1.1 de Baptiste Audouin Découverte des API REST](https://francoisbrucker.github.io/do-it/promos/2024-2025/Baptiste-Audouin/mon/temps-1.1/)

{% endlien %}

## Table des matières
- [Table des matières](#table-des-matières)
- [Introduction :](#introduction-)
- [Comment intégrer des API REST dans NestJS?](#comment-intégrer-des-api-rest-dans-nestjs)
  - [**1. Créer une Ressource avec Nest CLI**](#1-créer-une-ressource-avec-nest-cli)
  - [**2. Configurer un Contrôleur REST**](#2-configurer-un-contrôleur-rest)
  - [**3. Implémenter la Logique Métier dans le Service**](#3-implémenter-la-logique-métier-dans-le-service)
  - [**4. Ajouter des DTOs pour Valider les Données**](#4-ajouter-des-dtos-pour-valider-les-données)
  - [**5. Connecter une Base de Données (MongoDB)**](#5-connecter-une-base-de-données-mongodb)
  - [**5. Ajouter Swagger pour Documenter les API**](#5-ajouter-swagger-pour-documenter-les-api)
- [**Horodatage**](#horodatage)
- [Sources :](#sources-)

Le but de ce MON est d'acquérir des compétences sur les API REST afin de pouvoir les utiliser dans mon POK. [Veuillez consulter mon POK](https://francoisbrucker.github.io/do-it/promos/2024-2025/Amar-Mbaye/pok/temps-2/) pour une application directe de tout ce que je vais aborder dans ce MON, qui sera divisé au tour de la question  comment intégrer les API REST dans NestJS. 
Pour comprendre l'intégration sur la partie React, je vous invite a consulter [mon github](https://github.com/MbayeSyAmar/api_rest_dans_react/blob/main/api_rest_dans_react.md).  
 
## Introduction :

Cette première partie du MON (la base), à savoir qu'est-ce qu'une API et son fonctionnement, a été traitée de manière très explicite par Baptiste Audouin dans son [MON Temps 1](https://francoisbrucker.github.io/do-it/promos/2024-2025/Baptiste-Audouin/mon/temps-1.1/).  

Pour répondre aux besoins spécifiques de mon POK, je vais me concentrer davantage sur des aspects concrets : comment utiliser une API REST dans un projet intégrant un backend développé avec NestJS.  

## Comment intégrer des API REST dans NestJS?

L'intégration d'API REST dans **NestJS** consiste à créer des **contrôleurs**, des **services** et des **modèles** pour gérer les données et répondre aux requêtes HTTP. Je me suis appuyé principalement sur la documentation officielle de NestJS ainsi que sur des exemples sur GitHub pour la mise en place de l'API.  

---

### **1. Créer une Ressource avec Nest CLI**

NestJS propose une commande pour générer rapidement une ressource REST complète (contrôleur, service et module).

Exemple : Générer une ressource pour les **posts**.

```bash
nest generate resource posts
```

Pour comprendre au mieux la structure des fichiers dans Nestjs ainsi que la base, vous pouvez consulter mon MON (2.1)(lien au niveau des prerequis).

Le CLI crée les fichiers suivants dans `src/posts/` :
- `posts.module.ts`
- `posts.service.ts`
- `posts.controller.ts`
- DTOs : `create-post.dto.ts`, `update-post.dto.ts`

---

### **2. Configurer un Contrôleur REST**

Le **contrôleur** gère les routes et définit les endpoints de l'API. Modifie `posts.controller.ts` pour gérer les opérations CRUD de base.

Exemple de contrôleur REST pour les **posts** :
{% lien %}
   - [Contrôleur REST](https://github.com/MbayeSyAmar/Comment-integrer-des-API-REST-dans-NestJs.git)
{% endlien %} 

La section *Controllers* de la **documentation NestJS** m'a aidé à comprendre la structure des fichiers, les méthodes HTTP, et les annotations utilisées comme `@Controller` et `@Get`, avec un exemple concret d’un contrôleur simple sur GitHub, gérant des opérations CRUD dans **GitHub - NestJS Examples**, notamment dans la section `cats.controller.ts`. Les liens se trouvent dans la partie ressources.  

---

### **3. Implémenter la Logique Métier dans le Service**

Le fichier `posts.service.ts` contient la logique métier. C'est ici qu'on gère les interactions avec la base de données ou d'autres ressources.

Exemple de service pour gérer les posts en mémoire (avant d’ajouter MongoDB) :

{% lien %}
   - [Exemple de service](https://github.com/MbayeSyAmar/Comment-integrer-des-API-REST-dans-NestJs.git)
{% endlien %} 

En plus de **NestJS Documentation - Providers** qui explique comment injecter et structurer des services dans une application NestJS, j'ai consulté aussi **GitHub - NestJS Examples** la section `cats.service.ts` qui fournit un service fonctionnel pour gérer la logique métier.

---

### **4. Ajouter des DTOs pour Valider les Données**

Les DTOs (**Data Transfer Objects**) permettent de valider et de typer les données envoyées par le client.

Exemple de `create-post.dto.ts` :
{% lien %}
   - [Exemple de DTO](https://github.com/MbayeSyAmar/Comment-integrer-des-API-REST-dans-NestJs.git)
{% endlien %} 

La section *Controllers* de la **documentation NestJS** m'a aidé à comprendre la structure des fichiers, les méthodes HTTP, et les annotations utilisées comme `@Controller` et `@Get`, avec un exemple concret d’un contrôleur simple sur GitHub, gérant des opérations CRUD dans **GitHub - NestJS Examples**, notamment dans la section `cats.controller.ts`. Les liens se trouvent dans la partie ressources.  

---

### **5. Connecter une Base de Données (MongoDB)**

1. **Installer les Dépendances MongoDB** :
   - Installe Mongoose pour interagir avec une base MongoDB.
   ```bash
   npm install @nestjs/mongoose mongoose
   ```

2. **Configurer Mongoose dans le Module Principal** :
   - Modifie `app.module.ts` pour connecter NestJS à MongoDB.
   
   {% lien %}
   - [Configurer Mongoose](https://github.com/MbayeSyAmar/Comment-integrer-des-API-REST-dans-NestJs.git)
{% endlien %} 

3. **Définir un Schéma Mongoose pour les Posts** :
   - Ajoute un fichier `post.schema.ts` dans le dossier `posts`.
   
{% lien %}
   - [Définir un Schéma](https://github.com/MbayeSyAmar/Comment-integrer-des-API-REST-dans-NestJs.git)
{% endlien %}

4. **Lier le Modèle au Module Post** :
   - Modifie `posts.module.ts` pour inclure le schéma.
   
   {% lien %}
   - [Lier le Modèle au Module](https://github.com/MbayeSyAmar/Comment-integrer-des-API-REST-dans-NestJs.git)
{% endlien %}

5. **Adapter le Service pour Utiliser MongoDB** :
   - Modifie `posts.service.ts` pour interagir avec MongoDB via Mongoose.
   
    {% lien %}
   - [Adapter le Service](https://github.com/MbayeSyAmar/Comment-integrer-des-API-REST-dans-NestJs.git)
{% endlien %}

Avec **NestJS Documentation - Databases** et **GitHub - MongoDB with NestJS**, j'ai pu comprendre comment connecter MongoDB à une application NestJS avec Mongoose, définir des schémas et utiliser des modèles avec un projet complet montrant l'intégration de MongoDB. Les liens se trouvent dans la partie sources.  

---

### **5. Ajouter Swagger pour Documenter les API**

1. **Installer le Module Swagger** :
   ```bash
   npm install @nestjs/swagger
   ```

2. **Configurer Swagger dans `main.ts`** :
    
      {% lien %}
   - [Configurer Swagger](https://github.com/MbayeSyAmar/Comment-integrer-des-API-REST-dans-NestJs.git)
{% endlien %}

3. **Ajouter des Décorateurs dans les DTOs** :
 {% lien %}
   - [Ajouter des Décorateurs](https://github.com/MbayeSyAmar/Comment-integrer-des-API-REST-dans-NestJs.git)
{% endlien %}

Pour comprendre cette partie, j'ai consulté  **GitHub - Swagger Integration Example**, qui fournit un exemple complet avec Swagger intégré pour documenter l’API.  

---
{% details "Ce que j'ai appris" %}

Voici un résumé de ce que j'ai compris sur NestJS :
| **Composant**                     | **Rôle**                                                                                                           |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| **API REST**                       | Fournir une interface standardisée pour échanger des données entre le backend NestJS et les clients.                |
| **Nest CLI**                       | Générer automatiquement les fichiers nécessaires (contrôleurs, services, modules, DTOs) pour une ressource REST.    |
| **Contrôleurs** (`posts.controller.ts`) | Gérer les routes et définir les endpoints de l'API pour effectuer les opérations CRUD.                             |
| **Services** (`posts.service.ts`)  | Contenir la logique métier, gérer les interactions avec la base de données ou d'autres ressources.                  |
| **DTOs**                           | Valider et typer les données envoyées par le client pour sécuriser et structurer les entrées.                       |
| **MongoDB avec Mongoose**          | Fournir une base de données pour persister les données et définir des schémas avec Mongoose.                        |
| **Swagger**                        | Documenter l'API, facilitant la compréhension et l'utilisation par les développeurs tiers.    |
{% enddetails %}

---

## **Horodatage**
Voici a peu pret (pas exactement car des fois ca depasse de quelque minutes) comment organiser mon temps d'etude pour ce MON.
| **Étape**                                                                                                 | **Durée** |
|----------------------------------------------------------------------------------------------------------|-----------|
| Comprendre ce qu'est une API REST et comment elle fonctionne dans un contexte pratique                   | 1h30 min    |
| Découvrir les outils  : MongoDB et Swagger et savoir pourquoi ils sont utiles | 1h    |
| Configuration NestJS : Créer une ressource, un contrôleur, un service, et des DTOs              | 1h        |
| S'entraîner à connecter MongoDB avec NestJS : Installer, configurer, créer des schémas et utiliser les services | 1h        |
| Voir comment documenter une API avec Swagger : Installation et utilisation des décorateurs         | 30 min    |
| Revision React : Comprendre comment appeler une API avec Axios, créer un service API et afficher des données | 1h15 min        |
| Voir des techniques comme: Gérer les appels API avec cache et synchronisation automatique | 1h        |
| Comprendre comment gérer l'état global avec Redux pour partager les données de l'API entre plusieurs composants | 1h        |
| Rédaction sur le site | 1h25 min        |


## Sources :
{% lien %}
- [NestJS Documentation - Controllers](https://docs.nestjs.com/controllers)
- [GitHub - NestJS Examples](https://github.com/nestjs/nest/tree/master/sample/01-cats-app)
- [NestJS Documentation - Providers](https://docs.nestjs.com/providers)
- [GeeksForGeeks - NestJS DTOs](https://www.geeksforgeeks.org/why-do-we-need-dtos-and-interfaces-both-in-nest-js/)
- [NestJS Documentation - Databases](https://docs.nestjs.com/recipes/prisma#set-the-database-connection)
- [GitHub - MongoDB with NestJS](https://github.com/nestjs/nest/tree/master/sample/06-mongoose)
- [GitHub - Swagger Integration Example](https://github.com/nestjs/nest/tree/master/sample/11-swagger)

{% endlien %}  
