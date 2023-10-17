---
layout: layout/pok.njk

title: "Apprendre un language Rust(ique) "
authors:
  - ORY Victor

date: 2024-09-19

tags:
  - 'temps 1'
  - 'Rust'
  - 'Intermédiaire'

---

{%details "Pré-requis"%}

- Niveau novice
- Pré-requis de C++ ( que je n'ai pas trop)

{%enddetails%}



{%details "Les ressources"%}

- [Rust By Example](https://doc.rust-lang.org/rust-by-example/)
- [Documentation Rust](https://doc.rust-lang.org/stable/book/title-page.html)
- [Rust by Practise](https://practice.rs/why-exercise.html)
- [GitHub Exercice](https://github.com/rust-lang/rustlings)
- [Livre "From Javascript to Rust"](https://github.com/wasmflow/node-to-rust/raw/HEAD/from-javascript-to-rust.pdf)
- [MON de Assane](../../../Diouf-Asssane/mon/Rust/)
- [POK de Assane](../../../Diouf-Asssane/pok/temps-1/)

{%enddetails%}

## Objectifs

Voici les objectifs que je me suis fixé :

- Finir le livre [Rust Documentation](https://doc.rust-lang.org/stable/book/title-page.html) (★★★☆☆)
- Finir les exercices de [GitHub Exercice](https://github.com/rust-lang/rustlings)(★★★★☆)
- Tester mes connaissances sur le projet du Chapitre 12 de la [Documentation Rust](https://doc.rust-lang.org/stable/book/title-page.html)(★★★★☆)
- Réaliser un outil en commande Line pour écouter de la musique Spotify (★★★★★★★)

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

Je vais suivre mon progrès en accomplissant les 96 exercices progressivement plus complexes du référentiel [Rustlings](https://github.com/rust-lang/rustlings), qui couvrent ces concepts essentiels. Actuellement, j'en suis à la première étape de progression : 
[>-----------------------------------------------------------] 1/96 (1.0 %), mais j'ai pour objectif d'atteindre 100 %.

Une fois cette étape terminée, j'ai l'intention de m'attaquer au projet proposé dans la documentation Rust, à savoir [Projet : Gestionnaire de lignes de commande](https://doc.rust-lang.org/book/ch12-00-an-io-project.html).

### Réalité du parcours

## [Rust Documentation](https://doc.rust-lang.org/stable/book/title-page.html) 

* Fondamentale, complète, accessible et claire =  nécessaire mais pas suffisant *

J'ai réussi à lire le [livre Rust](https://doc.rust-lang.org/stable/book/title-page.html) jusqu'au 15ème chapitre, où les concepts clés ont été expliqués et on commence à aller ne profondeur. Toutefois, pour consolider ces connaissances, j'ai dû réaliser des exercices supplémentaires proposés par [Rust By Practice](https://practice.rs/why-exercise.html). Mon défi personnel a été d'autant plus grand car mes bases en C++ sont limitées, étant donné que ma formation initiale dans ce domaine remonte à un certain temps.

### [GitHub Exercice](https://github.com/rust-lang/rustlings)

* Bon complément au [livre Rust](https://doc.rust-lang.org/stable/book/title-page.html) *

Cela se concrétise notamment avec la complétion du projet [GitHub Exercice](https://github.com/rust-lang/rustlings) à hauteur de 67/97 à cause de concept avancé que je n'ai pas encore vu comme le multi thread programming.

Les concepts les plus complexes à assimiler ont été les cycles de vie et la manipulation des chaînes de caractères. En conséquence, je n'ai pas pu progresser aussi rapidement que prévu pendant mes 20 heures d'apprentissage. Néanmoins, j'ai tenu à créer quelque chose de concret, c'est pourquoi j'ai renoncé à l'idée de développer un outil en ligne de commande pour écouter Spotify. J'ai opté pour un outil en ligne de commande qui reproduit le comportement de "grep", c'est-à-dire un outil qui filtre la sortie d'une commande exécutée dans l'invite de commandes.

## Pratique 

* Facile avec les guides toutefois quand on navigue à vue, cela devient bien plus dure, un bon entraînement. Ça force à penser à TOUT ce qu'on a appris *

Mon travail est accessible dans ce [repo](https://github.com/Hagarde/CmdLineProject).
Ce projet repose sur le [tutoriel](https://doc.rust-lang.org/book/ch12-00-an-io-project.html) proposé par le livre, toutefois j'ai souhaité commencer avec puis ajouter de la complexité sans suivre le tutoriel pour réellement confronter mes connaissances à la réalité.

## Conclusion

J'ai pas été très efficace pour cette tâche en raison de ma confiance en mes capacités en C++ après seulement le cours de 2A. Les concepts ont été dures à appréhender et ont consommé la plupart de mon temps et je me suis éparpillé entre les différentes sources pour essayer d'avoir des points de vue différents sur les concepts que je ne comprenais pas. Cela explique aussi le fait que j'ai passé beaucoup de temps sur les exercices dures du [GitHub](https://github.com/rust-lang/rustlings).

Cela aurait été mieux d'en faire un MON avant pour éviter le temps perdu sur l'apprentissage et non la pratique.

Source explorées : 
- [Rust to javascript](https://annas-archive.org/md5/77a5209a50709593652c64d097088439) ( parce que j'ai pas mal d'expérience en javascript )
- [Zero To Production in Rust - An introduction to backend development](https://annas-archive.org/md5/819c53acaf3bff8c145179d26aa8cd0a) ( bases = pré-requis )
- [Vidéo Youtube](https://www.youtube.com/watch?v=BpPEoZW5IiY) ( lent mais représentatif de ma progression )
