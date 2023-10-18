---
layout: layout/mon.njk

title: "Introduction au langage Rust"
authors:
  - Paul VIETOR

date: 2023-10-18
tags: 
  - "temps 1"

résumé: "Une introduction au langage Rust au travers du livre Rust officiel."
---

## Introduction

Dans ce second MON, j'ai décidé de me lancer dans le langage Rust en parcourant le [livre de Rust](https://doc.rust-lang.org/stable/book/title-page.html), en faisant les quelques projets qui y sont proposés au cours de sa lecture.

Mais, me demanderez-vous, qu'est-ce que Rust ? 

## Présentation du langage Rust

D'après [Wikipédia](https://fr.wikipedia.org/wiki/Rust_\(langage\)), "Rust est un langage de programmation compilé multi-paradigme conçu et développé par Mozilla Research depuis 2010."... Ouais. Ça ne nous avance pas beaucoup, et même si le reste de la page nous donne de plus amples explications, c'est un peu long pour tout citer ici, donc je vais me contenter des grandes propriétés importantes :
- Tout d'abord, reprenons les deux termes cités ci-dessus :
  - Rust est compilé : on écrit du code en Rust, puis on le donne à un compilateur qui va lui nous donner un exécutable, un fichier en langage machine que le processeur pourra directement utiliser. Il est en cela similaire à des langages tels que le C, le C++, l'OCaml, et bien d'autres, et s'oppose par exemple aux langages Bash et Perl.
  - Rust est multi-paradigme : en programmation, un paradigme est, grossièrement, l'approche utilisée par un langage pour décrire le programme. En programmation dite impérative (C, Python...), un programme est une suite d'instructions que doit exécuter le processeur. En programmation fonctionnelle (OCaml, Haskell), un programme est une chaîne d'évaluations de fonctions. Enfin, pour ne citer que trois exemples, en programmation orientée (Java, C#...), un programme consiste en un ensemble d'"objets", des sortes de briques du programme, qui interagissent entre eux. Dans les faits, très peu de langages modernes se restreignent à un seul de ces paradigmes, et en ce qui concerne Rust, c'est un langage principalement impératif et fonctionnel, qui intègre quelques notions de la programmation orientée objet.
- Rust est de plus un langage fortement typé : chaque variable a un type qui définit les opérations que l'on peut faire sur cette variable, et il est interdit de changer implicitement le type d'une variable. Par exemple, on ne peut pas additionner une variable entière et un nombre à virgule flottante ou une chaîne de caractère (à moins de ne définir explicitement l'opération nous-même), contrairement à ce qui est possible en JavaScript, qui acceptera volontiers de dire que la chaîne de caractère `"Hello"` à laquelle on additionnerait le nombre `2.718` nous donne... la chaîne de caractère `"Hello2.718"`. 
- Il est également statiquement typé : à chaque variable est associé un unique type, et on ne peut pas lui assigner une valeur d'un type différent.
- Enfin, sa syntaxe est similaire à celle du C (et du C++, de JavaScript...), avec l'utilisation d'accolades pour définir des blocs de code, de parenthèses pour définir les arguments de ses fonction, les points-virgules en fin de ligne... avec quelques différences, notamment au niveau de la déclaration du type d'une variable, qui se trouve après le nom de la variable.

## En quoi consiste le livre de Rust

La communauté Rust a écrit un livre à destination de ceux désirant apprendre le langage Rust. En une vingtaine de chapitres (trop pour que je puisse le finir en 10h), il nous présente les fonctionnalités du langage Rust, et nous accompagne dans 3 projets : un très simple jeu dans lequel le joueur doit deviner un nombre aléatoire entre 1 et 100, dès le chapitre 2, un clone minimaliste du programme `grep`, qui permet de rechercher une chaîne de caractères dans un fichier, au chapitre 12, et enfin un serveur web *multithreadé*, c'est-à-dire qui exécute plusieurs tâches en parralèle sur différents *threads* du processeur, au chapitre 20.

Tout d'abord, le premier chapitre est dédié à l'installation des outils nécessaires au développement en Rust, et le deuxième chapitre nous guide au travers du premier projet.  
Ensuite, les chapitres 3 à 10 nous présentent les fonctionnalités et spécificités essentielles du langage : les types et structures de données de base disponibles, les bibliothèques (nommées *crates*), la gestion des erreurs, et, bien sûr, la spécificité incontournable de Rust, la notion de propriété, reprise plus en détail par Assane Diouf dans son [premier MON]({{ "/promos/2023-2024/Diouf-Asssane/mon/Rust" | url }}).  
Le chapitre 11, quant à lui, nous présente les fonctionnalités de tests automatiques qui pourront être exécutés par `cargo`, l'outil principal de gestion des projets Rust, afin de nous préparer au deuxième projet, au chapitre 12.  
Enfin, les chapitres 13 à 19 nous présentent les fonctionnalités avancées de Rust afin de nous préparer au dernier projet du chapitre 20, à l'exception du chapitre 14 qui revient sur `cargo` ainsi que la gestion des *crates* et [Crates.io](https://crates.io/), le site officiel pour trouver des *crates*.

Pour ce MON, je vais donc tenter d'expliquer de façon succinte les divers concepts rencontrés dans ce livre au fil de ma lecture, chapitre par chapitre, jusqu'au point auquel j'aurai réussi à arriver en dix heures.

## Mon avancement dans la lecture du livre


### Chapitre 1 : Outils et installation

Le chapitre 1 était très rapide, puisqu'il n'a été pour moi que l'affaire de lancer quelques commandes et attendre que les téléchargements se fassent.

### Chapitre 2 : Premier projet

Le chapitre 2 m'a pris environ une heure et demi pour tout bien comprendre. Ce chapitre sert d'introduction à plusieurs concepts que nous verrons plus en profondeur dans les chapitres suivants :
- Les variables mutables/non-mutables
- Les références
- Les entrées/sorties sur l'invite de commandes
- L'énumération `Result` pour décrire le succès ou l'échec d'une opération
- Les erreurs de compilation
- Le `match`
- La gestion des dépendances

### Chapitre 3 : Notions communes en programmation

Le chapitre 3, rapide à lire quand on a déjà des bases de programmation, présente des notions communes à la très grande majorité des langages de programmation : les variables, les types de données, les fonctions, les commentaires et les structures de contrôle (*control flow*). On y découvre quelques spécificités de Rust :
- Il existe 3 classes de variables différents : non-mutable, déclarée avec `let`, mutable, déclarée avec `let mut` et constante, déclarée avec `const`. Les variables mutables peuvent recevoir pendant l'exécution du programme une valeur différente de leur valeur initiale, mais de même type, contrairement aux variables non-mutables ou constantes qui gardent la même valeur. De plus, la valeur d'une variable constance doit être connue au moment de la compilation. On nous présente également le *shadowing* de variable, quand on déclare une nouvelle variable avec le même nom qu'un variable pré-existante, qui permet de garder le nom de la variable mais d'en changer le type, par exemple.
- Les caractères sont représentés sur 4 octets et contiennent un caractère Unicode.
- Une fonction peut renvoyer la valeur d'une expression qu'elle contient sans avoir besoin de `return` explicite, mais il est également possible d'utiliser `return`.
- Quand on évalue une condition, par exemple dans un `if`, il faut obligatoirement que la condition à évaluer soit un booléen : on ne peut pas faire `if 3 {}`, par exemple, là où en C, Python, et la plupart des autres langages, le 3 serait implicitement converti en le booléen `true`.

### Chapitre 4 : La propriété

Le chapitre 4 est le chapitre qui présente la notion de propriété, et peut être long à comprendre puisque qu'il explique la gestion de la mémoire en Rust. J'en ai personnellement eu pour deux petites heures, en ayant déjà rencontré certaines notions abordées dans ce chapitre. Je ne reviendrai pas sur la notion de propriété spécifiquement, puisque ce serait une redite de ce qu'a déjà expliqué Assane dans son MON. Cependant, je peux expliquer la gestion de la mémoire : en Rust, les données peuvent aller à deux endroits :
- La **pile** (*stack*), pour les valeurs de types de taille constante (un nombre, un caractère) et, généralement, réduite
- Le **tas** (*heap*), pour les valeurs de types de taille variable (les chaînes de caractères) ou les valeurs qui sont particulièrement grandes.
Quand on crée une variable de type, par exemple, `i32` (un nombre entier entre -2³¹ et 2³¹-1), qui est de taille constante (32 bits), Rust met sa valeur sur le haut de la pile. Cette variable est ainsi particulièrement rapide d'accès et peut être copiée et transférée très rapidement.  
Quand on crée une chaîne de caractères, par contre, Rust va allouer une certaine quantité de mémoire sur le tas dans laquelle il va enregistrer les caractères, et mettre sur la pile une valeur de taille fixée qui contient l'emplacement sur le tas de la chaîne de caractère, et quelques informations sur la chaîne de caractères : sa longueur, et la place disponible pour cette chaîne de caractères sur le tas.

La distinction est importante car, quand on assigne une valeur à une variable, on assigne seulement la valeur qui se trouve sur la pile. Ainsi, si on déclare deux entiers, `a` et `b`, puis que l'on fait `b = a`, b est une copie indépendante de a, et on peut modifier b sans affecter la valeur de a (pour peu que b soit mutable, évidemment).  
Cependant, si on essaye de faire la même chose avec deux chaînes de caractères, b ne va copier que la valeur de a se trouvant sur la pile : l'emplacement sur le tas, la longueur et la place disponible. Les deux variables pointeront donc aux même données sur le tas, et toute modification à b modifierait a, et inversement. Pour éviter de faire cette erreur, Rust rend alors a invalide : on ne peut plus l'utiliser, sous peine de causer une erreur à la compilation. Si on veut réellement copier a dans une nouvelle variable, il faut le faire explicitement avec la méthode `clone()`.

{% info %}
La façon dont Rust détermine le comportement à adopter en pratique implique le **trait** Copy, mais les traits étant seulement au programme du chapitre 10, il ne me semblait pas intéressant d'en parler ici.
{% endinfo %}

### Chapitre 5 : Structures

Le chapitre 5 présente les structures (`struct`s), en opposition aux uplets (*tuples*), décrits dans le chapitre 3. Les deux permettent de stocker plusieurs valeurs dans une même variables, mais dans une structure, chacune de ces valeurs peut avoir un nom, et une structure est en soi un type de données nommé, dont le nom est donné par le programmeur. Cela permet alors de passer des structures comme arguments à nos fonctions, rendant le code plus clair, et de définir des **méthodes** pour les structures.

{% note %}
Pour implémenter une méthode pour notre structure, il faut utiliser un bloc `impl` dans lequel on met nos méthodes, séparé du bloc `struct` définissant la structure.
{% endnote %}

{% note %}
Il est également possible de créer des structures ne stockant aucune valeur, on a alors un type dit unité (et de même pour les uplets, on peut créer le 0-uplet `()` qui ne contient aucune valeur). Cela peut également avoir des intérêts, mais qu'on ne verra pas avant le chapitre 10.
{% endnote %}

Ainsi, ce chapitre nous montre comment utiliser une structure pour représenter un rectangle, et définit quelques méthodes sur ces rectangles : le calcul de leur aire, et savoir si un rectangle rentre dans un autre.

{% info %}
Les `structs` et les uplets pouvant encapsuler plusieurs valeurs, ce sont ce que l'on appelle des types produits, en référence au produit cartésien d'ensembles en mathématiques. On les distingue des types dits sommes, tels que les énumérations dont nous parle le chapitre 6.
{% endinfo %}

### Chapitre 6 : Énumérations et match

Ce chapitre 6 nous présente les énumerations (`enum`s), qui sont des types dont la valeur peut elle-même être de plusieurs types différents, mais un seul à la fois : ce sont des types sommes, comme dit dans l'encadré juste au-dessus. Chacun de ces types est alors appelé une **variante** de notre type énumération, ces variantes peuvent elles-mêmes contenir des valeurs.

{% info %}
On peut alors considérer chaque variante de notre énumération comme une structure, éventuellement unité si la variante ne contient aucune valeur.
{% endinfo %}

Les énumérations ont plusieurs utilités : il se pourrait que l'on veuille, par exemple utiliser des adresses IP. Or, il existe de nos jours deux types d'adresses IP : les adresses IPv4 et les adresses IPv6. Plutôt que de devoir s'embêter avec un type (qui serait alors une structure) pour chaque forme, on peut utiliser une énumération, et définir des méthodes communes à toutes les adresses IP, n'avoir qu'une seule définition de fonction qui doit prendre une adresse IP en paramètre, etc.

Cependant, cette approche demande de pouvoir distinguer les opérations que l'on fait selon la variante de l'énumération : c'est là que `match` entre en jeu.  
Quand on utilise `match` sur une variable dont le type est une énumération, on peut emprunter une différente branche de notre programme pour chaque variante, et, si cette variante contient elle-même une valeur, on peut lier cette valeur à une variable pour la durée de la branche.

Enfin, ce chapitre nous parle des énumérations `Result` et `Option`, représentant respectivement un résultat, qui pourrait indiquer un échec ou une réussite avec une valeur, et une valeur pouvant éventuellement valoir `Null` (qui est en quelque sorte une "absence de valeur"), et de certaines méthodes ou fonctionnalités du langage que l'on peut utiliser avec ces énumérations.

### Chapitre 7 : *Crates*, paquets et modules

Ce chapitre 7 nous présente les *crates*, les paquets et les modules. C'est un chapitre important, relativement long et complexe, j'ai mis près d'une heure et demi à bien l'assimiler.

En Rust, formellement, une ***crate*** est tout simplement une unité de code que considère le compilateur. On distingue deux types de *crates* : les *crates* binaires, qui sont des programmes exécutables, et les *crates* bibliothèques, qui contiennent des fonctionnalités réutilisables depuis d'autres programmes. En général, quand on parle de *crate*, on parle de ce second type.

Un **paquet** est un ensemble de une ou plusieurs *crates*, mais qui ne peut pas avoir plus d'une *crate* bibliothèque. À chacune des *crates* d'un paquet va correspondre soit le fichier `src/main.rs`, qui est la *crate* binaire principale du paquet, soit le fichier `src/lib.rs`, qui est la *crate* bibliothèque du paquet, soit un fichier dans `src/bin`.

Enfin, tout fichier qui ne correspond à aucun de ces chemins peut définir un **module**, que l'on peut ensuite utiliser dans notre code avec l'instruction `mod <nom du module>`, où le nom du module est le nom du fichier sans l'extension ou le nom d'un dossier contenant un fichier `mod.rs`.  
Par défaut, tout ce que l'on définit dans un module est privé, il faut précéder les déclarations du mot-clef `pub` afin de rendre ce que l'on définit accessible par le module parent et utiliser `pub mod` au lieu de `mod` pour rendre les sous-modules accessibles au module parent.

### Chapitre 8 : Collections

Le chapitre 8 est consacré aux collections, qui sont des types contenant multiples valeurs d'un même type. Ici on nous présente 3 collections : les vecteurs, les `String`s et les tables de hachage (*hash tables*). C'est également notre première rencontre avec les génériques, qui seront là encore vus plus en profondeur au chapitre 10.

En ce qui concerne les vecteurs, on nous présente comment créer un vecteur, comment en récupérer une valeur, ou en ajouter ou supprimer une, ainsi que comment itérer sur les éléments d'un vecteur. De plus, bien qu'un vecteur ne puisse contenir que des éléments d'un même type, rien n'empêche ce type d'être une énumération, donc pour créer un vecteur dont les éléments peuvent avoir certains types prédéfinis, il suffit d'utiliser une énumération dont les variantes peuvent contenir les types de données souhaitées.

Ensuite, on nous présente les `String`s, qui contiennent des chaînes de caractères Unicode encodés en UTF-8. En particulier, puisque ce type de données n'est "que" un vecteur avec quelques méthodes supplémentaires ou légèrement modifiées, la majorité des méthodes disponibles pour les vecteurs sont disponibles sur les `String`s. Cependant, on ne paut pas utiliser `[]` pour récupérer un élément d'un `String`, puisque cela correspondrait à récupérer un élément du vecteur sous-jacent, qui n'est souvent pas un caractère à lui tout seul. De plus, on nous donne deux méthodes pour concaténer des `String`s, soit avec l'opérateur `+`, soit avec `format!`. Enfin, pour itérer sur un `String`, Rust nous donne deux méthodes : `chars()` et `bytes()`, qui permettent d'itérer respectivement sur les caractères, qui sont alors donnés sous forme de `char`s de Rust, et sur les octets de l'encodage UTF-8.

{% info %}
On peut récupérer *une partie d'un* `String` en l'indiçant avec un *range* entre crochets, mais cela est fortement déconseillé car peut causer des erreurs.
{% endinfo %}

Enfin, les tables de hachage sont un type qui implémente les dictionnaires : un ensemble de couples (clef, valeur) qui nous permet de récupérer une valeur étant donnée la clef correspondante. Contrairement aux vecteurs et aux `String`s, les tables de hachage ne sont pas ordonnées. Enfin, là encore, on nous présente les méthodes pour insérer ou enlever des éléments.

### Chapitre 9 : La gestion des erreurs

Il ne me restait pas beaucoup de temps, et le chapitre 10 me semblait plus intéressant que le chapitre 9, donc j'ai décidé de passer le chapitre 9 pour ce MON.

### Chapitre 10 : Types génériques, traits et durées de vie

Ce chapitre, qui est le dernier que j'ai eu le temps de lire, nous présente la programmation générique : ne pas se soucier des types mêmes, mais uniquement de propriétés qu'ont les types. Par exemple, on peut définir des relations d'ordres sur de nombreux types, tels que les entiers, les nombres à virgule flottante, les chaînes de caractères... mais dans un langage statiquement typé comme Rust, à priori, il faudrait écrire une fonction pour chacun de ces types si on souhaite par exemple trier une liste, ou en trouver le maximum. Pour remédier à cela, on va utiliser un type **générique**, et dire au compilateur que, pour que l'appel à notre fonction soit valide, il faut que ce type supporte une relation de comparaison. 

{% note %}
Il est également possible d'utiliser des types génériques dans les définitions de structures ou d'énumération, de la même façon que dans les fonctions.
{% endnote %}

C'est là qu'interviennent les **traits**. En Rust, un trait est un propriété qu'a un type. Par exemple, un type sur les éléments duquel est définie une relation d'ordre (partielle) aura le trait `std::cmp::PartialOrd`, un type dont les éléments supportent l'addition avec `+` aura le trait `std::ops::Add`, etc. On dit alors que le type **implémente** le trait. En général, implémenter un trait veut dire que l'on implémente les méthodes que doit supporter le trait. Ensuite, quand on crée une fonction, un énumération, une structure... qui demande un type générique implémentant le trait, on est garanti que l'on va pouvoir utiliser ces méthodes.

{% note %}
Il est également possible de demander à ce que le type générique implémente plusieurs traits, en séparant les différents traits requis d'un `+`.
{% endnote %}

{% info %}
Pour les traits cités ci-dessus, les méthodes à implémenter sont en fait celles que Rust va appeler quand on utilisera les opérateurs `<`, `>` et `+`, ce qui nous permet d'utiliser directement ces opérateurs dans notre code.
{% endinfo %}

{% info %}
Comme il est souvent chronophage d'implémenter toutes les méthodes requises pour un trait, Rust nous permet de demander au compilateur de créer une implémentation par défaut pour certains traits en utilisant la macro `derive`, mais ce n'est pas abordé dans ce chapitre.
{% endinfo %}

Enfin, ce chapitre présente les durées de vie. C'est ce qui détermine dans quel cadre (pour combien de "temps") une référence est valide. Cela est notamment utile quand on veut écrire une fonction qui renvoie une référence ou une structure dont un des membres est une référence, puisqu'il faut que Rust sache quand est valide cette référence par rapport à la structure ou aux arguments de la fonction.  
Cependant, c'est un sujet que je n'ai pas encore bien compris, et que j'espère réussir à comprendre en passant à la pratique lors du projet.

## Conclusion

Au travers de ces 10 premiers chapitres, on a pu découvrir les fonctionnalités de base de Rust, comment les appréhender et les utiliser, et comment ces fonctionnalités et son compilateur permettent de données certaines garanties de sécurité et de validité des opérations qui sont effectuées lors la compilation, permettant d'éviter bien des erreurs au moment d'utiliser le programme, dans un langage qui se veut pourtant relativement proche de la machine. Il reste cependant de nombreuses fonctionnalités qui ne seront présentées que dans les chapitres suivants, donc je continuerai la lecture de mon côté, notamment en vue du développement sur notre projet.
