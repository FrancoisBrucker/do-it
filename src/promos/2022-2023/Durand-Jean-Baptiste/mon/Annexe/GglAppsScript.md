---
layout: layout/post.njk

title: "Annexe du MON Google Apps Script"
authors:
  - Jean-Baptiste Durand
---

Voici le code source de mon projet pour le MON de Google Apps Script. [lien vers le site](../../GglAppsScript)

Il permet de créer un Google Sheet fonctionnant comme un Tricount.

```javascript

////////////////////////////////
// [START modifiable parameters]
var tricountSettings = {
  sourceSheet: 'Ajout_achat',
  targetSheet: 'Historique',
  statSheet: 'Statistiques',
  people:["Personne 1","Personne 2", "Personne 3"]
}
// [END modifiable parameters]
////////////////////////////////


/**
* Take the form from the SourceSheet to add it in the TargetSheet
* It add also formulas to calculate the impact on everybody balance

* I built this function, inspired by the work of --Hyde 
* see https://support.google.com/docs/thread/41717054
*/
function tricountAddToHistory() {


  var timestamp = new Date();

  // Parameters

  let nb_people = tricountSettings.people.length


  // Import Sreadsheet

  var ss = SpreadsheetApp.getActive();
  var sheet = ss.getSheetByName(tricountSettings.targetSheet);
  if (!sheet) {
    sheet = ss.insertSheet(tricountSettings.targetSheet);
    sheet.appendRow(['Timestamp', 'Data']);
  }

  let A1_range = tricountSettings.sourceSheet + "!A2:" + columnToLetter(3+nb_people) + "2"
  var range = ss.getRange(A1_range);
  var values = range.getValues();


  // Storage cells

  var casesToDelete = [];
  var turnTrueCases = []
  var historiqueRow = [timestamp];

  // Generate ation to do
  let caseDescision=["move","move","move"]
  for(let i=0;i<nb_people;i++){
    caseDescision.push("turnTrue")
  }

  //loop actions
  for (var column = 0, numcolumns = values[0].length; column < numcolumns; column++) {
    var action = null;
    action = caseDescision[column]
    switch (action) {
      case 'move':
        historiqueRow = historiqueRow.concat(values[0][column]);
        casesToDelete.push(column);
        break;
      case 'turnTrue':
        historiqueRow = historiqueRow.concat(values[0][column]);
        turnTrueCases.push(column);
        break;
      default:
        ;
    }
  }

  // row where to put, to add formulas
  const wherePut = sheet.getRange(1,10+ 2*nb_people).getValue() + 1

  //add to TargetSheet the values of the SourceSheet
  sheet.appendRow(historiqueRow);

  //formulas to add
  var formulas=[]
  formulas = formulas.concat("=COUNTIF(R[0]C[-"+(nb_people)+"]:R[0]C[-1];TRUE)")

  for(let i=0;i<nb_people;i++){
    formulas = formulas.concat("=IF(R[0]C[-"+(2+nb_people+i)+"]=\""+tricountSettings.people[i]+"\";R[0]C[-"+(3+nb_people+i)+"];0) - IF(R[0]C[-"+(1+nb_people)+"];R[0]C[-"+(3+nb_people+i)+"]/R[0]C[-"+(1+i)+"];0)")
  }
  
  sheet.getRange(tricountSettings.targetSheet+"!"+columnToLetter(5+nb_people)+wherePut+":"+columnToLetter(5+2*nb_people)+wherePut).setFormulasR1C1([formulas])
  sheet.getRange(tricountSettings.targetSheet+"!"+columnToLetter(7+2*nb_people)+wherePut+":"+columnToLetter(8+2*nb_people)+wherePut).setFormulasR1C1([["=SUM(R[0]C[-"+(1+nb_people)+"]:R[0]C[-2])","=MONTH(R[0]C[-"+(7+2*nb_people)+"])"]])


  // Delete in SourceSheet cases or turn them to true
  if (casesToDelete.length) {
    var sourceSheet = range.getSheet();
    var rowStart = range.getColumn();
    for (var i = casesToDelete.length - 1; i >= 0; i--) {
      sourceSheet.getRange(2, rowStart + casesToDelete[i]).clear();
    }
  }

  if (turnTrueCases.length){
    var sourceSheet = range.getSheet();
    var rowStart = range.getColumn();
    for (var i = turnTrueCases.length - 1; i >= 0; i--) {
      sourceSheet.getRange(2, rowStart + turnTrueCases[i]).setValue(true);
    }
  }

  //turn the button to validate to false
  SpreadsheetApp.getActiveSheet().getRange(2, 5+nb_people).setValue(false);
}

/**
 * Return the letter of the column, having the number
 * https://stackoverflow.com/questions/21229180/convert-column-index-into-corresponding-column-letter
 */

function columnToLetter(column)
{
  var temp, letter = '';
  while (column > 0)
  {
    temp = (column - 1) % 26;
    letter = String.fromCharCode(temp + 65) + letter;
    column = (column - temp - 1) / 26;
  }
  return letter;
}

/**
 * trigger the function tricountAddToHistory, when the form is ready
 */
function onEdit(e){
  const value = SpreadsheetApp.getActive().getSheetByName(tricountSettings.sourceSheet).getRange(2, 6+tricountSettings.people.length).getValue();
  if(value){
    tricountAddToHistory()
  }
}

/**
 * Generate all the cells needed to make it work
 */
function generateSheet(){
  var ss = SpreadsheetApp.getActive();
  var sourceSheet = ss.getSheetByName(tricountSettings.sourceSheet)
  var targetSheet = ss.getSheetByName(tricountSettings.targetSheet);
  var statSheet = ss.getSheetByName(tricountSettings.statSheet)
  if (!sourceSheet) {
    sourceSheet = ss.insertSheet(tricountSettings.sourceSheet);
  }else{sourceSheet.clear()}
  if (!targetSheet) {
    targetSheet = ss.insertSheet(tricountSettings.targetSheet);
  }else{targetSheet.clear()}
  if (!statSheet) {
    statSheet = ss.insertSheet(tricountSettings.statSheet);
  }else{targetSheet.clear()}

  const nb_people = tricountSettings.people.length


  // SourceSheet
  sourceSheet.appendRow(["Commentaire","Prix","Payé par"].concat(tricountSettings.people).concat(["","Valider"]))
  var liste=["","",""]
  for(let i=0;i<nb_people;i++){
    liste.push("TRUE")
  }
  liste=liste.concat(["","FALSE"])
  sourceSheet.appendRow(liste)

  sourceSheet.getRange(2,6+nb_people).setFormula("=AND(R[0]C[-1],NOT(ISBLANK(B2)),NOT(ISBLANK(C2)),OR(D2:"+columnToLetter(3+nb_people)+"2))")


  // https://spreadsheet.dev/working-with-checkboxes-in-google-sheets-using-google-apps-script
  sourceSheet.getRange("D2:"+columnToLetter(3+nb_people)+"2").insertCheckboxes()
  sourceSheet.getRange(columnToLetter(5+nb_people)+"2").insertCheckboxes()


  //https://developers.google.com/apps-script/reference/spreadsheet/data-validation-builder
  var cell = sourceSheet.getRange('C2');
  var range = sourceSheet.getRange('D1:'+columnToLetter(3+nb_people)+'1');
  var rule = SpreadsheetApp.newDataValidation().requireValueInRange(range).build();
  cell.setDataValidation(rule);

  sourceSheet.getRange(columnToLetter(6+nb_people)+"2").setFontColor("white")

  //TargetSheet
  
  liste = ["Timestamp","Commentaire","Prix","Payé par"].concat(tricountSettings.people)
  liste.push("Nb Personnes")
  tricountSettings.people.forEach(person=>{
    liste.push("Coût "+person)
  })
  liste.push("")
  liste.push("Check somme")
  liste.push("Mois")
  liste.push("Dernière Ligne")

  targetSheet.appendRow(liste)
  targetSheet.getRange(1,10+2*nb_people).setFormula("=COUNTIF(A1:A,\"<>\")")

  // StatSheet

  statSheet.appendRow(["Somme"])
  statSheet.appendRow(tricountSettings.people)
  liste=[]

  for(let i=0;i<nb_people;i++){
    liste.push("=SUM("+tricountSettings.targetSheet+"!"+columnToLetter(6+nb_people+i)+"2:"+columnToLetter(6+nb_people+i)+")")
  }

  statSheet.appendRow(liste)
}
```