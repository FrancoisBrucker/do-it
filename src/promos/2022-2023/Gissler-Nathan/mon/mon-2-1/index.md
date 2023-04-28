---
layout: layout/mon.njk

title: "Web Back"
authors:
    - Nathan Gissler

date: 2023-01-04

tags:
  - 'temps 2'
  - 'web'
  - 'back'
  - 'express'
---

<!-- début résumé -->

Pour ce MON, je vais apprendre à utiliser les outils de back qui me permettront de déployer mon site sur un seveur lors de mon POK, et ce notamment grâce au cours de François Brucker.

<!-- fin résumé -->

## Déploiement d'un dossier sur OVH

On peut déployer d'un coup tous les fichiers de notre site sur le serveur OVH avec les commandes suivantes :

Archivage et compression du dossier contenant tous les fichiers du site

    tar -Jcvf archive_dossier.tar.xz dossier/

Copie de l'archive compressée sur le serveur avec le protocole SSH

    scp chemin/archive_dossier.tar.xz mon_herbe@ovh1.ec-m.fr:www/archive_dossier.tar.xz

Décompression et désarchivage

    tar -Jxvf archive_dossier.tar.xz

On peut désormais accéder aux fichiers du site de cette manière : `http://mon_herbe.ovh1.ec-m.fr/dossier_du_site/chemin`.

## Utilisation de Node.js et Express pour son site

![Logo Express](express.png)

Création du fichier de configuration package.json

    npm init

Ajout du module Express

    npm add --save express

Il faut également créer un fichier `index.js` qui va nous aider à gérer simplement les routes de notre site avec Express, c'est-à-dire les différents URL auxquels on peut accéder sur le serveur.

Pour lancer le site, on exécute `node index.js` sur le serveur.

Un bon usage est de séparer la partie front de la partie back. Pour cela, on créer un dossier `static` qui contiendra tous les fichiers front de notre site.

### Utilisation du fichier `index.js`

Exemple du fichier `index.js` que j'utilise pour mon site, dans le cadre de mon POK :

    const path = require('path')

    const express = require('express')
    const app = express()

    const hostname = '127.0.0.1';
    const port = 3000;

    app.use("/static", express.static(path.join(__dirname, '/static')))

    app.get('/', (req, res) => {
        res.redirect(301, '/static/index.html')
    })


    app.use(function (req, res) {
        console.log("404 : " + req.url);

        res.statusCode = 404;
        res.setHeader('Content-Type', 'text/html');

        res.end("<html><head><title>404</title></head><body>404</body></html>");

    })

    app.listen(port, hostname);
    console.log(`Server running at http://${hostname}:${port}/`);

Ici, j'utilise le port 3000 du serveur local (qui correspond à l'adresse IP 127.0.0.1).

A chaque fois que l'on va envoyer une requête au serveur, chaque appel de `app` va être testé (sachant que `use` fonctionne avec toutes les requêtes, `get` avec les requêtes de type `get` et `post` avec les requêtes de type `post`), et dès que la condition du premier paramètre d'un des appels est satisfait on exécute le deuxième paramètre de cet appel.

Par défaut, les appels suivants de `app` ne sont pas exécutés. On peut tout de même faire en sorte d'exécuter l'appel suivant grâce à la fonction `next()`, utilisée en fin d'appel.

Dans mon exemple, on commence par filtrer toutes les requêtes dont l'url (après l'url du site lui-même) est `static/` qui sont renvoient vers les pages du site correspondantes (dans le dossier `static` du site).

On gère ensuite le cas où notre requête contient simplement l'url du site afin de rediriger vers le fichier `static/index.html` qui est la première page du site.

Enfin, toutes les requêtes qui n'ont pas encore été gérées à ce stade tombent sur le dernier appel qui renvoie dans tous les cas vers une page d'erreur 404 (assez rudimentaire ici).

#### Utilisation de l'objet `Router` d'Express

Lorsque l'on travaille sur un site d'une taille plus conséquente, il peut être pratique d'utiliser les `Router`, qui permettent des groupes de routes.

Par exemple, on peut créer un `Router` pour un ensemble de requêtes dans un fichier, puis l'appeler en deux lignes dans notre `index.js` :

    const router = require('chemin_vers_le_router');

    app.use('/requetes_concernees', router);

## Gestion de la modification en temps réel d'un document collaboratif

![Logo Meteor](meteor.png)

Pour la réalisation de notre POK, il faudrait que nous puissions, dans l'idéal, faire en sorte que les partitions du site "Mon sheet c'est moi" soient collaboratives et que les modifications d'un utilisateur soient visibles en temps réel par les autres utilisateurs. Cela fonctionnerait à la manière d'un Google Docs mais pour des partitions musicales.

Cela est possible avec des frameworks comme Firebase ou Meteor. Le principe est que chaque utilisateur soit authentifié et que les modifications qu'il apporte à un document soient enregistrées dans sa session sur le serveur. Dès qu'une modification est apportée par un utilisateur, une notification est envoyée aux autres utilisateurs puis leur version du document est actualisée en temps réel.

Nous pensons utiliser Meteor pour cela, il faudra se documenter plus en détail lors de la réalisation du POK.

## Liens

- [SSH et Serveur OVH](https://francoisbrucker.github.io/cours_informatique/cours/ops/ssh/)
- [Cours Serveur Web](https://francoisbrucker.github.io/cours_informatique/cours/web/serveur-web/)
- [Documentation de Meteor](https://docs.meteor.com)