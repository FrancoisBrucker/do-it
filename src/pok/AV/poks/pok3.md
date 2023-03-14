---
layout: layout/post.njk

title: "POK 3"
authors:
  - Antoine Varnerot

---
<head>
  <link rel="stylesheet" href="../../assets/style.css">
</head>

## Plan du POK

## Sprint 1

- ~~sign in (back)~~
- ~~sign up (back)~~
- ~~sign out (back)~~
- <span style="color:orange">login (front)</span>
- <span style="color:orange">noter les musiques</span>
- ~~déployer en ligne~~

## Sprint 2

- tests unitaires
- utilisation de docker
- CI (avec gitlab peut-être ou directement avec les "actions" de GitHub)

## Points difficiles/techniques

1. Mise en ligne de l'API

L'API et le front-ent étant décomposés en deux dossier différents, on commence d'abord par mettre en ligne l'API sur l'OVH.
Tout d'abord dans notre API, on replace le port dé déploiement par défaut par un port géré par l'OVH. Dans notre fichier ```server.js``` on remplace le port 3000 par le 8080 comme suit:

```js
const port = normalizePort(process.env.PORT || '8080');
```

On voudra lancer la commande ```nodemon serve``` sur notre OVH une fois les fichiers déployés, mais l'OVH ne reconnait pas la commande nodemon directement, cependant il reconnait les commandes npm.
Pour pouvoir lancer la commande nodemon, il faut donc la renseigner dans notre fichier ```package.json```:

```json
scripts": {
  "start": "nodemon serve",
```

Il nous suffit maintenant de copier les fichiers de notre dossier API dans le dossier /node de l'OVH puis, directement depuis la console, lancer notre commande

```shell
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

3. Authentification

Pour le système d'authentification, on avait sous-estimé le temps que ca prendrait. En effet, on a utilisé les JWT tokens et même si on a trouvé un tutoriel sur le site <https://www.bezkoder.com/>, il y avait eu quelques changements depuis que ce tutoriel a été fait et notre application express était en "type: module" (paramètre dans le package.json) et ca gênait beaucoup. On a préféré terminé cela parce que c'était un gros point technique du projet et qui allait nous servir pour d'autres projets.
