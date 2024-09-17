---
layout: layout/pok.njk

title: "Un POK traitant de la création d'une plateforme de certification en ligne"
authors:
  - Serigne Mbaye Sy AMAR

date: 2024-16-09

tags: 
  - "développement web"
  - "Laravel "

résumé: Un POK traitant de la création d'une plateforme de certification en ligne où les utilisateurs peuvent suivre des cours en vidéo et obtenir un certificat après évaluation.
---

{% prerequis %}

- Avoir des connaissances en développement web (HTML, CSS, JavaScript).
- Connaître le framework back-end Laravel.
- Des bases en bases de données (MySQL).
- Connaître l'utilisation de systèmes de gestion des utilisateurs et d'authentification.

{% endprerequis %}
{% lien %}

[Les lien utiles pour la compréhension de celui-ci.](https://laravel.com/docs/10.x)

{% endlien %}


## Tâches
L'objectif de ce projet est de créer une plateforme en ligne où les étudiants peuvent suivre des cours en vidéo et passer une évaluation pour obtenir un certificat. Les instructeurs peuvent s'inscrire, et une fois approuvés par le super administrateur, ils peuvent ajouter des cours. Le projet est divisé en trois sprints pour structurer les étapes de développement.
### Sprints

But final: 
Créer une plateforme fonctionnelle de certification en ligne avec :

- Un espace pour les étudiants où ils peuvent s'inscrire, visionner des cours, et passer des tests d'évaluation.
- Un espace pour les instructeurs permettant d'ajouter et de gérer leurs cours après approbation par un administrateur.
- Un système d'authentification sécurisé avec gestion des droits d'accès.
- Un système de paiement en ligne pour l'accès aux cours ou aux certifications.

#### Sprint 1 : : Frontend de la plateforme

Ce sprint est dédié à la création de l'interface utilisateur de la plateforme et la la mise en place des systèmes d'authentification et des droits d'accès pour les différents rôles (étudiant, instructeur, super admin). Les tâches incluent la conception des pages et l'intégration du frontend.

- [x] Concevoir la page d'accueil et les pages de présentation des cours.
- [x] Créer les formulaires d'inscription pour les étudiants et les instructeurs.
- [x] Mettre en place la structure des pages pour les vidéos de cours.
- [x] Implémenter le système d'authentification pour les étudiants et les instructeurs.
- [x] Créer une page de connexion pour les utilisateurs.
- [ ] Développer un tableau de bord pour le super admin afin de gérer les comptes.
***Étude post-mortem :***  À la fin de ce sprint, je vais évaluer les composants d'interface sont bien fonctionnels et ajuster les éventuels bugs ou incohérences graphiques pour le prochain sprint. Je vais aussi réviser l'efficacité du système de gestion des utilisateurs et des accès. Vérifier si les rôles sont bien distribués et s'assurer qu'il n'y a pas de faille de sécurité.

#### Sprint 2 : Sécurité, ajout de cours et gestion des paiements
Ce sprint est dédié à l'ajout de fonctionnalités permettant aux instructeurs de créer des cours, aux étudiants de les suivre et de passer des évaluations, et à la gestion des paiements pour accéder aux cours ou obtenir les certificats.
  - [ ] Mettre en place un système de gestion des rôles et des droits d'accès.
  - [ ] Assurer la sécurité des données des utilisateurs (chiffrement des mots de passe, HTTPS).
  - [ ] Permettre aux instructeurs de créer, modifier et supprimer des cours.
  - [ ] Intégrer un lecteur vidéo pour permettre aux étudiants de suivre des cours en ligne.
  - [ ] Créer des évaluations pour chaque cours avec un système de notation.
  - [ ] Générer des certificats après la réussite des évaluations.
  - [ ] Intégrer un système de paiement.
 ***Étude post-mortem :*** Évaluer la fluidité de la gestion des cours, le processus de paiement et la génération de certificats. Ajuster les problèmes liés à l'expérience utilisateur ou à la gestion des données.


### Horodatage

Toutes les séances et le nombre d'heure que l'on y a passé.

| Date | Heures passées | Indications |
| -------- | -------- |-------- |
| Mardi 27/08  | 1H  | Travail sur la trame du site |

## Contenu

Le contenu du POK.
