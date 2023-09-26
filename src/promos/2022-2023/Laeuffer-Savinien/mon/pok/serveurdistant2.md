---
layout: layout/pok.njk

title: "Backend & Serveur distant (suite)"
authors:
  - Savinien Laeuffer

date: 2023-01-25

tags:
  - 'temps 3'
---

<!-- début résumé -->
Backend & déploiement sur un serveur distant (suite)
<!-- fin résumé -->

## Description du projet

Ce projet vise à remplacer mon groupe messenger avec mes amis sur lequel on envoie des musiques peu connues chaque jour, par une application web avec des fonctionnalités supplémentaires qui répertorie tous les envois plus facilement.

Ce temps 2 va donc être consacré à la création de cette application web de gestion de musiques en ligne. L'utilisateur peut ajouter des musiques à l'application à partir de liens YouTube ou Soundcloud, il en rentre les informations nécessaire à la bonne identification de la musique (Artiste, titre, lien, album, label, genre), celle-ci s'ajoute à sa collection et apparait dans le feed général que tout le monde peut consulter.
Chaque utilisateur peut ajouter une musique à ses favoris et voter pour une musique si il le juge nécessaire.

## Découpage en sprint

**Sprint 1**
- Tests unitaires
- Login
- Notation des musiques
- Déploiement sur l'OVH

**Sprint 2**
- Utilisation de Docker
- CI (avec Gitlab ?)

## Plan du POK

1. Mise en ligne de l'API

L'API et le front-ent étant décomposés en deux dossier différents, on commence d'abord par mettre en ligne l'API sur l'OVH.
Tout d'abord dans notre API, on replace le port dé déploiement par défaut par un port géré par l'OVH. Dans notre fichier ```server.js``` on remplace le port 3000 par le 8080 comme suit:
```js
const port = normalizePort(process.env.PORT || '8080');
```

On voudra lancer la commande ```nodemon serve``` sur notre OVH une fois les fichiers déployés, mais l'OVH ne reconnait pas la commande nodemon directement, cependant il reconnait les commandes npm.
Pour pouvoir lancer la commande nodemon, il faut donc la renseigner dans notre fichier ```package.json```:
```json
scripts": {
  "start": "nodemon serve",
```

Il nous suffit maintenant de copier les fichiers de notre dossier API dans le dossier /node de l'OVH puis, directement depuis la console, lancer notre commande 
```
npm run serve
```

L'API est désormais en ligne sur le port 8080.

2. Mise en ligne du front

Maintenant que notre API est en ligne sur l'OVH, il faut relier le front-end à l'API en changeant l'adresse des requêtes.
Dans ```/src/app/services/music.service.ts```, on va remplacer les URL par ceux de l'API en ligne comme suit:
```js
getMusics() {
        const route = `http://node.origan.ovh1.ec-m.fr:8080/api/musics`;
        return this.http.get<Music[]>(route);
    }

    addMusic(newMusic: Partial<Music>) {
        const route = `http://node.origan.ovh1.ec-m.fr:8080/api/newMusic`;
        return this.http.post<any>(route, newMusic);
    }
```

On build notre application localement avec la commande ```npm run build```. Cela va nous générer les fichiers nécessaire à déployer.
Un dossier ```/dist``` s'est alors créé avec un sous-dossier (chez nous: ```/projet3a```)

On supprime au prélable sur l'OVH tous les fichiers du dossier ```/www```, puis on colle tout le contenu de notre dossier dans ce dernier.

Notre site est désormais en ligne, et en se connectant on remarque que le front-end fonctionne correctement et communique bien avec l'API puisque les infos du feed de musique ont bien été collectées depuis MongoDB