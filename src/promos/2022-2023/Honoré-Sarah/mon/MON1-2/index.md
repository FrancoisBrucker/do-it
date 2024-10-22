---
layout: layout/mon.njk

title: "MON de Sarah "
authors:
  - Sarah Honoré
date: 2022-10-19

tags:
  - 'temps 1'
  - 'gestion de projet'
  - 'lean management'
  - 'agile'
---
<!-- Début Résumé -->
Comparatif des typologies de gestion de projets
<!-- fin résumé -->

Pour la deuxième partie du temps 1, j'ai choisi d'étudier les différentes méthodes de management et notamment les nouvelles méthodes de management. Louise ayant déjà traité ce sujet dans la première partie du temps, je vous invite à lire en premier son MON  en guise d'introduction pour mieux comprendre ce qui suit. 

Ce MON a pour vocation de présenter un état de l'art des différentes gestions de projets possibles en les classant en 3 grandes catégories : 
- **Le project Management et ses dérivées**
- **Le Lean Management et ses dérivées**
- **L'Agile et ses dérivées**

## Introduction et définition de la gestion de projet
Tout d'abord, il convient de définir de manière simple ce qu'est la gestion de projet. L'[ipag](https://www.ipag.edu/blog/gestion-projet) le définit de la manière suivante : ***"La gestion de projet, ou le management de projet, consiste à organiser le déroulement d’un projet de A à Z, de sa phase de conception à sa phase finale. Pour ce faire, il faut définir les objectifs, les ressources humaines et matérielles nécessaires, le budget, les délais et les contraintes éventuelles."***

Il existe une multitude de méthodes de management de projet plus ou moins pertinentes selon l'entreprise et sa culture, les caractéristiques du projet, le nombre de personnes impliquées dans le projet...

## Le Project Management et ses dérivées
Dans un premier temps, nous allons étudier les méthodes **les plus traditionnelles** (à savoir la méthode en cascade et Waterfall) et ses dérivées. 

Les **caractéristiques essentielles** de ses méthodes sont : 
- un **découpage précis des tâches** : le chef de projet définit dès le début les différentes étapes du projet. Il vérifie que chaque étape est finie avant de passer à la suivante. 
- Le **cadre et le planning sont définis en amont** en accord entre le client et le chef de projet. Tout est cadré dans le cahier des charges du projet. 

En ayant tout défini dès le début du projet, il y a peu d'interactions entre le client et le chef de projet. Le client découvre le produit de sa demande à la fin lorsqu'il est complètement fini. 

Les **points de vigilance** à avoir dans ce type de management sont : 
- l'effet tunnel dû au manque de communication entre chef de projet et client
- le manque de flexibilité car aucun retour en arrière n'est possible, il faut donc anticiper tous les risques

### La méthode Waterfall
La méthode Waterfall se nomme ainsi car elle divise un projet en **6 grandes étapes** qui s'enchainent les unes aux autres et comme l'eau dans une cascade, il n'est pas possible de revenir à l'étape précédente lorsqu'elle est terminée. 

Les 6 grandes étapes de la méthode Waterfall sont les suivantes : 
- **Définition des besoins**
- **Conception**
- **Mise en oeuvre**
- **Test**
- **Déploiement**
- **Maintenance***

Dans la première étape, le client **exprime ses besoins et ses objectifs**. L'équipe projet recueille le maximum d'informations car les étapes d'après dépendent de cette prise d'informations. Le chef de projet établit un plan de chaque phase du projet, la liste des ressources nécessaires et des personnes qui travailleront sur chaque étape.

Dans la deuxième étape, la conception, l'équipe projet **choisit le matériel** qu'elle va utiliser. Elle élabore le squelette puis les organes qui projet. dans le cadre d'un développement de logiciel, c'est dans cette étape qu'elle décide du langage de programmation et de l'interface utilisateur par exemple. 
La méthode Waterfall nécessite de bien documenter chaque étape pour que l'équipe puisse toujours savoir ce qui a été fait à l'étape précédente et mesurer l'avancement du projet

Dans la troisième étape, l'équipe projet **met en oeuvre et développe** conformément à ce qui été exigé à l'étape 1 et structuré à l'étape 2. 

Dans la phase de test, l'équipe qui a développé le projet le transmet à une équipe de testeurs chargés de documenter tous les problèmes, bugs ou erreurs qu'ils rencontrent. 

Dans la phase de déploiement, le produit final est livré au client. 

Dans la dernière étape, la phase de maintenance, l'équipe projet peut corriger des bugs que n'auraient pas vu les tests ou mettre à jour le produit. 


*Les avantages de la méthode Waterfall*
- facile à mettre en place
- structurée
- tout est planifié donc l'estimation des ressources (monétaires, temporelles, etc) est plus simple 
- la documentation permet de revenir sur les processus et rend le projet reproductible
- suivi du projet simple avec des outils de type diagramme de Gantt


*Les inconvénients de la méthode Waterfall*
- aucune flexibilité : en cas d'obstacle ou de retard, tout le projet est retardé
- impossibilité de revenir en arrière
- les tests interviennent à la toute fin de processus, aucune itération n'est possible
- retour vers le client uniquement lors de la livraison : possibilité de déception si ses attentes ont changé

La méthode en cascade ou Waterfall ne sont pas adaptés aux projets très complexes ou très longs.



### Méthode du cycle en V
La particularité de la méthode de cycle en V est d'avoir **plusieurs étapes de tests** après la réalisation et la mise en oeuvre contrairement à la méthode en cascade qui n'a qu'une phase de test à la fin du processus.
<img src="cycle_en_V.PNG">
source : https://www.manager-go.com/gestion-de-projet/cycle-en-v.htm

Dans cette méthode, l'équipe projet teste d'abord chaque brique fonctionnelle, ce sont les tests unitaires. Puis des tests sont effectués sur l'ensemble du produit, ce sont les tests d'intégration. Viennent ensuite les tests systèmes et la validation qui impliquent les futurs utilisateurs du produits, ils vérifient alors que la fonctionnalité de la solution. Juste avant la production, l'équipe projet consulte le client pour vérifier que le produit répond bien aux exigences qu'il a exprimé au début du projet, c'est la recette 

Les avantages et les inconvénients de la méthode du cycle en V sont les mêmes que ceux de la méthode en cascade 

### PRINCE2, une variante du Waterfall
PRINCE signifie **PRojects IN Controlled Environments**. Cette méthode dérive de la méthode de la cascade en cela que tout est minutieusement planifié et contrôlé du début à la fin. 
 
La méthode PRINCE2 repose sur **7 principes** qui sont : 
- le projet doit avoir une **justification commerciale** : nécessité d'avoir un besoin clair, un client défini et une évaluation des coûts détaillés
- les équipes doivent tirer des leçons à chaque étape : les équipes doivent **documenter** chaque étape du processus 
- les **rôles et les responsabilités sont clairement définis** : tout le monde doit savoir qui est responsable de quoi
- le travail est organisé par **séquences**
- les comités de pilotage appliquent le **"management par exception"** : les membres du conseil d'administration n'ont pas le temps de gérer au quotidien le projet donc ils délèguent le travail à un chef de projet en lui fournissant des exigences. En cas de problème entrainant un non respect des exigences, c'est une exception et c'est le comité de pilotage qui intervient 
- les équipes se focalisent sur la **qualité**: les livrables sont constamment contrôlés pour vérifier qu'ils respectent les exigences
- l'approche est **adaptée** à chaque projet

Il existe **7 rôles** dans le PRINCE2. Les 3 principaux sont le comité de pilotage, le chef de projet et l'équipe projet mais il y en a d'autres. 
Les 7 rôles sont les suivants  : 
- **le client** qui la personne qui paie pour le projet
- **l'utilisateur** qui soit sera affecté par les résultats du projet soit utilisera les livrables du projet (dans de nombreux cas, le client et l'utilisateur sont la même personne)
- **le fournisseur** est l'expert qui apporte les connaissances nécessaires à la réalisation du produit
- **le chef de projet** est le responsable du projet, il gère l'organisation, la planification, il supervise. Il décide des personnes qui participent au projet et de leurs tâches. Il est responsable du travail réalisé et des délais.
- **L'équipe projet et le responsable d'équipe** ce sont eux qui réalisent les différentes tâches du projet. **Les responsables d'équipe** sont de intermédiaires entre le chef de projet et l'équipe projet
- **l'administrateur** est la personne qui organise les réunions, transmet les informations, assure le suivi de la documentation. Sur des petits projets, c'est le chef de projet qui assure ce rôle. 
- **le comité de pilotage** est composé du client, de l'utilisateur final et du fournisseur

Le processus PRINCE2 est ensuite divisé en **7 séquences** : 
- La **mise en place d'un nouveau projet** : le demandeur envoie une demande que l'on appelle un mandat de projet. C'est un document bref qui explique brièvement le projet. Une personne évalue le mandat pour vérifier que la société peut répondre au projet.
- La **direction d'un projet** : le comité de pilotage  définit la marche à suivre pour chaque projet et ce qui va être déléguer au chef de projet
- Le **démarrage d'un projet** : le chef de projet rédige la documentation et notamment les 6 objectifs de rendement : durée, coût, qualité, portée, risque et bénéfice. Ces documents sont validés par le comité de pilotage
- Le **contrôle d'une séquence** : le chef de projet divise le projet en blocs dont il confie la réalisation aux responsables d'équipe qui coordonnent le travail journalier. Le chef de projet supervise et intervient lors d'erreurs ou d'obstacles.
- La **gestion de la livraison du produit** : le chef de projet vérifie que les livrables sont conformes aux exigences et le comité de pilotage valide ou invalide les blocs de tâches terminés
- La **gestion des limites de séquence** : à la fin de chaque séquence, le chef de projet et le comité de pilotage vérifie que le projet est toujours conforme aux exigences. Les chefs de projet aussi une réunion rétrospective avec l'équipe projet pour tirer des enseignements de la séquence.
- La **clôture du projet** : lorsque le projet est terminé, le chef de projet met au clair la documentation, les résultats et les rapports.

*Les avantages de PRINCE2*
- La division en étapes simplifie la gestion et permet d'avoir un résultat de qualité
- Les nombreuses réunions favorisent la communication
- Les parties prenantes ont leur mot à dire au cours du projet, elles sont informées des avancées
- Il est possible d'apporter des améliorations et de corriger les défauts
- En étant bien organisé, cette méthode peut faire gagner beaucoup de temps

*Les inconvénients de PRINCE2*
- Cette méthode n'est pas très flexible et réactive face aux imprévus
- La mise en oeuvre est complexe et nécessite une formation spéciale.

## Le Lean management et ses dérivées
### Le Lean Project Management
Le Lean Project Management est un système d'organisation complexe malgré ce que laisse entendre la traduction littérale française qui qualifie ce management de "maigre"

La méthode repose sur : 
- une diminution des stocks
- une réduction des défauts et du gaspillages
- une production en flux tendu
- un respect des délais
- un personnel flexible avec une meilleure gestion des compétences
- une réduction des coûts

L'innovation dans cette méthode de gestion de projet est de travailler en **amélioration continue**, étape par étape en mesurant régulièrement les progrès en fonction des objectifs. 
L'élément clé de cette méthode est de bien choisir ses indicateurs de performances. Des indicateurs quantitatifs sont évidents mais il faut aussi des indicateurs qualitatifs tel que la motivation des collaborateurs du projet. 

Les **7 principes du Lean Project Management** sont les suivants : 
1. **Eliminer le gaspillage**
Tout ce qui n'a pas de valeur ajoutée sur le produit finale doit être éliminé ou au moins réduit
2. **Améliorer l'apprentissage**
Il faut anticiper les besoins en compétences et former les membres de l'équipe en amont. Au démarrage du projet, il faut lister les compétences nécessaires et planifier des formations en amont du besoin de cette compétence. Il peut aussi être anticipé de travailler en binôme avec une personne expérimentée qui en forme une autre moins expérimentée
3. **Retarder l'engagement**
Tant que l'engagement n'est pas pris, le champ des possibles large, on a donc plus de flexibilité
4. **Livrer aussi vite que possible**
De courtes itérations permettent de valider des parties du projet sur lesquelles il n'est pas nécessaire de retravailler. Cela permet aussi au client de suivre l'avancée du projet
5. **Donner le pouvoir à l'équipe**
Avoir le pouvoir de décision au sein de l'équipe permet d'avoir plus d'efficacité que lorsqu'il est centralisé sur quelques personnes extérieures. En effet, les membres de l'équipe sont plus à même de gérer les tâches et les priorités. De plus, cela renforce la motivation et l'efficacité
6. **Intégrer la qualité dès la conception**
Associer la qualité à chaque étape permet de réduire les coûts et de les lisser sur l'ensemble des tâches. A la fin, le produit final correspond plus aux attentes du client et il a coûté moins cher car les corrections ont été moins nombreuses.
7. **Considérer le produit dans sa globalité**
Il est important de conserver une vision globale du projet malgré les itérations courtes pour ne pas perdre de vue l'objectif final

*Les avantages du Lean Project Management*
Les avantages principaux du Lean sont la réduction de coûts et l'amélioration de la qualité des produits.

*Les inconvénients du Lean Project Management*
Il faut faire attention avec cette méthode à ne pas basculer dans les extrêmes en étant obsédé par les chiffres, pas les indicateurs et en oubliant le bien-être au travail.

Le Lean Project Management est plus adapté pour des **petits projets sur une courte durée**. L'auto-gestion est plus compliquée sur de gros projets.

Plus de détails sur les concepts du Lean Project Management [ici](https://www.piloter.org/six-sigma/lean-management.htm)

### Le Kanban et le Six Sigma, des dérivés avec des outils en plus
#### Le Six Sigma
Le Lean Six Sigma cherche la cause profonde des problèmes dans la gestion de projet dans le but de réduire le gaspillage de temps et de ressources. 

La méthode utilise l'outil DMAIC (Define, Measure, Analyse, Improve, Control) dont les 5 étapes sont : 
- **définir** la portée du projet, les objectifs et la valeur pour le client
- **mesurer** la performance et la variabilité
- **analyser** les problèmes, les forces, les faiblesses
- **améliorer** les solutions pour éliminer les problèmes 
- **contrôler** les solutions mises en place pour qu'il n'y ait pas de retours en arrière

Les outils les plus utilisé dans Six Sigma sont la **cartographie des chaines de valeur**, des **sondages sur les réactions du client**, les **diagrammes de Gantt** et les **tableaux de contrôle de processus statistiques**

Plus de détails sur le Six Sigma [ici](https://www.planzone.fr/blog/quest-ce-que-la-methodologie-six-sigma#:~:text=%C2%AB%20Six%20sigma%20%C2%BB%20signifie%20donc%206,produits%20issus%20de%20ce%20processus.) et [ici](https://www.lafabriquedunet.fr/gestion-de-projet/la-gestion-de-projet-lean-definitions-et-bonnes-pratiques/)

#### La méthode Kanban
La méthode Kanban est une méthode dérivée du Lean qui permet de visualiser les tâches à faire pour augmenter l'efficacité et atteindre l'amélioration continue. 
Les différentes tâches sont représentées sous la forme de cartes dans un **tableau Kanban**. Dans ce tableau se trouve différentes colonnes telles que "A faire", "En cours" et "Terminé". Lorsqu'une personne commence une tâche, elle décale la carte de la tâche de la colonne "A faire" à la colonne "En cours". Cela permet à l'ensemble de l'équipe de savoir où en est le projet à l'instant T.

<img src="tableau kanban.PNG">
source = https://kanbanize.com/fr/ressources/debuter-avec/methode-kanban)-

### Le Lean startup
Le Lean Startup est une adaptation du Lean Project Management au monde des PME et des startups. Le but est de trouver rapidement un modèle commercial fiable.

Les deux méthodes ont pour but de répondre aux intérêts du client mais il y a néanmoins 3 différences majeures à noter. 

1. **Une portée différente**
Le Lean Project Management viser à améliorer l'entreprise dans son ensemble et à contrôler toute la chaîne de production alors que le Lean Startup se focalise sur le cycle de commercialisation des produits
Le Lean Project Management insuffle une culture d'amélioration continue de l'organisation alors que le Lean Startup cherche à proposer rapidement un produit performant

2. **Une maturité différente**
Le Lean Startup vise des petites entreprises et des entreprises naissantes qui n'ont pas forcément encore de produits à proposer. Cette méthode de management vise à être utilisé lors du lancement d'une entreprise sur un marché.
Le Lean Project Management vise de grandes et de petites entreprises qui recherchent une méthodologie globale. Cette méthode de management tend à être utilisée sur le long terme.

3. **Une nature de produit différente**
Le Lean Project Management recherche l'optimisation de toute la production pour avoir un produit défini et de qualité alors que le Lean Startup développe un produit primaire, appelé Minimum Viable Product (MVP) qui permet à l'entreprise de mesurer le marché, de répondre aux hypothèses commerciales faites en amont et de réadapter le produit.

Même si les deux styles de management ont des différences, ils ont aussi des points communs : 
- Le **client au centre**  
- le **zéro gaspillage** 
- la **mesure de la performance**

Finalement, même si les deux méthodes se ressemblent, elles diffèrent tout de même de par leurs outils, les usages et leurs portées.


## L'Agile et ses dérivées
La gestion de projet Agile suit le même principe que pour le Lean : **la valeur délivrée au client est au centre des préoccupations**. En revanche, le pratique pour atteindre cet objectif sont différentes.

En gestion de projet Agile, le travail est organisé en **itérations**, appelé "sprints". Chaque itération apporte une amélioration au produit. Au départ, on livre un produit simple mais qui fonctionne et on complexifie peu à peu. Le cadre de travail a le moins de contraintes possibles : les échanges oraux sont favorisées par des réunions régulières. L'équipe s'auto-organise comme elle souhaite ce qui permet de déployer leurs compétences. L'avancement est mesurée par les différents sprints. La raison pour avoir aussi peut de contraintes est que l'équipe doit être flexible, agile et pouvoir prendre en compte des changements même tard dans le projet et c'est cela que repose cette approche. 

Lorsque le management en mode agile s'est développé, les spécialistes de ce management se sont regroupé pour rédiger le [Manifeste Agile](https://manifesteagile.fr/). Ce document regroupe les 4 grandes **valeurs** et les 12 **principes** qui définissent les critères d'une gestion agile de projets informatiques.

Il existe de nombreuses méthodes dérivées du management agile. Louise ayant déjà traité le Safe, le Scrum et le Shape-Up. Nous allons ici nous intéresser à l'Extreme Programming et au Crystal.

### Extreme Programming ou XP
La méthodologie eXtreme Programming est une méthode de gestion de projet qui applique, comme son nom l'indique, à l'extrême les principes du management agile, qui sont : **se focaliser sur les besoins clients, avoir un développement itératif et de l'intégration continue.**
La **relation avec le client** est au coeur de XP. 

XP repose sur 5 valeurs essentielles qui sont : 
- **la communication**
Chaque membre de l'équipe doit communiquer tous les jours avec les autres membres de l'équipe et avec le client. Cela permet de mieux résoudre les problèmes.
- **la simplicité**
On privilégie la manière la plus simple d'arriver au résultat. L'équipe projet fait ce qui est demandé mais rien de plus. Plus c'est simple, plus c'est facile à faire évoluer.
- **les feedbacks**
Avoir le retour du client sur les différents livrables est fondamental. L'équipe envoie aussi souvent que possible ses différentes étapes pour avoir des feedbacks et valider ou non les étapes. Si le client demande une modification, elle est de suite prise en compte.
- **le respect**
Le travail de chacun doit être respecté et le client doit aussi être respecté.
- **le courage**
Le courage permet de sortir des situations difficiles, lorsqu'une itération n'est pas validée par exemple.

Les 5 valeurs se déclinent en 13 pratiques qui vous pouvez retrouver [ici](https://www.planzone.fr/blog/quest-ce-que-la-methodologie-extreme-programming)

La méthode XP peut être utilisé dans de petites ou moyennes équipes (pas plus de 20 personnes). Il faut aussi que la culture de l'entreprise s'y prête car cela demande de s'adapter à une méthode de management assez extrême. Il faut aussi que le client joue le jeu en étant très présent pour l'équipe projet.

*Les avantages de l'eXtreme Programming* sont : 
- un contact privilégié avec le client
- aucun travail inutile
- aucune heure supplémentaire, travail à son propre rythme
- les modifications peuvent être prises en charge très rapidement

*Les inconvénients de l'eXtreme Programming* sont :
- l'extrême communication entraine une charge de travail supplémentaire
- le client doit être très investi dans la démarche
- cette méthodologie requiert beaucoup d'autodiscipline pour la mise en oeuvre

### Crystal
La méthode agile Crystal est connue pour être une méthode assez **souple** avec un ensemble de bonnes pratiques. Contrairement à d'autres méthodes, cette méthode n'est **pas centrée sur les processus** mais sur :
- les personnes
- les interactions
- la communauté
- les compétences
- les talents
- la communication

La méthode Crystal a **différentes variantes** selon la taille de l'équipe qui l'utilise. Chaque variante a une couleur pour identifier le "poids" de la méthode agile à utiliser en fonction du projet. 
Il y a donc les méthodes Crystal Clear (la plus connue), Crystal Yellow, Crystal Orange, Crystal Orange Web, Crystal Red, Crystal Maroon, Crystal Diamond et Crystal Sapphire.

Cependant ces variantes partagent les **7 points communs de la méthode Crystal** qui sont : 
- des livraisons fréquentes
- un processus d'amélioration continue
- une grande communication entre les membres de l'équipe
- une grande confiance entre les différents membres de l'équipe
- la priorité à la concentration
- une facilité d'accès aux experts
- un environnement technique permettant des tests automatisés et des intégrations fréquentes

La majorité de ses principes sont communs à d'autres méthodes de management excepté **la concentration** qui est mise en avant pour la première fois et qui mérité d'être expliquée plus en détail.
La concentration est fondamentale dans cette méthode de management, toutes les sources de distraction sont donc éloignées, les téléphones sont éteints, il ne faut pas poser des questions en dehors de leur contexte etc. En effet, si on interrompt la concentration d'une personne, elle aura besoin d temps pour retrouver son niveau de concentration initiale et aura donc perdu du temps et de la productivité. La méthode Crystal définit 2 règles à ce propos : 
- une personne de l'équipe doit travailler au minimum 2 heures sans être interrompue
- un membre de l'équipe ne doit pas travailler moins de 2 jours sur un sujet avant d'en changer sans quoi il n'a pas le temps  de s'approprier complètement le sujet et d'être pleinement efficace

## Conclusion
Nous avons vu ici les 3 grands types de managements et certaines de leurs dérivées. Il en existe encore beaucoup d'autres qui mériteraient certainement d'être étudiées. 
Chaque méthode a des avantages et des inconvénients et n'est pas forcément adaptée à tous les types de projets. Avant de commencer un nouveau projet, il faut donc prendre le temps de réfléchir au style de management le plus pertinent.



#### Sources 
{% prerequis "Sources supplémentaires" %}
* [introduction project management](https://www.appvizer.fr/magazine/operations/gestion-de-projet/methode-classique-gestion-de-projet)
* [Waterfall, source 1](https://www.planzone.fr/blog/quest-ce-que-la-methodologie-waterfall)
* [Waterfall, source 2](https://asana.com/fr/resources/waterfall-project-management-methodology)
* [cycle en V](https://blog.hubspot.fr/marketing/cycle-en-v)
* [PRINCE2](https://www.wrike.com/fr/blog/prince2-la-reine-des-methodologies-de-gestion-de-projet/)
* [PRINCE2, avantages et inconvénients](https://www.skriv.com/fr/blog/methode-prince2)
* [Lean](https://www.nutcache.com/fr/blog/la-gestion-de-projet-lean/)
* [Kanban](https://kanbanize.com/fr/ressources/debuter-avec/methode-kanban)
* [Lean Startup](https://blog.toyota-forklifts.fr/lean-management-lean-startup-differences)
{% endprerequis %}
* [agile](https://www.saagie.com/fr/blog/tout-savoir-des-methodes-lean-et-agile/)
* [crystal](https://www.nutcache.com/fr/blog/methode-agile-crystal/)

