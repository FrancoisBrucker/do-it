---
layout: layout/pok.njk

title: "Réalisation d'un site sur eleventy et comparaison avec WordPress"
authors:
  - Ossama Abdane

date: 2023-01-04

tags:
  - 'temps 2'
---

## Objectif
L'objectif de ce POK est d'approfondir les bases de création acquise lors du temps 1. L'idée est de suivre le tutoriel créé par Nicolas pour son MON : "Créer un site web statique avec 11ty". Pour ainsi découvrir un nouveau moyen de créer un site internet.
Dans un deuxième temps, j'ai réalisé une comparaison entre la création d'un site avec eleventy et WordPress (réalisée dans mon MON2.2). 

## Création d'un site avec Eleventy  

Le MON de Nicolas a été très  et complet pour la création d'un site statique basique. En le suivant, j'ai pu créer facilemnt un premier site simple.

{% info %}
Une formation **html** peut être nécessaire pour mieux comprendre et réaliser des templates.  
{% endinfo %}

## Eleventy 

### Avantages

* Rapidité et performance élevées : Comme Eleventy génère des sites statiques, ils sont généralement plus rapides et plus performants que les sites dynamiques générés par des systèmes de gestion de contenu comme WordPress. Les sites statiques ne nécessitent pas de requêtes de base de données ou de scripts PHP pour charger le contenu, ils sont donc plus rapides à charger pour les utilisateurs.
* Flexibilité en termes de mise en page : Eleventy est basé sur des templates, ce qui signifie que vous pouvez utiliser n'importe quel type de fichier pour créer votre site web, comme HTML, CSS, JavaScript, etc. Cela vous permet de personnaliser entièrement l'apparence de votre site web et de l'adapter à vos besoins spécifiques.
* Peut être utilisé avec n'importe quel type de fichier : Eleventy est un générateur de site statique qui peut utiliser n'importe quel type de fichier pour générer votre site web. Cela signifie que vous pouvez utiliser des fichiers Markdown, JSON, YAML, etc. pour créer votre contenu, ce qui est particulièrement utile pour les sites web de documentation ou les blogs.


### Inconvénients 

* Pas autant de fonctionnalités que WordPress : Eleventy est un générateur de site statique, il est donc moins capable de fournir les fonctionnalités avancées que vous pourriez trouver dans un système de gestion de contenu comme WordPress, comme les formulaires de contact, les commentaires, les médias, etc.
* Moins de support et de communauté : Eleventy est un projet open-source relativement nouveau comparé à WordPress, il y a donc moins de support et de communauté disponible pour résoudre les problèmes ou pour obtenir de l'aide.

### Exemples de sites utilisant eleventy

* Mozilla Developer Network : https://developer.mozilla.org/fr/
* Snipcart : https://snipcart.com/fr
* Smashing Magazine : https://www.smashingmagazine.com

## WordPress 

### Avantages

* Facilité d'utilisation : WordPress est un système de gestion de contenu très populaire qui est conçu pour être facile à utiliser pour les utilisateurs non techniques. Il fournit une interface utilisateur intuitive pour créer et gérer du contenu, ajouter des images et des vidéos, etc.
* Grande variété de fonctionnalités et d'extensions : WordPress est un système de gestion de contenu très populaire et bien supporté, il y a donc une grande variété de fonctionnalités et d'extensions disponibles pour ajouter des fonctionnalités supplémentaires à votre site web, comme des formulaires de contact, des commentaires, des médias, etc. Il existe également de nombreux thèmes et plugins gratuits ou payants disponibles pour personnaliser l'apparence et les fonctionnalités de votre site web.
* Bien supporté et grande communauté d'utilisateurs et de développeurs : WordPress est un projet open-source très populaire et bien supporté, il y a donc une grande communauté d'utilisateurs et de développeurs qui peuvent aider à résoudre les problèmes et fournir de l'aide. Il y a également beaucoup de documentation et de tutoriel disponible pour apprendre à utiliser WordPress.

### Inconvénients 

* Peut être plus lourd et moins performant que les sites statiques : Comme WordPress génère des sites dynamiques qui nécessitent des requêtes de base de données et des scripts PHP pour charger le contenu, ils peuvent être plus lents à charger pour les utilisateurs que les sites statiques générés par Eleventy.
* Moins de flexibilité en termes de mise en page : Bien que WordPress permet de personnaliser l'apparence de votre site web à l'aide de thèmes et de plugins, il peut être moins flexible que Eleventy en termes de mise en page car il est basé sur des templates prédéfinis.

### Exemples de sites utilisant WordPress

* BBC America : https://www.bbcamerica.com
* Sony Music : https://www.sonymusic.fr
* The New Yorker : https://www.newyorker.com
* Forbes : https://www.forbes.fr


## Cadre opportun d'utilisation 

### Pour Eleventy :

* Sites web à haute performance : Si vous avez besoin d'un site web qui charge rapidement et qui offre une grande expérience utilisateur, Eleventy peut être une excellente option car il génère des sites statiques qui sont généralement plus rapides et plus performants que les sites dynamiques générés par des systèmes de gestion de contenu tels que WordPress.
* Sites web à contenu statique : Si vous avez besoin d'un site web qui affiche principalement du contenu statique (comme une page "à propos", une page de contact, etc.) et qui n'a pas besoin de fonctionnalités avancées telles que les formulaires de contact ou les commentaires, Eleventy peut être une excellente option car il est facile à utiliser et offre une grande flexibilité en termes de mise en page.
* Sites web de documentation ou de blogs : Si vous avez besoin d'un site web pour présenter des articles, des guides, des tutoriels, etc., Eleventy peut être une excellente option car il peut utiliser des fichiers Markdown, JSON, YAML, etc. pour créer votre contenu, ce qui est particulièrement utile pour les sites web de documentation ou les blogs.

### Pour WordPress :

* Sites web à contenu dynamique : Si vous avez besoin d'un site web qui affiche du contenu dynamique (comme des articles de blog, des actualités, etc.) et qui a besoin de fonctionnalités avancées telles que les formulaires de contact, les commentaires, les médias, etc., WordPress peut être une excellente option car il est facile à utiliser et offre une grande variété de fonctionnalités et d'extensions pour ajouter des fonctionnalités supplémentaires.
* Sites web de tous types : WordPress est un système de gestion de contenu très populaire qui peut être utilisé pour créer des sites web de tous types, des blogs aux sites d'entreprise. Il est facile à utiliser et offre une grande variété de fonctionnalités et d'extensions pour ajouter des fonctionnalités supplémentaires.
* Sites web avec une forte exigence en terme de personnalisation: WordPress est un système de gestion de contenu très populaire qui est bien supporté et possède une grande communauté d'utilisateurs et de développeurs. Il existe de nombreux thèmes et plugins gratuits ou payants disponibles pour personnaliser l'apparence et les fonctionnalités de votre site web, ce qui en fait une option idéale pour les sites web qui ont une forte exigence en termes de personnalisation.
* Sites web à forte fréquentation : Si vous prévoyez que votre site web aura une forte fréquentation, WordPress peut être une bonne option car il est bien supporté et peut être configuré pour gérer efficacement les requêtes et les visites. Il existe également des plugins et des services tels que des cache pour améliorer les performances, ce qui peut aider à gérer les charges de trafic élevées.

### Combinaison des deux :

Il est tout à fait possible de combiner les avantages d'Eleventy et de WordPress pour créer un site web qui répond parfaitement à vos besoins. Il y a plusieurs façons de combiner ces deux options :

* Utiliser Eleventy pour générer des pages statiques et WordPress pour gérer les fonctionnalités dynamiques : Vous pouvez utiliser Eleventy pour générer les pages statiques de votre site web (comme la page d'accueil, la page "à propos", etc.) et WordPress pour gérer les fonctionnalités dynamiques telles que les formulaires de contact, les commentaires, les médias, etc. Cela permet de profiter des avantages de la rapidité et de la performance d'Eleventy pour les pages statiques, tout en utilisant les fonctionnalités avancées de WordPress pour les parties dynamiques de votre site web.
* Utiliser Eleventy pour générer les pages statiques et WordPress pour gérer le contenu : Vous pouvez utiliser Eleventy pour générer les pages statiques de votre site web et WordPress pour gérer le contenu. Cela permet de profiter des avantages de la rapidité et de la performance d'Eleventy pour les pages statiques, tout en utilisant les fonctionnalités de gestion de contenu de WordPress pour créer et gérer facilement le contenu de votre site web.
* Utiliser Eleventy pour générer les pages statiques et WordPress pour gérer les données : Vous pouvez utiliser Eleventy pour générer les pages statiques de votre site web et WordPress pour gérer les données. Cela permet de profiter des avantages de la rapidité et de la performance d'Eleventy pour les pages statiques, tout en utilisant les fonctionnalités de gestion de données de WordPress pour créer et gérer facilement les données de votre site web.

Il est important de noter que combiner Eleventy et WordPress nécessite une certaine expertise technique pour configurer et maintenir les deux systèmes, mais cela permet de créer un site web qui répond parfaitement à vos besoins en termes de performance et de fonctionnalités.

## Ressources utilisées 

* Site Eleventy : https://www.11ty.dev
* Tutoriel youtube : https://www.youtube.com/watch?v=BKdQEXqfFA0
* MON de Nicolas : https://francoisbrucker.github.io/do-it/mon/NB/mes-mon/statique-eleventy/
* WordPress contre 11ty : Quel est le meilleur ? : https://targettrend.com/fr/wordpress-vs-11ty/
* Kinsta : https://kinsta.com/fr/blog/generateurs-de-sites-statiques/