---
layout: layout/pok.njk

title: "Une étude de cas sur la gestion d'une cyberattaque"
authors:
  - TAING Henri

date: 2024-02-08

tags:
  - "temps 3"
  - Cybersécurité
  - Management
  - Gestion de projets
  - Gestion de risques

résumé: Ce POK a pour but de valoriser la connaissance que j'ai acquise au cours de mon alternance qui porte sur la gestion des cyberattaques. 

---

{%prerequis 'POK débutant+'%}
Un cerveau et vaguement quelques connaissances en tech
{%endprerequis%}

## Table des matières

1. [Objectifs et backlog produit](#section-1)
2. [Ce que j'ai prévu au 1er sprint et ce qui a été fait finalement](#section-2)
3. [Sprint 1 Review](#section-3)
4. [Ce que j'ai prévu au 2ème sprint et ce qui a été fait finalement](#section-4)
5. [Sprint 2 Review](#section-5)
6. [Conclusion](#section-6)
7. [Sources](#section-7)

## Objectifs et backlog produit <a id="section-1"></a>

**Les objectifs**

- Savoir écrire une étude de cas
- Intégrer le savoir que j'ai acquis durant la première partie de mon alternance
- Partager ce savoir 

**Backlog produit**

- <u>Faire un backlog précis et le mettre à jour</u> [X] = 2 (1h)

- <u>Lire et intégrer la documentation prêtée par Laetitia PIET sur la méthodologie pour créer une étude de cas</u> [X] = 1 (2h)

- <u>Rédiger l'étude de cas</u> [] = 6 (3h)

  - Choix et présentation de cas [X] = 2 (20 minutes)
  - Créer les arbres de décision pour I.AB [X] = 2 (1h40)
  - Créer les arbres pour II.1.B [] = 2 (1h)

- <u>Programmation du jeu</u> [] = 13

  - Coder les parties communes I. [X] = 7 (6h)

    - Implémenter I. [X] = 5 (5h)
      - Chapitre 1 [X]
      - Chapitre 2 [X]
      - Chapitre 3 [X]
      - Chapitre 4 [X]
      - Chapitre 5 [X]
    - Mettre les fonds/personnages/transitions dans I. [X] = 2 (1h)

  - Route A [X] = 2 (1h)

    - Fin A [X] = 1 (45 min)
    - Mettre les fonds/transitions fin A [X] = 1 (15 min)

  ~~- Coder les parties communes II.1 [] = 4 (3h30)~~


- <u>Customisation de GUI</u> [] = 2 (1h)

  - Menu principal [] = 1
  - Barre de dialogue [] = 1

- <u>Documenter le POK</u> [] = 1 (1h)

## Ce que j'ai prévu au 1er sprint et ce qui a été fait finalement <a id="section-2"></a>

**Backlog Sprint 1**
On prendra comme user-stories à faire :

- <u>Faire un backlog précis et le mettre à jour</u> [X] = 3 (2h)

- <u>Rafraîchir ses connaissances en Python et prendre en main Renpy</u> [X] = 5 (1h30)

- <u>Gestion des ressources infographiques pour le jeu, personnages et fonds</u> [X] = 2 -> 3 (1h -> 2h)

- <u>Arbre de décision Figma</u> [] = 4 (2h)

  - Parcourir le scénario et décider des points de ruptures [X] = 2 (20 minutes)
  - Créer les arbres de décision pour I.AB [X] = 2 (1h40)

- <u>Coder les parties communes I.</u> [] = 5

  - Implémenter I. [] = 5 (5h)
    - Chapitre 1 [X]
    - Chapitre 2 [X]
    - Chapitre 3 []
    - Chapitre 4 []
    - Chapitre 5 []

**Ajouté durant le sprint car c'était trop moche**

- <u>Customisation de GUI</u> [X] = 2 (1h)

  - Menu principal [X] = 1
  - Barre de dialogue [X] = 1

## Sprint 1 Review <a id="section-3"></a>

J'ai sous-estimé le temps à prendre pour adapter mon texte à la fenêtre de dialogue et au code en général, sans compter les nombreux bugs que j'ai eus au début pendant la prise en main, et les problèmes d'images.

Mais, maintenant que la partie d'adaptation est passée, j'irai beaucoup plus vite. Pour autant, le backlog ne pourra pas être effectué en entier réalistiquement dans la limite des 20h. Il faudra aussi compter le temps de déploiement/mise en ligne du jeu que j'avais oublié initialement. 

Une chose qui est sûre, maintenant, je comprends pourquoi les jeux sont généralement fait par des studios et non des personnes toutes seules. Scénariste, graphiste et développeur, ça commence à faire beaucoup. 

# Quelques images

**Changement de l'interface (GUI) avec à gauche la version basique et à droite la version actuelle**
:-------------------------:|:-------------------------:
<img src="welcome_basic.png" width="350" height="350"> | <img src="welcome_aimer.png" width="350" height="350">
<img src="menu_basic_save.png" width="350" height="350"> | <img src="menu_aimer_save.png" width="350" height="350">
<img src="menu_basic_preferences.png" width="350" height="350"> | <img src="menu_aimer_preferences.png" width="350" height="350">

**Une image du jeu et le code associé**
<img src="image1.png">

```
define j = Character('Jeanne', color="#006416") #Définition du personnage

label start:  #début du jeu

  scene bg bus_stop_night     #appelle l'arrière-plan

  show jeanne cold smile at left       #appelle l'image associée
  show lise turtleblacksmile at right

  j "Jeanne. Same as you."        #dialogue

return      #fin du jeu
```

**Situation de choix et code associé**
<img src="choix1.png">

```
menu:     #crée le menu de choix

        "Prout.":
            jump suite1_1_1    #envoie vers suite1_1_1

        "Wanna be friends?":
            jump suite1_1_2

    label suite1_1_1:

        j "Wanna be friends?"

        jump suite1_1_2

    label suite1_1_2:

        j "Like friends?"
```

## Ce que j'ai prévu au 2ème sprint et ce qui a été fait finalement <a id="section-4"></a>

**Backlog Sprint 2**
On prendra comme user-stories à faire :

~~- <u>Le reste de l'arbre de décision Figma</u> [] = 2 (1h)~~

  ~~- Créer les arbres pour II.1.B [] = 2 (1h)~~

- <u>Coder la deuxième moitié des parties communes I.</u> [X] = 3 (3h -> 4h)

  - Implémenter I. [X] = 5 (2h -> 3h)
    - Chapitre 3 [X]
    - Chapitre 4 [X]
    - Chapitre 5 [X]
  - Mettre les fonds/personnages/transitions dans I. [] = 2 (1h)

- <u>Route A</u> [X] = 2 (1h)

  - Fin A [X] = 1 (45 min)
  - Mettre les fonds/transitions fin A [X] = 1 (15 min)

~~- <u>Début II.</u> [] = 1 (1h)~~

~~  - Chapitre 1 [] = 1~~

- <u>Déploiement du jeu</u> = 3 [X] (1h)

- <u>Test et débug</u> = 2 [X] (1h)

## Sprint 2 Review <a id="section-5"></a>

J'ai oublié l'importance de tester et retester au fur et à mesure. Pour preuve, ça m'a beaucoup ralenti sur la deuxième moitié de la partie 1, car j'ai dû tout reprendre petit à petit. 
Le déploiement s'est effectué beaucoup plus facilement que prévu grâce au build fourni par Renpy.


## Conclusion <a id="section-6"></a>

Je conseille Renpy pour faire un visual novel. C'est simple. Barbant. Efficace. Un vrai outil de débutant. 
J'aurais néanmoins voulu avoir plus (beaucoup plus) de temps pour vraiment finir de coder **tout mon roman** et ne pas simplement livrer la première partie, et également pour nettoyer et organiser mieux le code.

Enfin, tant mieux que ce soit fini, j'allais devenir fou. 

Voici le lien pour essayer mon jeu ! 
[Le jeu !](https://henritaing.itch.io/merrychristmas)

## Sources <a id="section-7"></a>

[Tutoriel pour créer un jeu avec Renpy (en anglais)](https://www.youtube.com/watch?v=C3Ldd-5PKCw&ab_channel=ZeilLearnings) de ZeilLearnings
[Documentation pour débuter sur Renpy](https://www.renpy.org/doc/html/quickstart.html)
[Customiser l'interface graphique (GUI)](https://www.renpy.org/doc/html/gui.html#gui)
[Ressources pour les arrières-plans](https://lemmasoft.renai.us/forums/viewtopic.php?t=17302)
[Autre ressources pour les arrières-plans](https://noranekogames.itch.io/yumebackground)
[Ressources pour les personnages](https://sutemo.itch.io/)
[Déploiement du jeu sur itch.io](https://www.youtube.com/watch?v=WTatB4W-vKg)
[Le jeu !](https://henritaing.itch.io/merrychristmas)