---
layout: layout/pok.njk

title: "POK 3"
authors:
  - Antoine Varnerot

date: 2023-01-25

tags:
  - 'temps 3'
  - docker
  - login
  - angular
  - express
  - test
  - javascript
---
<head>
  <link rel="stylesheet" href="../assets/style.css">
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

- ~~tests unitaires~~
- ~~utilisation de docker~~
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

5. Utilisation de Docker (docker-compose)

Il est dans notre cas possible d'utiliser l'outil Docker Compose pour créer une application multi-conteneurs avec le front et l'API.

Tout d'abord il nous faut définir le Dockerfile pour l'API.
Dans notre dossier ```/front``` on crée un fichier ```Dockerfile``` puis on copie le code suivant:

```dockerfile
FROM node:14-alpine as development
WORKDIR /usr/src/app/front

COPY package*.json ./

RUN npm install -g @angular/cli @angular-devkit/build-angular && npm install

EXPOSE 4201

CMD ["npm", "start"]
```

Dans notre fichier ```package.json``` on cherche la ligne associée à la commande "start" et on remplace par

```json
"ng serve --host=0.0.0.0 --port 4201",
```

Pareil dans le dossier API on crée un fichier ```Dockerfile``` qui contient le code:

```dockerfile
FROM node:14-alpine as development

WORKDIR /usr/src/app/api

COPY package*.json ./

RUN npm install

EXPOSE 3080

CMD ["npm", "run", "start"]
```

Dans notre fichier ```package.json``` on cherche la ligne associée à la commande "start" et on remplace par

```json
"start": "nodemon serve",
```

On supprime les dossiers ```node_modules``` et le fichier ```package-lock.json``` pour éviter les potentiels conflits et erreurs.

On crée notre fichier ```docker-compose.yml```

```yml
version: '3'
services:
  nodejs-server:
    build:
      context: ./API
      dockerfile: Dockerfile
    ports:
      - "3080:3080"
    container_name: node-api
    volumes:
      - ./API:/usr/src/app/api
      - /usr/src/app/api/node_modules
  angular-ui:
    build:
      context: ./front
      dockerfile: Dockerfile
    ports:
      - "4201:4201"
    container_name: angular-ui
    volumes:
      - ./front:/usr/src/app/front
      - /usr/src/app/app-ui/node_modules
```

Et il suffit dans le terminal les commandes suivantes pour lancer en local l'application

```bash
docker-compose build --no-cache
docker-compose up
```

Attention à bien changer les ports et les appels à l'API dans le code de l'application !
