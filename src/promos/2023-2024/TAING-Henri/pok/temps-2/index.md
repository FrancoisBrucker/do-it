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

- Apprendre à utiliser l'outil Renpy (Pour la création du jeu)
- Se familiariser avec Figma (Pour faire l'arbre de décisions)
- Avoir une raison de finir d'écrire mon livre (Il sera simplifié pour le jeu, les 3/4 sont déjà écrits), il est en **anglais** donc ne soyez pas surpris que tout soit codé en anglais, etc.
- Créer un jeu qui dure environ 1h30 avec trois fins différentes, A, B et C (dont une qui est simplement une sorte de game-over). **Après avoir tâté un peu le terrain, on tentera déjà la fin A et la partie commune à B et C**.

**Backlog produit qui évoluera**

Le roman est divisé en plusieurs parties I., II.1. (première moitié de la deuxième partie du roman), II.2., III.1., III.2.

- <u>Faire un backlog précis</u> [] = 3 (1h30)

- <u>Rafraîchir ses connaissances en Python et prendre en main Renpy</u> [] = 5 (1h30)

- <u>Gestion des ressources infographiques pour le jeu, personnages et fonds</u> [] = 1 (30 minutes)

- <u>Arbre de décision Figma</u> [] = 11 (4h)

  - Parcourir le scénario et décider des points de ruptures [] = 2 (20 minutes)
  - Créer les arbres de décision pour I.ABC [] = 2 (1h40)
  - Créer les arbres pour II.1.BC [] = 2 (1h30)
    <!-- - Créer les arbres pour II.2.B [] = 1 (40 min) -->
    <!-- - Créer les arbres pour III.B [] = 1 (30 min)
  - Créer les arbres pour III.C [] = 1 (40 min) -->
  - Vérifier la cohérence [] = 1 (30 min)

- <u>Programmation du jeu</u> [] = 34

  - Coder les parties communes [] = 15 (10h)

    - Définir les flags qui nous serviront pour passer d'une route à l'autre [] = 5
    - Petits choix 1ère partie du roman [] = 3
    - Implémenter le scénario/petits choix + 1er grand choix qui sont communs aux trois routes dans I. [] = 5
    - Implémenter scénario/petits choix + 2e grand choix + 3e grand choix qui sont communs aux routes B et C dans II.1. [] = 5
    - Mettre les fonds/personnages dans I. [] = 2
    - Mettre les transitions dans I. [] = 1
    - Mettre les fonds/personnages dans I. [] = 2
    - Mettre les transitions dans I. [] = 1

  - Route A [] = 5 (1h)

    - Pages fin A [] = 1
    - Mettre les fonds qui manquent [] = 1
    - Mettre les transitions [] = 1

  - Route B [] = 7 (1h)

    - Pages fin B [] = 1
    - Mettre les fonds qui manquent [] = 1
    - Mettre les transitions [] = 1

  <!-- - Route C [] = 7 (1h30)
    - Petits choix II.2.C après 2ème grande décision [] = 2
    - Petits choix III.C après 3ème grande décision [] = 2
    - Page fin C [] = 1
    - Mettre les fonds qui manquent [] = 1
    - Mettre les transitions [] = 1 -->

- <u>Customisation de GUI</u> [] = 2 (30 minutes)
  - Menu principal [X] = 1
  - Barre de dialogue [X] = 1

## Ce que j'ai prévu au 1er sprint <a id="section-2"></a>

**Backlog Sprint 1**
On prendra comme user-stories à faire :

- <u>Faire un backlog précis</u> [X] = 3 (1h30)

- <u>Rafraîchir ses connaissances en Python et prendre en main Renpy</u> [X] = 5 (1h30)

- <u>Gestion des ressources infographiques pour le jeu, personnages et fonds</u> [X] = 1 (30 minutes)

- <u>Arbre de décision Figma</u> [] = 11 (Environ 4h)

  - Parcourir le scénario et décider des points de ruptures [X] = 2 (20 minutes)
  - Créer les arbres de décision pour I.ABC [X] = 2 (1h40)
  - Créer les arbres pour II.1.BC [] = 2 (1h30)
  - Vérifier la cohérence [] = 1 (30 min)

- <u>Programmation du jeu</u> [] = 5h

  - Coder les parties communes

    - Petits choix 1ère partie du roman [] = 2 -> 3 (Pour les bugs)
    - Implémenter le scénario/petits choix + 1er grand choix qui sont communs aux trois routes dans I. [] = 5 -> 8 (Me prend beaucoup plus de temps que prévu, car je dois 1. Adapter le texte à la fenêtre d'affichage 2. Résoudre les bugs/Retrouver les problèmes d'indentation)

- <u>Customisation de GUI</u> [X] = 2 (30 minutes)
  - Menu principal [X] = 1
  - Barre de dialogue [X] = 1

## Sources <a id="section-6"></a>

[Tutoriel pour créer un jeu avec Renpy (en anglais)](https://www.youtube.com/watch?v=C3Ldd-5PKCw&ab_channel=ZeilLearnings) de ZeilLearnings
[Documentation pour débuter sur Renpy](https://www.renpy.org/doc/html/quickstart.html)
[Customiser l'interface graphique (GUI)](https://www.renpy.org/doc/html/gui.html#gui)
[Ressources pour les arrières-plans](https://lemmasoft.renai.us/forums/viewtopic.php?t=17302)
[Ressources pour les personnages](https://sutemo.itch.io/)
