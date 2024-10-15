---
layout: layout/mon.njk

title: "Que sont les API et comment les créer ?"
authors:
  - Manuela BARRETO

date: 2024-10-14

tags: 
  - "temps 1"

résumé: "Un MON traitant de la compréhension du concept d'API et sa création."
---

{% prerequis %}

Il est intéressant de comprendre ce qu'est HTTP et comment il fonctionne, mais ce n'est pas obligatoire.

{% endprerequis %}
{% lien %}

[APIs for Beginners 2023 - How to use an API (Full Course / Tutorial)](https://www.youtube.com/watch?v=WXsD0ZgxjRw) - Vidéo qui explique en termes simples ce qu'est une API et donne des exemples d'outils pour la tester.

[REST vs. SOAP](https://www.redhat.com/en/topics/integration/whats-the-difference-between-soap-rest) - Découvrez les deux principaux types d'API

[6 règles de l'API REST](https://appmaster.io/pt/blog/as-seis-regras-de-descanso-apis) - Pouvoir lister les règles REST

[Quelle est la différence entre REST et RESTful](https://stackoverflow.com/questions/1568834/whats-the-difference-between-rest-restful) - Comprendre la différence entre les concepts REST et RESTfull

[Authentification et autorisation dans les API Rest](https://www.youtube.com/watch?v=IVMccb2h9dw) - Comprendre la différence entre l'authentification et l'autorisation

[REST API - Versioning REST APIs](https://www.youtube.com/watch?v=42J4KMHUJjE) - Comprendre les principales méthodes de versionnement d'une API REST

[What Components are in a Request?](https://safe-software.gitbooks.io/fme-server-rest-api-training-2018/content/FMESERVER_RESTAPI1Overview/1.2.WhatComponentsAreInARequest.html) - Identifier les composants d'une requête

[Qu'est-ce que le test API ? Avantages, types et meilleures pratiques](https://www.astera.com/pt/type/blog/the-ultimate-guide-to-api-testing/) - Découvrez quels sont les types de tests d'API et leur importance

[Documentation d'API étape par étape](https://br.hubspot.com/blog/marketing/documentacao-de-api) - Apprendre les bonnes pratiques pour rédiger la documentation d'une API développée

{% endlien %}

# Sommaire

- [Objectif](#objectif)
- [Qu'est-ce qu'une API ?](#quest-ce-quune-api)
- [Composants d'une API et d'une Requête](#composants-dune-api-et-dune-request)
  - [Composants d'une API](#composants-dune-api)
  - [Composants d'une Requête](#composants-dune-requete)
  - [Différence entre les Composants de l'API et de la Requête](#difference-entre-les-composants-de-lapi-et-de-la-requete)
- [Normes API : REST X SOAP](#normes-api--rest-x-soap)
  - [REST](#rest)
  - [SOAP](#soap)
- [Authentification et Autorisation](#authentification-et-autorisation)
- [Versionnement d'API](#versionnement-dapi)
- [Tests d'APIs](#tests-dapis)
- [Erreurs et Exceptions dans les APIs](#erreurs-et-exceptions-dans-les-apis)
- [Documentation des APIs](#documentation-des-apis)

## Objectif <a id="objectif"></a>

L'objectif de ce document est de **fournir une compréhension claire et approfondie des APIs** pour les développeurs et les gestionnaires de projets informatiques. La maîtrise des APIs est cruciale dans le paysage technologique actuel, car elles permettent l'intégration de systèmes, la consommation de services externes et la création d'applications interopérables.

### Importance pour les Développeurs et les Gestionnaires

- **Pour les développeurs :** Comprendre les APIs est essentiel pour créer des solutions modernes qui communiquent avec différentes plateformes.
- **Pour les gestionnaires :** La connaissance des APIs permet de mieux coordonner les équipes techniques et de prendre des décisions stratégiques en matière d'intégration de systèmes.

Comme je ne sais pas encore quelle carrière je veux suivre, j'ai décidé d'étudier ce sujet, qui sera important pour tout choix que je ferai.

## Qu'est-ce qu'une API ? <a id="quest-ce-quune-api"></a>

Les **APIs** (Interfaces de Programmation d'Applications) sont des interfaces qui permettent d'accéder aux données et fonctionnalités d'une application ou d'un service. Elles jouent un rôle clé dans la communication entre différents systèmes ou applications, qu'ils soient internes ou externes.

### API vs UI

Pour mieux comprendre le rôle d'une API, comparons-la à une **UI** (Interface Utilisateur) :

- **UI :** C'est le pont entre l'utilisateur humain et le système. L'UI facilite les interactions de l'utilisateur avec une application.
- **API :** Elle fonctionne comme un pont entre différents systèmes, permettant à un logiciel d'envoyer et de recevoir des données.

Dans les deux cas, l'objectif est de simplifier l'interaction :

- **Pour l'utilisateur (UI) :** Interaction intuitive et fluide.
- **Pour les systèmes (API) :** Communication efficace et bien documentée.

## Composants d'une API et d'une Requête <a id="composants-dune-api-et-dune-request"></a>

### Composants d'une API <a id="composants-dune-api"></a>

Les **composants d'une API** définissent son fonctionnement et son interaction. Voici les principaux éléments :

- **Endpoints :** Chemins vers les ressources. Exemples :
  - `/utilisateurs` pour lister ou manipuler des utilisateurs.
  - `/produits` pour accéder aux produits.

- **Méthodes HTTP :** Actions sur les endpoints, telles que :
  - `GET` : Récupérer des données.
  - `POST` : Envoyer des données pour créer un nouvel élément.
  - `PUT` : Mettre à jour des données existantes.
  - `DELETE` : Supprimer des données.

- **En-têtes (Headers) :** Métadonnées accompagnant la requête, telles que `Content-Type`, `Authorization`, etc.

- **Codes de Statut :** Indiquent le résultat de la requête. Exemples :
  - `200 OK` : Requête réussie.
  - `404 Not Found` : Ressource non trouvée.

- **Corps (Body) :** Contenu de la requête ou de la réponse, utilisé pour envoyer ou recevoir des données, notamment avec les méthodes `POST` et `PUT`.

### Composants d'une Requête <a id="composants-dune-requete"></a>

Les **composants d'une requête** sont les éléments spécifiques utilisés lors d'un appel à l'API. Voici les principaux :

- **URL :** Adresse complète de l'endpoint, incluant éventuellement des paramètres. Ex. : `https://api.exemple.com/utilisateurs?statut=actif`.

- **Méthode HTTP :** Indique l'action effectuée (GET, POST, etc.).

- **En-têtes (Headers) :** Incluent des informations telles que :
  - `Authorization` : Jeton ou clé API.
  - `Content-Type` : Format des données envoyées (souvent `application/json`).

- **Corps de la Requête (Body) :** Données envoyées, utilisé avec `POST`, `PUT`, etc. Ex. pour créer un utilisateur :

  ```json
  {
      "nom": "Jean Dupont",
      "email": "jean.dupont@example.com"
  }
  ```

- **Code de Statut :** Indique si l'opération a réussi, comme `200 OK` ou `404 Not Found`.

### Différence entre les Composants de l'API et de la Requête <a id="difference-entre-les-composants-de-lapi-et-de-la-requete"></a>

La principale différence réside dans leur fonction :

- **Composants de l'API :** Décrivent la structure et les ressources disponibles.
- **Composants d'une requête :** Utilisés lors de l'interaction avec l'API.

## Normes API : REST X SOAP <a id="normes-api--rest-x-soap"></a>

Créer une API n'est pas simple. Les deux approches les plus courantes sont **SOAP** (Simple Object Access Protocol) et **REST** (Representational State Transfer).

### REST <a id="rest"></a>

REST est un ensemble de principes architecturaux pour la construction d'APIs. Les **APIs RESTful** reçoivent des requêtes via HTTP et renvoient des résultats souvent en JSON, un format léger et facilement interprétable.

#### Principes de REST

Pour qu'une API soit RESTful, elle doit suivre six lignes directrices architecturales :

1. **Client-Serveur :** Séparation entre le client et le serveur.
2. **Communications sans État (Stateless) :** Chaque requête contient toutes les informations nécessaires.
3. **Cacheabilité :** Facilite la mise en cache des réponses.
4. **Système en Couches :** Architecture séparée en plusieurs couches.
5. **Utilisation des Méthodes Standards et Interface Uniforme :**
   - **Identification des ressources :** URI unique pour chaque ressource, ex. : `/clients/{id}`.
   - **Manipulation par représentations :** Utilisation de JSON/XML pour les échanges de données.
   - **Messages autodescriptifs :** Chaque requête doit être suffisamment informative.
   - **HATEOAS (Hypermedia as the Engine of Application State) :** Navigation dynamique via hyperliens.

6. **Code à la Demande (optionnel) :** Possibilité pour le serveur de fournir du code exécutable au client.

### SOAP <a id="soap"></a>

SOAP est un protocole formel utilisé pour la communication entre applications de langages et de plateformes différents. Bien que plus rigide et complexe, il offre une sécurité et une standardisation avancées, ce qui le rend adapté pour des cas d'utilisation critiques, comme les applications bancaires. La sortie est toujours en **XML**.

## Authentification et Autorisation <a id="authentification-et-autorisation"></a>

L'authentification et l'autorisation sont deux concepts très importants dans le monde des API. L'authentification concerne votre identité et, lorsque nous parlons d'API RESTful, nous parlons d'une architecture sans état, ce qui signifie que cette authentification doit être transmise dans l'en-tête de l'API chaque fois qu'elle est nécessaire. L'autorisation fait référence à la permission. Une fois que vous avez été authentifié, êtes-vous autorisé à faire la demande que vous souhaitez ?

Il est donc évident que ces deux éléments sont essentiels à la sécurité de l'API, car ils garantissent que seuls les utilisateurs ou systèmes autorisés ont accès aux ressources sensibles. Il existe plusieurs approches pour mettre en œuvre ces mécanismes, mais il s'agit d'un sujet complexe en soi qui devrait être exploré en profondeur dans le cadre d'un MON à part entière.

## Versionnement d'API <a id="versionnement-dapi"></a>

Le versionnage de l'API est une pratique essentielle dans le développement d'applications qui permet l'évolution continue d'une API sans rompre la compatibilité avec les clients existants. Lorsque de nouvelles fonctionnalités sont ajoutées ou que des modifications sont apportées à la structure des données, le versionnement permet de gérer ces changements de manière organisée.

Les méthodes les plus courantes de versionnement des API RESTful sont les suivantes :

- **Versionnement du chemin URI** : Les clients incluent la version de l'API dans l'URL, par exemple `api/v1/auteurs`. Cette approche est intuitive et permet aux développeurs d'identifier facilement la version de l'API qu'ils utilisent.

- **Chaîne de requête du paramètre URI Versioning** : Dans ce cas, la version souhaitée est indiquée en tant que paramètre de la chaîne de requête, par exemple `api/authors?v=1.1`.

- **URI Parameter Versioning acceat header** : Ici, l'URL ne change pas. La version souhaitée est indiquée dans l'en-tête `Accept`, par exemple `Accept: application/app.v1.categories`.

## Tests d'APIs <a id="tests-dapis"></a>

Toujours dans le cadre du développement d'APIs, les **tests d'APIs** constituent une étape cruciale, garantissant que l'API fonctionne comme prévu, qu'elle soit fiable, sécurisée et évolutive. Étant donné que les APIs sont souvent la base de la communication entre différents services et applications, leur stabilité est essentielle pour assurer le bon fonctionnement de l'ensemble du système. 

### Types de Tests d'API

Il existe plusieurs types de tests d'API, chacun se concentrant sur des aspects spécifiques de l'API. Explorons les principaux types de tests :

### **1. Tests Fonctionnels**
Les tests fonctionnels vérifient si les points de terminaison (endpoints) de l'API répondent correctement aux requêtes et renvoient les résultats attendus. 

- **Exemple** : Tester si l'endpoint `/users/123` renvoie les informations correctes pour l'utilisateur ayant l'ID 123.

### **2. Tests d'Intégration**
Les tests d'intégration garantissent que l'API peut communiquer correctement avec d'autres services, bases de données ou systèmes externes. 

- **Exemple** : Vérifier si une API de paiement interagit correctement avec un système bancaire pour traiter les transactions.

### **3. Tests de Performance (ou de Charge)**
Ces tests évaluent comment l'API se comporte dans différentes conditions d'utilisation, y compris des pics de trafic. 

- **Exemple** : Envoyer des milliers de requêtes simultanées à l'endpoint `/orders` et mesurer le temps de réponse.

### **4. Tests de Sécurité**
Les tests de sécurité vérifient si l'API est correctement protégée contre les menaces telles que les attaques par injection de code et l'accès non autorisé.

- **Exemple** : Tester si une API ne permet qu'aux utilisateurs autorisés d'accéder à certaines ressources.

### **5. Tests de Validation des Données**
Ces tests garantissent que l'API valide correctement les entrées des utilisateurs.

- **Exemple** : Envoyer un email invalide dans le champ d'inscription et vérifier si l'API renvoie une erreur appropriée.

### **6. Tests de Fiabilité (ou de Stabilité)**
Ces tests vérifient comment l'API se comporte sur de longues périodes d'utilisation continue.

- **Exemple** : Exécuter une série de requêtes sur une longue période et surveiller le comportement de l'API.

### **7. Tests de Compatibilité**
Ces tests garantissent que l'API fonctionne correctement dans divers environnements et systèmes d'exploitation.

- **Exemple** : Vérifier si l'API fonctionne correctement sur différentes versions de systèmes d'exploitation ou de navigateurs.

### **Outils pour les Tests d'APIs**
Plusieurs outils facilitent le processus de tests d'APIs, permettant à la fois des tests manuels et automatiques. Voici quelques-uns des outils les plus couramment utilisés :

- **Postman** : Permet la création, l'envoi et l'analyse des requêtes de manière conviviale.

- **Insomnia** : Un outil axé sur la simplicité pour tester des APIs REST et GraphQL.

- **JMeter** : Utilisé pour les tests de charge et de performance.

- **SoapUI** : Prend en charge les tests d'APIs REST et SOAP, offrant des fonctionnalités avancées.

## Erreurs et Exceptions dans les APIs <a id="erreurs-et-exceptions-dans-les-apis"></a>

Le traitement approprié des **erreurs et exceptions** est fondamental dans le développement d'APIs robustes. Une bonne gestion des erreurs implique le retour de **codes de statut HTTP** appropriés et l'affichage de messages d'erreur détaillés.

### **Codes de Statut HTTP**
Les APIs RESTful utilisent des codes de statut HTTP pour indiquer le succès ou l'échec d'une opération. Ces codes peuvent être regroupés comme suit :

- **Codes de Succès (2xx)** : Indiquent que la requête a été traitée avec succès.

- **Codes d'Erreur du Client (4xx)** : Indiquent un problème avec la requête envoyée par le client.

- **Codes d'Erreur du Serveur (5xx)** : Indiquent qu'une erreur est survenue sur le serveur.

### **Messages d'Erreur Detaillés**
Les APIs doivent fournir des messages d'erreur informatifs dans le corps de la réponse.

- **Description de l'erreur** : Indiquer ce qui a causé l'erreur.
- **Code d'erreur** : Un code spécifique pour aider à identifier l'erreur.
- **Suggestions de correction** : Des orientations sur la façon de corriger l'erreur.

**Exemple de réponse JSON pour une erreur 400 :**
```json
{
  "error": "Bad Request",
  "message": "Le champ 'email' est obligatoire.",
  "code": 400,
  "timestamp": "2024-10-14T12:00:00Z"
}
```

### **Traitement des Exceptions sur le Serveur**
Le traitement des exceptions est responsable de la capture des erreurs inattendues. Les exceptions internes doivent être enregistrées, mais jamais envoyées directement au client.

### **Bonnes Pratiques de Traitement des Erreurs**
1. **Consistance** : Suivre un modèle cohérent de retour d'erreurs.
2. **Sécurité** : Éviter de révéler des informations sensibles dans les erreurs.
3. **Documentation** : Documenter les types d'erreurs que l'API peut retourner.

## Documentation des APIs <a id="documentation-des-apis"></a>

La documentation des APIs est un composant vital qui garantit l'utilisabilité et la compréhension du fonctionnement de l'API. 

### **Importance de la Documentation**
1. **Facilité d'Utilisation** : Permet aux développeurs de comprendre rapidement comment interagir avec l'API.
2. **Minimisation des Erreurs** : Aide à éviter des erreurs courantes.
3. **Facilitation de la Maintenance** : Ressource précieuse lors de la maintenance de l'API.
4. **Soutien à l'Intégration** : Guide pour les développeurs tiers.

### **Composants d'une Bonne Documentation d'API**
Une documentation efficace doit inclure les composants suivants :

- **Vue d'Ensemble de l'API** : Introduction au but et aux fonctionnalités de l'API.
- **Authentification et Autorisation** : Méthodes d'authentification nécessaires.
- **Endpoints** : Liste de tous les endpoints disponibles.
- **Paramètres et Données** : Détails sur les paramètres d'entrée et de sortie.
- **Codes de Statut** : Explication des codes de statut HTTP.
- **Exemples Pratiques** : Exemples de requêtes et de réponses.
- **Guide des Erreurs** : Répertorie les erreurs courantes et leurs solutions.

Une documentation bien élaborée est un guide qui oriente les développeurs dans l'utilisation efficace de l'API, assurant une expérience positive et productive.

## Conclusion

Dans ce travail, j'ai exploré les principaux aspects du développement d'APIs, tels que l'authentification, l'autorisation, le versionnement, les tests et la documentation. J'ai appris qu'il est essentiel de créer des APIs robustes pour garantir la sécurité et la fiabilité des systèmes. Le traitement adéquat des erreurs et une documentation claire facilitent l'intégration et l'utilisation par les développeurs.

Face à l'importance croissante des APIs dans la technologie actuelle, il est crucial d'adopter de bonnes pratiques pour améliorer l'expérience utilisateur et renforcer la compétitivité des organisations. À l'avenir, je prévois d'approfondir mes études dans des domaines tels que les tests automatisés et l'intégration continue, afin d'améliorer encore ma compréhension et mes compétences dans le développement d'APIs.

