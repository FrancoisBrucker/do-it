---
layout: layout/post.njk

title: "Jeu Mots croisés - Temps 3"
authors:
  - Nicolas BERT
  - Jean-Baptiste DURAND

tags: 
    - 'POK'
    - 'temps 3'
    - 'amelioration continue'
---

## Choses à faire durant ce temps 3

- Amélioration du jeu (style, mécanique ...)
- Écriture de tests ?
- Optimisation du déploiement (scripts ou pipeline)

## 1er Sprint

- Mise en place des tests sur le back

## Ce qui a été fait au 1er sprint

- Tests sur le microservice de génération de grille
- Mise en place de protections de la branche *main* sur github avec :
  - Blocage des commits
  - Merge si les tests passent
- Nettoyage de toutes les fonctions inutiles du Back

## 2e Sprint

- Mise en place des logs

## Ce qui a été fait au 2e sprint

- Mise en place de logs personnalisés
- Dockerisation du microservice (mots-croises-generateur):
  - publication sur le [Docker Hub](https://hub.docker.com/repository/docker/instraben13/mots-croises-generateur/general)
  - integration avec Docker Compose