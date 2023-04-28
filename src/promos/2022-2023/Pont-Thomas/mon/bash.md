---
layout: layout/mon.njk

title: "MON 3 : Bash"
authors:
 - Thomas Pont

date: 2023-01-04

tags:
  - 'temps 2'
  - 'bash'
---

<!-- Début Résumé -->

Bash : utilisation d'une interface en ligne de commande
<!-- Début Résumé -->

## Introduction

Ce MON est destiné à des **débutants** en Bash. En effet, avant de débuter ce travail je n'avais que peu de connaissances sur le sujet.

Bash (ou Bourne-Again Shell) est un **interpréteur en ligne de commande**. C’est un Shell : il reçoit des commandes informatiques d’un utilisateur et les envoie au système d’exploitation pour que ce dernier les exécute. Il permet **d’utiliser son ordinateur de façon efficace** et de **réaliser des opérations complexes très rapidement**.
Il s’agit d’une **interface en ligne de commande** ou CLI (“Command Line Interface”).  L’utilisateur est face à un terminal dans lequel il entre ses lignes de commandes. La plupart des utilisateurs utilisent une interface graphique ou GUI (“Graphical User Interface”). C’est l’utilisation la plus classique de son ordinateur : avec l’accueil, le bureau, les icônes,... Même si une CLI peut être **plus complexe à maîtriser et moins intuitive**, elle est **plus puissante** qu’une GUI.
Par ailleurs Bash fonctionne généralement en **commande synchrone**. Cela signifie que les lignes de commande sont lues et exécutées une par une.

## Comment faire du Bash ?

Bash est conçu pour être utilisé sur un environnement Linux ou MacOS. On peut également en faire sur Windows mais, sans interpréteur, certaines fonctions peuvent être limitées.
Pour ce MON, j’ai utilisé Bash sur un système Linux en me **connectant à mon compte Centrale**. Pour cela j’ai lancé la commande suivante dans un terminal Windows Powershell:

```bash
ssh tpont@sas1.ec-m.fr
```

En entrant son mot de passe Centrale, on se connecte sur son environnement de travail Centrale.

Lorsqu’on est connecté, on peut voir que sa ligne de commande commence par :

```bash
[tpont@sas1 ~]$
```

Dans un premier lieu (avant le ~), il s’agit du **nom d’utilisateur**. Le signe “~” en fin de ligne indique que l’on se situe dans le **dossier home**. Le signe “$” quant à lui signifie qu’on est connecté en tant qu’**utilisateur classique**.
Afin d’apprendre les bases de Bash, j’ai suivi le cours suivant : [Apprendre à utiliser le shell Bash - Pierre Giraud](https://www.pierre-giraud.com/shell-bash/).

## Les principales commandes

Bash s’effectue en ligne de commande. Pour cela, il faut connaître les différentes commandes existantes. Sur certaines commandes, on peut rajouter des options. Cela permet d’avoir plus de fonctionnalités que la commande de base. Elles sont matérialisées par des "-".

### Principales commandes

Les **principales commandes** en Bash sont les suivantes :

- **pwd** : print working directory renvoie le **chemin** du répertoire courant
- **ls** : list files and directories renvoie le **contenu** d’un répertoire
- **cd** : change directory permet de se **déplacer** vers un nouveau répertoire

Par exemple,

```bash
[tpont@sas1 ~]$cd Documents
```

permet de se déplacer dans le dossier Documents. Ceci est matérialisé par l’invite de commande qui est désormais :

```bash
[tpont@sas1 ~/Documents]$
```

{% info %}
La commande **cd ..** permet de revenir dans le **dossier parent** de là où l'on se trouve.
{% endinfo %}

- **less** : **lit un fichier texte**. Pour quitter ce fichier texte il faut appuyer sur la touche q.
- **file** : donne le **type** d’un fichier
- **compgen** et plus particulièrement **compgen -c**: affiche **la liste de toutes les commandes** disponibles là où l’on se situe
- **man** : affiche une **description sur une commande** et explique comment l’utiliser. Il affiche également toutes les options que l’on peut ajouter à cette commande et leurs effets.
- **touch** ou **nano** : **crée un fichier texte**. Ce sont des exemples de commande. D'autres commandes permettent de le faire.
- **cp** : **copie** un fichier ou un répertoire

```bash
cp fichier1 fichier2
```

copie fichier1 et nomme la copie fichier2. Si fichier2 existait déjà, la précédente version en est écrasée.

```bash
cp fichier1 répertoire1
```

copie fichier1 et met cette copie dans répertoire1. On peut copier plusieurs fichiers dans un répertoire en mettant leurs noms les uns à la suite des autres.

Enfin, pour copier répertoire1 et mettre une copie dans un répertoire nommé répertoire2, on utilise la commande :

```bash
cp -R répertoire1 répertoire2
```

Comme précédemment si répertoire2 n'existait pas il est créé. Sinon, le répértoire2 déjà existant est écrasé.

{% attention "**Attention** aux espaces" %}
Si le nom du document ou du dossier comporte des espaces, pour que la commande puisse bien être interprétée, il faut mettre des \ avant les espaces ou des “ ” ou encore des ‘ ’  autour du nom du fichier ou du dossier.
Par exemple :

```bash
cp “ mon document.txt” Dossier
```

{% endattention %}

- **mv** : **renomme ou déplace** des fichiers et des répertoires dans d'autres fichiers et répertoires

```bash
mv fichier1.txt fichier.txt
```

renomme le fichier "fichier1.txt" en "fichier.txt".

```bash
mv fichier1.txt répertoire1
```

déplace le fichier "fichier1.txt" dans répertoire1. Cette commande fonctionne de manière identique pour déplacer un répertoire dans un autre répertoire.

- **rm** : **supprime** des fichiers ou répertoires

```bash
rm fichier1.txt
```

supprime "fichier1.txt" de manière définitive.

```bash
rm -r répertoire1
```

supprime le répertoire "répertoire1" et ce qu'il contient de manière définitive.

- **mkdir** : make directory **crée un nouveau répertoire**

```bash
mkdir nouveau_répertoire
```

crée un nouveau répertoire intitulé "nouveau_répertoire".

### Les extensions

Les commandes ci-dessus permettent de naviguer dans les fichiers et les répertoires. Cependant, ceci est également possible avec l'interface graphique. Mais, Bash permet également d'utiliser des **extensions**. Ceci permet de réaliser des **tâches plus complexes rapidement**. C'est par exemple le cas de l'utilisation de **métacaractères**.

Ainsi on peut **sélectionner des fichiers et/ou des répertoires** à l'aide de ces **métacaractères**.

Par exemple, la commande

```bash
cp *.txt Dossier
```

permet de copier tous les fichiers en .txt dans le répertoire Dossier.

L'accolade {} permet de réaliser une même action sur des motifs qui se répètent. Par exemple :

```bash
mkdir répertoire-{1,2,3,4}
```

permet de créer quatre répertoires numérotés de 1 à 4.

Par ailleurs, on peut à l'aide de la **substitution de commande** écrire plusieurs commandes sur une seule ligne.

```bash
mkdir $(seq 1 5)
```

permet d'engendrer une séquence des chiffres de 1 à 5 et à l'aide de la substitution de commandes de créer des répertoires numérotés de 1 à 5.

## Projet en Bash

Après avoir vu les commandes élémentaires et les avoir testées pour bien les comprendre, on peut réaliser un projet en Bash qui peut être pratique pour effectuer différentes tâches.

### Création d'un script en Bash

Pour lancer un script faisant appel à des commandes, on peut créer un script en Bash.
La commande suivante permet de le faire :

```bash
cd $HOME && touch script.sh && chmod +x script.sh
```

Ceci permet de se placer dans le dossier home, de créer un script "script.sh" et de l'ajouter dans la liste des scripts exécutables. Un script Bash doit commencer par :

```bash
#!/bin/bash'
```

pour pouvoir être exécuté correctement.
On peut écrire un script qui affiche "Hello world !" quand on le lance en utilisant la commande **nano**.

```bash
#!/bin/bash'
echo "Hello World !"
```

Le script ci-dessus affiche "Hello World !" quand on le lance, soit quand on effectue **./script.sh** dans l'invite de commande.

### Scripts plus complexes

L'idée est alors de réaliser des scripts plus compliqués permettant d'effectuer des tâches complexes. Une première idée est de réaliser un script qui cherchera et affichera toutes les occurrences d'un mot dans les fichiers texte d'un répertoire en indiquant leurs positions.

#### Recherche d'un mot clé dans les fichiers d'un répertoire

Ce script doit prendre en entrée deux arguments : un répertoire où chercher le mot clé et le mot clé.

On commence par vérifier que notre script prend bien deux arguments en entrée puis on cherche le mot clé dans les documents du répertoire.

```bash
if [ "$#" -ne 2 ]; then
    echo "Il n'y a pas le bon nombre d'argument. Veuillez entrer, un répertoire et un mot clé."
    exit 1
fi

fichiers=$(ls $1)

for fichier in $fichiers; do
  grep -n "$2" "$1/$file"
done
```

Ce script permet dans un premier temps de vérifier que le script prend bien deux arguments en entrée. En effet **$#** permet de connaître le nombre d'argument. Ensuite, la commande **grep -n** permet de renvoyer les lignes d'un document où un mot apparaît

{% attention "**Attention** aux opérateurs de comparaison" %}
Attention, pour la comparaison d'entiers, les opérateurs de comparaisons peuvent être retrouvés [ici](https://abs.traduc.org/abs-fr/ch07s03.html).

{% endattention %}

#### Gestionnaire de tâches

L'objectif est de créer un gestionnaire de tâches. Ce gestionnaire stockera une liste de tâches dans un fichier texte et permettra de stocker leur état (à faire, fait).

Pour ce faire, on crée un script *gestion.sh* et un fichier texte *tache.txt*.
On a besoin de plusieurs commandes pour faire fonctionner ce gestionnaire :

- **add** : pour ajouter une tâche (on doit vérifier qu'il y a bien une tâche à ajouter
- **do** : pour marquer la tâche faite (on doit vérifier que la tâche existe bien et n'est pas marquée comme effectuée)
- **undo** : pour modifier une tâche faite en non faite (on doit vérifier que la tâche existe bien et est marquée comme effectuée)

```bash
#!/bin/bash

case "$1" in
        "add")
                # code pour ajouter une tache
                if [ "$#" -eq 1 ]; then
                        echo "La tâche à ajouter ne peut pas être vide"
                        exit 1
                fi
                echo " $2" >> tache.txt
                echo "Tâche ajoutée"
                ;;
        "done")
                # code pour marquer une tâche effectué
                if [ "$#" -eq 1 ]; then
                        echo "Vous n'avez pas entré de tâche à valider"
                        exit 1
                fi

                if ! grep -iq "$2" tache.txt; then
                        echo "Cette tâche n'existe pas"
                        exit 1
                fi

                tache=$2
                #awk '/$2/{echo NR;exit}' tache.txt >> temporaire.txt
                #index=cat temporaire.txt
                #awk '/$2/{index_tache = NR;exit}' tache.txt

                if sed -n '$3p' tache.txt | grep -q '^X'; then
                        echo "La tâche a déjà été terminée"
                        exit 1
                fi

                sed -i .txt '$3s/^/X /' tache.txt
                echo "Tache marquée comme faite";;
        "undo")
                # code pour marquer une tâche non faite
                if [ "$#" -eq 1 ]; then
                        echo "Vous n'avez pas entré de tâche."
                        exit 1
                fi

                if ! grep -iq "$2" tache.txt; then
                        echo "Cette tâche n'existe pas"
                        exit 1
                fi

                if ! sed -n '$3p' tache.txt | grep -q '^X'; then
                        echo "La tâhe n'est pas terminée"
                        exit 1
                fi

                sed -i .txt '$3s/^X //' tache.txt
                echo "Tâche marquée comme non finie"
                ;;
esac
```

Ce code permet d'ajouter une tâche, de marquer une tâche comme faite et comme non faite.

Il possède néanmoins un problème. Je n'arrive pas à récupérer le numéro de ligne d'un texte dans mon script. J'arrive à le faire directement dans l'invite de commande grâce à la commande suivante :

```bash
awk '/$2/{echo NR;exit}' tache.txt >> temporaire.txt
```

Cela permet de stocker la valeur dans un fichier temporaire et de la récupérer grâce à la commande cat. Ainsi, il est ici nécessaire d'entrer la ligne de la tâche pour les commandes *done* et *undo* en troisième paramètre.

## Autres ressources utilisées

- [Comment créer un script exécutable](https://blog.desdelinux.net/fr/bash-como-hacer-un-script-ejecutable/)
- [La commande grep](https://docs.oracle.com/cd/E19620-01/805-1608/6j1io9lh3/index.html#:~:text=La%20commande%20grep%20est%20souvent,%C3%A0%20l'aide%20de%20grep%20.)
- [Script bash avec des arguments](https://www.lemagit.fr/conseil/Administration-Linux-creez-des-scripts-qui-prennent-en-compte-des-arguments)
