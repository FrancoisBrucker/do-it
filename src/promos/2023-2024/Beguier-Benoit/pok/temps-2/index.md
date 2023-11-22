---
layout: layout/pok.njk

title: "Ouais Benoît fait son site Internet"
authors:
  - Benoit BEGUIER

date: 2023-12-13

tags: 
  - "temps 2"
  - "Spotify"
  - "Playlist"
  - "HTML"
  - "CSS"
  - "API"

résumé: Je vais dans ce POK créer mon site Internet permettant à l'utilisateur d'analyser ses goûts musicaux, en utilisant l'API de Spotify.
---

{% prerequis %}
**Niveau :** débutant
**Prérequis :**
- Bases de développement Web (HTML et CSS)
- Des prérequis en utilisation d'API peuvent être un plus mais ne sont pas indispensables
{% endprerequis %}

Pour la réalisation de ce cours, je me réfèrerais aux sources listées ci-dessous : 

- *Créez votre site web avec HTML5 et CSS3.* OpenClassrooms. Accessible [ici](https://openclassrooms.com/fr/courses/1603881-creez-votre-site-web-avec-html5-et-css3).
- Developer Mozilla. Accessible [ici](https://developer.mozilla.org/fr/)

## Sommaire

1. Objectifs du Sprint 1
2. Objectifs du Sprint 2
3. Maquette Figma
4. Création des pages du site en HTML
5. Mise en page V1 en CSS
6. Retour d'expérience du Sprint 1


Le but de ce POK est de mettre en pratique mon MON1.2 sur le développement web. Je souhaite créer un site web fonctionnel, qui utilise l'API de Spotify. Ce site permettrait à l'utilisateur de connecter son compte Spotify personnel, et en retour afficher une analyse de ses goûts musicaux.

{% exercice %}
"Analyser les goûts musicaux de l'utilisateur" : ça veut dire quoi concrètement ?
{% endexercice %}

Il y a une multitude d'analyses possibles à partir d'un compte Spotify.
Concrètement j'aimerais proposer les fonctionnalités suivantes :

- Afficher une liste des principaux genres de musique que l'utilisateur écoute
  - Si possible, afficher un graphique des genres écoutés en fonction de l'heure de la journée. Cela pourrait (et je dis bien pourrais) potentiellement mettre en avant une tendance de l'utilisateur : par exemple des musiques mouvementées à haut *bpm* (*beats per minute*) en fin d'après-midi lors de sa séance de sport.

- Afficher des graphiques décomposant les musiques écoutées par l'utilisateur selon des paramètres définis dans la suite du POK.

- En bonus, effectuer une analyse en composantes principales (ACP, *PCA* en anglais) des musiques écoutées par l'utilisateur, et afficher le spectre d'écoute (*cf.* image ci-dessous). Vous pourrez trouver [ici](https://fr.wikipedia.org/wiki/Analyse_en_composantes_principales) la documentation sur l'ACP.





## Objectifs du Sprint 1
Voici les objectifs que je me suis fixé :
- Première maquette sur Figma (★☆☆☆☆, 2 heures estimées)
- Création des pages et de leur contenu primaire en HTML (★☆☆☆☆, 4 heures estimées)
- Mise en page V1 en CSS (★★☆☆☆, 4 heures estimées)

Les étoiles correspondent au niveau de difficulté de l'objectif dans mon référentiel de débutant en DevWeb.