---
layout: layout/pok.njk

title: "Aimer, un petit jeu suivant une romance ordinaire"
authors:
  - TAING Henri

date: 2023-10-16

tags:
  - "temps 2"
  - Renpy
  - Python

résumé: Ce POK a pour but de créer un visual novel - un roman avec des images dans lequel on peut faire des choix pour orienter l'histoire - à l'aide de Renpy. Il reprendra un roman que j'ai écrit, mais que je n'ai pas fini. Ce sera l'occasion pour moi de finir de l'écrire et de coder un petit jeu.
---

{%prerequis 'POK débutant+'%}
Avoir fait un poil de Python, juste un petit peu, pour ne pas être perdu au début et donc ne pas perdre la motivation
{%endprerequis%}

## Table des matières

1. [Objectifs et backlog produit](#section-1)
2. [Ce que j'ai prévu au 1er sprint](#section-2)
3. [Ce que j'ai fait au 1er sprint](#section-3)
4. [Ce que je prévoyais pour le 2ème sprint](#section-4)
5. [Ce que j'ai fait au 2ème sprint](#section-5)
6. [Sources](#section-6)

## Objectifs et backlog produit <a id="section-1"></a>

**Les objectifs**

- Prendre en main l'outil Renpy (Pour la création du jeu)
- Se familiariser avec Figma (Pour faire l'arbre de décisions)
- Avoir une raison de finir d'écrire mon livre (Il sera simplifié pour le jeu, les 3/4 sont déjà écrits), il est en **anglais** donc ne soyez pas surpris que tout soit codé en anglais, etc.
- Créer un jeu qui couvrira la partie I et la partie II de mon roman.

**Backlog produit qui évoluera**

A : Lié à la fin A | B : Lié à la fin B | C : Lié à la fin C
Le roman est divisé en plusieurs parties I.ABC., II.BC et III.B et III.C, mais on ne s'intéressera qu'à I.ABC, II.1.BC.

- <u>Faire un backlog précis et le mettre à jour</u> [] = 3 (2h)

- <u>Rafraîchir ses connaissances en Python et prendre en main Renpy</u> [] = 5 (1h30)

- <u>Gestion des ressources infographiques pour le jeu, personnages et fonds</u> [] = 2 (1h)

- <u>Arbre de décision Figma</u> [] = 6 (3h)

  - Parcourir le scénario et décider des points de ruptures [] = 2 (20 minutes)
  - Créer les arbres de décision pour I.AB [] = 2 (1h40)
  - Créer les arbres pour II.1.B [] = 2 (1h)

- <u>Programmation du jeu</u> [] = 13

  - Coder les parties communes I. [] = 7 (6h)

    - Implémenter I. [] = 5 (5h)
      - Chapitre 1 []
      - Chapitre 2 []
      - Chapitre 3 []
      - Chapitre 4 []
      - Chapitre 5 []
    - Mettre les fonds/personnages/transitions dans I. [] = 2 (1h)

  - Route A [] = 2 (1h)

    - Fin A [] = 1 (45 min)
    - Mettre les fonds/transitions fin A [] = 1 (15 min)

  - Coder les parties communes II.1 [] = 4 (3h30)

    - Implémenter II.1 [] = 3 (3h)
      - Chapitre 1 []
      - Chapitre 2 []
    - Mettre les fonds/personnages/transitions dans I. [] = 1 (30 min)

- <u>Customisation de GUI</u> [] = 2 (1h)

  - Menu principal [] = 1
  - Barre de dialogue [] = 1

- <u>Documenter le POK</u> [] = 1 (1h)

## Ce que j'ai prévu au 1er sprint et ce qui a été fait finalement <a id="section-2"></a>

**Backlog Sprint 1**
On prendra comme user-stories à faire :

- <u>Faire un backlog précis et le mettre à jour</u> [X] = 3 (2h)

- <u>Rafraîchir ses connaissances en Python et prendre en main Renpy</u> [X] = 5 (1h30)

- <u>Gestion des ressources infographiques pour le jeu, personnages et fonds</u> [X] = 2 (1h)

- <u>Arbre de décision Figma</u> [] = 6 (3h)

  - Parcourir le scénario et décider des points de ruptures [X] = 2 (20 minutes)
  - Créer les arbres de décision pour I.AB [X] = 2 (1h40)
  - Créer les arbres pour II.1.B [] = 2 (1h)

- <u>Coder les parties communes I.</u> [] = 7 (6h)

  - Implémenter I. [] = 5 (5h)
    - Chapitre 1 [X]
    - Chapitre 2 [X]
    - Chapitre 3 [X]
    - Chapitre 4 []
    - Chapitre 5 []
  - Mettre les fonds/personnages/transitions dans I. [] = 2 (1h) **Ajouté pendant le sprint**

- <u>Customisation de GUI</u> [X] = 2 (1h) **Ajouté pendant le sprint**

  - Menu principal [X] = 1
  - Barre de dialogue [X] = 1

## Sources <a id="section-6"></a>

[Tutoriel pour créer un jeu avec Renpy (en anglais)](https://www.youtube.com/watch?v=C3Ldd-5PKCw&ab_channel=ZeilLearnings) de ZeilLearnings
[Documentation pour débuter sur Renpy](https://www.renpy.org/doc/html/quickstart.html)
[Customiser l'interface graphique (GUI)](https://www.renpy.org/doc/html/gui.html#gui)
[Ressources pour les arrières-plans](https://lemmasoft.renai.us/forums/viewtopic.php?t=17302)
[Ressources pour les personnages](https://sutemo.itch.io/)
