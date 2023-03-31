---
layout: layout/post.njk

title: "WebSockets"
authors:
  - Timothée Bermond

tags :
---

<!-- début résumé -->
Découverte du protocole WebSockets.
Le protocole permet d'échanger des données en temps réel entre le client et le serveur.
Il faut un niveau intermédiaire (savoir développer un site web) pour suivre ce MON.
<!-- fin résumé -->

Pour ce MON j'ai suivi tout d'abord suivi la [formation LogRocket sur les WebSockets](https://blog.logrocket.com/websocket-tutorial-real-time-node-react/).

Grâce à ce tutoriel j'ai pu bien comprendre le concept derrière le protocole WebSocket. Il s'agit de créer une connexion entre le client et le serveur avec un système de handshake (le client envoie une demande de connexion et le serveur lui répond avec un message d'acceptation). Une fois la connexion établie, les deux parties peuvent s'envoyer des messages.

Il existe différentes API pour gérer WebSockets. Ce tutoriel utilise l'API [websocket](https://www.npmjs.com/package/websocket).

Après avoir installé l'API avec la commande : 
```
npm install --save websocket http
```

- [une vidéo utilisant l'API WebSocket](https://www.youtube.com/watch?v=wV-fDdHhGqs&ab_channel=Vuka)
- [un petit tuto utilisant Typescript](https://medium.com/factory-mind/websocket-node-js-express-step-by-step-using-typescript-725114ad5fe4)