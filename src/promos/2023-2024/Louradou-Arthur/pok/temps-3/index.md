---
layout: layout/pok.njk

title: "SérénaDo_It 2 - Vers un projet pérenne"
authors:
  - Arthur Louradou

date: 2023-02-14

tags: 
  - "temps 3"

résumé: Cette seconde partie du projet SérénaDo_It a pour objectif de définir les bases d'un projet pérenne. Elle abordera la mise en place d'une architecture logicielle robuste, la définition des processus de déploiement continu et la mise en place d'une stratégie de tests unitaires.
---

## Objectifs { #objectifs }

- Améliorations et fonctionnalitées
  - Changer la fonction de suppression des cours pour la rendre plus résiliente
  - Assurer une comparaison entre les emplois du temps
  - Permettre de résoudre la correspondance de noms de cours en base de données (en cas de divergence d'orthographe)
- Mettre en place une stratégie de tests
- CI/CD
  - Déployer le code à l'aide d'une image Docker
  - Mettre en place un pipeline de déploiement continu


### Sprint 3 { #sprint-3 }

Les temps suivants seront des estimations. Nous pourrons ajouter une colonne à la fin du POK pour mesurer les écarts.

| Tâche                                     | Difficulté | Temps |
|-------------------------------------------|------------|-------|
| Refonte de la fonction de choix des cours | 2          | 2h    |
| Volet d'administration                    | 5          | 4h    |
| Amélioration du cache                     | 3          | 2h    |
| Tests unitaires                           | 2          | 2h    |


### Sprint 4 { #sprint-4 }

Ce Sprint est encore vague et sera enrichi des retours du sprint 3.

| Tâche                                               | Difficulté | Temps |
|-----------------------------------------------------|------------|-------|
| Export automatique avec validation des cours saisis | 3          | 5h    |
| Intégration et Déploiement continus                 | 8          | 5h    |


