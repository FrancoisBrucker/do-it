---
layout: layout/pok.njk

title: "POK 3 : Bibliothèque Rust et programmation par les tests"
authors:
 - Thomas Pont

date: 2023-01-25

tags:
  - 'temps 3'
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

Après avoir suivi cela, j'ai décidé de créer une première bibliothèque de gestion de structure de données. J'ai en particulier orienté mon travail sur les tableaux. Plusieurs fonctionnalités ont été implémentées comme la création d'un tableau, l'ajout ou la suppression d'éléments, la somme de deux tableaux, le tri d'un tableau, ...
Chaque fonction a été réalisée avec des tests unitaires qui se lancent avec [une bibliothèque disponible via Cargo](https://doc.rust-lang.org/book/ch11-01-writing-tests.html).

## Sprint 2

Dans la suite de ce POK, je me concentrerai sur l'implémentation d'autres fonctionnalités sur les tableaux et l'implémentation d'autres structures de données telles que les arbres.

### Objectifs

[x] Continuer à suivre le tutoriel Rust
[x] Implémenter de nouvelles fonctionnalités dans ma bibliothèque sur les tableaux (comme la fusion de deux tableaux triés)
[x] Créer une nouvelles bibliothèques sur les arbres binaires de recherches
[x] Implémenter des fonctionnalités:

- Création d'un arbre
- Insertion et suppression d'éléments
- Somme des éléments d'un tableau
- Différents parcours de l'arbre
- Hauteur et taille
- ...

## Comment faire du Rust ?

[Lien](https://www.rust-lang.org/tools/install)pour installer Rust sur Windows

Commande pour compiler du Rust :

```bash
rustc main.rs
```

Commande pour lancer le code :

```bash
./main
```

Pour créer une bibliothèque

```bash
cargo new nom_de_votre_bibliotheque --lib
```

Le code de la bibliothèque doit être mis dans le fichier src/lib.rs

Pour compiler le code de la bibliothèque :

```bash
cargo build
```

Pour les tests unitaires, il faut indiquer #[test] devant chaque test.

Pour lancer les tests unitaires :

```bash
cargo test
```

## Lien

[Librairie Tableau](https://github.com/ThomasP04/POK3-Liste)
[Librairie Arbre](https://github.com/ThomasP04/POK3)
