---
layout: layout/pok.njk

title: "SérénaDo_It"
authors:
  - Arthur Louradou

date: 2023-12-13

tags: 
  - "temps 2"
  - "Data"
  - "Excel"
  - "Google Spreadsheet"
  - "Python"


résumé: Ce POK, modestement nommé selon le nom de son grand frère Sérénade, est un projet de création d'un site web de gestion de calendrier pour les élèves en 3A.
---

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

À ce stade, le code n'est pas propre et il faut encore le nettoyer. Cependant, il permet d'obtenir un DataFrame contenant les données du calendrier :

<div style="overflow: scroll">

| index | Ors,    | Ors, | Semaine,du | Semaine,au | Lundi,8h-9h     | Lundi,9h-10h | Lundi,10h-11h          | Lundi,11h-12h15 | Lundi,14h-15h                             | Lundi,15h-16h | Lundi,16h15-17h15 | Lundi,17h15-18h15 | Mardi,8h-9h | Mardi,9h-10h | Mardi,10h15-11h15 | Mardi,11h15-12h15 | Mardi,14h-15h | Mardi,15h-16h | Mardi,16h15-17h15 | Mardi,17h15-18h15 |
|-------|---------|------|------------|------------|-----------------|--------------|------------------------|-----------------|-------------------------------------------|---------------|-------------------|-------------------|-------------|--------------|-------------------|-------------------|---------------|---------------|-------------------|-------------------|
| 0     | NaN     | NaN  | NaN        | NaN        | NaN             | NaN          | NaN                    | NaN             | NaN                                       | NaN           | NaN               | NaN               | NaN         | NaN          | NaN               | NaN               | NaN           | NaN           | NaN               | NaN               |
| 1     |         |      | du         | au         | 8h-9h           | 9h-10h       | 10h-11h                | 11h-12h15       | 14h-15h                                   | 15h-16h       | 16h15-17h15       | 17h15-18h15       | 8h-9h       | 9h-10h       | 10h15-11h15       | 11h15-12h15       | 14h-15h       | 15h-16h       | 16h15-17h15       | 17h15-18h15       |
| 2     | temps 1 |      | 28/08      | 01/09      |                 |              |                        |                 |                                           |               |                   |                   |             |              |                   |                   |               |               |                   |                   |
| 3     |         |      | 04/09      | 08/09      | tronc commun 3A |              |                        |                 |                                           |               |                   |                   |             |              |                   |                   |               |               |                   |                   |
| 4     |         | 1    | 11/09      | 15/09      |                 |              | Bonjour \!(FB--LP\)218 |                 | TC1 : Agilité\(Florian Magnani\)Visio/218 |               |                   |                   | Langues     |              |                   |                   |               |               |                   |                   |

</div>

On voit que le header a une forme satisfaisante pour être exploitable par la suite.

Un point important à noter est que les cases fusionnées dans Excel ne sont présenter que dans la première ligne du DataFrame. On pourrait considérer les remplir avec la méthode `fillna(method='ffill')`, mais cela engenderait des incohérences et des "trous" dans l'emploi du temps seraient remplis.

Pour combler ceci, il va falloir extraire les informations de fusion du google spreadsheet. Après de longues recherches, ceci s'est avéré impossible.

Il faut donc trouver une autre solution, dont l'une retenue est d'exporter la taille des cours du fichier excel exporté, qui lui possède bien les informations de fusion. 

Nous verrons dans un second temps comment procéder.



### Traitement { #traitement }

À l'aide de fonctions utilitaires et d'une boucle, on peut extraire les informations de l'emploi du temps :

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

- Faire des Tests Unitaires ! Cela facilitera l'intégration des fonctions de traitement de données
- Intégrer le POC au code
- Automatiser l'exportation du (des !) fichier .ics pour les élèves


