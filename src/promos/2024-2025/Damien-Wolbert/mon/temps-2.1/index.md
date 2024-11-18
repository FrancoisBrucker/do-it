---
layout: layout/mon.njk

title: "Peut-on monter rapidement en compétence sur Excel avec : les requêtes relationnelles, les opérations sur les strings et les listes déroulantes ?"
authors:
  - Damien WOLBERT

date: 2024-11-08
tags: 
  - "temps 2"

résumé: L'objectif de ce MON est d'étudier les possibilités apportées par les requêtes relationnelles, les opérations sur les strings et les listes déroulantes, pour la maitrise d'Excel. Ces possibilités seront étudier par le prisme de leur accessibilité.
---

{% prerequis %}
- VBA : niveau intermédiaire
- Excel : niveau intermédiaire
{% endprerequis %}
{% lien %}
- Mathier, Sébastien. « Cours VBA gratuit ». Excel-Pratique, https://excel-pratique.com/fr/vba.
- Qu’est-ce que Power Query ? - Power Query. 24 janvier 2024, https://learn.microsoft.com/fr-fr/power-query/power-query-what-is-power-query.
- KathleenDollard. Fonctions de chaîne - Visual Basic. 2 juin 2023, https://learn.microsoft.com/fr-fr/dotnet/visual-basic/language-reference/functions/string-functions.
- « VBA Regex ». Automate Excel, https://www.automateexcel.com/vba/regex/.
{% endlien %}

## Les requêtes relationnelles sur Excel
### Objectif
Excel pouvant être utilisé pour stocker et/ou utiliser des bases de données, il intéressant de se demander s'il est possible d'utiliser facilement des requêtes relationnelles de type SQL. L'objectif de cette réflexion n'est pas de plonger dans chacune des solutions mais fair eun état des lieu de leur accessibilité.

### Des possibilités...
{% note %}
Afin de lister les différentes possibilités, j'ai utilisé ChatGPT pour initier mes recherches.
| Requête ChatGPT | Commentaire |
|-----------------|-------------|
| Comment utiliser SQL avec VBA ? | Question trop précise est orientée. Empêche d'explorer toutes les possibilités. Omets toutes les solutions hors VBA et hors SQL |
| Comment utiliser des requêtes relationnelles en VBA ? | Question trop précise est orientée. Empêche d'explorer toutes les possibilités. Omets toutes les solutions hors VBA. |
| Comment utiliser des requêtes relationnelles sur Excel ? | Question trop large pour obtenir des résumés intéressants pour réaliser des recherches approfondies |
| Liste moi les différentes possibilités pour réaliser des requêtes relationnelles en excel en séparant les solutions passant par VBA et celles sans VBA. Sois exhaustif. | Meilleure requête réalisée : permet d'aborder un large pannel de solution avec suffisemment d'informations pour réaliser des recherches par la suite |

{% endnote %}
| Possibilités | Type | Description | Avis |
|--------------|------|------|
| Power Query | Manuel et Programmation | Power Query permet de mettre en forme les données en créant et en automatisant des requêtes. Dans ce cas, chaque requeête correspond à une nouvelle feuille Excel. | Power Query n'est pas forcément rapide de prise en main. Il est nécessaire de se plonger dans sa découverte pour obtenir des résultats satisfaisants. |
| VBA | Programmation | Coder des fonctions VBA permettant de filtrer les données de plusieurs tableaux en fonction de critères définis. | Solution rapide et efficace dès lors que le VBA est d'ores et déjà maitrisé ou connu. |
| Tableaux dynamiques | Manuel et Programmation | Utiliser les outils de tableaux dynamiques d'Excel. Accessible également depuis VBA. | Méthode pouvant être limité pour certaines requêtes, notamment celles ne faisant pas intervenir d'opération particlières. Très utiles pour les requêtes de type "JOIN" pour calculer des sommes, moyennes, extrema etcs.. : les commandes sont alors très intuitives. |
| Filtres | Manuel et Programmation | Utiliser les fonctions "Filtrer", également accessible en VBA | Bon intermédiaire entre le VBA et les tableaux dynamiques. Demande une attention particulière concernant l'ordre d'application des filtres ainsi que la supression des filtres à chaque opération. |
| VBA + SQL : Microsoft ActiveX Data Objects Library (ADO) | Programmation | Utiliser les fonctionnalités de "ADO" pour pouvoir rédiger des requêtes SQL directement depuis VBA | La mise en place de ce type de méthodes est n'est pas facile. La rédaction de fonctions VBA "classiques" est plus accessible pour des codes de longueurs comparables.|

### Conclusion
Différentes solutions permettent de réaliser des requêtes relationnelles via des lignes de code (avec ou sans VBA) ou en no/low-code (tableaux dynamiques, Power Query). Toutefois, les solutions de type "code" semblent pertientes sur Excel dès lors qu'elles peuvent être intégrées à des Macros VBA. Or, ces dernières solutions n'apportent pas de plus-value particulière comparativement à l'écriture de Macros classiques.  
**Il semble plus judicieux de dépenser de l'énergie à l'installation et l'utilisation de logiciels adaptés aux requêtes relationnelles.**  
*Exemples :*
- *SQLite pour utiliser SQL*
- Librairie pandas de python.

## Les listes déroulantes dépendantes
### Objectif
L'utilisation et la réalisation de documents complexes ou documents de suivi sur Excel engendre souvent le recours à des listes déroulantes. Afin d'affiner leur utilisation, il est intéressant de se demander comment réaliser des listes déroulantes dépendantes.

{% details "Définitions" %}
Des listes déroulantes dépendantes sont des listes déroulantes dont les choix possibles dépendent d'une autre cellule comme le montre l'image suivante.
![Exemple listes](./Exemple%20listes.png)
{% enddetails %}

### Les possibilités

**Idées initiales :**
| Possibilités | Détail | Inconvénient | Avantages |
|--------------|--------|--------------|-----------|
| Réaliser des filtres dans des zones non visibles du tableurs | Filtrer le tableau des données d'entrée et ce dans des cellules non utilisées (exemple : colonne GZ, soit la colonne numéro 208). | Peut altérer l'utilisation d'une feuille de calcul en monopolisant des plages de données. | Méthode dynamique permettant de changer les plages de données d'entrée sans modifier les cellules contenant les listes déroulantes.|
| Utiliser une feuille "Back-end" | Utiliser une feuille intermédiaire sur laquelle il serait possible de filtrer le tableau de données pour chacune des cellules intégrant une liste déroulante. | Création d'une page supplémentaire. | Méthode dynamique permettant de changer les plages de données sans modifier les cellules contenant les listes déroulantes.|
| Définir des plages de données | Segmenter les différentes parties des données d'entrée en plages nommées afin de définir les listes déroulantes à partir de ces plages. | Méthode non dynamique : il est nécessaire de lancer une modification des plages nommées à chaque ajout de données d'entrée. | N'ajoute pas de données ou de tableaux supplémentaires (pas de feuilles de calcul supplémentiares). |

La solution qui a été retenue est la solution numéro 2 : la complexité de sa programmation étant limitée et les inconvénients des autres solutions trop contraigants.
{% note %}
Il a finalement été possible de masquer cette page. Le back-end augmente donc le nombre de feuilles et la taille du fichier mais ne pollue pas l'espace de travail de l'utilisateur.
{% endnote %}

### Conclusion

La méthode a été mise en place avec succès comme visible dans le document suivant : ![Fichier excel de test à télécharger](./Listes%20déroulantes%20dépendantes.xlsm)
Elle pourrait être généralisée à des listes dépendantes à plus de deux niveaux en procédant par récurence d'un niveau à l'autre.

## Opérations sur les chaines de caractère en VBA

### Objectif
Identifier la structure d'une chaine de caractère peut se révéler puissant pour analyser et/ou traiter des données. Demandons-nous comment peut-on traiter les chaines de caractère sur Excel : lecture, extraction, segmentation et expressions régulières.
{% details "Exemple de cas d'utilisation" %}
Lister, hiérarchiser et trier une base de donnée contenant les références et présentation de différentes normes de constructions industrilles de l'Afnor. Chaque norme possède un identifiant d'une forme particulière. La manipulation de cette base de données nécessite donc la décomposition et comparaison des chaines de caractères des identifiants de normes.
{% enddetails %}

### Les opérations de base
Un certain nombre de méthodes et fonctions permettent de manipuler les chaines de carcatère en VBA. Les principales sont présentées et illustrés sur la page suivante : [Lien utile](https://learn.microsoft.com/fr-fr/dotnet/visual-basic/language-reference/functions/string-functions)

Parmis elles, voici un liste d'opérations intéressantes pouvant êtres réalisées :
| Fonction | Utilisation |
| Format | Permet de mettre en forme une chaine de caractère. Ex : Fomats de date, Format de nombres (séparateur des milliers, nombre de décimales...)|
| InStr | Permet d'obtenir la position de la première occurence d'une chaine dans une autre. |
| Mid | Permet d'extraire une partie de chaine en utilisant une position de début et de fin. |
| Trim | Permet d'avoir une copie de chaine de caractère sans espace de début et de fin. Fonction utile pour éviter des erreurs lors de tests et comparaisons. |

### Pour aller plus loin : les expressions régulières
Les expressions régulières permettent d'automatiser la reconnaissance de chaines de caractères et de leurs composants. Il est possible de les utiliser en VBA via l'objet RegExp. Les trois méthodes principales de cette objetf sont : Test (recherche de correspondance de motif : True ou False), Replace (rempacement de motifs), Execute (renvoie les correspondances du motifs).

Le lien suivant permet de comprendre les différentes façons d'utiliser les expressions régulières en VBA : [Lien utile](https://www.automateexcel.com/vba/regex/)
Il permet de :
- Se familiariser avec la syntaxe des expressions régulières.
- Configurer l'éditeur VBA pour utiliser RegExp.
- Se familiariser aux différentes méthodes de RegExp au travers d'exemples.

### Conclusion
VBA inclue un grand nombre de fonctions et méthodes permettant de réaliser rapidement de nombreuses opérations sur les chaines. Toutefois, dans un objectif d'automatisation et d'industrialisation de certaines opérations, le recours aux expressions régulière semble fournir une plus grande robustesse. *Exemple : Un programme peut ne pas reconnaître une chaine si certaines lettres sont en majuscule alors que cela n'était pas prévu. Bien que la méthode UCase permettent de convertir une chaine en majuscule, le recours systématique aux expressions régulière semble plus facile d'automatisation.*

## Conclusion
1. La mise en place de requêtes relationnelles sur Excel est possible mais nécessite du temps. Sans contrainte particulière, il semble plus judicieux de se concentrer sur d'autres logiciels ou outils pour cela.
2. La mise en place de listes déroulantes dépendante et facile et rapide. Le programme réalisé dans ce MON est reproductible et peut être copié d'un document à l'autre.
3. Les chaines de caractère peuvent êtres manipulées rapidement en VBA. En outre, l'utilisation des expressions régulières peut permettre une plus grande robustesse des Macros réalisées.





