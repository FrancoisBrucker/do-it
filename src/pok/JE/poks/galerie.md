---
layout: layout/post.njk

title: "Ma galerie pour mon portfolio"

authors:
  - Jeffrey Edisah

tags :
  - 'info'
  - 'java'
  - 'spring'
---

<!-- début résumé -->

Pour continuer sur le POK précédent, je me lance dans le développement d'une galerie d'images où je peux charger les images simplement et qui s'occupera de la mise en page.

<!-- fin résumé -->

Voici le lien vers mon [repo github](https://github.com/JeffreyEdisah/Image-Gallery)

Vu que mon stage sera en Spring, j'utiliserai Spring pour le backend de cette app, ainsi que React et du CSS classique pour le front end. Les images seront stockées soient dans une base de données MongoDB, soit dans l'object storage d'AWS S3.

## 1er sprint :
- Faire le back de la page d'upload
- Faire un premier component React pour une image

### Bilan :
Il s'avère que pour ce 1er sprint je n'ai pas assez décomposé mes tâches, dans le sens où j'ai des connaissances en Spring mais pas en gestion de fichiers en Java. Or c'est le coeur de ce que je veux faire, déplacer des fichiers dans un système. Le système Spring est donc fait, il me reste donc à voir comment gérer les flux de fichiers en Java pour faire un Storage Service. Je vais essayer pour ce 2ème sprint de mieux découper mes tâches.

## 2ème sprint :

- Programmer le Storage Service
- Ajouter du react au template Thymeleaf
- Tester le Storage Service avec un fichier .txt
- Déployer le Storage Service de texte
- Le transformer en Storage Service pour des images
- Créer un composant React de base pour mes images
- (Sous réserve de temps) Faire un programme de conversion de PNG en WEBP

Ce sprint est assez ambitieux, mais mieux découpé que mon premier sprint.
