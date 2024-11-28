---
layout: layout/projet.njk

title: "JukeBox"
authors:
  - Loïck Goupil-Hallay
  - Sofiane Ouadda
  - Thomas Merle
  - Mathis Adinolfi

date: 2024-09-19

tags:
  - "IA"
  - "dev"
  - "web"
  - "golang"
  - "musique"
  - "Vue.js"

résumé: Génération interactive de musique en direct
---

{%prerequis '**Projet avancé**'%}
- [Golang](https://golang.org/)
- [Vue.js](https://vuejs.org/)
{%endprerequis%}

{% lien '**Liens utiles**' %}
- [Repository GitHub](https://github.com/boxboxjason/jukebox)
{% endlien %}

## Brief
L'objectif du projet est de permettre aux utilisateurs de **générer de la musique de manière collaborative**. Cette génération de musique passe par l'intermédiaire d'un **chat en live** qui permet aux utilisateurs de donner des instructions à une **IA** qui modifiera la musique *en cours de lecture*.

## Technical

### Génération de musique
La musique est générée par un modèle d'**intelligence artificielle** nommé [RAVE](https://forum.ircam.fr/projects/detail/rave-vst/).\
Il s'agit d'un **auto-encoder** qui prend en entrée des fichiers audios et les modifie en fonction des instructions données. Ce correspond parfaitement à notre besoin car il permet de **générer de la musique en temps réel**, et les paramètres de la musique peuvent être contrôlés en temps réel.

### Filtrage et modération du chat
Le chat est modéré par un **filtre de grossièretés** (de type regex) et de spam.\
Le chat est également modéré par un **filtre IA** qui détecte les messages à caractère nocif pour l'IA générateur de musique. Ce filtre IA se charge de détecter les messages destinés à la génération de musique, les **reformule si besoin** et les transmet au générateur s'ils sont valides.

### Frontend
Le frontend est développé en **Vue.js**. Il **communique avec le backend** via son API REST pour la plupart des requêtes de fonctionnement. Une communication **websocket** est mise en place pour le chat en live ainsi que pour le streaming de musique.

#### Fonctionnalités
- Chat en live
- Création de compte utilisateur
- Connexion à un compte utilisateur
- Affichage des paramètres actuels de la musique
- Affichage responsive, adapté à tous les écrans

### Backend
Le backend est développé en **Golang**, il expose une **API REST** pour remplir toutes ses fonctionnalités. Il s'agit d'un **serveur HTTP** qui gère les requêtes utilisateurs et les transmet à l'IA générateur de musique.

#### Fonctionnalités
- Gestion des utilisateurs (création, stockage, connexion)
- Gestion sécurisée de l'authentification
- Gestion des messages du chat (via websocket et API REST, stockage en base de données)
- Filtrage des messages du chat
- Communication avec l'IA générateur de musique
- Réceptions des requêtes frontend et envoi des réponses
