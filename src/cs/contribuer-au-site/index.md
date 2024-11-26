---
layout: layout/post.njk

title: "Contribuer au site"
authors:
  - François Brucker

tags: ["cs"]
---

Le site <span style="font-family: Consolas, sans-serif;">Do_<span style="color: #4a86e8">It</span></span> est un site constitué de fichiers écrit au format [Markdown](https://francoisbrucker.github.io/cours_informatique/tutoriels/format-markdown/). Y contribuer est très simple, il suffit de suivre ce document.

## Architecture d'un post

Un post <span style="font-family: Consolas, sans-serif;">Do_<span style="color: #4a86e8">It</span></span> est un dossier à mettre dans le code source du site. Par exemple, cette page est le dossier <https://github.com/FrancoisBrucker/do-it/tree/main/src/cs/contribuer-au-site>

Ce dossier contient :

- un fichier `index.md` qui est le texte de votre post
- les images ou autres fichier de ressources (code source, données, etc) que vous voulez montrer.

Il y a 3 endroits où placer ses contributions :

- dans le dossier `cs`{.fichier}
- dans le dossier `pok`{.fichier}
- dans le dossier `mon`{.fichier}

### Post cs

Votre dossier de post doit s'appeler comme l'intitulé du cours, en remplaçant les espace par des `-`.

Par exemple ce post s'appelle `contribuer-au-site`{.fichier} et est rangé dans le dossier `cs`{.fichier} :

```
src
└── cs
    ├── contribuer-au-site
    │   └── index.md
    └── index.njk
```

### Post pok

Comme plusieurs groupes de personnes peuvent faire le même pok, on ajoute une indirection. Votre dossier de post doit s'appeler des initiales des personnes constituant le groupe (séparés par des `-`) et être placé dans le dossier du pok correspondant. Par exemple si j'avais avec Geo fait le pok "un site chez moi", le post aurait été nommé `FB-GD`{.fichier}, et aurait été de cette forme :

```
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

### Post mon

De la même manière que le poste pok.

## Le fichier `index.md`{.fichier}

Il est constitué de trois parties :

- l'entête
- son résumé
- le corps du texte en markdown

### Exemple

Ce fichier est visible à [cette adresse](https://raw.githubusercontent.com/FrancoisBrucker/do-it/main/src/cs/contribuer-au-site/index.md).

### Entête

Ce sont les premières lignes du site. Elles contiennent les méta-données du post :

- le layout html à utiliser
- le titre du post
- le ou les auteurs (il suffit d'ajouter une ligne)
- les tags du site. Doit au minimum contenir `cs`{.fichier} si vous faite un cs, `pok`{.fichier} si vous faites un pok et `mon`{.fichier} si vous faites un mon.

```text
---
layout: layout/post.njk

title: "Contribuer au site"
authors:
  - François Brucker
résumé: "Comment contribuer au site Do_It."

tags:
  - 'cs'
---
```

### Résumé

Dans l'entête.

### corps du texte

Le reste du post, écrit en markdown. Le titre est déjà mis, vos différentes parties sont donc de niveau `##`{.language-}

### les ressources

Placez les ressources dans le même dossier que votre post. Vos liens auront alors l'une des deux formes suivantes

#### Ressources à télécharger

```text
[ressource à télécharger](./sources.zip)`{.fichier}
```

#### Images

```text
![image à voir](./mon-image.png)`{.fichier}
```

{% attention %}
Si vous nommez votre fichier autrement que `index.md`{.fichier}, il faut mettre `../` devant le chargement de votre ressource (ex : `![image à voir](../mon-image.png)`{.fichier}).

En effet, si vous utilisez par exemple `mon_fichier.md`{.fichier} comme nom de post, eleventy va :

1. créer un dossier nommer `mon_fichier`{.fichier}
2. placer votre post dans ce dossier et le renommer `index.md`{.fichier}

Vos images ne se retrouvent du coup plus dans le bon dossier...

C'est pourquoi, il est recommandé de toujours créer un dossier avec le nom de votre post et d'y mettre vos données,fichier `index.md`{.fichier} et ressources.

{% endattention %}

## Possibilités étendues en markdown

Plusieurs balises spéciales ont été ajoutées pour vous aider à écrire des parties spécifiques de votre post.

### liens

Il existe plusieurs façons d'écrire les liens. On suppose que l'on a l'architecture suivante :

```
src
└── pok
    ├── un-site-chez-moi
    │   ├── FB-GD
    │   │   ├── index.njk
    │   │   └── sources.zip
    │   ├── RS
    │   └── index.njk
    ├── index.njk
    └── cs
       ├── contribuer-au-site
       │   └── index.md
       └── index.njk
```

Et que l'on veuille, depuis le post `FB-GD`{.fichier}, aller vers le post `contribuer-au-site`{.fichier}.

Il y a deux façons de faire :

- lien absolu. Depuis la racine du site (qui est `src`{.fichier}) `[lien]({{ "/cs/contribuer-au-site" | url }})`{.language}
- lien relatif. Depuis là on je suis : `[lien](../../../cs/contribuer-au-site)`{.language} (je remonte 3 dossier avant de redescendre dans l'arborescence)

### Texte spécial

En plus des possibilités markdown, on ajoute deux distinctions de texte :

- fichier : `nom-fichier`{.fichier} que l'on écrit : \`nom-fichier\`\{.fichier\}
- code : `print("coucou !")`{.language-} que l'on écrit : \`print("coucou !")\`\{.language-\}

### Shortcodes

Les _shortcodes_ sont des aides markdown. Elles permettent de mettre en valeur un paragraphe. elles sont toutes de la même forme :

```text
<div>
&#123;% nom_shortcode "titre de la shortcode" %}

le contenu de la shortcode.

&#123;% endnom_shortcode %}
</div>
```

{% note %}
Le titre de la shortcode est toujours optionnel. Mais s'il est présent il est **obligatoirement** entre " ".
{% endnote %}

#### Shortcode `attention`

{% attention "**faisez** attention" %}
Une _grosse_ mise en garde.
{% endattention %}

Code :

```text
<div>
&#123;% attention "**faisez** attention" %}
Une *grosse* mise en garde.
&#123;% endattention %}
</div>
```

#### Shortcode `note`

Nom de la shortcode : `note`

{% note %}
Une note à retenir.
{% endnote %}

Code :

```text
<div>
&#123;% note %}
Une note à retenir.
&#123;% endnote %}
</div>
```

#### Shortcode `info`

{% info %}
Un truc marrant ou une information utile, mais pas indispensable.
{% endinfo %}

Code :

```text
<div>
&#123;% info %}
Un truc marrant ou une information utile, mais pas indispensable.
&#123;% endinfo %}
</div>
```

#### Shortcode `faire`

{% faire %}
Quelque-chose à faire.
{% endfaire %}

Code :

```text
<div>
&#123;% faire %}
Quelque-chose à faire.
&#123;% endfaire %}
</div>
```

#### Shortcode `details`

{% details "titre de la shortcode" %}
Quelque chose de caché. Que l'on peut _écrire_ en `Markdown`
{% enddetails %}

Le titre de la shortcode est automatiquement mis en gras.

Code :

```text
<div>
&#123;% details "titre de la shortcode" %}
Quelque chose de caché. Que l'on peut *écrire* en `Markdown`
&#123;% enddetails %}
</div>
```

#### Shortcode `exercice`

{% exercice %}
Un exercice à faire.
{% endexercice %}

On peut le combiner avec la shortcode `details` pour créer un exercice et son corrigé :

{% exercice %}
Sujet de l'exercice
{% endexercice %}
{% details "corrigé" %}
Le corrigé de l'exercice.
{% enddetails %}

Code :

```text
<div>
&#123;% exercice %}
Sujet de l'exercice
&#123;% endexercice %}
&#123;% details "corrigé" %}
Le corrigé de l'exercice.
&#123;% enddetails %}
</div>
```

#### Shortcode `chemin`

Pour emmener vers un autre cours par exemple :

{% chemin %}
[Cours do-it de FB](https://francoisbrucker.github.io/cours_informatique/enseignements/ecm/3A/do-it/)
{% endchemin %}

Code :

```text
<div>
&#123;% chemin %}
[Cours do-it de FB](https://francoisbrucker.github.io/cours_informatique/enseignements/ecm/3A/do-it/)
&#123;% endchemin %}
</div>
```

#### <span id="prerequis"></span>Shortcode `prerequis`

{% prerequis %}

- un pré-requis à lire
- un autre pré-requis à lire

{% endprerequis %}

Code :

```text
<div>
&#123;% prerequis %}

- un pré-requis à lire
- un autre pré-requis à lire

&#123;% endprerequis %}

</div>
```

#### <span id="lien"></span> Shortcode `lien`

{% lien %}

- [un MON utile](/promos/2023-2024/Lucie-Le-Boursicaud/mon/temps-2.2/)
- [un cours qui sert](https://francoisbrucker.github.io/cours_informatique/cours/web/)

{% endlien %}

Code :

```text
<div>
&#123;% lien %}

- [un MON utile](/promos/2023-2024/Lucie-Le-Boursicaud/mon/temps-2.2/)
- [un cours qui sert](https://francoisbrucker.github.io/cours_informatique/cours/web/)

&#123;% endlien %}

</div>
```

#### Shortcode `lieninterne`

{% lieninterne "/promos/20XX-20YY/Zola-Gordon/pok/temps-1" %}

Code avec un lien absolu :

```text
&#123;% lieninterne "/promos/20XX-20YY/Zola-Gordon/pok/temps-1" %}
```

Codes avec des liens relatifs (par exemple dans votre fichier `/promos/20XX-20YY/Zola-Gordon/pok/index.md)` :

```text
&#123;% lieninterne "./temps-1" %}
&#123;% lieninterne "./temps-2/" %}
```


### Écrire du code

Pour écrire du code, le thème [prismjs](https://prismjs.com/) se chargera de la coloration syntaxique.

Par exemple :

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <link rel="icon" href="assets/favicon.png" />
        ...
    </head>
    <body class="language-none">
    <header data-plugin-header="line-numbers"></header>
    <section class="language-markup">
      <h1>How to use</h1>
      ...
    </body>
</html>
```

Peut s'écrire avec le markdown suivant :

<pre>
    <code>
```html
&lt;!DOCTYPE html>
&lt;html lang="en">
    &lt;head>
        &lt;meta charset="utf-8" />
        &lt;link rel="icon" href="assets/favicon.png" />
        ...
    &lt;/head>
    &lt;body class="language-none">
    &lt;header data-plugin-header="line-numbers"></header>
    &lt;section class="language-markup">
      &lt;h1>How to use</h1>
      ...
    &lt;/body>
&lt;/html>
```
    </code>
</pre>

Également, il est possible d'ajouter les numéros de ligne comme ceci :

```python/
print(42)
print(43)
```

Avec le code :

<pre>
    <code>
```python/
print(42)
print(43)
```
    </code>
</pre>


### Tables

On utilise les possibilités de [multimarkdown](https://fletcher.github.io/MultiMarkdown-6/syntax/tables.html)

#### Table avec titre

| titre colonne 1 | titre colonne 2 |
| --------------- | --------------- |
| Content Cell    | Content Cell    |
| Content Cell    | Content Cell    |

Code :

```text
| titre colonne 1  | titre colonne 2 |
| ---------------- | --------------- |
| Content Cell     | Content Cell    |
| Content Cell     | Content Cell    |
```

#### Tables sans titre

| ------------- | ------------- |
| Content Cell | Content Cell |
| Content Cell | Content Cell |

Code :

```text
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
```

#### Tables multi-colonnes

| ------------- | ------------- |
| Je prends 2 colonnes ||
| Content Cell | Content Cell |

Code :

```markdown
| ------------- | ------------- |
| Je prends 2 colonnes ||
| Content Cell | Content Cell |
```

#### Tables multi-lignes

| ------------- | ------------- |
| Je prends 2 lignes |Content Cell |
| ^^ |Content Cell |
| Content Cell | Content Cell |

Code :

```markdown
| ------------- | ------------- |
| Je prends 2 lignes |Content Cell |
| ^^ |Content Cell |
| Content Cell | Content Cell |
```

#### plusieurs ligne dans une cellule

| ------------- | ------------- |
| 1. ligne colonne 1 | 1. ligne colonne 2 | \
| 1. ligne colonne 1 | 2. ligne colonne 2 |
| Content Cell | Content Cell |

Code :

```markdown
| ------------- | ------------- |
| 1. ligne colonne 1 | 1. ligne colonne 2 | \
| 1. ligne colonne 1 | 2. ligne colonne 2 |
| Content Cell | Content Cell |
```

#### Alignement horizontal

| :- | :-: | -: |
| Content Cell | Content Cell | Content Cell |
| Content Cell | Content Cell |Content Cell |
| Content Cell | Content Cell |Content Cell |

Code :

```markdown
| :- | :-: | -: |
| Content Cell | Content Cell | Content Cell |
| Content Cell | Content Cell |Content Cell |
| Content Cell | Content Cell |Content Cell |
```

#### Alignement vertical

On ajoute un style, mais il ne faut pas que ce soit la dernière colonne. Exemple sur une colonne multi-ligne :

| ------------- | ------------- |
| Content Cell {style="vertical-align:middle"}| Content Cell |
| ^^| Content Cell |
| Content Cell | Content Cell |

Code :

```markdown
| ------------- | ------------- |
| Content Cell {style="vertical-align:middle"}| Content Cell |
| ^^| Content Cell |
| Content Cell | Content Cell |
```

Si l'on veut avoir un alignement vertical de la dernière colonne, il faut ajouter une colonne vide (je ne sais pas trop pourquoi) :

| ------------- | ------------- | - |
| Content Cell | Content Cell {style="vertical-align:middle"}| |
| Content Cell | ^^ | |
| Content Cell | Content Cell | |

Code :

```markdown
| ------------- | ------------- | - |
| Content Cell | Content Cell {style="vertical-align:middle"}| |
| Content Cell | ^^ | |
| Content Cell | Content Cell | |
```

## tbd

> TBD
>
> - résumé :
>
>   1. toujours pris en compte : dans l'entête
>   2. dans les résumés si pas 1
>      1. premier paragraphe
>      2. entre balise
>
> - pok, mon, mon-index, pok-index, projet
> - entête, pas de `[]` que des listes
