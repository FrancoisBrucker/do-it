---
layout: layout/pok.njk

title: "POK 3: Google Apps Cure"
authors:
  - Sebastien Sarah

date: 2024-14-02

tags: 
  - "temps 3"
  - "Google Apps Script"
  - "Google Sheet"

résumé: "Ce MON traitera de l'apprentissage de Google Sheet et d'Apps Script et de leur application au travers d'un mini projet qui impliquera, une gestion d'une BDD, des liens entre les différentes applications Google (Forms, Sheets) et un traitement des données."

---
---

{%prerequis 'Niveau débutant'%} 
Prérequis : Aucun
{%endprerequis%}

## Sommaire

- [Introduction](#introduction)
- [Backlog](#backlog)
- [Recherches des ressources](#ressources)
- [Focus sur Google Sheet](#googlesheet)
- [Focus sur Google Apps Scripts](#googleAppscript)
- [Une courte présentation de Google Apps Cure](#projet)
- [Vers le sprint 2](#sprint2)

<h2 id=introduction> Introduction</h2>

J'ai déjà utilisé VBA à maintes reprises au cours de mon alternance et dans mon [premier POK](../temps-1/). Mais j'ai remarqué que si VBA était, jusque là, l'incontournable outil quand il s'agissait de créer des macros, le nom d'"Apps Script" commençait à s'entendre de plus en plus souvent. Alors je me suis dit, *pourquoi ne pas découvrir un peu de quoi il en retourne ??* Et puis comme ça je pourrai comparer les 2 langages, et me faire mon propre avis. 

<h2 id=backlog> Backlog</h2>

Voici mon backlog pour le sprint 1 : 

|Intitulé|Temps estimé|
|---|---|
|- Lecture des différents MON sur le sujet |45 mins|
|- Recherches et ajouts de ressources personnelles sur le sujet |30 mins|
|- Prise en main de Google Sheet à l'aide des ressources listées |30mins|
|- Application à un sujet de traitement de BDD |2h|
|- Prise en main de Google Apps Script à l'aide des ressources listées |1h30|
|- Entraînement à l'application de ces connaissances sur un sujet|3h|
|- Entraînement à la connexion d'Apps Scripts aux autres applications Google |1h30|
|- Définition du backlog pour le mini projet imaginé|15 mins|

<h2 id=ressources> Recherches des ressources</h2>

En ayant épluché tout le site de Do-It sur le sujet, voici un petit guide sur ce qui a déjà été traité et comment : 

|Numéro|Nom|Résumé|
|---|---|---|
|1|[Un peu d'Excel/Google Sheets pour mourir moins idiot](../../../TAING-Henri/mon/temps-2-1/) <br> de Henri Taing|- Des explications sur l'utilisation de notions de Google Sheet *(vue filtrée, tableau croisé dynamique, mise en forme conditionnelle, quelques fonctions...)* <br> - Recommandation pour Sheet et Apps Scripts des tutos de [ce site](https://www.sheets-pratique.com/) qui lui ont mis *"des paillettes dans les yeux*"|
|2|[Google Apps Script](../../../../2022-2023/Laeuffer-Savinien/mon/appsscript/) <br> de Savinien Laeuffer|- utilise la *doc fournie par Google sur son service* <br> - aborde les thèmes de **Toast**, **d'envoi de mails**, de **déclencheurs**, des **scripts HTML**, de **menus personnalisés** <br> - *REMARQUE :c'est assez pratique car il a mis dans son MON tous ses codes, mais on a peu d'aperçu sur le rendu de ce qu'il a fait* |
|3|[Temps 1 - MON - Google Apps Script](../../../../2022-2023/Romer-Kasimir/mon/MON1-1/) <br> de Kasimir Romer|- réalisation d'une to do list sur google sheet mise à jour automatiquement par action de l'utilisateur <br> - cite en ressource [cette vidéo youtube](https://www.youtube.com/watch?v=Nd3DV_heK2Q), de [la documentation Google](https://developers.google.com/apps-script/reference/spreadsheet?hl=fr) et de [la documentation JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference)|
|4|[Google Apps Script](../../../../2022-2023/Varnerot-Antoine/mon/google-app-script/) <br> de Antoine Varnerot|- conseille vivement les [tutos de Google](https://developers.google.com/apps-script/guides/sheets?hl=fr) et les tutos de [cette playlist Youtube](https://www.youtube.com/playlist?list=PLozmtcO5OqdqZZ6sP6faU18jIdyCiiYvS) <br> - pour s’entraîner, il propose d'utiliser [ce site](https://developers.googleblog.com/2022/04/getting-started-is-hardest-part-find.html) qui propose des idées de mini-projets à faire avec Google Apps Script <br> - Détails sur sa proposition pour le projet *"Clean up data in a spreadsheet"* |
|5|[Google Apps Script](../../../../2022-2023/Durand-Jean-Baptiste/mon/gglAppsScript/) <br> de Jean-Baptiste Durand|- c'est le seul à donner quelques explications à Google App Scripts (qu'est ce que c'est, les principales fonctionnalités, etc..) <br> - répertorie plusieurs formules basiques utiles et évoque la notion de *déclencheurs temporels*, qu'il n'a pas eu le temps de trop aborder mais il conseille [la documentation de Google](https://developers.google.com/apps-script/guides/triggers/installable?hl=fr) sur le sujet <br> - réalise ensuite un tricount sur Sheet avec Apps Script (*BEMOL: son lien vers le code source de son travail ne marche pas et on a accès à son Sheet qu'en lecture seule, donc pas possible d'accéder à sa macro...*)|
|6|[MON 1: Google apps script](../../../../2022-2023/Abdane-Ossama/mon/mon1/) <br> de Ossama Abdane|- a focalisé son MON sur les **triggers** : explications et quelques exemples de triggers classiques <br> - explique en détails les *déclencheurs temporels* et l'applique à une fonction qui envoie un mail tous les matins pour lui rappeler d'aller signer la feuille de présence <br> - utilise les mêmes ressources que dans les MON précédents, et y inclue [ce site](https://spreadsheet.dev/triggers-in-google-sheets) pour les triggers temporels|
|7|[MON 2.1: Google Apps Script : Rappel anniversaire](../../../../2022-2023/Abdane-Ossama/mon/mon2.1/)<br> par Ossama Abdane|-application des connaissances de son MON précédent sur la réalisation d'un outil qui prévient automatiquement par mail de la date d'anniversaire d'une personne dans une liste stockée sur Sheet|
|8|[MON 2 : Google Apps Script](../../../../2022-2023/Pont-Thomas/mon/gas/) <br> de Thomas Pont|- réalisation d'un outil pour *"automatiser l'envoi de mails personnalisés"* <br> - donne des conseils sur la gestion des dates dans Sheet <br> - explique la gestion de texte HTML avec Apps Script|

<h2 id=googlesheet> Focus sur Google Sheet</h2>

Pour m'entrainer, je me suis appuyée sur ce [fichier csv](olympics.zip) envoyé gracieusement par un  gentil collègue de IAM. 

Ce fichier traite de certaines caractéristiques de chaque vainqueur des JO *(l'athlète, son sexe, sa nationalité, la couleur de sa médaille, la catégorie dans laquelle il a gagné, etc...)*. 

### Ressources 
Je me suis dit que ça ferait une base parfaite pour m'entraîner sur Sheet. Pour cela j'ai étudié et appliqué les différentes parties du **cours sur Google Sheet** de [ce site](https://www.sheets-pratique.com/) qu'Henri avait conseillé, j'ai aussi utilisé [cette page](https://support.google.com/docs/table/25273?hl=f) de Google qui répertoriait un grand nombre de formules pour Sheet, et qui m'a été, ma foi, très utile. 

### Entrainement sur Sheet

Vous retrouverez [ici](https://docs.google.com/spreadsheets/d/1zAQRbf99pT2mR93Ry3i1bm-QLbhTylIE4CK-WcgO86I/edit?usp=sharing) un lien vers le Sheet que j'ai créé. 

- **onglet "olympics"** : base de données brut avec mise en forme conditionnelle de la couleur de chaque cellule de la colonne *"Medal"*, en fonction de la couleur de la médaille correspondante.
- **onglet "test formules"** : test de plusieurs formules pour mettre en valeur certaines données.
- **onglet "graphique"** : récupération des données de tous les pays *(via la formule UNIQUE())* pour venir chercher le nombre de médailles gagnées, de chaque couleur. Puis mise en forme de ces données sous la forme d'un graphique adapté
- **onglet "Tableau croisé dynamique"** : création d'un tableau croisé dynamique avec la gestion des *segments*.

Finalement, contente d'en être arrivée jusque là, j'ai voulu continuer, en essayant d'appliquer mon [MON 2.1](../../mon/temps-2.1/), en créant un tableau de bord sur Sheet. Mais là... je me suis heurtée à un mur : dès que j'ai commencé à avoir plusieurs graphiques et à manipuler les données, Sheet ne parvenait plus à actualiser correctement et le temps de réponse devenait parfois inquiétant. 
J'ai alors compris que Sheet n'était pas **DU TOUT** fait pour ça. Mais je suis restée sur ma faim. Alors j'ai fait mes petites recherches et j'ai découvert **Looker Studio**, le Power BI de Google. 

### A la découverte de Looker Studio

N'ayant jamais utilisé Power BI, je partais ici avec un oeil innocent. Pour savoir un peu dans quelle direction partir en ouvrant le logiciel, j'ai regardé [cette vidéo Youtube](https://www.youtube.com/watch?v=BVBvo9eKK40) qui expliquait très bien comment prendre en main l'outil. 
Il est assez intuitif et simple à utiliser alors 12mins47 étaient largement suffisantes pour savoir comment procéder. 
Je ne suis pas extrêmement rentrée dans les détails des options qu'offraient Looker Studio, car ce n'était pas le but ici, mais il a l'air assez complet *(ex: possibilité de créer des champs personnalisés calculés très pointus)*. 

Alors finalement, après 1h30 de dur labeur, je vous présente mon tableau de bord, avec lequel vous pouvez jouer [ici](https://lookerstudio.google.com/reporting/3a53aba0-98ac-4a1d-aa94-3af36f8d6195)

<img src=looker_studio.png>

<h2 id=googleAppscript> Focus sur Google Apps Scripts</h2>

### Ressources 

Après avoir lu autant d’encensements des vidéos youtube de [cette playlist youtube](https://www.youtube.com/playlist?list=PLozmtcO5OqdqZZ6sP6faU18jIdyCiiYvS), j'ai regardé toutes les vidéos. Et je dois dire qu'elle méritait les éloges, les vidéos étaient très complètes et très bien expliquées. *Je la recommande, moi aussi !* Mais je la complèterai quand même avec les explications de [sheets-pratique.com](https://www.sheets-pratique.com/) qui abordent des points cruciaux qui n'apparaissent pas dans les vidéos *(ex : comment créer un bouton sur Sheet et y affecter une macro, ou comment enregistrer un script directement depuis Sheet,...)*

### Entraînement sur Apps Script

Cependant, quand j'ai voulu passer à un exercice applicatif, ça a été compliqué... J'ai voulu utilisé [ce site](https://developers.googleblog.com/2022/04/getting-started-is-hardest-part-find.html), conseillé par Antoine qui répertorie des applications simples pour débutant à refaire pour se familiariser avec le langage. Mais j'ai été déçue du peu de quantité d'exercices qu'il y avait, et du fait que les exercices ne soient pas guidés dans leur réalisation, mais seule la correction est indiquée. 

J'ai donc voulu créer mon propre entraînement, pour cela il me fallait trouver l'inspiration. Je voulais trouver le moyen de parvenir à interagir avec l'utilisateur:

J'ai cherché sur [data.world](https://data.world/search?type=all) des BDD qui pourraient être intéressantes. J'en ai trouvées plusieurs qui traitaient de la composition de plusieurs aliments. J'aimais beaucoup le thème mais je les trouvais trop dures à exploiter.
En cherchant plus globalement sur internet, j'ai trouvé [celle-ci](https://www.kaggle.com/datasets/kaggle/recipe-ingredients-dataset) sur un site appelé Kaggle. *Cette BDD contenait une liste de recettes, la nationalité de la recette et les ingrédients*. J'ai tout de suite eu l'idée de faire un script qui permettrait de proposer à l'utilisateur des recettes en fonction des ingrédients et des types de cuisine qu'il aurait sélectionnés sur le sheet. _Un peu comme l'option "Frigo" de l'application de **Marmiton**, ou d'autres applications de **Frigos intelligents**_.

Mais la réalisation de mon idée affichait déjà quelques contraintes:

- **BEMOL n°1** : les fichiers à télécharger étaient sous le format JSON
- **BEMOL n°2** : il n'y avait aucun nom de recettes dans le fichier, juste des ID

Il en fallait plus pour m'arrêter.

#### Résolution des problématiques

##### BEMOL n°1 :

Je savais qu'il y avait la possibilité d'utiliser **Power Query** pour importer des fichiers JSON. J'ai juste regardé [cette vidéo](https://www.youtube.com/watch?v=SlAuMFCF-aQ) qui expliquait comment **importer et parsemer des données d'un fichier JSON sur Excel**. J'ai fait en sorte de *parsemer* les ingrédients de **2 façons**, pour pouvoir plus facilement traiter les données par la suite.

|**étendre sur plusieurs lignes**|**extraire les valeurs**|
|---|---|
|<img src=json_excel1.png>|<img src=json_excel2.png>|
|Permet d'avoir un ingrédient par ligne|Permet d'avoir tous les ingrédients dans une même cellule|

##### BEMOL n°2 :

<img align="right" width=150 src=API_chatGPT.png>

L'outil idéal pour trouver le nom d'une recette facilement à partir de l'origine de la recette et de ses ingrédients était évident : **ChatGPT**. Mais lui poser la question pour chaque ligne était trop fastidieux. Après quelques recherches, j'ai vu qu'il était possible de connecter facilement **l'API de ChatGPT** à **Sheet**. *Processus très bien expliqué dans [cette vidéo](https://www.youtube.com/watch?v=2OukmKPCW1I)*

Ni une ni deux, je m'y atèle. 
- **première étape** : traduire tous les textes *(origine et ingrédients)* en français. Facile avec la formule de *Google Translate*. (Mais qui laisse à désirer parfois quand même)

```
=GOOGLETRANSLATE(B2;"en";"fr")
```

- **deuxième étape** : concaténer les informations de l'origine de la recette et des ingrédients pour *faciliter la requête ChatGPT*

```
="origine de la recette : "&C2&" / ingrédients de la recette :"&E2
```

-**troisème étape**: faire la requête ChatGPT
```
=GPT("peux tu me donner le nom de la recette seulement dont ";F2)
```

On obtient alors en résultat : 
<img src=nom_recette.png>

{%info "REMARQUES"%}
- chaque requête à l'API est **payante**. Le prix dépend du type de la requête. Ce genre de requête n'est pas très cher. Mais comme mes crédits gratuits n'étaient pas illimités, j'ai choisi de restreindre à **62 recettes**.
- les requêtes sont re-effectuées à **chaque ouverture du Sheet**. J'ai donc désactivé le mode *"dépense"*. Il se peut qu'à l'ouverture, les cellules de la colonne ChatGPT indiquent **#ERROR!**
{%endinfo%}

#### Mise en forme du sheet

Après adaptation des données obtenues *(ex: suppression des lignes que ChatGPT ne trouvait pas)*. J'ai tout mis proprement dans un onglet **BDD recettes**. 

J'ai créé un onglet **CHOIX** où je suis venue placer la liste de **tous les ingrédients disponibles** *(obtenue en réalisant une fonction UNIQUE sur la colonne "ingrédients" du fichier généré avec l'étape "étendre sur plusieurs ligne" d'Excel, expliqué plus haut)* et de **tous les types de cuisine disponibles** *(même process)*.

On rajoute ensuite des **case à cocher** (Menu *Insertion*>*Case à cocher*). Et hop, le tour est joué ! 

#### Réalisation du script

Besoin de 2 fonctions : 

- une fonction **contientElement** qui va venir tester si un élément est dans un tableau *(car le cas se présente plusieurs fois dans la fonction principale)*


{% details "contientElement" %}
```javascript
function contientElement(array, element) {
  return array.includes(element); // Retourne true si l'élément est trouvé dans le tableau
}
```
{% enddetails %}

- une fonction **getRecipe** qui récupère les choix de l'utilisateur et les recherche dans la BDD de recettes pour lui trouver une recette remplissant tous les critères, et lui fournir tous les ingrédients de cette recette.

{% details "getRecipe" %}
```javascript
function getRecipe() {
  //Definition des paramètres des pages 
  let mainSheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('CHOIX');
  let mainLastRow = mainSheet.getLastRow();
  let mainRange = mainSheet.getDataRange();

  let backSheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('BDD ingrédients');
  let backLastRow = backSheet.getLastRow();
  let backRange = backSheet.getDataRange();

  var ingredients = [];
  var typeCuisine = [];
  var recetteIngredients = [];

  var recetteRetenue = 'aucune';

  //On récupère les ingrédients sélectionnés par l'utilisateur + types de cuisine
  for (let i=2; i <= mainLastRow; i++){

    if (mainRange.getCell(i,1).getValue()===true){
      ingredients.push(mainRange.getCell(i,2).getValue())
    }
    if (mainRange.getCell(i,4).getValue()===true){
      typeCuisine.push(mainRange.getCell(i,5).getValue())
    }
  }
  //On parcout toute la liste de BDD recettes
    for (let k=2; k<= backLastRow;k++){
      var ingredientTest = backRange.getCell(k,5).getValue()
      var typeTest = backRange.getCell(k,3).getValue();
      
      //Un élement correspond aux 2 conditions, on garde en mémoire la recette correspondante
      if (contientElement(ingredients,ingredientTest) && contientElement(typeCuisine,typeTest)){
        recetteRetenue = backRange.getCell(k,6).getValue();
        console.log(recetteRetenue);
        break; //Une recette a été trouvée, on sort de la boucle
      }
    }
  //on vient récupérer la liste des ingrédients de la recette
  for (let l=2; l<= backLastRow; l++){
    if (backRange.getCell(l,6).getValue()===recetteRetenue){
      recetteIngredients.push(backRange.getCell(l,5).getValue());
    }
  }
  
  //on affiche le message finale 
  var ui = SpreadsheetApp.getUi();
  if (recetteRetenue==='aucune'){
    var message = "Aucune recette n'a été trouvée... Ressayez avec d'autres ingrédients, ou de voyagez ailleurs?"
  }else{
    var message = "Vous pouvez réaliser un(e) "+recetteRetenue + "\n\n Il vous faudra tous ces ingrédients:\n -" + recetteIngredients.join('\n-');
  }
  ui.alert('Voici une recette possible', message, ui.ButtonSet.OK);
}
```
{% enddetails %}

#### Test du script

Aujourd'hui, j'avais envie de manger **italien**. Mais je n'avais chez moi que des **cacahuètes grillées** et de la **canneberge séchée**. 
*Qu'est ce que j'allais bien pouvoir cuisine?*

<img width=350 src=resultat_recette.png>




{%info "REMARQUES/DEFAUTS"%}
- il y a beaucoup d'ingrédients qui sont en **double** *(ex: beurre, beurre fondu, beurre sans sel)*
- certaines traductions de Google sont très approximatives *(ex: Il traduit "bifteck de flanc" un "flank steak", qui signifie "bavette")*
{%endinfo%}

--- 

{%prerequis 'Lien vers le projet'%} 
- [Lien vers le Sheet](https://docs.google.com/spreadsheets/d/1KGEUPpCguz-CgjBRoZtw-efDRjphKRTtqgmCwERGkHs/edit?usp=sharing)
- [Lien vers le script](https://script.google.com/u/0/home/projects/16E4KcCd9lwJmOOt_XYX1SBhEZnGqHfAb8tCSZGMxqZN0VCO6gRwqTxmR/edit)
{%endprerequis%}

<h2 id=projet> Une courte présentation de Google Apps Cure</h2>


<h2 id=sprint2> Vers le sprint 2</h2>

Si on reprend le backlog du sprint 1 que je m'étais fixé :

|Intitulé|Temps estimé|Temps réalisé|
|---|---|---|
|- Lecture _**et synthétisation**_  des différents MON sur le sujet |45 mins|**1h**|
|- Recherches et ajouts de ressources personnelles sur le sujet |30 mins|**/**|
|- Prise en main de Google Sheet à l'aide des ressources listées |30mins|**15mins**|
|- Application à un sujet de traitement de BDD |2h|**30 mins**|
|- _**Réalisation d'un tableau de bord sur Looker Studio**_ |*/*|**2h**|
|- Prise en main de Google Apps Script à l'aide des ressources listées |1h30|**1h10**|
|- _**Recherche d'une BDD adaptée à l'entraînement sur Apps Script**_ |*/*|**50mins**|
|- Entraînement à l'application de ces connaissances sur un sujet|3h|**4h15**|
|- Entraînement à la connexion d'Apps Scripts aux autres applications Google |1h30|**/**|
|- Définition du backlog pour le mini projet imaginé|15 mins|**/**|

Au final, j'ai passé *légèrement* plus que 10h sur ce Sprint 1. Mais c'est mieux ainsi. Ce mini projet sur Apps Script m'a permis de **bien prendre en main** les **macros Google**, et de faire en sorte que l'utilisation de **sheet** devienne plus **instinctive**. Ce qui sera un point essentiel dans la réalisation du sprint 2.

On peut alors redéfinir le backlog pour le sprint 2 :

|Intitulé|Temps estimé|
|---|---|
|- Définition du backlog pour le mini projet imaginé|15 mins|
|- Recherches sur les connexions Apps Script avec les autres applications Google *(Form,Gmail)* |30 mins|
|- Recherche et récupération des ressources utiles sur les déclencheurs|30 mins|
|- Mise en forme des données récupérées |2h|
|- Mise au point du contenu du questionnaire et création du Form|45 mins|
|- Codage du script de récupération des données du Form|45 mins|
|- Codage du script de gestion de données du Sheet|3h mins|
|- Codage du script de gestion de l'envoi des mail|45 mins|
|- Réalisations de divers tests et correction du code|1h30|
