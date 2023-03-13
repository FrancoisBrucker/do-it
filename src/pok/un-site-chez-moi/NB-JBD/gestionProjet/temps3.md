---
layout: layout/post.njk

title: "Jeu Mots croisés - Temps 3"
authors:
  - Nicolas BERT
  - Jean-Baptiste DURAND

tags: 
    - 'pok3'
    - 'amélioration-continue'
---

## Choses à faire durant ce temps 3

- Amélioration du jeu (style, mécanique ...)
- Écriture de tests ?
- Optimisation du déploiement (scripts ou pipeline)

## 1er Sprint

- Mettre en place des tests sur le back

## Ce qui a été fait au 1er sprint

- Tests sur le microservice de génération de grille
- Mise en place de protections de la branche *main* sur github avec :
  - Blocage des commits
  - Merge si les tests passent
- Nettoyage de toutes les fonctions inutiles du Back