---
layout: layout/pok.njk

title: "POK Temps 1 : Développement d'une application de suivi de course à pied avec Bubble.io"
authors:
  - OLIANA Guillaume

date: 2024-09-18

tags:
  - "temps 1"
  - "low/no code"
  -

résumé: Un POK sur la création d'une application web avec Bubble.io pour le suivi de course à pied et la personnalisation de plans d'entraînement.

---

{% prerequis %}

Aucun prérequis ici, je suis parti de zéro. L'idée est de prendre en main Bubble.io au fur et à mesure du projet.

{% endprerequis %}
{% lien %}

[Documentation Bubble.io](https://manual.bubble.io/)  
[Applications de référence : Runna, Campus]

{% endlien %}

Ce POK présente le développement d'une application web avec Bubble.io pour aider les coureurs à suivre leurs performances et à personnaliser leurs plans d'entraînement selon leurs objectifs. Ce projet vise à terme à inclure la mise en place de fonctionnalités de base que l'on peut retrouver dans les applications déjà existantes et la personnalisation des plans d'entrainement en fonction des données fournies par l'utilisateur lors de son inscription.

<div style="margin: auto; width: fit-content;">
  <img src="./logo_RunMate.png" alt="RunMate" style="width: 200px">

</div>


## Tâches

### Sprints

Développer une application complète et fonctionnelle pour le suivi de course à pied avec plans d'entraînement personnalisés.

#### Sprint 1

- [x] Formation sur Bubble.io
- [x] Réflexion sur l'UI/UX
- [x] Exploration des fonctionnalités des applications existantes (Runna, Campus)
- [x] Création de la base de données utilisateurs
- [x] Création des pages d'inscription et d'informations utilisateur
- [x] Développement du tableau de bord (dashboard) utilisateur
- [ ] Création de la base de données Plan qui stock les séances


**Étude post-mortem Sprint 1 :**
Le premier sprint s'est bien déroulé, avec une prise en main efficace de Bubble.io et la mise en place des premières fonctionnalités essentielles (sign-up, base de données utilisateurs, dashboard). Les prochaines étapes se concentreront sur la personnalisation des plans d'entraînement et l'amélioration du dashboard. 

#### Sprint 2

- [ ] Personnalisation des plans d'entraînement en fonction des choix d'inscription
- [ ] Finalisation du parcours utilisateur
- [ ] Création des plans d'entraînement affichés dans la page Plan avec détails des séances
- [ ] Intégration des fonctionnalités avancées (filtres par mois, année)
- [ ] Tests utilisateurs pour ajuster l'UI/UX
- [ ] Intégration d'API externes (Strava, Garmin)

**Étude post-mortem Sprint 2 :**
Le sprint 2 se concentrera sur l'intégration des plans personnalisés. L'objectif est d'avoir une application complète avec une interface claire et des fonctionnalités avancées pour les coureurs.

### Horodatage

Toutes les séances et le nombre d'heures passées sur le projet.

| Date         | Heures passées | Indications                                                                         |
| ------------ | -------------- | ----------------------------------------------------------------------------------- |
| Samedi 14/09 | 2H             | Exploration des fonctionnalités des applications existantes (Runna, Campus)          |
| Samedi 14/09 | 2H             | Réflexion sur l'UI/UX et identification des fonctionnalités principales à développer |
| Dimanche 15/09 | 2H            | Création de la base de données et structure des utilisateurs                         |
| Dimanche 15/09 | 2H            | Création des pages d'inscription et d'informations utilisateur                      |
| Dimanche 15/09 | 2H            | Développement du Dashboard utilisateur                                               |

## Contenu

### Premier Sprint

#### Formation sur Bubble.io

J'ai débuté ce projet en me formant sur la plateforme **Bubble.io**, une solution de développement no-code qui permet de créer des applications web sans avoir à coder. J'ai appris à manipuler les workflows, gérer la base de données, et utiliser les éléments de design pour concevoir des interfaces intuitives.

Pour cela j'ai suivi une formation vidéo sur Youtube expliquant point par point tous les aspects de Bubble.

J'ai vite préféré passer peu de temps sur la formation vidéo ( d'une durée de 5h) et d'experimenter par moi-même sur Bubble.

#### Réflexion sur l'UI/UX et exploration des fonctionnalités des applications existantes

Une réflexion sur l'interface utilisateur (UI) et l'expérience utilisateur (UX) a été menée pour définir le parcours utilisateur optimal. J'ai également pris le temps d'explorer les fonctionnalités des applications existantes, comme **Runna** et **Campus**, pour voir sur quelles fonctionnalités principales se concentrer. Cela m'a aussi donné des idées sur des fonctionnalités qui ne sont pas encore présentées et que je pourrais développer pour différencier mon application.



#### Création de la base de données utilisateurs (User)

La base de données **User** est l'un des éléments centraux de l'application, car elle permet de stocker toutes les informations nécessaires pour personnaliser l'expérience utilisateur et proposer des plans d'entraînement adaptés à chaque coureur. Voici un aperçu détaillé des étapes et des choix effectués pour la création de cette base de données :

<div style="margin: auto; width: fit-content;">
  <img src="./Screenshot from 2024-09-18 12-00-33.png" alt="RunMate">

</div>


##### 1. Structure de la base de données

J'ai conçu la base de données en tenant compte des informations essentielles à collecter lors du processus d'inscription et pour personnaliser les plans d'entraînement. Les champs suivants ont été créés pour chaque utilisateur :

- **Prénom** (`name`) : utilisé pour personnaliser l'interface et les interactions avec l'utilisateur, par exemple sur le tableau de bord (« Bienvenue, [nom de l'utilisateur] ! »).
- **Nom de famille** (`lastname`) : collecté pour des raisons d'identification unique et peut être utilisé dans de futures fonctionnalités (par exemple, pour une communauté de coureurs ou des classements).
- **Date de naissance** (`birth_date`) : cette information est essentielle pour adapter les recommandations d'entraînement en fonction de l'âge de l'utilisateur. Les plans d'entraînement peuvent différer selon que l'utilisateur est jeune ou plus âgé.
- **Ville** (`Ville`) : permet d'adapter certaines recommandations selon les spécificités géographiques (par exemple, les conditions météorologiques ou les événements locaux de course).
- **Niveau de l'utilisateur** (`level`) : ce champ est essentiel pour catégoriser les utilisateurs en fonction de leur expérience de course. Il est collecté via la page où l'utilisateur indique s'il est débutant ou pratiquant déjà la course à pied. Cela influencera le type de plan d'entraînement proposé.
- **Volume d'entraînement hebdomadaire** (`running_volume`) : ce champ enregistre le nombre de kilomètres qu'un utilisateur court en moyenne par semaine. Cette donnée est cruciale pour proposer un plan d'entraînement réaliste et progressif, basé sur ce que l'utilisateur peut déjà accomplir.
- **Nombre de sessions d'entraînement par semaine** (`sessions_per_week`) : lors de l'inscription, l'utilisateur choisit combien de fois il souhaite s'entraîner par semaine (entre 3, 4 ou 5 sessions). Cette information personnalise le plan d'entraînement pour s'assurer que les charges de travail sont adaptées à ses disponibilités et objectifs.
- **Objectif de course** (`goal_race`) : ce champ permet à l'utilisateur de définir son objectif principal parmi trois choix (10 km, semi-marathon, marathon). Cet objectif détermine la durée et l'intensité du plan d'entraînement personnalisé.
- **Semaine actuelle du plan d'entraînement** (`current_plan_week`) : il s'agit d'un champ dynamique qui évolue au fur et à mesure que l'utilisateur progresse dans son plan d'entraînement. Il permet de suivre l'avancée du plan et de proposer des ajustements si nécessaire.
- **Email** (`email`) : utilisé pour l'authentification de l'utilisateur et les communications futures, telles que des rappels d'entraînement ou des statistiques de progression.

##### 2. Logique de conception

La conception de cette base de données a été pensée pour répondre aux objectifs de l'application, qui sont de proposer des plans d'entraînement personnalisés et d'adapter les recommandations en fonction des préférences et capacités de l'utilisateur.

L'approche était de créer un modèle de données simple mais évolutif, où chaque utilisateur dispose de champs spécifiques à ses objectifs et préférences de course. Cela permettra, à l'avenir, d'ajouter des fonctionnalités supplémentaires sans avoir à remanier la structure de base.

##### 3. Relations entre les données

Chaque utilisateur dans la base de données **User** est relié à un ensemble d'autres tables et workflows qui interagissent avec ses données personnelles :
- **Table des séances d'entraînement** : une relation peut être établie avec une table qui stockera les séances d'entraînement hebdomadaires personnalisées pour chaque utilisateur. Les plans seront générés en fonction des choix faits lors de l'inscription (niveau, nombre de sessions, objectif).
- **Progression de l'utilisateur** : en fonction des performances enregistrées (volume de course, temps estimé de course, etc.), les données dans la base de données peuvent être mises à jour dynamiquement pour refléter les progrès de l'utilisateur et ajuster le plan d'entraînement en conséquence.

##### 4. Dynamisme des champs et personnalisation

L'un des aspects clés de cette base de données est son caractère dynamique. Par exemple :
- Le champ **current_plan_week** sera mis à jour automatiquement chaque semaine pour refléter la progression de l'utilisateur dans son plan d'entraînement. Cela permet de proposer des séances adaptées à la semaine en cours.
- Le champ **goal_race** peut être modifié si l'utilisateur change d'objectif (par exemple, passer d'un 10 km à un marathon). Cette flexibilité permettra à l'utilisateur de revoir ses objectifs et de recevoir un nouveau plan ajusté.

##### 5. Flexibilité pour les futures évolutions

La base de données **User** est conçue pour être évolutive. À l'avenir, d'autres champs pourront être ajoutés, comme :
- **Données biométriques** (poids, taille, fréquence cardiaque).
- **Synchronisation avec des services externes** (Strava, Garmin) pour importer des données de course directement dans l'application et ajuster les recommandations en fonction de performances réelles.

Cette architecture de base de données me permettra de gérer les informations des utilisateurs de manière efficace, tout en assurant la personnalisation des plans d'entraînement, l'adaptation des conseils et le suivi des progrès au fil du temps.


#### Développement des pages d'inscription et d'informations utilisateur

J'ai créé les pages permettant aux utilisateurs de s'inscrire et de renseigner des informations essentielles pour personnaliser leur expérience. Le parcours utilisateur inclut :
- Une page **Info 1** pour renseigner les informations personnelles (nom, ville, date de naissance).
- Une page **Info 2** pour choisir entre débutant ou pratiquant déjà la course à pied.
- Des pages supplémentaires pour définir le volume d'entraînement hebdomadaire, l'objectif de course, et le nombre de sessions par semaine.

<div style="margin: auto; width: fit-content;">
  <img src="./Screenshot from 2024-09-18 12-12-55.png" alt="Page infos">

</div>


#### Développement du tableau de bord (Dashboard)

J'ai mis en place un **tableau de bord** affichant les performances de l'utilisateur avec des données sur :
- Le progrès de l'allure
- La distance totale parcourue
- Le nombre de sessions d'entraînement
- Les tendances d'allure
- Les heures de course effectuées

Des graphiques dynamiques permettent de visualiser les progrès mois par mois.

<div style="margin: auto; width: fit-content;">
  <img src="./Screenshot from 2024-09-18 12-18-01.png" alt="Dashboard">

</div>


### Second Sprint

#### Personnalisation des plans d'entraînement

Le deuxième sprint sera consacré à la personnalisation des plans d'entraînement. En fonction des informations fournies par l'utilisateur lors de son inscription (niveau, volume hebdomadaire, objectif de course, nombre de sessions), un plan détaillé sera généré et affiché dans la **page Plan**. Cette page, encore vierge à l'heure actuelle, présentera le détail des séances hebdomadaires, adaptées aux objectifs de l'utilisateur.

#### Intégration des fonctionnalités avancées

Je prévois d'ajouter des fonctionnalités comme la possibilité de filtrer les performances par mois ou année, ainsi que d'intégrer des API externes comme **Strava** pour synchroniser les données de course.

#### Tests utilisateurs et amélioration de l'UI

Des tests utilisateurs seront effectués pour valider l'expérience utilisateur et ajuster l'interface en fonction des retours.
