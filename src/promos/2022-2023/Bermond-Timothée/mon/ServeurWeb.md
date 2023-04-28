---
layout: layout/mon.njk

title: "Publier son site sur un serveur web"
authors:
  - Timothée Bermond

date: 2023-01-04

tags:
  - 'temps 2'
  - 'Serveur web'
---

<!-- début résumé -->
Comment passer d'un site statique en local à un site publié sur un serveur grâce au [cours](https://francoisbrucker.github.io/cours_informatique/cours/web/) de Mr. Brucker.
<!-- fin résumé -->

## Prérequis

Pour ce MON, je maitrisais déjà la partie front (html, CSS et javascript), je ne la traiterais donc pas dans ce MON. Mais il est possible de se former sur cette partie avec les [MON Dev Web](https://francoisbrucker.github.io/do-it/mon/GB/) de Gabriel Barbé.

## Serveur Web

J'ai commencé par la partie serveur web qui se découpe en 2 partie :
- [Lire des données](https://francoisbrucker.github.io/cours_informatique/cours/web/lire-donn%C3%A9es/)
- [Serveur web](https://francoisbrucker.github.io/cours_informatique/cours/web/serveur-web/)

Ce cours m'a permis d'apprendre comment fonctionnent les promesses grâce à la fonction *.then(reponse => {})*. Ce qui permet à d'attendre que la fonction se termine avant de passer à la suivante.

Cela est particulièrement utile lorsque l'on utilise la fonction *fetch* de javascript qui permet de récupérer les données sous la forme d'un objet de type Response pour les utiliser en front. Il est important que les données soient de type json.
Il est également possible de récupérer un fichier texte ou une image.

Par défaut, il n'est possible de fetch des données qu'avec un script issu du site contenant les données. Cependant, il est possible d'ajouter un fichier donnant accès à tout le monde au dossier dans lequel il est contenu.

La [suite](https://francoisbrucker.github.io/cours_informatique/cours/web/serveur-web/minimal/) du cours permet d'apprendre à créer un serveur web minimal avec node et explique le fontcionnement du protocole http(requête, réponse et status)

La [partie suivante](https://francoisbrucker.github.io/cours_informatique/cours/web/serveur-web/routes/) porte sur la gestion des routes notamment afin de permettre à notre serveur de lire des fichiers html ou l'image flavicon.

On apprend [ensuite](https://francoisbrucker.github.io/cours_informatique/cours/web/serveur-web/express/) à utiliser le module *express* pour faciliter la gestion de notre site. En effet, le module *express* permet de créer nos routes très simplement.

La [dernière partie](https://francoisbrucker.github.io/cours_informatique/cours/web/serveur-web/routes-param%C3%A8tres/) explique comment gérer des routes avec paramètres afin de ne pas avoir à créer toutes les routes une par une à la main ce qui n'est pas faisable. Pour cela, il est possible d'encoder les paramètres dans l'url ou bien dans une query.

## Gestion de données Serveur

J'ai ensuite suivi la partie gestion de données côté serveur qui se découpe aussi en 2 parties :
- [La gestion de données côté serveur](https://francoisbrucker.github.io/cours_informatique/cours/web/gestion-donn%C3%A9es-serveur/)
- [Utilisation de bases de données](https://francoisbrucker.github.io/cours_informatique/cours/web/bases-de-donn%C3%A9es/)

La 1ère partie explique ce qu'est une API, la méthode CRUD et recommande l'utilisation de JSON pour sérialiser ses données.

La 2ème partie introduit la base de données relationnelle SQLite ainsi que sequelize pour la gestion. Elle explique comment mettre en oeuvre la méthode CRUD avec sequelize. Ainsi, que la configuration, l'initialisation et l'utilisation de la base de données.

