---
layout: layout/post.njk

title: "Mon sheet c'est moi"
authors:
  - Léonard Barbotteau
  - Nathan Gissler

tags: []
---

<!-- début résumé -->
Mon sheet c'est moi (POK-Temps 1)
<!-- fin résumé -->
## 1. Idée initiale
<br/><br/>

## 2. Première version de partition interactive
<br/><br/>

## 3. To-do list
<br/><br/>
- ### Coder la partition en Javascript :
  #### A l'aide de javascript et dans un canvas html, dessiner la portée et la coder de telle sorte que:
    - On affiche au départ les barres de mesure et les silences tant que les rondes ne sont pas placées
    - On puisse placer des notes (pour l'instant des rondes) où l'on veut en cliquant sur la partition
    - Quand on passe le curseur sur un emplacement vacant, une note grisée s'affiche
    - On puisse les retirer en appuyant sur un bouton qui change le mode (ajouter une note/supprimer une note) 
<br/><br/>
- ### Permettre de lire la partition (lecture audio de la partition)
  #### Liste des fonctionnalités à mettre en place:
    - Un bouton pour lire la partition
    - (Un bouton pour changer le tempo)
<br/><br/>
- ### Arborescence du site
  #### Créer une arborescence du site:
    - L'accueil avec description du fonctionnement du site, puis le choix entre faire une nouvelle partition ou en ouvrir une sauvegardée
    - Le choix de la partition où l'on peut retrouver les partitions sauvegardées ou en créer une nouvelle 
    - La page avec la partition correspondante (et peut-etre une bulle d'aide visible d'une certaine manière) et les différents boutons qui permettent de modifier la partition
<br/><br/>
- ### Sauvegarder les partitions
  #### Trouver un moyen de sauvegarder la partition modifiée:
    - Stocker les informations dans un fichier d'un format spécifique (json à priori)
    - Pouvoir nommer et renommer le fichier depuis le site