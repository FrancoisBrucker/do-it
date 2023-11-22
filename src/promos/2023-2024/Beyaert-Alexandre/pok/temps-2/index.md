---
layout: layout/pok.njk

title: "La Data Science au service de l'Anatomie Pathologique"
authors:
  - Alexandre Beyaert

date: 1971-01-01

tags: 
  - "temps 2"

résumé: Un POK traitant de l'usage de la Data Science au service de l'anatomie Pathologique. En particulier, le risque de récidive d'une tumeur.
---

## Risque de récidive du carcinome basocellulaire estimé par l’intégration de multiples jeux de données (images histologiques, compte-rendus, etc…)


### Informations générales

Titre 	Evaluation du risque d’agressivité des carcinomes basocellulaires à partir de multiples jeux de données
Champ médical	Cancérologie Diagnostic Anatomie Pathologique
Entité de rattachement (unité de recherche, services etc…)	Service d’Anatomie Pathologiques, Timone, APHM
UMR911, MMG, AMU
Mots-clefs (2-3 mots clefs) santé/science	Basal cell carcinoma – prognosis

### Description du projet

Contexte et problématique du projet 
Rapide présentation du cadre dans lequel ce sujet s’inscrit, contexte de soin, de recherche…

L'Anatomie Pathologique (anapath) est une spécialité médicale portant le diagnostic des maladies sur le plan microscopique, c’est-à-dire sur l'interprétation d’images des tissus et cellules, et notamment de toute la pathologie tumorale et du cancer.

Le développement des techniques de numérisation offre de nouvelles perspectives pour cette spécialité qui pourra bientôt se passer de microscopes optiques au profit d’écran haute résolution. Dans ce contexte de numérisation totale, l'analyse d'images et certains pipeline de machine-learning offrent des perspectives de développement d’outils pratiques et/ou puissants d’aide au diagnostic: outre l’accélération de la vitesse pour rendre un diagnostic en routine aidé par l’informatique, la genèse de données normalisées et reproductibles de santé par l’intermédiaire de ces outils est un enjeu de compétitivité majeure pour la recherche et le développement en cancérologie dans les 5 prochaines années. Les tissus offrent de très nombreuses couches d’information actuellement peu exploitables. 

Les images microscopiques sont multimodales et le pathologiste peut s’aider de techniques pour visualiser différentes modalités d’information biologique, superposées sur une même coupe tissulaire, comme l’expression de protéines spécifiques qui jouent alors un rôle de filtre pour masquer ou au contraire révéler des cellules tumorales, les vaisseaux ou encore l’inflammation : l’immunohistochimie. Grace à ces images, et après intégration aux données cliniques, le pathologiste est à même de proposer des éléments pour la décision médicale. 

Le cancer de la peau le plus fréquent est le carcinome basocellulaire, qui est un diagnostic facile au microscope avec des images prototypiques, reproductibles. L’incidence élevée de ce cancer mobilise de nombreuses ressources pour le diagnostic, qui pourraient être automatisées.

La thématique de l’aide au diagnostic et de l’automatisation du diagnostic en pathologie s’inscrit dans un contexte actuel très concurrentiel portant essentiellement sur l’analyse d’image avec divers projets industriels et commerciaux en phase de validation voire de production dans d’autres organes (Medipath, Ibex, Vita-DX, Primaa, Howkin), qui sont financés. Seule la société Primaa développe des algorithmes dédiés à la dermatopathologie. In fine, ces nouveaux outils d’aide au diagnostic rencontreront nécessairement des obstacles réglementaires (marquage CE) et financiers (remboursement CPAM et/ou RIHN).

Aucun de ces projets ne se focalisent sur les données existantes (compte-rendus) ni sur l’intégration de multiples jeux de données (clinique, histologique) avec l’analyse d’image pour répondre à des questions cliniques précises. Dans le carcinome basocellulaire, la question clinique à se poser est : la tumeur va-t-elle récidiver ? Ce qui conditionne la surveillance et des traitements complémentaires.

Le but de ce projet est de créer un outil répondant le plus précisément à cette question du risque de récidive en se basant sur le plus de données disponibles et fiables possible.

Ce projet s’articule en parallèle, pour la partie compte-rendus, avec un autre projet déposé portant sur l’extraction automatisée de données de compte-rendus d’anatomie pathologique : il sert de validation théorique en vie réelle, sur une question clinique donnée.


### Missions et attendue souhaité 
Détailler ce que vous souhaiteriez produire, dans l’idéal, à la fin de la période de projet (logiciel, prototype, traitement de donnée, étude de faisabilité, preuves de concepts etc…)


- 1. Etude de faisabilité préalable :
Production de données à partir des lames de microscopes virtuelles (analyse d’image),
Extraction (Parsing) de données à partir des compte-rendus PDF et/ou DOCX,
Extraction de données à partir de la database du laboratoire (SGL/Access).

- 2. Production d’une base de données : training set
à partir de l’analyses d’images, du compte-rendu, des données de la base du service, des données cliniques, création d’une base de données concernant toutes les variables disponibles pour chaque patient atteinte de carcinome basocellulaire.

- 3. Corrélation à la question clinique : le cancer a-t-il récidivé ?
Entrainement sur un training-set annoté à des données cliniques de suivi (récidive ou non ?) pour proposer une estimation du risque de récidive afin d’aider le clinicien dans sa démarche décisionnelle afin d’indiquer un traitement complémentaire (tumeur à haut-risque) ou non (tumeur à bas-risque).

- 4. Validation des algorithmes sur cohorte indépendante, en condition vie réelle

- 5. Valorisation : publication scientifique (proof of concept ?) et/ou partenariat industriel 


### Données  
Le cas échéant détailler les données qui vont être utilisées dans le cadre du projet, leurs formats, leurs nombres, les modalités d’accès à ces données et les contraintes réglementaires d’accès…. 


-	Fichiers images : lames de microscopes numérisées, format .ndpi – anonymisées.
-	Fichiers textes : compte-rendus au format DOCX ou PDF – anonymisés. 
-	Fichiers tabulés : métadonnées extraites du système de gestion du laboratoire.

Le nombre de carcinomes basocellulaires analysables par an est environ 500 cas, ce qui représente 1500 à 2000 images de microscope par an. Des données concernant leur suivi sont déjà disponibles pour certaines années, en raison de travaux ultérieurs.
