---
layout: layout/mon.njk

title: "Docker"
authors:
  - ORY Victor

date: 2023-09-27

tags:
  - 'temps 1'
  - 'Docker'
  - 'DevOps'
  - 'Intermédiaire'
---

## Ressources :

- [La doc de Docker](https://docs.docker.com/)
- [Vidéo tutoriel de 3H](https://www.youtube.com/watch?v=3c-iBn73dDE)
- [MON de Tuncay](../../../2022-2023/Bilgi-Tuncay/mon/Docker.md)

## Pré-requis : 

{%prerequis 'Niveau novice '%}

Pré-requis :

- Un site à mettre en ligne
- Terminal
- basic réseau (port)
- Savoir ce qu'est Docker

{%endprerequis%}

### Résumé et Objectifs 

Ce MON est le premiers pas sur le chemin du DevOps. En effet, Docker est un élément essentiel des systèmes d'informations actuelles. Ainsi, ce MON va essayer de nous familiariser avec les concepts et voir leurs interactions avec des éléments classiques d'une application web.

## Ce qu'on veut faire :

- Dockeriser l'application que nous avons.
- Comprendre les processus pour la mettre en ligne sur un serveur cloud.

# Let's go 

## Pourquoi utiliser Docker ? 

C'est un procédé de standardisation des applications pour pouvoir les déployer partout facilement. On fait un package de l'applications, ses dépendances et sa configuration facilement transportable. Deux éléments sont importants dans cet écosystème : les images et les containers. L'image est le moule qui contient les dépendances, les configurations et l'image devient un container lorsque qu'elle est hébergée sur ton ordinateur. Le container est un environnement en fonctionnement autour d'une image. Une image peut être utilisée dans plusieurs containers, mais chaque container n'utilise qu'une image. Chaque image est découpée en layers ou couches, ce qui permet lors de changement localisé de modifier seulement une layer et non l'ensemble de l'image.  

# Installation 

Pour l'installation, cela est très bien expliqué à travers du [MON de Tuncay](/promos/2022-2023/Bilgi-Tuncay/mon/Docker), cela permet d'installer notamment le CLI, une façon de communiquer avec l'application Docker à travers un terminal.

Ainsi après tout cela effectué, on peut commencer à travailler ! Car le travail c'est la vie.

### Mon application 

Pour ce cours, j'utilise une application que j'ai conçue pour un autre projet, mais elle peut être résumée par :

- une base de données MongoDB locale,
- une API en relation avec cette base de données en Express,
- un front en React.

## On fait quoi avec ça ? 

Ainsi, l'objectif pour une application de ce genre est de créer un container à base d'une image adaptée à chaque composant. Pour cela, nous pouvons nous aider de [Docker Hub](https://hub.docker.com/), un répertoire d'images pour les différents usages avec une documentation associée souvent.

Une fois téléchargée, l'image peut être utilisée à travers ce genre de ligne de commande :

``` shell
docker run -phostport:containerport -d -e variable environnement 
```


La commande permet de créer un container à partir d'une image où :

- `-p` permet de faire le binding de port.
- `-d` permet de détacher le shell du cycle de vie du container.

Le port binding consiste à associer un port à un container, puis le lier à un port réel de l'ordinateur.

### Workflow classique :

Le déroulement classique et simple peut être le suivant :

1. Développement en local.
2. Tests variés sur le projet (compilation, test unitaire, etc.).
3. Création d'une image Docker avec le projet incorporé, suivie de la publication de l'image sur un répertoire accessible par d'autres.
4. Déploiement de l'image sur un serveur dédié avec exactement la même configuration, suivi de tests des différentes fonctionnalités.
5. Retour d'informations (feedback).

# Les différents concepts de Docker :

## Docker network :

Il est possible de créer un réseau fictif reliant les différents conteneurs, qui peuvent héberger des éléments différents de la structure du site : base de données, API backend, frontend, etc. Cela simplifie les échanges entre les différents composants du réseau et permet de s'abstraire de la complexité réelle du réseau.

## Docker Compose :

Docker Compose permet de gérer plusieurs conteneurs en même temps, d'automatiser leur mise en service, leur configuration et leur mise en relation. Ces différents conteneurs forment automatiquement un réseau. Les différentes manipulations sont codifiées et stockées dans un fichier facilement modifiable. Ainsi, au lieu de configurer chaque conteneur avec des variables et des bindings de port, il devient possible de stocker la configuration voulue dans un fichier .yaml qui regroupe tous ces éléments et les automatise.

## Docker volume :

Les volumes sont des mémoires persistantes entre les différentes constructions d'un conteneur à partir d'une même image. C'est essentiel lorsque l'on souhaite créer une base de données, par exemple. Si l'on n'utilise pas de volume, à chaque redémarrage du conteneur à partir de l'image, les données de l'utilisation précédente disparaissent. Le volume Docker est donc un montage d'un espace du conteneur sur un espace physique réel de l'hôte. L'espace du conteneur renvoie directement à l'emplacement en dehors du conteneur et sur la machine, ce qui le rend persistant et permet de conserver les données au-delà des cycles de vie des conteneurs.

## Automatisation et Process :

Cet ensemble de procédés et d'outils est un maillon essentiel de l'automatisation des processus dans l'industrie de l'IT. Il permet la collaboration entre différents employés, de mettre en commun leurs modifications sur GitHub, puis de créer une image avec la dernière version du produit, avec sa configuration et ses dépendances, grâce à un [Jenkinsfile](/promos/2022-2023/Bilgi-Tuncay/mon/Jenkins), un fichier dans lequel sont notées les instructions à effectuer après chaque modification. Cela permet ensuite de déployer automatiquement la dernière version du projet sur un serveur de test, où une équipe de test vérifie le bon fonctionnement de chaque élément.

## Dockerfile

Un Dockerfile est un fichier d'instructions qui permet de créer une image avec en plus notre projet, par exemple. Ainsi, il sera plus facilement déployé sur d'autres serveurs. Cela permet de créer une nouvelle image personnalisée et de la partager avec d'autres, notamment en la mettant à disposition sur le Docker Hub.

Vous ne me croyez pas ? Allez donc voir [mon répertoire Docker Hub](https://hub.docker.com/r/hagard/frontexperisite).

# Conclusion 

- La [vidéo](https://www.youtube.com/watch?v=3c-iBn73dDE) est super, pédagogue, couvre beaucoup de sujets, test réellement et ça c'est cool ! 
j'aimerais maintenant plus pratiquer et jouer avec dans un POK par exemple.
- La [documentation](https://docs.docker.com/) est très efficace pour le début. 
- Le [MON de Tuncay](../../../2022-2023/Bilgi-Tuncay/mon/Docker.md) aide bien pour commencer toutefois la vidéo permet de réellement se lancer et avoir un petit panorama.