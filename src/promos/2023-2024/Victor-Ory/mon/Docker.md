---
layout: layout/mon.njk

title: "Cryptographie"
authors:
  - ORY Victor

date: 2023-09-16

tags:
  - 'temps 1'
  - 'Cryptographie'
---
# Résumé :



## Ressources :

- [La doc de Docker](https://docs.docker.com/)
- [Vidéo tutoriel de 3H](https://www.youtube.com/watch?v=3c-iBn73dDE)


## Pré-requis : 

{%prerequis 'Niveau débutant '%}

Pré-requis :

- Un site trop cool à mettre en ligne
- Un compte AWS gratuit 

 {%endprerequis%}

## Ce qu'on veut faire  :

- Dockerier l'application que nous avons 
- La mettre en ligne sur un serveur AWS 

### Let's go 

## Pourquoi utiliser Docker ? 

C'est un procédé de standardisation des applications pour pouvoir les déployer partout facilement.
On fait un package de l'applications, ses dépendances et sa configuration.
Deux éléments sont importants dans cet écosystème : les images et les containers. 
L'image est le moule qui contient les dépendances, les configurations et l'image devient un container lorsque qu'elle est hébergée sur ton ordinateur.
Le container est un environnement en fonctionnement autour d'une image. 
Une image peut être utilisé dans plusieurs container mais chaque container n'utilise qu'une image.
Chaque image est découpé en layer ou couche.  

## Truc cool 

Port binding : on associe un port à un container puis le lier à un port réel de l'ordinateur. 
-p permet de faire le binding de port et -d permet de détacher le shell du cycle de vie du container ==> pas besoin d'avoir un shell qui tourne en même temps que l'application.

''' shell
docker run -phostport:containerport -d -e variable environnement 
'''

# Classique Workflow : 

Développement en local ==> Continious Integration (Jenkins) crée un build et une image docker ==> image pushed to private repositories ==> deployement on deployement server 

# Docker network 

Il est possible de créer un réseau fictif reliant les différents conteneurs qui peuvent héberger des éléments différents de la structure du site : Base de données, API backend, frontend, ... 

# Docker Compose

Cela permet de gérer de multiples containers en même temps, d'automatiser leur mise en service, leur configuration et leur mise en relation. `Ces différents containers forment automatiquement un réseau. Les différentes manipulations sont codifiées et stockées dans un fichier facilement modifiable.
Ainsi au lieu de configurer chaque container avec des variables, des binding de port, il devient possible de stocker la configuration voulue dans un fichier en .yaml qui réunit tout cela et l'automatise. une nouvelle image, cela permet de 

# Docker volume 

Les volumes sont des mémoires persistantes entre les différentes construction d'un container à partir d'une même image. Cela est essentielle si nous voulons créer une base de données par exemple.

# CI/CD 

Cet ensemble de procédé et outils sont donc des maillons essentiels de l'automatisation de process dans l'industrie de 'IT. Cela permet la coopération des différents employés, mettre en commun leurs modifications sur GitHub puis de créer une image avec la dernière version du produit avec sa configuration, ses dépendances grâce à un Jenkinsfile, un fichier dans lequel sont notés les instructions à effectuer après chaque modification. Cela permet par exemple ensuite de déployer automatiquement la dernière version du projet sur un serveur de test pour qu'une équipe de test vérifie le bon fonctionnement de chaque élément. 

# Dockerfile 

Un Dockerfile est un fichier d'instructions qui permettent de créer une image avec en plus notre projet par exemple, ainsi il sera plus facilement déployé sur d'autres serveurs. 