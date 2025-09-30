---
layout: layout/pok.njk

title: "POK3 - B.A.-BA en Bases de données"
authors:
  - Inès Kebbab

date: 2024-12-17

tags:
  - "temps 3"
  - "info"

résumé: Ce POK tourne aux enjeux de la constitution d'une base de données et aux techniques de scrapping de site web, dans le cadre de mon projet aux Entrep'.

---

Autres POK ou MON en lien :
- POK de Jeanne Ménager ;
- POK d'Alix Duréault.


## Objectifs

L'objectif de ce POK est de constituer une base de donnée comprenant un nombre important de références, issues de différentes sources (nettoyage de la donnée, des doublons, mise en cohérence...). Pour cela, j'aimerais découvrir les outils de scraping web.

*Contexte initial : Ce POK s'inscrirait dans le cadre de mon projet aux Entrep' qui consiste à développer un comparateur d'appareils numériques, avec une dimension numérique responsable : l'objectif est de calculer et attribuer à chaque appareil un impact environnemental et social. La première version du projet, à présenter en mars 2025, se concentre sur la comparaison d'ordinateurs.*

Finalement, j'ai préféré constituer une base de données de films cultes à voir, avec pour objectif de pouvoir les utiliser pour une application personnelle que je crééerais ultérieurement. Ces données ont également pu me servir pour tester 

## Tâches

#### Sprint 1 - Base de données de références d'ordinateurs
1. [X] Apprentissage des bases en scrapping web
2. [X] Recherche de bases existantes et ressources
3. [X] Nettoyage des données
4. [ ] Import dans une solution de base de données adaptée (dynamique ou statique ?)

#### Sprint 2 - Base de données d'indicateurs environnementaux et sociaux
1. [X] Apprentissage avancé
2. [X] Nettoyage des données
3. [X] Analyse critique de la base finale (maintenance, veille, automatisation...)
4. [ ] Intégration au site (à confirmer)


## Contenu

### Premier Sprint

J'ai commencé par lire les POK&MON en lien sur le Scraping (il traite notamment de la légalité du scraping). J'ai ensuite suivi la formation qu'avait conseillé Jeanne [(lien)](https://www.youtube.com/watch?v=sOAZpHDEdkg&t=276s&ab_channel=Docstring), qui est très complète et propose des exercices pas à pas pour prendre en main les outils de scraping web.

### Les outils
- **Requests:**
    - Effectuer une requête HTTP, récupérer le HTML
    - Peut être remplacé par HTTPX qui permet de gérer les requêtes asynchrones et autres protocole HTTP.
- **BeautifulSoup**
    - Analyser le HTML, naviguer dans le DOM (ou parseur)
    - On peut l’utiliser sans l’autre si on a déjà les fichiers HTML en local.
- **Selectolax**
    - Il permet de parser le code HTML comme BS4 et obtenir de la même façon un arbre et aux éléments de la page. La différence peut être pertinent lors du scraping d'un large nombre de pages.
- **Loguru**
    - Créer des loggers plus facilement, pour ne pas avoir à retenir le module loggin par défaut (pour la gestion des erreurs notamment).
- **Playwright**
    - Cette librairie est plus jeune mais permet de gagner en perfomance en gérant notamment automatiquement le débogage (et les blocages éventuels). Elle propose également une interface 
- **C'est quoi le DOM ?**
    - Le DOM (Document Object Model) est une interface de programmation qui représente un document HTML, XML ou SVG sous forme d'une structure arborescente, permettant aux langages de script comme JavaScript d'interagir avec son contenu, sa structure et son style de manière dynamique.
- CSS Selector 

### Légalité
La formation traite de la partie légale du scraping. Dans mon cas, mon projet s'appuie sur des bases de données "à faible valeur", publiques et n'étant pas à caractère personnel.

En effet, les bases de données de films ne sont pas uniques et les différents sites se font concurrence : la valeur qualitative de la donnée est donc plus faible que si je récupère des analyses de film ou des statistiques plus difficile. La loi française prend largement en compte la qualité de la donnée récoltée plutôt que la quantité pour définir si la copie d'une partie d'une base de données est légitime ou non.

De plus, les données sont accessibles sans connexion et ne sont pas cachées derrière un paywall. Par rapport à la taille des sites que je souhaite scraper, le nombre de requêtes ne devrait pas nuire au bon fonctionnement du site.

Certaines solutions existent sur le marché pour garantir que le projet de scraping est compliant avec la loi et éthique.

### Second Sprint

J'ai pu terminé la formation, notamment avec les tutos pour apprendre à utiliser Playwright.

Je me suis ensuite concentrée sur l'extraction de différentes listes Sens Critique ainsi qu'une liste IMDB.

Selon les pages, les structures étaient différentes et il fallait revoir le script pour qu'il soit plus robuste.

Pour chaque page, j'ai rempli un tableau Pandas/DataFrames avant d'exporter mes données en csv et excel. 

#### Analyse des données extraites
Il reste encore à consolider les différentes données, avec de nombreux doublons avant de pouvoir l'implémenter dans une base de données unique.

De plus, s'il ne me semble pour ce projet pas utile d'automatiser la veille ou la maintenance de la base avec de nouveaux films (même s'il serait possible de faire une veille sur les sorties cinéma), il reste néanmoins possible de mettre en place ce genre de démarche.

Pour lancer automatiquement un script Python à fréquence régulière avec le Planificateur de tâches sous Windows (ou cron sous Linux et MacOS) :

1. Ouvrir le Planificateur de tâches → Créer une tâche.
2. Onglet Déclencheurs : choisir « Tous les jours » à l’heure voulue.
3. Onglet Actions : choisir « Démarrer un programme » et mettre :
   - Programme/script : chemin vers python.exe
   - Arguments : chemin complet vers le script .py

Il est important dans ce cas là de consolider la partie de tests et de gestions des erreurs / exceptions, pour qu'il ne crash pas.

### Conclusion et suites possibles

Pour faire évoluer le projet et exploiter pleinement la technologie, voici quelques idées :
- Automatiser le scraping régulier d'un site, pour veiller sur les dernières sorties à ne pas laisser passer, avec une gestion plus fine des exceptions ;
- Utiliser la donnée collectée.

Je pense continer à utiliser le scraping web, notamment pour mon POK1 où je m'inspirais d'un site déjà existant pour créer une checklist d'objectifs dans un jeu : je souhaiterais y récupérer les différentes images disponibles sur le site, ainsi qu'éventuellement les différents titres des items pour ne pas les lister par moi-même.

C'est un réel gain de temps, une fois la technologie maîtrisée.

Comme précédemment mentionné, je souhaite exploiter ses données à des fins personnelles pour créer une liste et un suivi des films cultes à voir dans sa vie. Je souhaiterais donc faire évoluer ces listes vers une vraie base de données (SQL ou autre).

#### Ce que j'ai appris :

Bases du scraping web et des technologies à connaître.

#### Les erreurs à éviter :

Faire attention aux choix des sites pour débuter, car de nombreux sites sont protégées car de nombreux sites sont protégés contre les bots ou requêtes nécessaires au scraping web.

### Horodatage

Toutes les séances et le nombre d'heure que l'on y a passé.

| Date | Heures passées | Indications |
| -------- | -------- |-------- |
| 13/09/25 | 4H | Lecture des précédents POK + Début Formation et réalisation des premiers exercices |
| 14/09/25 | 3H | Scraping Sites Sens Critique  |
| 20/09/25 | 5H | Suite Formation et exercices |
| 21/09/25 | 2H30 | Scraping IMDB + nettoyage des données |
| 27/09/25 | 2H | Fin Formation et exercices |
| 28/09/25 | 1H | Rédaction POK  |