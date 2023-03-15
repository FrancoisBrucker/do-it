---
layout: layout/post.njk

title: "POK 3 : Bibliothèque Rust et programmation par les tests"
authors:
 - Thomas Pont

tags:
    - 'Rust'
    - 'Programmation par les tests'
---

<!-- Début Résumé -->

Rust
<!-- Fin Résumé -->

## Présentation

Rust est un langage de programmation de bas niveau pouvant être utilisé entre autre pour le développement de moteurs de jeux, de systèmes de fichiers, de sites web ou encore de systèmes d’exploitation. Ce langage est plus sûr, plus rapide que d'autres langages existants comme le C ou C++ tout en étant simple d'utilisation en offrant une abstraction de haut niveau.

Ce langage est en plein essor. L'objectif de ce POK est de monter en compétence dans celui-ci en réalisant une bibliothèque de structure de données. Chacune des fonctionnalités sera testée avec des tests unitaires.

## Sprint 1

### Objectifs

- Suivre un [tutoriel Rust](https://doc.rust-lang.org/stable/rust-by-example/index.html)
- Définir les fonctionnalités de ma bibliothèque
- Ecrire des tests unitaires et les fonctions

### Travail réalisé

Lors de ce temps, j'ai suivi la moitié du tutoriel de Rust. Ce tutoriel est très bien fait et permet de découvrir les notions de Rust tout en pouvant les tester en parallèle. De plus, il y a des petits exercices qui permettent de s'assurer qu'on a bien compris comment ce langage fonctionne.

Après avoir suivi cela, j'ai décidé de créer une première bibliothèque de gestion de structure de données. J'ai en particulier orienté mon travail sur les tableaux. Plusieurs fonctionnalités ont été implémentées comme la création d'un tableau, l'ajout ou la suppression d'éléments, la somme de deux tableaux, le tri d'un tableau, la fusion de deux tableaux triés, ...
Chaque fonction a été réalisée avec des tests unitaires qui se lancent avec [une bibliothèque disponible via Cargo](https://doc.rust-lang.org/book/ch11-01-writing-tests.html).

## Sprint 2

Dans la suite de ce POK, je me concentrerai sur l'implémentation d'autres fonctionnalités sur les tableaux et l'implémentation d'autres structures de données telles que les arbres.

## Lien

[Lien vers le Github](https://github.com/ThomasP04/POK3-Rust)
