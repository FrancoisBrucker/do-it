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

Le but de ce MON est d'acquérir des compétences sur les API REST afin de pouvoir les utiliser dans mon POK. Veuillez consulter mon POK (sous format de lien) pour une application directe de tout ce que nous allons aborder dans ce MON, qui sera divisé en deux grandes questions : comment intégrer les API REST dans NestJS, puis comment intégrer les API REST dans React.  

## Introduction :

Cette première partie du MON (la base), à savoir qu'est-ce qu'une API et son fonctionnement, a été traitée de manière très explicite par Baptiste Audouin dans son [MON Temps 1](https://francoisbrucker.github.io/do-it/promos/2024-2025/Baptiste-Audouin/mon/temps-1.1/).  

Pour répondre aux besoins spécifiques de mon POK (sous format de lien), je vais me concentrer davantage sur des aspects concrets : comment utiliser une API REST dans un projet intégrant un backend développé avec NestJS et un frontend avec React.  

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

Le fichier `posts.service.ts` contient la logique métier. C'est ici que tu gères les interactions avec la base de données ou d'autres ressources.

Exemple de service pour gérer les posts en mémoire (avant d’ajouter MongoDB) :

{% lien %}
   - [Exemple de service](https://github.com/MbayeSyAmar/Comment-integrer-des-API-REST-dans-NestJs.git)
{% endlien %} 

En plus de **NestJS Documentation - Providers** qui explique comment injecter et structurer des services dans une application NestJS, j'ai consulte aussi **GitHub - NestJS Examples** la section `cats.service.ts` qui fournit un service fonctionnel pour gérer la logique métier.

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

### **6. Ajouter Swagger pour Documenter les API**

1. **Installer le Module Swagger** :
   ```bash
   npm install @nestjs/swagger
   ```

2. **Configurer Swagger dans `main.ts`** :
    
      {% lien %}
   - [Configurer Swagger](https://github.com/MbayeSyAmar/Comment-integrer-des-API-REST-dans-NestJs.git)
{% endlien %}

3. **Ajouter des Décorateurs dans les DTOs** :
  (lien github ici)
 {% lien %}
   - [Ajouter des Décorateurs](https://github.com/MbayeSyAmar/Comment-integrer-des-API-REST-dans-NestJs.git)
{% endlien %}

Pour comprendre cette partie, j'ai consulté  **GitHub - Swagger Integration Example**, qui fournit un exemple complet avec Swagger intégré pour documenter l’API.  

---
## **Comment intégrer des API REST dans React ?**
<!-- 

## **Comment intégrer des API REST dans React ?**

L'intégration des API REST dans un projet React repose principalement sur l'utilisation d'outils comme **`fetch`**, **`axios`**, et des hooks comme **`useEffect`** pour interagir avec le backend. Voici une démarche étape par étape.

Pour avoir la base sur React, vous pouvez consulter mon MON (1.1).

---

### **1. Configurer un Service API dans React**

La meilleure pratique consiste à créer un fichier dédié pour centraliser les appels API, afin d'éviter les répétitions dans les composants.

#### **Créer un Service API avec `axios`**

1. **Installer `axios` :**

   ```bash
   npm install axios
   ```

2. **Créer un fichier `api.js`** dans le dossier `src/services`. 

#### Exemple : api.js

   {% lien %}
   - [Exemple de service API](https://github.com/MbayeSyAmar/Comment-integrer-des-API-REST-dans-React.git)
{% endlien %} 


   

---

### **2. Appeler une API dans un Composant React**

Utilise `axios` pour appeler les API depuis React.

#### Exemple : Afficher la Liste des Posts

1. **Créer un composant `PostList.js` :**

     {% lien %}
  - [Exemple de composant](https://github.com/MbayeSyAmar/Comment-integrer-des-API-REST-dans-React.git)
{% endlien %} 

---


### **3. Sécuriser les Requêtes avec JWT**

1. **Gérer l’Authentification** :

   - Lors de la connexion, récupère le **token JWT** depuis l’API NestJS et stocke-le dans le **localStorage**.

     {% lien %}
  - [Exemple de gestion de l'authentification]([https://github.com/your-username /your-repo/blob](https://github.com/MbayeSyAmar/Comment-integrer-des-API-REST-dans-React.git))
{% endlien %} 

1. **Vérifier les Permissions** dans les Composants :

   - Vérifie la présence du token pour afficher ou masquer certains éléments.

     {% lien %}
     - [Exemple de vérification de permissions]([https://github.com/your-username/your-re po/blob](https://github.com/MbayeSyAmar/Comment-integrer-des-API-REST-dans-React.git))
{% endlien %} 

---


### **4. Optimiser l’Intégration**

- **Mémoisation avec React Query** :
   - Remplace `useEffect` par [React Query](https://tanstack.com/query/latest) pour gérer les appels API avec cache et synchronisation automatique.

- **Gestion d’État Global avec Redux** :
   - Centralise les données des API REST dans un store Redux pour les partager entre plusieurs composants.

### **Horodatage**
Voici a peu pret (pas exactement car des fois ca depasse de quelque minutes) comment organiser mon temps d'etude pour ce MON.
| **Étape**                                                                                                 | **Durée** |
|----------------------------------------------------------------------------------------------------------|-----------|
| Comprendre ce qu'est une API REST et comment elle fonctionne dans un contexte pratique                   | 30 min    |
| Découvrir les outils essentiels : NestJS, React, MongoDB, et Swagger, et savoir pourquoi ils sont utiles | 30 min    |
| Apprendre à configurer NestJS : Créer une ressource, un contrôleur, un service, et des DTOs              | 1h        |
| S'entraîner à connecter MongoDB avec NestJS : Installer, configurer, créer des schémas, et utiliser les services | 1h        |
| Découvrir comment documenter une API avec Swagger : Installation et utilisation des décorateurs         | 30 min    |
| Revision React : Comprendre comment appeler une API avec Axios, créer un service API, et afficher des données | 1h        |
| Apprendre à sécuriser les requêtes avec JWT dans React                                                   | 30 min    |
| Explorer des techniques comme: Gérer les appels API avec cache et synchronisation automatique | 1h        |
| Comprendre comment gérer l'état global avec Redux pour partager les données de l'API entre plusieurs composants | 1h        |
| Réviser et pratiquer : Ajuster les concepts appris et les appliquer à des projets concrets              | 1h        |

-->

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
