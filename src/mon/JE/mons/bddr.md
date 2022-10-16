---
layout: layout/post.njk

title: "Bases de Données relationnelles, MySQL, SQLAlchemy"
authors:
  - Jeffrey Edisah

---
<!-- début résumé -->

Revoir le SQL, créer et gérer une base de données relationnelle, découvrir l'ORM SQLAlchemy

<!-- fin résumé -->


## SQL

Le langage SQL sert à manipuler, récupérer des informations dans, créer et supprimer les bases de données relationnelle. Savoir utiliser ce langage est un prérequis. Les cours disponibles sont pour la plupart liés à la récupération des données dans les tables. Une requête s'écrit comme ceci

    SELECT column_name FROM table
    WHERE condition
    GROUP BY column_name
    HAVING function(column_name)

Avec généralement moins de ces mots clés dans les instructions. **SELECT** est le mot clé principal, nécessaire dans toutes les requêtes. **WHERE** permet de mettre des conditions pour les données que la requête demande. **GROUP BY** de la même façon permet d'afficher les données selon une catégorie spécifique.

le site web [sql.sh](sql.sh) permet de revoir le langage tandis que [sqlzoo](sqlzoo.net) permet de travailler ceux-ci à l'aide d'exercices pratiques pour plusieurs types de requêtes, en particulier pour les jointures **JOIN** qui peuvent être un peu retors.

## Création d'une base de données avec MySQL

## SQLAlchemy