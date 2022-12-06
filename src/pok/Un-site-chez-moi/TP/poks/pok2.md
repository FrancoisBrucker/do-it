---
layout: layout/post.njk

title: "POK 2 : Serveur distant"
authors:
 - Thomas Pont

tags: ['Serveur distant']
---

<!-- Début Résumé -->

Serveur distant
<!-- Fin Résumé -->

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
