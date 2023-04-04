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
- Me former sur WebSocket grâce au [MON 3.1](../../../../mon/TB/Mes_MON/WebSockets).
- Faire une 1ère version du site où tout le monde a accès à la même feuille de score.

Durant ce sprint, j'ai eu le temps de me former sur les WebSocket. 

J'ai également pu développer la partie collaborative de mon site. Pour ce faire, à chaque changement sur ma page je récupère l'id ainsi que la valeur de l'élément qui a changé puis j'envoie tout ça au serveur. Côté serveur je créé un array contenant les points de tous les joueurs et le modifie à chaque changement. Puis je recalcule la somme des points de chaque joueur. Enfin je renvoie les points actualisé à toutes les clients connectés et modifie l'affichage afin qu'il soit cohérent avec les points de chaque joueur.

Les principaux problèmes que j'ai rencontré durant ce sprint étaient principalement des petites erreurs de précision ou de cas particuliers. 

Le site est dispo [ici](http://node.poireau.ovh1.ec-m.fr/static/index.html).

Et le code [ici](https://github.com/Timothee-Bermond/yams).

Pour le prochain sprint je vais essayer de créer des parties séparés afin que deux groupes qui se connectent en même temps puissent chacun avoir leurs parties. Je ne sais pas encore exactement comment je vais faire.

## Objectifs sprint 2
Pour le 2nd sprint je prévois de :
- Finir mon site en ajoutant la possibilité de créer ou rejoindre des parties afin de pouvoir plusieurs parties différentes.
- Si j'ai encore du temps mettre en place la possibilité de directement jouer sur le site.

## Sprint 2

Durant ce sprint j'ai mis en place la possibilité de créer ou de rejoindre des parties. Pour cela j'ai ajouté deux pages :
- une page permettant de choisir si l'on veut créer ou rejoindre une partie
- une page permettant de rejoindre une partie déjà créée. 

Mettre en place la possibilité de créer ou de rejoindre des parties a été bien plus compliqué que ce que je pensais.
En effet, il faut que je stock les points de chaque parties différement et que j'actualise les scores pour les joueurs faisant partie de la partie.

Ma 1ère idée a été d'utiliser une base de données. À chaque création de nouvelle partie, je créé une nouvelle partie dans la bd et j'enregistre l'id de la partie dans les cookies. Sauf que je me suis retrouvé avec le même problème que dans le POK 2 avec des cookies qui s'enregistrent pas sans que je comprenne pourquoi.


Ma seconde idée a été de créer une liste contenant tous les points avec comme index l'indice de chaque de partie : à chaque création de nouvelle partie je push une liste de points vierge et l'id de la partie est la longueur de la liste des parties. Et d'enregistrer l'id dans les cookies puis d'y faire appel à chaque changement dans une partie.

C'est finalement cette idée que j'ai mise en place non sans mal.

En effet, lorsque je modifiais le score d'une partie cela modifiais le score pour toutes les parties. Il m'a fallu du temps pour comprendre d'où ça venait. Au début je pensais que c'était un problème avec les cookies mais non enfait. 

Le problème venait du fait que je pushais mon template de la liste de points dans la liste des parties sauf que quand je modifiais les points pour une partie ça modifiait directement le template et donc les points de toutes les parties et pas uniquement ceux de la partie modifiée.
J'ai réglé ce problème avec ces deux lignes : 

```javascript
let temp = JSON.stringify(points)
list_parties.push(JSON.parse(temp))
```

J'ai également eu un problème car je voulais récupérer l'id de la partie dans les cookies lors de l'échange websocket mais je n'ai pas trouvé comment faire. J'avais besoin d'un fetch afin de récupérer les cookies or webscoket n'utilise pas la méthode fetch et malgré de longues recherches je n'ai pas trouvé comment les récupérer. Mais j'ai assez facilement contourné ce problème en envoyant l'id avec la méthode *emit*. 

Enfin il fallait que j'envoie mes scores actualisés aux clients et qu'il y ait uniquement les clients jouant la partie modifiée qui prennent en compte ces points. J'ai résolu cela avec un simple *if* sur l'id de la partie.

Je pense que le site est encore améliorable. Notamment la manière de stocker les points qui n'est pas optimale surtout si beaucoup de parties sont créées. 

Finalement je n'ai pas eu le temps de mettre en place la possibilité de directement jouer sur le site.