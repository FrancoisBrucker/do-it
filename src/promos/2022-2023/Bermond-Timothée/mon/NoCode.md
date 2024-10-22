---
layout: layout/mon.njk

title: "No code"
authors:
  - Timothée Bermond

date: 2023-01-25

tags:
  - 'temps 2'
  - 'WordPress'
  - 'Bubble'
---

<!-- début résumé -->
Formation à WordPress et Bubble.
<!-- fin résumé -->

{% prerequis %} 

Pas de prérequis même si c'est plus facile à comprendre si on est déjà familier avec le dev web.

{% endprerequis %}

## Qu'est-ce que le No code?

Le No code est un mode de développement de logiciels sans ligne de codes (ou presque) à l'aide d'outils de modélisation et de configuration visuels (templates, drag-and-drop, extensions,...). Il permet de rendre accessible le dev web à des personnes n'ayant pas ou peu de connaissances en langages informatiques.

## Pourquoi le No code ?

Le No code est de plus en plus utilisé et a de nombreux avantages :
- Facile à prendre en main : les outils No code sont assez facile à prendre en main même sans connaissance en dev et souvent très intuitive.
- Réduction des coûts : grâce aux outils No code les coûts de développement sont diminués (requièrent moins d'expertise, pas besoin d'une équipe de dev).
- Meilleur agilité : très facile de mettre en place une application afin de la tester, peut-être très utile pour les MVP.
- Gain de temps : plus rapide que le développement traditionnel.
- Facilement modifiable : la où il faut réussir à comprendre le code afin de le modifier sans tout casser avec un outil No code il est très simple de modifier son site ou son application.

Cependant les outils No code restent plus rigides que le dev traditionnel (personnalisation restreinte) et leur utilisation entraîne un manque de contrôle, on devient dépendant technologiquement de la plateforme No code utilisée.

Dans la suite je vais vous présenter deux plateformes No code : WordPress et Bubble.

## WordPress

J'ai suivi la formation openclassrooms [Créez un site moderne et professionnel avec WordPress5](https://openclassrooms.com/fr/courses/5489551-creez-un-site-moderne-et-professionnel-avec-wordpress-5)

Cette formation utilise [Themecloud](https://app.themecloud.io/) comme hébergeur qui nous permet de disposez d'un site WordPress gratuit pendant 30 jours. 

Une fois sur Themecloud, il faut se connecter et créer un nouveau site en lui choisissant un nom.

### Dashboard

Pour pouvoir modifier son site, il faut se rendre sur l'URL monsite.com/wp-login.php (où monsite est le nom de votre site).

Afin d'avoir la même interface que dans le tuto openclassrooms j'ai installé le thème *Twenty Seventeen*. Ce n'est pas obligatoire mais plus simple pour suivre le tuto.

WordPress propose deux types de contenus par défaut :
- des articles (contenu d'actualité daté)
- des pages (contenu statique qui peut notamment contenir des articles)

### Paramètrage

Il y a plusieurs paramètres qu'il est possible de régler, en voici une liste non exhaustive :
- la langue de l'interface;
- le titre, c'est ce qui va apparaître dans les résultats des recherches google, il faut donc qu'il soit accrocheur;
- le slogan, qui va aussi apparaître dans les résultats de recherche;
- les paramètres des commentaires;
- la page d'accueil du site;
- la visibilité pour les moteurs de recherche (il est intéressant de décocher cette case afin que personne ne tombe sur le site avant qu'il soit fini);
- la structure des liens (le mieux est d'avoir le titre de l'article dans l'url pour le référecement naturel).

### Premier article

Pour créer un article, il faut se rendre dans *"Posts"* puis cliquer sur *"Add new"*. On a ensuite la possibilité d'entrer un titre et du contenu. Pour ajouter des **blocs** de contenus il suffit de cliquer sur le *plus* en haut à gauche et de choisir quel type de bloc on veut ajouter. Il existe plein de type de bloc différent par exemple texte, media, widget, design... 

On peut ensuite agencer les blocs dans l'ordre qu'on le souhaite avec l'icône présentant 6 petits points ou avec les flèches haut/bas.

Dans les paramètres de l'article, il est possible d'ajouter des **catégories** ou des **tags**. La différence est que les catégories ont une hiérarchie (il est possible de créer des sous-catégories) contrairement aux tags. On peut également ajouter une "Featured Image" qui correspond à l’image principale rattachée à l’article.

Pour publier l'article il suffit de cliquer sur le bouton "Publish".

Pour chaque article il est possible de :
- modifier sa **visibilité** (public, privé ou protégé par un mdp);
- **planifier** une date de publication;
- **épingler** l'article pour qu'il soit toujours afficher en tête de liste.

### Créer une page d'accueil

Afin de créer une nouvelle page, il faut se rendre dans le dashboard, aller dans *Pages* puis cliquer sur *Add New*. On accède à la même interface que pour la création des articles. 

Dans *Settings*, puis *Reading*, en choissant *A static page*, il est possible de choisir quelle page sera la page d'accueil et quel page contiendra les articles.

Il faut ensuite créer un menu de navigation afin de se rendre d'une page à une autre.

Pour cela, on se rend dans *Appearance* puis *Menus* et on peut créer un menu dans lequel on ajoute les pages que l'on veut voir apparaitre. On peut également choisir l'ordre en glissant une page au-dessus d'une autre. Afin de l'afficher comme menu de navigation il faut sélectionner *Top menu*.

### Customizer

Le customizer permet de modifier l'apparence générale du site (logo, favicon, couleurs, mise en page).

Afin d'y accéder, il faut aller dans *Appearance* puis dans *Customize*.

### Themes et page builder

Il est possible d'installer des thèmes Wordpress. Ce sont des templates qui peuvent être gratuits ou non et qui configurent la structure et l'apparence du site. 

Le "page builder" est un composant qui permet de créer des pages plus complexes en "drag-and-drop"

### Extensions

Une extension Wordpress est un composant qui permet d'ajouter une fonctionnalité qui n'existe pas dans WordPress. Il en existe une multitude pour faire à peu prêt tout ce qu'on veut.

### Dernière étape

Une fois que l'on a créé son site il ne faut pas oublier le réferencement. Je ne vais pas le détailler ici.

Il faut également vérifier que toutes les pages du site fonctionnent bien (affichage, liens, formulaires,...), et sécuriser son site pour éviter de se faire hacker.

## Bubble

Bubble est un logiciel No code permettant de développer des sites ou des applications web. 
Pour y accéder il faut se rendre sur la [page](https://bubble.io) et se créer un compte.
Puis on peut créer une nouvelle application. Pour cela, il suffit de choisir une url et c'est parti.
Personnellement j'ai suivi la [formation ottho](https://www.ottho.co/sinitier-au-no-code?formation-categorie=e-learning-i#programme) qui est très complète. J'ai fait un petit résumé simplifié de ce qu'il est possible de faire avec Bubble mais je vous invite à suivre la formation si vous voulez être complètement opérationnel sur Bubble. 

### L'interface

L'interface de Bubble est très intuitive, un panneau à gauche contient 7 menus. 
Nous allons tout d'abord nous concentrer sur le menu design qui contient les différents éléments qu'il est possible d'ajouter sur la page en cliquant ou en drag-and-drop.
Il existe 3 catégories d'éléments : 
- Visual element : affichage / appel de la donnée (texte, image, bouton,...)
- Containers : permet de grouper des éléments
- Input forms : permet d'enregistrer de la donnée

Une fois l'élément ajouté une fenêtre d'options s'ouvre dans laquelle il est possible de modifier l'apparence, la disposition ou les dépendances.

Dans cette fenêtre d'options il est possible de modifier le style des textes. On peut choisir des styles déjà existants (h1, h2, ...) ou bien créer son propre style.

Avec *Arrange* en haut à droite ou avec un clic droit on peut accéder à des outils permettant d'organiser la mise en page (centrer, aligner, mettre au premier plan,...).

### Les workflows

Un *workflow* est un ensemble d'actions qui démarre à partir d'un événément déclenché sur la page. 
Il y a 2 types d'événements :
- Passif : quand la page se charge, ...
- Actif : quand l'utilisateur clique sur un bouton, ...
Une fois que l'événement à déclenché le workflow les actions s'enchainent les unes à la suite des autres de manière linéaire.
Il est également possible d'ajouter des conditions qui empêchent certaines actions de s'effectuer tant qu'elles ne sont pas remplies.

### Base de données

Il est possible de créer des tables comme on le souhaite ainsi que d'y ajouter ou de supprimer les champs que l'on souhaite. Pour chaque champ il faut entrer quel type de donnée est attendu.

Il est également possible de créer des relations entre différentes tables. Pour ce faire, il suffit d'ajouter dans le champ de la table 1 la table 2. Cette relation a un sens, on peut accéder aux informations de la table 2 dans la table 1 mais pas aux informations de la table 1 dans la table 2.

Lorsque l'on veut afficher des données contenues dans une table il est possible de trier ou bien de filtrer les données.

