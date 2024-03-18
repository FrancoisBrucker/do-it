---
layout: layout/mon.njk

title: "Utiliser Microsoft Power BI pour comprendre la donnée]"
authors:
  - TAING Henri

date: 2024-02-07

tags:
  - "temps 3"
  - Microsoft Power BI

résumé: Utiliser Microsoft Power BI pour faire mumuse avec des données.


---

{%prerequis 'MON débutant'%}
Ne pas avoir peur de tout casser à chaque fois
{%endprerequis%}

---

## Table des matières

1. [Introduction](#section-1)
2. [Power BI Desktop](#section-2)
3. [Power BI Service](#section-3)
3. [Cas des bibliothèques](#section-4)
4. [Conclusion](#section-5)
5. [Sources et horodateur](#section-6) 

## 1. Introduction <a id="section-1"></a>

J'ai mis sur mon CV que je savais utiliser Power BI alors que je n'avais pas fait que joujou rapidement avec. Donc, il est temps de faire de mon bullshit une réalité. 

Je me suis appuyé sur le cours proposé par Skillsoft et mis à disposition par mon entreprise :
[Mastering Power BI](https://www.skillsoft.com/journey/mastering-power-bi-00f66d92-1f14-41d1-9835-249e5ada7126)

Je n'ai comptabilisé que les heures passées sur le premier cours (environ 8h) et le temps de mettre en forme toutes mes notes que j'ai prises durant ces 24 heures de formation (environ 2h).

## 2. Power BI Desktop <a id="section-2"></a>

Il faut savoir premièrement que dans la plupart des cas, vous n'aurez pas à mettre les mains dans le code. Sauf si la base de données utilisée est exécrable. 

**Organisation de Power BI**
Il faut d'abord faire la différence entre Power BI Desktop et Power BI Service :
- Power BI Desktop, application en local,
- Power BI Service, sur le cloud et permet de partager ses rapports en live.

Les deux permettent quasiment les mêmes opérations, mais Power BI Desktop est plus maniable et plus rapide.
On va s'intéresser plus à Power BI Desktop en premier lieu.

**Pour commencer**
Vous avez 3 fenêtres sur la colonne de gauche qui correspondent de haut en bas à votre page de rapport (Report View), votre base de données (Table View) et les liens entre les différentes tables et colonnes (Model View).

Pour **extraire** une base de données qu'on va étudier, analyser puis visualiser, il suffit d'aller dans "Get Data", puis de choisir ce qui vous intéresse. 
{% details "Remarques sur l'extraction" %}
- Il faut avoir les autorisations nécessaires et ses identifiants si on veut utiliser les données d'un sharepoint de son entreprise par exemple
- Faire attention à bien avoir la même version installée pour SQL Connector et MySQL/SQLServer 
- Utiliser un compte avec le moins de privilèges possible pour des raisons de sécurité, ce genre de comptes peut être créé par exemple quand on utilise Google Cloud ou AWS. 
{% enddetails %}

Une fois votre base de données extraite, il est temps de la transformer.

### Table View
**Transformer avec Power Query Editor**
On peut d'abord consulter les profils des colonnes en faisant un clic droit sur les colonnes et en sélectionnant Column Quality (Valid - Error- Empty) et Column Distribution (Répartition des données entrées dans la colone) ou en allant dans View > Cocher ces mêmes cases. 

<img src="profile_distrib.PNG">

Puis changer la première ligne en titre si ce n'est pas fait avec "Use First Row as Headers". 
En faisant ça, une ligne apparaît avec **Promoted Headers** sur la droite dans Query Settings (Si vous ne voyez pas cette fenêtre, il suffit d'aller dans View > Cliquer sur Query Settings). Cette fenêtre fournit un suivi des opérations effectuées sur la table.
Si vous cliquez sur une opération par exemple, vous pouvez voir la formule utilisée que vous pouvez modifier.
```
= Table.PromoteHeaders(#"Nom_initial_de_la_table", [PromoteAllScalars=true])
```
Si vous appliquez une autre transformation, par exemple, clic droit une colonne et "Remove Errors", on a :
```
= Table.RemoveRowsWithErrors(#"Promoted Headers", {"nom_colonne"})
```
On vient donc d'appliquer Table.RemoveRowsWithErrors à la table précédente nommée "Promoted Headers" à cause de notre transformation (on peut la renommer dans la fenêtre Querry Settings). 

Pour aller plus loin, vous pouvez utiliser l'éditeur avancé : View > Advanced Editor
<img src="advanced_editor.PNG">

Pour créer d'autres colonnes, vous pouvez utiliser Add Column :
- Merge Columns pour concaténer des colonnes 
- Custom Column avec une formule DAX (Data Expressing Formula) avec des IFs, des opérations mathématiques, etc.
- dans le cas de plusieurs tables, vous pouvez utiliser les colonnes d'autres tables, mais il faut bien vérifier leurs liens logiques dans la partie "Model View". 

### Report View


## 3. Power BI Service <a id="section-3"></a>


## 5. Conclusion <a id="section-5"></a>

## 6. Sources et horodateur <a id="section-5"></a>

Le cours est mis à disposition par mon entreprise CGI. Il s'agit d'une formation proposée par Skillsoft Aspire Journeys. 
[Mastering Power BI](https://www.skillsoft.com/journey/mastering-power-bi-00f66d92-1f14-41d1-9835-249e5ada7126)

Bases de données utilisés pour les exemples : 
[Baromètre des représentations sociales du changement climatique de l'ADEME](https://www.data.gouv.fr/fr/datasets/barometre-representations-sociales-du-changement-climatique/)
[Base de données sur les bibliothèques](https://www.data.gouv.fr/fr/datasets/adresses-des-bibliotheques-publiques-2/#/resources)
**Horodateur** : 
> Vendredi 01/03/2024 : 2h (Début du premier cours)
> Mercredi 06/03/2024 : 3h (Première partie du premier cours)
> Jeudi 07/03/2024 : 3h (Fin du premier cours)
> Vendredi, Samedi, Dimanche : Suite du cours de mon côté
> Lundi 18/03/2024 : 2h (Notes)
