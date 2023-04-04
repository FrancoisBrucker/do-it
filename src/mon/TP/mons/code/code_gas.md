---
layout: layout/post.njk

title: "MON 2 : Google App Scripts"
authors:
 - Thomas Pont

tags:
---

<!-- Début Résumé -->

Code de mon MON.
<!-- Début Résumé -->

```java
function gestionConvocations() {
  const convocationMailTemplateDocId = "18RqDPW3E0JV-08OpF0aM5vteJQaCg8PNqv5ixK9WqlM";
  const convertedDocHTML = ConvertGoogleDocToCleanHtml(convocationMailTemplateDocId);
  const inscriptionsSheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Inscriptions");
  const inscriptions = inscriptionsSheet.getDataRange().getValues();
  for (let i=1;i<inscriptions.length;i++) {
    const nom = inscriptions[i][0];
    const prenom = inscriptions[i][1];
    const email = inscriptions[i][2];
    //const date = inscription[i][3];
    const date = new Date(inscriptions[i][3]);
    const dateFormatee = Utilities.formatDate(date, "GMT+1", "dd/MM/YYYY");
    const heure = inscriptions[i][4];
    const sujet = inscriptions[i][5];
    const convocationDejaEnvoyee = inscriptions[i][6];
    if (nom != "" && prenom != "" && email != "" && date != "" && sujet != "" && heure != "" && !convocationDejaEnvoyee) {
      const variables = { "Prenom":prenom, "Nom":nom, "Evenement":sujet, "Date":dateFormatee, "Heure": heure, "email":email};
      const isMailSent = envoiEmail(convertedDocHTML, variables, "Convocation")
      if (isMailSent) {
        inscriptionsSheet.getRange(i+1,7).setValue("TRUE");
      }
    }
  }
}

function envoiEmail(emailTemplateHTML, variables, mailSubject) {
  const mailTo = variables.email;
  var mailBodyHTML = (emailTemplateHTML.html).slice();
  var options = {};
  for(const id in variables)
  {
    if(variables.hasOwnProperty(id)) {
      mailBodyHTML = mailBodyHTML.replace("["+id+"]",variables[id]);
    }
  }
  options['htmlBody'] = mailBodyHTML;
  var inlineImages = {};
  for (let j=0; j<emailTemplateHTML.images.length; j++) {
    inlineImages[[emailTemplateHTML.images[j].name]] = emailTemplateHTML.images[j].blob;
  }
  options['inlineImages'] = inlineImages;
  try {
    Logger.log("Envoi convocation à :"+mailTo);
    MailApp.sendEmail(mailTo, mailSubject, mailBodyHTML.replace(/<[^>]*>/g, ''), options);
    return true;
  }
  catch (e) {
    Logger.log("Error : " + e.message + "\n" + e.stack);
    Logger.log(JSON.stringify(variables));
    Logger.log("Le email n'a pas pu être délivré");
  }
  return false;
}
```
