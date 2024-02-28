---
layout: layout/pok.njk

title: "Apprendre Unity avec un jeu mobile"
authors:
  - Vladimir Jeantroux

date: 2023-09-18

tags:
  - 'temps 3'
  - 'POK'
  - 'Unity'
  - 'C#'
  - 'Jeu mobile'

---

## Description 

Pour continuer dans ma lancée d'apprendre des moteurs de création de jeux, j'ai décidé de m'attaquer à Unity, en créant un jeu mobile simple dans le style de Subway Surfers ou Temple Run, pour Android. 

**Pourquoi Unity ?**

Unity est l'un des moteurs les plus populaires dans le milieu du développement de jeux vidéo, notamment dans l'industrie mobile. Il est très complet, adapté à de multiples plateformes, et dispose d'une documentation extrêmement fournie. De plus, parmi les plus gros moteurs, il est aussi parmi les plus faciles à prendre en main pour un débutant. Unity utilise aussi C#, langage avec lequel je suis déjà familier et qui me permettrait de pratiquer la programmation orientée objet. J'aimerais travailler dans le gamedev plus tard, et donc pour m'y préparer je souhaite expérimenter avec différents moteurs de jeu et élargir mon éventail de ressources. Unity est aussi gratuit.

**Qu'a-t-on appris du [dernier POK](https://francoisbrucker.github.io/do-it/promos/2023-2024/Vladimir-Jeantroux/pok/temps-2/) ?**

- __Faire de son premier jeu quelque chose de simple.__ Les jeux de combat, bien que complet et permettent de passer en revue beaucoup d'éléments d'apprentissage pour le développement d'un jeu vidéo, sont aussi extrêmement difficiles à développer en entier, et surtout ensuite d'en faire quelque chose de fonctionnel. J'ai dû dessiner moi même des personnages afin que le jeu soit un minimum lisible, aussi bien pour un joueur qu'un développeur. Ici, on va faire un jeu où il faut attraper des pièces et sauter par dessus des obstacles. Tous les éléments du jeu (ou presque) seront des cubes colorés.

- __Choisir son moteur en fonction du jeu qu'on veut faire, et pas l'inverse.__ Godot est un moteur populaire, mais pas adapté pour les jeux de combat. Unity, en revanche, a beaucoup de support et d'extensions permettant de travailler avec des applis Android et iOS, rendant tout le développement un peu plus fluide.

- __Prévoir son POK selon le contenu de ses MON précédents.__ Enseignement un peu plus général, mais ici je n'aurai pas à apprendre tout un langage en même temps que le moteur que j'utilise pour le POK. J'ai des bases de C#, et quelques notions de game design grâce au MON sur Rust.

## Backlog initial

**Sprint 1 : Le jeu de base**

- Se documenter sur Unity(2h) []
- Création du personnage (1h) []
- Création de la carte/piste (2h) []
- Système de score, comptage, meilleur score,... (2h) []
- Ajout d'obstacles (1h) []
- Perdre et recommencer (1h) []

**Sprint 2 : Fonctions supplémentaires**

- Menus (1h) []
- Boutique et monnaie in-game (1h30) []
- Power-ups (2h) []
- Pubs (1h) []
- Processus tournant lorsque l'appli est fermée (1h) []
- Pouvoir continuer si on perd (1h30)[]
- Exportation en application (1h)

## Résumé du Sprint 1

Bonne nouvelle : les objectifs du sprint 1 ont été fait en la moitié du temps. Mauvaise nouvelle : je n'ai pas pu avancer plus à cause d'imprévus. Pour le moment, on a un jeu très rudimentaire : un cube pouvant seulement sauter par dessus des obstacles s'avançant vers lui à des intervalles aléatoires. Le score augmente à chaque seconde où le joueur encore en vie, et le jeu recommence si le joueur touche un obstacle. C'est un jeu très simple, mais déjà fonctionnel, par dessus lequel je pourrai construire et ajouter des fonctionnalités. 

![Capture en jeu](./basegame.JPG "Capture d'écran du jeu")

## Ajustements et objectifs pour le Sprint 2

En plus des objectifs déjà établis pour le sprint 2 :
- Faire des obstacles qui apparaissent sur les pistes gauche et droite 
- Héberger sur un serveur les infos telles que le meilleur score
- Rendre le jeu compatible sur iOS 

## Bibliographie 

- Documentation Unity : https://docs.unity.com
- Procedural Generation: Endless Runner Unity Tutorial : https://www.youtube.com/watch?v=Ldyw5IFkEUQ
- 3D ENDLESS RUNNER IN UNITY - JUMP : https://www.youtube.com/watch?v=x-EtYggJdP0&list=PLvcJYjdXa962PHXFjQ5ugP59Ayia-rxM3

**Horodatage**

*Sprint 1*
>Initiation sur les fonctions utiles de Unity pour le projet (1h30)
>Initialisation d'éléments basiques et leurs interactions terrain/joueur/obstacle (1h45)
>Programmation du comportement du jeu (quand et où les obstacles apparaissent) (30 min)
>Création du score, et d'un menu rudimentaire (45 min)
>Implémentation des mouvements gauche et droite (45 min)

*Sprint 2*