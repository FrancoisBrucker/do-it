---
layout: layout/mon.njk

title: "Un peu d'Excel/Google Sheets pour mourir moins idiot"
authors:
  - TAING Henri

date: 2023-10-15

tags:
  - "temps 2"
  - Excel
  - Google Sheets

résumé: "Un vieux qui apprend à faire des tableaux et des graphes sur Excel/Google Sheets, enfin"
---

{%prerequis 'MON débutant'%}
Avoir un cerveau à moitié allumé et encore...
{%endprerequis%}

---

## Table des matières

1. [Introduction](#section-1)
2. [Les bases en quelques mots](#section-2)
3. [Des graphiques de partout !](#section-3)

## 1. Introduction <a id="section-1"></a>

Pendant le premier cours d'éco-système digital, on nous a demandé de faire un tableau de données sur Excel/Google Sheets, quelques calculs et donner une représentation pertinente. N'ayant pas Excel, j'ai utilisé Google Sheets.
Et je fus incapable de créer un beau graphique. Quelle ne fut pas ma tristesse. Mon graphe était moche et j'avais eu l'impression d'avoir cliquer sur une suite de boutons sans sens. Puis franchement, ce serait dommage de mourir sans savoir ce qu'est un tableau croisé dynamique depuis le temps que j'en entends parler.

Il est donc temps de devenir moins idiot. Pour ça, j'ai décidé de faire comme **[Lola BOURDON dans son MON 1.2](../../../Lola-Bourdon/mon/temps-1.2/)** en suivant le cours sur [excel-pratique.com](excel-pratique.com) qui est divisé en 11 parties :

1. Les bases [X]
2. Les tableaux [X]
3. Les formats [X]
4. Insertions d'objets [X]
5. Recopie incrémentée [X]
6. Formules et fonctions [X]
7. Les graphiques []
8. Mise en forme conditionnelle []
9. Tri et filtres []
10. Validations de données []
11. Tableau croisé dynamique []

## 2. Les bases en quelques mots <a id="section-2"></a>

Ayant déjà fait un peu d'analyse de données avec Python l'année dernière et utilisé Google Sheets pour des tâches simples, j'ai pu survoler les premières parties.
Seulement, le fait que le tutoriel soit sur Excel et non sur Google Sheets m'a beaucoup ralenti, car je devais toujours trouver l'équivalent sur Google Sheets, et la syntaxe changeait parfois.

Par exemple, pour la fonction MID (ou STXT), qui permet d'extraire des chaînes de caractères.
Google Sheets me renvoie "#ERROR" me disant qu'il y a une erreur dans ma formule. J'ai pris une demi-heure pour me rendre compte que les "," ne servaient pas de séparation dans la formule, mais qu'il fallait utiliser des ";".

### Sources

[Formation en Excel](excel-pratique.com) par excel-pratique.com
