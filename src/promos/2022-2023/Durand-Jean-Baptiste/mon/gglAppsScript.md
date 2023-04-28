---
layout: layout/mon.njk

title: "Google Apps Script"
authors:
  - Jean-Baptiste Durand

date: 2022-10-07

tags:
  - 'temps 1'
  - 'Google Apps Script'
  - 'Javascript'
  - 'Google Sheet'
---

<!-- début résumé -->
Google apps script ou comment automatiser les choses embêtantes dans un tableur
<!-- fin résumé -->

<h2 id="toc"> Table des matières </h2>

- [Table des matières](#toc)
- [Qu'est ce que Google Apps Script ?](#h1)
- [Quelles sont les principales fonctionnalités ?](#h2)
  - [Fonctions de calcul personnalisées](#h2-1)
  - [Automatiser plusieurs cases](#h2-2)
    - [Class Range](#h2-2-1)
    - [Class Sheet](#h2-2-2)
  - [Déclencheur de fonction](#h2-3)
    - [Manuellement](#h2-3-1)
    - [Temporellement](#h2-3-2)
    - [Listener](#h2-3-3)
- [Exemple - Création d'un Tricount](#h3)
- [Liens Utiles](#liens)

<h2 id="h1"> Qu'est ce que Google Apps Script ? </h2>

**Google Apps Script** est un outils permettant d'**automatiser** les autres outils de Google en effectuant des taches régulières, ou en réaction à l'interaction d'un utilisateur.

Nous nous concentrerons sur l'apport que peut faire Google Apps Script à Google Sheet, mais il est aussi possible d'automatiser Google Docs et Google Slides ([↓ liens vers la documentation ↓](#liens))

**Google Apps Script** est un outils qui execute du **JavaScript** pour effectuer vos actions. Il est possible aussi d'ajouter des bibliothèques, mais attention, l'utilisation de bibliothèque ralentit l'execution du code.

**Comment accéder Google Apps Script sur Google Sheet ?**

<img src="../Image/google_apps_script_acces.png" alt="Technologies utilisées" style="height: 200px; margin: 0 auto; border: 0" />

<h2 id="h2"> Quelles sont les principales fonctionnalités ? </h2>

<h3 id="h2-1">Fonctions de calcul personnalisées</h3>

Google Sheet a une grande quantité de formules déjà définies pour faire des opérations simples, SOMME, MOYENNE, ...

Mais il existe un nombre limité de fonctions, Google Apps Script permet de créer la fonction qui répond à nos besoins.

**Comment faire ?**

On créer une fonction :

```javascript
function MaFonction(mesParametres){
  // Mes calculs
  return resultat
}
```

et dans la case où on veut appliquer la fonction, on applique le calcul : **=MaFonction(A1)**

<h3 id="h2-2">Automatiser plusieurs cases</h3>

Les fonctions de Google Apps Script **n'offrent pas seulement** la possibilité de modifier une unique case (une formule retourne une unique valeur qui est stockée dans une seule cellule). 
Google Apps Script offre aussi la possibilité de gérer un grand nombre de cases, en accédant de manière indépendante à l'ensemble des cases du tableur.

Pour cela, il faut savoir comment **accéder**, en *lecture* et en *écriture*, **aux cellules**, à partir de la fonction.

{% prerequis %}
Pour avoir la documentation exacte, je vous laisse vous référer aux [liens](#liens).
{% endprerequis%}
 
Sinon voici quelques fonctions essentielles pour bien commencer 👇

<h4 id="h2-2-1">Class Range</h4>

| Méthode                | Description                                                                     |
| ---------------------- | ------------------------------------------------------------------------------- |
| clear()                | Efface le contenu d'une plage de donnée                                         |
| getA1Notation()        | Récupère la description au format A1                                            |
| getValue()             | Renvoie la valeur de la case ou de la case en haut à gauche si plage de données |
| getValues()            | Renvoi l'ensemble des valeurs de la plage de données                            |
| getFormulas()          | Idem mais la formule                                                            |
| getFormulas()          | Idem mais les formules de la plage de données                                   |
| setValue(value)        | Modifie la valeur de la case ou de la case en haut à gauche si plage de données |
| setValues(values)      | Modifie l'ensemble des valeurs de la plage de données                           |
| setFormulas(formula)   | Idem mais la formule                                                            |
| setFormulas(formuulas) | Idem mais les formules de la plage de données                                   |

{% attention "**Attention** aux Formules" %}
Les formules que l'on **get** et que l'on **set** sont en anglais : la traduction faite pour Google Sheet (ex : SOMME), redevient en anglais (ex : SUM)
{% endattention %}


<h4 id="h2-2-2">Class Sheet</h4>

| Méthode               | Description                     |
| --------------------- | ------------------------------- |
| getRange(a1Notation)  | Renvoi l'ensemble des cases     |
| appendRow(rowContent) | Ajoute un ligne avec le contenu |

<h3 id="h2-3">Déclencheur de fonction</h3>

<h4 id="h2-3-1">Manuellement</h4>

Pour executer de manière manuelle la fonction, il faut d'abord l'importer,

Ensuite, on peut l'executer à tous moment :

<img src="../Image/google_apps_script_function_execution.png" alt="Executer la fonction" style="height: 200px; width:1000px; margin: 0 auto; border: 0" />

{% faire %}
Il vous sera demandé d'autoriser l'execution d'un script
{% endfaire %}

<h4 id="h2-3-1">Temporellement</h4>

Il est possible de déclencher une fonction de manière temporelle.

Voici un exemple, issue de la documentation de Google [liens](#liens)

```javascript
function createTimeDrivenTriggers() {
  // Trigger every 6 hours.
  ScriptApp.newTrigger('myFunction')
      .timeBased()
      .everyHours(6)
      .create();
  // Trigger every Monday at 09:00.
  ScriptApp.newTrigger('myFunction')
      .timeBased()
      .onWeekDay(ScriptApp.WeekDay.MONDAY)
      .atHour(9)
      .create();
}
```

J'ai pas cependant eu l'occasion d'aller en profondeur dans cette fonctionnalité, le laisse cette possibilité à quelqu'un d'autre pour un autre MON 😉

<h4 id="h2-3-1">Listener</h4>

En créant une fonction ayant des noms spécifiques, il est possible de déclencher un script lors qu'un action se produit.

Les 2 principales fonctions sont :
  - onEdit : executée à chaque fois qu'un utilisateur modifie une case
  - onOpen : executée à chaque fois qu'un utlisateur (ayant des droits de modification) se connecte sur le google sheet.

exemple : 
```javascript
function onEdit(e){
  //supprime le contenu de toute les cases modifiées (⊙ˍ⊙)
  const range = e.range;
  range.clear()
}
```

Il existe quelques autres fonctions, comme d'habitude le détail dans les [liens](#liens)👇

<h2 id="h3"> Exemple - Création d'un Tricount </h2>

{% info %}
L'objectif est de créer un Tricount, permettant de gérer les comptes à plusieurs. Très utilisé dans les colocs centraliennes notamment. Chacun ajoute les dépenses faites pour le groupe et l'application comptabilise combien d'argent chacun doit à qui.
{% endinfo %}

Le projet est composé de paramtères modifiables, pour permettre de personnaliser le Google Sheet
```javascript
const tricountSettings = {
  sourceSheet: 'Ajout_achat',
  targetSheet: 'Historique',
  statSheet: 'Statistiques',
  people:["Personne 1","Personne 2", "Personne 3"]
}
```

Et de 4 fonctions :
- **tricountAddToHistory**, dont le but est de transférer les données d'ajout d'achat dans la partie historique (fonction inspirée du [travail de --Hyde](https://support.google.com/docs/thread/41717054))
- **columnToLetter**, dont le but est de transformer la ième colonne en la lettre associée (fonction créée par [AdamL](https://stackoverflow.com/questions/21229180/convert-column-index-into-corresponding-column-letter))
- **onEdit**, dont le but est de déclencher la fonction **trincountAddToHistory** si les conditions sont réunies
- **generateSheet**, dont le but est de créer toute la mise en page du tricount au début

Tout le code source est disponible [liens](#liens).

<h2 id="liens"> Liens Utiles </h2>

Documentation de Google sur l'utilisation de Google Apps Script sur ses différents produits :
- [Google Sheet](https://developers.google.com/apps-script/guides/sheets)
- [Google Docs](https://developers.google.com/apps-script/guides/docs)
- [Google Slides](https://developers.google.com/apps-script/guides/slides)

Documentation sur les fonctionnalitées :
- [Class Sheet](https://developers.google.com/apps-script/reference/spreadsheet/sheet) : classe de feuille de calcul
- [Class Range](https://developers.google.com/apps-script/reference/spreadsheet/range) : classe d'un ou plusieurs cases
- [Déclencheurs listener](https://developers.google.com/apps-script/guides/triggers) : Fonction listener
- [Déclencheur temporel](https://developers.google.com/apps-script/guides/triggers/installable) : Fonction exéctuée de manière régulière

Mon travail :
- [Le Google Sheet](https://docs.google.com/spreadsheets/d/1g3JqFxX8HgXEYpOcudeMbe4TtCH9vGVsyqudbTxTd6E/edit?usp=sharing)
- [Le code source](../../Annexe/GglAppsScript)
- [Inspiration pour **tricountAddToHistory**](https://support.google.com/docs/thread/41717054)
- [Fonction **columnToLetter**](https://stackoverflow.com/questions/21229180/convert-column-index-into-corresponding-column-letter)

