---
layout: layout/mon.njk

title: "Google AppScript et son cousin VBA"
authors:
  - Damien WOLBERT
date: 2024-09-08
tags: 
  - "temps 1"

résumé: "Ce MON vise à à construire un socle de connaissances pour s'initier à Google Appscript. De plus, il présente les similitudes entre ce langage et VBA, afin de pouvoir passer de l'un à l'autre pour les fonctionnalités principales."
---

{% prerequis %}

- Connaissances des bases de VBA

{% endprerequis %}
{% lien %}

- Site pratique pour commencer en VBA : https://excel-pratique.com/fr/vba
- Site pratique pour commencer en AppScript : https://sheets-pratique.com/fr/apps-script

{% endlien %}

## Contexte
Ayant dû utiliser Google AppScript pour des projets personnels avant de réaliser ce MON, j'ai préféré ajouter une comparaison à VBA afin qu'il ait une plus-value supplémentaire pour moi et les prochains lecteurs.

## Introduction

Le langage Google Appscript permet de coder des programmes sur Google Drive et notamment Google Sheet. Il est pour Google Sheet ce que VBA est pour Excel. Toutefois, les syntaxes de ces deux langages sont assez différentes. Ce MON contient un ensemble d'éléments de base pour coder en AppScript ainsi qu'une comparaison avec des éléments de base de VBA.

{% note %}
ChatGPT peut s'avérer être un véritable allié pour apprendre à coder dans ces langages. Attention toutefois à vérifier tous les résultats proposés : en effet certains ne fonctionnent pas. Une partie de ce MON a été réalisé en s'appuyant sur ChatGPT.
{% endnote %}

## Comment utiliser AppScript ?

### Créer un projet AppScript depuis GSheet

Pour créer un projet AppScript depuis un fichier GSheet, il suffit de cliquer sur le mneu "Extension" de la barre de tâche, puis sur "Google AppScript". Une fenêtre s'ouvre avec un projet vierge.

- Nommer son projet
- Nommer son premier fichier (par défaux appelé "Code.gs")
- Créer une fonction de mise en route, par exemple une fonction affichant "Hello World" dans une cellule d'un tableau. Cela permettra de lancer les demandes d'autorisation pour l'accès aux données. Chaque utilisateur des différentes fonctions et programmes que vous créez doivent autoriser vos programmes à acceder à vos données.

{% attention '**ATTENTION !**' %}
Lorsque vous travaillez avec d'autres collaborateurs, chacun doit réaliser les tâches d'autorisation avant toute automatisation (Utilisation de programmes et/ou d'automatisation créées par d'autres personnes, lancements différés automatiques...).
{% endattention %}

### Les choses à savoir

Google AppScript possède un certain nombre de défauts qui n'en sont plus lorsque nous savons qu'ils existent.

{% details "L'enregistrement" %}
L'enregistrement est réalisé soit manuellement, soit avant chaque lancement de programme. Il est réalisé sur l'ensemble du projet et indique les erreurs de syntaxe. Cela permet en effet de limiter le risque de perte mais pose un problème majeur : vous ne pouvez pas laisser une fonction en attente ! Si vous lancez un programme vous devez vous assurer que la synthaxe de l'entièreté de votre projet est correcte.
Ainsi, il est pratique **d'enregistrer régulièrement son travail !** et de convertir les blocs "en attente", en commentaire.
{% enddetails %}

{% details "Les droits d'accès" %}
Comme évoqué précemment, tout utilisateur d'un nouveau programme doit d'abord autoriser ce dernier à s'exécuter. Pour se faire, il est intéressant de créer une fonction simple, permettant d'accéder ou de modifier la valeur d'une cellule du document GSheet (N'afficher qu'un message dans la boite de dialogue ne fonctionne par exemple pas).

```
function Hello_world() {
  // Le document actif possède une feuille dont le nom est "Feuille 2"
  feuille = SpreadsheetApp.getActive().getSheetByName("Feuille 2");

  // On inscrit "Hello World" dans la cellule A1 (première ligne, première colonne)
  feuille.getRange(1,1).setValue("Hello World");
}
```
Après avoir cliqué sur le bouton de lancement, un certain nombre de fenêtre vont se succéder.
![Autorisation 1](./Autorisation%201.webp)
![Autorisation 2](./Autorisation%202.webp)
![Autorisation 3](./Autorisation%203.webp)
![Autorisation 4](./Autorisation%204.webp)

{% enddetails %}

{% details "Les déclencheurs" %}
Les déclencheurs permettent de lancer des programmes de manière différentes ou lors d'un évènement.  
**Types de déclencheurs :**
- Basé sur une feuille de calcul : Ouverture, modification (modification manuelle d'une cellule), changement (modifications structurelles ou par des programmes : nouvelle feuille, nouvelle colonne...), envoie d'un formulaire.
- Horaires : date et heure précise, intervalles de temps (de la minute au mois).
- Basé sur un agenda : A la modification d'un google agenda.

![Menu déclencheurs](Menu%20déclencheurs.webp)
![Réglage déclencheur](Réglage%20déclencheur.webp)
{% enddetails%}

{% details "Journal d'exécution" %}
Le journal d'exécution permet de tester ses fonctions et programmes plus facilement, sans avoir à afficher des boites de dialogues nécessitant une action utilisateur. Par exemple, fermer la boite de dialogue pour que le programme puisse continuer.
On utilise donc la commande **console.log()** pour faire appraraïtre des résultats dans le journal
```
console.log("7");
console.log("8");
```
Résultat :
![Journal d'exécution](./Journal%20d'exécution.webp)
{% enddetails %}

## Syntaxes AppScript et VBA

{% attention %}
En Appscript, chaque ligne doit être terminée par **";"** !!!!
{% endattention %}
{% info %}
Les commentaires se font :  
- **En VBA :** Avec ***'***
- **En AppScript :** Avec ***//***
{% endinfo %}

### Données de référence pour comparaison

Considérons les données suivantes : 
- Un fichier (Gsheet ou Excel) nommé "Suivi"
- "Suivi" possède deux feuilles : "Page de garde" et "KPI" telles que suit :

### Variables
#### Déclarer des variables
En VBA ou en AppScript il n'est pas nécessaire de déclarer les variables que l'on utilise. Cela reste tout de même une bonne pratique pour ne pas avoir de problème entre variables locales et variables globales.
**En VBA :**
```
Sub test()

'Déclarer avec le type
Dim a As Integer
a = 7
'Déclarer sans le type
Dim b
b = 10
'Affecter directement une valeur
c = 12

End Sub
```
**En Appscript :**
```
function Variables() {
  // Déclarer et affectercer
  var a = 7;
  // Ne pas déclarer
  b = 8;
}
```
#### Types principaux et fonctions de conversion
**En Appscript :**
| Type | Description | Conversion |
|------|-------------|------------------------|
| Number | Nombres entiers et flottants | Fonction **Number()**, s'applique aux chaines de caractères et aux booléens |
| String | Chaine de caractère | Méthode **.toString()**|
| Boolean | Valeur booléenne : **true** ou **false** | Fonction **Boolean()**. Renvoie true pour toute chaine de caractère autre que la chaine vide "" et pour tout Number autre que 0 |
| Array | Tableaux | |

**En VBA :**
| Type | Description | Conversion |
|------|-------------|------------------------|
|Integer| Entiers entre -32 768 et 32 767 | Fonction **CInt()** |
|Long| Entiers entre -2 147 483 648 et 2 147 483 647|Fonction **CLng**|
|Double|Nombres décimaux|Fonction **CDbl()**|
|String|Chaines de caractère|Fonction **CStr()**|
|Boolean|Valeur booléenne : **True** ou **False**|Fonction **CBool()**|

### Opérateurs logiques et conditions
Supposons que nous voulons tester la valeur d'une variable : si elle est supérieure à 5, on lui ajoute 10 ; si elle est égale à 2, on lui attribue  0 ; sinon, on lui ajoute 5.

**En Appscript :**
```
let a = 2;
if(a >= 10){
  a = a + 10;
} else if(a == 2){
  a=0;
} else {
  a = a + 5;
}
```
**En VBA :**
```
a = 2
If a >= 10 Then
    a = a + 10
ElseIf a = 2 Then
    a = 0
Else
    a = a + 5
End If
```
### Boucles
#### Boucle while
Suppossons que nous voulons connaitre le premier élément de la suite de Fibonacci supérieur à 8, ainsi que son rang dans la suite.
{% details "Rappel sur la suite de Fibonacci" %}
D'après Wikipédia :
![Suite de Fibonacci](./Suite%20de%20Fibonacci.webp)
{% enddetails %}
**En Appscript :**
```
rang = 1;
seuil = 95;

f0 = 0;
transi = 0;
f1 = 1;

while(f1<seuil){
  rang += 1;
  transi = f1;
  f1 = f1 + f0;
  f0 = transi;
```

**En VBA :**
```
rang = 1
seuil = 95

f0 = 0
transi = 0
f1 = 1

While f1 < seuil
    rang = rang + 1
    transi = f1
    f1 = f1 + f0
    f0 = transi
Wend

MsgBox (rang)
MsgBox (f1)
```

#### Boucle for
Reprenons l'exemple de la suite de Fibonacci, cette fois-ci, nous voulons créer une liste avec les n premiers éléments de la suite.

**En AppScript :**
```
  rang = 50;
  f0 = 0;
  transi = 0;
  f1 = 1;
  liste = [f0,f1];

  for(let i=2;i<=rang-2;i++){
    transi = f1;
    f1 = f1 + f0;
    f0 = transi;
    liste.push(f1);   
  }
```
**En VBA :**
```
rang = 50
f0 = 0
transi = 0
f1 = 1
Set liste = New Collection

For i = 2 To rang - 2
    transi = f1
    f1 = f1 + f0
    f0 = transi
    liste.Add f1
Next
```
### Les listes
#### Doit-on réellement utiliser des listes ? L'utilité d'un "back-end"
AppScript et VBA sont souvent utilisés pour intéragir avec des tableurs. Il est donc facile de stocker des valeurs dans un de ces tableaux.
Lorsque des listes sont utilisées de manière récurrente pour l'exécution d'un programme, il peut être interessant de créer une feuille de calcul annexe permettant de stocker et d'accéder à différentes données. J'ai pour habitude de nommer cette feuille **Back-end**.

{% attention %}
En VBA, l'utilisation de listes ou de tableaux n'est pas facile, voire ineffcicace.
{% endattention %}

#### Opérations sur les listes
##### ¤ Créer une liste
***En AppScript :***
```
liste = []; // Création d'une liste vide
liste = ["a","b","c","d","e"]
```
***En VBA :***
En VBA, il est possible d'utiliser des tableaux, des collections, des Arraylist, des dictionnaires... La structure la plus simple d'utilisation est la collection.
```
Dim liste = New Collection 'Création d'une liste vide
liste.Add "a"
liste.Add "b"
liste.Add "c"
liste.Add "d"
liste.Add "e"
```

##### ¤ Longueur de liste
***En AppScript :***
```
Longueur = liste.length;
```
***En VBA :***
```
Longueur = liste.Count
```
##### ¤ Accéder à des éléments
***En AppScript :***
```
premier = liste[0]; // Premier élément de la liste
dernier = liste[liste.length-1]; //Dernier élément de la liste
troisieme = liste[2]; // Troisème élément de la liste. LE RANG COMMENCE A 0 !!
```
***En VBA :***
```
premier = liste(1) // Premier élément de la liste
dernier = liste(liste.Count) // Dernier élément de la liste
troisième = liste(3) // Troisième élément de la liste. LE RANG COMMENCE A 1 !!
```

##### ¤ Ajouter et supprimer des éléments

***En AppScript :***
```
liste.push("x","y","z"); // Ajoute "x", "y" et "z" à la fin de la liste
liste.unshift("alpha"); // Ajoute "alpha" au début de la liste
position = 0;
nombre = 2;
liste.splice(position,nombre,"delta","mu"); // Permet de supprimer un certain nombre d'éléments à partir d'une position initiale et d'ajouter d'autres éléments à la place
```
{% details "Méthode .splice()" %}
La méthode **.splice()** permet de supprimer des éléments mais aussi de les ajouter à une certaine position à place d'un certain nombre d'autres.
```
liste = [1,2,3,4,5,6,7,8,9,10];
liste.splice(4,0,152,189,204); // 152, 189, 204 sont les valeurs insérée à la position 4
// liste est maintenant égale à [1, 2, 3, 4, 152, 189, 204, 5, 6, 7, 8, 9, 10]
```
{% enddetails %}

{% details "Methode .filter()" %}
**.filter()** permet de créer une liste fille en filtrant une liste mère.
```
liste=[1,2,3,4,5,6,7];
liste = liste.filter(nombre => nombre!=5); //liste est alors égale à [1,2,3,4,6,7]
```
{% enddetails %}
***En VBA :***
```
liste.Add "z"
```
{% attention %}
En VBA, on ne peut pas éliminer facilement un élément d'une Collection. Il faut utiliser une boucle pour créer une nouvelle collection dépourvue des éléments à supprimer.
Les **ArrayList** sont en cela plus simples d'utilisation mais il semble nécessaire d'importer des bibliothèsques spéciales pour cela.
{% endattention %}

## Créer des programmes et des fonctions
### AppScript
Pour travailler en AppScript il est nécessaire d'utiliser des fonctions ou de définir les fonctions utilisées dans un fichier à part. En effet, il est possible d'écrire un programme sans fonction au sein d'un fichier. Cependant, lors de l'éxecution de celui-ci, toutes les fonction également définies sur le fichier seront exécutées.

**Pour définir des fonctions :**
```
function MaFonction(x,y){
  return()
}
```
- Notons qu'une fonction peut ne rien renvoyer et donc peu ne pas comporter de return().
- Pour utiliser une fonction au sein d'une autre, il suffit de l'appliquer, la fonction sera notamment proposée après avoir tapé les premiers caractères de son nom.
### VBA
Pour travailler en VBA, il faut obliagtoirement travailler au sein d'un **Sub** dans lequel il sera possible d'appeler d'autres **Sub** ou d'autres **fonctions**.
```
Sub MonSub(argument)
argument = argument + 1
End Sub

'''''''''''''''''''''''''''''
Sub MonGrandSub()
x = 2
Call MonSub(x) // La fonction MonSub est appliquée à x, qui devient donc égal à 3
End Sub
```
Lorsque nous voulons utilser une fonction renvoyant quelque chose, il faut utiliser **Function**
```
Function Ajouter_Deux(argument)
Ajouter_Deux = argument + 2
End Function
```
{% attention %}
La valeur renvoyée par la fonction doit posséder le même nom que la fonction.
{% endattention %}

## Les fonctions utiles en AppScript
Supposons que nous travaillons avec un document nommé "Suivi" et possédant deux feuilles : "Page de garde" et "KPI".

### Accéder à des fichiers et des feuilles de calcul
Pour pouvoir accéder à un document GSheet, plusieurs méthodes sont possibles :
```
Document = SpreadsheetApp.getActive(); // La variable Document permet maintenant de se référer au document GSheet ouvert.
DocumentBis = SpreadsheetApp.OpenByUrl("https://..."); // La variable DocumentBis permet de se référer au document dont on a donné l'url.

Feuille = Document.getSheetByName("KPI"); // La variable Feuille permet de se référer à la feuille "KPI" du document "Suivi".
FeuilleBis = Document.getActiveSheet(); // La variable FeuilleBis permet de se référer à la feuille active du document "Suivi".

Toutes_feuilles = Document.getSheets();
```
### Accéder ou modifier la valeur d'une cellule
```
Feuille = SpreadsheetApp.getActive().getSheetByName("KPI");
valeur = Feuille.getRange(3,2).getValue(); // valeur est égale au contenue de la cellule positionnée à la 3ème ligne, 2ème colonne.
Feuille.getRange(3,2).setValue("Nom d'assurance"); // La cellule de la 3ème ligne, 2ème colonne est maintenant égale à "Nom d'assurance".
```
### Dernière ligne ou colonne d'un tableau
Il est parfois intéressant de connaitre les dimensions d'un tableau afin de réaliser des boucles par exemple.
```
Feuille = SpreadsheetApp.getActive().getSheetByName("KPI");
derniere_ligne = Feuille.getLastRow();
derniere_colonne = Feuille.getLastColumn();
```
### Nom d'une feuille
```
Feuille = SpreadsheetApp.getActive().getActiveSheet();
nom = Feuille.getName(); // Nom de la feuille active
```
### Nombre de feuilles du classeur
```
Feuilles = SpreadsheetApp.getActive().getSheets();
Nbr = Feuilles.length;

Feuille = SpreadsheetApp.getActive().getActiveSheet();
numero = Feuilles.indexOf(Feuille);
```
{% note %}
Si l'index est **-1**, cela signifie que la feuille n'a pas été trouvée.
{% endnote %}

### Sortir d'une boucle ou d'une fonction
- Afin de sortir d'une boucle, on utilise **break**.
- Afin de sortir d'une fonction en cours, on utilise **return**.