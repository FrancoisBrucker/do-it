---
layout: layout/post.njk

title: "Mon Portfolio chez OVH"
authors:
  - Jeffrey Edisah

---
<!-- début résumé -->

Pour ce deuxième POK, je continue à travailler sur mon site portfolio en mettant cette fois l'accent sur le back et en le déployant sur le serveur OVH de l'école.

<!-- fin résumé -->

Voici le lien de mon repo GitHub : https://github.com/JeffreyEdisah/pok_serveur_distant

Les technologies que je veux utiliser sont : Flask, PostGreSQL, MongoDB, Bootstrap(?), Tailwind(?)

Ce que je veux concevoir dans ce deuxième POK :

- Une API pour recevoir les commissions et me les envoyer par mail
- Mise en place d'une base de données relationnelle pour les commissions
- Une session utilisateur, pour qu'un utilisateur ne puisse pas me faire plusieurs commissions à la suite (mais qu'il puisse corriger une erreur)
- Une API de gestion d'images pour que je puisse uploader mes oeuvres sur mon site
- Mise en place d'une base de données NoSQL MongoDB pour les images (à rechercher)
- (Sous réserve de temps) retravailler le front
- Déploiement fonctionnel du site sur le serveur OVH

## Sprint 1

Les tâches que je veux faire pour mon 1er sprint :

  - Une API pour recevoir les commissions et me les envoyer par mail
  - Mise en place d'une base de données relationnelle pour les commissions
  - Une session utilisateur de 24h, pour qu'un utilisateur ne puisse pas me faire plusieurs commissions à la suite (mais qu'il puisse corriger une erreur s'il s'est trompé)
  - Déploiement du site (non fini) sur le serveur OVH pour tester

### Bilan

La session a été mise en place, cependant je n'ai pas trouver un moyen d'envoyer de mail en fin de session car la fin de session se fait sans envoi de requête. J'essaierai de mettre en place une vérification périodique de ma base de données (hebdomadaire) et l'envoi d'un mail en cas de nouvelles entrées.

Le point le plus épineux de ce sprint a été la mise en place de la base de données avec SQLAlchemy que je n'arrive pas à mettre en place, et je ne comprends pas pourquoi. De fait, je n'ai pas pu tester le déploiement sur le serveur OVH de l'école car je veux avant tout une apllication fonctionnelle avec une base de données MySQL sur ma machine local

## Sprint 2

Les tâches que je veux faire pour mon 2ème sprint : 

- Connexion effective de ma base de données MySQL à mon application à l'aide de SQLAlchemy
- Déploiement sur le serveur OVH
- Fonction d'envoi de mail périodique
