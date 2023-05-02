---
layout: layout/pok.njk

title: "Mon Portfolio chez OVH"
authors:
  - Jeffrey Edisah

date: 2023-01-04

tags:
  - 'temps 2'
  - 'info'
  - 'web'
  - 'back'
  - 'python'
  - 'flask'
  - 'ssh'
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

Le point le plus épineux de ce sprint a été la mise en place de la base de données avec SQLAlchemy que je n'arrive pas à mettre en place, et je ne comprends pas pourquoi. De fait, je n'ai pas pu tester le déploiement sur le serveur OVH de l'école car je veux avant tout une application fonctionnelle avec une base de données MySQL sur ma machine local

## Sprint 2

Les tâches que je veux faire pour mon 2ème sprint : 

- Connexion effective de ma base de données MySQL à mon application à l'aide de SQLAlchemy
- Déploiement sur le serveur OVH
- Fonction d'envoi de mail périodique

### Bilan

J'ai au final réussi à connecter ma base de données local à l'aide de SQLAlchemy et à avoir une base de données effectives. J'ai également pu déployer finalement mon projet sur le serveur OVH sur le lien [node.houblon.ovh1.ec-m.fr](http://node.houblon.ovh1.ec-m.fr) avec l'aide de M.Brucker, la configuration nginx Flask étant daté. 
Je n'ai par contre pas pu mettre en place l'envoi de mail périodique dans ma boîte mail avec le contenu actualisé de la base de données car la fin d'une session se fait sans l'envoi de requêtes. Je me pose la question de la pertinence de cet ajout, car il était surtout présent pour que je puisse toucher un peu aux sessions, ce que j'ai déjà pu voir à travers ce POK et un peu à travers mon projet 3A.

## Conclusion

Ce POK a été très instructif, tout comme ce temps, où j'ai pu toucher aux technologies back, à un serveur Linux, et voir à mon échelle la création d'une application de bout en bout, du développement au déploiement. En terme de gestion de projet, j'ai pu également voir que j'ai eu les yeux plus gros que le ventre au 1er Sprint, et que je n'ai pas su bien jauger l'ampleur des tâches que je voulais faire, j'ai été beaucoup plus raisonnable au 2ème sprint et je pense que j'arrive à cet équilibre où j'arrive à jauger ce que je dois faire comme il faut.

Le 2ème POK s'attellera à la programmation d'une galerie où je pourrais charger mes oeuvres (et d'autres images) pour les afficher sur mon site sans difficulté, ainsi qu'à une refonte du front, je ne sais pas à l'aide de quel framework (ou bien sans framework).
