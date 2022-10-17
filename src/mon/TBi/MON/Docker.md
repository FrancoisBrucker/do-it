---
layout: layout/post.njk

title: "MON de Tuncay : Jenkins ou Docker ?"
authors:
  - Tuncay Bilgi

tags: ['Docker']
---

# Docker :

Docker est un outil qui peut empaqueter une application et ses dépendances dans un conteneur isolé, qui pourra être exécuté sur n'importe quel serveur 
Il est largement utiliser dans la mise en production des appications.
Le MON consiste à prendre l'outil en main en suivant [la doc officielle]() et un workshop [officiel]().
Le but est d'en faire un maximum puisque l'on à moins de 10h sur ce MON.

{info} Le projet est mis en place sur Windows et je ne mettrais pas la doc pour Linux ou Mac. {enfinfo}
{attention} Les prérequis sont : les bases de bash et de Linux, l'utilisation d'un CLI {endattention}

## [Le Workshop]() :

### Initialisation et premiers pas.

Il faut installer Docker depuis  [le site officiel]().

Ensuite, on suit le workshop.

Docker permet d'empaqueter une application dans un conteneur, c'est à dire que le but est de créer, sur notre ordinateur, une boite isolée du reste du système. Cette boite va contenir le code de l'application que l'on veut mettre en production, et tout ce dont elle a besoin pour fonctionner.
Ces boites doivent donc possèder leur propre système d'exploitation. Nous n'allons pas recreer ce système nous même, mais nous allons le chercher sur DockerHub qui contient pleins d'images.

#### Hello World

Pour chercher une image, ici une image de la distribution Linux Fedora, on se place dans le répertoire de notre projet et on lance :

  docker pull fedora latest

Ensuite, pour notre premier hello world, on va effectuer une commande Linux avec le système fedora que l'on a téléchargé :

  docker run fedora echo 'hello world'

Cette commande va initialiser un container à partir de l'image fedora et va l'utiliser pour lancher un echo, puis va s'arreter.

on reçoit donc l'echo : 

  hello world

On peut utiliser cette commande avec des options à chercher dans docker --help .

{info}


    docker run --help //liste les commandes et les options
    -i  //maintenir le container ouvert après l'executions des tâches
    -t  //ouvrir un pseudo terminale
    -d  // exectuer les taches en deamon -> en arrière plan, dans un autre terminale.


{endinfo}

D'autres commandes importantes : 

    docker ps //liste tous les containers en marche
    docker stop [id] // arrete le container proprement
    docker kill [id] // force l'arret
    docker log -f [id] // renvoie tous les logs du container sur le terminale


#### Dockerfile

Une image est un template pour créer un container. Au lieu de simplement copier celle des autres, nous pouvons creer ou modifier les notre avec des Dockerfile.

On creer un Dockerfile dans le projet et on ouvre vscode dans le dossier courant :

    >> New-Item Dockerfile
    >> code .

On crée notre Dockerfile, il va chercher l'image fedora et lancer une commande pour nous qui va installer une dépendance, ici figlet, qui permet de faire de jolies echos.
Le Dockerfile ressemble à ça :

    FROM fedora:latest

    RUN yum install -y figlet

Enfin, on construit l'image dans le dossier courant (où il y a le Dockerfile) et on le nomme figlet :

    >> docker build -t figlet .


Nous voila avec une nouvelle image figlet, que l'o,=n peut utiliser pour instancier des containers comme au début du tutoriel!

{info} Les dockerfiles fonctionnent avec des mots clefs tel que FROM,RUN,CMD,ENTRYPOINT.. voir la doc pour savoir à quoi ils servent. {endinfo}

On peut publier notre image sur le dockerhub avec une commande spéciale :

    docker build -t mon_pseudo_docker/nom_image:latest .

Puis sur docker desktop on clique sur push to hub.



