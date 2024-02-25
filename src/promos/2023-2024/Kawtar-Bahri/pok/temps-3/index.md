---
layout: layout/pok.njk

title: "Automatisation de l'analyse des dépenses technologiques - VBA Excel "
authors:
  - Kawtar Bahri

date: 1971-03-01

tags: 
  - "temps 3"

résumé: L'objectif de ce projet est de me préparer au stage de fin d'études en apprenant plus sur les dépenses technologiques des entreprises et m’introduisant au VBA.  Le rendu de ce POK est une solution VBA Excel pour automatiser l'analyse des dépenses technologiques d’une entreprise.
---

## Feuille de route
- Recherches sur les dépenses technologiques des entreprises 
- Sélection des dépenses à étudier et leurs normes (pour pouvoir faire le suivi et les alertes)
- Configuration des fonctionnalités de base (structure de base du classeur Excel des données de l'entreprise fictive)
- Développement des calculs en VBA 
- Tester par des données factices

## Sprint 1
- Apprendre le VBA : 
J'ai appris à automatiser de simples tâches en enregistrant une macro, modifier le code et créer un bouton d’exécution grace à ce [tuto](https://www.excel-pratique.com/fr/vba)
- Lister les dépenses technologiques des entreprises : 

***Dépenses récurrentes***
| Catégorie de Dépenses     | Exemples                                | Coûts Estimés (par mois/année) |
|----------------------------|-----------------------------------------|---------------------------------|
| Logiciels                  | Abonnements à des logiciels SaaS        | 100 € - 500 € par utilisateur et par an |
| Services Cloud             | Hébergement web, stockage en ligne      | 50 € - 200 € par mois           |
| Télécommunications        | Abonnements Internet, téléphonie fixe   | 100 € - 300 € par mois          |
| Sécurité Informatique     | Logiciels de sécurité, services de sauvegarde | 50 € - 200 € par mois         |
| Formation et Support      | Formation des employés, services de support technique | 100 € - 500 € par mois    |
| Services d'Assistance     | Abonnements à des services d'assistance technique | 20 € - 100 € par utilisateur et par mois |

***Dépenses non récurrentes***
| Catégorie de Dépenses     | Exemples                                | Coûts Estimés (ponctuels)     |
|----------------------------|-----------------------------------------|--------------------------------|
| Matériel Informatique      | Ordinateurs, serveurs, périphériques    | 500 € - 5000 € par équipement  |
| Logiciels                  | Licences de logiciels, développement d'applications | 1000 € - 10000 € par projet |
| Infrastructure de Réseau  | Câblage réseau, équipements réseau      | 1000 € - 5000 € par projet      |
| Développement de Logiciels| Développement d'applications personnalisées | 5000 € - 50000 € par projet |
| Équipements de Pointe      | Dispositifs IoT, équipements de réalité virtuelle/augmentée | 1000 € - 10000 € par équipement |
