---
layout: layout/mon.njk

title: "Créer un site web statique avec 11ty"
authors:
  - Nicolas BERT

date: 2022-10-07

tags:
  - 'temps 1'
  - 'eleventy'
  - 'statique'
  - 'markdown'
  - 'web'
---

<!-- début résumé -->
Site web statique avec 11ty (Temps 1)
<!-- fin résumé -->

Dans ce cours nous allons apprendre à créer un site web statique de zéro en utilisant [Eleventy](https://www.11ty.dev/).

Eleventy est un générateur de site statique, il va, ici, transformer le langage markdown en langage HTML. Il utilise un langage de templating qui s'appelle Nunjucks.

{% faire %}
Nous allons avoir besoin de Node.js, si vous ne l'avez pas vous pouvez le télécharger sur le site officiel de [Node.js](https://nodejs.org/) (version > 12).
{% endfaire %}

## 1. Création du projet

### 1.1 Créer le répertoire du projet

Pour commencer, nous allons créer un dossier `mon-site` . Pour cela, ouvrir le terminal et taper les commandes suivantes :

```bash
mkdir mon-site
cd mon-site
```

*Vous pouvez ensuite ouvrir ce dossier dans votre éditeur de code favori. Pour ma part j'utilise VSCode, il me suffit de taper `code .` afin d'ouvrir le dossier avec VSCode.*

### 1.2 Installer le package `eleventy`

Afin d'installer `eleventy` dans notre projet, nous allons utiliser `npm` (Node Package Manager).
Commençons par initialiser npm dans notre projet puis installer `eleventy`. Pour cela, exécuter les deux commandes suivantes :

```bash
npm init -y
npm install -D @11ty/eleventy
```

Une fois ces deux commandes exécutées vous devriez avoir l'arborescence suivante :

```bash
mon-site
    ├── node_modules
    ├── package-lock.json
    └── package.json

```

Vous devriez également voir `"@11ty/eleventy": {version}` dans la partie `"dependencies` du fichier `.package.json`.

### 1.3 Lancer le projet

Afin de lancer le projet, il faut demander à `eleventy` de compiler les fichiers du projet. Pour cela on utilisera la commande :

```bash
npx @11ty/eleventy
```

Eleventy va alors vous dire qu'il a compilé 0 fichier et c'est normal, on n'a rien écrit encore ! :D

{% attention %}
Si jamais la compilation indique des erreurs, recommencez depuis le début.
{% endattention %}

### 1.4 Première page

Pour montrer que la compilation fonctionne, il serait bien d'avoir un fichier à compiler ! C'est parti ! Créons un fichier `index.md`.

```html
# Une belle page !

Regarder ce mot est en **gras** et celui là est en *italique* !
```

Relançons la commande `npx @11ty/eleventy`. On voit alors que notre fichier `index.md` a été compilé en un fichier `index.html` dans le dossier `_site`. Voilà son contenu :

```html
<h1>Une belle page !</h1>
<p>Regarder ce mot est en <strong>gras</strong> et celui là est en <em>italique</em> !</p>
```

Si vous connaissez un minimum le langage HTML vous voyez que la compilation ne fait rien de délirant et que c'est logique, c'est bien !

### 1.5 Mettre en place le serveur web en local

Afin d'éviter d'avoir à relancer la compilation à chaque fois, nous allons mettre en place un serveur web local pour qu'Eleventy détecte les changements en permanence, nous allons le lancer la commande `npx @11ty/eleventy --serve`.
Rendez-vous ensuite sur [http://localhost:8080](http://localhost:8080) et vous devriez voir le contenu de votre fichier compilé !

{% info %}
Actuellement, il est nécessaire de rafraîchir la page web pour voir les modifications, c'est normal ! Ce problème sera réglé plus tard :)
{% endinfo %}

{% faire "**Mise en place d'un alias pour la compilation**" %}
Cette commande étant un peu difficile à se souvenir, nous allons créer un alias à cette commande dans le fichier `package.json`. Pour cela, il suffit d'ajouter la ligne suivante :

```json
{
  ...
  "scripts": {
    ... 
    "test": "echo \"Error: no test specified\" && exit 1",
    "serve": "npx @11ty/eleventy --serve"
    ...
  }
  ...
}
```

La ligne de `"test"` se trouve déjà là, cependant n'oubliez pas d'ajouter la virgule à la fin de cette ligne !

{% endfaire %}

## 2. Mise en place des templates & configuration

### 2.1 Création d'un template

Les templates sont comme leur nom l'indique des templates qui pourront être utilisé par d'autres pages. Les templates doivent se trouver dans le dossier `_includes/`. Créons notre premier template que nous appellerons `base.njk`

```html
---
title: Mon super site statique
---

<!doctype html>
<html lang="fr">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{ title }</title>
  </head>
  <body>
    Bienvenue à tous sur mon site créer avec Eleventy !
    { content | safe }
  </body>
</html>
```

{% attention %}
**ATTENTION**, ici il faut remplacer les simples accolades "{ }" par des doubles accolades afin que le contenu soit interprété comme il faut. Je ne peux pas les afficher ici puisqu'elles sont interprétées directement par le compilateur.
{% endattention %}

Ici, dans la balise `content` sera ajouté le contenu des "enfants", c'est-à-dire les pages qui vont utiliser ce template.
Afin que la page que nous venons de créer utiliser ce template il faut rajouter les quelques lignes suivantes en en-tête du fichier `index.md`.

```markdown
---
layout: base.njk
title: Ma première page
---

# Une belle page !

Regarder ce mot est en **gras** et celui là est en *italique* !

```

Dans cette en-tête on indique à Eleventy qu'il doit utiliser le template base.njk et qu'il doit afficher "Ma première page" dans l'emplacement "title" du template. Si cette valeur de title n'est pas spécifié dans la page, elle vaudra par défaut celle du template, ici "Mon super site statique".

{% info %}
Il est possible d’enchaîner les templates les uns dans les autres et d'avoir ainsi plusieurs niveau de templating !
{% endinfo %}

### 2.2 configuration

Pour gagner en lisibilité, nous allons mettre tous nos fichiers à compiler dans un dossier `src` et les fichiers compilés seront dans le dossier `dist`. Pour cela nous allons ajouter à la racine du projet le fichier de configuration appelé `.eleventy.js`. (Attention, il y a un **.** devant !) Voici la configuration a insérer dans le fichier :

```js
module.exports = function (eleventyConfig) {
    return {
        dir: {
            input: "src",
            output: "dist"
        }
    }
}
```

Il faut cependant déplacer le dossier de layout dans le dossier `src`. On a alors l'arborescence suivante :

```bash
node_modules
dist
├── index.html
src
├── _includes
|  ├── base.njk
└── index.md
.eleventy.js
package.json
package-lock.json
```

Voilà à ce niveau du tutoriel vous avez de quoi créer votre site statique !

{% prerequis %}
Pour davantage d'informations, rendez-vous sur la [documentation d'Eleventy](https://www.11ty.dev/).
{% endprerequis%}

## 3. Installation de TailwindCSS

{% details "A vos risques et périls" %}

Afin de faciliter la création du style, nous allons utiliser [TailwindCSS](https://tailwindcss.com/) dans notre projet. TailwindCSS est un framework CSS basé sur le principe de classes utilitaires. Cela rend la phase de développement beaucoup plus simple.

Commençons par installer `tailwindcss` et `concurrently` (cela nous servira plus tard):

```bash
npm install -D tailwindcss concurrently
npx tailwindcss init
```

La deuxième commande permet de créer automatiquement un fichier de configuration pour TailwindCSS. Nous allons le modifier de cette façon :

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./dist/**/*.{html,js,njk,md}"],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

Ainsi, on indique à Tailwind que les fichiers contenant les classes utilitaires se trouvent dans le dossier `dist`.

Commençons par créer un fichier `tailwind.css` dans `src/styles/`, puis nous allons importer le style de base de TailwindCSS.

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Nous devons ensuite indiquer à notre template `base.njk` d'utiliser le style de Tailwind. Pour cela on rajoute dans la balise `head` :

```html
<link href="/styles/index.css" rel="stylesheet" />
```

{% attention %}
Le chemin indiqué ici fait référence au fichier CSS compilé. Ce chemin est défini dans la commande `tailwind`, dans le `package.json` que nous allons modifier ci-après.
{% endattention %}

Pour que le commande de lancement du serveur compile aussi le style de Tailwind, nous allons devoir effectuer des modifications dans le fichier `package.json`.

```json
{
  ...
  scripts": {
    "serve": "npx @11ty/eleventy --serve",
    "tailwind": "npx tailwindcss -i ./src/styles/tailwind.css -o ./dist/styles/index.css --watch",
    "start": "concurrently \"npm run tailwind\" \"npm run serve\""
  },
  ...
}
```

La commande `serve` (se lançant avec `npm run serve`) permet de lancer la compilation des fichiers avec Eleventy, et la commande `tailwind` (se lançant avec `npm run tailwind`) permet de compiler le style de Tailwind.

Pour exécuter ses deux commandes en parallèle, on lance `npm run start`.
*(Cette commande utilise `concurrently`, une bilbiothèque permettant de lancer des scripts en parallèle.)*

Modifions désormais notre `base.njk` pour y ajouter des classes Tailwind !

```markdown
---
title: Mon super site statique
---

<!doctype html>
<html lang="fr">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Créer un site web statique avec 11ty</title>
  </head>
  <body class="text-3xl text-blue-600">
    Bienvenue à tous sur mon site créer avec Eleventy !
    {{ content | safe }}
  </body>
</html>
```

Il ne reste plus qu'à lancer la commande npm run start, les fichiers ainsi que le style vont être compilés et tindiinnn !

{% attention %}
J'ai découvert cela durant l'élaboration de ce MON. Quand vous appliquez des classes Tailwind sur un template pas de problème. En revanche si vous appliquer ces classes à l'intérieur d'une de vos pages dans un fichier markdown, le style de tailwind prendre le dessus sur le style du Markdown.

**Exemple** : le code ci dessous, une fois compilé n'affiche que du vert et le mot `amis` n'est pas mis en gras et les étoiles sont affichées. ⟶ **Le style du Markdown n'est pas pris en compte**.

```markdown
<div class="text-green-600">
  Bonjour les **amis** !
</div>
```

⟶ Ainsi je vous conseille de ne pas utiliser de classes Tailwind dans vos pages mais seulement dans vos templates.
{% endattention %}

{% enddetails %}

## 4. Un exemple + des bidouilles

J'ai crée un petit site pour présenter les formations du GInfo en suivant le tuto ci dessus. Voilà le lien du repo : [https://github.com/nbert71/eleventy-cours](https://github.com/nbert71/eleventy-cours)
Vous pouvez le consulter à l'adresse suivante : [http://nbert.perso.ec-m.fr/eleventy](http://nbert.perso.ec-m.fr/eleventy)

J'ai installé [Bootstrap](https://getbootstrap.com/docs/5.2/getting-started/introduction/) (via le CDN pour aller plus vite) pour styliser rapidement mes pages.

{% info %}
J'ai créé plusieurs pages. Il faut savoir que si l'on n'utilise pas de bilbiothèque spécifique pour gérer la navigation, le rounting du site suivra l'arbrescence des fichiers de votre projets. Exemple : si vous mettez la page `linux` dans un dossier `formations`, celle-ci sera accessible sur `http://monsite.com/formations/linux`
{% endinfo %}

Vous pouvez voir différentes pages ainsi qu'une page regroupant toutes les formations. Vous avez la possibilité de filtrer suivant un tag pour n'afficher que les formations qui possèdent ce tag. Ensuite en cliquant sur une formation vous avez accès au détail de la formation.
