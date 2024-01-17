---
layout: layout/mon.njk

title: "Prise de note tutoriel viéo Kubernetes"
authors:
  - Arthur Louradou

date: 2024-01-17

tags: 
  - "temps 2"
  - "kubernetes"
  - "devops"
---

## Source

[Kubernetes Crash Course for Absolute Beginners [NEW]](https://www.youtube.com/watch?v=s_o8dwzRlu4)

## Master Node

Ce qui tourne sur le master Node :

- Un serveur API qui constitue une entrée vers le cluster Kubernetes
- Un controller manager qui garde la trace de ce qui se passe dans le cluster
- Un Scheduler qui s’assurer de la programmation en fonction de la charge de chaque nœud
- Un etcd qui garde le status de chaque nœud pour stoker les états de chaque nœud (une sorte de base de données)
- Un réseau local dans lequel sont déployés les nœuds (worker nodes)

Un point important est d’avoir plusieurs master nodes pour qu’en cas de panne du premier master on ait une redondance à l’accès aux worker nodes.

## Node et Pod

Un **Node** ou nœud est une machine (virtuelle ou physique).

Un **Pod** est une unité dans Kub, et est une abstraction du container Docker.

Souvent, un pod a une seule application conteneurisée à l’intérieur. Chaque Pod a une adresse IP locale à l’intérieur. Ils sont éphémères et peuvent changer d’IP lorsqu’ils redémarrent. C’est pourquoi on met en place des **services**, attachés à un Pod et qui eux ne changent pas.

Un **service** a bien une adresse IP définie. Il est possible d’avoir des services **externes** et **internes**. Pour les services externes, il est possible d’ajouter une sorte de résolveur DNS appelé **ingress**.

## Mise en place de ConfigMap et de secrets

Permet la configuration par exemple des adresses de bases de données et autres services qui doivent être appelés dans l’appli.

Pour les données secretes comme les noms d’utilisateur et mots de passe, il y a aussi un module pour ça et on peut sécuriser les secrets en les chiffrant avec des outils externes.

## Faire persister une base de données alors qu’elle est lancée sur plusieurs Pods

Comme avec Docker, il est possible de rattacher un **volume** à nos services. Le stockage peut être interne ou distant (dans le Cloud par exemple).

## Deployment et Statefulset

Un déploiement est un clone du serveur qui permet de switcher quelle nœud est appelé si une application tombe.

Il est possible de répliquer une base de données mais on doit s’assurer de la consistance des données à l’intérieur. Pour cela, on a besoin d’un autre élément qui gère l’état et la consistance. Ce n’est pas une tâche facile et elle peut être coûteuse.

## Configuration

Nous avons vu qu’il y avait 3 possibilités pour interagir avec Kub : UI, API ou ligne de commande (kuectl). Cela signifie que l’on va lui glisser des fichiers de configuration sous format yaml ou json pour lui indiquer les déclarations de Deployments et des Services

- Metadata
- Specifications : dépendent du type (deployment ou service)
- Status (généré automatiquement) : compare l’état désiré à l’état courant

<aside>
💡 Stocker les fichiers de configuration sur le repo git est une bonne pratique

</aside>
