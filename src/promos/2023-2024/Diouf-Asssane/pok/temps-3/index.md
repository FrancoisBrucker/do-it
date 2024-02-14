---
layout: layout/pok.njk

title: "Un CLI avec Rust"
authors:
  - Assane Diouf

date: 2024-02-14

tags: 
  - "temps 3"

résumé: Développement d'une commande avec Rust
---

## Introduction
Lors du premier temps à Do_It, j'ai découvert Rust. Rust est un langage bas niveau très apprécié par les développeurs pour son aspect "safe by design". J'ai donc envie d'appliquer mes connaissances en Rust pour progresser davantages.
Dans ce POK, je vais développer un CLI (Command Line Interface). Il s'agit d'un programme qui tourne dans l'invité de commande avec laquelle l'utilisateur peut intéragir grace à des commandes. Pour ce faire je vais utiliser le crate clap.rs, qui vient avec plein d'outils pour créer des commandes avec Rust.

## Idée
J'ai pensé développer un outil simple de suivi des projets pour les développeurs sur leur machine locale. Les fonctionnalités seraient les suivantes :
- Ajouter un projet (nom, description)
- L'ouvrir dans l'IDE qui convient
- Le cloner directement dans le bon dossier si le projet n'est pas présent en local
- Suivre le temps passé sur chaque projet

## Ce que j'aimerai faire pour le sprint 1
- [ ] Découvrir les commandes clap.rs (2h)
- [ ] Sérializer/désérializer les configurations (2h)
- [ ] Pouvoir ajouter des projets (1h)
- [ ] Pouvoir lister les projets présents sur la machine (1h)
- [ ] Afficher les informations spécifiques à un projet (1h)
- [ ] Supprimer des projets (1h30)
- [ ] Mettre à jour des projets (1h30)

## Ce que j'ai fait au premier sprint

## Ce que j'aimerai faire au sprint 2
- [ ] Pouvoir ouvrir les projets dans l'ide souhaité par le développeur (2h)
- [ ] Pouvoir suivre le temps passé sur chaque projet (4h)
  - [ ] Conserver dernière date d'ouverture (1h)
  - [ ] Ajouter une commande pour indiquer que l'utilisateur arrête de travailler sur le projet (2h)
  - [ ] Garder en mémoire le temps passé (1h)
- [ ] Pouvoir ouvrir les projets dans vscode (1h)
- [ ] Cloner le projet si il n'est pas présent en local (1h)

## Ce que j'ai fait au sprint 2

## Conclusion
