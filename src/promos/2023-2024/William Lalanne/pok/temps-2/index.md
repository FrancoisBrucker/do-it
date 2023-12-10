---
layout: layout/pok.njk

title: "Titre du POK du temps 2"
authors:
  - William Lalanne

date: 1971-01-01

tags: 
  - "temps 2"

résumé: Ajout d'un back sur mon site de Memory avec Node.js et express.
---

## Objectifs de ce POK
Dans ce POK j'aimerais commencer à intégrer l'aspect backend au site que j'ai développé pour mon premier POK. Pour cela je vais utiliser Node.js et express sur lesquels je vais me former lors d'un MON. 

## Les étapes pour le Sprint 1
- Reprendre le front (parce que certains trucs sont pas top)
- Créer des popup pour la connexion et l'inscription
- Voir comment fonctionne MongoDB
- Création de la base de données sur MongoDB
- Création du serveur avec Node et Express

## Les étapes pour le Sprint 2
- Créer les requêtes pour permettre aux utilisateurs de s'inscrire, se connecter et se déconnecter
- Afficher l'historique des parties du joueur connecté 


## Sprint 1 - Reprise du Front
Certaines choses que j'avais faites la dernière fois doivent être modifié. D'abord je dois ajouter des boutons pour la connexion et l'inscription. De plus, j'ai modifié les boutons pour paramétrer la partie sur la page d'accueil, voici ce que ça donne: 

![Page accueil modifié](Page_Accueil.png)

Ensuite sur les pages de jeux, je trouvais que tous les éléments étaient trop gros, on ne voyait donc pas tous les éléments sur la page sans scrollé. J'ai fait en sorte de tout réduire:

![Page de jeu](Page_Jeu.png)

Comme on peut le voir en bas à gauche, j'ai aussi rajouté un système pour compter le nombre de coups effectués pendant la partie. Cela permet au joueur de comparer ses parties. 

## Popup pour s'inscrire et se connecter

Pour s'incrire, l'utilisateur doit appuyer sur le bouton inscription, puis un formulaire s'affiche pour collecter les informations nécessaires :

![Inscription](Inscription.png)

Pour s'inscrire l'utilisateur doit rentrer obligatoirement son prénom, son nom, son adresse mail, son mot de passe et confirmer son mot de passe. Il peut aussi, s'il le souhaite, ajouter une photo de profil. 



