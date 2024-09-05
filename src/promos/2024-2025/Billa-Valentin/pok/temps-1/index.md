---
layout: layout/pok.njk

title: "GoAuth2"
authors:
  - Valentin Billa

date: 2024-09-05

tags: 
  - 'temps 1'
  - 'vert'
  - 'avancé'
  - 'Go'
  - 'Authentification'
  - 'OAuth2'

résumé: Création d'un serveur OAuth2 en Go.
---

# POK 1 - GoAuth2
Création d'un serveur OAuth2 en Go

## Objectifs
Je n'ai jamais codé en Go, mais le langage m'intrigue depuis un moment,
c'est pourquoi j'ai envie de tenter de coder un projet concret pour m'initier aux bases.
En l'occurence, ce sera un serveur d'authentification OAuth2,
mes connaissances sur le sujet sont relativement superficielles,
c'est pourquoi je souhaite les approfondir au long de ce POK.

## À propos de OAuth et Go
OAuth est un protocole d'autorisation utilisé pour permettre à des applications tierces d'accéder aux
ressources d'un utilisateur sans divulguer les identifiants de celui-ci. Il est couramment utilisé pour
permettre des connexions via des services comme Google, Facebook, etc.

Go (ou Golang) est un langage de programmation développé par Google, connu pour sa simplicité,
ses performances élevées, et son support solide pour la concurrence grâce aux goroutines.

## Plan d'action
> Volontairement très (trop) fourni, pour être certain de ne pas manquer de contenu.

### Sprint 1
- **Introduction à Go**
    - Configurer l'environnement de développement Go.
    - Parcourir les tutoriels de base sur Go.
    - Écrire quelques programmes simples pour se familiariser avec la syntaxe et les concepts de Go.

- **Concepts de base d'OAuth2**
    - Étudier le protocole OAuth2 (RFC 6749).
    - Comprendre les différents rôles (Client, Ressource Owner, Authorization Server, Resource Server).
    - Examiner les types de flux (Authorization Code, Implicit, Resource Owner Password Credentials, Client Credentials).

- **Développement initial**
    - Créer un projet Go pour le serveur OAuth2.
    - Implémenter une première version du serveur OAuth2 avec les routes de base pour l'autorisation et les tokens.
    - Tester les premières implémentations avec des clients simples.

### Sprint 2
- **Tests et Client**
  - Écrire des tests unitaires pour quelques fonctions internes.
  - Écrire des tests d'intégration pour les routes principales.
  - Créer une page de connection avec Java Spring Boot Oauth.

- **Persistence des données**
    - Choisir et configurer une base de données (ex. MySQL).
    - Mettre en place les schémas de base pour stocker les utilisateurs, les clients OAuth2, et les tokens.
