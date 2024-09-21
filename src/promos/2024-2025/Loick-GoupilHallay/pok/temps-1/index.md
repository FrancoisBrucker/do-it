---
layout: layout/pok.njk

title: "Déploiement automatisé de l'environnement de développement"
authors:
  - Loïck Goupil-Hallay

date: 2024-09-05

tags:
  - "temps 1"
  - "dev"
  - "cyber"

résumé: Déploiement automatisé d'un environnement de développement sécurisé pour une équipe de développement moderne
---

# Déploiement automatisé de l'environnement de développement
Le but est de déployer de manière automatisée et sans possibilité d'échec un environnement de développement sécurisé et complet pour une équipe de développement moderne.

## Liens
- [GitHub](https://github.com/boxboxjason/svcadm)


## Introduction

Ce POK se base sur un projet déjà existant qui déployait à l'époque des services antivirus de manière automatisée en utilisant des conteneurs accessibles depuis un proxy.\
Le code était écrit en bash et était peu personnalisable.

## Planification

### Sprint Planning 1
- [ ] Outil de gestion des codes sources
- [ ] Cluster de base de données
- [ ] Outils de gestion des artefacts
- [ ] Outils de communication
- [ ] Outil d'analyse de qualité de code
- [ ] Outil d'analyse antivirus

## Pratique

Le sprint ne s'est pas du tout déroulé comme prévu, j'ai trouvé qu'il y avait très peu de plus value à réécrire des scripts non personnalisables en bash.\
Cela ne correspond pas du tout au besoin des équipes de développement modernes qui veulent des outils personnalisables et faciles à utiliser.

J'ai donc réorienté le fonctionnement du projet, en offrant la possibilité de customiser les services à déployer et en utilisant un fichier de configuration pour les paramétrer.

Pour m'offrir plus de flexibilité, j'ai décidé d'utiliser golang pour l'intégralité du code car c'est un langage que je maîtrise bien et qui est utilisé pour la plupart des opérateurs de conteneurs & kubernetes.

### Sprint Réel 1
- Rédaction d'un fichier de configuration pour l'outil entier (1h)
  - Choix des services à activer
  - Paramétrage de chaque service
- Code du parser & validateur de fichier de configuration (5h)
- Code du script de déploiement par des conteneurs (1h)
- Fine tuning pour chaque service (3h)

