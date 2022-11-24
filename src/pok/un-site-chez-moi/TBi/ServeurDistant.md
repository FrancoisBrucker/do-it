---
layout: layout/post.njk

title: "Artblog Déploiement"
authors:
  - Tuncay Bilgi

tags: ['pok']
---

# Déploiement sur un site distant.

Le but du POK est d'appréhender le déploiement de projets sur un serveur.
Ici, je vais spécifiquement déployer le site développé pendant le POK1 : Artblog, qui est un blog.

## Pré-requis

- Avoir un site à déployer.

- Avoir les connaisances pour se connecter à un serveur distant : 

    - CLI Unix
    - SSH
    - Git Terminal

- Avoir des connaisances de Dev Fullstack :

    - Projet à déployer qui est fait en JS avec React et Next.js

### Remarque :

Mon back étant hébergé sur un HeadlessCMS il n'y a pas besoin de déployer la BDD, je vais donc potentiellement créer un mini projet qui contient une BDD classique juste pour me frotter au déploiement complet d'une application.

## Objectifs finaux :

- Pouvoir acceder à mon site sur ovh1.
- Faire en sorte que le contenu se mette à jour sans nécéssiter de redéploiement.

# Gestion de Projet :

Organisation en deux sprints séparés par le point POK.

## Taches Premier sprint :

 - Explorer le serveur ovh1 pour voir comment marche le déploiement
 - Corriger les bugs majeurs du Artblog
 - Build une version du Artblog
 - Bonus : déployer un projet tout simple (Express + front + back + bdd) pour se faire les dents

## Backlog :

- Deployer Artblog sur ovh1
- Bonus : mettre en place une automatisation avec Jenkins.



