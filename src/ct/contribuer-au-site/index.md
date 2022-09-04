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

Le reste du post, écrit en markdown. Le titre est déjà mis, vos différentes parties sont donc de niveau `##`{.language-}

### les ressources

Placez les ressources dans le même dossier que votre post. Vos liens auront alors la forme suivante :

* `[ressource à télécharger](./sources.zip)`{.fichier}
* `![image à voir](./mon-image.png)`{.fichier}

## Possibilités étendues en markdown

Plusieurs balises spéciales ont été ajoutées pour vous aider à écrire des parties spécifiques de votre post.

### liens

Il existe plusieurs façon d'écrire les liens. On suppose que l'on a l'architecture suivante :


```shell
src
└── pok
    ├── un-site-chez-moi
    │   ├── FB-GD
    │   │   ├── index.njk
    │   │   └── sources.zip
    │   ├── RS
    │   └── index.njk 
    ├── index.njk
    └── ct
       ├── contribuer-au-site
       │   └── index.md
       └── index.njk
```

Et que l'on veuille, depuis le post `FB-GD`{.fichier}, aller vers le post `contribuer-au-site`{.fichier}.

Il y a deux façon de faire :

* lien absolu. Depuis la racine du site (qui est `src`{.fichier}) `[lien]({{ "/ct/contribuer-au-site" | url }})`{.language}
* lien relatif. Depuis là on je suis : `[lien](../../../ct/contribuer-au-site)`{.language} (je remonte 3 dossier avant de redescendre dans l'arborescence)

### texte spécial

En plus des possibilités markdown, on ajoute deux distinction de texte :

* fichier : `nom-fichier`{.fichier} que l'on écrit : \`nom-fichier\`\{.fichier\}
* code : `print("coucou !")`{.language-} que l'on écrit : \`print("coucou !")\`\{.language-\}

### shortcodes

Les *shortcodes* sont des aides markdown. Elles permettent de mettre en valeur un paragraphe. elles sont toutes de la même forme :

\{\% nom_shortcode "titre de la shortcode" \%\}

le contenu de la shortcode

\{\% endnom_shortcode \%\}

{% note %}
Le titre de la shortcode est toujours optionnel. Mais s'il est présent il est **obligatoirement** entre " ".
{% endnote %}

Regardez [le code source de cette page](https://raw.githubusercontent.com/FrancoisBrucker/do-it/main/src/ct/contribuer-au-site/index.md) pour voir comment sont écrit ces différentes façon de mettre du texte en relief.

#### Une mise en garde

{% attention "**faisez** attention" %}
Une *grosse* mise en garde.
{% endattention %}

#### Une note

{% note %}
Une note à retenir.
{% endnote %}

#### Une information

{% info %}
Un truc marrant ou une information utile, mais pas indispensable.
{% endinfo %}

#### A faire

{% faire %}
Quelque-chose à faire.
{% endfaire %}

#### Partie cachée

{% details "spoiler" %}
Quelque chose de caché. Que l'on peut *écrire* en `Markdown`
{% enddetails %}

#### Exercice avec son corrigé

{% exercice %}
Un exercice à faire.
{% endexercice %}
{% details "corrigé" %}
Le corrigé de l'exercice.
{% enddetails %}

### Tables

On utilise les possibilités de [multimarkdown](https://fletcher.github.io/MultiMarkdown-6/syntax/tables.html)

#### Tables de base

| titre colonne 1  | titre colonne 2 |
| ---------------- | --------------- |
| Content Cell     | Content Cell  |
| Content Cell     | Content Cell  |

#### Tables sans titre

| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |

#### Tables multi-colonne

| ------------- | ------------- |
|     Content Cell             ||
| Content Cell  | Content Cell  |

#### Tables multi-ligne

| ------------- | ------------- |
| Content Cell  | Content Cell  |
| ^^            | Content Cell  |

#### plusieurs ligne dans une cellule

| ------------- | ------------- |
| Content Cell  | * Content Cell  | \
| Content Cell  | * Content Cell  |
| Content Cell  | Content Cell  |

#### Alignement horizontal

| :- | :-: | -: |
| Content Cell  | Content Cell  | Content Cell |
| Content Cell  | Content Cell  |Content Cell  |
| Content Cell  | Content Cell  |Content Cell  |

#### Alignement vertical

On ajoute un style, mais il ne faut pas que ce soit la dernière colonne.

| ------------- | ------------- |
| Content Cell  {style="vertical-align:middle"}| Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eleifend, orci nec pharetra lacinia, lacus dolor euismod ipsum, quis pulvinar ipsum urna non purus. Cras accumsan ex ligula, eu pellentesque mauris congue ac. Integer venenatis elementum est ac imperdiet. Etiam lectus purus, imperdiet gravida commodo non, faucibus at metus. Maecenas elit nibh, venenatis a efficitur vitae, placerat vitae nulla. Fusce volutpat nisl sem, vel iaculis risus sagittis vel. Nunc felis tellus, sollicitudin eu felis vel, cursus egestas arcu. Sed laoreet ex a nisl vestibulum, id placerat leo pellentesque. Praesent nec ultrices purus, ut congue elit. Pellentesque in diam ultrices purus volutpat lacinia. |
| Content Cell  | Content Cell  |

Pour la dernière colonne, il faut ajouter une colonne vide :

| ------------- | ------------- | - |
| Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eleifend, orci nec pharetra lacinia, lacus dolor euismod ipsum, quis pulvinar ipsum urna non purus. Cras accumsan ex ligula, eu pellentesque mauris congue ac. Integer venenatis elementum est ac imperdiet. Etiam lectus purus, imperdiet gravida commodo non, faucibus at metus. Maecenas elit nibh, venenatis a efficitur vitae, placerat vitae nulla. Fusce volutpat nisl sem, vel iaculis risus sagittis vel. Nunc felis tellus, sollicitudin eu felis vel, cursus egestas arcu. Sed laoreet ex a nisl vestibulum, id placerat leo pellentesque. Praesent nec ultrices purus, ut congue elit. Pellentesque in diam ultrices purus volutpat lacinia. | Content Cell  {style="vertical-align:middle"}| |
| Content Cell  | Content Cell  | |
