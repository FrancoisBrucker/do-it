---
layout: layout/mon.njk

title: "WebSocket"
authors:
  - Timothée Bermond

date: 2023-03-23

tags:
  - 'temps 3'
  - 'websocket'
  - 'socket.io'
  - 'temps reel'
  - 'handshake'
---

<!-- début résumé -->
Découverte du protocole WebSockets.
Le protocole permet d'échanger des données en temps réel entre le client et le serveur.
Il faut un niveau intermédiaire (savoir développer un site web) pour suivre ce MON.
<!-- fin résumé -->

## Intro

J'ai souhaité faire ce MON sur le protocole WebSocket afin de pouvoir l'implémenter sur mon [POK](../../../../pok/TB/Mes_POK/WebSocket).

Grâce à ce MON j'ai pu bien comprendre le concept derrière le protocole WebSocket. Il s'agit de créer une connexion entre le client et le serveur avec un système de handshake (le client envoie une demande de connexion et le serveur lui répond avec un message d'acceptation). Une fois la connexion établie, les deux parties peuvent s'envoyer des messages.

Il existe plusieurs API permettant d'implémenter le protocole WebSocket. Durant ce MON j'ai pu en découvrir 2 :
- [websocket](https://www.npmjs.com/package/websocket)
- [socket.io](https://socket.io/)

## API websocket

Pour ce MON j'ai suivi tout d'abord suivi la [formation LogRocket sur les WebSockets](https://blog.logrocket.com/websocket-tutorial-real-time-node-react/). 

Le tuto est composé d'une vidéo tuto qui nous explique comment créer un système de chat en temps réel et d'un tuto écrit qui reprend un code et qui l'explique partie par partie. J'ai trouvé que la vidéo était beaucoup plus simple à comprendre que le tuto écrit. Je conseille de d'abord suivre la vidéo puis de lire le tuto afin d'être sûr d'avoir tout compris.

C'est le tuto le plus complet sur lequel je suis tombé.

Le petit bémol de cette formation c'est qu'elle utilise react que je ne maitrise pas encore.


J'ai également suivi une autre [vidéo tuto](https://www.youtube.com/watch?v=wV-fDdHhGqs&ab_channel=Vuka). Elle apprend également comment faire un mini système de chat en temps réel.

Elle était très intéressante car elle utilisait node et express en plus de l'API websocket comme ce que j'utilise sur mon POK. Elle est plus simple que la 1ère mais du coup est très utile en complément.

## API socket&#46;io

J'ai suivi 3 vidéos tutos pour l'API socket.io que j'ai d'ailleurs choisi pour mon POK car je l'ai trouvée plus simple à implémenter.

Je conseille de commencer par cette [vidéo](https://www.youtube.com/watch?v=7uwRTSYq5lY&t=1105s&ab_channel=Pentiminax) qui encore, une fois, créé un chat en temps réel. Elle permet de rapidement comprendre les bases et les principales fonctionnalités de socket&#46;io. De plus, elle est en français ce qui la rend très facile à comprendre.

Elle se couple bien avec cette deuxième [vidéo](https://www.youtube.com/watch?v=9Jup6YUshak&ab_channel=ThomasMouchelet) qui, elle, créé une application de vote en temps réel. Cette vidéo est également en français et montre une autre manière d'utiliser l'API socket&#46;io.

Enfin la dernière vidéo est plus complexe, elle montre comment créer un chat en temps réel avec plusieurs rooms en utilisant le concept de session sur express. Je conseil de la suivre en dernier une fois que l'on est bien habitué à socket&#46;io. 