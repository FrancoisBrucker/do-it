---
layout: layout/post.njk

title: "Contribuer au site"
authors:
  - François Brucker

tags: ['ct']
---

<!-- début résumé -->

Comment contribuer au site do-it.

<!-- fin résumé -->

Le site do-it est un site constitué de fichiers écrit au format [Markdown](https://francoisbrucker.github.io/cours_informatique/tutoriels/format-markdown/). Y contribuer est très simple, il suffit de suivre ce document.

## architecture d'un post

Un post do-it est un dossier à mettre dans le code source du site. Par exemple, cette page est le dossier <https://github.com/FrancoisBrucker/do-it/tree/main/src/ct/contribuer-au-site/francois-brucker>

Ce dossier contient :

* un fichier `index.md` qui est le texte de votre post
* les images ou autres fichier de ressources (code source, données, etc) que vous voulez montrer.

Il y a 3 endroits où placer ses contributions :

* dans le dossier `ct`{.fichier}
* dans le dossier `pok`{.fichier}
* dans le dossier `mon`{.fichier}

### post ct

Votre dossier de post doit s'appeler comme l'intitulé du cours, en remplaçant les espace par des `-`.

Par exemple ce post s'appelle `contribuer-au-site`{.fichier} et est rangé dans le dossier `ct`{.fichier} :

```shell
src
└── ct
    ├── contribuer-au-site
    │   └── index.md
    └── index.njk
```

### post pok

Comme plusieurs groupes de personnes peuvent faire le même pok, on ajoute une indirection. Votre dossier de post doit s'appeler des initiales des personnes constituant le groupe (séparés par des `-`) et être placé dans le dossier du pok correspondant. Par exemple si j'avais avec Geo fait le pok "un site chez moi", le post aurait été nommé `FB-GD`{.fichier}, et aurait été de cette forme :

```shell
src
└── pok
    ├── un-site-chez-moi
    │   ├── FB-GD
    │   │   ├── index.njk
    │   │   └── sources.zip
    │   ├── RS
    │   └── index.njk 
    └── index.njk
```

Il aurait en effet contenu, en plus du fichier `index.md`{.fichier} les sources du site compressées au format `zip`.

### post mon

De la même manière que le poste pok.

## le fichier `index.md`{.fichier}

Il est constitué de trois parties :

* l'entête
* son résumé
* le corps du texte en markdown

### exemple

Ce fichier est visible à [cette adresse](https://raw.githubusercontent.com/FrancoisBrucker/do-it/main/src/ct/contribuer-au-site/index.md).

### entête

Ce sont les premières lignes du site. Elles contiennent les méta-données du post :

* le layout html à utiliser
* le titre du post
* le ou les auteurs (il suffit d'ajouter une ligne)
* les tags du site. Doit au minimum contenir `ct`{.fichier} si vous faite un ct, `pok`{.fichier} si vous faites un pok et `mon`{.fichier} si vous faites un mon.

```text
---
layout: layout/post.njk

title: "Contribuer au site"
authors:
  - François Brucker

tags: ['ct']
---
```

### résumé

Juste en dessous de l'entête.

```shell
<!-- début résumé -->

Comment contribuer au site do-it.

<!-- fin résumé -->
```

### corps du texte

Le reste du post, écrit en markdown.

### les ressources

Placez les ressources dans le même dossier que votre post. Vos liens auront alors la forme suivante :

* `[ressource à télécharger](./sources.zip)`{.fichier}
* `![image à voir](./mon-image.png)`{.fichier}

## Possibilités étendues en markdown



