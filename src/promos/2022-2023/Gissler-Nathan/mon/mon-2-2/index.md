---
layout: layout/mon.njk

title: "Unix"
authors:
    - Nathan Gissler

date: 2023-01-25

tags:
  - 'temps 2'
  - 'unix'
---

<!-- début résumé -->

Pour ce MON, je vais apprendre à utiliser les commandes Unix utiles.

<!-- fin résumé -->

## Ressources utilisées

Pour apprendre les commandes shell Unix, j'ai utilisé ce [tutoriel](https://www.tutorialspoint.com/unix/unix-getting-started.htm), accessibles pour les débutants avec Unix.

Les commandes peuvent être testées même si l'on n'est pas sous unix, sur [ce site](https://www.tutorialspoint.com/codingground.htm) (inscription gratuite). Cependant, je n'ai pas réussi à créer de compte (l'email ne s'envoyait pas). J'ai donc utilisé [ce site](https://bellard.org/jslinux/vm.html?url=alpine-x86.cfg&mem=192) à la place.

## Connexion

Changer de mot de passe

    passwd

Savoir avec quel login on est connecté

    whoami

Savoir qui est connecté (plusieurs utilisateurs peuvent être connectés en même temps)

    users

ou

    who

ou

    w

Les deux derniers sont plus détaillés

Déconnexion

    logout

## Gestion des fichiers

Lister les fichiers et dossiers dans le répertoire courant

    ls

Ajouter `-l` pour plus d'informations

Informations par colonne :
- type de fichier et permissions
- nombre de blocs mémoire occupés
- propriétaire (créateur) du fichier
- groupe auquel ce dernier appartient
- taille du fichier en bits
- date et heure de dernière modification
- nom

### Comment lire la première colonne ?

Le premier caractère indique le type de fichier :
- `\-` : fichier classique
- `b/c` : fichiers spéciaux
- `d` : répertoire
- `l` : fichier redirigeant vers un autre fichier
- `p/s` : autres types de fichiers spéciaux

Les 9 autres caractères représentent les permissions associées au fichier, elles sont détaillées plus loin.

### Métacaractères

Des métacaractères peuvent être utilisés dans les commandes pour remplacer des caractères : `?` pour exactement un caractère ou `*` pour n'importe quel nombre de caractères (qui peut être 0).

Exemples :

    $ls ch?.doc

Liste les fichiers dont le nom est de la forme `ch?.doc`, où `?` représente un seul caractère.

    $ls ch*.doc

Liste tous les fichiers dont le nom commence par `ch` et finit par `.doc`

### Fichiers cachés

Les fichiers cachés peuvent être listés avec l'option `-a`.

`ls -a` liste tous les fichiers cachés, dont le nom commence par `.`, ainsi que le fichier `.` qui représente le répertoire actuel et le fichier `..` qui représente le répertoire parent.

### Création et modification de fichiers

Pour ouvrir un fichier ou le créer s'il n'existe pas :

    vi nomdufichier

Une fois le fichier ouvert, on peut utiliser :
- `l` pour se déplacer dans le fichier vers la droite
- `h` pour se déplacer vers la gauche
- `k` pour se déplacer vers le haut
- `j` pour se déplacer vers le bas
- `i` pour rentrer en mode édition et modifier réellement le fichier
- `esc` pour sortir du mode édition
- `Shift + ZZ` (deux fois `Z`) pour fermer le fichier

### Autres opérations sur les fichiers

Afficher le contenu :

    cat nomdufichier

On peut ajouter `-b` pour avoir les numéros de lignes.

Compter les lignes/mots (il est possible de mettre plusieurs noms de fichier à la suite) :

    wc nomdefichier

Valeurs renvoyées :
- nombre de lignes
- nombre de mots
- taille en bits
- nom du fichier

Copier un fichier :

    cp nomdufichier nomdelacopie

Renommer un fichier (le fichier est en fait remplacé par un nouveau avec le nom spécifié) :

    mv anciennom nouveaunom

Supprimer un fichier :

    rm nomdufichier

On peut ajouter `-i` pour qu'une confirmation soit demandée avant la suppression.

## Répertoires

Se déplacer dans un autre répertoire :

    cd répertoire

Le répertoire peut être désigné par :
- un chemin absolu commençant par `/`
- un chemin relatif sans `/` au début
- `~` pour le "home directory"
- `~username` pour le "home directory" d'un autre utilisateur
- `-` pour le répertoire précédent

Se situer dans l'arborescence :

    pwd

Lister les fichiers du répertoire :

    ls

Auquel on peut ajouter un nom de répertoire si on ne veut pas le répertoire courant.

Créer un répertoire :

    mkdir nomdurépertoire

On peut aussi utiliser un chemin relatif ou absolu, et créer plusieurs répertoires d'un coup. Si le chemin utilise des répertoires inexistants il faut ajouter l'option `-p` pour ne pas avoir d'erreur et que ces répertoires soient créés.

Supprimer un répertoire :

    rmdir nomdurépertoire

Supprime un ou plusieurs répertoires, qui doivent être vides
renommer, comme pour les fichiers.

    mv anciennom nouveaunom

### Répertoires spéciaux

Les fichiers `.` et `..` représentent respectivement le répertoire courant et le répertoire parent (on peut les voir avec `ls -la`), on peut donc remmonter au répertoire parent avec `cd ..`, par exemple.

## Permissions

Les permissions associées aux fichiers sont représentées par 9 caractères, sous cette forme : `rwxrwxrwx`.

- `r` signifie `read` et représente la permission de lire le contenu du fichier
- `w` signifie `write` représente la permission de modifier le contenu du fichier
- `x` signifie `execute` et représente la permission d'exécuter le fichier

Pour un répertoire, `r` et `w` représentent la possibilité de voir et d'ajouter/supprimer des fichiers dans le répertoire. `x` permet à l'utilisateur d'utiliser `ls` et `cd`
dans la représentation `rwxrwxrwx`, chaque groupe de trois caractères représentent les permissions accordées à un type d'utilisateur :

1. le propriétaire
2. les membres du groupe associé au fichier
3. les autres utilisateurs

Une permission qui n'est pas accordée est représentée par `-`
par exemple, `rwx--x---` signifie que le propriétaire a toutes les permissions sur le fichier, que les membres du groupe associé peuvent l'exécuter, et que les autres utilisateurs n'ont aucune permission.

Modifier les permissions :

    chmod

On ajoute à la commande :
- `u` (propriétaire), `g` (groupe) ou `o` (autres utilisateurs)
- `+` (ajouter telles permissions), `-` (supprimer telles permissions) ou `=` (définir les permissions de telle manière)
- les lettres correspondant aux permissions correspondantes
on peut les permissions de plusieurs groupes d'utilisateurs en même temps

Par exemple :

En partant des permissions `r--rwx--x` et avec la commande `chmod u+x, g-rw, o = wx fichier`, on obtient les permissions `r-x--x-wx`.

On peut également utiliser `chmod 513 fichier` avec la numérotation suivante (où les permissions fonctionnent comme les représentations binaires des nombres associés) :
- 0 pour `---`
- 1 pour `--x`
- 2 pour `-w-`
- 3 pour `-wx`
- 4 pour `r--`
- 5 pour `r-x`
- 6 pour `rw-`
- 7 pour `rwx`

Changer le propriétaire ou le groupe :

    chown utilisateur fichier(s)

    chgrp groupe fichier(s)

`utilisateur` et `groupe` peuvent être remplacés par le nom ou l'ID correspondant.

Seul le propriétaire d'un fichier peut changer sa propriété (ou le super utilisateur `root` qui a toutes les permissions).

## Environnement

Créer une variable d'environnement :

    variable="contenu"

Accéder au contenu d'une variable d'environnement :

    echo $variable

Au lancement, le shell lit deux fichiers (s'ils existent) afin d'initialiser l'environnement : `/etc/profile`, géré par l'administrateur de la machine, et `.profile`, situé dans le "home directory" de l'utilisateur et pouvant être modifié par lui. Le fichier `.profile` nous permet d'initialiser notre environnement comme on le souhaite pour chaque démarrage du shell
type de terminal.

L'un des paramètres nécessaires au shell pour démarrer est le type de terminal, qui se trouve dans la variable d'environnement `TERM`. le shell peut ne pas reconnaître les commandes si ce paramètre est mal renseigné, on peut alors s'en sortir en définissant notre type de terminal de cette manière :

    TERM=vt100

Cette valeur est une sorte de dénominateur commun.

### Répertoire(s) des commandes

Les répertoires contenant les commandes pouvant être utilisées par le terminal sont stockés dans la variable `PATH`, par exemple
`PATH=/bin:/usr/bin`.

`:` sépare des répertoires, ici cela correspond donc aux répertoires `/bin` et `/usr/bin`.

### Modification du texte d'invite de commande (command prompt)

Le texte d'invite de commande est stocké dans la variable `PS1` et peut être modifié.

Quelques variables utiles peuvent être utilisées dans cette chaîne de caractère :
- `\t` pour l'heure en HH:MM:SS
- `\d` pour la date
- `\n` pour aller à la ligne
- `\s` pour l'environnement du shell
- `\W` pour le répertoire actuel
- `\w` pour le répertoire actuel (chemin complet)
- `\u` pour le nom d'utilisateur
- `\h` pour l'hôte de la machine
- `\#` pour le numéro de la commande actuelle
- `\$` pour le symbole $, ou # si on est connecté en tant que `root`

La variable `PS2` fonctionne de la même manière et contient les caractères d'invite de commande secondaire, apparaissant lors de commandes incomplètes.

Il existe un certain nombre d'autres variables d'environnement importantes utilisées par le shell pour gérer les chemins, les fuseaux horaires, générer des nombres aléatoires, etc.

## Impression de fichiers

La commande `pr` permet de reformater un fichier avant de l'afficher (sans altérer le fichier lui-même), et ce avec différentes options (affichage en colonnes, ajout d'un en-tête, modification des marges...).

La commande `lp` (ou `lpr`) permet ensuite d'imprimer le fichier sur papier.

`lpstat` et `lpq` donnent des informations sur la file d'attente d'impression.

`cancel` et `lprm` permettent d'annule une ou plusieurs impressions.

Les commandes d'impressions n'étaient pas reconnues par le shell que j'utilisais, probablement parce que c'est un shell en ligne. Je ne les ai donc pas testées.

## Envoie d'emails

La commande `mail adresse_destinataire` permet d'envoyer des emails.

On peut ajouter un objet (option `-s`), des cc (`-c`) et bcc (`-b`).

Le texte de l'email s'écrit ensuite avec `ctrl-D` en début de ligne et `.` en fin de message.

On peut voir les emails reçus avec la commande `mail` seule.

La commande `mail` n'était pas reconnue, comme les commandes d'impression.

## "Pipes" et filtres

Une "pipe" consiste à encaîner plusieurs commande en une seule ligne. on sépare pour cela les commande avec `|` et la sortie d'une commande devient l'entrée de la suivante.

La commande `grep` permet de rechercher des séquences de caractères (ou expressions régulières) dans les noms de fichiers et d'afficher les lignes correspondantes. Elle peut être combinée à `ls` pour ne pas avoir à spécifier les fichiers parmi lesquels chercher :

    ls | grep "séquence à rechercher"

Il existe plusieurs options supplémentaires à cette commande
la commande `sort` permet de trier par ordre alphabétique les lignes d'un fichier. Plusieurs options existent (pour trier numériquement, inverser l'ordre, ou encore ne pas prendre en compte la casse).

## Processus

Toutes les tâches exécutées sous Unix fonctionnent avec des processus. Dès que l'on lance une une commande dans le shell, un processus est créé. Chaque processus possède un identifiant unique à cinq chiffres (`pid`).

Les processus sont exécutés au premier plan par défaut mais peuvent aussi exécutés en arrière plan en ajoutant `&` à la fin de la commande. Un processus exécuté en arrière plan n'empêche pas d'autres processus de s'exécuter lorsqu'il attend une réponse de l'utilisateur contrairement aux processus au premier plan. Il attendra simplement d'être remis au premier plan et d'avoir une réponse.

On peut afficher la liste des processus en cours avec la commande ps (on peut ajouter `-f` pour plus d'informations).

Tuer un processus

On peut tuer un processus au premier plan avec `ctrl-C`, mais pour un processus en arrière plan, il faut récupérer son `pid` puis exécuter `kill pid` (en ajoutant `-9` si cela ne fonctionne pas).

Chaque processus a un parent, désigné par le `ppid` (parent process ID).

La commande `top` est une commande permettant de visualiser les processus de manière plus intéractive.

## Communication

On peut tester les connexions dans un réseau auquel on est connecté avec la commande `ping` à laquelle on ajoute le nom de l'hôte ou l'adresse IP.

Il existe d'autres outils de communication que l'on peut utiliser dans le shell, tels que `ftp` pour transférer des fichiers ou telnet pour travailler sur une machine à distance.

## Scripts

Il est également possible de ne pas se limiter à de simples commandes et d'écrire des scripts composés de suites d'instructions et exécutables par le shell. Je n'aurai pas le temps de détailler cette partie.