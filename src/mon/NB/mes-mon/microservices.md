---
layout: layout/post.njk

title: "Microservices"
authors:
  - Nicolas BERT

---

<!-- début résumé -->
Introduction aux microservices en informatique
<!-- fin résumé -->

Dans ce MON, nous allons discuter du principe de microservices et plus particulièrement de son utilisation et implémentation en informatique.

## Introduction

Quand on pense aux microservices, on pense premièrement à plein de petites structures bien organisées qui sont chacune responsable d'une fonctionnalité et destinée à fonctionner ensemble.

Cette organisation de "délégation" et de "répartition" du travail n'est clairement pas anodine. On retrouve cette méthode de travail à de nombreux niveaux. Par exemple, le gouvernement français est découpé en ministère qui vont chacun s'occuper d'un domaine particulier (santé, justice, éducation, travail, intérieur ...) tout en fonctionnant en les uns avec les autres. De même, lorsque l'on travail en équipe projet à Centrale chacun se répartit le travail et s'occupe d'une partie du projet tout en restant avertit du travail des autres. L'idée de cette répartition des tâches est de gagner en efficacité, clarté, organisation et performance. Ce concept se démocratise beaucoup et est devenu très populaire dans les projets IT.

## Le concept de microservice

### Historique

Le terme **microservices** est apparu en 2011 au cours d'ateliers d'architecture, bien qu'il réutilise un grand nombre de principes largement employés par les systèmes d'information des grandes entreprises, notamment les concepts de l'architecture orientée service (SOA). Le sujet est réellement évoqué à partir de 2014 selon Google Trends. Parmi les pionniers, on compte **Netflix** qui a oeuvré pour populariser ces architectures.

### Philosophie

La philosophie de l'architecture en microservices s'inspire en grande partie de la **philosophie UNIX** qui prône **"ne faire qu'une seule chose, et la faire bien"**. Elle est décrite de la façon suivante :
- Les services sont **petits** et conçus pour remplir **une seule fonction** (facturation, interface, sécurité, authentification ...).
- Chaque service est élastique, résilient, composable, minimal et complet.
- Les services individuels sont **simples à remplacer**.
- Ils peuvent être **développés et déployés indépendamment** les uns des autres.
- L'organisation du projet doit prendre en compte **l'automatisation**, **le déploiement** et **les tests**.
- L'architecture est plus **horizontale** que verticale (passage d'une architecture client-serveur à une architecture de plusieurs entités communicantes)

{% info %}
En informatique, l'architecture en **microservices** est une technique de développement logiciel qui structure une application comme un ensemble de services faiblement couplés. Un microservice est une fonction/fonctionnalité essentielle d'une application. Ainsi, chacun peut fonctionner (ou dysfonctionner) sans affecter les autres. Les microservices indépendants communiquent les uns avec les autres en utilisant des API (REST la plupart du temps) indépendantes du langages de programmation.
{% endinfo %}

L'architecture en microservices permet aussi de restructurer les équipes de développement et la communication entre les services pour mieux se préparer aux inévitables pannes, mais aussi aux évolutions futures et à l'intégration de nouvelles fonctions.

## Est-ce que découper son application en fonctionnalités c'est faire du microservices ?

Attention, on a l'habitude de découper une application en fonctionnalités/services (**S**ervice **O**riented **A**rchitecture) afin d'éviter une application monolithique très difficile à maintenir et faire évoluer. Cependant, l'architecture en microservices ressemble à la SOA mais diffère sur quelques points.

L'architecture orientée services structure les applications en services individuels et réutilisables qui communiquent via un ESB (Entreprise Service Bus). Dans cette architecture, chaque service individuel suit une protocole de communication (SOAP, ActiveMQ ou Apache Thrift) pour se "déplacer" dans l'ESB. Ensemble, tous ces services intégrés via l'ESB constituent l'application. D'un côté cela permet de développer, tester et paramétrer les services simultanément et ainsi échapper au cycle des développement monolithiques. Par ailleurs, l'ESB représente un point individuel de défaillance pour l'ensemble du système. Ainsi, les efforts pour supprimer le "monolithe" n'ont fait qu'en créer un autre.

Dans une architecture en microservices, les microservices peuvent communiquer entre eux de manière directe. Les applications développées en microservices sont donc plus tolérantes aux pannes et ne sont pas tributaires d'un seul service (ESB). PAr ailleurs, cela permet à chaque équipe d'utiliser n'importe quelle technologie/langage pour développer le microservice dont ils ont la responsabilité.

{% info %}
L'architecture en microservices n'est pas une idée nouvelle (comparaison avec la SOA) cependant elle est devenue plus viable grâce aux progrès réalisés en matière de technologies. La conteneurisation Linux réalisée le plus souvent à l'aide de Docker, permet d'exécuter plusieurs parties d'une application indépendamment les unes des autres. Avec les API et le DevOps, les microservices conteneurisés sont la base des applications cloud-native.
{% endinfo %}


## Avantages et inconvénients

**Avantages** :
- Nouvelle manière de travailler, les développeurs peuvent travailler plus aisément sur le développement simultané de plusieurs microservices. Ainsi plusieurs personnes peuvent travailler en même temps sur l'application, on gagne du temps !
- Les déploiements sont facilités grâce au processus de CI/CD qui est facilité.
- L'architecture dispose d'une grande évolutivité, on peut étendre les déploiements sur plusieurs infrastructures.
- Les services sont résilients, ils n'ont aucun impact sur les autres. Si un service tombe en panne, l'ensemble de l'application ne cesse pas de fonctionner comme pour une application monolithique.
- L'évolution et l'amélioration des services sont grandement accélérés grâce aux cycles de développement plus courts surtout si cette architecture est associée aux méthodes de développement agiles.
- Les services étant indépendants les uns de autres, les équipes peuvent choisir les technologies et langages qui conviennent le mieux.


**Inconvénients** : 
- Les services étant séparés par rapport à une architecture classique, le coût de mise en place est plus important.
- Difficulté d'adaptation si l'entreprise envisage de passer à une architecture en microservices (techniques, méthodologie de travail, responsabilité, )

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

## Exemple de microservices

Il existe de nombreuses façons de découper un projet en microservices. Pour l'exemple uniquement, voici comment Amazon pourrait organiser une partie de son application en microservice. *(Amazon fonctionne très probablement en microservices, mais le découpage que je propose est purement fictif)*

<img src="./../images/amazon.png" style="width: 100%;">

Ici j'ai pris l'exemple de la recherche d'un article et de son achat sur Amazon. Chaque fonctionnalité représenté par un rectangle rouge pourrait être organisé comme un microservice.

- La barre de recherche
- Les suggestions d'articles (à l'aide d'algorithme se basant par exemple sur les précédentes visites de l'utilisateur, la période actuelle, sa localisation ....)
- La partie concernant la livraison (estimation des délais de livraison, retour de produits, gestion des stocks...)
- Le panier
- ...

Toutes ces fonctionnalités, qui sont externes au site (dans le sens où elles vont faire appel à des algorithmes externes et afficher seulement le résultat sur le site), peuvent être découpées et séparées en microservices. On peut évidemment pensez à d'autre fonctionnalités : paiement, évaluations des produits ...





## Sources

- https://fr.wikipedia.org/wiki/Microservices
- https://www.redhat.com/fr/topics/microservices/what-are-microservices
