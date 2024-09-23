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

Autres POK ou MON en lien :
* [Web Front 1 HTML/CSS/JS](https://francoisbrucker.github.io/do-it/promos/2022-2023/Gissler-Nathan/mon/mon-1-1/) (MON de Nathan Gissler)
* [Un peu de JavaScript](https://francoisbrucker.github.io/do-it/promos/2023-2024/William%20Lalanne/mon/temps-1.2/) (MON de William Lalanne)


## Objectifs

Ayant déjà de bases du dev web (front end, back end...), les objectifs principaux de ce projet est :
  1. **Se raffraichir la mémoire sur les notions utiles**, notamment en vu de suivre (peut-être) le CS "Dev Web : Zero to hero" au temps 2.
  2. **Se perfectionner** en front, sur HTML/CSS/JS et approfondir la compréhension du back (notamment avec des requêtes et la gestion d'une base de données simple).
  3. **Finir mon premier projet concret en solo de A à Z (ou presque)**, sur un site complètement solo, du début à la fin.

## Tâches

#### Sprint 1 - Rodage et premiers tests
1. [X] Maquette express (avec des wireframes ?) de l'interface et choix de premières catégories à implémenter pour le sprint.
2. [X] Remise à niveau / rappels HTML et CSS.
3. [/] Remise à niveau / rappels en JS et analyse du code de site de James Turner pour comprendre la structure.
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
| Dimanche 15/09  | 10h  | Rappels HTML/CSS, réalisation du front en parallèle, recherches JS et premiers tests (infructueux) - Sprint 1 |

## Contenu

### L'idée du projet
Ce projet est inspiré par ma propre expérience de jeu sur les Sims 4 où je me mets au défi de "finir le jeu à 100%", au travers d'une partie et donc obtenir toutes les réussites du jeu, compléter toutes les collections, atteindre le niveau maximal de toutes les compétences, etc. 

La liste de choses à découvrir est longue et pour suivre mon avancement, j'utilise le  [site du joueur James Turner](https://jamesturner.yt/supersim/tracker) qui répond partiellement au besoin (et m'ayant ainsi inspiré ce POK), un Google Doc avec des checklists, ainsi qu'une liste papier selon les items.

L'objectif serait donc d'avoir une interface web pour suivre au même endroit les items réalisés rangés par catégorie, à l'instar du site d'inspiration, avec quelques filtres supplémentaires (éléments manquants,...) et l'enregistrement de la progression sans connexion.

Une fonctionnalité supplémentaire *(pour explorer plus de fonctionnalités)* serait d'afficher des informations d'aide pour réaliser l'item de la checklist.


### Premier Sprint
#### Rappels HTML et CSS
Pour commencer, j'ai repris mes bases en HTML et CSS pour faire un site "agréable" en partant de zéro. Je me suis aidée des formations du GInfo et du cours HTML/CSS d'Open Classroom pour me rafraîchir la mémoire. 

Ayant créé un site Wordpress récemment, j'ai pu faire beaucoup de liens entre les options des components et les valeurs de style ce que j'ai trouvé assez amusant.

Les notions principales que je garde en mémoire :
* **Pour les marges :** la valeur padding sert aux marges internes alors que la valeur margin sert aux marges externes.
* **Pour "séparer" une div :** après avoir foncé dans le tas en cherchant la propriété "width:65%; align: left;" etc dans le but d'avoir deux colonnes, je me suis retrouvée bloquée un certain temps avec un bug de div qui n'avait pas les bonnes couleurs de fond ou les bons alignements... Tout simplement car ce n'était pas la bonne propriété ! La propriété CSS utile est *"display"*, avec les valeurs *"flex", "flex-direction"* etc. Avec l'affichage *"grid"*, j'ai même pu avoir la grille souhaitée pour la checklist.
* **Faire du CSS propre n'est pas une perte de temps :** j'ai d'abord été tenté d'inclure quelques styles dans les balises HTML... avant de me raisonner car de nombreuses balises avaient des propriétés similaires et il était beaucoup plus efficace de créer une classe (ou un id). Cela m'a aussi permis de me raisonner lorsque j'ai commencé le JS. 

Même si j'ai survolé le cours OpenClassrooms (et que l'ordre d'apprentissage ne correspondait pas à ce que je souhaitais réaliser), j'ai tout de même pu apprendre quelques notions supplémentaires notamment en CSS. De plus, cela m'a forcé a quasiment écrire toutes mes lignes à la main.

Il y a encore des ajouts HTML et CSS à faire, mais la version actuelle permet d'avoir une première section avec les données pour tester et incorporer le JS.

J'ai passé davantage de temps que prévu pour affiner et m'approprier le design de mon site. Je n'étais d'abord pas convaincue de la direction (dans les tons verts) avant de me décider sur un dark mode qui me permettait d'avoir des contrastes plus appréciables.

#### Rappels Javascript
Contrairement au HTML et CSS, je n'avais plus de souvenirs du JS. Un rappel théorique a été de rigueur, avec la formation du GInfo sur le Javascript. Cela m'a permis d'avoir déjà quelques intuitions sur les outils que j'utiliserais dans le second sprint (notamment pour la mise en cache au local).

J'ai aussi pu analyser et mieux comprendre comment été construit le site de James Turner. Cela m'a semblé lourd et peu flexible pour un jeu très complexe de données, avec de nombreuses informations redondantes. J'aimerais en discuter avant mon prochain sprint pour savoir si poursuivre en JS est le plus optimal pour "gérer la base de données" (d'autant plus, que JS ne communique pas entre les pages du site).

J'ai fait des premiers tests à partir d'exemples de codes de "to do list" trouvé sur le net et réadapté pour mon besoin, afin de sélectionner les items de la to do (et les marquer comme réalisé) pour la première catégorie d'item ("Morts")... Mais ils n'ont pas été fructueux. En fait, je me suis rendue compte que c'était comme si j'avais essayé de me lancer dans ma propre recette de cuisine improvisée avec tous les ingrédients en main... sauf que je ne m'étais pas rendue compte que je n'avais aucun ustensile dans ma cuisine. Bref,  survoler le concept ne suffira pas ici avant de s'amuser, il me faut creuser davantage et éclaircir les zones de floues qu'il me reste en suivant pas à pas quelques tutos basiques.

J'ai fini ce POK en me documentant sur JS et en recherchant les ressources utiles conseillées sur les autres MON/POK sur le sujet. Avant le début du sprint 2, je souhaite ainsi me pencher et faire quelques tests en dehors de ce projet avec :
* Le site MDN sur la section [Javascript](https://developer.mozilla.org/fr/docs/Web/JavaScript) ;
* Le cours OpenClassrooms ["Apprenez le Javascript](https://openclassrooms.com/fr/courses/7696886-apprenez-a-programmer-avec-javascript) ;
* Le cours OpenClassrooms ["Créer des pages web dynamiques avec JavaScript"](https://openclassrooms.com/fr/courses/7697016-creez-des-pages-web-dynamiques-avec-javascript) ;
* La page [Legacy JavaScript Algorithms and Data Structures](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/) de FreeCodeCamp (EN) ;
* Le cours de M. Brucker ["Javascript - bases"](https://francoisbrucker.github.io/cours_informatique/cours/web/javascript-bases/) ;
* Pléthore de vidéos YouTubes, de durées variables (EN) ;

J'ai été quelque peu perdue dans la quantité de ressources pour démarrer et dans le choix de celle qui sera la plus adaptée à mon besoin (avoir une bonne compréhension, sans prétendre à maîtriser l'outil).

Pour clôturer le sprint 1, j'ai réussi à faire une catégorie ouverte/fermée comme prévue en JS lors du sprint 2... mais sans JS, avec l'aide de la balise "details" en HTML ! Il reste néanmoins quelques sujets de style à régler et corriger (et notamment avec l'affichage de la balise "summary", qui entre en conflit avec mon titre H3 et les marges internes de mes boîtes).

#### Quid d'une base de données ?
J'avais hésité dès le départ à créer une base de données dans laquelle il serait facile d'ajouter un élément via l'interface plus tard. Pour me forcer à explorer au maximum Javascript, j'ai décidé de faire sans. Néanmoins, au vu du code sur le site d'inspiration, la rédaction est lourde et si l'on souhaite à terme avoir les mêmes données sur différentes pages, la donnée sera plutôt redondante (voire pire, une usine à gaz ?).

En me rendant finalement compte des timings réels d'un sprint, je pense revoir le back sur mon temps libre ainsi que les bases de données. La base de données pourra comprendre la "catégorie" d'items, le nom, son statut (réalisé ou non) et éventuellement d'autres informations complémentaires / utiles (*pex : des infos sur comment compléter tel item*).

#### Conclusion du sprint 1
J'étais finalement plus rouillée que je le pensais, mais cela m'a permis de repartir sur des bases solides en HTML et CSS... J'espère néanmoins rattraper ce léger retard sur le sprint 2.

### Second Sprint

### Conclusion et suites possibles
Souhaitant aborder d'autres sujets au cours de mes prochains POK & MON, je ne pense pas continuer ce projet dans ce cadre. Néanmoins, je souhaite poursuivre l'amélioration de cette page et du site dans le cadre de mon utilisation personnelle.

#### Ce que j'ai appris :
XXX

#### Les erreurs à éviter :
* Le CSS peut être très chronophage, surtout si on cherche à debug un bug graphique !
* Ne pas (toujours) foncer directement dans le code sans réfléchir...
* Ne pas fractionner son temps de travail : travailler 10h sur une journée car on se laisse emporter par le sujet, c'est tenable une fois mais ça ne permet pas d'avoir du recul et de bien mesurer le temps qu'on passe sur des détails parfois inutile (ou sur lesquels on manque de recul, et sur lesquels la nuit porterait conseil).