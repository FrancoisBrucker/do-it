---
layout: layout/post.njk

title: "MON 3 : Bash"
authors:
 - Thomas Pont

tags: ['Bash']
---

<!-- Début Résumé -->

Bash : utilisation d'une interface en ligne de commande
<!-- Début Résumé -->

## Introduction

Ce MON est destiné à des débutants en Bash. En effet, avant de débuter ce travail je ne connaissais pratiquement rien sur le sujet.

Bash (ou Bourne-Again Shell) est un **interpréteur en ligne de commande**. C’est un Shell : il reçoit des commandes informatiques d’un utilisateur et les envoie au système d’exploitation pour qu’il les exécute. Il permet **d’utiliser son ordinateur de façon efficace** et de **réaliser des opérations complexes très rapidement**.
Il s’agit d’une **interface en ligne de commande** ou CLI (“Command Line Interface”).  L’utilisateur est face à une “grande boîte noire” dans laquelle il peut entrer ses lignes de commandes. La plupart des utilisateurs utilisent une interface graphique ou GUI (“Graphical User Interface”). C’est l’utilisation plus classique de son ordinateur avec l’accueil, le bureau, les icônes,... Même si une CLI peut être **plus dure à maîtriser et moins intuitive**, elle est **plus puissante** qu’une GUI.
Par ailleurs Bash fonctionne généralement en **commande synchrone**. Cela signifie que les lignes de commande sont lues et exécutées une par une.

## Comment faire du Bash ?

Bash est conçu pour être utilisé sur un environnement Linux ou MacOS. On peut également en faire sur Windows mais sans interpréteur certaines fonctions peuvent être limitées.
Pour ce MON, j’ai utilisé Bash sur un système Linux en me **connectant à mon compte Centrale**. Pour cela j’ai lancé la commande suivante dans mon terminal Windows Powershell:

```bash
ssh tpont@sas1.ec-m.fr
```

En entrant son mot de passe Centrale, on se connecte sur son environnement de travail de Centrale.

Lorsqu’on est connecté, on peut voir que sa ligne de commande commence par:

```bash
[tpont@sas1 ~]$
```

Dans un premier lieu (avant le ~), il s’agit du **nom d’utilisateur**. Le signe “~” avec rien derrière indique que l’on se situe dans le **dossier home**. Enfin, le signe “$” signifie qu’on est connecté en tant qu’**utilisateur classique**.
Afin d’apprendre les bases de Bash, j’ai suivi le cours suivant : [Apprendre à utiliser le shell Bash - Pierre Giraud](https://www.pierre-giraud.com/shell-bash/).

## Les principales commandes

Bash s’effectue en ligne de commande. Pour cela, il faut connaître les différentes commandes existantes:

- **#** : commentaire (tout  le texte situé après ce signe sera ignoré par le terminal)
- **pwd** : renvoie le chemin du répertoire courant

Par exemple, si on entre la commande suivante :

```bash
[tpont@sas1 ~]$ pwd
```

Le système va nous répondre :

```bash
/users/home2/tpont
```

En effet, on est un utilisateur, home2 correspond aux élèves et tpont à ma session.

- **ls** : renvoie le contenu d’un répertoire
- **cd** : change directory permet de se déplacer dans un nouveau répertoire

Par exemple,

```bash
[tpont@sas1 ~]$ cd Documents
```

permet de se déplacer dans le dossier Documents. Ceci est bien matérialiser par l’invite de commande qui est désormais :

```bash
[tpont@sas1 ~/Documents]$
```

- **cp** : copie/colle un fichier

```bash
[tpont@sas1 ~/Documents]$ cp document.txt Dossier
```

copie document.txt qui est dans Documents et le colle dans Dossier qui est un dossier dans Documents.

{% attention "**Attention** aux espaces" %}
Si le nom du document ou du dossier comporte des espaces, pour que la commande puisse bien être interprétée il faut mettre des \ avant les espaces ou des “ ” ou encore des ‘ ’  autour du nom du fichier ou du dossier.
Par exemple :

```bash
[tpont@sas1 ~/Documents]$ cp “ mon document.txt” Dossier
```
{% endattention %}