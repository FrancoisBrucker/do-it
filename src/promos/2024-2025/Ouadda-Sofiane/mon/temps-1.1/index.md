---
layout: layout/mon.njk

title: "Découverte des fondamentaux HTML/CSS et Git"
authors:
  - Sofiane Ouadda
date: 2024-09-16

tags: 
  - "temps 1"
  - "Developpement FrontEnd"
  - "HTML"
  - "CSS"
  - "Git"

résumé: "Durant cette première phase d'apprentissage, j'ai étudié les bases du HTML, du CSS et de Git, principalement via des vidéos YouTube et un cours GitHub. Cet apprentissage m'a permis de poser les fondations pour développer un site web et de comprendre les concepts clés du versionnage de code avec Git. J'ai également commencé à apprendre les bonnes pratiques pour structurer un projet de développement avec du HTML et CSS."

---

{% prerequis %}

Aucun prérequis nécessaires.

{% endprerequis %}
{% lien %}

[`Introduction au HTML - YouTube`](https://www.youtube.com/watch?v=68oSyuKVjeU&t=0s)

[`Introduction au CSS - YouTube`](https://www.youtube.com/watch?v=iSWjmVcfQGg)

[`Tutoriel GitHub - Web Dev for Beginners`](https://github.com/microsoft/Web-Dev-For-Beginners/blob/main/3-terrarium/1-intro-to-html/README.md)

{% endlien %}

## Contenu

### HTML

Mon apprentissage du HTML a commencé avec une vidéo YouTube qui m’a permis de comprendre les concepts fondamentaux de ce langage. J'ai appris que le HTML permet de structurer les pages web et de définir les différents éléments visibles. J'ai découvert comment utiliser des balises pour organiser le contenu, ainsi que des attributs pour ajouter des détails et des liens. Le tutoriel GitHub que j'ai suivi m'a permis de consolider ces connaissances en réalisant des exercices pratiques, ce qui m’a aidé à mieux comprendre comment les balises s'imbriquent et comment structurer efficacement une page.

#### Qu'est-ce que HTML ?

HTML (HyperText Markup Language) est le langage de base pour structurer le contenu d'une page web. Il permet de définir des éléments tels que les titres, les paragraphes, les images, les liens, etc. Chaque élément de la page est encadré par des balises (tags).

Exemple d’une balise HTML :
```<p>Ceci est un paragraphe en HTML</p>```

#### Les bases du HTML
##### Structure de base d'une page HTML
Chaque document HTML suit une structure de base qui commence par la déclaration <!DOCTYPE html>. Voici un exemple de la structure minimale d'une page HTML :

```
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mon site vitrine</title>
</head>
<body>
    <header>
        <h1>Bienvenue sur mon site vitrine</h1>
    </header>
    <main>
        <p>Ceci est une simple page web réalisée en HTML et CSS.</p>
    </main>
    <footer>
        <p>&copy; 2024 MonSite</p>
    </footer>
</body>
</html>
```
* `<!DOCTYPE html>` : Indique au navigateur qu'il s'agit d'un document HTML5.
* `<html>` : La balise racine qui contient tout le contenu de la page.
* `<head>` : Contient les métadonnées (titre, encodage, etc.) de la page.
* `<body>` : Contient le contenu visible de la page.

##### Balises HTML courantes
Voici quelques balises couramment utilisées dans les pages HTML :

* `<h1>` à `<h6>` : Balises de titres, `<h1>` étant le plus important.
* `<p>` : Balise de paragraphe.
* `<a>` : Balise pour créer des liens hypertextes.
* `<img>` : Balise pour insérer des images.

##### Liens et images
Les liens et les images sont des éléments essentiels de toute page web.

Exemple de lien hypertexte :

```
<a href="https://www.example.com">Visitez mon site</a>
```

Exemple d'image :

```
<img src="image.webp" alt="Description de l'image">
```

### CSS

En parallèle, j'ai étudié le CSS à travers une autre vidéo YouTube, qui portait sur la mise en forme des pages HTML. Le CSS est utilisé pour styliser les pages en ajustant les couleurs, les polices, les tailles, les marges, et la disposition des éléments sur la page. J'ai appris à utiliser les sélecteurs CSS pour cibler des éléments précis et appliquer des styles. J'ai aussi découvert comment gérer la mise en page en utilisant des concepts comme le "box model", ainsi que la gestion des marges, des bordures et des espacements pour créer des designs plus avancés. 

#### Qu'est-ce que CSS ?

CSS (Cascading Style Sheets) est le langage utilisé pour styliser une page web. Il permet de définir l'apparence des éléments HTML, comme la couleur, la taille des polices, les marges, les bordures, etc.

Exemple d’un style CSS :
```
p {
  color: blue;
  font-size: 18px;
}
```

#### Les bases du CSS
Introduction aux sélecteurs CSS
Les sélecteurs CSS sont utilisés pour cibler les éléments HTML à styliser. Voici quelques exemples courants :

* Sélecteur par type de balise : sélectionne tous les éléments de ce type.
* Sélecteur par classe : sélectionne tous les éléments avec une certaine classe.
* Sélecteur par ID : sélectionne l'élément avec l'ID spécifique.

#### Mise en forme du texte et des éléments
Le CSS permet de modifier l'apparence du texte et des éléments HTML. Voici quelques propriétés de base :

* Couleur du texte : color
* Police : font-family
* Taille du texte : font-size
* Marges : margin
* Padding (espacement intérieur) : padding

Exemple : 
```
h1 {
    color: blue;
    font-family: Arial, sans-serif;
    margin-bottom: 20px;
}
```
#### Disposition et mise en page
Le CSS propose différentes techniques pour organiser les éléments sur la page, notamment :

* Flexbox : une méthode puissante pour aligner et distribuer les éléments dans un conteneur.
* Grid : une autre méthode pour créer des mises en page plus complexes.


### Git

En parallèle de l’apprentissage du HTML et du CSS, j'ai appris à utiliser Git pour versionner mon travail. Git est un outil essentiel dans le développement, qui permet de suivre les modifications du code et de collaborer plus facilement. J'ai appris les commandes basiques comme `git init`, `git add`, `git commit` et `git status`. Cela m’a permis de mieux comprendre comment gérer un projet et enregistrer mes différentes étapes de développement de manière efficace.

### Bonnes pratiques de développement

En complément de ces apprentissages, j'ai commencé un tutoriel sur les bonnes pratiques pour structurer un projet de développement en HTML et CSS. Ce tutoriel m'a enseigné comment organiser mes fichiers, structurer mon code de manière propre et lisible, et respecter les standards du web pour améliorer la maintenance de mon projet à long terme. J'ai notamment appris l'importance d'une architecture de fichiers bien définie (par exemple, séparer les fichiers CSS externes du HTML), ainsi que des conventions de nommage claires pour éviter la confusion dans les gros projets.

### Horodateur

| Date            | Heures passées | Indications |
| --------------- | -------------- |-------------|
| Lundi 09/09     | 2H             | Introduction au HTML avec une vidéo YouTube |
| Mercredi 11/09  | 1H             | Premières notions sur Git et utilisation des commandes de base |
| Vendredi 13/09  | 1H             | Apprentissage des bases du CSS via une vidéo YouTube |
| Dimanche 15/09  | 2H             | Tutoriel GitHub : exercices pratiques sur HTML et CSS |
| Lundi 16/09     | 2H             | Suite de l'apprentissage des bases du CSS |
| Mardi 16/09     | 1H             | Exploration plus poussée des attributs HTML et des sélecteurs CSS |
| Mardi 17/09     | 1H             | Initiation aux bonnes pratiques de développement en HTML/CSS : structurer un projet |