---
layout: layout/post.njk

title: "MON 2 : Google Apps Script"
authors:
 - Thomas Pont

tags: ['Google Apps Script']
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

Vous êtes conviés à la réunion de fin de projet le 24/10/2022 à 15h dans la salle de réunion n°2.

Cordialement,
Yves Martin
```

## Réalisation de ce programme

Dans un premier temps, j'ai relu et étudié les précédents MON fait sur Google App Script pour revoir les principales fonctionnalités déjà utilisé et principalement celle de l'envoi de mail.

### Fichier texte

Pour commencer on crée un Google Doc avec le texte que l'on souhaite envoyer aux différents destinataires du mail.

```txt
 Bonjour [Prenom] [Nom],

 Vous êtes conviés [Evenement] le [Date] à [Heure] dans [Lieu].

 Cordialement,
 Yves Martin
```

Les éléments entre crochet seront ensuite automatiquement remplacé en fonction des informations sur la personne et sur l'évènement.

### Google Sheet

### Personnalisation du mail

### Envoi du mail

### Automatisation
