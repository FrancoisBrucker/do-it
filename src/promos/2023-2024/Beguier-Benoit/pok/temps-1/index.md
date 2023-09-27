---
layout: layout/pok.njk

title: "Modélisation dynamique d'une monoplace : d'un point matériel à un modèle simplifié"
authors:
  - Benoit BEGUIER

date: 2023-09-27

tags: 
  - "temps 1"
  - "Modélisation"
  - "Matlab"

résumé: Je vais dans ce POK effectuer une modélisation d'une monoplace. Le but est de commencer par la modélisation la plus simpliste, le point matériel, pour arriver à un modèle plus poussé et permettant de jouer sur plusieurs paramètres qui seront à déterminer.
---

{% prerequis %}
**Niveau :** intermédiaire
**Prérequis :**
- Bases de programmation
- Matlab et Simulink
{% endprerequis %}

Pour la réalisation de ce cours, j'aurais plusieurs sources principales : 
- *Race Car Vehicle Dynamics*, de William F. MILLIKEN et Douglas L. MILLIKEN, consulté en pdf.
- *Race Car Design*, de Derek Seward
- *MATLAB and Simulink Racing Lounge: Vehicle Modeling* accessible [ici](https://fr.mathworks.com/matlabcentral/fileexchange/63823-matlab-and-simulink-racing-lounge-vehicle-modeling)

## Sommaire

1. Objectifs
2.Tâtonnement
3. Première modélisation du comportement dynamique d'une monoplace



## Objectifs
Voici les objectifs que je me suis donné :
- Documentation et analyse de l'existant
- Modélisation dynamique simple du comportement d'une monoplace
- Etablir les paramètres d'intérêts pour une étude dynamique
- Complexifier l'étude avec un paramétrage plus poussé

## Tâtonnement
{% exercice %}
Comment s'y prendre ?
{% endexercice %}


A l'heure où je débute ce projet, je ne sais pas encore par quel bout le prendre. Je décide alors de me renseigner sur l'existant de la modélisation de la dynamique d'un véhicule par un point matériel, et ce sur Matlab ou sur un autre logiciel. Après plusieurs recherches, je décide de m'orienter vers le package *MATLAB and Simulink Racing Lounge: Vehicle Modeling* accessible [ici](https://fr.mathworks.com/matlabcentral/fileexchange/63823-matlab-and-simulink-racing-lounge-vehicle-modeling). Une fois cela fait, je fixe alors mes objectifs.


## Première modélisation du comportement dynamique d'une monoplace
#### Prise en main de la bibliothèque
J'ai commencé par me mettre à jour sur le contenu de la bibliothèque.

![Biblio Simulink](Bibliothèque.png)

#### Réalisation d'une première modélisation

