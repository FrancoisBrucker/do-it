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
- *Race Car Design*, de Derek SEWARD, consulté en pdf.
- *MATLAB - Simulink Tutorial for Beginners | Udemy instructor, Dr. Ryan Ahmed*, vidéo Youtube accessible [ici](https://www.youtube.com/watch?v=vxzR3W2BcRk)
- *MATLAB and Simulink Racing Lounge: Vehicle Modeling* accessible [ici](https://fr.mathworks.com/matlabcentral/fileexchange/63823-matlab-and-simulink-racing-lounge-vehicle-modeling).

## Sommaire

1. Objectifs
2. Tâtonnement
3. Première modélisation du comportement dynamique d'une monoplace


## Objectifs
Voici les objectifs que je me suis donné :
- Documentation et analyse de l'existant (moyen)
- Modélisation dynamique simple du comportement d'une monoplace (moyen)
- Etablir les paramètres d'intérêts pour une étude dynamique (facile)
- Complexifier l'étude avec un paramétrage plus poussé (compliqué, bonus)

## Tâtonnement
{% exercice %}
Comment s'y prendre ?
{% endexercice %}


A l'heure où je débute ce projet, je ne sais pas encore par quel bout le prendre. Je décide alors de me renseigner sur l'existant de la modélisation de la dynamique d'un véhicule par un point matériel, et ce sur Matlab ou sur un autre logiciel. 
J'ai passé plus de temps que prévu sur la documentation et la recherche. J'ai aussi du regarder une vidéo Youtube de 1 heure pour me remettre à niveau sur Simulink.
J'ai ensuite consulté sans m'attarder les deux documents .pdf, qui donnent les bases dynamiques d'un véhicule. Ceux-ci me permettent d'estimer plus précisément les paramètres importants à prendre en compte.

Je décide de m'orienter vers le package *MATLAB and Simulink Racing Lounge: Vehicle Modeling* accessible [ici](https://fr.mathworks.com/matlabcentral/fileexchange/63823-matlab-and-simulink-racing-lounge-vehicle-modeling). Une fois celui-ci téléchargé, je peux commencer ma modélisation.


## Première modélisation du comportement dynamique d'une monoplace
#### Prise en main de la bibliothèque
J'ai commencé par me mettre à jour sur le contenu de la bibliothèque. Celle-ci étant très fournie, j'effectue alors des petits tests pour visualiser des données simples, telles que l'angle du volant.

![Biblio Simulink](Bibliothèque.png)

#### Réalisation d'une première modélisation

