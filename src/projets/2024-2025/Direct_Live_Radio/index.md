---
layout: layout/projet.njk

title: "Direct Live Radio"
authors:
  - Loick Goupil-Hallay
  - Sofiane Ouadda
  - Thomas Merle
  - Mathis Adinolfi

date: 2024-09-19

tags:
  - "Projet 3A"
  - "Radio Live Custom"
  - "IA"
  - "Dev"

résumé: Création et déploiement d'un ChatBot de composition de musique interactif
---

## Le Principe
L'objectif de ce projet est de créer un ChatBot qui compose et joue de la musique en direct, accessible en streaming et avec plusieurs fonctionnalités comme :
* Possibilité d’influencer le style de la musique en direct en mettant des commentaires
* Possibilité d’influencer la prochaine musique en mettant des commentaires
* Peut-être +, qui sait ?

{% details "Exemples de fonctionnalités" %}
* Ajouter des basses
* Règler le volume
* Supprimer/Ajouter des harmoniques
* Supprimer/Ajouter les lyrics
* Des idées supplémentaires ?
{% enddetails %}

## Liens
- [GitHub]()

## En Pratique

### Liste des tâches à réaliser

1. **Partie 1 : Gestion de l'IA en C++** 
* Importer en C++ une IA qui permet de modifier une musique jouée
* Fournir les inputs que l'on souhaites à l'IA que nous devrons définir (comments issus du chat ou instructions à l'aide curseurs et boutons par exemple)

2. **Partie 2 : Gestion du BackEnd en GO**
* Prompt Engineering : utiliser GO pour gérer/traiter/filtrer les messages des users
* Utilisation d'un LLM pour interprêter le message du user : 2ème IA à prévoir pour la traduction ? 
* Gestion des requêtes users : création d'une queue dans les requêtes 
* Interaction avec le FrontEnd : API REST/Route

3. **Partie 3 : FrontEnd JS** 
* Création des interfaces : page de connexion, intégration du ChatBot, page queue, etc