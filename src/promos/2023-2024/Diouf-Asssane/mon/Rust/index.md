---
layout: layout/mon.njk

title: "Introduction à Rust"
authors:
  - Assane Diouf

date: 2023-09-27

tags: 
  - "temps 1"

résumé: "Découvrons ensemble le langage Rust. Il est de plus en plus adopté dans l'industrie pour ses performances et ses idées nouvelles, comme l'ownership."
---

{%prerequis 'MON débutant'%} 
Il faut connaître : 
- des bases en C/C++ 
- l'utilisation d'un CLI (un terminal de commande) 
{%endprerequis%}

Pour faire mes débuts en Rust j'ai d'abord consulté le [site officiel](https://www.rust-lang.org/fr) du langage. On peut y trouver un livre (gratuit) pour apprendre le langage : [https://doc.rust-lang.org/book/](https://doc.rust-lang.org/book/).

J'ai aussi pu me baser sur un livre que m'a prêté M. Brucker : **Hands-on Rust : Effective learning through 2D Game Development and Play** de Herbert Wolverson. Etant donné que le livre proposé par Rust est composé de plusieurs chapitres d'explication avec peu de pratique, il m'a permis de commencer à pratiquer en même temps que j'apprenais les concepts du langage.

Cette vidéo Youtube est aussi une présentation (très) rapide à Rust : [Rust](https://www.youtube.com/watch?v=5C_HPTJg5ek)

## Présentation de Rust
- Parmis les langages préféré des développeurs
- Performant, sécurisé (typage, ownership), productif
- Permet de :
  - construire des CLI
  - se compile en web assembly
  - faire du réseau
  - faire du développement embarqué

## Comment faire du Rust ?
Rust étant un langage compilé, il faut commencer par installer le compilateur rustc. Ensuite, pour éditer du code en Rust, il faut un IDE comme Visual Studio Code ou CLIon. Enfin, pour exécuter son premier programme Rust, il faut créer l'exécutable avec la commande :
```bash
rustc main.rs 
```
et exécuter ce dernier avec : 
```bash
./main
```

L'usage est cependant d'utiliser **cargo** pour développer avec Rust. Cargo va permettre de gérer l'ensemble des dépendances du projet avec d'autres librairies Rust (des crates) et de facilement créer un exécutable et le tester.

## Les particularités de Rust
Tout d'abord, Rust est un **langage** typé, mais contrairement à d'autres langages, il prend aussi en compte l'espace occupé par chaque type. Par exemple, un entier signé sur 32bits a pour type i32 alors qu'un entier signé sur 8bits a pour type i8. Je trouve Rust particulièrement plus lisible que le C/C++ avec ces notations. En plus de ce système de type, Rust vient avec un système *simple* de conversion des variables d'un type à un autre. Rust introduit aussi une forme de string plus piégeuse que dans d'autres langages mais, en contrepartie, permet vraiment de travailler avec tout type de charactères de façon sécurisée.


On peut aussi parler du fait que la valeur nulle n'existe pas dans Rust. A la place, Rust introduit des énumérations comme les Options qui peuvent valoir Some(quelque chose) ou None. Couplé avec les matchs par exemple, cela permet de mieux gérer les erreurs à mon sens.


Ensuite, il y a l'**ownership** (la *propriété* en français), qui est un ensemble de 3 règles dont le but est de réduire le nombre d'erreurs dûe à la manipulation de la mémoire.


## C'est quoi l'ownership ?
L'ownership est un système de **management de la mémoire** en Rust, basé sur les règles suivantes :
- Chaque valeur a un propriétaire.
- Il ne peut y avoir qu'un proprétaire à la fois par valeur.
- Les valeurs sont automatiquement détruites avec le propriétaire.

Ces règles sont importantes à garder en tête lors du maniement de certaines valeurs. Il est alors intéressant, à mon sens, de tout voir alors comme dans le cas où l'on possède un objet :
- il n'a qu'un seul propriétaire
- si on le donne, il n'est plus à nous
- on peut cependant le prêter
- il y a plusieurs type de prêts (on récupère toujours l'objet identique ou on le récupère modifié)

Le cas des prêts représente les **références** en Rust. Les références permettent, par exemple, de passer une de ces valeurs à une fonction sans en perdre la propriété.

## Conclusion
A mon avis, Rust est un langage intéressant qui vaut le détour. Je souhaite maintenant étendre mes connaissances du langage et pratiquer davantage. Durant ces 10h, je n'ai en effet pas eu le temps d'explorer des sujets comme les pointeurs intelligents, la POO en Rust, le multithreading, etc...

Enfin Rust est aussi un langage qui se compile très facilement en WebAssembly, laissant une multitude de possibilités avec ce langage. J'aborderai le WebAssembly plus en détail dans mon premier POK.