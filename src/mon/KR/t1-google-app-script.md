---
layout: layout/post.njk

title: "Temps 1 - MON - Google Apps Script"
authors:
  - Kasimir Romer

tags: ['mon']
---
<!-- Début Résumé -->
Ici je vais mettre les informations sur mon MON de temps 1, google apps script.
<!-- fin résumé -->

## But du projet
Liste de tâches à faire ("To-Do") dans Google Sheets

1. créer une liste de choses à faire - avec l'API : https://dummyjson.com/todos
2. tri par date de fin
3. possibilité de cocher quand une tâche est terminée
5. créer un graphique (par jour : nouveau, terminé)

## Déroulement du projet
1. Tutoriel sur YouTube
2. Reconstruit le projet du tutoriel
3. Création d'un plan pour le projet to-do (le but du projet)
4. Creation de la liste des tâches avec l'API
5. Trier la liste et correction d'erreur (au début, l'en-tête du tableau a également été trié)
6. Récupérer le statut "terminé" et le convertir en case à cocher
7. Griser les tâches accomplies
8. Génération d'un charte basique á la base de la documentation
9. Travailler avec le debugger pour identifier des fautes 
10. Création d'une fonction permettant de compter le nombre de tâches effectuées/non effectuées par jour
  - J'ai d'abord fait, sans trop réfléchir, quelques essais naïfs avec des tableaux et JSON, qui n'ont abouti à rien.
  - Ensuite, j'ai imaginé un algorithme (voir ci-dessous) que j'ai ensuite converti en code.
  - Cette tâche a pris beaucoup plus de temps que prévu, car je n'ai pas encore beaucoup d'expérience dans le traitement des données et dans les opérations sur les arrays, les listes, les dictionnaires etc.
11. Création d'un graphique avec le nombre de tâches effectuées/non effectuées par jour 
12. TODO Appeller la fonction a chaque modification de la feuille (onEdit)
13. TODO Nettoyage : externaliser dans des fonctions, supprimer le logging
14. TODO Documentation du code 

## Algorithmus für die Daten
1. Erstes Datum herausfinden
2. Letztes Datum herausfinden
3. Hilfstabelle erstellen mit jedem Datum zwischen erstem und letztem Datum, initialisieren mit 0 für Anzahl erledigt und 0 für Anzahl offen: | Datum | Anzahl erledigt | Anzahl offen |
4. Für jede Zeile in der Tabelle:
    1. Datum der Zeile herausfinden
    2. In der Hilfstabelle das Datum suchen
    3. Wenn die Zeile erledigt ist, dann Anzahl erledigt um 1 erhöhen, sonst Anzahl offen um 1 erhöhen
5. Graph erstellen mit den Daten aus der Hilfstabelle

## Ressources utilisées
- Tutoriel sur YouTube: https://www.youtube.com/watch?v=Nd3DV_heK2Q
- Documentation sur Google Apps Script en utilisant avec Google Sheets: https://developers.google.com/apps-script/reference/spreadsheet/
- Documentation de la génération de graphiques: https://developers.google.com/apps-script/reference/spreadsheet/embedded-chart
- Documentation du debugger: https://developers.google.com/apps-script/guides/support/troubleshooting#debugging
- Documentation de la fonction onEdit: https://developers.google.com/apps-script/guides/triggers#onedite)
- Documentation des Arrays in JavaScript: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array
- Documentation de JSON in JavaScript: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON
- Documentation de la fonction Date in JavaScript: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date
- Boucler les dates: https://stackoverflow.com/questions/4345045/loop-through-a-date-range-with-javascript

## Conclusion
- Google Apps Script est un outil très puissant pour automatiser des tâches répétitives. Il s'agit pour ainsi dire de JavaScript conçu pour les Google Apps. Google met à disposition des classes spéciales pour les Google Apps, qui permettent d'interagir avec les applications.
- J'ai appris pas mal de choses, notamment en rafraîchissant mes connaissances en JavaScript, et je pense que je vais maintenant automatiser plus souvent quelque chose dans Google Apps Script.
- Néanmoins, Google Apps Script n'est pas adapté aux développements sérieux qui dépassent le cadre des produits Google. Il ne peut être développé qu'en ligne dans l'éditeur Google et le debugger n'a que peu de fonctionnalités. Pour les débutants et les petits projets, Goole Apps Script est toutefois très bien adapté.

[<-- Retour](../)