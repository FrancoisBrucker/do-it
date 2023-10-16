---
layout: layout/pok.njk

title: "Apprendre un language Rust(ique) "
authors:
  - ORY Victor

date: 2024-09-19

tags:
  - 'temps 1'
  - 'Rust'
  - 'Super facile'

---

{%details "Pré-requis"%}

- Niveau novice
- Pré-requis de C++

{%enddetails%}


{%details "Les ressources"%}

- [Rust By Example](https://doc.rust-lang.org/rust-by-example/)
- [Documentation Rust](https://doc.rust-lang.org/stable/book/title-page.html)
- [Rust by Practise](https://practice.rs/why-exercise.html)
- [GitHub Exercice](https://github.com/rust-lang/rustlings)
- [Livre "From Javascript to Rust"](https://github.com/wasmflow/node-to-rust/raw/HEAD/from-javascript-to-rust.pdf)

{%enddetails%}

# Objectifs 

**Rust** est un language efficace et polyvalent, il peut faire du front, du back, du CLI, des jeux, du programme embarqué.

Donc je vais essayer d'en apprendre les fondements et de tester mes compétences sur le projet suivant :

- Créer une application pour écouter Spotify comme celle disponible à ce [repo](https://github.com/hrkfdn/ncspot) qui est conseillé par [Rust By Practise](https://practice.rs/why-exercise.html).

# Prévision pour le point 1 : 

- Apprendre les concepts de base de Rust :
  - Variables;
  - Iterators;
  - Smart Pointers;
  - Ownership / Borrowship;
  - ...
  

## Objectif initial

Mon premier objectif est d'acquérir une compréhension solide des concepts de base de Rust, notamment :

- Les variables
- Les itérateurs
- Les pointeurs intelligents
- La gestion de la propriété et des emprunts (ownership/borrowship)

Je vais suivre mon progrès en accomplissant les 96 exercices progressivement plus complexes du référentiel [Rustlings](https://github.com/rust-lang/rustlings), qui couvrent ces concepts essentiels. Actuellement, j'en suis à la première étape de progression : [>-----------------------------------------------------------] 1/96 (1.0 %), mais j'ai pour objectif d'atteindre 100 %.

Une fois cette étape terminée, j'ai l'intention de m'attaquer au projet proposé dans la documentation Rust, à savoir [Projet : Gestionnaire de lignes de commande](https://doc.rust-lang.org/book/ch12-00-an-io-project.html).

### Réalité du parcours

J'ai réussi à lire l'intégralité de la [documentation Rust](https://doc.rust-lang.org/stable/book/title-page.html), où les concepts clés ont été expliqués. Toutefois, pour consolider ces connaissances, j'ai dû réaliser des exercices supplémentaires proposés par [Rust By Practice](https://practice.rs/why-exercise.html). Mon défi personnel a été d'autant plus grand car mes bases en C++ sont limitées, étant donné que ma formation initiale dans ce domaine remonte à un certain temps.

Les concepts les plus complexes à assimiler ont été les cycles de vie et la manipulation des chaînes de caractères. En conséquence, je n'ai pas pu progresser aussi rapidement que prévu pendant mes 20 heures d'apprentissage. Néanmoins, j'ai tenu à créer quelque chose de concret, c'est pourquoi j'ai renoncé à l'idée de développer un outil en ligne de commande pour écouter Spotify. J'ai opté pour un outil en ligne de commande qui reproduit le comportement de "grep", c'est-à-dire un outil qui filtre la sortie d'une commande exécutée dans l'invite de commandes.

Mon travail est accessible dans ce [repo](https://github.com/Hagarde/CmdLineProject).
Ce projet repose sur le [tutoriel](https://doc.rust-lang.org/book/ch12-00-an-io-project.html) proposé par le livre, toutefois j'ai souhaité commencer avec puis ajouter de la complexité sans suivre le tutoriel pour réellement confronter mes connaissances à la réalité.

## Objectif en cours

Dans la prochaine phase de mon parcours d'apprentissage, je vais me concentrer sur...
