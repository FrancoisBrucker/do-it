---
layout: layout/pok.njk

title: "Un forum de discussion avec React pour le front-end et NestJS pour le back-end"
authors:
  - Serigne Mbaye Sy AMAR

date: 2024-10-18
tags: 
  - "temps 2"
  - "NestJs"
  - "React"
  - "API Rest"
  - Forum

résumé: Le but de ce POK est de mettre en évidence les connaissances que j’ai acquises durant l’ensemble de mes MONs, en créant un forum de discussion avec React comme front-end et NestJS comme back-end, en utilisant bien évidemment les API Rest pour la connexion entre les deux.
---

{% prerequis %}

- Une base en NestJs 
- Une Base en React 
- Une base solide aux apis Rest 
{% endprerequis %}
{% lien %}

Les lien utiles pour la compréhension de celui-ci:
- [Mon Mon 1.1](https://francoisbrucker.github.io/do-it/promos/2024-2025/Amar-Mbaye/mon/temps-1.1/)
- [Mon Mon 2.1](https://francoisbrucker.github.io/do-it/promos/2024-2025/Amar-Mbaye/mon/temps-2.1/)
- [Mon MON 2.2](https://francoisbrucker.github.io/do-it/promos/2024-2025/Amar-Mbaye/mon/temps-2.2/)

{% endlien %}

<!-- table des matieres -->
## Table des matières<a name="table-des-matières"></a>

- [Table des matières](#table-des-matières)
  - [**Présentation du Projet : Forum de Discussion**](#présentation-du-projet--forum-de-discussion)
  - [**Outils et Méthodes Utilisées**](#outils-et-méthodes-utilisées)
    - [**1. Méthodologie Agile : Sprint Planning**](#1-méthodologie-agile--sprint-planning)
    - [**2. Horodatage**](#2-horodatage)
    - [**3. Étude Post-Mortem**](#3-étude-post-mortem)
    - [**Sprint 1 : Frontend et Maquette**](#sprint-1--frontend-et-maquette)
    - [**Sprint 2 : Backend et Intégration**](#sprint-2--backend-et-intégration)
  - [**Architecture et Fonctionnalités**](#architecture-et-fonctionnalités)
    - [**1. Fonctionnalités Clés du Forum**](#1-fonctionnalités-clés-du-forum)
    - [**2. Architecture du Projet**](#2-architecture-du-projet)
- [Résultat (Sous format de vidéo)](#résultat-sous-format-de-vidéo)
- [Sources :](#sources-)


### **Présentation du Projet : Forum de Discussion**
Pour ce projet, je vise à développer un forum de discussion où les utilisateurs peuvent partager des idées, poser des questions, et échanger des avis.

**Objectif :**  
Créer un forum de discussion où je vais:  

- Permettre aux utilisateurs de poster leurs questions ou réflexions.
- Offrir une fonctionnalité de commentaires pour interagir avec les discussions existantes.
- Intégrer des fonctionnalités supplémentaires comme les likes et le partage des posts. 

**Technologies utilisées :**  
- **Frontend** : React.js  
- **Backend** : NestJS  
- **Base de données** : MongoDB  
- **API REST** : Pour la communication entre le frontend et le backend.  

---

### **Outils et Méthodes Utilisées**

#### **1. Méthodologie Agile : Sprint Planning**


- **Sprint 1 : Frontend et Maquette**  
  - [x] Création de la maquette du forum (UX/UI) [(lien vers la maquette)](https://www.figma.com/design/6EleCT87Blb4ecdAUifrFx/forum?t=404V5TOHt19Sr2Qc-1)
  - [x] Développement des composants frontend en React.js.  
  - [x] Configuration initiale des interactions utilisateur (ajouter un post, afficher des posts).  

- **Sprint 2 : Backend et Intégration**  
  - [x] Mise en place du backend avec NestJS.  
  - [x] Implémentation des endpoints API REST pour gérer les posts, commentaires et likes.  
  - [x] Intégration frontend-backend pour synchroniser les fonctionnalités.

---

#### **2. Horodatage**


| Sprint      | Étapes                          | Temps Alloué | Description                                                                 |
|-------------|-------------------------------------|--------------|-----------------------------------------------------------------------------|
| **Sprint 1** | Création de la maquette (UX/UI)    | **3h**       | Conception de la maquette du forum                       |
|             | Développement du frontend          | **5h**      | Développement des composants React.js pour afficher et gérer les données.   |
|             | Test et ajustements frontend       | **2h**       | Débogage et amélioration de l'expérience utilisateur.                       |
| **Sprint 2** | Configuration du backend avec NestJS | **4h**      | Création des modules, services, et contrôleurs pour gérer les données.      |
|             | Connexion avec MongoDB             | **3h**       | Mise en place des modèles Mongoose et validation des données.               |
|             | Intégration frontend-backend       | **3h**       | Tests de communication via API REST et corrections des bugs rencontrés.     |

**Total :** 20 heures pour les deux sprints.  


---

#### **3. Étude Post-Mortem**
Après chaque sprint, j'ai effectué une **analyse post-mortem** pour évaluer ce qui a fonctionné, ce qui a été difficile et ce qui doit être amélioré.

#### **Sprint 1 : Frontend et Maquette**
- **Points forts :**
  - Une interface respectant la maquette initiale.
  - Modularité des composants React.js, qui facilite les modifications et les ajouts futurs.
- **Points faibles :**
  - Difficile d’anticiper les besoins exacts du backend, ce qui a nécessité des ajustements plus tard.
  - Probléme de PC trop lent
- **Leçons apprises :**
  - Mieux coordonner les spécifications entre le frontend et le backend dès le début.
-  **Améliorations :**
    - Développer un meilleur système de gestion d’état global (comme Redux ou Context API).
  
  {%info%}
Redux est un gestionnaire d'état global pour les applications React. Il permet de gérer l 'état de l'application de manière centralisée et de réduire la complexité des composants. 
{%endinfo%}

#### **Sprint 2 : Backend et Intégration**
- **Points forts :**
  - Les endpoints REST sont bien organisés (CRUD standardisé).

- **Points faibles :**
  - Gestion des erreurs CORS qui a ralenti l'intégration initiale.
  - Probléme de PC trop lent
  - Complexité dans la synchronisation des états entre le frontend et le backend.
- **Leçons apprises :**
  - Toujours prévoir du temps pour les tests d’intégration entre les différentes parties du projet.

  - **Améliorations :**
    - Ajouter des tests automatisés pour éviter les régressions.
  
   {% info %}
Les tests automatisés sont des scripts qui vérifient automatiquement que le code fonctionne comme prévu. Ils permettent de détecter les erreurs et les bugs rapidement et de garantir la qualité du code.
{% endinfo %}
 
 
---

### **Architecture et Fonctionnalités**

#### **1. Fonctionnalités Clés du Forum**
- **Posts** :
  - Les utilisateurs peuvent créer, lire, modifier et supprimer des posts (CRUD).
  - Les posts sont affichés avec leur titre et contenu.

- **Commentaires** :
  - Chaque post peut recevoir des commentaires.
  - Les utilisateurs peuvent ajouter .

- **Interactions** :
  - Les utilisateurs peuvent liker et partager des posts.

#### **2. Architecture du Projet**
Le projet est divisé en plusieurs couches.

- **Frontend** (React.js) :
  - Composants principaux :
    - **MainContent** : Affiche la liste des posts.
    - **Editor** : Permet à l’utilisateur de créer un post.
    - **QuestionListItem** : Gère les interactions avec un post (likes, commentaires).

- **Backend** (NestJS) :
  - Modules :
    - **PostsModule** : Gère les endpoints pour les posts.
    - **CommentsModule** : Gère les endpoints pour les commentaires.
  - Modèles Mongoose :
    - **Post** : Définit la structure d’un post dans MongoDB (titre, contenu).
    - **Comment** : Définit la structure d’un commentaire (contenu, post associé).

---

## Résultat (Sous format de vidéo)
<!-- integrer video .mp4 --> 
<video controls>
 <source src="./Resultat.mp4" type="video/mp4">
</video>

## Sources :
{% lien %}
- [Mon Mon 1.1](https://francoisbrucker.github.io/do-it/promos/2024-2025/Amar-Mbaye/mon/temps-1.1/)
- [Mon Mon 2.1](https://francoisbrucker.github.io/do-it/promos/2024-2025/Amar-Mbaye/mon/temps-2.1/)
- [Mon MON 2.2](https://francoisbrucker.github.io/do-it/promos/2024-2025/Amar-Mbaye/mon/temps-2.2/)

{% endlien %}  
