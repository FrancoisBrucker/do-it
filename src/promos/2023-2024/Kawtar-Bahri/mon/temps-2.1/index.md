---
layout: layout/mon.njk

title: "Data Collection & Data storage"
authors:
  - Kawtar Bahri

date: 2023-11-22
tags: 
  - "temps 2"

résumé: Pendant mon parcours académique et mes stages, j'ai développé des compétences en matière de transformation, de traitement et de visualisation des données, sans pour autant avoir une compréhension approfondie de leur origine ou du processus de collecte. Il est temps que j'apprenne les notions de collecte et de stockage des données.
---

## Un MOOC sur la collection et le stockage de données
-	Collection des données ***6h*** : [AWS: Data Collection Systems](https://www.coursera.org/learn/aws-data-collection-systems?specialization=exam-prep-das-c01-aws-certified-data-analytics-specialty)
-	Stockage de données ***7h*** : [AWS: Storage Systems and Data Management](https://www.coursera.org/learn/storage-systems-and-data-management?specialization=exam-prep-das-c01-aws-certified-data-analytics-specialty) 



Les MOOCs que j’avais l’intention de suivre ne traite pas le thème choisi dans sa globalité. En effet, comme ils sont réalisés par AWS, le contenu est technique et très adapté aux outils d’AWS (comme Kinesis Data Streams ou Firehose, Kinesis API) qui sont payants. 

## Stockage de données 
En parlant du stockage des données, on pense principalement au fondement physique où les informations sont conservées de manière permanente. Toutefois, dans ce MON, je m’intéresse plutôt à l'architecture intellectuelle qui donne sens, cohérence et efficacité à ces données : les structures de bases de données.
### Fondamentaux du Système de Base de Données
Pour aborder cette partie j'ai suivi ce [Cours](https://www.coursera.org/programs/s9-common-track-uqhpe/projects/fondamentaux-du-systme-de-base-de-donnes?authProvider=ecole-centrale-casablanca&source=search) qui m’a permis de mettre en pratique un cours de SQL que j’ai déjà suivi. Pour ce, j’ai utilisé Visual Studio Community et une base de données des films fournie par le mooc. 

J'ai appris comment créer une base de données, la connecter au serveur, et manipuler cette base de données (Insertion, Sélection, Suppression et actualisation des données). 

### Types de bases de données 
|Type de Base de Données|Avantages|Inconvénients|Critère de choix|
|---    |---    |---    |---   |---    |
|Relationnelle|- Structure claire et bien définie <br>- Langage SQL standard<br>- Transactions ACID (Atomicité, Cohérence, Isolation, Durabilité)|- Moins flexible pour les données non structurées <br>- Difficulté à évoluer avec des schémas changeants <br>- Difficulté à gérer les données hiérarchiques|- Besoin de conformité avec un schéma fixe <br> - Intégrité des données et relations importantes |
|NoSQL (Not Only SQL)|- Flexibilité pour différents types de données <br>- Évolutivité horizontale*<br>- Gestion de gros volumes de données|- Manque de normes et de cohérence entre les systèmes <br>- Moins adapté pour les requêtes complexes<br>- Risque de duplication des données|- Grande variété de données non structurées, semi-structurées<br> - Besoin d'une évolutivité horizontale|	
|Orientée graphe|- Modélisation naturelle des relations <br>- Performances élevées pour les requêtes de graphes|- Complexité pour les structures de données simples <br> - Pas adapté pour tous les types de données|- Analyses et requêtes basées sur des relations complexes <br> - Données fortement liées ou nécessitant une modélisation graphique|	
||	|	||	

SQL permet de garantir l’unicité de la donnée (non dupliquée), ce qui était utile dans une époque où le cout de stockage etait extrêmement élevé.
Et comme ce n’est plus le cas, on peut maintenant se permettre de dupliquer la donnée en faisant du NoSQL, pour répondre à un besoin d’agilité (pouvoir modifier la donnée sans se soucier de sa structure). 

Evidement cette liste n’est pas exhaustive, on peut trouver d’autres types de base des données (Base de données embarquée, base de données XML/JSON, ...)

*L'évolutivité horizontale se réfère à la capacité d'une base de données à gérer une augmentation de la charge de travail en ajoutant simplement de nouveaux serveurs au lieu d'augmenter la capacité des serveurs existants. Contrairement à l'évolutivité verticale, qui implique l'ajout de ressources (comme la RAM, le processeur, etc.) à un serveur existant, l'évolutivité horizontale permet de répartir la charge sur plusieurs serveurs, formant souvent un cluster.
## Collecte de données 
### Web scrapping
Le web scraping, également appelé extraction de données web, est une technique informatique qui consiste à extraire des informations ou des données à partir de sites web. C'est un moyen efficace d'obtenir des données structurées à partir de pages web, que ce soit pour la recherche, l'analyse de marché, la surveillance concurrentielle, ou d'autres applications.

J'ai suivi le tutoriel de [Webscraping Lab How-To]( https://www.coursera.org/videos/css-capstone/dA9sj?query=web%20scra&source=search). Cette vidéo fait partie de Computational Social Science Capstone Project, réalisé par University of California sur Coursera. Elle explique comment collecter de la donnée, en donnant un exemple à partir d’une page d'un chaine youtube.

Pour ce, j'ai utilisé l'extension WebScaper.io sur mon navigateur, sélectionné quelque données à collecter, et visualisé ma base de données.

Contrainte : Le WebScraper sélectionne les informations souhaitées pour toute la page. Toutefois, dans les réseaux sociaux tout le contenu n’est désormais pas totalement chargé, vu que cela ce fait dynamiquement en fonction du système de recommendation. D'où la nécessité d'utiliser un outil de contrôle de navigateur automatisé.

### Autres moyens de collecte de données
- **IoT** : Les IoT sont des capteurs souvent utilisés par fabricants afin de mieux comprendre les usages et les besoins des utilisateurs.
Ces données peuvent être stockées sous leur forme “brute”, généralement sur une plateforme reliée au Cloud, puis étudiées en profondeur. La data peut également être traitée partiellement avant d’être stockée, grâce à certains algorithmes déjà installés sur les objets connectés, permettant ainsi de réduire la bande passante nécessaire pour la transmission des données.


- **Les enquêtes** : Qu'elles soient menées sous forme de questionnaires, d'entretiens ou de sondages, permettent de recueillir des données subjectives directement auprès des individus, offrant ainsi un aperçu des perceptions, des opinions et des expériences.


## Sécurité des données 
Lors de la collecte des données sur le web, il convient d'être attentif aux règles et coutumes qui s'y rapportent.
-	Les questions relatives aux droits de propriété intellectuelle dépendent de la législation en vigueur, ainsi que de la nature de la collecte et de sa réutilisation. 
-	On risque d’enfreindre le contrat d'utilisation de l'entreprise/site web. Pour éviter ceci pour le WebScraping par exemple, il est recommandé de consulter les règles fixées par le propriétaire du site web en ajoutant l'annexe .../robots.txt au domaine. (par exemple https://www.youtube.com/robots.txt). Ce fichier indique aux robots d'indexation des moteurs de recherche quels sont les éléments du site qu'ils sont autorisés ou non à explorer. Si le protocole d'exclusion des robots n'interdit pas la collecte, il n'y a pas de danger à collecter.
- En outre, il existe une grande zone grise et les règles sont encore en cours d'élaboration. En 2019, un [procès](https://en.wikipedia.org/w/index.php?title=HiQ_Labs_v._LinkedIn&oldid=960556303) très médiatisé a permis à une entreprise d'extraire automatiquement des données que LinkedIn ne souhaitait pas voir collectées. En 2020, différentes entreprises en ligne se sont poursuivies mutuellement pour avoir [collecté des photos](https://www.nytimes.com/2020/01/18/technology/clearview-privacy-facial-recognition.html) sur leurs sites web afin d'entraîner des logiciels de reconnaissance d'images. Dans tous ces débats en cours, la principale préoccupation semble être ce qui est fait des données. Les gens semblent moins préoccupés par le fait que des données accessibles au public soient collectées (les données existent de toute façon) que par la manière dont elles sont utilisées. 


## Conclusion : 
{%faire "**Ce que j'ai fait**"%}
-	Commencé les cours d'AWS ***3h***
- Suivi un MOOC de Fondamentaux du Système de Base de Données ***2h***
- Effectué des recherches sur les bases de données ***2h***
-	Suivi un MOOC de Web scrapping ***3h***
- Effectué des recherches sur la sécurité des données ***1h***
{% endfaire %}
{%info "**Ce que j'ai appris**"%}
-	Choisir le type de base de données selon le besoin du projet
-	Manipuler des bases de données avec SQL (J’ai déjà étudié SQL mais je ne l’ai jamais mis en pratique avant)
-	Collecter les données aves du web scraping 
-	Contraintes et risques de collecte de données 
{% endinfo %}