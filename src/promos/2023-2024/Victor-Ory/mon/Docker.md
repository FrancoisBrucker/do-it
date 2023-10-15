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
- basic réseau ( port )

 {%endprerequis%}

### Résumé et Objectifs 

Ce MON est le premiers pas sur le chemin du devOps. En effet, Docker est un élément essentiel des systèmes d'informations actuelles.  Ainsi ce MON va essayer de nous familiariser avec les concepts et voir leurs interaction avec des éléments classiques d'une application web.


## Ce qu'on veut faire  :

- Dockeriser l'application que nous avons.
- Comprendre les processus pour la mettre en ligne sur un serveur cloud

# Let's go 

## Pourquoi utiliser Docker ? 

C'est un procédé de standardisation des applications pour pouvoir les déployer partout facilement.
On fait un package de l'applications, ses dépendances et sa configuration facilement transportable.
Deux éléments sont importants dans cet écosystème : les images et les containers.
L'image est le moule qui contient les dépendances, les configurations et l'image devient un container lorsque qu'elle est hébergée sur ton ordinateur.
Le container est un environnement en fonctionnement autour d'une image.
Une image peut être utilisé dans plusieurs container mais chaque container n'utilise qu'une image.
Chaque image est découpé en layer ou couche, ce qui permet lors de changement localisé de modifier seulement une layer et non l'ensemble de l'image.  

# Installation 

Pour l'installation, cela est très bien expliqué à travers du [Mon de Tuncay](/promos/2022-2023/Bilgi-Tuncay/mon/Docker), cela permet d'installer notamment le CLI, une façon de communiquer avec l'application docker à travers un terminal.

Ainsi après tout cela effectué, on eut commencer à travailler ! Car le travail c'est la vie.

### Mon application 

Pour ce cours, j'utilise une application que j'ai conçu pour un autre projet, mais elle peut être résumée par :

- une base de données MongoDB locale,
- une API en relation avec cette base de données en Express,
- un front en React

## On fait quoi avec ça ? 

Ainsi, l'objectif pour une application de ce genre est de créer un container à base d'un image adaptée à chaque composant. 
Pour cela, nous pouvons nous aider de [Docker Hub](https://hub.docker.com/), un répertoire d'image pour les différents usage avec une documentation associée souvent.

Une fois téléchargée, l'image peut être utilisé à travers ce genre de ligne de commande :

``` shell
docker run -phostport:containerport -d -e variable environnement 
```
La commande permet de créer un container à partir d'une image où  : 

- -p permet de faire le binding de port 
- -d permet de détacher le shell du cycle de vie du container 

Port binding : on associe un port à un container puis le lier à un port réel de l'ordinateur. 

### Classique Workflow : 

Le déroulement classique et simple qu'il pourrait y avoir :

- Développement en local
- Test en tout genre sur le projet ( compilation, test unitaire, ...)
- Création d'une image docker avec le projet incorporé ==> Publication de l'image sur un répertoire accessible par d'autres
- Déploiement du l'image sur un serveur dédié avec exactement la même configuration ==> Test des différentes fonctionnalités
- Feedback

# Les différents concepts de Docker : 

## Docker network :

Il est possible de créer un réseau fictif reliant les différents conteneurs qui peuvent héberger des éléments différents de la structure du site : Base de données, API backend, frontend, ... Cela permet de simplifier les échanges entre les différents composants du réseau et de s'abstenir de la complexité réel du réseau. 

## Docker Compose : 

Cela permet de gérer de multiples containers en même temps, d'automatiser leur mise en service, leur configuration et leur mise en relation. `Ces différents containers forment automatiquement un réseau. Les différentes manipulations sont codifiées et stockées dans un fichier facilement modifiable.
Ainsi au lieu de configurer chaque container avec des variables, des bindings de port, il devient possible de stocker la configuration voulue dans un fichier en .yaml qui réunit tout cela et l'automatise. une nouvelle image, cela permet de 

## Docker volume :

Les volumes sont des mémoires persistantes entre les différentes construction d'un container à partir d'une même image. Cela est essentielle si nous voulons créer une base de données par exemple. Si nous n'utilisons pas de volume, à chaque redémarrage du container à partir de l'image, les données de l'utilisation précédente ont disparus. Le volume Docker est donc un montage d'un espace du container sur un espace physique réel de l'hôte. L'espace du container renvoie directement à l'endroit en dehors du container et sur la machine, donc persistant, et cela permet de conserver les données au-delà des cycles de vie des containers.

## Automatisation et Process :

Cet ensemble de procédé et outils est donc un maillons essentiel de l'automatisation de process dans l'industrie de l'IT. Cela permet la coopération des différents employés, mettre en commun leurs modifications sur GitHub puis de créer une image avec la dernière version du produit avec sa configuration, ses dépendances grâce à un [Jenkinsfile](/promos/2022-2023/Bilgi-Tuncay/mon/Jenkins), un fichier dans lequel sont notés les instructions à effectuer après chaque modification. Cela permet par exemple ensuite de déployer automatiquement la dernière version du projet sur un serveur de test pour qu'une équipe de test vérifie le bon fonctionnement de chaque élément.

## Dockerfile

Un Dockerfile est un fichier d'instructions qui permettent de créer une image avec en plus notre projet par exemple, ainsi il sera plus facilement déployé sur d'autres serveurs. Ainsi, cela permet de créer une nouvelle image personnalisé et il devient possible de la partager avec d'autres, notamment en la mettant disponible sur le Docker Hub. 

Vous ne me croyez pas ?  Allez donc voir [mon répertoire Docker hub](https://hub.docker.com/r/hagard/frontexperisite)
