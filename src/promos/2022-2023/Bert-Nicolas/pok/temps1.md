---
layout: layout/pok.njk

title: "Jeu Mots croisés - Temps 1"
authors:
  - Nicolas BERT
  - Jean-Baptiste DURAND

date: 2022-10-07

tags:
  - 'temps 1'
  - 'un site chez moi'
---

## Ce qu'on a prévu pour le 1er point POK

- *Découvrir* les framework pour le front : Svelte et TailwindCSS
  - [Tuto Svelte](https://svelte.dev/tutorial/basics)
  - [Tuto TailwindCSS](https://tailwindcss.com/docs/installation)
  - TailwindCSS avec Svelte : [lien 1](https://blog.logrocket.com/how-to-use-tailwind-css-with-svelte/), [lien 2](https://tailwindcss.com/docs/guides/sveltekit)
- Créer une *ébauche* de front en static
  - Créer une page avec des *éléments simples* 
  - Créer une page avec différents *components*
  - Commencer à structurer la page du projet
    - Component *grille*
    - Component *navbar*
    - Component *info utilisateurs*


## Ce qu'on a fait

- Découverte de Svelte et implémentation de TailwindCSS
- Création des différents composants + interaction (bind des variables, props)
- Style avec TailwindCSS + animations
- Création des différents pages (jeu, login, register)
- Début des tutoriels NestJS + génération du backend et docker compose.
- Réflexion sur le schéma d'entités (On va utiliser MySQL plutot que MongoDB)

## Ce qu'on a prévu pour le second point POK

- Découverte plus approfondie de NestJS
- Création des entités (User et Game)
- Création des routes associées si on fait une API REST ou bien création + paramétrage du endpoint si on utilise GraphQL
- Connexion du front avec le backend + modifications pour bon fonctionnement + ajout de la connexion et de la sécurité à l'aide des JWT

*Si on a le temps : essayer de faire un algo qui génère une grille à partir d'une liste de mots obtenue via une API externe*

## Ce qu'on a fait à la fin du temps 1

- Création du backend (DB + PHPMyAdmin) le tout fonctionnant avec Docker.
- Création des entités (User et Game)
- Connexion du backend avec la base de données
- Hashage des mots de passe en base de données
- Sécurisation de l'API via JWT (Guard)
- Connexion entre le front et le back avec stockage du token de connexion dans le localStorage
- Ajout de la mécanique de jeu dans le backend

## Ce qu'il reste à faire pour le temps 2

- Amélioration du code
- Finitions
- Création de l'algo de génération de grille avec appel à une API externe
- Amélioration de l'environnement Docker
- Création de fixtures ?
- Rédaction de tests unitaires ?
- Début de pipeline ?