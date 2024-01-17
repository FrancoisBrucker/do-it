---
layout: layout/mon.njk

title: "Kubernetes"
authors:
  - Arthur Louradou

date: 2024-01-17

tags: 
  - "temps 2"
  - "kubernetes"
  - "devops"

résumé: "Ce MON a pour objectif de se former à l'orchestrateur Kunbernetes pour continuer la montée en compétences DevOps de ce temps."
---

<br />
<img align="center" width="500" src="./assets/kube-logo.png" alt="Logo Kubernetes" />

## Objectifs

L'objectif est avant tout de comprendre le rôle d'un orchestrateur dans le déploiement d'une application, en particulier web.

Ensuite, l'idée est de se familiariser avec Kubernetes. Si cela vous intéresse de découvrir comment sont déployées des applications (sites webs, APIs, bases de données dans le Cloud, etc.) de façon moderne : vous êtes au bon endroit !

## Prérequis

Des connaissances solides en Linux sont nécessaires pour aborder la pratique de ce MON. Autant que faire ce peut, je tâcherai de rendre compréhensible pour des néophytes les tâches exécutées. Aussi, je recommande vivement la lecture des différents MONs de Do_It à propos de Docker, auxquels je ferai régulièrement référence lors de cette restitution. En effet, nous allons déployer des applications que nous avons préalablement empaquetées avec cet outil.

## Autres MONs

<img align="right" width="350" src="./assets/docker-logo.svg" alt="Logo Docker" />

Je renvoie à nouveau vers les différents MON sur Docker, puisque celui-ci sera la continuité de mon [MON 2.1](../temps-2.1).

Évidemment, re recommande toujours la lecture des différents MONs de Do_It, qui sont très bien faits et qui m'ont permis de monter en compétences sur ces sujets DevOps.
 - [Docker - Tunçay](../../../../2022-2023/Bilgi-Tuncay/mon/Docker/)
 - [Docker - Victor](../../../Victor-Ory/mon/Docker/)

## Objectifs du MON

L’objectif qui sera notre fil conducteur sera de déployer une application comprenant un Back-End, un Front-End et une belle base de données à l’aide d’un orchestrateur pour le rendre plus résilient aux erreurs et aux lenteurs qui peuvent survenir dans un projet informatique. Le but est de se former à des problématiques rencontrées en entreprise pour monter en compétences dans les domaines auxquels j’ai pu postuler et auxquels je postulerai à l’avenir.

Prêt ? Alors c’est parti : embarquons dans le monde merveilleux des orchestrateurs…

## Un orchestrateur, pourquoi faire ?

Un outil d’orchestration permet de gérer des applications conteneurisées. Pour rappel, un conteneur est une unité d'exécution légère et autonome qui contient tout ce dont une application a besoin pour s'exécuter, y compris le code, les dépendances et les configurations. Les conteneurs sont portables, faciles à déployer et à mettre à l'échelle, et ils offrent un environnement isolé pour exécuter des applications.

L’intérêt majeur est la disponibilité : si un container tombe à l’intérieur d’un orchestrateur, l’application reste disponible. En effet, l’orchestrateur peut se charger de lancer plusieurs instances d’une même application (un back-end par exemple) et de relancer une instance qui aurait crashé.

Ensuite, celui-ci permet de régler des problématiques de mise à l’échelle. En effet, en fonction de la demande sur un site, la charge et le temps de réponse diffèrent. C’est pourquoi l’orchestrateur choisit de répartir la charge et de définir des règles qui augmentent la scalabilité (un anglicisme souvent employé dans le monde de la blockchain pour parler de mise à l’échelle) d’une application.

## Les bases de Kubernetes

### Cheat Sheet des commandes apprises au cours du MON

Je recommande vivement de lire le [cheat sheet](./cheat_sheet) que j'ai rédigé pour ce MON. Il contient les commandes de base pour utiliser Kubernetes.

