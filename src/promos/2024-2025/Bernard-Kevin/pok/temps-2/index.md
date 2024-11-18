---
layout: layout/pok.njk

title: "POK 2 : Site Web avec mon Portfolio"
authors:
  - Kévin BERNARD

date: 2024-10-16

tags:
  - "temps 2"

résumé: Un POK où je crée un site web pour mon portfolio.
---

{% prerequis %}

Pas de prérequis pour le moment

{% endprerequis %}

{% lien %}

<b>SOURCES</b>

- Rien pour le moment

{% endlien %}

{% chemin %}
<b> POK & MON </b>
- [MON 2.1 : Introduction à React.js, Omar SALAME](../../../../2023-2024/Omar-Salame/mon/temps-2.1/index.md)
- [MON 3.1 : Débuter avec React.js, Thomas DUROY](../../../../2022-2023/Duroy-Thomas/mon/MON_3.1/index.md)
{% endchemin %}

**Liste d'idées:**
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

J'avais envie de reprendre React donc vraiment bien et Blender aussi.

## Tâches

### Sprints

#### Sprint 1

- [ ] Création v0 de la maquette de l'application 
<!-- (<b>estimé : </b>, <b>réel : </b>) -->
- [ ] Création des pages

#### Sprint 2

### Horodatage

<!-- | Date | Heures passées | Indications |
| -------- | -------- |-------- |
| **Début Sprint 1** |
| Mardi 05/11  | 2H45  | Création de la mind map et de la maquette (barre de navigation + couleurs) |
| Dimanche 10/11 | 1H | Maquette : page Agenda |
| Jeudi 14/11 | 1H35 | Maquette: inspiration de House of Dreamers + table de ClipArtMag et livre de Pixabay sur Pinterest + idéation des thèmes des pages sur la mind map + Idée des 4 saisons avec le texte qui est par-dessus les paysages, à la fois beaucoup plus simple et plus joli |
| Vendredi 15/11 | 1H | Importation du modèle blender sur la page web |
| Vendredi 15/11 | 0H45 | Ajustement de la lumière |
| Total | 7H05 | -->
<!-- | **Début Sprint 2** |
| Total | 0H | -->



## Contenu

Mettre les liens avec le nom de la source parce que le lien peut devenir obsolète.

### Premier Sprint

- [Fichier blender](https://fr.3dexport.com/3dmodel-aerial-grassy-and-rocky-mountain-5-466915.htm) de Mixalisg sur 3DEXPORT
- [Background summer](https://fr.pinterest.com/pin/16255248649915602/) sur Pinterest
- [Background spring](https://www.etsy.com/fr/listing/1816504003/24-images-clipart-haute-resolution-de) ou bien (https://fr.pinterest.com/pin/969188782452898341/)
- [Background ](https://le-petit-fermier.com/products/tableau-peinture-paysage-nature?variant=50060240290118) Tableau, le petit fermier PARADIS 
- [Background winter](https://fr.freepik.com/images-ia-premium/paysage-hiver-noel_66796941.htm) ou bien (https://fr.pinterest.com/pin/391672498864069106/)


### Second Sprint