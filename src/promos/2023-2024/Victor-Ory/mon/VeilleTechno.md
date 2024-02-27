---
layout: layout/mon.njk

title: "Vieille technologie ou Veille technologique ?"

authors:
  - ORY Victor

date: 2023-09-16

tags:
  - 'temps 3'
  - 'Cybersécurité'
  - 'Relation Internationales'
  - 'Veille'
  
---
## Résumé :

Deux parties vont constituer ce MON :

    - Comprendre et mettre en place la méthode de veille 
    - Mettre en place ce dispositif
    - Faire un petit rapport sur les sujets de politiques publiques du monde cuber

## Comprendre :

### Étapes pour faire une veille :

1) Analyser ses besoins : Quels domaines ou sources surveiller ? Pour quelles finalités ? Combien de temps ai-je à y consacrer ?

2) Définir son périmètre de recherche : savoir ce qu'on cherche et préciser son sujet pour éviter de générer du bruit ou du silence. Quelles thématiques ? Quelles problématiques ? Quels mots-clés ? Bien définir son sujet de recherche et ses mots-clés est essentiel pour mener une veille efficace.

3) Identifier ses sources : où chercher l'information ? Ma source est-elle fiable/pertinente/de qualité ? Fraîcheur de la source : publie-t-elle régulièrement ou est-elle obsolète ?

4) Collecter les sources : utiliser une méthode manuelle (pull) ou une méthode automatisée (push), comment organiser sa veille ?

5) Traiter et analyser

6) Diffuser et partager
  
Ensuite deux méthodes existent pour la collecte d'informations auprès de ses sources :

   - Push : On va à la recherche de l'information, cela peut être lorsqu'on va consulté l'Humanité ou autre, cela peut prendre du temps, mais c'est gratuit ...
   - Pull : Les informations vont à notre recherche, on configure un outil pour nous notifier des activités des différentes sources que nous avons identifié, on peut y appliqué des filtres pour spécifier nos recherches, pour cela des outils existent mais bien souvent payant.

#### Choisir son outil :

J'ai testé les produits suivants :

  - [Feedly](https://feedly.com/) --> Bon UI, compatibles avec bcps de sites, mais les fonctionnalités de base sont payantes.
  - [Inoreader](https://www.inoreader.com/fr/) --> Pareil que Feedly, 
  - [NewsBlur](https://newsblur.com/), Open-source, gratuit mais pas vraiment de fonctionnalités qui le rendent plus utiles qu'une recherche classique.
  - [Raven Reader](https://github.com/hello-efficiency-inc/raven-reader), NewsBlur en un peu beau, tout site ayant un flux RSS, cela pourrait faire partie d'un futur projet de cloner ce répertoire et d'y ajouter une fonction de filtre par mots, le projet n'est plus maintenu donc aucun modification n'est acceptée mais une nouvelle version est en préparation ...

## Mettre en place :

### 1 / Analyser ses besoins :

J'aimerais effectuer une veille pour préparer mon stage, le sujet étant d'imaginer la présence possible des forces de l'ordre dans le métaverse. Par conséquent, j'aimerais comprendre les différents acteurs, événements, concepts relatif à ce milieu, il faudra étendre aussi au sujet de la blockchain.
Je souhaite développer cette veille sur quelques mois pour préparer mon stage et m'aider dans mes premiers temps pour comprendre le sujet.

### 2 / Définir le périmètre :

J'aimerais comprendre plus spécifiquement :

  - les problèmes, les crimes qui surviennent pour le moment,
  - comprendre les développements futurs de cet espace pour mieux comprendre les usages actuels et potentiels,
  - les acteurs majeures de cet éco-système,

Par conséquent, les mots-clés que j'ai choisi de suivre sont les suivants :

   - Métaverse,
   - Réalité Mixte,
   - Réalité Virtuelle,
   - Blockchain,
   - Decentraland,

Les mots-clés ne me permettent pas forcément d'avoir exactement ce que je veux, par conséquent la spécification se fera principalement par les sources.

### 3 / Identifier ses sources :

##### Les sources classiques : blog, journal, ... 

Je cherche des sources spécialisées dans la sécurité informatique pour ne pas avoir un bruit trop important avec des news inutiles sensationnalistes en rapport avec le Métaverse.

 - [Revue Réseaux](https://www.cairn.info/rss/rss_revue-RES.xml)
 - [CNRS](https://lejournal.cnrs.fr/rss)

##### Les réseaux sociaux :

J'aimerais suivre des médias pour comprendre les tendances mais aussi des think tank ou des spécialistes pour avoir un -e vision plus long-terme. La fonctionnalité de filtrage par mots-clé est nécessaire pour les flux de réseaux sociaux pour éviter le bruit inutile.
Ce medium va abrité des acteurs parfois biaisé, intéressé, sensationnaliste ...

- Reddit :  
  
  - [SubReddit Crypto](https://www.reddit.com/r/CryptoCurrency/)
  - [SubReddit Métaverse](https://www.reddit.com/r/metaverse/)

- Twitter :
  
  - @Metaverse
  - @EUBlockchain
  - @adan_asso --> lobby
  - @accessnow --> asso de défense des droits numériques
  - @laquadrature --> asso de défense des droits numériques

### 4 / Collecter les sources :

Pour le moment, la méthode push est privilégiée toutefois je développe mon app mais pour le moment, la fonctionnalité essentielle est RSS puis filtre puis compatibilité avec Twitter mais cela ne rentrera jamais dans les 10h ...
Pour pallier au problème de prix et de fonctionnalité, j'ai eu le choix entre créer une application dédiée ou bien commencer petit avec des automatisations simples. J'ai donc créer une série d'automation sur la plateforme [Zapier](https://zapier.com/app/dashboard) pour récolter des flux rss, les filtrer de façon stricte m'envoyer un message discord.
C'est simple mais je peux suivre 10 flux RSS avec un filtre plutôt strict pour pas avoir plus de 3 notifs par jour.
Cette solution est efficace pour les flux RSS mais n'est pas compatible avec Twitter et Reddit car leurs APIs ne sont plus disponibles.

Voici le template que j'ai crée : [cliquez ici](https://zapier.com/shared/b388aedb52dd5d5fb3c11bf51d62d9ade926c1c7)
Cela me permets d'avoir tout les jours un condensé côté métaverse et côté RI grâce à des filtres de temps et de mots clé.

### 5 / Traiter et analyser :

Analyse en cours ... Affaire à suivre dans [mon POK](../pok/Rapport.md)

### Résultats :

J'aime bien le concept mais c'est chiant qu'il n'y est rien de gratuit, comme Mr.Magnagni l'avait expérimenté, les outils manquent encore pour faire ça bien... La méthode pour le cadrage et identifier les sources est intéressante, je pense que je vais poursuivre cette veille toutefois cela restera chronophage.

#### Horodatage :

[19/02] : Lecture sur concept, démarche = 1h30
[21/02] : Établir le cadre, les limites de ma veille  = 1H
[24/02] : Test des différentes solutions et sélection : [Feedly](https://feedly.com/), [Inoreader](https://www.inoreader.com/fr/), [NewsBlur](https://newsblur.com/), [Raven Reader](https://github.com/hello-efficiency-inc/raven-reader) = 1h30
[24/02] : Penser à faire une application de lecture de flux RSS avec des filtres, car aucune app ne le permet alors que ça n'a pas l'air si complexe ... = 1H
[25/02] : Identification des sources pertinentes : 2H
[27/02] : Mise en place d'automatisation Zapier : 2H
[27/02] : Analyse des articles triés et sélectionné par l'automatisation : 1H
