---
layout: layout/pok.njk

title: "POK1 - Complesims, l'interface web pour gérer des objectifs"
authors:
  - Inès Kebbab

date: 2024-09-05

tags:
  - "temps 1"
  - "info"

résumé: Ce premier POK vise à créer un petit site web pour suivre l'avancée dans une liste d'objectifs dans un jeu vidéo (Les Sims 4).
---

L'objectif de ce POK est de revoir les notions de base de développement web en réalisant un POK. 

*à compléter avec le niveau des pré-requis et les liens des autres POK/MON en lien.*
POK en liens :
* [Web Front 1 HTML/CSS/JS](https://francoisbrucker.github.io/do-it/promos/2022-2023/Gissler-Nathan/mon/mon-1-1/)
* [Un peu de JavaScript](https://francoisbrucker.github.io/do-it/promos/2023-2024/William%20Lalanne/mon/temps-1.2/)

Inspirations rédaction POK :
[Lucas Rioual : récap par sprint](https://francoisbrucker.github.io/do-it/promos/2023-2024/Rioual-Lucas/pok/temps-1/)
[Khaoula : apprentissages et erreurs](https://francoisbrucker.github.io/do-it/promos/2023-2024/Khaoula-Belaaziz/pok/temps-1/)


## Objectifs

Ayant déjà de bases du dev web (front end, back end...), les objectifs principaux de ce projet est :
  1. **Se raffraichir la mémoire sur les notions utiles**, notamment en vu de suivre (peut-être) le CS "Dev Web : Zero to hero" au temps 2.
  2. **Se perfectionner** en front, sur HTML/CSS/JS et approfondir la compréhension du back (notamment avec des requêtes et la gestion d'une base de données simple).
  3. **Finir mon premier projet concret en solo de A à Z (ou presque)**, sur un site complètement solo, du début à la fin.

## Tâches

#### Sprint 1 - Rodage et premiers tests
1. [ ] Maquette express (avec des wireframes ?) de l'interface et choix de premières catégories à implémenter pour le sprint.
2. [ ] Remise à niveau / rappels HTML et CSS.
3. [ ] Remise à niveau / rappels en JS et analyse du code de site de James Turner pour comprendre la structure.
4. [ ] Implémentation du premier bloc de checklist "simple", en front end VS en back puis front end.

#### Sprint 2 - Ajout des autres blocs et informations
1. [ ] Implémentation de blocs à checklist à niveau d'avancement (1,2,3... Fait).
2. [ ] Gestion des filtres d'affichages (DLCs et non terminé/terminé).
3. [ ] Affichage des pourcentages d'avancement par catégorie.
4. [ ] Affichage d'informations au survol des informations sur l'item.
5. [ ] Sauvegarde et/ou mise en cache.
6. [ ] Etudier l'évolution vers une base de donnée (+ rappels back).
7. [ ] *(Bonus : Animation / pop up si la checklist est complétée.)*


### Horodatage

Toutes les séances et le nombre d'heure que l'on y a passé.

| Date | Heures passées | Indications |
| -------- | -------- |-------- |
| Dimanche 15/09  | 10h  | Rappels HTML/CSS, réalisation du front en parallèle, recherches JS et premiers tests (infructueux) |

## Contenu

### L'idée du projet
Ce projet est inspiré par ma propre expérience de jeu sur les Sims 4 où je me mets au défi de "finir le jeu à 100%", au travers d'une partie et donc obtenir toutes les réussites du jeu, compléter toutes les collections, atteindre le niveau maximal de toutes les compétences, etc. 

La liste de choses à découvrir est longue et pour suivre mon avancement, j'utilise le  [site du joueur James Turner](https://jamesturner.yt/supersim/tracker) qui répond partiellement au besoin (et m'ayant ainsi inspiré ce POK), un Google Doc avec des checklists, ainsi qu'une liste papier selon les items.

L'objectif serait donc d'avoir une interface web pour suivre au même endroit les items réalisés rangés par catégorie, à l'instar du site d'inspiration, avec quelques filtres supplémentaires (éléments manquants,...) et l'enregistrement de la progression sans connexion.

Une fonctionnalité supplémentaire *(pour explorer plus de fonctionnalités)* serait d'afficher des informations d'aide pour réaliser l'item de la checklist.


### Premier Sprint

### Second Sprint

### Conclusion et évolutions possibles
#### Ce que j'ai appris :
XXX

#### Les erreurs à éviter :
* Le CSS peut être très chronophage, surtout si on cherche à debug un bug graphique !
* Ne pas (toujours) foncer directement dans le code sans réfléchir...

#### Quid d'une base de données ?
J'avais hésité dès le départ à créer une base de données dans laquelle il serait facile d'ajouter un élément via l'interface plus tard. Pour me forcer à explorer au maximum Javascript, j'ai décidé de faire sans. Néanmoins, au vu du code sur le site d'inspiration, la rédaction est lourde et si l'on souhaite à terme avoir les mêmes données sur différentes pages, la donnée sera plutôt redondante.

Finalement, je reverrais le back sur mon temps libre. La base de données pourra comprendre la "catégorie" d'items, le nom, son statut (réalisé ou non) et éventuellement d'autres informations complémentaires / utiles (*pex : des infos sur comment compléter tel item*).