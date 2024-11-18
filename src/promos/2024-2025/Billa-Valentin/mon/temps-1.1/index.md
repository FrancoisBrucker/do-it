---
layout: layout/mon.njk

title: "SQL Avancé"
authors:
  - Valentin Billa

date: 2024-09-05

tags:
  - 'temps 1'
  - 'vert'  
  - 'avancé'
  - 'sql'

résumé: Apprentissage de fonctionnalités avancées SQL
---

{% prerequis "**Prérequis :**" %}
* Vocabulaire de base solide en SQL (colonne, table, query...)
* SQL Basique (SELECT, FROM, WHERE...)
{% endprerequis %}

## Objectifs
Ayant une attirance particulière pour le back, SQL me fait de l'œil !
C'est pourquoi je souhaite me former à ses fonctions les plus avancées, 
à minima pour savoir qu'elles existent le jour où j'en aurais besoin.

Ce MON sera plutôt orienté MySQL (car j'aime bien leur doc) mais je
tenterais de faire des parallèles avec d'autres SGBD (Système de Gestion de Base de Données)
comme SQLite, PostgresSQL

## Optimization en Général

### SQL

Une particularité de SQL qu'il est important de garder en tête est qu'il ne s'agit pas réellement d'un langage
de programmation au sens traditionnel, mais plutôt d'un langage déclaratif. Lorsque nous écrivons une requête SQL,
nous ne donnons pas d'instructions détaillées sur la façon d'obtenir les données, mais nous décrivons plutôt
le résultat souhaité. C'est au SGBD de déterminer le meilleur moyen d'obtenir ce résultat.

Pour optimiser les requêtes SQL, il est crucial de comprendre comment le moteur de base de données interprète et exécute
ces requêtes. Une des méthodes essentielles pour obtenir y arriver est l'utilisation de la commande `EXPLAIN`.

### La commande `EXPLAIN`

La commande `EXPLAIN` permet de voir comment le SGBD interprète une requête SQL. Elle fournit des informations
détaillées sur le plan d'exécution d'une requête, ce qui peut aider à identifier les parties de la requête qui
pourraient être optimisées pour améliorer les performances.

Pour utiliser `EXPLAIN`, il suffit de la précéder à une requête SQL :

```sql
EXPLAIN SELECT * FROM users WHERE age > 25;
```

Le résultat de `EXPLAIN` comprend plusieurs colonnes importantes, notamment :

- **id** : l'identifiant unique de l'étape de requête.
- **select_type** : le type de requête SQL principale.
- **table** : la table à laquelle la requête accède.
- **possible_keys** : les index qui peuvent être utilisés pour accélérer la requête.
- **key** : l'index effectivement utilisé.
- **rows** : le nombre estimé de lignes que le SGBD doit parcourir pour satisfaire cette étape de la requête.
- **Extra** : des informations supplémentaires sur l'exécution de la requête.

{% note %}
La commande `EXPLAIN` renvoie un résultat honnêtement difficile à aborder les premières fois.
Avec le temps, on comprend de mieux en mieux les particularités à prendre en compte eg. les différents types de 
**select_type** et en l'occurrence ceux qui sont symptomatiques d'une query qui va être lente.
{% endnote %}

Par exemple, pour la requête précédente, le résultat de `EXPLAIN` pourrait ressembler à ceci :

```text
> EXPLAIN EXPLAIN SELECT * FROM users WHERE age > 25;
+----+-------------+-------+---------------+---------+---------+------+---------+-------------+
| id | select_type | table | possible_keys | key     | key_len | ref  | rows    | Extra       |
+----+-------------+-------+---------------+---------+---------+------+---------+-------------+
|  1 | SIMPLE      | users | NULL          | NULL    | NULL    | NULL | 1000000 | Using where |
+----+-------------+-------+---------------+---------+---------+------+---------+-------------+
```

Dans cet exemple, on voit que la table `users` est analysée sans utiliser d'index (NULL), et que la requête estime
devoir parcourir un million de lignes pour trouver les résultats. Cette estimation n'est pas anodyne, le SGBD fait 
des statistiques au fur et à mesure des requêtes faites en bases de données et s'en sert pour mieux adapter le plan
d'exécution, il est important que ces estimations ne soient pas trop loin du compte.

Une autre utilité d'`EXPLAIN` est de déterminer si deux requêtes SQL sont strictement équivalentes lors de leur exécution.
Ça peut être utile quand on essaie de réécrire une requête pour qu'elle soit plus lisible.

Par exemple
```sql
-- requête 1 (on parlera du mot clés WITH en dessous)
EXPLAIN WITH filtered_users AS (
    SELECT * FROM users WHERE age > 25
)
SELECT f.*, orders.*
FROM filtered_users f
JOIN orders ON f.user_id = orders.user_id;

-- requête 2
EXPLAIN SELECT u.*, o.*
FROM users u, orders o
WHERE u.age > 25 AND u.user_id = o.user_id;
```

Les plans d'exécution pour ces deux requêtes sont identiques, car elles accomplissent essentiellement la même tâche.

```text
+----+-------------+-------+---------------+---------+---------+------+---------+--------------------------------+
| id | select_type | table | possible_keys | key     | key_len | ref  | rows    | Extra                          |
+----+-------------+-------+---------------+---------+---------+------+---------+--------------------------------+
|  1 | SIMPLE      | users | NULL          | NULL    | NULL    | NULL | 1000000 | Using where; Using join buffer |
|  1 | SIMPLE      | orders| NULL          | NULL    | NULL    | NULL | 1000000 |                                |
+----+-------------+-------+---------------+---------+---------+------+---------+--------------------------------+
```

{% note %}
Attention néanmoins, il faut toujours garder en tête que même si deux requêtes font la même chose, 
elles peuvent mener à un plan d'exécution différent. En effet, le SQBD est libre d'interpréter le SQL
comme il le souhaite la seule garantie est qu'il renverra les résultats qu'on lui a demandés.
{% endnote %}

### La commande `ANALYZE`

La commande `ANALYZE` est utilisée pour analyser et stocker les informations clé pour une table. 
Elle permet d'explicitement demander au SGBD de collecter des statistiques sur la distribution des données dans une table.
Comme on l'a vu dans la partie `EXPLAIN` elle peut être très utile pour corriger des erreurs d'estimations.

```sql
ANALYZE TABLE users;
```

### La commande `OPTIMIZE`

La commande `OPTIMIZE` est utilisée pour optimiser les tables dans des bases de données comme MySQL. Elle est utile pour
récupérer l'espace inutilisé et pour améliorer les performances des requêtes. Après de nombreuses opérations
d'insertion, de mise à jour et de suppression, les tables peuvent devenir fragmentées. Utiliser la commande `OPTIMIZE`
aide à défragmenter les tables et à réorganiser les données sur le disque pour une performance optimale.

```sql
OPTIMIZE TABLE users;
```

Lorsque la commande est exécutée, le SGBD effectue les étapes suivantes:

- Défragmente la table et libère l'espace inutilisé.
- Réarrange les tables et les index.
- Actualise les statistiques des tables.

`OPTIMIZE` tout comme `ANALYZE` est une opération lourde qui doit être utilisée à bon escient, ie. par avant chaque requête,
ce serait contre productif.

## Indexes

Les **indexes** sont des structures de données associées aux tables d'une base de données. Ils permettent d'accélérer
considérablement les opérations de recherche en fournissant un accès rapide aux lignes de la table en fonction des
valeurs des colonnes indexées.

Ils permettent des optimisations de deux façons :
- **Amélioration des performances des requêtes** : Les indexes réduisent le temps de recherche des données. Par exemple,
  une recherche d'une ligne spécifique basée sur une colonne indexée sera beaucoup plus rapide qu'une recherche sans
  index.
- **Optimisation des tris et des jointures** : Les indexes peuvent être utilisés pour accélérer les opérations de tri (
  ORDER BY) et de jointure (JOIN), car les données sont souvent organisées de manière pré-optimisée.

Cependant, les indexes ont un **coût spatial** non négligeable. En effet, ils occupent de l'espace disque supplémentaire
qui peut devenir significatif, surtout si plusieurs colonnes d'une table sont indexées. Les indexes doivent également
être mis à jour chaque fois que les données de la table sont modifiées (insertions, suppressions, mises à jour), ce qui
peut ajouter un surcoût en termes de temps de traitement.

{% info %}
Une bonne pratique est de prioriser l'indexage des colones que l'on utilise beaucoup pour faire des tris ou filtres.
{% endinfo %}

Voici un exemple de création d'index pour la colonne `age` de la table `users` :

```sql
CREATE INDEX idx_users_age ON users (age);
```

Ce code crée un index sur la colonne `age` de la table `users`, ce qui peut améliorer la performance des requêtes qui
filtrent ou trient par la colonne `age`.

L'impact de cet index peut être observé dans le tableau `EXPLAIN` précédent :

```text
> EXPLAIN EXPLAIN SELECT * FROM users WHERE age > 25;
+----+-------------+-------+---------------+---------------+---------+------+---------+--------------------------+
| id | select_type | table | possible_keys | key           | key_len | ref  | rows    | Extra                    |
+----+-------------+-------+---------------+---------------+---------+------+---------+--------------------------+
|  1 | SIMPLE      | users | idx_users_age | idx_users_age | 5       | NULL | 1000000 | Using where; Using index |
+----+-------------+-------+---------------+---------------+---------+------+---------+--------------------------+
```

Avec l'index `idx_users_age`, le SGBD (Système de Gestion de Base de Données) peut utiliser cet index pour optimiser
l'accès aux lignes de la table `users` en fonction de la colonne `age`, réduisant ainsi le temps de traitement des
requêtes.

### Indexes spatiaux

Il existe aussi des **indexes spatiaux** (comme les R-trees dans PostGIS pour PostgreSQL) qui sont très utiles pour les
opérations géospatiales impliquant des centaines de millions de points. J'ai utilisé ces indexes dans un projet
PostGIS pour optimiser les requêtes géospatiales, telles que les recherches de proximité et les calculs d'intersection,
qui seraient autrement très coûteux en termes de temps de traitement (surtout avec des dizaines de millions de coordonnées).

Voici un exemple d'utilisation d'un index spatial pour optimiser une requête :

```sql
CREATE INDEX idx_spatial_users_location ON users USING GIST (location);

EXPLAIN ANALYZE
SELECT * FROM users
WHERE ST_DWithin(location, ST_MakePoint(-73.9866, 40.7306)::geography, 5000);
```

Créer un index spatial sur la colonne `location` permet au SGBD de traiter beaucoup plus rapidement les requêtes
impliquant des opérations géospatiales complexes.

{% note %}
Pour la suite du MON, j'ai exploré différents concepts sans forcément chercher à faire des liens entre eux.
Ce sont des mots clés, options, possibilités utiles individuellement.
{% endnote %}

## Vues

Les **vues** (mot clé `VIEW`) sont des objets de la base de données qui permettent de sauvegarder des requêtes
sous la forme d'une table virtuelle. Elles permettent de simplifier l'écriture de requête, souvent  en encapsulant 
des jointures complexes. Voici un exemple de création de vue :

```sql
CREATE VIEW users_over_25 AS
SELECT *
FROM users
WHERE age > 25;
```

Cette vue `users_over_25` peut ensuite être utilisée comme une table normale :

```sql
SELECT *
FROM users_over_25;
```

Les vues peuvent également être mises à jour si elles satisfont certaines conditions, notamment si elles référencent une
seule table.

{% note %}
Il ne faut cependant pas se faire avoir, les jointures complexes ou conditions définies dans la vue ne sont **pas**
calculées en avance, mais plutôt intégrées lors de l'exécution de la requête. De ce fait, l'utilisation de vue fait
gagner en lisibilité sans gain de performance.
{% endnote %}

### Les mots clés `WITH`

Le mot clé `WITH` est utilisé pour introduire une clause `Common Table Expressions` (CTE) qui permet de définir des
tables temporaires dont la portée est limitée à la requête dans laquelle elles sont définies. Cela peut entraîner une
meilleure lisibilité et réutilisation des requêtes complexes. Voici un exemple de CTE :

```sql
WITH UsersOver25 AS (
    SELECT *
    FROM users
    WHERE age > 25
)
SELECT *
FROM UsersOver25
WHERE name LIKE 'A%';
```

Dans cet exemple, la CTE `UsersOver25` est définie et utilisée dans la même requête pour filtrer les utilisateurs dont
le nom commence par 'A'.

Les CTE peuvent également être récursives. Voici un exemple de CTE récursive :

```sql
WITH RECURSIVE EmployeeHierarchy AS (
    SELECT employee_id, manager_id, name
    FROM employees
    WHERE manager_id IS NULL
UNION ALL
    SELECT e.employee_id, e.manager_id, e.name
    FROM employees e
    INNER JOIN EmployeeHierarchy eh ON e.manager_id = eh.employee_id
)
SELECT *
FROM EmployeeHierarchy;
```

Ce code permet de créer une hiérarchie de l'organisation des employés où chaque employé est relié à son manager.

{% lien %}
La feature est intéressante, mais pas facile à comprendre, la meilleure
explication que j'ai trouvée pour l'instant est dans une [réponse StackOverflow](https://stackoverflow.com/a/18660789).
{% endlien %}

## Procédures stockées

Les **procédures stockées** sont des sous-programmes stockés dans la base de données. Elles permettent d'exécuter des
suites d'instructions de manière réutilisable et optimisée. Cette fonctionnalité n'est pas standardisée c'est pourquoi
nous allons devoir faire une disjonction de cas en fonction du SGBD.

### SQLite

SQLite ne supporte pas directement les procédures stockées. Il est plutôt encouragé de créer lesdites procédures
directement dans le programme appellant en créant des scripts.

### MySQL

La syntaxe pour créer une procédure stockée en MySQL est la suivante :

```sql
DELIMITER $$

CREATE PROCEDURE AjouterUtilisateur(IN nom VARCHAR(255), IN age INT)
BEGIN
    INSERT INTO users (name, age) VALUES (nom, age);
END$$

DELIMITER ;
```

Vous pouvez appeler cette procédure comme suit :

```sql
CALL AjouterUtilisateur('John Doe', 30);
```

Les procédures stockées peuvent accepter des paramètres d'entrée (`IN`), de sortie (`OUT`), ou des
paramètres d'entrée/sortie (`INOUT`).

### PostgreSQL

Pour créer une procédure stockée en PostgresSQL, on peut utiliser deux syntaxes :
1. `CREATE FUNCTION`
  ```sql
  CREATE FUNCTION AjouterUtilisateur(nom VARCHAR, age INTEGER)
  RETURNS VOID AS $$
  BEGIN
      INSERT INTO users (name, age) VALUES (nom, age);
  END;
  $$ LANGUAGE plpgsql;
  ```
2. `CREATE PROCEDURE` *introduite à partir de la version 11*
  ```sql
  CREATE PROCEDURE AjouterUtilisateur(nom VARCHAR, age INTEGER)
  LANGUAGE SQL
  AS $$
  INSERT INTO users (name, age) VALUES (nom, age);
  $$;
  ```

Pour appeler cette fonction, on utilise :

```sql
SELECT AjouterUtilisateur('Jane Doe', 25);
```

Les fonctions peuvent retourner différentes valeurs types (par exemple, `VOID`, `TABLE`, etc.)
et prennent en charge un large éventail de langages de programmation via des langages procéduraux comme `plpgsql`.

## Bibliographie

{% lien %}
- [W3Schools SQL Quickref](https://www.w3schools.com/sql/sql_quickref.asp)
  *documentation plutôt détaillée de tout un tas de fonctionnalités SQL*
- [GeeksForGeeks](https://www.geeksforgeeks.org)
  *bon site regroupant tutoriels et explications (pas seulement pour SQL)*
- [Doc MySQL 9.0](https://dev.mysql.com/doc/refman/9.0/en/)
  *je la trouve plus facile à naviguer que les deux autres*
- [Doc SQLite](https://www.sqlite.org/docs.html)
- [Doc PostgresSQL 16.4](https://www.postgresql.org/docs/current/index.html)
- [Writing My Own Database From Scratch - Tony Saro](https://www.youtube.com/watch?v=5Pc18ge9ohI) 
  *vidéo extrêmement enrichissante sur les détails techniques des SGBD*
{% endlien %}

## Concepts à approfondir
- [Window Functions](https://dev.mysql.com/doc/refman/8.4/en/window-functions-usage.html)
- [Temporal Tables (SQL Server)](https://sqlspreads.com/blog/temporal-tables-in-sql-server/)
  *J'en ai entendu parler lors de mon premier stage, le concept a l'air sacrément utile*
- [FULLTEXT Search](https://dev.mysql.com/doc/refman/8.4/en/fulltext-search.html)
  *Permet de créer un index sur des données textuelles pour faire de la recherche rapide*

