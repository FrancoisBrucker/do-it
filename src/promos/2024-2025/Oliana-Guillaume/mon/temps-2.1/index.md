---
layout: layout/mon.njk

title: "Introduction à Firebase"
authors:
  - Ton Nom

date: 2024-11-15

tags: 
  - "Firebase"
  - "Backend"
  - "JavaScript"
  - "Database"
  - "HTML/CSS"

résumé: "Un MON pour découvrir Firebase, comprendre ses fonctionnalités, et réaliser une mini-application d'authentification en JavaScript Vanilla avec une base de données."
---

{% prerequis %}

Avoir des notions de base en programmation HTML et JavaScript. Pas besoin de connaître Firebase ou les bases de données à l'avance.

{% endprerequis %}

{% lien %}

Quelques liens utiles pour en savoir plus :

- [Documentation Firebase](https://firebase.google.com/docs)
- [Introduction à Firebase (Guide officiel)](https://firebase.google.com/start)
- [MDN Web Docs - JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

{% endlien %}

---

# Sommaire : Découverte de Firebase et Projet Pratique

## 1. Comprendre Firebase
- **1.1 C'est quoi Firebase ?**
- **1.2 Ses principales fonctionnalités**
- **1.3 Pourquoi l’utiliser et dans quels cas ?**

## 2. Passer à la pratique
- **2.1 Configurer Firebase pour votre projet**
- **2.2 Développer une mini-app d'authentification avec base de données**
- **2.3 Ce que vous obtenez à la fin (et la suite possible)**

---

# 1. Comprendre Firebase

## 1.1 C'est quoi Firebase ?

Firebase, c’est un outil proposé par Google qui permet aux développeurs de se concentrer sur la création de leur application sans devoir gérer un serveur complexe. En gros, ça permet de ne pas se casser la tête à gérer soit même un serveur, c'est pratique, surtout quand on sait pas faire. 
Plus concrètement, c’est ce qu’on appelle une plateforme **"Backend-as-a-Service" (BaaS)**. En résumé, tout ce qui est backend (base de données, gestion des utilisateurs, stockage de fichiers) est déjà prêt, vous n’avez qu’à l’utiliser.




<div style="display: flex; flex-direction: column; align-items: center; margin: 20px;">
  <a href="https://www.youtube.com/watch?v=p9pgI3Mg-So">
    <img src="https://img.youtube.com/vi/p9pgI3Mg-So/hqdefault.jpg" alt="Miniature de la vidéo" width="560">
  </a>
  <h2>Vidéo explicative complète du fonctionnement de Firebase</h2>
</div>



### Pourquoi c’est génial ?
- **Facile à démarrer** : En quelques clics, votre projet est configuré.
- **Pas besoin de serveur** : Pas besoin d’acheter, configurer, et maintenir un serveur.
- **Flexible et scalable** : Parfait pour les petits projets, mais ça peut aussi gérer des millions d’utilisateurs.

---

### 1.2 Les principaux outils proposés par Firebase

Firebase est une plateforme complète de services cloud qui permet aux développeurs de créer, gérer et faire évoluer leurs applications rapidement, sans avoir besoin de gérer une infrastructure complexe. Voici les outils les plus populaires qu’elle propose, accompagnés d’exemples concrets.

---

#### 1.2.1 Firebase Authentication

**Description :**  
Firebase Authentication est un service qui permet de gérer facilement l'inscription, la connexion et la gestion des utilisateurs. Il prend en charge plusieurs méthodes d'authentification :
- Email et mot de passe.
- Authentification via fournisseurs tiers (Google, Facebook, Twitter, GitHub, etc.).
- Connexion anonyme.
- Téléphone/SMS.

**Cas d’utilisation :**  
- Une application de réseau social où les utilisateurs peuvent se connecter avec leurs comptes Google ou Facebook.  
- Une plateforme de commerce en ligne nécessitant une inscription pour gérer les commandes.

**Exemple concret :**  
Imaginons une application de recettes. Firebase Auth permettrait aux utilisateurs de créer un compte avec leur email pour enregistrer leurs recettes favorites. Comme on va le voir ensuite, c'est facile à mettre en place, et c'est un gain de temps considérable pour le développeur qui ne voudrait pas se casser la tête à configurer le systeme d'authentification lui-même, ou tout simplement qui n'aurait pas les compétences pour le faire (mon cas).


---

#### 1.2.2 Cloud Firestore (Base de données NoSQL)

**Description :**  
Cloud Firestore est une base de données NoSQL entièrement managée qui synchronise les données en temps réel entre les utilisateurs et le backend. Ses fonctionnalités incluent :
- Structure en **documents** et **collections**, ce qui la rend flexible et facile à organiser.
- Synchronisation en temps réel.
- Requêtes complexes, tri et filtres.

**Cas d’utilisation :**  
- Une application de chat où les messages s’affichent instantanément.  
- Une application de gestion de tâches où les modifications sont synchronisées en temps réel entre plusieurs appareils.

**Exemple concret :**  
Dans une application de tableau blanc collaboratif, Firebase Firestore pourrait stocker les dessins et les positions des éléments. Dès qu'un utilisateur dessine, les autres voient les changements instantanément.

---

#### 1.2.3 Firebase Hosting

**Description :**  
Firebase Hosting est un service d'hébergement rapide et sécurisé pour les applications web. Il est conçu pour déployer facilement des fichiers HTML, CSS, JavaScript et autres actifs.

**Cas d’utilisation :**  
- Déploiement d'une Progressive Web App (PWA) ou d’un site vitrine.  
- Hébergement d'un projet de portfolio pour développeur.

**Exemple concret :**  
Un développeur front-end peut utiliser Firebase Hosting pour déployer son portfolio en quelques secondes, bénéficiant ainsi d’un SSL gratuit pour sécuriser son site.

---

#### 1.2.4 Cloud Functions

**Description :**  
Cloud Functions permet d'exécuter du code backend (Node.js) sans gérer de serveur. Ces fonctions s’exécutent en réponse à des événements (par exemple, ajout d’un document dans Firestore) ou via des appels HTTP.

**Cas d’utilisation :**  
- Automatisation d'envoi d'email lorsqu'un utilisateur s'inscrit.  
- Traitement de paiements en ligne via une intégration avec Stripe.

**Exemple concret :**  
Dans une application de réservation d’hôtel, une Cloud Function pourrait envoyer un email de confirmation lorsqu'une réservation est ajoutée dans Firestore.

---

#### 1.2.5 Firebase Realtime Database

**Description :**  
Firebase Realtime Database est une base de données NoSQL qui permet de synchroniser les données en temps réel entre les clients et le serveur. Contrairement à Firestore, elle stocke les données sous forme de JSON.

**Cas d’utilisation :**  
- Une application de suivi GPS en temps réel.  
- Une application de gestion d’inventaire où les stocks se mettent à jour instantanément.

**Exemple concret :**  
Dans une application de suivi de taxis, la Firebase Realtime Database pourrait afficher les positions des taxis en temps réel sur une carte.

---

#### 1.2.6 Firebase Storage

**Description :**  
Firebase Storage permet de stocker et de servir des fichiers volumineux (images, vidéos, documents) de manière sécurisée. Il s’intègre parfaitement avec Firebase Authentication pour gérer les permissions.

**Cas d’utilisation :**  
- Une application de gestion de documents où les utilisateurs peuvent uploader des fichiers PDF.  
- Une application de partage de photos entre amis.

**Exemple concret :**  
Dans une application de réseau social, Firebase Storage peut être utilisé pour stocker les photos de profil et les images partagées par les utilisateurs.

---

#### 1.2.7 Firebase Analytics

**Description :**  
Firebase Analytics est un outil puissant pour analyser le comportement des utilisateurs dans une application. Il fournit des rapports détaillés sur l’engagement, les événements personnalisés, et les performances.

**Cas d’utilisation :**  
- Analyse de l'utilisation des fonctionnalités d’une application mobile.  
- Suivi des clics sur les publicités dans une application de jeux.

**Exemple concret :**  
Une application de fitness pourrait utiliser Firebase Analytics pour suivre quelles séances d'entraînement sont les plus populaires et ajuster les futures fonctionnalités.

---

#### 1.2.8 Firebase Crashlytics

**Description :**  
Firebase Crashlytics est un outil de gestion des bugs. Il permet de détecter les crashs en temps réel, d’analyser leurs causes et d’envoyer des rapports détaillés.

**Cas d’utilisation :**  
- Détection de crashs dans une application mobile après une mise à jour majeure.  
- Surveillance d'une application en production pour identifier les bugs critiques.

**Exemple concret :**  
Dans une application de livraison, Crashlytics peut signaler un bug où l’application plante lorsqu’un utilisateur tente de suivre sa commande.

---

#### 1.2.9 Firebase Performance Monitoring

**Description :**  
Firebase Performance Monitoring aide à identifier les goulots d’étranglement dans les performances d’une application, que ce soit au niveau du réseau ou du rendu d’interface.

**Cas d’utilisation :**  
- Optimisation des temps de chargement dans une application web.  
- Analyse des performances réseau dans une application mobile.

**Exemple concret :**  
Une application de streaming vidéo pourrait utiliser Firebase Performance Monitoring pour repérer des temps de latence élevés lors du chargement des vidéos.

---

#### 1.2.10 Firebase Test Lab

**Description :**  
Firebase Test Lab est un outil de test qui permet d'exécuter des tests automatisés sur des appareils réels hébergés dans le cloud.

**Cas d’utilisation :**  
- Tester la compatibilité d'une application mobile sur différentes versions d’Android.  
- Identifier des bugs spécifiques à certains modèles de téléphones.

**Exemple concret :**  
Un développeur peut s’assurer qu'une application de jeu fonctionne correctement sur tous les principaux appareils Android avant une mise en production.

---

### Conclusion de cette section
Firebase est une boîte à outils complète, allant de l’authentification des utilisateurs à l’analyse des performances. Ces services permettent aux développeurs de se concentrer sur le développement des fonctionnalités de leur application sans se soucier de l’infrastructure ou des outils complexes.

Dans la prochaine section, nous mettrons en pratique certains de ces outils en construisant une mini-application JavaScript avec Firebase comme backend.

# 2. Passer à la pratique

On va maintenant utiliser Firebase pour créer une mini-application où les utilisateurs peuvent s’inscrire et se connecter. Le tout, directement en **JavaScript Vanilla**, sans frameworks complexes.

---

## 2.1 Configurer Firebase pour votre projet

1. **Créez un projet Firebase**  
   - Allez sur [Firebase Console](https://console.firebase.google.com).
   - Cliquez sur "Add Project", donnez-lui un nom, et suivez les étapes.

2. **Ajoutez une application web**
   - Une fois le projet créé, cliquez sur "Add App" et choisissez "Web".
   - Firebase vous donnera un objet de configuration comme celui-ci :
     ```javascript
     const firebaseConfig = {
       apiKey: "votre-api-key",
       authDomain: "votre-projet.firebaseapp.com",
       projectId: "votre-projet",
       storageBucket: "votre-projet.appspot.com",
       messagingSenderId: "1234567890",
       appId: "1:1234567890:web:abcdef123456"
     };
     ```

3. **Activez l’authentification par email/mot de passe**
   - Allez dans "Authentication" > "Sign-in Method".
   - Activez "Email/Password".

---

## 2.2 Développer une mini-app d'authentification

### Étape 1 : Installez Vite
Vite est un outil qui permet de démarrer rapidement un projet JavaScript. Pour l’installer :
```bash
npm create vite@latest mon-firebase-app --template vanilla
cd mon-firebase-app
npm install firebase

```


<div style = "display : flex; flex-direction: column; align-items : center; margin: 20px">
  <a href= "https://www.youtube.com/watch?v=_Xczf06n6x0&t=79s">
    <img src = "https://img.youtube.com/vi/Xczf06n6x0/hqdefault.jpg">

  </a>
  <h2>Tutoriel Youtube pour réaliser l'application simple avec authentification</h2>
</div>

