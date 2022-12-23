---
layout: layout/post.njk

title: "Microservices"
authors:
  - Nicolas BERT

---

<!-- début résumé -->
Introduction aux microservices en informatique
<!-- fin résumé -->

Dans ce MON, nous allons discuter du principe de microservices et plus particulièrement en informatique.

## Introduction

Quand on pense aux microservices, on pense premièrement à plein de petites structures bien organisées qui sont chacunes responsables d'une fonctionnalité et destinées à fonctionner ensemble.

Cette organisation de "délégation" et de "répartition" du travail n'est clairement pas anodine. On retrouve cette méthode de travail à de nombreux niveaux. Par exemple, le gouvernement français est découpé en ministère qui vont chacun s'occuper d'un domaine particulier (santé, justice, éducation, travail, intérieur ...) tout en fonctionnant en les uns avec les autres. De même, lorsque l'on travail en équipe projet à Centrale chacun se répartit le travail et s'occupe d'une partie du projet tout en restant avertit du travail des autres. L'idée de cette répartition des tâches est de gagner en efficacité, clarté, organisation et performance. Ce concept se démocratise beaucoup et est devenu très populaire dans les projets IT.

## Définition & concept

*(issu de https://fr.wikipedia.org/wiki/Microservices)*

### Historique

Le terme **microservices** est apparu en 2011 au cours d'ateliers d'architecture, bien qu'il réutilise un grand nombre de principes largement employé par les systèmes d'information des grandes entreprises, notamment les concepts de l'architecture orientée service (SOA). Le sujet est réellement évoqué à partir de 2014 selon Google Trends. Parmi les pionniers, on compte **Netflix** qui a oeuvré pour populariser ces architectures.

### Philosophie

La philosophie de l'architecture en microservices s'inspire en grande partie de la **philosophie UNIX** qui prône **"ne faire qu'une seule chose, et la faire bien"**. Elle est décrite de la façon suivante :
- Les services sont **petits** et conçus pour remplir **une seule fonction** (facturation, interface, sécurité, authentification ...).
- L'organisation du projet doit prendre en compte **l'automatisation**, **le déploiement** et **les tests**.
- Chaque service est élastique, résilient, composable, minimal et complet.
- Les services individuels sont simples à remplacer.
- L'architecture est plus symétrique que hiérarchique (passage d'une architecture client-serveur à une architecture de plusieurs entités communicantes)

{% info %}
En informatique, les **microservices** sont une technique de développement logiciel qui stucture une application comme un ensemble de services faiblement couplés. Les microservices indépendants communiquent les uns avec les autres en utilisant des API (REST la plupart du temps) indépendantes du langages de programmation.
{% endinfo %}

### Avantages et inconvénients

Lorsqu'une ressource a besoin d'être mise à jour, seul le microservice contenant cette ressource aura besoin d'être mis à jour, l'ensemble de l'application restant compatible avec la modification, contraitement à une architecture classique ou la totalité de l'application serait en panne (ex: architecture trois tiers = front/back/db ou modèle MVC).

En revanche, les services étant séparés par rapport à une architecture classique, le coût de mise en place est plus important.

https://www.redhat.com/fr/topics/microservices/what-are-microservices