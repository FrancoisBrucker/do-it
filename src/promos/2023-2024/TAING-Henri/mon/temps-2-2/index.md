<!-- ---
layout: layout/mon.njk

title: "Dépoussiérer ses connaissances en SQL et Python pour l'analyse de données"
authors:
  - TAING Henri

date: 2023-10-15

tags:
  - "temps 2"
  - SQL
  - Python

résumé: "Un vieux qui reprend ce qu'il a appris dans l'espoir de faire des jolis graphes"
---

{%prerequis 'MON débutant'%}
Avoir un cerveau à moitié allumé et quelques bases pour suivre le Python
{%endprerequis%}

---

## Table des matières

1. [Introduction](#section-1)
2. [SQL débutant](#section-2)
3. [SQL intermédiaire](#section-3)
4. [Rappels sur Python et ses librairies pour l'analyse de données](#section-4)
5. [Quelques résultats et représentations à partir d'une base de données sur le Speed Dating](#section-5)
6. [Conclusion](#section-6)
7. [Sources](#section-7)

## 1. Introduction <a id="section-1"></a>

En finissant mon MON 2-1, je me suis dit "Quand même, pas de jointure sur Google Sheets, c'est audacieux, en SQL, on en faisait à l'époque. Attends, comment on fait déjà ?!"

Il est donc temps de dépoussiérer tout ça. Pour ça, j'ai décidé de réapprendre SQL par l'application en essayant de résoudre les exercices faciles et intermédiaires proposés par [sql.sh](https://sql.sh/exercices-sql), puis j'ai repris le cours d'I3 Python Scientifique de l'an dernier pour proposer de nouvelles représentations de la base de données que j'ai étudiée dans le cadre de mon projet.

## 2. SQL débutant <a id="section-2"></a>

J'ai appris le SQL à la va-vite en classes préparatoires. Ça doit être comme le vélo, non ? Ça ne s'oublie pas.

Eh bien, je me suis souvenu que j'étais nul au vélo. Heureusement, le site est bien documenté et les explications super bien ficelés.
J'ai utilisé MySQL, car c'était ce que j'utilisais en classes préparatoires.

Voici à quoi ressemble la base de données qu'on extrait à l'aide de la commande SELECT.
**Base de données sur les villes françaises**
<img src="Capture1.png">

Ci-dessous, la syntaxe classique :

```
SELECT *
FROM table
WHERE condition
GROUP BY nom_colonne
HAVING condition avec une fonction
{UNION | INTERSECT | EXCEPT}
ORDER BY DESC/ASC
LIMIT nombre
OFFSET début

```

Je vous fais part des questions que j'ai trouvé intéressantes dans le sens où elles me serviront comme fiches pour réapprendre quand je réoublierai, car je sais que ça arrivera très vite.

{% details "Q1" %}

```


```

{% enddetails %}

## 3. SQL intermédiaire <a id="section-3"></a>

**Base de données 1 sur les Miss**
<img src="graphiques.png">

**Base de données 2 sur des acteurs/célébrités**
<img src="repetition_incrementee.png">

## 4. Rappels sur Python et ses librairies pour l'analyse de données <a id="section-4"></a>

**Utilisation de filtres**
:-------------------------:|:-------------------------:
<img src="filtre.png" width="350" height="350"> | <img src="filtre2.png" width="350" height="350">
<img src="vuefiltre.png">

**Mise en forme conditionnelle avec dégradé de couleurs**
:-------------------------:|:-------------------------:
<img src="mise_en_forme_conditionnelle_2.png" width="350" height="350"> | <img src="mise_en_forme_conditionnelle_3.png" width="350" height="350">

**Graphes**
:-------------------------:|:-------------------------:
<img src="graphe1.png" width="350" height="350"> | <img src="graphe2.png" width="350" height="350">

**Tableau croisé dynamique à partir du classement des Miss- FAIL**
:-------------------------:|:-------------------------:
<img src="tableaudyn_fail.png" width="600" height="600"> | <img src="editeurtableaudyn.png" width="350" height="350">

Première chose, je suis déçu. Je pensais que la création d'un tableau croisé dynamique était un truc de malade, mais il s'agit simplement de cliquer sur deux boutons...
Deuxième chose, je me suis rendu compte que la façon avec laquelle j'ai rempli ma base de données ne convenait pas à une analyse par tableaux croisés dynamiques. Doublement déçu.

Que faire ? Refaire une base de données à la main ? Pfff. Bande de fous. QUE NENNI ! (Je regrette ce choix...)

Avec les 5 heures qu'il me reste, il est temps de voir ce qu'est App Scripts, l'équivalent du VBA :o. Va-t-il m'apporter une solution ou sera-t-il un trou sans fond de connaissances ?

## 5. Quelques résultats et représentations à partir d'une base de données sur le Speed Dating <a id="section-5"></a>

Eh bien, en fait. App Scripts, c'est un langage de programmation. Pourquoi personne ne me l'a jamais dit ?! J'avais toujours cette image obscure de la chose et pis en fait, c'est juste du code. (-.-)
En plus, c'est un langage qui est plutôt facile à prendre en main pour l'usage que je prévois d'en faire (#J'ai menti, j'ai souffert).

M'appuyant sur mon B2 en Python et mon A1 en C#, Java, j'ai donc suivi le tutoriel sur ([sheets-pratique.com/fr/apps-script](https://www.sheets-pratique.com/fr/apps-script)) avec des étoiles dans les yeux.
Il est divisé en 12 parties que j'ai survolées (peut-être un peu trop vite parfois) :

1. Introduction [X]
2. Variables et tableaux [X]
3. Feuilles et cellules [X]
4. Conditions [X]
5. Boucles [X]
6. Fonctions [X]
7. Tableaux avancés [X]
8. Déclencheurs [X]
9. Menus [X]
10. Boîtes de dialogue [X]
11. Fenêtres personnalisées [X]
12. Compléments [X]

C'était intéressant de voir la liberté qu'on avait avec App Scripts, mais comme le bon Centralien que je suis, je suis allé vers l'essentiel.
Après avoir lu et noté ce dont j'aurai besoin pour ma tâche qui était de réécrire mon tableau sous une forme plus appropriée, je suis parti comme une flèche (ou plutôt une tortue asthmatique et amnnésique).

## 6. Conclusion <a id="section-6"></a>

J'ai l'impression à peu près fait le tour de Google Sheets en terme de fonctionnalités. Par contre, quant à Apps Scripts, je n'ai qu'effleuré la surface de son potentiel. A voir si j'en ai besoin dans ma vie.

Le MON s'est plutôt bien passé, j'ai bien aimé (et beaucoup souffert psychologiquement pendant la partie Apps Scripts, moi qui ne suis pas un fan de programmation). Je dirai que j'ai passé un poil plus que 10h, mais on va dire que ça valait le coup.

## 7. Sources <a id="section-7"></a>

[Formation en Excel](excel-pratique.com) par excel-pratique.com
[Formation en Google Sheets](https://www.sheets-pratique.com/) par sheets-pratique.com
[Formation en Apps Scripts](https://www.sheets-pratique.com/fr/apps-script) par sheets-pratique.com
 -->
