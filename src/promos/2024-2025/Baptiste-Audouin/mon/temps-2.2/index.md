---
layout: layout/mon.njk

title: "Découverte de R"
authors:
  - Baptiste Audouin

date: 2024-12-17
tags: 
  - "temps 2"

résumé: "Ce MON traite de la découverte du langage R"
---

{% prerequis %}

Aucun prérequis

{% endprerequis %}
{% lien %}

-['Site du MTECT'](https://mtes-mct.github.io/parcours_r_socle_introduction/)
-['Inside Airbnb'](https://insideairbnb.com/get-the-data/)

{% endlien %}

A travers ce mode j'ai voulu découvrir R qui est un langage de programmation important et connu dans le monde de l'analyse de données et des statistiques. Après m'être documenté sur le Github du ministère j'ai chercher un type de données sur lesquelles je pouvais m'exercer et jh'ai trouvé le site ['Inside Airbnb'](https://insideairbnb.com/get-the-data/) qui fournit tous types de données sur les offres postées sur le site **Airbnb**.J'ai donc cécidéde travailler sur les données des offres à Paris et de visualiser des données de prix, de types de logement et de localisation à l'aide de tableaux, graphiques et cartes. 


## Sommaire
  
  1. **Chargement et nettoyage des données**
  2. **Manipulation des données**
  3. **Visualisation des données**
  4. **Création de cartes avec la librairie *leaflet* and *shiny***

### 1. Chargement et nettoyage des données

Dans cette première partie j'ai chargé les données *.csv* des annonces à Paris sur le site ['Inside Airbnb'](https://insideairbnb.com/get-the-data/). Ensuite, à l'aide de la librairie de base de manipulations de données *dplyr*, j'ai supprimé les colonnes inutile à mon analyse et j'ai convertit certaines données comme les prix et les textes au bon format. 
Maintenant, avec ce nouveau dataset nettoyé, nous pouvons passer à la suite.

{% details "Head" %}

![Data_head](./images/data_head.png)

{% enddetails %}

### 2. Manipulation des données

Dans un premier temps j'ai voulu créer  desnouveaux tableaux qui vont nous données des détails sur les données, comme si on faisait des requêtes. J'ai pu générer des tableaux comme les prix moyens par quartiers, les prix par types de logements ou encore les nombre d'annonces et prix moyen par types de chambre et quartier.

### 3. Visualisation des données

Dans cette  partiej'ai voulu me familiariser avec la librairie *ggplot2* qui permet de visualiser les données à partir de graphiques. 
Ci-dessous un histogramme des prix des offres à Paris ainsi que la répartition des prix en fonction des types de logement sous deux formes  différentes :


<div><img src="/Users/baptisteaudouin/Documents/GitHub/do-it/src/promos/2024-2025/Baptiste-Audouin/mon/temps-2.2/images/histogramme_prix.png"></div>
<div><img src="/Users/baptisteaudouin/Documents/GitHub/do-it/src/promos/2024-2025/Baptiste-Audouin/mon/temps-2.2/images/prix_logement.png"></div>
<div><img src="/Users/baptisteaudouin/Documents/GitHub/do-it/src/promos/2024-2025/Baptiste-Audouin/mon/temps-2.2/images/prix_logement_violon.png"></div>

</div>

### 4. Création de cartes avec la librairie *leaflet* and *shiny*

