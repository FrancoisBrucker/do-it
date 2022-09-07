---
layout: layout/post.njk

title: "Jeu Mots croisés"
authors:
  - Nicolas BERT
  - Jean-Baptiste DURAND

tags: ['pok']
---

<!-- début résumé -->
Mon site chez moi (POK-Temps 1)
<!-- fin résumé -->


## Idée de ce POK

L'idée de ce POK est de créer une site contenant une partie frontend, une partie backend qui va communiquer avec le frontend via une API. On ajoutera également une base de données afin de pouvoir stocker les informations.

Dans ce POK nous allons recrée un jeu de ticket à gratter : le jeu de mots croisés. Voici une photo du ticket en question :

<img src="./images/mots-croises.jpg" alt="Image jeu de mots croisés" style="height: 500px; margin: 0 auto;" />
<br>

{% info %}
**Règles du jeu**
Nous disposons de 14 cases **?** et d’une grille de mots. Derrière chaque case se trouve une lettre qui apparaît dans la grille. A chaque lettre révélée il faut gratter les occurrences de cette lettre dans la grille. Une fois toutes les cases **?** grattées, on remporte de l’argent suivant le nombre de mots entièrement reconstitués.
{% endinfo %}

## Technologies utilisées

<img src="./images/choix_techno.jpg" alt="Technologies utilisées" style="height: 500px; margin: 0 auto; border: 0" />

-  **Front-end** : Svelte + TailwindCSS
- **Back-end** : NestJS
- **API** : GraphQL
- **Moyen d'authentification** : JWT (*JSON Web Token*)
- **Base de données** : MongoDB

## Fonctionnalités

Par la suite, le back-end fera appelle à une API de dictionnaire qui répcupèrera une liste de mots et un algorithme s'occupera de générer la grille de mots croisés à partir de cette liste de mots.

Gestion des utilisateurs, avec connexion et gestion de solde.

## Objectifs points POK

<!-- ### Ce qu'on avait prévu la dernière séance
### Ce qu'on a fait depuis
### Ce qu'on prévoit pour la prochaine séance  -->

### Ce qu'on a prévu pour la prochaine séance

- *Découvrir* les framework pour le front : Svelte et TailwindCSS
  - [Tuto Svelte](https://svelte.dev/tutorial/basics)
  - [Tuto TailwindCSS](https://tailwindcss.com/docs/installation)
  - TailwindCSS with Svelte : [lien 1](https://blog.logrocket.com/how-to-use-tailwind-css-with-svelte/), [lien 2](https://tailwindcss.com/docs/guides/sveltekit)
- Créer une *ébauche* de front en static
  - Créer une page avec des *éléments simples* 
  - Créer une page avec différents *components*
  - Commencer à structurer la page du projet
    - Component *grille*
    - Component *navbar*
    - Component *info utilisateurs*
