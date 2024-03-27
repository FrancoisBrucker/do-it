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

## Rappels { #rappels }

Le projet permettant aux élèves de Do_It de consulter leur emploi du temps est déployé à l'adresse suivante :

<a href="http://node.oignon.ovh1.ec-m.fr/" class="buttonGithub">
  <span>Accéder à SérénaDo_It !</span>
</a>

(Tenez, une belle animation qui vous donnera envie de lire [mon dernier MON](../../mon/temps-3.2/) peut-être ? 😉)

Le projet a été débuté au temps 2, et a été présenté dans le [POK 2](../temps-2/). Le code source est disponible [sur mon GitHub](https://github.com/alouradou/SerenaDo_It).


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

## Sprint 4 - Finitions { #sprint-4-finish }

J'ai finalement pu continuer ce dernier Sprint en mettant en place plusieurs fonctionnalités qui semblaient cruciales pour la pérennisation du projet.

D'abord, j'ai ajouté une base de donneées pour gérer plusieurs éléments :

1. La modification des feuilles de calculs sources de la donnée (utile pour le changement d'anée scolaire)
2. La gestion des noms de cours donnés sur la feuille de calcul
3. La gestion du cache pour éviter de recalculer les emplois du temps à chaque fois

On peut s'amuser un peu avec l'interface d'administration pour supprimer et ajouter des cours : 
[La page d'administration](http://node.oignon.ovh1.ec-m.fr/admin)

Avec la fonctionnalité de personnalisation du calendrier, il devient crucial de pouvoir associer fidèlement les cours donnés sur la feuille de calcul EDT avec ceux du sheet élève (choix des cours).
Pour cela, le parti pris a été de laisser cette opération à tous les utilisateurs qui souhaitent contribuer.

Dès lors, si un cours n'est pas reconnu, il est possible de l'ajouter dans la base de données pour l'associer à un cours du sheet élève et qu'il soit reconnu par la suite. À chaque fois qu'un emploi du temps est demandé par l'utilisateur, apparaitra la liste des cours aux noms non reconnus pour qu'il puisse les associer à un cours de la base de données.

Il n'y a pas encore de système qui permette d'en avertir l'utilisateur dans la page, mais on peut imaginer une notification qui apparaitrait en haut de la page.


## Conclusion { #conclusion }

Finalement, à l'issue de ces quatre Sprints, il s'est passé beaucoup de choses et j'ai appris énormément.

J'ai pu conceptualiser une preuve de concept à partir de l'analyse d'un besoin du côté des étudiants, puis j'ai pu le développer et le déployer. Entre ces étapes, beaucoup de technologies et techniques ont été utiles et que je peux remettre en perspective avec l'anneée passée et mon parcours scolaire qui s'achève (presque...).

En effet, les cours de Data que j'ai suivi durant ma césure m'ont permis de mener à bien cette preuve de concept en explorant les possibilités offertes par différentes bibliothèques dans des notebooks Python. Ensuite, les cours d'Ops suivis en Do_It nous ont offert une connaissance de la mise de ligne d'APIs et de la gestion de serveurs. Je m'en suis servi pour consruire le serveur Flask qui fait tourner la plateforme. Nous avons aussi appris à mettre en place des bonnes pratiques pour ce code, notamment avec les tests unitaires et l'intégration continue dans des cours de Do_It, ce n'est pas à négliger ! Aussi, les POKs et les MONs des autres élèves ont fait expérimenter le travail collaboratif.

Enfin, j'espère que ce projet pourra être utilisé l'année prochaine grâce aux fonctions d'administration et de déploiement continu fraichement ajoutées.


<style>
    a.buttonGithub {
      display: inline-block;
      padding: 15px 30px;
      background-color: #3498db;
      color: #fff;
      border-radius: 10px;
      border: 2px solid #3498db;
      text-decoration: none;
      position: relative;
      overflow: hidden;
      transition: background-color 0.3s, transform 0.3s ease-in-out;
    }

    a.buttonGithub:hover {
      background-color: #3498db;
      transform: translateY(-5px);
      color: #3498db;
    }

    a.buttonGithub span {
      position: relative;
      z-index: 1;
    }

    a.buttonGithub::before {
      content: "";
      position: absolute;
      top: 0;
      left: -100%;
      width: 100%;
      height: 100%;
      background-color: #fff;
      transition: left 0.3s;
    }

    a.buttonGithub:hover::before {
      left: 0;
    }
  </style>

