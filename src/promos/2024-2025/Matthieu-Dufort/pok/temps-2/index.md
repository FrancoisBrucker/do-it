---
layout: layout/pok.njk

title: "Titre du POK du temps 2"
authors:
  - Matthieu Dufort

date: 2024-11-20

tags: 
  - "temps 2"
  - "Novice"
  - "C"

résumé: Un POK ayant pour objectif d'apprendre le langage C.
---

{% prerequis %}

Pas de prérequis particulier son nécessaire mais il peut être intéressant de lire le MON de Cassandra en complément.

{% endprerequis %}
{% lien %}

- [Documentation C](https://openclassrooms.com/fr/courses/19980-apprenez-a-programmer-en-c)
- [MON de Cassandra Ledins](https://francoisbrucker.github.io/do-it/promos/2023-2024/Ledins-Cassandra/mon/temps-1.2/)
- [Code créé au cours de l'apprentissage](CodeSprint1.zip)

{% endlien %}

Pour ce POK, j'ai décidé d'apprendre un nouveau langage afin d'élargir mes compétences en développement avec un langage un peu moins intuitif que python. Je vais me former sur l'utilisation du langage C. Pour cela je vais partir de la documentation et construire ensuite dans un second temps un petit projet (probablement un morpion ou un mini jeu de ce genre) afin de le prendre un peu plus en main.

## Tâches

- Regarder les MON et POK traitant du sujet afin de trouver un bon moyen d'apprendre
- Suivre un cours pour avoir des bases sur ce langage
- Construire des programmes pour apprendre
- Construire un mini jeu pour prendre en main le langage

### Sprints

Le but final de ce POK et de parvenir a comprendre du code en C et d'être capable d'écrire des programmes simples.

#### Sprint 1

- [x] Se renseigner sur les anciens POK et MON dessus
- [x] Trouver un cours à suivre
- [/] Suivre le cours pour monter en compétence

#### Sprint 2

- [ ] Chercher un petit projet type un jeu réalisable en C en 10h
- [ ] Réaliser ce mini projet par moi même

Liste des taches que l'on pense faire. On coche si la tache est réalisée. A la fin du sprint on fait une petite étude post-mortem pour voir ce qui s'est passé et les ajustement à faire pour le prochain sprint, pok.

### Horodatage

| Date | Heures passées | Indications |
| -------- | -------- |-------- |
| Vendredi 15/11  | 4H  | Inventaire des POK et MON, choix du cours et début, Installation d'un compilateur|
| Samedi 16/11  | 5H  | Suite du cours d'openclassrooms|
| Dimanche 17/11 | 4h | Suite du cours d'openclassrooms |

## Contenu

### Premier Sprint

Après avoir fait l'inventaire des POK et MON traitant du langage C : j'ai choisi de suivre le cours d'open ClassRoom qui est fortement recommandé par Cassandra et qui lui a permis d'acquérir de bonnes bases. Je vais essayer de compléter son MON en abordant d'autres points du langage C. Je recommande donc au futur personne voulant apprendre ce langage de lire aussi son [MON](https://francoisbrucker.github.io/do-it/promos/2023-2024/Ledins-Cassandra/mon/temps-1.2/).

## Ecrire du C avec VSCode

J'ai décidé de travailler, comme toujours, avec VSCode et j'ai donc installé une extension spéciale pour le C afin de faire la compilation et de débugger (+ pouvoir écrire avec un style adapté : couleurs etc.). Je recommande donc : [C/C++](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools). Cependant, elle n'a vite plus marché (pour la compilation) dès que j'ai réparti mon code sur plusieurs fichiers. J'ai du ensuite compiler à chaque fois avec le terminal de commande en compilant chaque fichier .c en objet .o puis en compilant ensemble les objets en .exe.

Pour la compilation, il est nécessaire aussi d'installer un compilateur, j'ai choisi [MinGW](https://sourceforge.net/projects/mingw/) et de rentrer ensuite son path dans l'ordinateur et dans les options de l'extension de VSCode pour pouvoir l'utiliser.

{% details "Utiliser le compilateur installé" %}

Pour changer le path du compilateur dans l'extension :

- ctrl + shift + P
- C/C++ : Edit configuration (UI)
- Changer le path du compilateur pour : *C:\MinGW\bin\gcc.exe* par exemple si votr fichier gcc.exe de MinGW se situe la bas

Pour utiliser les lignes de code dans le terminal, il faut ajouter le path en variable d'environnement sur votre ordinateur :

- Paramètre puis propriétés systèmes
- Variable d'environnement
- Path puis modifier
- Ajouter le nouveau Path : *C:\MinGW\bin\gcc.exe*

Ceci fonctionne sur windows (en tout cas sur le mien 🙂)

{% enddetails %}

J'ai du perdre environ 2h la dessus le temps de configurer VS Code puis mon ordinateur n'ayant jamais vraiment utiliser avant un langage nécessitant une compilation avant d'être lancé. Une fois que tout marchait avec l'extension de VS Code, j'ai de nouveau eu des soucis 3h après quand j'ai utilisé plusieurs fichier. Finalement je n'ai plus pu l'utiliser (ne me demandez pas pourquoi, je ne sais toujours pas) et je suis passé directement par des lignes de code dans le terminal pour compiler avec :

```
> gcc -c main.c -o main.o
> gcc -c multiplication.c -o multiplication.o
> gcc main.o multiplication.o -o main.exe
```

Finalement, j'ai enfin pu  me concentrer sur le code en parvenant a compiler les fichiers !

## Infos générales

### Introduction de variable et fonction

Le langage C est plus proche en écriture du Java que du python. C'est un langage ou il faut annoncer le type de chaque variable et de chaque fonction.

``` C
int variable ; //Variable pour un entier
float variable = 1.5 ; // Variable pour un floatant initialisée
int fonction(){ // Fonction retournant un entier
  return 1;
}
```

{% note %}

Il faut mettre un point virgule à la fin de chaque ligne d'instruction.

{% endnote %}

Voici les plages d'utilisation maximum de chacun des types étant du à l'espace de mémoire accordé :
![test](typeLangageC.png)*Tableau des tailles de chiffres possible en fonction du type, Openclassroom*

### Calcul

Pour le système de calcul standard, on retrouve les abréviations des autres langages tel que :

``` C
int variable = 2 ;
variable ++ ; // incrémente variable de 1
variable += 5 // ajoute 5 à variable 
variable *= 4 // multiplie variable par 4
```

{% info %}

Le nom du langage C++ découle du format de l'incrémentation en C (C=C+1 <=> C++). Ce nom a été choisi pour évoquer l'évolution du langage C mais c'est en réalité deux langages utilisés pour faire des choses différentes.

{% endinfo %}


### fonction

Pour une fonction qui ne renvoie rien on utilise l'indicateur *void*.

L'utilisation des fonctions d'affichage dans le terminal est assez différente de ce qui est fait en python ou en Java :

```C
int variable ;
printf("Quelle valeur voulez vous donner à la variable ?");
scanf("%d", &variable);
printf("Vous avez donnée la valeur %d", variable);
```

Ceci permet de demander la valeur puis d'afficher ce que l'utilisateur à écrit. on référence les variables dans l'affichage avec le % suivi du type de variable comme le tableau ci-joint :

![test](AffichageEnC.png)*Tableau des format en fonction du type, Openclassroom*

On peut rajouter le type **%s** pour les chaines de caractères ou **%c** pour un type char.

## Système de mémoire

### Fonctionnement de la mémoire système

Le cours d'openclassroom m'a permis d'apprendre beaucoup sur le fonctionnement de la mémoire.

Elle fonctionne sous forme de tableau avec une colonne contenant les adresses (des numéros de 1 à X) et une colonne associée contenant les espaces de stockage.

Lorsque l'on défini une variable, on demande à l'ordinateur un espace de stockage et on le réserve pour la valeur de la variable. On peut réserver cet espace en le laissant vide ou en l'initialisant directement avec une valeur mais dans tous les cas, l'espace est reservé dès la ligne de création de variable.

En C, il y a beaucoup de manipulation qui découle de ce fonctionnement. Le système de définition de variable en est un exemple :

```C
int variable;

scanf("%d", &variable); //le symbole & permet d'accéder à l'adresse de stockage de la variable
// On modifie ici la valeur dans la case associée à l'adresse de stockage de variable
```

Ce fonctionnement permet de définir des pointeurs.

### Pointeur

Un pointeur conssiste a définir une variable comme étant l'adresse d'une autre variable. Ceci est utilisé pour modifier une variable définie dans une fonction ou dans le main à un autre endroit (autre fonction).

En effet, avec un return à la fin d'une fonction on ne peut modifier qu'une variable mais graçe au pointeur cela n'a plus de limite.

``` C
int variable;
*pointeur = &variable ; // permet de définir le pointeur

printf("%d", pointeur); // affiche l'adresse de stockage de variable
printf("%d", *pointeur); // affiche la valeur de variable
```

C'est en utilisant le *pointeur dans d'autre fonction que l'on peut modifier la variable en dehors de l'endroit ou elle est définie dans avoir besoin de la retourner à la fin de la fonction.

{% details "Bilan Sprint 1" %}

J'ai vraiment bien aimé ce début de pok ou j'ai pu apprendre plein de choses autant sur le fonctionnement général d'un ordianteur que sur le code en C. J'ai découvert de 0 ce langage qui demande beaucoup de rigueur et j'ai bien aimé. J'ai par contre perdu beaucoup trop de temps pour parvenir a faire marcher la compilation du code au début et dès l'utilisation de fichiers multiples. J'espère donc que la première partie de ce compte rendu pourra bien aider les suivants à gagner du temps la dessus. Je n'ai donc pas eu le temps de finir le cours mais j'ai hate de le continuer au prochain sprint pour passer sur du dev de mon coté pour bien appliquer tout ce que j'ai appris.

{% enddetails %}

### Second Sprint
