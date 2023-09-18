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
docker run -phostport:containerport -d 
'''