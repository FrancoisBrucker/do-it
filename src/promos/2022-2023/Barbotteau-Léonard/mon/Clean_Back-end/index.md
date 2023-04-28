---
layout: layout/mon.njk

title: "Le MON-4 de Léonard"
authors:
  - Léonard Barbotteau
date: 2023-01-25

tags:
  - 'temps 2'
---

<!-- début résumé -->
Le Back-end pour les débutants, comment bien structurer le code.
<!-- fin résumé -->

## Sources
[Glossaire pour le jargon du développement](https://www.wholewhale.com/tips/developer-terms-glossary/)
[cours oppenclassroom](https://openclassrooms.com/fr/courses/6390246-passez-au-full-stack-avec-node-js-express-et-mongodb/6466459-optimisez-la-structure-du-back-end)
[Architecture du backend](https://www.codecademy.com/article/back-end-architecture)

# Introduction
Malgré les cours sur le back-end et meme après y avoir touché lors de mon POK, je remarque que je n'ai pas les bases pour vraiment comprendre comment fonctionne le back-end, à quoi il sert, comment structurer les fichiers entre eux et à quoi servent tous les fichiers que l'on peut voir dans un projet utilisant du back-end. Je connais une partie de ce que je vais annoncer, mais je préfère tout revoir afin de consolider mes connaissances et aussi si ce cours est amené à etre lu par autrui.
Les mots en gras sont affichés dans le lexique.

## A quoi sert le back-end?
Le backend (ou "côté serveur") est la partie du site Web que vous ne voyez pas. Elle est chargée de stocker et d'organiser les données et de s'assurer que tout ce qui se trouve du côté client fonctionne réellement. Le backend communique avec le frontend, envoyant et recevant des informations qui seront affichées sous forme de page Web.
Par exemple, chaque fois que vous remplissez un formulaire (login par exemple), que vous saisissez une adresse web ou que vous effectuez un achat (toute interaction avec le client), votre navigateur envoie une requête au serveur, qui renvoie des informations sous la forme d'un code frontal que le navigateur peut interpréter et afficher.
Pour alors réaliser un site, il faut écrire tout le back-end afin que l'on puisse en faire une application web dynamique, c'est-à-dire un site web dont le contenu peut changer en fonction de ce qui se trouve dans sa base de données et qui peut être modifié par les entrées de l'utilisateur.

## Fonctionnement du back-end
Le serveur exécute une application qui contient une logique sur la façon de répondre à diverses demandes en fonction du verbe HTTP et de l'identificateur de ressources uniformes (URI). La paire <b>HTTP</b>/<b>URI</b> s'appelle une route et leur mise en correspondance en fonction d'une demande s'appelle le routage.
Pour en savoir plus vous pouvez voir le début de mon [autre cours](../NodeSqlite/) qui parle de ces routes plus précisément.

## Les points auxquels bien faire attention
- En général, le serveur ne peut pas initier de réponses sans demandes (requests)
- Chaque demande nécessite une réponse, même s'il s'agit simplement d'un code d'état 404 indiquant que le contenu n'a pas été trouvé. Sinon, votre client sera laissé en suspens (en attente indéfinie).
- Le serveur ne doit pas envoyer plus d'une réponse par demande. Cela entraînera des erreurs dans votre code.

## La structure hiérarchique des fichiers dans le back-end
Les exemples donnés fonctionnent pour node.js

- Le fichier package.json, initialement vierge, qui contient le détails de tous les packages npm que l'on utilise dans le projet.
- Le fichier .gitignore qui va contenir les fichiers qui ne seront pas communiqués à github (les packages justement, qui pourront etre installés à l'aide du fichier précédent)
- Le fichier du serveur, par exemple server.js
- Le fichier contenant l'application, par exemple app.js
- Un dossier contenant les modèles pour la base de données
- Un dossier contenant les routes
- Un dossier contenant les controleurs


On va créer un dossier pour les routes et un dossier pour les controleurs, afin que le fichier principal (par exemple app.js) ne soit pas trop chargé, et afin de clarifier le code.

### Lexique des mots utiles pour développer
Ceci est une liste non exhaustive du jargon qui peut etre utilisé par les développeurs en back-end. Elle est amenée à etre complétée.

- <b>404</b> : Message d'erreur lorsque ce qui a été demandé ne peut être trouvé.
- <b>API</b> : Interface de programmation, c'est la façon dont les ordinateurs et les applications communiquent entre eux.
- <b>Attribut</b> : Informations sur les éléments d'un composant dans la conception/construction de votre site web.
- <b>Cache</b> : Le stockage de certains éléments permettant d'accélérer les temps de chargement pour les visiteurs réguliers du site. S'il y a un changement dans le site web il faut vider son cache pour qu'il n'y ait pas de conflit entre les deux versions. 
- <b>Champs</b> : Il s'agit de l'élément de base de la collecte de données. Il s'agit des unités de stockage que les visiteurs de votre site Web utilisent pour saisir leurs noms, adresses électroniques, notes, etc.
- <b>Classe</b> : Un plan pour créer quelque chose, un peu comme si on utilisait le plan d'une voiture existante pour créer un nouveau type de voiture.
- <b>Cookies</b> : Ce sont les données envoyées par un serveur Internet à un navigateur. À chaque fois que le navigateur accède au même serveur, il renvoie ces données afin de savoir comment (et combien de fois) il accède au serveur. 
- <b>CORS</b> : Un système de sécurité qui par défaut bloque les appels HTTP entre des serveurs différents.
- <b>Domaine</b> : L'adresse d'un site web telle qu'elle est saisie dans le navigateur.
- <b>HTTP</b> : Un ensemble de méthodes de requête pour indiquer l'action souhaitée à effectuer pour une ressource donnée.
- <b>ORM</b> : Un ensemble de classes permettant de manipuler les tables d’une base de données relationnelle comme s’il s’agissait d’objets.
- <b>Plan du site</b> : Plan de toutes les pages d'un site web, organisé par ordre hiérarchique.
- <b>URI</b> : Un élément permettant d'identifier une ressource. Une URL permet de localiser un élément, une URN est un identifiant unique dans le temps et l'espace pour une ressource.

