---
layout: layout/mon.njk

title: "MON 2 : Google Apps Script"
authors:
 - Thomas Pont

date: 2022-10-19

tags:
  - 'temps 1'
  - 'google apps script'
  - 'automatisation'
---

<!-- Début Résumé -->

Google Apps Script
<!-- Début Résumé -->

## Objectif de ce MON

L'objectif de ce MON est d'automatiser une tâche avec Google App Script.

Ici on cherchera à automatiser l'envoi de mails personnalisés. à des personnes.

Pour cela, on va réaliser un programme qui va automatiser l'envoi de mail lors de l'organisation d'évènements (réunions, cours..). A la fin, il faudrait que l'on ait juste à indiquer dans un Google Sheet, le prénom, le nom, le mail du participant ainsi que la nature, la date et l'heure de l'évènement auquel il est convié et qu'un mail comme celui qui suit s'envoie automatiquement.

```txt
Bonjour Jean Dupont,

Vous êtes conviés à la réunion de fin de projet le 24/10/2022 à 15h.

Cordialement,
Yves Martin
```

## Réalisation de ce programme

Dans un premier temps, j'ai relu et étudié les précédents MON fait sur Google App Script pour revoir les principales fonctionnalités déjà utilisé et principalement celle de l'envoi de mail.

### Fichier texte

Pour commencer on crée un Google Doc avec le texte que l'on souhaite envoyer aux différents destinataires du mail.

```txt
 Bonjour [Prenom] [Nom],

 Vous êtes conviés [Evenement] le [Date] à [Heure].

 Cordialement,
 Yves Martin
```

Les éléments entre crochets seront ensuite automatiquement remplacé en fonction des informations sur la personne et sur l'évènement.

On doit ensuite convertir ce texte en HTML pour qu'il puisse être bien envoyé. Pour cela, on récupère une fonction publique disponible sur ce [Github](https://github.com/oazabir/GoogleDoc2Html/blob/master/code.js).
On nomme le texte ainsi converti mailBodyHTML

### Google Sheet

On crée un Google Sheet permettant de réunir les éléments des mails que l'on doit envoyer. On le place dans un onglet intitulé Inscriptions.

|Nom |Prénom | Mail | Date | Heure | Nom Evènement |
|:----|:----|:----|:----|:----|:----|
|Dupont |Jean | jean.dupont@gmail.com | 24/10/2022 | 15h | à la réunion de fin de projet |
|Dulieu |Anna | anna.dulieu@gmail.com | 24/10/2022 | 15h | à la réunion de fin de projet |

### Personnalisation du mail

Il faut ensuite qu'on écrive un script qui prend les informations du tableau et qui complète automatiquement le texte du mail.

Dans une fonction, on extrait les données du tableau de cette manière :

```java
const nom = inscriptions[i][0];
const prenom = inscriptions[i][1];
const email = inscriptions[i][2];
const date = new Date(inscriptions[i][3]);
const dateFormatee = Utilities.formatDate(date, "GMT+1", "dd/MM/YYYY");
const heure = inscriptions[i][4];
const sujet = inscriptions[i][5];
```

{% attention "**Attention** aux dates" %}
Il faut faire attention à la gestion des dates dans le tableau. Si on fait seulement

```java
const date = inscriptions [i][3];
```

rien ne sera extrait du tableau
De même si on formate pas la date on récupère également l'heure de minuit ainsi que le fuseau horaire de là où on se situe.
Il est donc important de bien l'extraire et de bien la formater.
{% endattention %}

On place toutes ses données ainsi récupérées dans un tableau *variables*.
Pour compléter le texte on utilise la fonction suivante :

```java
  for(const id in variables)
  {
    if(variables.hasOwnProperty(id)) {
      mailBodyHTML = mailBodyHTML.replace("["+id+"]",variables[id]);
    }
  }
  ```

  Ceci permet de lire le texte du mail et de remplacer les [] par l'information correspondante.

### Envoi du mail

Il faut maintenant lier les scripts pour le texte ainsi former puisse être envoyé et qu'il le soit à la bonne personne.

Pour cela, on peut utiliser la commande ci-dessous :

```java
MailApp.sendEmail(mailTo, mailSubject, mailBodyHTML.replace(/<[^>]*>/g, ''), options);
```

On peut choisir l'intitulé tel que Convocation qu'on peut stocker dans une constante.

On peut retrouver ici le tableau avec le Google App Script final. L'envoi du mail se fait lorsqu'on l'on lance la fonction gestionConvocations.

Ainsi on peut lancer manuellement cette fonction et le bon mail s'enverra à Jean et Anna. Il reste cependant un problème. Si on décide d'envoyer ce mail à quelqu'un d'autre, qu'on rajoute cette personne dans le tableau, le mail se renverra également à Jean et Anna.
Pour pallier à ce problème on peut ajouter une colonne intitulée *Mail envoyé*. On place des cases non cochées dans ce tableau. Lorsque le mail est bien envoyé un ajoute une ligne dans le code pour que la case soit cochée.

```java
inscriptionsSheet.getRange(i+1,7).setValue("TRUE");
```

Si on relance le script, en vérifiant si la case est bien décochée, seules les lignes non cochées vont recevoir le mail.

## Lien vers le code

[Mon code](../code/code_gas)
