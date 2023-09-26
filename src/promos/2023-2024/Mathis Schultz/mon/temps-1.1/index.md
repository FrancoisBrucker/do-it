---
layout: layout/mon.njk

title: "TailwindCSS et le langage HTML au service du Front Web"
authors:
  - Schultz Mathis

date: 2023-09-25

tags: 
  - "temps 1"

résumé: "Premier pas dans le langage HTML/tailwindcss"
---

<a href="https://tailwindcss.com/" target="_blank">
        <img src="logo_tailwindcss.png" rounded-full alt="Click me" width="200" height="150">
    </a>

> Le front web au travers d'une introduction à [TailwindCSS](https://tailwindcss.com/).

<h2 id="toc"> Table des matières </h2>

- [Table des matières](#toc)
- [Introduction](#h1)
  - [Qu'est ce que le langage HTML ?](#h1-1)
  - [Qu'est ce que TailwindCSS ?](#h1-2)
- [Outils complémentaires](#h2)
- [Liens utiles](#liens)

<h2 id="h1"> Introduction </h2>

Le but de ce MON est de découvrir le front web au travers d'une introduction à TailwindCSS.

<h3 id="h1-1"> Qu'est ce que le language HTML ? </h3>

Le langage HTML (HyperText Markup Language) est un langage utilisé pour créer et structurer le contenu d'une page web pour la rendre lisible et agréable pour le lecteur.

<h3 id="h1-2"> Qu'est ce que TailwindCSS ? </h3>

L'idée de TailwindCSS est de proposer des classes faciles à utiliser et extrêmement modifiable, afin d'avoir la personnalisation la plus complète possible de la page web avec des fonctions faciles d'utilisation.

```html
<body class="min-h-screen bg-slate-50 dark:bg-black dark:text-white">
    <header class="bg-teal-700 text-white sticky top-0 z-10">
        <section class="max-w-4xl mx-auto p-4 flex justify-between items-center">
            <h1 class="text-3xl font-medium"></h1>
                TailwindCSS
        </section>
</body>
```

Ce paragraphe permet de créer un titre avec des personnalisations :

- le fond va être "bg-teal-700" (une sorte de vert)
- "text-white" écris en blanc
- "dark:bg-black" défini la couleur du background en dark mode, cela permet donc de créer facilement son site web dans les deux coloris.
- "items-center" permet de centrer les objets

L'intérêt est donc d'avoir des abréviations intuitives qui permettent de personnaliser efficacement

<h2 id="h2"> Outils complémentaires </h2>

En vue d'utiliser TailwindCSS et plus généralement pour écrire du code HTML, il est nécessaire d'avoir un environnement de travail qui soit propre. Ainsi, les extensions suivantes permettent de faciliter le développement :

- [Tailwind CSS IntelliSense](https://code.visualstudio.com/docs/editor/intellisense)
, le but de cette extension est de faciliter l'écriture du code tailwind css, en effet elle permet la complétion automatique de syntaxe et surligne les erreurs.

<img src="tailwind.png">

- [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)
, le but de cette extension est d'avoir votre page web toujours ouverte et toujours à jour ! Cela permet de ne plus effectuer de "npm run serve" et de ne plus avoir de temps d'attente entre la modification et le rendu graphique.

<img src="live_server.png">

- [Inline Fold](https://marketplace.visualstudio.com/items?itemName=moalamri.inline-fold)
, le but de cette extension est de rendre le code lisible, lorsque l'on écrit en html et en Tailwind, les personnalisations viennent encombrer notre écran, cette extension va masquer la partie personnalisation de chaque Class en vue de ne garder que la structure de la page. Lorsque l'on souhaite modifier la personnalisation d'une classe, il nous suffit de cliquer sur les trois points de suspension.

<img src="inline_fold.png">

Voici un exemple du code précédent en utilisant Inline Fold, il permet doc de masquer toutes les personnalisations tant qu'on ne clique pas sur les points de suspensions :

<img src="inline_exemple.png">

<h2 id="liens"> Liens utiles </h2>

Voici différents lien permettant de se former à l'utilisation de TailwindCSS :

### Un tutoriel de Dave Gray

<a href="//www.youtube.com/watch?v=lCxcTsOHrjo" target="_blank">
        <img src="video.png" rounded-full alt="Click me" width="200" height="150">
    </a>

Ce tutoriel permet d'installer proprement un environnement de travail pour développer une page Web en utilisant TailwindCSS, il utilise ensuite les différents outils qu'il présente pour construire une petite page internet.

### La page web officielle de TailwindCSS

<a href="https://tailwindcss.com/" target="_blank">
        <img src="logo_tailwindcss.png" rounded-full alt="Click me" width="200" height="150">
    </a>

Cette page met en évidence les différentes applications et intérêts de TailwindCSS

### Le discord de TailwindCSS

En cas de problème, ou pour élargir ses connaissances sur le sujet, [le discord de TailwindCSS](https://discord.gg/7NF8GNe) peut être d'une grande aide pour approfondir son sujet.
