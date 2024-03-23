---
layout: layout/mon.njk

title: "MON 2.1 - VBA"
authors:
  - Schultz Mathis

date: 2023-11-23
tags: 
  - "temps 2"
  - "VBA"
  - "excel"

résumé: "Découverte du langage VBA"
---

<h2 id="h1"> Introduction </h2>

<h2 id="toc"> Table des matières </h2>

- [Introduction](#h1)
- [Table des matières](#toc)
- [Présentation d'excel](#h2)
- [Les limites d'excel](#h3)
- [Le langage VBA](#h4)
- [Google sheet](#h5)
- [Conclusion](#h6)
- [Liens utiles](#liens)

<h2 id="h2"> Présentation d'excel </h2>

Microsoft Excel est une application de logiciel de tableur utilisée pour stocker, organiser et analyser des données. Lancé en 1985, il est devenu l'un des programmes informatiques les plus importants dans les entreprises du monde entier.

Excel est un outil puissant qui s'est solidement ancré dans les processus commerciaux à travers le monde, que ce soit pour l'analyse des actions ou des émetteurs, la budgétisation, ou l'organisation des listes de ventes clients. La capacité qu'a excel à répondre à l'ensemble des besoins des clients lui a permis de s'imposer sur le marché, en effet, sa simplicité combiné à son ensemble de fonctions comme le langage VBA lui a permis de devenir essentiel.

**Finance et Comptabilité :**
Les services financiers et la comptabilité sont des domaines de la finance qui dépendent le plus des tableurs Excel. Dans les années 1970 et au début des années 1980, les analystes financiers passaient des semaines à exécuter des formules avancées manuellement. Aujourd'hui, Excel permet d'effectuer des modélisations complexes en quelques minutes. Les départements financiers et comptables utilisent intensivement Excel pour analyser les résultats financiers, créer des budgets et des prévisions, et prendre des décisions commerciales importantes.

**Marketing et Gestion de Produits :**
Les professionnels du marketing et de la gestion de produits utilisent également Excel pour la gestion des cibles clients, la planification des stratégies marketing futures.

**Planification des Ressources Humaines :**
Bien que des systèmes de base de données comme Oracle, SAP et Quickbooks soient utilisés pour gérer la paie et les informations sur les employés, l'exportation des données dans Excel permet d'analyser les tendances, de résumer les dépenses et les heures par période de paie, mois ou année, et de mieux comprendre la répartition de la main-d'œuvre par fonction ou niveau de salaire.

**Polyvalence des Tableurs Excel :**
Excel est un outil polyvalent utilisé dans de nombreuses applications commerciales, telles que le suivi des listes d'invités et des coûts pour les événements d'entreprise, la création de modèles de croissance des revenus, la planification éditoriale, la budgétisation des produits, le suivi des dépenses, le calcul des remises clients...

**Persistance d'Excel dans le Monde des Affaires :**
Excel reste un outil essentiel dans le monde des affaires, avec des applications allant des projets informatiques aux pique-niques d'entreprise. La maîtrise d'Excel est cruciale pour de nombreux professionnels de bureau, et des compétences plus avancées peuvent ouvrir des opportunités de promotion et de leadership. Bien que puissant, Excel nécessite un utilisateur compétent pour tirer le meilleur parti de ses fonctionnalités au profit de l'entreprise.

<h2 id="h3"> Les limites d'excel </h2>

Excel s'est imposé sur la marché avec une stratégie simple : un outil qui est modulable pour répondre aux besoins de tous. Il est rentré dans le quotidien de chaque entreprises et s'est rendu indispensable. Aujourd'hui le monde des finances est bloqué dans excel. Ce système conçu dans les années 80 est dépassé mais personne n'ose faire de transition vers d'autre système par peur de créer d'énormes problèmes. Voici quelques exemples de problème lié à des erreurs d'utilisation d'excel :

**Oubli du signe moins de 2,6 milliards de dollars :**
En décembre 1994, un comptable du fonds commun de placement Magellan de Fidelity Investments a omis un signe moins (-), transformant une perte nette en capital de 1,3 milliard de dollars en un gain de 1,3 milliard de dollars. Cette erreur a entraîné le retrait de la distribution de fin d'année promise de 4,32 $ par action.

**La grande différence entre "Masquer" et "Supprimer" :**
Lors de l'effondrement de Lehman Brothers en septembre 2008, Barclays Capital a failli acheter par accident 179 contrats de négociation de Lehman. En envoyant un fichier Excel à un tribunal de faillite, des lignes cachées au lieu d'être supprimées ont créé une confusion, détectée après l'approbation de l'accord.

**L'erreur de "Couper" et "Coller" de 24 millions de dollars :**
En 2003, TransAlta Corp, une entreprise d'électricité canadienne, a subi une perte de 24 millions de dollars en raison d'une erreur de "Couper" et "Coller" lors de la soumission des offres pour des contrats de couverture de transmission d'électricité. Des prix de soumission plus élevés ont été attribués à des itinéraires à faible demande en raison d'une mauvaise alignation des lignes dans le fichier du tableur.

Voici donc des limites liées à l'utilisation d'excel qui nécessite qu'un autre outil mieux conçu prenne le relai.

<h2 id="h4"> Le langage VBA </h2>

**Pourquoi le langage VBA**

Que ce soit à titre personnel ou professionnel, il arrive parfois de faire plusieurs fois les mêmes actions dans un projet. Cela a peu de valeur ajoutée de refaire toujours la même chose. C'est là que le langage VBA fait sens : il permet de faire un code qui automatise la tâche, appelé Macro. VBA dépasse excel dans la mesure où les Macros peuvent s'utiliser sur d'autre applications : outlook, word...

**les principaux cas d'usages**

- Automatisation simple 
- Traitement automatique 
- Automatisation complète 
- ERP (Enterprise Resource Planning) professionnel complet.

**Les Macros**

L'enregistreur de macros permet pour des cas simples de réaliser une suite d'action en très peu de temps : il reproduit les actions que vous lui montrez. Ce n'est pas une solution optimale car l'exécution n'est pas très rapide, et ne permet pas toutes les fonctionnalités : faire des boucles ou des teste.

Pour aller plus loin on peut ouvrir l'éditeur de Macros pour apporter des modifications à cette suite d'action : cela nécessite de coder les actions.

{% info "Attention" %}
Pour enregistrer les macros il faut que le fichier soit en .xlsm ou .xlsb
{% endinfo %}


MsgBox :
Utilisée pour afficher des boîtes de dialogue avec des messages pour l'utilisateur.

```vb
MsgBox "Hello, World!"
```

InputBox :
Permet de demander à l'utilisateur d'entrer des données.

```vb
Dim userInput As String
userInput = InputBox("Entrez quelque chose :")
```

Variables :
Pour stocker et manipuler des données.

```vb
Dim myNumber As Integer
myNumber = 10
```

Conditions (If...Then...Else) :
Utilisées pour exécuter des instructions en fonction d'une condition.

```vb
If myNumber > 5 Then
    MsgBox "La variable est supérieure à 5."
Else
    MsgBox "La variable est inférieure ou égale à 5."
End If
```

Boucles (For...Next, Do...Loop) :
Permettent d'exécuter des instructions de manière répétée.

```vb
For i = 1 To 5
    MsgBox "Ceci est la itération " & i
Next i
```

Fonctions intégrées :
Excel VBA offre également un large éventail de fonctions intégrées, similaires à celles d'Excel.

```vb
Dim result As Double
result = WorksheetFunction.Sum(Range("A1:A10"))
```

**D'autre possibilités**

- La fonction  Dir  permet de lister les différents fichiers dans un dossier.
- La fonction  MkDir  permet de créer des dossiers.
- Il est possible de déplacer, supprimer, tester ou encore copier des fichiers avec l’objet "FileSystemObject".
- Certains événements liés à une feuille ou au classeur peuvent déclencher un sous-programme et faire des actions spécifiques.
- On peut ajouter des paramètres afin que le programme sache lui-même s'il doit lancer les sous-programmes.
- Pour automatiser le lancement du programme, on peut utiliser le planificateur de tâches de Windows par exemple.

**Sécurité**

{% info "Attention" %}
Certaines fonctionnalités liés à l'exécution de code peut comporter des risques. Surtout lorsque l'on n'est pas auteur du code. Voici quelques démarches à suivre pour s'en protéger
{% endinfo %}

- L’ajout d’un certificat à une macro permet d'authentifier en signant la macro avec un nom.
- L’utilisation du "Username" permet de réduire l'exécution du code aux personnes qui y sont autorisées.
- Pour une protection maximale, il est possible d’ajouter un mot de passe pour afficher le code dans le VBE.

**La gestion de série temporelle**

- Les séries temporelles sont des graphiques qui permettent de comprendre l’évolution dans le temps d’une variable.
- On peut décomposer une date en plusieurs variables comme les jours de la semaine, les semaines, les trimestres, des périodes spécifiques, des heures, etc.
- Pour lisser les séries temporelles ou pour gommer les variations saisonnières, on utilise une moyenne mobile.
- Les prévisions des séries temporelles se font sur les historiques en gardant les variations saisonnières.

<h2 id="h5"> Google sheet</h2>

Pour travailler sur google sheet, le langage VBA ne fonctionne pas. Cependant, il y a un équivalent, le javascript. 

<h2 id="h6"> Conclusion </h2>

J'ai suivit les cours d'Open Classroom qui prennent environ 4-5 heures chacuns. Ils permettent de se saisir des bases du vba et d'aller plus loin dans la gestion de fichier et de data. Il sont très bien fait, Louise a quand à elle suivit le tutoriel de microsoft qui se trouve dans les liens utiles, et qui selon elle est tout aussi bien.

<h2 id="liens"> Liens utiles </h2>

Microsoft propose beaucoup de ressource pour appréhender VBA, voici des liens qui renvoies vers :

- [Les Fonction VBA](https://www.excel-pratique.com/fr/fonctions-vba)
- [Le tutoriel Microsoft](https://www.excel-pratique.com/fr/vba)

Le premier cours d'[Open Classroom](https://openclassrooms.com/fr/courses/8039296-decouvrez-les-fondamentaux-vba)
Le second cours d'[Open Classroom](https://openclassrooms.com/fr/courses/8017296-analysez-vos-donnees-avec-vba)
