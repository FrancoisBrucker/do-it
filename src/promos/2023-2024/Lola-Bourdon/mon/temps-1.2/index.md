---
layout: layout/mon.njk

title: " MON 2 : Excel - Repartir sur de bonnes bases "
authors:
  - Lola Bourdon

date: 2023-10-18

tags: 
  - "temps 1"
  - "excel"

résumé: "MON 1.2 sur les bases d'excel"
---

{%prerequis 'Niveau débutant'%}  
{%endprerequis%}

Mes objectifs pour ce deuxième MON sont de redécouvrir les bases d'excel. En effet, lors de mes derniers stages, j'ai été amenée a utiliser excel mais je me suis souvent retrouvée en difficulté dans la manipulation des données. C'est pourquoi je repars du début afin d'être capable de les maîtriser convenablement dans le cadre d'un futur stage en entreprise et aussi poursuivre avec les fonctions VbA.

### Méthodologie

Pour recommencer une formation sur excel a partir de zéro, j'ai suivi le cours excel sur. Qui se divise en 11 parties synthétiques :

1. Les bases
2. Les tableaux
3. Les formats 
4. Insertions d'objets
5. Recopie incrémentée
6. Formules et fonctions
7. Les graphiques
8. Mise en forme conditionnelle
9. Tri et filtres
10. Validations de données
11. Tableau croisé dynamique

J'ai réalisé les exercices proposé tout au long de la formation.

État des lieux le 06 octobre : 5h de formation.

### Chapitres 1 à 8

Dans cette première partie, je vais simplement énumérer et détailler les fonctionnalités d'excel qui me paraissent utile à revoir si on estime ne pas avoir besoin de refaire toute la formation:

1. L'utilisation du `$` qui permet de fixer une cellule/colonne/ligne lorsque nous utilisons des formules, par exemple :
![excel](EXCEL2.png)
Dans cette exemple, on divise par la valeur **3**, qui apparaît dans la cellule **B8**. Seulement on veut pouvoir diviser à chaque fois par cette **même valeur** de cellule **B8** lors de la recopie. Corrigeons:
![excel](EXCEL3.png)
Pour cela; le premier `$` de `$B$8` fixe la **colonne** lors de la recopie et le second `$` fixe la **ligne**. Ici,  on aurait pu simplement fixer la ligne.

1. 