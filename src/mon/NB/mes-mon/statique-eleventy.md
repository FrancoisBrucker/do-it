---
layout: layout/post.njk

title: "Créer un site web statique avec 11ty"
authors:
  - Nicolas BERT

---

<!-- début résumé -->
Site web statique avec 11ty (Temps 1)
<!-- fin résumé -->

Dans ce cours nous allons apprendre à créer un site web statique de zéro en utilisant [Eleventy](https://www.11ty.dev/).

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
    ├── package.json

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

### 1.5 Mettre en place le serveur web en local

Afin qu'Eleventy détecte les changements en permanence, nous allons lancer la commande `npx @11ty/eleventy --serve`.
Rendez-vous ensuite sur [http://localhost:8080](http://localhost:8080) et vous devriez voir le contenu de votre fichier compilé !

{% info %}
Actuellement, il est nécessaire de rafraîchir la page web pour voir les modifications, c'est normal ! Ce problème sera réglé plus tard :)
{% endinfo %}

{% faire "**Mise en place d'un alias pour la compilation**" %}
Cette commande étant un peu difficile à se souvenir, nous allons créer un alias à cette commande dans le fichier `package.json`. Pour cela, il suffit d'ajouter la ligne suivante :

```json
{
  ...
  "srcipts": {
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
    <title>{{ title }}</title>
  </head>
  <body>
    Bienvenue à tous sur mon site créer avec Eleventy !
    {{ content | safe }}
  </body>
</html>
```

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
Il est possible d'enchainer les templates les uns dans les autres et d'avoir ainsi plusieurs niveau de templating !
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