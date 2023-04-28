---
layout: layout/post.njk

title: "Jeu Mots croisés - Temps 2"
authors:
  - Nicolas BERT
  - Jean-Baptiste DURAND

tags: 
    - 'POK'
    - 'temps 2'
    - 'serveur distant'
---

## Choses à faire durant ce temps 2

- Finir la connexion entre le front et le back
- Améliorer le projet : 
  - Création de parties
  - Listes des parties jouées
  - Pages de statistiques sur les parties jouées ?
  - Finitions de styles
  - Génération de grilles + choix des lettres améliorés (voyelles) pour pas gagner trop d'argent quand même
  - Connecter la page de register au back plus redirection qui s'en suit
  - Solde dans la navbar
  - Responsive à checker partout
  - Recharge de solde
- Mettre en prod le projet + régler tous les problèmes possibles
- Passer en PostgreSQL pour matcher avec ce qu'il y a sur le OVH ?

## 1er Sprint

- Fixer les quelques erreurs pour un jeu fonctionnel mais pas "complet" (le minimum syndical).
  - Problème de connexion (accès et limitation des pages, refresh sur la page d'accueil pour la connexion effective)
- Déployer le front, le back et la BDD.

## Ce qui a été fait au 1er sprint

- Correction du login et register
- Protection des routes
- Lister les parties
- Passage à PostgreSQL
- Mise en production du projet dans l'état actuel sur le serveur OVH : (front dans `/www/`, back dans `/node/`) et connexion avec la base de données en PGSQL disponibles sur le serveur OVH. L'application est disponible sur [http://balasamite.ovh1.ec-m.fr](http://balsamite.ovh1.ec-m.fr)
- Fix de bugs

## 2e sprint

- Connexion de la partie entre le front et le back
- Améliorer le style et la responsivité
- Algorithme de génération de grilles
- Solde dans la navbar
- Autres améliorations
- Redéployer l'ensemble du projet avec les modifications effectuées

## Ce qui a été fait au 2ème sprint

- Amélioration du style et de la responsivité (à poffiner encore un peu)
- Algorithme de génération de grilles sour la forme d'un microservice appelé par le backend
- Solde dans la navbar en lien avec le solde en DB
- Recharge du compte
- Logout
- Redéploiement du projet

## Ce qu'il reste à faire pour le temps 3

- Amélioration du jeu (style, mécanique ...)
- Optimisation de l'algo de génération de grilles
- Écriture de tests ?
- Optimisation du déploiement (scripts ou pipeline)