---
layout: layout/pok.njk

title: "SérénaDo_It 2 - Vers un projet pérenne"
authors:
  - Arthur Louradou

date: 2024-03-27

tags: 
  - "temps 3"

résumé: Cette seconde partie du projet SérénaDo_It a pour objectif de définir les bases d'un projet pérenne. Elle abordera la mise en place d'une architecture logicielle robuste, la définition des processus de déploiement continu et la mise en place d'une stratégie de tests unitaires.
---

## Objectifs { #objectifs }

- Améliorations et fonctionnalitées
  - Changer la fonction de suppression des cours pour la rendre plus résiliente
  - Assurer une comparaison entre les emplois du temps
  - Permettre de résoudre la correspondance de noms de cours en base de données (en cas de divergence d'orthographe)
- Mettre en place une stratégie de tests
- CI/CD
  - Déployer le code à l'aide d'une image Docker
  - Mettre en place un pipeline de déploiement continu


### Prévisionnel

#### Sprint 3 { #sprint-3 }

Les temps suivants seront des estimations. Nous pourrons ajouter une colonne à la fin du POK pour mesurer les écarts.

| Tâche                                     | Difficulté | Temps |
|-------------------------------------------|------------|-------|
| Refonte de la fonction de choix des cours | 2          | 2h    |
| Volet d'administration                    | 5          | 4h    |
| Amélioration du cache                     | 3          | 2h    |
| Tests unitaires                           | 2          | 2h    |


#### Sprint 4 { #sprint-4 }

Ce Sprint est encore vague et sera enrichi des retours du sprint 3.

| Tâche                                               | Difficulté | Temps |
|-----------------------------------------------------|------------|-------|
| Export automatique avec validation des cours saisis | 3          | 5h    |
| Intégration et Déploiement continus                 | 8          | 5h    |


### Sprint 3 - Réalisation { #sprint-3-real }

{% info %}
Tout ne s'est pas passé dans l'ordre prévu, la priorisation ayant changé au cours du sprint avec des aléas et des opportunités. Nous allons détailler cela !
{% endinfo %}

### Refonte de la fonction de choix des cours { #refonte-fonction }

Lors de cette étape, j'ai revu la fonction de suppression des cours pour la rendre plus résiliente. Des tests sont désormais exécutés et comparent un Excel de référence avec le résultat du traitement sur plusieurs types d'élèves.

J'ai également ajouté une fonctionnalité de comparaison entre les emplois du temps. Lorsqu'un élève se rend sur son emploi du temps personnel, il peut voir en bleu le sien et en rouge celui de la classe. Cela permet de voir les différences entre les deux et de les signaler si besoin.

Enfin, j'ai initialisé comme prévu un processus de résolution de la correspondance de noms de cours en base de données (en cas de divergence d'orthographe). Cette fonctionnalité sera clé dans la pérennisation du projet et sera donc terminée au prochain sprint.

### Résolution d'un bug (!) { #bug }

Google Calendar a décidé de se comporter différemment des autres logiciels de calendrier (Apple, Thunderbird, etc.). J'ai donc dû revoir la classe qui génère les horaires pour qu'elle inclue la timezone. Les recherches ont pris plus de temps que prévu, mais le bug est résolu.

En effet, la façon dont Google Implémente la gestion des fuseaux horaires est subtilement différente des autres logiciels. `Ce fut donc un combat acharné qui s'achève par des élèves à l'heure (// TODO: fix this in a future commit) 🙂`.

### CI/CD ! { #ci-cd }

Avant de parler d'intégration et de déploiement continu, j'ai consacré du temps au déploiement du code sur le serveur OVH que vous pouvez retrouver sur [le Readme du projet](https://github.com/alouradou/SerenaDo_It/blob/master/README.md).

Ces étapes ont été cruciales pour la suite, notamment la documentation de ces dernières. En effet, documenter ces fonctions m'a permis de mieux comprendre les étapes à suivre pour le déploiement continu.

Ainsi, avant de travailler avec Docker, j'ai décidé de mettre en place une Github Action à la lumière du cours de CI/CD que nous avons eu dans l'électif vert ["AWS/Docker"](#) `(insérer le lien vers le plan du cours dans le futur site)`.

La connexion entre le dépôt Github et le serveur OVH est désormais établie. Le code est automatiquement déployé sur le serveur à chaque push sur la branche `main`. Cela a fait gagner un temps précieux au dépoilement des correctifs mineurs et des nouvelles fonctionnalités développeées par la suite.

L'objectif est maintenant de pérenniser le projet en mettant en place un pipeline de déploiement continu avec Docker. Cela permettra de déployer le code dans un environnement isolé et de s'assurer que le code fonctionne bien avant de le mettre en production.


Voilà le code de la pipeline de déploiement continu GitHub Action qui reprend les principes évoqués dans le Readme :

{% details "Code de la pipeline de déploiement continu GitHub Action" %}
```yaml
name: CI/CD Pipeline

on:
  push:
    branches:
      - master

jobs:
  build:
    name: Build and Test
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Repository
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9

    - name: Install dependencies
      run: |
        python -m venv serenadoit .
        source serenadoit/bin/activate
        pip install -r requirements.txt

    - name: Run tests
      run: |
        # Ajoutez ici les commandes pour exécuter vos tests

  deploy:
    name: Deploy to Server
    runs-on: ubuntu-latest
    needs: build

    steps:
    - name: Checkout Repository
      uses: appleboy/ssh-action@master
      with:
        host: ${{ secrets.SERVER_HOST }}
        username: ${{ secrets.SERVER_USERNAME }}
        key: ${{ secrets.SERVER_SSH_KEY }}
        port: ${{ secrets.SERVER_PORT }}
        script: |
          cd serenadoit
          git stash
          git pull origin master
          git stash pop
          rm -rf ~/node/static/styles/ ~/node/static/scripts/ ~/node/static/images/
          cp -r ./static ~/node/

    - name: Install dependencies and restart server
      uses: appleboy/ssh-action@master
      with:
        host: ${{ secrets.SERVER_HOST }}
        username: ${{ secrets.SERVER_USERNAME }}
        key: ${{ secrets.SERVER_SSH_KEY }}
        port: ${{ secrets.SERVER_PORT }}
        script: |
          cd serenadoit
          python -m venv serenadoit .
          source serenadoit/bin/activate
          pip install -r requirements.txt
          kill $(ps aux | grep "^${{ secrets.SERVER_USERNAME }}" | grep '[g]unicorn' | awk '{print $2}') || true

    - name: SSH to server and deploy
      uses: appleboy/ssh-action@master
      with:
        host: ${{ secrets.SERVER_HOST }}
        username: ${{ secrets.SERVER_USERNAME }}
        key: ${{ secrets.SERVER_SSH_KEY }}
        port: ${{ secrets.SERVER_PORT }}
        script: |
          cd serenadoit
          source serenadoit/bin/activate
          gunicorn -w 4 -b 0.0.0.0:10410 run_prod:app --error-logfile logs/error.log --access-logfile logs/access.log -D

    - name: Check deployment
      run: |
        ps aux | grep "^$USER" | grep '[g]unicorn' || true
```
{% enddetails %}

### Correction de bugs mineurs { #bugs-mineurs }

Le sprint a aussi été l'occasion de corriger quelques bugs mineurs et améliorer des fonctionnalités. On peut citer quelques modifications de style et de texte, ainsi que des améliorations de performances qui seront complétées dans le dernier sprint par une gestion efficace du cache.

## La suite { #la-suite }

J'attends des feedbacks des utilisateurs pour prioriser les tâches du sprint 4. Jusqu'ici, cela m'a permis d'aboutir à une version stable et une idée claire des fonctionnalités du projet.

