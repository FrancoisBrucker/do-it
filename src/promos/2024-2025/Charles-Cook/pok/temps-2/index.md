---
layout: layout/pok.njk

title: "Gestion, analyse et présentations de données"
authors:
  - Charles Cook

date: 1971-01-01

tags: 
  - "temps 2"

résumé: L'objectif de ce POK est d'apprendre comment on nettoie et on gère de la donnée, mais également de montrer comment on présente et traite cette donnée.
---

{% prerequis %}

Aucun pré-requis

{% endprerequis %}
{% lien %}

- [Cours SQL](https://www.w3schools.com/sql/default.asp)
- [Base de données : Villes de France](https://sql.sh/exercices-sql/villes-de-france)
- [data.gouv](https://www.data.gouv.fr/fr/organizations/534fff99a3a7292c64a78016/#/datasets)

{% endlien %}

Lors de mes stages, j'ai pu constater que les données constituent un atout majeur pour une entreprise. Les données vont permettre de pouvoir faire une analyse des performances de l'entreprise, mais également de faire des prévisions afin d'ajuster les processus. L'enjeu majeur que constituent les données est également visible lorsque celles-ci sont incomplètes ou erronées, faussant voir paralysant certaines analyses et donc processus. C'est pourquoi j'ai décidé de m'intéresser à la gestion, la manipulation, l'analyse et la présentation de données. Ce sujet est très vaste mais je vais le découper en sous-thématiques : 
- Manipulation et navigation de bases de données relationnelles (SQL)
- Création d'une base de données et analyse de son contenu en SQL

## Tâches

### Sprints

Le but final est la compréhension de la gestion des données, depuis la création d'une base de données, jusqu'à l aprésentation de celles-ci, en passant par leur analyse.

#### Sprint 1

- [x] Apprentissage du langage SQL pour naviguer au sein d'une base de données
- [x] Application à une base de données
- [x] Création d'une base de données
- [x] Analyse et tests sur la données de cette table

#### Sprint 2

- [ ] Apprentissage d'une méthode d'analyse de données (Python ?)
- [ ] Application afin d'analyser les données d'une table
- [ ] Présentation de cette données



### Horodatage

| Date | Heures passées | Indications |
| -------- | -------- |-------- |
| Mardi 12/11  | 1H  | Apprentissage SQL |
| Mercredi 13/11 AM | 2H15  | Apprentissage SQL |
| Mercredi 13/11 PM | 1H45  | Application aux villes de France |
| Jeudi 14/11 AM | 2H  | Création d'une base de données pour les JO (une tentative a été faite pour la réaliser seul, mais le temps de mise en forme était trop important, je me suis donc rabattu sur une base de données gouvernementale existante pour laquelle la mise en forme était plus rapide) |
| Jeudi 14/11 PM | 1H30 | Manipulation de la base de données créée et définition des questions d'analyse |
| Vendredi 15/11 PM | 1H45  | Réponses aux questions d'analyse |
| Samedi 16/11 PM | 1H  | Rédaction Sprint 1 |
| Dimanche 17/11 PM | 1H  | Rédaction Sprint 1 |



## Premier Sprint
### Gestion de bases de données et de tables en SQL

*Afin d'illustrer les différentes fonctions que nous allons présenter, nous utiliserons deux tables :*
- *villes_france_free* comprenant les villes de France et leurs informations (nom, numéro de département, canton, population en 1999, 2010 et 2012, densité, longitude et latitude, surface,...).
- *departement* comprenant les départements de France et leurs numéros associés. 
#### Extraire des données d'une table
Afin d'extraire des données d'une base de données relationnelle, on utilise des fonctions SQL : 
| Fonction  | Explications     |
|-------------|----------------|
| ```SELECT``` | Renvoie une sous table contenant les éléments selectionnés |
| ```DISTINCT``` | Retourne seulement les valeurs uniques |
| ```WHERE``` | Permet de réaliser un filtre |
| ```ORDER BY``` | Permet de trier les lignes extraites |
| ```GROUP BY``` | Permet de grouper les données par catégories |
| ```LIKE``` | Utilisé dans un WHERE, pour spécifier ce que l’on cherche |
| ```IN``` | Permet de spécifier plusieurs caractères dans un même WHERE |
| ```BETWEEN``` | Sélectionne les valeurs comprises dans une plage de valeurs donnée |
| ```AS``` | Crée un alias donnant à une table ou une colonne un nom temporaire, tant que la requête est en cours |

**Quelles sont les villes du Vaucluse (84) ?**

{%details "Code et Résultats" %}

**Code**
```
SELECT * FROM villes_france_free WHERE ville_departement=84;
```
Ce code permet de créer un table temporaire des villes vauclusiennes dans l'odre alphabétique.

**Résultats**
![Villes Vaucluse Triées](<Images/Villes Vaucluse Triées.png>)

{%enddetails%}

| Fonction  | Explications     |
|-------------|----------------|
| ```AND``` | Combine plusieurs conditions pour réaliser une intersection |
| ```OR``` | Combine plusieurs conditions pour réaliser une réunion |
| ```NOT``` | Permet de réaliser une exclusion |
| ```LIMIT``` | Permet de préciser le nombre de lignes que l'on veut extraire |
| ```UNION``` | Permet de combiner les résultats de deux ou plusieurs instructions ```SELECT``` |

**Quelles sont les 10 villes les moins peuplées de France en 2012 ?**

{%details "Code et Résultats" %}

**Code**
```
SELECT * FROM villes_france_free
ORDER BY ville_population_2010 ASC
LIMIT 10;
```
Ce code permet d'extraire les 10 villes les moins peuplées, dans l'ordre croissant du nombre d'habitants.

**Résultats**
![TOP 10 villes les moins peuplées](<Images/TOP 10 des villes les moins peuplées en 2010.png>)

{%enddetails%}

##### Fonctions d'aggrégation
Une fonction d'aggrégation est une fonction qui réalise des calculs sur un groupe de données et qui renvoie une valeur unique. 

| Fonction  | Explications     |
|-------------|----------------|
| ```MAX``` | Renvoie la plus grande valeur d'une colonne |
| ```MIN``` | Renvoie la plus petite valeur d'une fonction |

**Quelles est la population de la ville la plus peuplée du Vaucluse (84) ?**

{% details "Code et Résultats" %}

**Code**
````
SELECT MAX(ville_population_2012)
FROM villes_france_free
WHERE ville_departement=84;
````

**Résultats**
Cette requête renvoie 90100, correspondant à la population d'Avignon en 2012.

{%enddetails%}

| Fonction  | Explications     |
|-------------|----------------|
| ```COUNT``` | Renvoie le nombre de ligne de la table qui respectent un critère donné |
| ```SUM``` | Renvoie la somme d'une colonne spécifiée |
| ```AVG``` | Renvoie la moyenne |
| ```HAVING``` | Permet de mettre une condition sur les lignes que l’on extrait avec des fonctions d’aggrégation (car WHERE ne le permet pas) |

**Combien de villes en France possède un nom débutant par 'Saint' ?**

{%details "Code et Résultats" %}

**Code**
````
SELECT COUNT(ville_nom)
FROM villes_france_free
WHERE ville_nom LIKE 'SAINT%';
````

**Résultats**
Cette requête renvoie 4260, ce qui signifie que 4260 villes commencent par 'Saint' en France.

{%enddetails%}

**Quels sont les noms de ville donnés plusieurs fois, du plus au moins rare ?**

{%details "Code et Résultats"%}

**Code**
````
SELECT ville_nom AS 'NOM VILLE', COUNT(ville_nom) AS 'NOMBRE DE VILLE'
FROM villes_france_free
GROUP BY ville_nom
HAVING COUNT(ville_nom)>1
ORDER BY COUNT(ville_nom) DESC;
````

**Résultats**
![Doublons noms de villes](<Images/Doublon noms de ville.png>)

La première colonne donne les noms de ville donnés plusieurs fois et la seconde fait apparaître combien de fois le nom a été donné.

{%enddetails%}

#### Modifier une table
Il peut être nécessaire de modifier les données d'une table afin de la mettre à jour. Plusieurs fonctions peuvent être utiles : 

##### Ajouter des données
| Fonction  | Explications     |
|-------------|----------------|
| ```INSERT INTO``` | Permet d'ajouter une ligne dans une table |

La syntaxe à adopoter est dans ce cas la suivante : 
````
INSERT INTO nom_de_la_table (colonne 1, colonne 2, colonne 3, ...)
VALUES 
(Value 1.1, Value 1.2, Value 1.3, ...),
(Value 2.1, Value 2.2, Value 2.3, ...);
````
*NB: Si on ajoute une valeur pour chaque colonne, il n’est pas nécessaire de préciser le nom de chaque colonne dans les parenthèses après le nom de la table, mais il faut bien respecter l’ordre des données.*

**Ajouter la ville de New-York à la table *villes_france_free.***

{%details "Code et Résultats" %}
**Code**
Afin d'ajouter une ligne pour la ville de New-York dans la table *villes_france_free*, le code est le suivant : 
````
INSERT INTO villes_france_free(ville_id,ville_code_commune,ville_nom) VALUES(000, 000, 'NEW YORK');
SELECT * FROM villes_france_free;
````

**Résultats**
![Ajout NY](<Images/Ajout NEW YORK.png>)

On remarque qu'une ligne a été ajouté à la fin de la table, pour la ville de New-York.

{%enddetails%}

###### Supprimer des données
| Fonction  | Explications     |
|-------------|----------------|
| ```DELETE``` | Permet de supprimer un élément, une ligne ou même tous les éléments d'une table |

***Exemple** : Supprimer tous les éléments de la table **villes_france_free** se ferait avec la requête ```DELETE FROM villes_france_free;```*

| Fonction  | Explications     |
|-------------|----------------|
| ```DROP TABLE``` | Permet de supprimer une table (pas seulement son contenu) |

##### Modifier des données
| Fonction  | Explications     |
|-------------|----------------|
| ```UPDATE``` | Mise à jour de la donnée |

**Mise à jour des données concernant la population de New-York**

{%details "Code et Résultats" %}

**Code**
```
UPDATE villes_france_free 
SET ville_population_2012=8347000, ville_population_2010=819000, ville_population_1999=7428000
WHERE ville_nom='NEW YORK';
```
Ce code permet de mettre à jour la ligne de la ville de New-York avec les populations en 1999, 2010 et 2012. 

{%enddetails%}

#### Combiner plusieurs tables
En entreprise, tous les employés n’ont pas accès à toutes les données, certaines étant classifiée sensibles. Ainsi, différentes bases de données (ou tables) peuvent être crées avec des niveaux de confidentialité différents. Afin d’extraire des données complètes, il peut être utile d’extraire des données provenant de différentes tables, c’est-ce qu’on appelle des jointures.

##### Jointures
Il existe différents types de jointure :
-   (INNER) JOIN : renvoie les lignes ayant correspondances dans les deux tables
-   LEFT (OUTER) JOIN : renvoie toutes les lignes de la table de gauche, et les données correspondantes dans la table de droite 
-   RIGHT (OUTER) JOIN : renvoie toutes les lignes de la table de droite, et les données correspondantes dans la table de gauche
-   FULL (OUTER) JOIN : renvoie toutes les lignes quand il y a une correspondance dans la table de gauche ou de droite
-   SELF JOIN : réalise une jointure d’une table avec elle-même

![Types de jointures](<Images/types de jointures.png>)
*[Source : w3schools](https://www.w3schools.com/sql/sql_join.asp)*

**Dans notre exemple, nous avons dans la table *villes_france_free* les départements uniquement renseignés par numéro. Nous allons tenter de réaliser une jointure avec la table *departement* pour renseigner également le nom du département.**

{%details "Code et Résultats" %}

**Code**
````
SELECT t1.ville_departement, t1.ville_nom, t2.departement_nom
FROM villes_france_free.villes_france_free AS t1
JOIN departement.departement AS t2 
ON t1.ville_departement = t2.departement_code
ORDER BY t1.ville_nom;
````

**Résultats**
![Jointure départements](<Images/Jointure département.png>)
Le résultat ci-dessus montre que nous pouvons à présent, grâce à la jointure réalisée entre les deux tables, faire apparaître le nom complet du département auquel appartient la ville et non plus seulement son numéro.

{%enddetails%}

#### Création d'une base de données, d'une table
##### Fonctions pour créer une base de données, une table

| Fonction  | Explications     |
|-------------|----------------|
| ```CREATE DATABASE``` | Création d'une base de données |
| ```CREATE TABLE``` | Création d'une table dans une base de données |
| ```DROP DATABASE``` | Suppression d'une base de données |
| ```DROP TABLE``` | Suppression d'une table dans une base de données |
| ```ALTER TABLE``` | Permet de modifier une table, en ajoutant une colonne, supprimant une colonne, modifiant le type de donnée d’une colonne, changer le nom du colonne |

##### Contraintes
Il est possible d’ajouter des contrainte sur une colonne lors de la création d’une table. Les contraintes possibles sont les suivantes :
| Contrainte  | Explications     |
|-------------|----------------|
| ```NOT NULL``` | Permet de s’assurer qu’une colonne ne possède pas de valeur ```NULL``` |
| ```UNIQUE``` | Permet de s’assurer que toutes les valeurs d’une colonne sont différentes |
| ```PRIMARY KEY``` | Une combinaison de ```NOT NULL``` et ```UNIQUE``` |
| ```FOREIGN KEY``` | Prévient des actions qui détruirait les liens entre différentes tables |
| ```CHECK``` | S’assure que les valeurs d’une colonne respectent bien une condition donnée |
| ```DEFAULT``` | Attribue une valeur par défaut pour une colonne si aucune valeur n’est spécifiée |

#### Application : Création et analyse du contenu d'une base de données
Nous allons tenter de créer une base de données afin de pouvoir réaliser une manipulation des données en langage SQL. Pour cela, nous allons nous intéresser aux médailles remportées par pays, durant les jeux Olympiques d'hiver entre 1924 et 2010. Pour cela, nous allons tout d'abord créer un base de données et un table vide.

##### Création de la base de données et la table 
Nous allons créer une base de données intitulée *winter_medals*, dans laquelle nous allons créer une table *medals* contenant les informations suivantes :
- Identifiant *id*
- Année de l'édition pendant laquelle la médaille a été obtenue, *years*
- Nom de la discipline, *sport*
- La couleur de la médaille, *medal*
- Le code du pays, *country*
- Le nom complet du pays, *pays*
- un boolen indiquant si le pays accueillait les jeux lorsqu'il a obtenu la médaille ou non, *host*

{%details "Code" %}
````
CREATE DATABASE winter_medals;
CREATE TABLE medals (
    id INT,
    years INT,
    sport VARCHAR(255),
    medal VARCHAR(255),
    country VARCHAR(255),
    pays VARCHAR(255),
    host VARCHAR(255)
);
````
On voit que pour chaque colonne créée, on précise le type de données qu'elle contient.

{%enddetails%}

##### Chargement des données
Afin de récolter les données, j'ai utilisé le site [Data Gouv](https://www.data.gouv.fr/fr/organizations/534fff99a3a7292c64a78016/#/datasets) permattant d'accéder à un certain nombre de données. J'ai ensuite modifié quelques typographies sur Excel afin de pouvoir charger les données dans la table *medals*

{%details "Code" %}
````
INSERT INTO medals (id, years, sport, medal, country, pays, host) VALUES
(131666,1924,'biathlon','gold','SUI','Switzerland','FALSE'),
(231666,1924,'biathlon','silver','FIN','Finland','FALSE'),
(331666,1924,'biathlon','bronze','FRA','France','TRUE'),
(431666,1960,'biathlon','gold','SWE','Sweden','FALSE'),
(531666,1960,'biathlon','silver','FIN','Finland','FALSE'),
(631666,1960,'biathlon','bronze','URS','USSR','FALSE'),
(731666,1964,'biathlon','gold','URS','USSR','FALSE'),
(831666,1964,'biathlon','silver','URS','USSR','FALSE'),
(931666,1964,'biathlon','bronze','NOR','Norway','FALSE'),
[…]
(256732514,2010,'snowboard','silver','RUS','Russian Federation','FALSE'),
(256832514,2010,'snowboard','bronze','AUT','Austria','FALSE'),
(256932514,2010,'snowboard','gold','CAN','Canada','TRUE'),
(257032514,2010,'snowboard','silver','FRA','France','FALSE'),
(257132514,2010,'snowboard','bronze','SUI','Switzerland','FALSE');
````
{%enddetails%}

On obtient ainsi une table contenant 2571 lignes. 

On remarque que le la colonne id est en fait une clé primaire, dont les 5 derniers chiffres renvoient au type d’épreuve, et les chiffres avant correspond au numéro de la ligne. Il est donc intéressant de changer le type de la première colonne pour indiquer que c’est une clé primaire : 
```
ALTER TABLE medals ADD PRIMARY KEY (id);
```

##### Etude des données
Grâce à la création de cette base de données, nous allons pouvoir répondre de manière plus simple aux questions suivantes, qui nous permettent de débuter une analyse de la donnée :
- Q1 : Quel est le tableau des médailles pour l'ensemble des éditions de 1924 à 2010 ?
- Q2 : Quel pays est en tête du classement des médailles par édition ?
- Q3 : Quel est le classement dans le tableau des médailles de chaque pays par édition ?
- Q4 : Sur l'ensemble des éditions entre 1924 et 2010, quel pays est le meilleur dans chaque discipline ?
- Q5 : La performance du pays organisateur (en terme de nombre de médailles) est elle supérieur que lorsque le même pays n'est pas organisateur ?

###### Question 1 : Quel est le tableau des éditions entre 1924 et 2010, quel pays est le meilleur dans chaque discipline ?

Lors des JO, les pays sont classés selon un *tableau des médailles*, classant les pays en fonctions du nombre de médailles d'or, puis de médailes d'argent, et enfin de médailles de bronze.

{%details "Code" %}

**Code**
````
SELECT pays AS 'Pays',
       COUNT(medal) AS 'Total Médailles',
       SUM(CASE WHEN medal = 'GOLD' THEN 1 ELSE 0 END) AS 'GOLD',
       SUM(CASE WHEN medal = 'SILVER' THEN 1 ELSE 0 END) AS 'SILVER',
       SUM(CASE WHEN medal = 'BRONZE' THEN 1 ELSE 0 END) AS 'BRONZE'
FROM medals
GROUP BY pays
ORDER BY GOLD DESC, SILVER DESC, BRONZE DESC;
````
**Explication du code**
Cette requête crée une table en faisant apparaître 5 colonnes : 
- Une colonne *Pays*
- Une colonne comprenant le somme totale de médailles par pays (*Total Médailles*)
- Une colonne par couleur de médaille, totalisant le nombre de médailles de chaque couleur par pays (*GOLD*, *SILVER* et *BRONZE*)

Les lignes sont quant à elles classées en fonction du nombre de médailles d'or, puis d'argent, puis de bronze.

{%enddetails%}

Le résultat de la requête est donc le tableau des médailles suivant, réalisé sur l'ensemble des médailles reçues lors des éditions de 1924 à 2010 : 
![Tableau des médailles](<Images/Tableau des médailles.png>)

###### Question 2 : Quel pays est en tête du classement des médailles par édition ?

Nous avons réalisé un tableau des médailles sur l'ensemble des éditions entre 1924 et 2010, mais il est intéressant d'extraire le pays en tête du classement lors de chacune des éditions. 

{%details "Code" %}

**Code**
````
SELECT m.years AS 'Année', m.pays AS 'Meilleur Pays', m.nombre_or AS 'Nombre de Titres'
FROM (
    SELECT years, pays,
           SUM(CASE WHEN medal = 'GOLD' THEN 1 ELSE 0 END) AS nombre_or
    FROM medals
    GROUP BY years, pays
) AS m
JOIN (
    SELECT years, MAX(nombre_or) AS max_or
    FROM (
        SELECT years, pays,
               SUM(CASE WHEN medal = 'GOLD' THEN 1 ELSE 0 END) AS nombre_or
        FROM medals
        GROUP BY years, pays
    ) AS subquery
    GROUP BY years
) AS max_counts ON m.years = max_counts.years AND m.nombre_or = max_counts.max_or
ORDER BY m.years;
````
**Explication du code**
Ce code réalise la jointure de deux sous tables :
- La première nommée *m* est un table comprenant 3 colonnes, donnant le nombre de médailles d'or obtenu par chaque pays à chaque édition des JO d'hiver.
- La seconde, nommée *max_counts* est une extraction de la première sous-table dans laquelle on conserve seulement la valeur maximum de nombre de médailles d'or par année.

En réalisant une jointure sur les années, on obtient ainsi le résultat ci-dessous.

{%enddetails%}

On obtient ainsi le table suivante, donnant le meilleur pays par année en nombre de titre (médailles d'or) :
![Meilleur pays par année](<Images/Meilleur payspar année.png>)
*Remarque : On pourrait être plus précis en prenant en compte égalelement le nombre de médailles d'argent et de bronze*

###### Question 3 : Quel est le classement dans le tableau des médailles de chaque pays par édition ?

Toujours afin d'étudier les performances des pays par édition, nous pouvons essayer d'extraire le classement dans le tableau des médailles par année.

{%details "Code" %}

**Code**
````
WITH classement AS (
    SELECT pays AS 'Pays',
           years AS 'Année',
           RANK() OVER (
               PARTITION BY years
               ORDER BY 
                   SUM(CASE WHEN medal = 'GOLD' THEN 1 ELSE 0 END) DESC,
                   SUM(CASE WHEN medal = 'SILVER' THEN 1 ELSE 0 END) DESC,
                   SUM(CASE WHEN medal = 'BRONZE' THEN 1 ELSE 0 END) DESC
           ) AS 'Classement'
    FROM medals
    GROUP BY years, pays
)
SELECT Pays, Année, Classement
FROM classement
ORDER BY Pays, Année;
````

**Explication du code**
Cette requête crée une sous-table *classement* créant un classement des médailles comme vu précédemment (Question 1), puis extrait le rang de chaque pays par année. 

Le résultat obtenu, trié par Pays et par Année, est ci-dessous.

{%enddetails%}

Le résultat obtenu est le suivant :
![Classement par année](<Images/Classement des médailles par année.png>)

###### Question 4 : Sur l'ensemble des éditions entre 1924 et 2010, quel pays est le meilleur dans chaque discipline ?

La base de données nous permet également de pouvoir réaliser une étude sur le pays le meilleur (en nombre de titre) en fonction du sport. 

{%details "Code" %}

**Code**
````
SELECT m.sport AS 'Discipline', m.pays AS 'Meilleur Pays', m.nombre_or AS 'Nombre de Titres'
FROM (
    SELECT sport, pays,
           SUM(CASE WHEN medal = 'GOLD' THEN 1 ELSE 0 END) AS nombre_or
    FROM medals
    GROUP BY sport, pays
) AS m
JOIN (
    SELECT sport, MAX(nombre_or) AS max_or
    FROM (
        SELECT sport, pays,
               SUM(CASE WHEN medal = 'GOLD' THEN 1 ELSE 0 END) AS nombre_or
        FROM medals
        GROUP BY sport, pays
    ) AS subquery
    GROUP BY sport
) AS max_counts ON m.sport = max_counts.sport AND m.nombre_or = max_counts.max_or
ORDER BY m.sport;
````
**Explication du code**
La méthode utilisée pour cette question est la même que pour la question 2, en remplaçant les années par les disciplines.

{%enddetails%}

On obtient ainsi la table suivante : 
![Meilleur par discipline](<Images/Meilleure pays dans chaque discipline.png>)

###### Question 5 : La performance du pays organisateur (en termes de nombre de médailles) est-elle supérieur que lorsque le même pays n'est pas organisateur ?

Lors de différents évènements sportifs, il existe un match aller, et un match retour. Ceci est organisé car lorsqu'une équipe joue à domicile, ses performances sont souvent meilleures. Il est donc intéressant de regarder si ce phénomène est visible dans les résultats des différents pays aux JO d'hiver. 

{%details "Code" %}

**Code et explication**

Table donnant le nombre de médailles obtenu par un pays qlorsqu'il n'est pas organisateur :
````
SELECT pays AS 'Pays', COUNT(medal) AS 'Nombre_Médailles'
FROM medals
WHERE host = 'FALSE'
GROUP BY pays
ORDER BY pays;
````

Table donnant le nombre de fois qu'un pays a organisé les jeux d'hiver et le nombre de médailles récoltées lors de ces éditions :
````
SELECT pays AS 'Pays',
       COUNT(years) AS 'Nombre_Organisateur',
       SUM(nombre_medaille) AS 'Total_Médailles'
FROM (
    SELECT years, pays, COUNT(medal) AS nombre_medaille
    FROM medals
    WHERE host = 'TRUE'
    GROUP BY years, pays
    ORDER BY years
) AS sous_requete
GROUP BY pays
ORDER BY 'Nombre Organisateur' DESC;
````

Ainsi, avec ces deux tables, nous pouvons obtenir une table donnant pas pays organisateur, le nombre de médailles obtenues à domicile, le nombre de médailles obtenues à l'extérieur, et le nombre de fois que chaque pays a organisé les JO d'hiver :

````
SELECT not_host.Pays AS Pays, not_host.Nombre_Médailles AS medailles_ext, host.Nombre_Organisateur AS Nbre_orga, host.Total_Médailles AS medailles_dom
FROM(
    SELECT pays AS 'Pays', COUNT(medal) AS 'Nombre_Médailles'
    FROM medals
    WHERE host = 'FALSE'
    GROUP BY pays
    ORDER BY pays) AS not_host
JOIN (
    SELECT pays AS 'Pays',
       COUNT(years) AS 'Nombre_Organisateur',
       SUM(nombre_medaille) AS 'Total_Médailles'
    FROM (
        SELECT years, pays, COUNT(medal) AS nombre_medaille
        FROM medals
        WHERE host = 'TRUE'
        GROUP BY years, pays
        ORDER BY years
    ) AS sous_requete
    GROUP BY pays
    ORDER BY 'Nombre Organisateur' DESC) AS host
ON not_host.Pays=host.Pays;
````
Finalement, en notant que la base de données recouvre les 21 éditions entre 1924 et 2010, on peut calculer les nombres moyens de médailles reçues à domicile et à l'extérieur par pays : 
````
SELECT Pays,
    ROUND(medailles_dom/Nbre_orga,1) AS Moyenne_médailles_domicile,
    ROUND(medailles_ext/(21-Nbre_orga),1) AS Moyenne_médailles_extérieur
FROM(
    SELECT not_host.Pays AS Pays, not_host.Nombre_Médailles AS medailles_ext, host.Nombre_Organisateur AS Nbre_orga, host.Total_Médailles AS medailles_dom
    FROM(
        SELECT pays AS 'Pays', COUNT(medal) AS 'Nombre_Médailles'
        FROM medals
        WHERE host = 'FALSE'
        GROUP BY pays
        ORDER BY pays) AS not_host
    JOIN (
        SELECT pays AS 'Pays',
        COUNT(years) AS 'Nombre_Organisateur',
        SUM(nombre_medaille) AS 'Total_Médailles'
        FROM (
            SELECT years, pays, COUNT(medal) AS nombre_medaille
            FROM medals
            WHERE host = 'TRUE'
            GROUP BY years, pays
            ORDER BY years
        ) AS sous_requete
        GROUP BY pays
        ORDER BY 'Nombre Organisateur' DESC) AS host
    ON not_host.Pays=host.Pays) AS under_query;
````
{%enddetails%}

Le résultat obtenu est la table suivante : 
![Moyenne médailles](<Images/Moyenne Médailles dom-ext.png>)

On remarque à l'aide de cette table que pour la totalité des pays ayant organisé les JO d'hiver (excepté pour la Suisse et l'Allemagne), les performances à domicile sont, au pire, égales à celles à l'extérieur, mais pour la plupart, les performances à domicile sont significativement meilleures (en termes de nombre total de médailles obtenues).

### Conclusion Sprint 1
Ce premier sprint nous a permis de comprendre comment créer une base de données relationnelles et comment extraire des tables afin de réaliser les prémices d'une analyse de données en SQL. Cependant, le langage SQL n'est pas le plus adapté pour réaliser de l'analyse de données. Nous explorerons plus en profondeur ceci lors du second sprint.

### Second Sprint
Pour explorer l'analyse de données, nous allons nous appuyer sur les bibliothèques suivantes : 
- Pandas
- Matplotlib (afin de tracer des figures)
- Seabron (une autre bibliothèque permettant de tracer des figures, que j'ai découvert un peu plus tard, mais qui est plus intuitive selon moi)

#### Mise en contexte
L'objectif de ce second sprint est de manipuler une base de données et de "la faire parler". Pour cela, nous nous placerons dans la peau d'un jeune musicien, qui énormément de talent mais qui peine à trouver de l'inspiration pour créer son premier morceau. Son objectif est de devenir viral très rapidement, avec une musique populaire. Pour cela, nous allons utiliser une base de données contenant plus de 60 000 morceaux recencés, et dont les caractéristiques suivantes sont rensignées : 
- track_id: Spotify ID pour le morecau.
- track_name: Nom du morceau.
- artist_name: Noms des artistes ayant travaillés sur le morceau, séparés par une virgule s'il y en a plusieurs.
- year: L'année de sortie du morceau.
- popularity: indice de popularité entre 0 et 100, basé sur le nombre d'écoute et si le morceau et récent ou non.
- artwork_url: URL du morceau.
- album_name: L'album dans lequel le morceau apparaît.
- acousticness: Un indice entre 0.0 et 1.0 montrant à quel point le morceau est acoustique. 
- danceability: Indice de dansibilité du morceau (0.0 = moins dansable, 1.0 = plus dansable).
- duration_ms: Longueur du morceau en millisecondes.
- energy: Un indice entre 0.0 et 1.0 d'énregie. 
- key: La clé musicale du morceau.
- liveness: Une mesure indiquant la probabilité qu'un morceau soit enregistré live.
- loudness: Le nivau sonore du morceau (dB).
- mode: Indique le mode du morceau (1 = major, 0 = minor).
- speechiness: Mesure la présence de mot parlé dans le morceau (proche de 1.0 signifie la présence importante de mots parlés).
- tempo: Le tempo estimé du morceau en bpm.
- time_signature: Le nombre de battement par minute, de 3 à 7.
- valence: Un indice de 0.0 à 1.0 mesure la positivité d'un morceau.
- track_url: L'URL Spotify pour le morceau.
- language: Langue des paroles du morceau (English, Tamil, Hindi, Telugu, Malayalam, Korean).

#### Analyse
Nous allons réaliser une analyse sur les thématiques suivantes : langue, positivité (valence), dansabilité, énergie

##### Comment la popularité des morceaux varie-t-elle en fonction des langues ?

Le premier objectif est d'estimer quelle langue permettra d'obtenir la plus grande popularité. Pour cela, nous allons estimer la popularité moyenne par langue. 

{%details "Code" %}
````
fig, ax = plt.subplots()
popularity_by_language = spotify_tracks.groupby("language")["popularity"].mean()
popularity_by_language.plot.bar(
    ax=ax,
    title="Popularité en fonction de la langue",
    xlabel="Langues",
    ylabel="Indice de popularité",
)
plt.show()
````
{%enddetails%}

Le résultat obtenu est le suivant : 

![Popularité moyenne par langue V1](<Images/Capture d’écran 2024-12-12 à 16.33.56.png>)

On remarque que le Coréen est la langue avec le plus grand indice de popularité moyen, suivi par le Hindi. Pourtant, l’anglais étant la langue la plus parlé au monde, il est surprenant de voir ce résultat. Nous allons donc approfondir la recherche afin de s'assurer de la cohérence du résultat.

Penchons nous sur le nombre de morceaux par langue : 

{%details "Code" %}
```
fig, ax = plt.subplots()
repartition_language = spotify_tracks['language'].value_counts()
repartition_language.plot.bar(
    ax=ax,
    title="Nombre de morceaux par langue",
    xlabel="Langues",
    ylabel="Nombre de morceaux",
)

plt.tight_layout() #Afin que tous les titres soient bien visibles
plt.show()
```
{%enddetails%}

On obtient les résultats suivants : 

![Nombre de morceaux par langue](<Images/Capture d’écran 2024-12-12 à 17.16.30.png>)

On observe alors que les morceaux en anglais sont beaucoup plus nombreux que les morceaux en Coréen ou Hindi. Il peut y aoir ainsi une fausseté dans la représentativité des données (la présence que de morceaux coréens populaires par exemple). Analysons ainsi l'écart type pour vérifier cette théorie : 

{%details "Code" %}
````
fig, ax = plt.subplots(figsize=(8, 6))
popularity_by_language = spotify_tracks.groupby('language')['popularity'].agg(['mean', 'std'])
popularity_by_language['mean'].plot.bar(
    yerr=popularity_by_language['std'],
    capsize=4,
    ax=ax,
    title="Popularité moyenne par langue et écart type",
    xlabel="Langues",
    ylabel="Indice de popularité moyenne",
)

plt.tight_layout() #Afin que tous les titres soient bien visibles
plt.show()
````
{%enddetails%}

On obtient le graphe suivant : 

![Ecart type popularité langue](<Images/Capture d’écran 2024-12-12 à 17.07.33.png>)

On remarque ainsi au travers de l’écart type des musiques coréennes par exemple que les musiques sélectionnées ont toutes un niveau de popularité assez élevé. Ceci fausse l’analyse. Nous allons donc explorer deux hypothèses afin de minimiser cet effet sur les résultats. 

**Hypothèse 1 :** prendre seulement les morceaux avec un indice de popularité supérieur à 50 :

{%details "Code" %}
````
popular_tracks = spotify_tracks[spotify_tracks['popularity'] > 50]
fig, ax = plt.subplots()
popularity_by_language = popular_tracks.groupby("language")["popularity"].mean()
popularity_by_language.plot.bar(
    ax=ax,
    title="Popularité en fonction de la langue",
    xlabel="Langues",
    ylabel="Indice de popularité",
)

plt.tight_layout() #Afin que tous les titres soient bien visibles
plt.show()
````
{%enddetails%}

![Hypothèse 1 popularité](<Images/Capture d’écran 2024-12-12 à 17.29.48.png>)

On note alors des résultats différents dans lesquels, parmi les morceaux ayant déjà un indice de popularité assez élevé, les morceaux en anglais sont les plus populaires.

**Hypothèse 2 :** prendre les 2000 musiques les plus populaires par langue :

{%details "Code" %}
````
top_2000 = spotify_tracks.groupby('language').apply(lambda x: x.nlargest(2000, 'popularity'))
top_2000_reset = top_2000.reset_index(drop=True) #Afin d'éliminer l'erreur due à l'ambiguité de 'language' en tant que colonne et indice

fig, ax = plt.subplots()
popularity_by_language = top_2000_reset.groupby('language')['popularity'].mean()
popularity_by_language.plot.bar(
    ax=ax,
    title="Popularité en fonction de la langue",
    xlabel="Langues",
    ylabel="Indice de popularité",
)

plt.tight_layout() #Afin que tous les titres soient bien visibles
plt.show()
````
{%enddetails%}

![Hypothèse 2 popularité](<Images/Capture d’écran 2024-12-12 à 17.44.12.png>)

Cette seconde hypothèse corrobore les résultats de l'hypothèse 1, en montrant que parmi les musiques les plus populaires par langue, les musiques en anglais ont un indice moyen de popularité plus élevé que les autres langues.

##### Quel est le rapport entre la valence (positivité) et la dansabilité ?

En tant qu'artiste, on souhaite savoir si un morceau dansable est forcément positif. 

Pour cela, nous allons tracer la reggression permettant de mettre en lumière un éventuel lien entre ce deux éléments.

{%details "Code" %}
````
sns.regplot(x=spotify_tracks['danceability'], y=spotify_tracks['valence'], line_kws={'color': 'black'})

plt.title("Lien entre la dansabilité et la positivité")
plt.xlabel("Indice de dansabilité")
plt.ylabel("Indice de positivité")

plt.xlim(0, 1)
plt.ylim(0, 1)

plt.tight_layout()

plt.show()
````
Ce code est écrit avec Seaborn, car je trouve la rédaction plus intuitive. Dans la suite de la rédaction, nous alternerons entre Seaborn et MatplotLib lorsque l'on ne peut pas utiliser Seaborn.
{%enddetails%}

Le résultat obtenu est le suivant : 

![Lien entre la positivité et la dansabilité](<Images/Capture d’écran 2024-12-12 à 18.13.00.png>)

On remarque une tendance avec ce graphique : l'indice de positivité semble augmenter avec l'indice de dansabilité. Ainsi, on peut admettre qu'un morceaux positif est de manière générale plus dansant. 

##### Existe-il un rapport entre la dansabilité et la popularité d’un morceau de musique ?

On cherche alors à savoir s'il est plus intéressant de composer un morceau dansant pour devenir populaire. 

{%details "Code" %}
````
sns.regplot(y=spotify_tracks['popularity'], x=spotify_tracks['danceability'], line_kws={'color': 'black'})

plt.title("Lien entre la dansabilité et la popularité")
plt.ylabel("Indice de popularité")
plt.xlabel("Indice de dansabilité")


plt.tight_layout()

plt.show()
````
{%enddetails%}

Le résultat obtenu est le suivant :

![Lien entre dansabilité et popularité](<Images/Capture d’écran 2024-12-12 à 18.19.33.png>)

Le graphe précédent ne permet pas de mettre en lumière un lien évident entre l'indice de dansabilité d'un morceau et son indice de popularité. 