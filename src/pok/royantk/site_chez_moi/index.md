---
layout: layout/post.njk

title: "[POK] Find the Key"
authors:
  - Killian ROYANT

tags: ['pok']
---

<!-- début résumé -->

Présentation de mon POK du temps 1 & 2 : Find The Key

<!-- fin résumé -->

{% chemin %}

**Ressources**

- [Le résultat du POK (front)](https://royantk.github.io/FindTheKey/)
- [Le Github du POK](https://github.com/royantk/FindTheKey)

{% endchemin %}

## Introduction

**Find The Key** est un jeu que j'ai développé durant mon S7. Le but est de trouver la clé placée aléatoirement sur un plateau puis de la ramener à la base en évitant les monstres.

![Image Find The Key](FindTheKey.png)

Find The Key a été d'abord designé à l'aide du logiciel de maquettage Adobe XD. J'ai ensuite utilisé un plugin pour transformer ce design en fichiers HTML et CSS. J'ai enfin dû adapter ces fichiers afin de les rendres utilisables pour communiquer avec le fichier JavaScript devant gérer le jeu.

Néanmoins, le projet a rencontré des **problèmes**, dont la plupart liés à l'exportation au format HTML/CSS depuis Adobe XD :

- La maquette étant dessinée par rapport à un certain nombre de pixels, le site n'est donc **pas responsif**
- La **police** utilisée sur le logiciel n'était **pas disponible** dans les fichiers exportés, ce qui rendait impossible leur affichage en ligne
- Le jeu n'est **pas compatible** avec des navigateurs comme **Firefox**. En effet, le fichier JavaScript responsable du placement des cases sur la mini carte utilise du code imcompatible avec le moteur de Firefox.
- Enfin, la **structure générée** par l'exportation au format HTML/CSS par le plugin d'Adobe XD est plutôt **brouillon** : un empilement de balises SVG dont les liens avec le fichier CSS sont mals optimisés et chaotiques. Ainsi, l'**utilisation et la modification du code** se trouvaient très difficiles.

### Objectif - Améliorer et réparer le jeu

Mes objectifs à l'occasion de ce POK sont les suivants :

- **Reprendre, réparer et améliorer** le contenu du projet commencé au S7
- **Transformer** le projet **en un projet Full Stack** à l'aide de Node.js et d'Express afin de gérer la génération des cases en back et de créer un système d'utilisateurs

### To-Do List

N'ayant pas les compétences nécessaires au développement full stack, j'ai décidé de consacrer mes MON à l'apprentissage du développement full stack et de me concentrer uniquement sur la refonte du **front pour le temps 1**. Le **temps 2** sera consacré à l'**implémentation du back**.

- **Temps 1**
  - ~~Régler le problème de police~~ *(fait)*
  - ~~Régler le problème de compatibilité Firefox~~ *(fait)*
  - Reprendre le code HTML/CSS pour l’améliorer (responsivité, gestion du CSS, etc.) *(commencé)*
  - Améliorer le jeu
    - Ajout d’un personnage
    - Ajout de pièces
  - Commencer à ajouter une partie « back » au site
- **Temps 2**
  - Continuer d'ajouter la partie « back » au site
    - Création du back
    - Déplacement de la génération des cases
    - Création d'une gestion des utilisateurs

[<-- Retour](../)
