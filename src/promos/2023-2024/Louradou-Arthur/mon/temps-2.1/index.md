---
layout: layout/mon.njk

title: "Docker"
authors:
  - Arthur Louradou

date: 2023-09-18

tags: 
  - "temps 2"

résumé: "Sur la base des travaux de mes camarades des années précédentes, se former à Docker et à son utilisation dans un contexte de production."
---

## Prérequis

Des bases en Linux seront nécessaires pour le suivi de ce MON le plus confortablement. Je tâcherai autant que possible de vulgariser les termes utilisés et d’expliquer pourquoi nous mettons en place les architectures que nous allons voir.

Autrement, pas de prérequis si ce n’est de l’intérêt pour l’administration système et le déploiement d’applications sous forme de micro-services !


## Objectifs

Les objectifs de cette réalisation sont les suivants :
- Lire la documentation écrite par les élèves des années précédentes
- Choisir les ressources pertinentes
- Se former à Docker avec les ressources établies
- Mettre en pratique les connaissances acquises en parralèle de l'apprentissage


## Autres MONs

[Docker - Tunçay](../../../../2022-2023/Bilgi-Tuncay/mon/Docker/)

[Docker - Victor](../../../Victor-Ory/mon/Docker/)

## Les bases de Docker

S’entrainer avec Docker sans l’installer sur ma machine :

https://labs.play-with-docker.com/

Par la suite, j'ai changé la configuration de ma machine pour pourvoir installer Docker Desktop et profiter pleinement du MON pour mettre en pratique les tutoriels et documentations consultées.

### Cheat Sheet des commandes apprises au cours du MON (vidéo)

La base, par exemple pour installer une distribution Linux partielle comme fedora :

```bash
docker pull fedora
docker run fedora <commande à exécuter dans le Docker>
docker run --interactive --tty fedora
```

Cette dernière commande (-i -t) ouvre un terminal interactif dans le container : ces options sont plus utilisées à des fins de debug que de production mais permettent de voir ce qui se passe dans le container en direct et interagir avec.

### Création d’un DockerFile : exemple d’application

Afin d’automatiser les actions à exécuter à la création de notre image Docker, nous pouvons créer un fichier qui dira à Docker quelles actions effectuer pour créer notre container.

La vidéo nous invite donc, après avoir installé DockerDesktop sur notre machine, à créer un fichier DockerFile qui se présente comme cela :

```docker
FROM fedora
RUN yum install -y figlet
```

Pour reprendre l’exemple du cours, voici comment installer la bibliothèque Figlet (un exemple de commande qui affiche des mots en text-art) avec la commande [yum](https://access.redhat.com/articles/yum-cheat-sheet) (un peu comme aptitude pour installer des paquets sur Fedora).

Ensuite, depuis le terminal, à partir du moment où il y a le fichier `Dockerfile` dans le répertoire courant, nous pouvons exécuter la commande suivante avec `-t nom_de_l'image` pour nommer l’image docker nom_de_l’image. Appliqué à notre exemple, cela donne :

```bash
docker build -t figlet ./
docker run figlet
```

### La commande CMD : exécuter une commande dans le Docker

Il convient avant d’exécuter nos premiers scripts de définir un entrypoint, qui définit une valeur par défaut à la commande CMD.

Exemple :

```docker
ENTRYPOINT ["figlet"]
CMD ["Hello World!"]
```

Pour plus de détails sur la syntaxe, voir [Référence CMD dans la documentation Docker](https://docs.docker.com/engine/reference/builder/#cmd)  et [Référence ENTRYPOINT dans la documentation Docker](https://docs.docker.com/engine/reference/builder/#entrypoint).

Où le entrypoint est la commande à exécuter et le CMD la valeur optionnelle en l’absence de paramètre à l’exécution de l’image docker.

→ C’est parti pour le test sur play-with-docker, en n’oubliant pas d’enregistrer le fichier Dockerfile sur lequel repose tout le service créé.

```docker
FROM fedora
RUN yum install -y figlet
ENTRYPOINT ["figlet"]
CMD ["Hello Word!"]
```

Résultat :

```bash
$ docker run figlet                                                             
 _   _      _ _        __        __            _ _ 
| | | | ___| | | ___   \ \      / /__  _ __ __| | |
| |_| |/ _ \ | |/ _ \   \ \ /\ / / _ \| \__/ _` | |
|  _  |  __/ | | (_) |   \ V  V / (_) | | | (_| |_|
|_| |_|\___|_|_|\___/     \_/\_/ \___/|_|  \__,_(_)
                                                   
$ docker run figlet coucou!
                                 _ 
  ___ ___  _   _  ___ ___  _   _| |
 / __/ _ \| | | |/ __/ _ \| | | | |
| (_| (_) | |_| | (_| (_) | |_| |_|
 \___\___/ \__,_|\___\___/ \__,_(_)
```

### Construire une image Python

Nous allons mettre en pratique les acquis précédent pour construire une application avec un Dockerfile un peu plus élaboré. Il s’agira de construire une image Python et de la configurer pour la mettre en réseau et d’y accéder. Pour cela, nous allons utiliser un back-end en Django.

Avec l’aide de quelques informations trouvées en ligne, on peut déployer l’application en quelques minutes : https://dockerize.io/guides/python-django-guide.

Une fois dans le répertoire du projet :

```bash
docker build -t python-django-app .
docker run -t python-django-app
```


> Mon application n’est pas accessible depuis le port 8000 où elle est censé être déployée d’après ce qu’indique le container. Pourquoi ?


Nous allons aborder ce point dans la partie suivante.

### Gestion du réseau

Ici, il s’agira de mettre en place l’ouverture des ports pour accéder au service depuis sa machine (et pas seulement depuis le container en question). Par exemple, `-p (--publish) 8000:8000` redirige le port 8000 du container vers le port 8000 de la machine hôte.

Or mon port 8000 est bien le port de l’app Django par défaut dans le container Docker. J’y accèderai donc sur ma machine à l’adresse `localhost:8000`.

### Faire persister la donnée

Jusqu’ici nous avons vu que les `docker build` généraient toujours la même image avec une suite d’instructions. Dès lors, on peut se demander comment une suite d’instruction déterministe pourrait donner un résultat différent avec des données différentes dans le cas où une image serait relancée. C’est pour cela que Docker gère **les volumes**.

La documentation indique ceci pour se lancer :

```bash
docker volume create todo-db
docker run --mount type=volume,src=todo-db,target=/etc/todos getting-started
```

Ces deux commandes ont pour but d’attacher le fichier `/etc/todos/todo.db` à notre container Docker lors de sa création. De la sorte, lorsqu’il est crée ou arrêté, il gardera le fichier `.db` en mémoire hors de l’image Docker, dans le Volume.

Il existe aussi les volumes de type “Bind Mounts”, qui permets de partager un dossier de la machine hôte sur le conteneur exécuté.

```bash
docker run -it --mount type=bind,src="$(pwd)",target=/src ubuntu bash
```

### Aller plus loin dans la gestion du réseau (et Docker Compose…)

Il est possible de procéder de deux manières pour faire communiquer deux conteneurs entre eux, d’abord en démarrant le container avec un réseau attaché ou bien en connectant un container en cours d’exécution au réseau. Dans tous les cas, on commence par la commande :

```bash
docker network create mon-application
docker run \
		--network mon-application \
		--network-alias mysql \
		--volume mon-app-mysql-data:/var/lib/mysql \
		mysql
```

> Petit point cependant, l’argument `--volume` s’utilise comme ceci :
`docker run --volume <chemin_hote>:<chemin_conteneur> nom_de_l_image`
C’est donc une simplification de la syntaxe de `--mount`
>

Ensuite, nous pouvons utiliser Docker Compose pour automatiser la mise en place des applications multi-conteneur.

Nous explorerons ces possibilités sur des mises en pratiques concrètes et des déploiements avec un orchestrateur dans le prochain MON que je vous invite à lire si celui-ci a retenu votre attention.

### Mettre en ligne l’image Docker sur Docker Hub

Dans cette partie, nous allons nous interroger sur la façon de sauvegarder le travail accompli sur notre image Docker de test. Pour cela, nous utiliserons un repo à la manière de Github pour y placer nos images et les récupérer depuis n’importe quelle machine autorisée.

Alors, après avoir créé mon repo appelé tutorial-1, nous pouvons exécuter ceci :

```bash
docker image tag figlet alouradou/tutorial-1:latest
docker image push alouradou/tutorial-1
```

Pour voir le résultat sur docker hub : [https://hub.docker.com/repository/docker/alouradou/tutorial-django/](https://hub.docker.com/repository/docker/alouradou/tutorial-django/general)

## Regard critique et ouverture

Nous avons ici abordé les points de compréhension de Docker et de la mise ne place de containers. Pour déployer des applications plus complexes, nous allons ensuite approfondir la notion d’orchestrateurs pour lancer nos conteneurs Docker de façon redondante.

À voir : **[Kubernetes Crash Course for Absolute Beginners](https://www.youtube.com/watch?v=s_o8dwzRlu4)**.

Durant le prochain MON, nous chercherons d’autres contenus de ce type pour Kubernetes et Elastic Search.

## Bibliographie

[1] Vidéo du MON de Tunçay :
[YouTube - Getting Started with Docker - Docker](https://www.youtube.com/watch?v=gAGEar5HQoU)

[2] Vidéo recommandée par Victor dans son MON :
[YouTube - Docker Tutorial for Beginners [FULL COURSE in 3 Hours] - TechWorld with Nana](https://www.youtube.com/watch?v=3c-iBn73dDE)

[3] Documentation Docker :
https://docs.docker.com/get-started/

[4] Exemple de déploiement d’une application réelle :
[YouTube - 95% des devs ne connaissent pas cette façon de déployer une application - Benjamin Code](https://youtu.be/10UU6umqqv8?si=RUJAD5NFs57oSnzK&t=496)
