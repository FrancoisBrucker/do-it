---
layout: layout/mon.njk

title: "Google Apps Script"
authors:
  - Savinien Laeuffer
date: 2022-10-19

tags:
  - 'temps 1'
---

<!-- début résumé -->
Google Apps Script
<!-- fin résumé -->

## Description

Le but de ce MON est de découvrir Google Apps Script, un outil/language de programmation développé par Google permettant d'executer des scripts entre les différents services proposés par Google. J'ai présenté ça sous la forme d'un tutoriel où j'explique différents outils de Google Apps Script , et j'essaye par la suite de les combiner entre eux pour en faire quelque chose d'utile et pratique.
Pour ce MON je me suis globalement servi de la documentation fournie par Google sur son service.
Apps Script apparait dans l'onglet Extension dans différents services proposés sur Google Drive (Sheets, Document)`

## Afficher un Toast

Pour afficher un toast, ce petit composant qui apparait en bas à droite de l'écran pour afficher un message, on peut utiliser la commande ```SpreadsheetApp.getActiveSpreadsheet().toast()``` comme suit:

```
SpreadsheetApp.getActiveSpreadsheet().toast('Les mails ont bien été envoyés !', 'Confirmation', 3);
```

Le premier argument correspond au corps du toast, le 2ème au titre du toast, et le 3ème, au nombre de secondes d'affichage (mettre -1 pour ne pas fermer automatiquement la notification)

## Envoyer un mail à une liste de diffusion


##### a. La liste de diffusion et le message (Google Sheets) 

Supposons que l'on a une liste de diffusion immense et on veut envoyer un message personnalisé à tous les destinataires en mentionnant à chacun leur prénom en début de mail.
Pour envoyer un mail à une liste de diffusion, il me faut tout d'abord une liste de diffusion que je crée comme ceci sur Google Sheets:

<figure>
  <img src="../mon2sheets.png">
  <figcaption>La liste de diffusion</figcaption>
</figure>

4 Contacts suffisent pour notre exemple.

Maintenant que nous avons la liste de diffusion, je crée mon message personnalisé dans une autre cellule:

<figure>
  <img src="../mon2texte.png">
  <figcaption>Le message</figcaption>
</figure>

##### b. Le script d'envoi

Maintenant que tout est prêt je peux commencer à écrire mon script. J'ouvre Appscript et j'entre le code suivant pour initialiser:

```
function MassEmails() {
   var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("listediffusion");
   var range = sheet.getRange("A2:B5").getValues();
   var template = sheet.getRange("E1").getValue();

   Logger.log(range);
}
```

Je sauvegarde mon code, et l'execute. A noter qu'il est important de renommer sa feuille "listediffusion" afin de pouvoir la trouver avec le script. Une fois exécuté, Google nous demande quelques autorisations que l'on passe sans problème. Des logs s'affichent:

```
00:36:02
Infos
[[zinedine.zidane@gmail.com, Zizou], [antoine.varnerot@centrale-marseille.fr, Raton], [yannick.noah@caramail.com, Yannick], [savinien.laeuffer@wanadoo.com, Moi]]
```

On a bien récupéré les informations dont nous avons besoin. La prochaine étape est de créer les différents mails en remplaçant les prénoms. On ajoute donc une boucle for comme ci-après:

```
for(var i=0; i<range.length;i++) {
  var finalMessage = template.replace("PRENOM", range[i][1])
}
```
En executant, on s'apperçoit dans les logs que le dernier message s'est affiché et correspond bien au dernier message.
On cherche maintenant à envoyer ces mails aux destinataires, on ajoute la ligne suivante dans la boucle for, juste après avoir défini ```finalMessage```:

```
GmailApp.sendEmail(range[i][0], "Salut mon pote", finalMessage)
```

Votre code devrait ressembler à ceci:

```
function MassEmails() {
   var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("listediffusion");
   var range = sheet.getRange("A2:B5").getValues();
   var template = sheet.getRange("E1").getValue();

   for(var i=0; i<range.length;i++) {
     var finalMessage = template.replace("PRENOM", range[i][1])
     GmailApp.sendEmail(range[i][0], "Salut mon pote", finalMessage)
   }

   //Logger.log(finalMessage);
}
```

Il suffit d'exécuter, passer les autorisations, et le tour est joué !

## Les déclencheurs simple

Les déclencheurs sont des fonctions qui s'exécutent automatiquement lorsque un évènement se produit (changement d'une cellule, ouverture d'un document).
Pour utiliser un déclencheur simple, il suffit de nommer sa fonction d'une certaine manière, voici les noms à donner et ce à quoi ils correspondent:

 - ```onOpen(e)```: Se lance lorsqu'on ouvre un fichier Google
 - ```onIntall(e)```: Se lance lorsqu'un module complémentaire est installé à partir de Google Docs, Sheets, Slides ou Forms.
 - ```onEdit(e)```: Se lance lorsqu'on modifie une valeur dans un Google Sheets
 - ```onSelectionChange(e)```: Se lance lorsque qu'un utilisateur modifie une certaine sélection dans un Google Sheets
 - ```doGet(e)```: Se lance lorsque l'utilisateur visite une application web ou qu'un programme envoie une requête HTTP ```GET``` à une application web
- ```doPost(e)```: Même chose mais avec une requête ```POST```

## Du HTML dans Apps Script

Il est aussi possible de créer et diffuser des fichiers HTML avec Apps Script. En cliquant sur le ```+``` pour ajouter un fichier, on nous propose de créer un fichier HTML. Créons donc un fichier ```index.html```:

```
<!DOCTYPE html>
<html>
  <head>
    <base target="_top">
  </head>
  <body>
    Hello, World!
  </body>
</html>
```
Si on veut diffuser ce fichier HTML, le code doit inclure une fonction ```doGet(e)``` (voir partie précédente) et doit renvoyer un objet ```HtmlOutput``` comme suit:

```
function doGet() {
  return HtmlService.createHtmlOutputFromFile('index');
}
```

Si par exemple on souhaite afficher ce ficher HTML dans une boite de dialogue, on peut utiliser le code suivant:

```
function openDialog() {
  var html = HtmlService.createHtmlOutputFromFile('index');
  SpreadsheetApp.getUi()
      .showModalDialog(html, 'Dialog title');
}
```

## Créer un menu personnalisé dans Google Sheets

On souhaite créer un menu sur le Google Sheets à partir des fonctions que l'on a créé. Cela permet d'exécuter les scripts créés plus rapidement. En plus de cela, on souhaite que ce menu se crée dès que l'on ouvre la feuille de calcul. On va donc d'abord appeler notre fonction comme suit:

``` 
  onOpen(e) {

  }
``` 

On ajoute la création d'un menu:

``` 
  onOpen(e) {
    SpreadsheetApp.getUi()
      .createMenu('⚙️ Outils MON2')
      .addItem('Item A', 'itemA')
      .addItem('Item B', 'itemB')
      .addToUi();
  }
``` 

On ajoute notre fonction pour envoyer des e-mails à une liste de diffusion et l'affichage de la boite de dialogue et on fait le lien entre les boutons du menu et les fonctions:

``` 
  onOpen(e) {
    SpreadsheetApp.getUi()
      .createMenu('⚙️ Outils MON2')
      .addItem('Envoyer les e-mails', 'MassEmails')
      .addItem('Diffuser HTML', 'openDialog')
      .addToUi();
  }

  function MassEmails() {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("listediffusion");
    var range = sheet.getRange("A2:B5").getValues();
    var template = sheet.getRange("E1").getValue();

    for(var i=0; i<range.length;i++) {
      var finalMessage = template.replace("PRENOM", range[i][1])
      GmailApp.sendEmail(range[i][0], "Salut mon pote", finalMessage)
    }
  }

  function openDialog() {
    var html = HtmlService.createHtmlOutputFromFile('index');
    SpreadsheetApp.getUi()
        .showModalDialog(html, 'Dialog title');
  }
```

Et pour finir on peut afficher un toast de confirmation pour dire que les e-mails sont bien envoyés:

``` 
  onOpen(e) {
    SpreadsheetApp.getUi()
      .createMenu('⚙️ Outils MON2')
      .addItem('Envoyer les e-mails', 'MassEmails')
      .addItem('Diffuser HTML', 'openDialog')
      .addToUi();
  }

  function MassEmails() {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("listediffusion");
    var range = sheet.getRange("A2:B5").getValues();
    var template = sheet.getRange("E1").getValue();

    for(var i=0; i<range.length;i++) {
      var finalMessage = template.replace("PRENOM", range[i][1])
      GmailApp.sendEmail(range[i][0], "Salut mon pote", finalMessage)
    }

    SpreadsheetApp.getActiveSpreadsheet().toast('Les mails ont bien été envoyés !', 'Confirmation', 3);
  }

  function openDialog() {
    var html = HtmlService.createHtmlOutputFromFile('index');
    SpreadsheetApp.getUi()
        .showModalDialog(html, 'Dialog title');
  }
```

Et voilà le résultat:

<figure>
  <img src="../menu.png">
  <figcaption>Le message</figcaption>
</figure>

Je vais éviter de lancer le programme d'envoi de mails pour pas que ```zinedine.zidane@gmail.com``` reçoive un message bizarre, mais en ce qui concerne la boite de dialogue à partir du fichier ```index.html``` on obient cela:

<figure>
  <img src="../dialog.png">
  <figcaption>Le message</figcaption>
</figure>