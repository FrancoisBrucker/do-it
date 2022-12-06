---
layout: layout/post.njk

title: "POK de Thomas"
authors:
  - Thomas Pont

tags: ['pok']
---

<!-- début résumé -->

Mon  pok qui crée un site web chez moi
<!-- fin résumé -->

## Liste des POK

- [POK2](./poks/pok2)

## Objectif de ce POK

Pour le temps 2, je vais reprendre la suite de mon POK. L'objectif sera de le rendre fonctionnel ce qui a été réalisé en reliant le front et le back et en améliorant le visuel. Puis, le but sera de le déployer sur un serveur distant.

## Objectif jusqu'au prochain point POK

- corriger le site
- améliorer le visuel
- se renseigner sur les méthodes de déploiement à distance

## Travail réalisé

Après réflexions, j'ai décidé de repartir sur un nouveau site. En effet, relié le front et le back de mon site réalisé au temps 1 semblait trop ambitieux dans le temps imparti.

L'idée est alors de créer une page de connexion en statique (pages HTML) relié à une base de données des utilisateurs pour savoir si la personne peut bien se connecter ou non.

Les différentes étapes réalisées sont :
- le front (page de connexion, page d'inscription, page une fois connecté);
- le back (serveur en Java) avec des requêtes (ajout d'un utilisateur à la base de données, vérification qu'un utilisateur existe bien dans la base de données);
- déploiement du front sur le serveur;
- front et back reliés en local.

Le serveur est visible à l'adresse suivante : http://cannelle.ovh1.ec-m.fr/

Le front actuel et le back actuel reliés entre eux sont visibles aux adresses suivantes:
- https://github.com/ThomasP04/POK2
- https://github.com/ThomasP04/POK2-back

## Travail à faire pour le prochain point

- déploiement du back sur le serveur,
- ajouter du la sécurité au site (hachage des mots de passe, etc)


- [POK1](./poks/pok1)

## Objectif de ce POK

Dans ce POK, l'objectif sera de créer une messagerie privée utilisant du back et du front. Les utilisateurs pourront envoyer des messages entre eux.

## Listes des choses à faire

Afin de réaliser ce projet, plusieurs étapes sont nécessaires.
En effet, il faudra à la fois gérer la partie back et la base de données ainsi que le design du site.

## Objectifs pour le prochain point POK

Pour le prochain point POK, le but sera de faire un premier visuel pour le site.

## Point atteint au 1er point POK

Durant la première moitié du POK, j'ai pu apprendre les bases de React et faire un visuel pour la messagerie. On peut ainsi naviguer entre les utilisateurs et voir à qui on a envoyé quels messages.

## Objectif pour la fin du POK

Pour la fin du POK, le but sera de faire le back et d'avoir une base de données des utilisateurs et des messages.

## Travail réalisé jusqu'au 2ème point POK

Lors de cette seconde partie de mon POK je devais faire le back de mon site. J'ai fait un serveur réalisé en Express avec une base de données en Sqlite après des problèmes lors d'utilisation d'autres technologies.
Les requêtes effectuées sur ce serveur à l'aide de Postman fonctionne. Cependant, je n'ai pas encore réussi à connecter mon front et mon back. En effet, les requêtes effectuées une fois sur mon front reviennent vide.

## Pistes d'amélioration

Relier le front et le back.

## Liens vers le code

[Github du front](https://github.com/ThomasP04/Mon-site-chez-moi)
[Github du back](https://github.com/ThomasP04/Mon-site-chez-moi-back)




## Suite du POK (temps 2)

Pour le temps 2, je vais reprendre la suite de mon POK. L'objectif sera de le rendre fonctionnel ce qui a été réalisé en reliant le front et le back et en améliorant le visuel. Puis, le but sera de le déployer sur un serveur distant.

## Objectif jusqu'au prochain point POK

- corriger le site
- améliorer le visuel
- se renseigner sur les méthodes de déploiement à distance
