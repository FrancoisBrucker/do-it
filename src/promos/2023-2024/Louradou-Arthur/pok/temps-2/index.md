---
layout: layout/pok.njk

title: "SérénaDo_It - Du POC à la production"
authors:
  - Arthur Louradou

date: 2024-01-17

tags: 
  - "temps 2"
  - "Data"
  - "Excel"
  - "Google Spreadsheet"
  - "Python"


résumé: Ce POK, modestement nommé selon le nom de son grand frère Sérénade, est un projet de création d'un site web de gestion de calendrier pour les élèves en 3A.
---

<a href="http://node.oignon.ovh1.ec-m.fr/" class="buttonGithub">
  <span>Accéder à SérénaDo_It !</span>
</a>

## Sommaire

- [Objectifs](#objectifs)
- [Sprint planning](#sprint-planning)
  - [Sprint 1](#sprint-1)
  - [Sprint 2](#sprint-2)
- [De la recherche au POC](#de-la-recherche-au-poc)
  - [Google Spredsheet](#google-spredsheet)
  - [Traitement](#traitement)
- [Du POC à la réalisation](#du-poc-à-la-réalisation)
- [Revue de Sprint 1](#revue-de-sprint-1)
- [Suite : Sprint 2](#suite--sprint-2)
  - [Objectifs à l'issue du Sprint 1](#objectifs-fin-sprint1)
  - [Lecture de documentation de **Google Workspace APIs** pour déployer en local](#documentation-google-api)
  - [Une solution inespérée, plus simple..!](#solution)
  - [Intégration du POC au code](#integration-poc)
  - [Traitement des données](#traitement-donnees)
  - [Tests unitaires](#tests-unitaires)
- [Perspectives et conclusion](#perspectives-et-conclusion)
- [Liens et documentation](#liens-et-documentation)

## Objectifs { #objectifs }

Les objectifs de cette réalisation sont les suivants :
- Extraire l'information pertinente du calendrier de la filière Do_It
- Exporter cette donnée à la main dans un fichier .ics
- Créer un site web permettant de s'abonner au calendrier élève par élève, à partir du travail de Duc

## Sprint planning { #sprint-planning }

### Sprint 1 { #sprint-1 }

| Tâche                                                        | Difficulté | Temps |
|--------------------------------------------------------------|------------|-------|
| Interagir avec l'API Google Spreadsheet                      | 1          | 1h    |
| Extraire les informations du tableur sous forme de DataFrame | 2          | 2h    |
| Extraire du DataFrame les informations pertinentes           | 3          | 2h    |
| Tester, débugger, chercher des solutions                     | 5          | 3h    |
| Exporter ces informations dans un fichier .ics               | 1          | 1h    |
| Générer l'architecture propre du projet                      | 2          | 2h    |

À la fin de ce sprint, nous devrions avoir un programme qui s'éxécute en ligne de commande et qui permet d'extraire les informations de l'Excel (Google Spreadsheet, en réalité) du calendrier de la filière Do_It.

### Sprint 2 { #sprint-2 }

| Tâche                                          | Difficulté | Temps |
|------------------------------------------------|------------|-------|
| Écrire les tests unitaires                     | 5          | 3h    |
| Mettre le POC du POK dans les classes python   | 3          | 2h    |
| Dégugger le code jusqu'à export du .ics        | 5          | 3h    |
| Créer une interface web pour exporter le .ics  | 3          | 2h    |

Dans cette partie, nous allons créer une interface permettant d'exporte un .ics et de s'abonner au calendrier de la filière Do_It, en tâchant de personnaliser cela aux élèves en utilisant le travail de Duc.


## De la recherche au POC { #de-la-recherche-au-poc }

Je vais vous présenter dans cette partie les pistes de codes envisagées au cours de la phase de recherche nécessaire à l'analyse de données.
En effet, ce projet comporte une phase de recherche importante, car il faut comprendre le fonctionnement de l'API Google Spreadsheet, et trouver un moyen de l'utiliser pour traiter les données du calendrier de la filière Do_It.

### Google Spredsheet { #google-spredsheet }

Pour commencer, voilà comment importer notre fichier dans Google Colab :


{% details "Authentification Google Colab et traitement de la donnée" %}


```python
from google.colab import drive
drive.mount('/content/drive')
```

Ensuite, il faut autoriser google à nous authentifier sur ses services :

```python
from google.colab import auth
auth.authenticate_user()

import gspread
from google.auth import default
creds, _ = default()

gc = gspread.authorize(creds)

workbook = gc.open_by_url(<url du spreadsheet Do_It>)
ws = workbook.worksheet('année')
```

On peut ensuite récupérer les données de la feuille de calcul :

```python
import pandas as pd
from datetime import datetime
import numpy as np

df = pd.DataFrame(ws.get_all_records())

sheet_titles = []

for sheet in workbook.worksheets():
  sheet_titles.append(sheet.title)

# Get_all_values from sheets and store in dictionary
dict_of_sheets = {}
for sheet_title in sheet_titles:
  sheet = workbook.worksheet(sheet_title)
  values = sheet.get_all_values()
  dict_of_sheets[sheet_title] = values
# To confirm all sheets made it into the dictionary
dict_of_sheets.keys()

df = pd.DataFrame.from_records(dict_of_sheets.get('année'))

df.loc[0] = df.loc[0].replace('', np.nan)
# df = df.fillna(axis=1, method='ffill')
df.loc[0] = df.loc[0].fillna(method='ffill')

two_first = df.iloc[0:2]
two_first = two_first.transpose()
first = two_first[0] + "," + two_first[1]

headers = df.iloc[0].values
df.columns = first
```

{% enddetails %}

À ce stade, le code n'est pas propre et il faut encore le nettoyer. Cependant, il permet d'obtenir un DataFrame contenant les données du calendrier :

{% details "Voir la DataFrame" %}

<div style="overflow: scroll">

| index | Ors,    | Ors, | Semaine,du | Semaine,au | Lundi,8h-9h     | Lundi,9h-10h | Lundi,10h-11h          | Lundi,11h-12h15 | Lundi,14h-15h                             | Lundi,15h-16h | Lundi,16h15-17h15 | Lundi,17h15-18h15 | Mardi,8h-9h | Mardi,9h-10h | Mardi,10h15-11h15 | Mardi,11h15-12h15 | Mardi,14h-15h | Mardi,15h-16h | Mardi,16h15-17h15 | Mardi,17h15-18h15 |
|-------|---------|------|------------|------------|-----------------|--------------|------------------------|-----------------|-------------------------------------------|---------------|-------------------|-------------------|-------------|--------------|-------------------|-------------------|---------------|---------------|-------------------|-------------------|
| 0     | NaN     | NaN  | NaN        | NaN        | NaN             | NaN          | NaN                    | NaN             | NaN                                       | NaN           | NaN               | NaN               | NaN         | NaN          | NaN               | NaN               | NaN           | NaN           | NaN               | NaN               |
| 1     |         |      | du         | au         | 8h-9h           | 9h-10h       | 10h-11h                | 11h-12h15       | 14h-15h                                   | 15h-16h       | 16h15-17h15       | 17h15-18h15       | 8h-9h       | 9h-10h       | 10h15-11h15       | 11h15-12h15       | 14h-15h       | 15h-16h       | 16h15-17h15       | 17h15-18h15       |
| 2     | temps 1 |      | 28/08      | 01/09      |                 |              |                        |                 |                                           |               |                   |                   |             |              |                   |                   |               |               |                   |                   |
| 3     |         |      | 04/09      | 08/09      | tronc commun 3A |              |                        |                 |                                           |               |                   |                   |             |              |                   |                   |               |               |                   |                   |
| 4     |         | 1    | 11/09      | 15/09      |                 |              | Bonjour \!(FB--LP\)218 |                 | TC1 : Agilité\(Florian Magnani\)Visio/218 |               |                   |                   | Langues     |              |                   |                   |               |               |                   |                   |

</div>

{% enddetails %}

On voit que le header a une forme satisfaisante pour être exploitable par la suite.

Un point important à noter est que les cases fusionnées dans Excel ne sont présenter que dans la première ligne du DataFrame. On pourrait considérer les remplir avec la méthode `fillna(method='ffill')`, mais cela engenderait des incohérences et des "trous" dans l'emploi du temps seraient remplis.

Pour combler ceci, il va falloir extraire les informations de fusion du google spreadsheet. Après de longues recherches, ceci s'est avéré impossible.

Il faut donc trouver une autre solution, dont l'une retenue est d'exporter la taille des cours du fichier excel exporté, qui lui possède bien les informations de fusion. 

Nous verrons dans un second temps comment procéder.



### Traitement { #traitement }

À l'aide de fonctions utilitaires et d'une boucle, on peut extraire les informations de l'emploi du temps :

{% details "Extraction des informations" %}

```python
from icalendar import Calendar, Event
from datetime import datetime, timedelta

row = df.iloc[17]  # Prenons un ligne pour exemple
row = row.fillna('').iloc[2:] # On enlève les deux premières colonnes, qui ne nous intéressent pas

cal = Calendar()

for col_name, col_value in row.items():
    if col_name == 'Semaine,du':
        week_start_date = datetime.strptime(col_value+"/2023", '%d/%m/%Y')
        week_end_date = week_start_date + timedelta(days=5)
        print("Traitement de la semaine du",week_start_date,"au",week_end_date)
    elif col_value:
        try:
            event_start_date, event_end_date = parse_custom_time(
                df[col_name].iloc[1],
                (week_start_date + timedelta(days=df[col_name].iloc[0])).date()
                )

            event_end_date = event_start_date + timedelta(hours=3)

            print("Événement détecté le",event_start_date,event_end_date,":",col_value)

            event = Event()
            event.add('summary', col_value)  # Ajoutez le contenu de la cellule comme titre de l'événement
            event.add('dtstart', event_start_date)
            event.add('dtend', event_end_date) # + compute_duration()

            cal.add_component(event)
        except Exception as e:
            print("Erreur dans la colonne",col_value,": ",e)
```

{% enddetails %}

Ce code parcourt donc les colonnes pour une ligne donnée, et crée un événement pour chaque cours détecté.
Le fait que cela fonctionne, et donne des cours d'une heure dans mon calendrier, est satisfaisant et démontre que l'on peut faire un Proof Of Concept de ce POK.

Le problème subsiste avec les cours de deux ou trois heures, qui sont détectés comme des cours d'une heure.

## Du POC à la réalisation { #du-poc-à-la-réalisation }

Pour passer du POC à la réalisation, il convient de quitter l'environnement Google Colab et d'ouvrir un repository Git digne de ce nom.

Nous travaillerons donc sur un environnement local en utilisant au maximum des classes python pour rendre le code plus lisible et plus facilement maintenable.

Je vous propose donc pour cette revue de Sprint 1 de vous présenter la structure qu'aura le code au repo suivant : https://github.com/alouradou/SerenaDo_It

## Revue de Sprint 1 { #revue-de-sprint-1 }

Dans ce Sprint, nous avons vu comment extraire les informations de l'emploi du temps de la filière Do_It, et comment les traiter pour les exporter dans un fichier .ics.

Nous avons ainsi produit un Proof Of Concept qui nous permet de voir que le projet est réalisable, puis nous avons défini la structure du code sous forme de classes qui sera utilisée pour la suite du projet.

Vous pourrez noter ici que la structure du code est générée à l'aide de l'assistant chatGPT et je m'assurerai que le contenu qui s'y trouve en dernier lieu sera bien vérifié et testé par mes soins.
Petit point méthodologique cependant : j'utilise principalement chatGPT dans ce genre de cas, à l'initialisation d'un projet, car ses réponses sont bonnes pour établir une architecture globale et "dans les règles de l'art" (respectant des bonnes pratiques dès le départ) d'une application. 

## Suite : Sprint 2 { #suite--sprint-2 }

### Objectifs à l'issue du Sprint 1 { #objectifs-fin-sprint1 }

- Faire des Tests Unitaires ! Cela facilitera l'intégration des fonctions de traitement de données
- Intégrer le POC au code
- Automatiser l'exportation du (des !) fichier .ics pour les élèves

### Lecture de documentation de **Google Workspace APIs** pour déployer en local { #documentation-google-api }

La solution prometteuse semblait être l’utilisation de l’API de Google pour le projet en dehors d’un environnement Google Workspace. Cependant, celle-ci a des règles bien spécifiques pour être utilisée sur n’importe quelle application, incluant un environnement de test contraignant ou bien une validation de la part de Google. Ce détour est néanmoins intéressant pour comprendre le fonctionnement de certaines applications Cloud. [3]

J’ai donc abandonné cette piste qui m’a conduit à d’autres recherches.

### Une solution inespérée, plus simple..! { #solution }

Durant les recherches sur l’API, certains posts ont mentionné des liens d’export et nous aurions pu commencer par là : analyser les requêtes effectuées par le navigateur pour télécharger un Google Spreadsheet en PDF, Excel, CSV, etc. En effet, à l’aide d’un simple lien composé de cette façon :

```python
csv_url = "https://docs.google.com/spreadsheets/d/" + sheet_id + "/gviz/tq?tqx=out:csv&sheet=" + sheet_name
xlsx_url = "https://docs.google.com/spreadsheets/d/" + sheet_id + "/export?format=xlsx&id=" + sheet_id
```

Avec le Sheet id se trouvant dans l’URL de l’emploi du temps de Do_It.

<aside>
💡 Merveilleux : nous avons désormais un Google Sheet qui se télécharge tout seul et qui peut être exploité par la bibliothèque `openpyxl` comme le fait DUC dans son MON !

</aside>

### Intégration du POC au code { #integration-poc }

Dans cette phase du projet, nous avons consolidé le Proof Of Concept (POC) que nous avons développé dans le Sprint 1. Pour ce faire, nous avons intégré le code du POC dans la structure du projet définie précédemment. Les fonctionnalités de traitement des données du Google Spreadsheet ont été encapsulées dans des classes Python pour assurer une intégration automatique à tout code python y faisant appel.

### Traitement des données { #traitement-donnees }

<div style="display:flex;flex-direction: row;">
  <div style="display: block; margin-right: 20px;">


Comme il ne s’agit pas de perdre tout le monde, j’invite les intéressés à regarder le code du projet et à tester par vous même l’interface disponible au moment où je poste ce MON à son adresse de déploiement. Je vais tout de même détailler les classes intéressantes du projet pour le traitement des données.

Dans la phase de traitement des données, nous avons utilisé les bibliothèques `openpyxl` et `pandas` pour extraire et manipuler les données de l’Excel et résoudre la problématique des cellules fusionnées.

Comme un schéma vaut mieux que mille mots, voici le schéma de la donnée à mettre en perspective avec le code.

### Fonctionnement de l’application { #fonctionnement-application }

<a href="http://node.oignon.ovh1.ec-m.fr/" class="buttonGithub">
  <span>Allons voir le projet !</span>
</a>

Le fonctionnement de l’application est possible de plusieurs façons que je vais détailler de la plus stable et fiable à la moins éprouvée.

</div>

<img src="./assets/schema_data_serenadoit.webp" style="width: 30vw; aspect-ratio: 1/1;" />

</div>

1. Le calendrier général (route `/annee`)

   Dans le cas où vous souhaitez consulter l’agenda général, vous pouvez vous y abonner et voir les cours de tout Do_It. Notez que ce calendrier marche avec l’agenda de l’option CliMaTHs car leur calendrier est de la même forme que celui de l’option Do_It. Pour ce qui est de la génération du calendrier avec abonnement à partir du Google Sheet, celle-ci a lieu lors du clic sur le bouton “La liste complète des cours de l’année”. Vous pouvez donc mettre à jours les cours de toute l’option en parcourant le site !

2. Personnalisation à partir de votre Excel (route POST `/annee/source-excel`)

   Vous pouvez vous-même supprimer les cours que vous n’avez pas choisi au cours de l’année et ainsi personnaliser votre calendrier et ajouter vos propres événements. Veillez à ne pas toucher à la structure de l’Excel et cela sera

3. Scrapping de l’export de Duc depuis Github (route `/github`)

   À l’origine, Duc a sorti un export lors de [son MON 1.2.](../../../Dang-Vu-Duc/mon/temps-1.2/) Il est donc possible de récupérer les fichiers Excel bruts sur le repo du site. On affiche ainsi une liste de documents qui peuvent être intégrés au programme de traitement.
   Problème relevé : lorsque l’orthographe des cours est inexacte dans la première ligne de la cellule de l’emploi du temps, le cours n’apparait pas. Deux solutions sont envisagées : modifier un peu l’algorithme pour le rendre plus robuste ou écrire des tests unitaires pour garantir l’intégrité du calendrier ainsi généré.

4. Utilisation de l’algorithme de Duc directement dans l’API (route `/eleves`)

   Cette route liste les élèves pour exécuter l’algorithme de sélection des cours directement dans l’application.


### Tests unitaires { #tests-unitaires }

Pour assurer la fiabilité de ce dernier algorithme (qui est le plus pratique pour les élèves), j’ai pu lors du peu de temps restant exécuter un test dont voici le principe :

1. Créer un élève “Test” qui aurait rempli de “X” toutes les cases de choix de cours.
2. Parcourir l’Excel généré par la fonction de Duc et l’Excel original, complet.
3. En relevant les différences, on sait si des problèmes d’orthographe ont été repérés.

Pour l’heure, je corrige ces problèmes en ajoutant dans CreateTimetable, la liste des cours problématiques comme s’ils s’agissait de tronc commun :

```python
"architecture si", "stratégje & si", "people analytics", "it & dynamique organisationnelle"
```

Il conviendrait d'en réaliser de nouveaux.

## Perspectives et conclusion { #perspectives-et-conclusion }

Ce projet a été très intéressant à réaliser car il m’a permis de découvrir des outils très utiles pour la gestion de données et de me sentir à l'aise avec des concepts de développement complets pour un résulat utilisable par les élèves de Do_It.

Je pense que ce projet peut être amélioré en plusieurs points :

- Demander des retours aux utilisateur 
- Ajouter des tests unitaires pour garantir la fiabilité de l’algorithme de persionnalisations des cours
- Ajouter une fonction de mise à jour automatique du calendrier

## Liens et documentation { #liens-et-documentation }

[1] Code du projet : https://github.com/alouradou/SerenaDo_It

[2] Testez le projet : http://node.oignon.ovh1.ec-m.fr/

[3] Documentation Google API : https://developers.google.com/workspace/guides/enable-apis#sheets-api


<style>
    a.buttonGithub {
      display: inline-block;
      padding: 15px 30px;
      background-color: #2ecc71;
      color: #fff;
      border-radius: 10px;
      border: 2px solid #2ecc71;
      text-decoration: none;
      position: relative;
      overflow: hidden;
      transition: background-color 0.3s, transform 0.3s ease-in-out;
    }

    a.buttonGithub:hover {
      background-color: #2ecc71;
      transform: translateY(-5px);
      color: #2ecc71;
    }

    a.buttonGithub span {
      position: relative;
      z-index: 1;
    }

    a.buttonGithub::before {
      content: "";
      position: absolute;
      top: 0;
      left: -100%;
      width: 100%;
      height: 100%;
      background-color: #fff;
      transition: left 0.3s;
    }

    a.buttonGithub:hover::before {
      left: 0;
    }
  </style>
