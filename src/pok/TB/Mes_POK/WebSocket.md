---
layout: layout/post.njk

title: "Site collaboratif grâce à WebSocket"
authors:
  - Timothée Bermond

---
<!-- Début Résumé -->
Amélioration de mon site pour compter les points au Yams du temps du 2.
Avec notamment l'utilisation de WebSocket afin de rendre collaborative les pages de score.
<!-- Fin Résumé -->

## Sprint 1

Pour le 1er sprint je prévois de :
- Me former sur WebSocket grâce au [MON 3.1](https://francoisbrucker.github.io/do-it/mon/TB/Mes_MON/WebSockets/).
- Faire une 1ère version du site où tout le monde a accès à la même feuille de score.

Durant ce sprint, j'ai eu le temps de me former sur les WebSocket. 

J'ai également pu développer la partie collaborative de mon site. Pour ce faire, à chaque changement sur ma page je récupère l'id ainsi que la valeur de l'élément qui a changé puis j'envoie tout ça au serveur. Côté serveur je créé un array contenant les points de tous les joueurs et le modifie à chaque changement. Puis je recalcule la somme des points de chaque joueur. Enfin je renvoie les points actualisé à toutes les clients connectés et modifie l'affichage afin qu'il soit cohérent avec les points de chaque joueur.

Les principaux problèmes que j'ai rencontré durant ce sprint étaient principalement des petites erreurs de précision ou de cas particuliers. 

Le site est dispo [ici](http://node.poireau.ovh1.ec-m.fr/static/index.html).

Et le code [ici](https://github.com/Timothee-Bermond/yams).

Pour le prochain sprint je vais essayer de créer des parties séparés afin que deux groupes qui se connectent en même temps puissent chacun avoir leurs parties. Je ne sais pas encore exactement comment je vais faire.

## Sprint 2
Pour le 2nd sprint je prévois de :
- Finir mon site en ajoutant la possibilité de créer ou rejoindre des parties afin de pouvoir plusieurs parties différentes.
- Si j'ai encore du temps mettre en place la possibilité de directement jouer sur le site.