---
layout: layout/pok.njk

title: "POK 2 : Site Web en React pour gérer mes tâches"
authors:
  - Kévin BERNARD

date: 2024-10-16

tags:
  - "temps 2"
  - "React"
  - "3D"
  - "Gestion de tâches"

résumé: Un POK où je crée un site web attirant en React pour gérer mes tâches avec des animations 3D.
---

{% prerequis %}
Pas de prérequis pour le moment
{% endprerequis %}

{% lien %}
<b>SOURCES</b>
- [Awwwards](https://www.awwwards.com/)
- [House of Dreamers de Andrea Giuffrida sur Awwwards](https://www.awwwards.com/sites/house-of-dreamers)
- [Image postée par Maria Rojas sur Pinterest](https://fr.pinterest.com/pin/16255248649915602/)
- [Images de HorizonPeaksDesigns sur www.etsy.com ](https://www.etsy.com/fr/listing/1816504003/24-images-clipart-haute-resolution-de)
- [Tableau peinture paysage nature PARADIS D'AUTOMNE, sur le-petit-fermier.com](https://le-petit-fermier.com/products/tableau-peinture-paysage-nature?variant=50060240290118)
- [Image générée par IA sur fr.freepik.com par pjdesign](https://fr.pinterest.com/pin/391672498864069106/)
- [How to Implement a Blender Model in a React.js Application using Three.js de Matthes.B sur FreeCodeCamp](https://www.freecodecamp.org/news/blender-three-js-react-js/)
- [GitHub du site](https://github.com/KevinBERNARD1901/creature_site)
{% endlien %}

{% chemin %}
<b> POK & MON </b>
- [MON 2.1 : Introduction à React.js, Omar SALAME](../../../../2023-2024/Omar-Salame/mon/temps-2.1/index.md)
- [MON 3.1 : Débuter avec React.js, Thomas DUROY](../../../../2022-2023/Duroy-Thomas/mon/MON_3.1/index.md)
- [MON 2.1 : Animation 3D en React, Kévin BERNARD](../../mon/temps-2.1/index.md)
{% endchemin %}

<!-- **Liste d'idées:**
- Faire un jeu en mode, réalisation de tâche = évolution de "Pokémon"
- Faire un excel pour gérer mes comptes
- Faire un excel pour gérer mes projets
- Faire un site en react (pourquoi pas le site de notre projet)
- Site avec toutes mes données d'écriture ou avec les stats de ce que j'écris

J'ai décidé de faire les tous en me créant une application qui me permettra de gérer mon activité d'illustrateur.

- J'aurai une page horodateur ou j'inscrirai mes tâches issues de ma TO DO de projets et rendez-vous...
- Ensuite j'aurai mon retroplanning de mes projets et un agenda regroupant mes tâches et tout ce que je veux mettre dedans (anniversaire, rendez-vous...)
- J'aurai une page qui sera dédiée à mon activité d'illustrateur avec mes clients, mes finances.
- La dernière page sera pour la gestion de mes créatures sachant que je mettrai des animations de ces créatures dans les autres pages suivant des actions (scroll de la page, tâche rempli...)
- Faire une carte regroupement la ou se trouve mes clients, voir le POK de Clarisse. Genre une map avec des points plus grands en fonction du nombre de clients qu'il y a dans la zone géographique.

Pour cela j'ai demandé à chatGPT ce qu'il me recommendait :
- Frontend : React.js avec des bibliothèques comme React-Three-Fiber (pour la 3D), FullCalendar (pour l’agenda), Chart.js ou Recharts (pour les finances).
- Backend : Node.js + Express avec une base de données comme MongoDB ou PostgreSQL.
- 3D et Animations : Modélisation et animation des créatures en Blender (export GLTF), puis intégration dans l’application avec Three.js (ou React-Three-Fiber pour les composants React). Utilisation de GSAP pour des animations fluides.
- Gestion des états : Redux pour un état global des tâches, projets, et créatures.
- Mobile et PWA : React Native pour une version mobile native ou PWA pour une app responsive.

J'avais envie de reprendre React donc vraiment bien et Blender aussi. -->

Le but de ce POK est de réaliser un site en React pour gérer mes tâches avec un horodateur, un agenda avec une importation de créatures 3D à partir de Blender. Ce qui peut se résumer à :

<center><b>Comment me créer un site de gestion de tâches attirant en React avec une expérience 3D ?</b></center>

## Tâches

### Sprints

#### Sprint 1

- [x] Création v0 de la maquette de l'application 
- [ ] Création des pages

#### Sprint 2

### Horodatage

| Date | Heures passées | Indications |
| -------- | -------- |-------- |
| **Début Sprint 1** |
| Mardi 05/11  | 2H45  | Création de la mind map et de la maquette |
| Dimanche 10/11 | 1H | Maquette : page Agenda |
| Jeudi 14/11 | 1H35 | Maquette: inspiration de House of Dreamers |
| Vendredi 15/11 | 1H | Importation du modèle blender sur la page web |
| Vendredi 15/11 | 0H45 | Ajustement de la lumière |
| Lundi 18/11 | 0H45 | Ajustement Caméra, position, taille |
| Mardi 19/11 | 2H15 | Création des pages et ajout de la navigation |
| Total | 9H45 |

<!-- | **Début Sprint 2** |
| Total | 0H | -->

## Contenu

### Premier Sprint

#### Mind map/Maquette

##### 1ère idée

Sachant que je n'avais aucune référence de laquelle m'inspirer, j'ai décidé de faire une MindMap de toutes mes idées sur Miro pour les organiser.
J'ai classé mes idées en 3 catégories :
- Animations : liste des interactions possibles entre les créatures et mes actions (hover, finir une tâche...)
- Créatures : description des créatures et de comment gamifier la réalisation de tâches. (gagner des pierres pour invoquer de nouvelles créatures par exemple)
- Site : liste des pages et de leurs fonctionnalités/particularités

En parallèle, j'ai avancé le design de ma maquette sur Figma. J'ai fait une barre de navigation et regarder d'autres sites de productivité comme Asana ou Monday.
Initialement, je suis parti sur un site classique avec les créatures qui seraient rajoutées avec des animations comme un tour du tableau de tâche quand je scroll vers le bas.
Il y avait 4 pages :
- Horodateur : horodateur classique
- To do : liste des tâches par thème, projet
- Agenda : calendrier avec les tâches
- Créatures : gestion des créatures

Cela ne m'allait pas, je ne trouvais pas la chose attirante donc j'ai recherché des inspirations de sites en 3D sur Instagram et des sites internets dont le site [Awwwards](https://www.awwwards.com/) où j'ai trouvé le modèle [House of Dreamers](https://www.awwwards.com/sites/house-of-dreamers) de Andrea Giuffrida qui m'a beaucoup plu.

<video controls src="media/houseofdreamers.mp4" title="Title"></video>

---

##### 2e idée

Le modèle House of Dreamers de Andrea Giuffrida m'a donné l'idée de faire un fond 3D avec les créatures dedans.
1. En premier lieu, je me suis dit que j'allais intégrer les informations de mon site à mon décor. Par exemple, il y a un lac avec une cascade et le texte s'affiche sur l'eau. 
Après réflexion, j'ai trouvé cela trop compliqué à rendre intéressant et à faire.
2. J'ai opté pour mettre le texte et mes graphiques par dessus mon décor. Pour le choix de mes décors :
   - **Option 1** : Plusieurs paysages différents -> **avantage** : très créatif; **problèmes** : beaucoup de travail de blender + cohérence entre les pages et le style
   - **Option 2** :  Même paysage avec un changement de saison d'une page à l'autre -> **avantages** : 4 fois moins de travail + cohérence avec les créatures qui sont organisées selon 4 éléments + cohérence des pages; **problème** : je n'aime pas, je trouve cela plat.
   - **Option 3** : Changement d'élément à chaque page, avec un décor correspondant -> **avantage** : cohérence avec les éléments des créatures; **problème** : manque de cohérence visuel entre les pages

J'ai passé beaucoup de temps sur l'apparence possible de mon site, je ne savais pas quoi décidé entre les 3 options.
Sachant que je n'aurai pas le visuel tout de suite puisqu'il faut créer les décors sur Blender, je me suis arrêté là sur la partie design pour me concentrer sur la création du site en React.
Pour l'instant, ma maquette ressemble à cela (option 2):
![alt text](media/Figma.png)

{% lien %}
<b>Sources</b>
- [Image postée par Maria Rojas sur Pinterest](https://fr.pinterest.com/pin/16255248649915602/)
- [Images de HorizonPeaksDesigns sur www.etsy.com ](https://www.etsy.com/fr/listing/1816504003/24-images-clipart-haute-resolution-de)
- [Tableau peinture paysage nature PARADIS D'AUTOMNE, sur le-petit-fermier.com](https://le-petit-fermier.com/products/tableau-peinture-paysage-nature?variant=50060240290118)
- [Image générée par IA sur fr.freepik.com par pjdesign](https://fr.pinterest.com/pin/391672498864069106/)
{% endlien %}

---

#### Importation module 3D

Ayant clarifier grossièrement à quoi ressemblera mon site, je suis passé à l'implémentation de  mon idée sur React.

Je me suis renseigné sur React et j'ai créé mon projet grâce aux MONs de Thomas DUROY et Omar SALAME.

{% chemin %}
- [MON 2.1 : Introduction à React.js, Omar SALAME](../../../../2023-2024/Omar-Salame/mon/temps-2.1/index.md)
- [MON 3.1 : Débuter avec React.js, Thomas DUROY](../../../../2022-2023/Duroy-Thomas/mon/MON_3.1/index.md)
{% endchemin %}

Ensuite, j'ai téléchargé un [modèle gratuit](https://fr.3dexport.com/3dmodel-aerial-grassy-and-rocky-mountain-5-466915.htm) de Mixalisg depuis 3DEXPORT sous format glb.
J'ai fait les recherches pour mon MON et téléchargé les bibliothèques React Three Fiber et React Three Drei.

{% chemin %}
- [MON 2.1 : Animation 3D en React, Kévin BERNARD](../../mon/temps-2.1/index.md)
{% endchemin %}

Dans un second temps, j'ai suivi un tutoriel de Matthes.B sur FreeCodeCamp pour importer un document depuis Blender jusqu'à ma page web. Et j'ai jouer avec les paramètres avoir quelque chose de satisfaisant.

{% lien %}
[How to Implement a Blender Model in a React.js Application using Three.js de Matthes.B sur FreeCodeCamp](https://www.freecodecamp.org/news/blender-three-js-react-js/)
{% endlien %}

Avec le temps qu'il me restait, j'ai rajouté les liens avec React-rooter-dom.

Pour le moment cela ressemble à cela :

![alt text](media/site_apres_sprint1.png)

### Second Sprint