---
layout: layout/mon.njk

title: "Python et analyse de données : application à des données sportives"
authors:
  - Baptiste Audouin

date: 2024-09-09
tags: 
  - "temps 1"

résumé: "Au cours de ce MON je souhaite découvrir la manipulation des bases de données avec Python et faire une application à des données sportives"
---

{% lien %}

* [Real python](https://realpython.com/python-for-data-analysis/)*

{% endlien %}


## Introduction

A travers ce MON, je souhaitait apprendre à manipuler et analyser des données sur python. Après quelques recherches notamment sur le site [Real python](https://realpython.com/python-for-data-analysis/) et sur Youtube je me suis lancer dans l'analyse des données de l'équipe de basketball de Golden State lors de la saison 2022/2023 et plus particulièrement de l'influence d'un joueur sur son équipe : Stephen Curry.

##  Sommaire

1. Importation des données
2. Nettoyage des données
3. Performances de Curry
4. Influence de Curry sur les performances de son équipe
5. Comparaison avec d'autres joueurs
6. Modélisation prédictive des résultats des Warriors

## 1. Importation des données

Pour faire ces analyses, il me fallait les statistiques de tous les matchs des Golden State Warriors los de la saison 2022/2023 ainsi que ceux des joueurs de l'effectif. Après quelques recherches, j'ai trouvé le site [Basketball Reference](https://www.basketball-reference.com) qui contient toutes ces données et bien plus encore. J'ai donc récupérer et téléchargé ces données pour commencer le projet.

```python
import panda as pd

warriors_data = pd.read_excel('GSW_season.xlsx')
curry_data = pd.read_csv('Regular_curry.csv')

# Aperçu des données
print("Données des Warriors :")
print(warriors_data.head())
print("\nDonnées de Stephen Curry :")
print(curry_data.head())
```
On joint maintenant les deux tables en utilisant la date comme clé primaire avant de passer aux nettoyage des données.

```python
curry_data['Date'] = pd.to_datetime(curry_data['Date'])
warriors_data['game_date'] = pd.to_datetime(warriors_data['game_date'])

merged_data = pd.merge(warriors_data, curry_data, left_on='game_date', right_on='Date', how='inner')
merged_data.head()
```

## 2. Nettoyage des données

Dans cette partie nous allons nettoyer les données afin d'en faciliter la manipulation. Certaines colonnes contiennent des éléments de types $string$ ce qui peut compromettre certains calculs, pour les matchs où Curry ne joue pas nous allons remplacer *'Inactive'* par *'Nan'* afin de pouvoir calculer les corrélations entre ses performances et celles de son équipe. De plus, ces calculs sont possible seulement avec des float on va donc remplacer les *'W'* et *'L'* qui signifient victoire ou défaite par des booléens, 1 pour une Win et 0 pour une Loose.

```python
merged_data['PTS'] = merged_data['PTS'].replace('Inactive', np.nan)
merged_data['AST'] = merged_data['AST'].replace('Inactive', np.nan)
merged_data['TRB'] = merged_data['TRB'].replace('Inactive', np.nan)

merged_data['wl_home'] = merged_data['wl_home'].replace({'W': 1, 'L': 0})
merged_data['wl_away'] = merged_data['wl_away'].replace({'W': 1, 'L': 0})

# Fonction pour convertir 'MM:SS' en minutes, avec gestion des valeurs comme 'Inactive'
def convert_to_minutes(time_str):
    try:
        if isinstance(time_str, str) and ':' in time_str:
            minutes, seconds = map(int, time_str.split(':'))
            return minutes + seconds / 60
        else:
            return 0  # Si le joueur est inactif ou la valeur est invalide
    except ValueError:
        return 0  # Si la valeur est autre que du texte attendu ou format erroné

# Appliquer cette fonction sur la colonne 'MP'
merged_data['MP'] = merged_data['MP'].apply(convert_to_minutes)
```
Nous avons également besoin d'une colonne qui nous donne les résultats des Warriors.

```python
result = [0]*len(merged_data['wl_home'])
for k in range(len(result)):
  if merged_data['team_abbreviation_home'][k] == 'GSW' :
    result[k] = merged_data['wl_home'][k]
  else :
    result[k] = merged_data['wl_away'][k]

merged_data['result'] = result
merged_data.head()
```

Enfin, nous ajoute au tableau le nombre de points marqués par l'équipe.

```python
points = [0]*len(merged_data['pts_home'])
for k in range(len(points)) :
  if merged_data['team_abbreviation_home'][k] == 'GSW' :
    points[k] = merged_data['pts_home'][k]
  else :
    points[k] = merged_data['pts_away'][k]

merged_data['points'] = points
```

## 3. Performances de Curry

Dans cette partie nous allons simplement visualiser les performances du joueur tout au long de la saison. Pour le premier graphe on regarde l'évolution des points du joueur sur la saison.

```python
# On prend seulement les matchs où Curry a joué

curry_played = merged_data[merged_data['MP'] > 0]
curry_played['PTS'] = pd.to_numeric(curry_played['PTS'], errors='coerce')
curry_played = curry_played.sort_values(by='game_date')


Y = curry_played['PTS']
X = curry_played['game_date']


plt.figure(figsize=(12, 6))
plt.plot(X, Y, marker='o', linestyle='-', color='blue')  # Ajout de marqueurs pour chaque point
plt.xlabel('Date')
plt.ylabel('Points')
plt.title('Évolution des points de Curry')
plt.grid()  # Ajout d'une grille pour faciliter la lecture
plt.tight_layout()  # Ajuste la mise en page pour éviter le chevauchement
plt.show()
plt.savefig('curry_points.csv')
```
METTRE LE PLOT

Le graphe suivant permet de faire une distinction entre les performances à domicile et à l'exterieur afin de savoir si ce paramètre à une influence sur le joueur.

```python
home_games = merged_data[merged_data['team_abbreviation_home'] == 'GSW']
away_games = merged_data[merged_data['team_abbreviation_away'] == 'GSW']

# Conversion des données en float
home_games[['PTS', 'AST', 'TRB']] = home_games[['PTS', 'AST', 'TRB']].apply(pd.to_numeric, errors='coerce')
away_games[['PTS', 'AST', 'TRB']] = away_games[['PTS', 'AST', 'TRB']].apply(pd.to_numeric, errors='coerce')

# Calcul des moyennes
home_avg = home_games[['PTS', 'AST', 'TRB']].mean()
away_avg = away_games[['PTS', 'AST', 'TRB']].mean()

comparison = pd.DataFrame({'Domicile': home_avg, 'Extérieur': away_avg})

comparison.plot(kind='bar')
plt.title("Performance de Curry à domicile vs extérieur")
plt.ylabel("Moyenne")
plt.show()
```
GRAPHE

Au vu de ces derniers résultats, on peut conclure que les statistiques du joueurs ont été constante cette saison et surtout les lieux de matchs n'ont eux aucun impacte sur lui.

## 4. Influence de Curry sur les performances de son équipe

Nous allons visualiser dans cette partie la matrice de corrélation entre les performances de Stephen Curry (points, passes décisives, rebonds, minutes jouées) et les résultats des Warriors (victoires ou défaites)

```python
correlation = merged_data[['PTS', 'AST', 'TRB', 'MP', 'result']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Corrélation entre performances de Poole et résultats des Warriors")
plt.show()
```
MATRICE

#### Analyse des corrélations :
- **Points (PTS) et Victoires (result)** : La corrélation entre les points de Curry et les victoires des Warriors est faible (0.069), ce qui indique que le nombre de points marqués par Curry n'a pas un impact direct sur les résultats de l'équipe.
- **Passes décisives (AST) et Victoires (result)** : Une corrélation plus forte (0.202) est observée entre les passes décisives de Curry et les victoires, suggérant que la capacité de Curry à faire des passes contribue davantage aux succès de l'équipe.
- **Minutes jouées (MP) et Victoires (result)** : Étonnamment, la corrélation entre les minutes jouées et les victoires est légèrement négative (-0.031), ce qui peut signifier que le simple fait que Curry passe plus de temps sur le terrain ne garantit pas toujours une victoire.
- **Autres corrélations** : Les corrélations entre les rebonds (TRB) et les victoires sont quasiment nulles (0.004), soulignant que les rebonds de Curry n'influencent pas significativement le résultat du match.

Dans la suite, nous allons comparer ces résultats avec ceux de deux autres joueurs clés des Warriors pour mieux comprendre l'impact des différentes contributions individuelles sur les victoires de l'équipe. Cela permettra de voir comment les performances collectives influencent les résultats.

## 5. Comparaison avec d'autres joueurs

Après avoir récupéré les données de deux autres joueurs majeurs de l'équipe (Jordan Poole et Klay Thompson) sur le même site [Basketball Reference](https://www.basketball-reference.com), j'ai effectué les mêmes manipulations sur leurs statistiques et voici les matrices obtenues :

DEUX MATRICES POOLE ET THOMPSON

#### Analyse

Poole et Thompson, montrent des corrélations plus importantes (surtout Thompson) dans des aspects du jeu qui impactent directement les résultats des matchs, notamment les points de Thompson et les passes de Poole. Curry, en tant que joueur constant semble moins "déterminant" dans les victoires ce qui s'explique par le fait que son niveau est toujours élevé. 

En résumé, bien que Curry soit essentiel pour la stabilité de l’équipe, les victoires des Warriors semblent davantage liées aux performances de Poole et surtout Thompson.

## 6. Modélisation prédictive des résultats des Warriors



###