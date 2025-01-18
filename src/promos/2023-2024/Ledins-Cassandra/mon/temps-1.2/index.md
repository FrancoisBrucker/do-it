---
layout: layout/mon.njk

title: "Bases en C"
authors:
  - Cassandra Ledins

date: 2023-18-10
tags: 
  - "temps 1"

résumé: "Apprendre les bases du C"
---

{% prerequis "**Prérequis**" %}

* des notions de programmation aident grandement
* de la patience sinon

{% endprerequis %}

## Introduction 

J'ai voulu développer mon champ de connaissance en programmation pour avoir plus d'outils à ma disposition pour aborder différents problèmes. J'ai pensé à apprendre le C ou le C++ (langage utilisé en développement de jeux vidéos, domaine qui m'intéresse). M. Brucker ayant suggéré d'apprendre le C d'abord, c'est ce que je vais faire ici. Cela me servira aussi pour mon alternance dans le milieu de l'intelligence artificielle, où on est parfois amenés à modifier des librairies écrites en C pour entraîner nos modèles.

Je pars de 0 dans ce langage. Je vais prendre le cours "Apprenez à programmer en C" d'OpenClassrooms, durée estimée 10h, de difficulté moyenne. **mettre lien** 

## A l'abordage !

On commence par nous rassurer et nous guider dans la création d'un projet C. **Je n'ai pas suivi les conseils exacts donnés** car j'avais envie de continuer à travailler dans VSCode et ils proposaient d'autres IDE.

On créé donc notre premier petit code "minimal" **main.c** qui a la tête suivante :

```c

/* Mon super programme de hacker 
Attention à vos mirettes*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
    printf("Hello world!\n"); //Ici, on veut impressioner en soirée mondaine en disant Bonjour monde.
    return 0;
}
```
**stdio.h** et **stdlib.h** sont des librairies avec lesquelles on travaille dans le code. Comme dans un code python où on import les librairies.
D'après ce que j'ai compris, stdio s'occupera de la gestion des standard input/output, et stdlib de l'exit.

On créé une fonction **main** qui sera exécutée en première par défaut. Elle retourne un "int" par convention (0) pour dire que tout s'est bien passé. 

{% note %}
Par lisibilité et car c'est fortement recommandé pour éviter les confusions, on doit donc, comme on le voit dans l'exemple, **déclarer le type de sortie** de la fonction.
{% endnote %}

Assez intuitivement, on retrouve les commentaires : sur une ligne avec **//** et sur plusieurs lignes avec **"/*"** et **"*/"**

A l'intérieur de la fonction entre crochets, on effectue deux choses : on print un message dans le terminal et on retourne 0 pour dire que ça s'est bien passé.

Mais avant d'observer ça, il va d'abord falloir compiler le code. Pour cela j'ai utilisé la commande gcc dans le terminal.

```
gcc main.c -o bonjour.exe
```

Ici, on utilise le compilateur gcc, sur notre fichier main.c que l'on vient d'écrire. Avec l'option -o, on indique que l'on veut compiler le tout sous forme d'un fichier exécutable que l'on veut appeler bonjour.exe.

Après avoir tapé cela dans le terminal, le fichier exécutable bonjour.exe apparaît dans notre dossier projet. Il ne nous reste plus qu'à taper son petit nom pour l'exécuter et voir la magie s'opérer (on s'assure d'écrire ./ devant le fichier pour que le shell sache qu'on parle d'un fichier et non d'une commande): 

```
./bonjour.exe

>Hello world!

echo $!

>0
```

On sait grâce au cours Linux/OPS comment vérifier le code de sortie, on voit que c'est 0. Donc on est super contents.

### Variables

Il y a plusieurs types de variables, et on doit également déclarer leurs types à la création. Il y a des variables pour les entiers (**int**, **long**, **signed char**), et pour les float (**float**, **double**). Leur différence tient dans la place en mémoire qu'ils prennent, ils sont donc aussi limités dans leur grandeur. On peut aussi ajouter **unsigned** devant tout ça, si on veut déclarer un nombre positif, et avoir la possibilité qu'il soit plus grand. 

On peut annoncer au monde en quelle année on est, en utilisant les outils de remplacement de variable **%**. Après ce symbole, on ajoute une lettre pour indiquer de quel type de variable il s'agira. Ici **d** pour un entier int, **f** pour un float. 

```c
 int annee = 2023;
 float compotes_mangées = 2.5;
 printf("Hello world!\nNous sommes actuellement en %d\nJ'ai actuellement mangé %f compotes depuis le début de ce MON.\n", annee, compotes_mangées);
```
Après compilation et exécution (avec le reste du code qu'on a écrit plus haut) :

```
Hello world!
Nous sommes actuellement en 2023
J'ai actuellement mangé 2.500000 compotes depuis le début de ce MON.
```

Pour les opérations mathématiques, ça ressemble à Python à ceci près que la division est automatiquement euclidienne entre 2 entiers. Pour avoir un résultat en float, il faudra diviser des floats. (5/2 = 2 mais 5.0/2.0 = 2.5). On va passer là-dessus.

On peut se servir de la variable dans une opération pour la redéfinir par exemple pour l'incrémentation:

```c
int pouet = 0;
pouet = pouet + 1;
```

Ce qui peut aussi être écrit avec :

```c
int pouet = 0;
pouet++
```

On peut aussi vouloir fixer une constante avec **const**. On ne pourra plus la modifier après sa déclaration !

```c
const int mes_compotes = 8; //PAS TOUCHE
```

Il existe aussi l'option **static** qui peut avoir 2 utilités : rendre une variable d'un fichier "locale" c'est-à-dire qu'elle ne sera pas accessible dans un autre fichier.
Ou si elle est utilisée sur une variable à l'intérieur d'une fonction, la variable ne sera pas "supprimée" à la fin de la fonction. Donc si elle est modifiée dans la fonction et que la fonction est ensuite rappelée, la fonction débutera avec la valeur **déjà modifiée** de la variable.

## Conditions

Pour les conditions c'est encore pareil que python à ceci près qu'on rajoute des accolades, des parenthèses et des points virgules.
```c
if (maConditionEstVraie)
{
  mesinstructions;
}
else if (uneAutreCondition)
{
  mesautresinstructions;
}
```
On a les comparateurs **==**,**<=**, et les opérateurs **&&**, **||**, **!**.

Pour éviter d'utiliser des conditions else if à la suite, on peut construire un **switch**:

```c
switch (mescompotes)
{
case 0:
  printf("Je suis dans la sauce");
  break;
case 1:
  printf("Je suis pas à l'aise");
  break;
case 2:
  printf("Va falloir aller faire les courses");
  break;
default:
  printf("Tout va bien");
  break;
}
```

On peut **assigner** une valeur à une variable en fonction de si une **condition** est vérifiée ou non de cette sorte:

```c 
variable = (condition) ? valeur1 : valeur2;
```

## Boucles

Il y a 3 boucles différentes: while, do... while et for.

Avec tout ce qu'on a appris je décide de faire un code de braquage de compotes. Vous allez me donner toutes vos compotes maintenant.

{% details "Le code de mon braquage" %}

```c
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int mes_compotes = 0;
    int ses_compotes = 1000;
    printf("Ceci est un braquage de compotes, laissez-vous faire\nVous avez 1000 compotes et vous allez devoir m'en donner jusqu'à ce que je sois rassasiée.\n");
    printf("Votre but est de garder le maximum de vos compotes.\n");
    while (mes_compotes<457)
    {
        if (mes_compotes<=100)
        {
            printf("J'ai très très faim\n");
        }
        else if (mes_compotes<=200)
        {
            printf("J'ai faim\n");
        }
        else if (mes_compotes<=300)
        {
            printf("Encore un peu\n");
        }
        else if (mes_compotes<=440)
        {
            printf("Je suis presque rassasiée\n");
        }
        else
        {
            int compotes_restantes = (457-mes_compotes);
            printf("Donne-moi encore %d compotes\n", compotes_restantes);
        }
        printf("Il te reste %d compotes, combien veux-tu m'en donner ?\n", ses_compotes);
        int compotes_transit = 0;
        scanf("%d", &compotes_transit);
        mes_compotes = mes_compotes + compotes_transit;
        ses_compotes = ses_compotes - compotes_transit;
    }
    printf("*s'endort*\nTu as réussi à apaiser le monstre des compotes, et il te reste %d compotes !\n", ses_compotes);
    return 0;
}
```
{% enddetails %}


<img src=braquage.webp>

## Fonctions

On peut bien sûr créer des fonctions comme ceci :

```c
type maFonction(type arg1, type arg2, ..)
{
  mesInstructions;
}
```

Puis les appeler autre part :

```c
int main()
{
  type arg1 = valeur1;
  maFonction(type arg1);
}
```
## Headers et fonctions modulaires

On peut également créer des fichiers annexes de headers et d'autres fonctions, comme des librairies. 

Dans notre code, si on définit une fonction après la fonction main, cela ne marchera pas. Pour faire cela, il faut indiquer dans un header (donc au début du code) le format de la fonction. Pour notre braquage par exemple on pourrait créer:

```c
void braquage(int compotes_voulues);
```

On peut même créer la fonction dans un autre fichier, par exemple fonctions.c. On créé avec celà un fichier header fonctions.h, qui contient des directives préprocesseurs de protection :

{% details "fonctions.h" %}
```c
#ifndef fonctions_h
#define fonctions_h

#include <stdio.h>

void braquage(int mes_compotes);

#endif 
``````
{% enddetails %}

Puis ensuite le fichier fonctions.c, dans lequel on explicite la fonction braquage:

{% details "fonctions.c" %}
```c
#include "fonctions.h"

void braquage(int compotes_voulues)
{
     int mes_compotes = 0;
    int ses_compotes = 1000;
    printf("Ceci est un braquage de compotes, laissez-vous faire\nVous avez 1000 compotes et vous allez devoir m'en donner jusqu'à ce que je sois rassasiée.\n");
    printf("Votre but est de garder le maximum de vos compotes.\n");
    while (mes_compotes<compotes_voulues)
    {
        if (mes_compotes<=100)
        {
            printf("J'ai très très faim\n");
        }
        else if (mes_compotes<=200)
        {
            printf("J'ai faim\n");
        }
        else if (mes_compotes<=300)
        {
            printf("Encore un peu\n");
        }
        else if (mes_compotes<=440)
        {
            printf("Je suis presque rassasiée\n");
        }
        else
        {
            int compotes_restantes = (compotes_voulues-mes_compotes);
            printf("Donne-moi encore %d compotes\n", compotes_restantes);
        }
        printf("Il te reste %d compotes, combien veux-tu m'en donner ?\n", ses_compotes);
        int compotes_transit = 0;
        scanf("%d", &compotes_transit);
        mes_compotes = mes_compotes + compotes_transit;
        ses_compotes = ses_compotes - compotes_transit;
    }
    printf("*s'endort*\nTu as réussi à apaiser le monstre des compotes, et il te reste %d compotes !\n", ses_compotes);
}
```
{% enddetails %}

On appelle ce fichier annexe dans les headers de la fonction main comme suit :

```c
#include <stdio.h>
#include <stdlib.h>
#include "fonctions.h"

int main()
{
    braquage(457);
    return 0;
}
```

On oublie pas de compiler l'ensemble des fichiers en .c en tapant:

```
gcc main.c fonctions.c -o test.exe
```
Et maintenant notre test fonctionne **exactement** comme toute à l'heure ! Sauf que notre fonction main est plus propre et pourra être complexifiée.


## Pointeurs 

Une variable est toujours stockée à une adresse. Un pointeur c'est un outil qui stocke l'adresse mémoire d'une variable. On le déclare avec le type de la variable et une étoile. On peut récupérer l'adresse d'une variable avec **&**.

```c
int variable = 0;
int *pointeur = &variable;
```
Maintenant le côté surprenant (en tout cas pour moi), c'est qu'afficher *pointeur retourne la valeur de la variable, et afficher pointeur retourne l'adresse de la variable.

On ainsi modifier depuis n'importe où la valeur de notre variable :
```c
*pointeur = 1;
printf("%d", variable);
```

Ce code retournera 1.

## Tableaux

On peut créer un tableau, de taille fixe, avec des crochets. On peut initialiser des valeurs ou non, les changer une par une. On peut aussi jouer avec les pointeurs : toutes les cases du tableaux sont stockées dans des **adresses succintes**, sachant que la première valeur se récupère à l'adresse indiquée par le nom de la variable. On ne peut stocker que des variables du **même type** dans un tableau.

```c
int monTableau[3];
monTableau[0] = 1;
*(monTableau + 1) = 2;
monTableau[2] = 3;
```

## Conclusion

Ca a été très intéressant pour moi de découvrir C et les concepts de pointeurs, de les appliquer dans des exercices. Ca a aussi permis de débloquer des problèmes de compréhension que j'avais dans les scripts en général (javascript ou shell). Je recommande vivement le cours d'OpenClassroom pour qui veut s'aventurer au C.