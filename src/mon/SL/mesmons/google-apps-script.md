---
layout: layout/post.njk

title: "Google Apps Script"
authors:
  - Savinien Laeuffer

---

<!-- début résumé -->
Google Apps Script
<!-- fin résumé -->

## Description

Le but de ce MON est de découvrir Google Apps Script, un outil/language de programmation développé par Google permettant d'executer des scripts entre les différents services proposés par Google.
Apps Script apparait dans l'onglet Extension dans différents services proposés sur Google Drive (Sheets, Document)

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
      .addToUi();
  }
``` 

On ajoute notre fonction pour envoyer des e-mails à une liste de diffusion et on fait le lien entre le bouton du menu et la fonction:

``` 
  onOpen(e) {
    SpreadsheetApp.getUi()
      .createMenu('⚙️ Outils MON2')
      .addItem('Envoyer les e-mails', 'MassEmails')
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
```

Et pour finir on affiche un toast de confirmation pour dire que les e-mails sont bien envoyés:

``` 
  onOpen(e) {
    SpreadsheetApp.getUi()
      .createMenu('⚙️ Outils MON2')
      .addItem('Envoyer les e-mails', 'MassEmails')
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
```