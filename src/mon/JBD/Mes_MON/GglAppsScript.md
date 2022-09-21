---
layout: layout/post.njk

title: "Google Apps Script"
authors:
  - Jean-Baptiste Durand
---

<!-- début résumé -->
Google apps script ou comment automatiser les choses embêtantes dans un tableur
<!-- fin résumé -->

<h2 id="toc"> Table des matières </h2>

- [Table des matières](#toc)
- [Qu'est ce que Google Apps Script ?](#h1)
- [Quelles sont les principales fonctionnalitées ?](#h2)
  - [Fonctions de calcul personnalisées](#h2-1)
  - [Automatiser plusieurs cases](#h2-2)
    - [Class Range](#h2-2-1)
    - [Class Sheet](#h2-2-2)
- [Exemple - Création d'un historique](#h3)
- [Liens Utils](#liens)

<h2 id="h1"> Qu'est ce que Google Apps Script ? </h2>

**Google Apps Script** est un outils permettant d'**automatiser** les autres outils de Google en effectuant des taches régulières, ou en réaction à l'interaction d'un utilisateur.

Nous nous concentrerons sur l'apport que peut faire Google Apps Script à Google Sheet, mais il est aussi possible d'automatiser Google Docs et Google Slides ([↓ liens vers la documentation ↓](#liens))

**Google Apps Script** est un outils qui execute du **JavaScript** pour effectuer vos actions. Il est possible aussi d'ajouter des bibliothèques, mais attention, l'utilisation de bibliothèque ralentit l'execution du code.

**Comment accéder Google Apps Script sur Google Sheet ?**

<img src="../../Image/google_apps_script_acces.png" alt="Technologies utilisées" style="height: 200px; margin: 0 auto; border: 0" />

<h2 id="h2"> Quelles sont les principales fonctionnalitées ? </h2>

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

Pour cela, il faut savoir comment accéder, en lecture et en écriture, aux cellules, à partir de la fonction.

Pour avoir la documentation exacte, je vous laisse vous référer aux [liens](#liens). Sinon voici quelques fonctions essentielles pour bien commencer :

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
Les formules que l'ont récupère et que l'on set sont en anglais : la traduction faite pour Google Sheet (ex : SOMME), redevient en anglais (ex : SUM)
{% endattention %}


<h4 id="h2-2-2">Class Sheet</h4>

| Méthode               | Description                     |
| --------------------- | ------------------------------- |
| getRange(a1Notation)  | Renvoi l'ensemble des cases     |
| appendRow(rowContent) | Ajoute un ligne avec le contenu |

<h2 id="h3"> Exemple - Création d'un historique </h2>

<h2 id="liens"> Liens Utils </h2>

Documentation de Google sur l'utilisation de Google Apps Script sur ses différents produits :
- [Google Sheet](https://developers.google.com/apps-script/guides/sheets)
- [Google Docs](https://developers.google.com/apps-script/guides/docs)
- [Google Slides](https://developers.google.com/apps-script/guides/slides)

[Mon exemple](https://docs.google.com/spreadsheets/d/1g3JqFxX8HgXEYpOcudeMbe4TtCH9vGVsyqudbTxTd6E/edit?usp=sharing)

Api pour accéder aux cellules
- [Class Sheet](https://developers.google.com/apps-script/reference/spreadsheet/sheet) : classe de feuille de calcul
- [Class Range](https://developers.google.com/apps-script/reference/spreadsheet/range) : classe d'un ou plusieurs cases