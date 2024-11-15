---
layout: layout/pok.njk

title: "Refonte du site de Do_It : Eleventy"
authors:
  - "Arthur Louradou"

date: 2024-10-16

tags: 
  - "temps 1"
  - "pok"
  - "web"
  - "statique"

résumé: Ce POK consistera en la refonte du site de Do_It avec les dernières technologies web statiques et en analysant le besoin des utilisateurs.
---

## Mise à jour du site de Do_It

### Besoin, problématique

- A priori, problèmes de lenteur liés à pagesearch (le menu de recherche) ou au style (css et postcss)
- Design améliorable sur certains aspects
- Manque de centralisation d’informations (Drive + Site pas forcément pratique)
- Séparation des années

### Solutions envisagées

1. Mise à jour majeure de 11ty (3.0 sortis le 2 octobre - voir le changelog)
2. Rechercher les concurrents à 11ty
3. Fix de performance sur pagesearch et sur la compilation des styles
4. Faire des sous repos indépendants chaque année, mais qui peuvent se combiner (chercher comment)
5. Séparer data et statique

### Alternatives

Une analyse de l’existant nous permettra de faire des choix techniques. On comparera la popularité des différents projets concurrents à 11ty (utilisé actuellement) à l’aide du nombre de personnes suivant le projet sur GitHub et représenté avec des étoiles ⭐.

[https://jekyllrb.com](https://jekyllrb.com/) (JS) 49000 ⭐ [GitHub](https://github.com/jekyll/jekyll)

[https://www.11ty.dev](https://www.11ty.dev/) (JS) 17000 ⭐ [GitHub](https://github.com/11ty/eleventy/)

[https://gohugo.io](https://gohugo.io/) (Go) 75000 ⭐ [GitHub](https://github.com/gohugoio/hugo)

[https://getpelican.com](https://getpelican.com/) (Python) 12500 ⭐ [GitHub](https://github.com/getpelican/pelican)

[https://www.getzola.org](https://www.getzola.org/) (JS) 13600 ⭐ [GitHub](https://github.com/getzola/zola)

Comparaison des alternatives :
https://www.abdullahyahya.com/2022/06/generate-a-static-website-with-11ty-eleventy/

### Migration

Pour poursuivre ce travail, j’ai essayé de compiler le site actuel avec GoHugo, l’outil qui semblait le plus prometteur pour construire un site statique. Malheureusement, les fichiers de templating de Eleventy rendent l’opération plus compliquée que de copier un répertoire.

Un inconvénient majeur de GoHugo réside dans le langage de programmation utilisé (Go), qui implique de faire changer à tous les utilisateurs leur environnement d’exécution.

On laissera donc GoHugo de côté pour le moment.

### Réunion avec F. Brucker

Pour continuer, nous avons pu nous entretenir brièvement pour cibler le besoin précis. À l’issue de cette réunion, je note quelques points importants :

- Fork le projet actuel en 11ty 3.0 (Un fork est une branche du projet git que je peux utiliser avec toutes les permissions sur mon propre repository. Voir le MON à suivre sur l’Open Source pour en savoir plus.)
- Deux sites : un pour les ressources communes (CS, contribuer au site, etc.) contenant en plus les archives des autres années et un autre pour la promo courante
- Ou bien un site générique et un petit site par promo, séparés en projets distincts
- Étudier la question des permaliens pour que les redirections ne se brisent pas lors de cette migration

## Améliorer les performances

### Correction du site actuel

Nous l’avons exprimé au départ, deux modules sont suspectés de provoquer des lenteurs dans la compilation du site actuel : soit **pagesearch**, soit le **style**. Pour isoler les causes, nous allons mener des tests de performances en désactivant ces paramètres dans le fichier de configuration `.eleventy.js`. Après la désactivation des modules, on constate que pagesearch a finalement un impact mineur. Nous allons donc enquêter du côté des styles, et un détail retient mon attention : le compilateur postcss copie énormément de fichiers en amont. Changeons la configuration de tailwind pour remédier à ce problème : 

```jsx
module.exports = {
    content: [
        "./src/assets/stylesheets/*.{html,js,njk}",
        "./src/*.{html,js,njk}",
        "./src/_includes/**/*.{html,js,njk}",
        "./src/cs/**/*.{html,js,njk}",
        "./src/mon/**/*.{html,js,njk}",
        "./src/pok/**/*.{html,js,njk}",
        "./config/markdown/shortcodes/quotes/!(index).js"
    ],
    theme: {
      extend: {},
    },
    plugins: [
      require('@tailwindcss/typography'),
    ],
    
  }
```

En réduisant ainsi la quantité de fichiers à compiler avec tailwind, on essaye de limiter les chargements en mémoire impliqués par la compilation.

#### Tests de performance

https://v2.11ty.dev/docs/debugging/

https://v2.11ty.dev/docs/debug-performance/

Avec le site actuel, en tapant ces commande :

```bash
$ DEBUG=Eleventy:Benchmark* npx @11ty/eleventy
$ grep -v " 0%" benchmark_1.log
```

```
Eleventy:Benchmark Benchmark  14306ms  25%   704× (Configuration) "eleventyNavigationBreadcrumb" Nunjucks Filter +0ms
Eleventy:Benchmark Benchmark  54014ms  95%     3× (Aggregate) Searching the file system (passthrough) +0ms
Eleventy:Benchmark Benchmark    313ms   1%  3668× (Aggregate) Template Compile +0ms
Eleventy:Benchmark Benchmark  38261ms  68%  3664× (Aggregate) Render +0ms
Eleventy:Benchmark Benchmark  54328ms  96%  2776× (Aggregate) Passthrough Copy File +0ms
Eleventy:Benchmark Benchmark  38082ms  67%     1× (Aggregate) > Render > ./src/assets/stylesheets/main.css +0ms
Eleventy:Benchmark Benchmark  14448ms  26%   778× (Aggregate) Template Write +0ms
[11ty] Copied 2776 files / Wrote 778 files in 56.69 seconds (72.9ms each, v2.0.1)
```

En appliquant la correction sur `tailwind.config.js` :

```
Eleventy:Benchmark Benchmark  14581ms  74%   704× (Configuration) "eleventyNavigationBreadcrumb" Nunjucks Filter +0ms
Eleventy:Benchmark Benchmark  16633ms  84%     3× (Aggregate) Searching the file system (passthrough) +1ms
Eleventy:Benchmark Benchmark    116ms   1%   787× (Aggregate) Template Read +0ms
Eleventy:Benchmark Benchmark    411ms   2%  3668× (Aggregate) Template Compile +0ms
Eleventy:Benchmark Benchmark    395ms   2%  3664× (Aggregate) Render +0ms
Eleventy:Benchmark Benchmark    209ms   1%     1× (Aggregate) > Compile > ./src/assets/stylesheets/main.css +0ms
Eleventy:Benchmark Benchmark    209ms   1%     1× (Aggregate) Engine (css) Init +0ms
Eleventy:Benchmark Benchmark  16866ms  85%  2776× (Aggregate) Passthrough Copy File +0ms
Eleventy:Benchmark Benchmark    228ms   1%     1× (Aggregate) > Render > ./src/assets/stylesheets/main.css +0ms
Eleventy:Benchmark Benchmark  14710ms  74%   778× (Aggregate) Template Write +0ms
[11ty] Copied 2776 files / Wrote 778 files in 19.85 seconds (25.5ms each, v2.0.1)
```

Réduction de 54 à 17 secondes sur le passe plat de fichiers et la compilation tailwind.

Avec la désactivation de pagesearch :

```
Eleventy:Benchmark Benchmark  14681ms  85%   704× (Configuration) "eleventyNavigationBreadcrumb" Nunjucks Filter +0ms
Eleventy:Benchmark Benchmark  16626ms  96%     3× (Aggregate) Searching the file system (passthrough) +0ms
Eleventy:Benchmark Benchmark    110ms   1%   787× (Aggregate) Template Read +0ms
Eleventy:Benchmark Benchmark    379ms   2%  3668× (Aggregate) Template Compile +0ms
Eleventy:Benchmark Benchmark    346ms   2%  3664× (Aggregate) Render +0ms
Eleventy:Benchmark Benchmark    183ms   1%     1× (Aggregate) > Compile > ./src/assets/stylesheets/main.css +0ms
Eleventy:Benchmark Benchmark    183ms   1%     1× (Aggregate) Engine (css) Init +0ms
Eleventy:Benchmark Benchmark  16740ms  97%  2776× (Aggregate) Passthrough Copy File +0ms
Eleventy:Benchmark Benchmark    204ms   1%     1× (Aggregate) > Render > ./src/assets/stylesheets/main.css +0ms
Eleventy:Benchmark Benchmark  14810ms  85%   778× (Aggregate) Template Write +0ms
[11ty] Copied 2776 files / Wrote 778 files in 17.38 seconds (22.3ms each, v2.0.1)
```

Pas de gain significatif pour cette modification. Laissons pagesearch de côté comme prévu.

## Mise à jour majeure vers Eleventy 3.0

## Réalisation

La mise à jour vers la version 3.0 de Eleventy (sortie le 02/10/2024) implique la remise à zéro de **tous les fichiers de configuration**. Cela inclus le fichier  `.eleventy.js` mais aussi ses diverses dépendances pour les rendre compatibles avec une version plus moderne de javascript : ESM scripts. Les plugins utilisés par le site ont donc été désactivés dans un premier temps pour compiler le tout étape par étape.

❓ **ESM Script**, par opposition à CommonJS, est un ensemble de méthodes récentes sur JavaScript améliorant la façon dont sont gérés les modules. Concrètement, cela impacte la manière dont on importe les fichiers : pour organiser et réutiliser du code via `import` et `export`.

### Le style : Tailwind

La plus grosse difficulté résida dans la mise à jour de Tailwindcss, une bibliothèque CSS permettant de styliser rapidement et efficacement les éléments HTML. La mise à jour vers la version 3.0 d'Eleventy a nécessité une reconfiguration complète de l'intégration de Tailwind dans le projet. Cela a impliqué la modification des fichiers de configuration de Tailwind et l'ajustement des imports dans les fichiers de style principaux.

## La suite…

- Corriger les bugs qui surviennent notamment avec les balises de résumés dans les projets
- Initialiser un nouveau git avec des sous modules
- Voir si on peut rendre autonome en local un sous projet qui ne comprend pas le site complet, mais qui compile avec un projet “hôte”