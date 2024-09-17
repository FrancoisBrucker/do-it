---
layout: layout/pok.njk

title: "POK 1 - VBA, fais-le pour moi"
authors:
  - Victor Pawlaczyk

date: 2024-09-01

tags:
  - "temps 1"
  - "Vert"
  - "VBA"

résumé: Au travail, certains collègues doivent effectuer des tâches qui me semblent plutôt basiques et surtout très répétitives sur Excel. Le but de ce POK est donc d’essayer d’utiliser les VBA pour automatiser certaines de ces tâches.
---

{% prerequis %}

Connaissances de base en VBA

{% endprerequis %}
{% lien %}

Les lien utiles pour la compréhension de celui-ci.

{% endlien %}

## Tâches

### Sprints

But final.

#### Sprint 1

Liste des taches que l'on pense faire. On coche si la tache est réalisée. A la fin du sprint on fait une petite étude post-mortem pour voir ce qui s'est passé et les ajustement à faire pour le prochain sprint, pok.

- [x] Répertorier des tâches répétitives que mes collègues aimeraient voir automatisées
- [x] Sonder des connaissances et/ou internet pour avoir des retours d'expériences sur ce genre de projets
- [x] De l'idéation à la conception : comment techniquement j'imagine que les demandes identifiées puissent être automatisées ?
- [x] Choisir un premier exemple concret d'automatisation, faire une maquette
- [x] Test de la maquette, réaction de mes collègues/retour d'expérience
- [ ] Codage du programme VBA à partir de la maquette, et des retours reçus
- [ ] Test de ce programme

#### Sprint 2

- [ ] Continuer le codage du programme du Sprint 1
- [ ] Test de ce programme + correction des bugs
- [ ] identification de ses faiblesses ou des améliorations possibles
- [ ] Correction des faiblesses, amélioration du programme
- [ ] Codage d'un autre programme qui réponde à une autre des demandes identifiées
- [ ] Test de ce programme + correction des bugs
- [ ] identification de ses faiblesses ou des améliorations possibles
- [ ] Correction des faiblesses, amélioration du programme

Liste des taches que l'on pense faire. On coche si la tache est réalisée. A la fin du sprint on fait une petite étude post-mortem pour voir ce qui s'est passé et les ajustement à faire pour le prochain sprint, pok.

### Horodatage

Toutes les séances et le nombre d'heure que l'on y a passé.

| Date | Heures passées | Indications |
| -------- | -------- |-------- |
| Jeudi 05/09  | 1H  | Echanges avec Corinne, identification de ses besoins |
| Vendredi 06/09  | 1H  | Retours d'expérience |
| lundi 09/09  | 3H  | Recherche de moyens techniques de répondre à la demande + élaboration de la maquette |
| Mercredi 11/09  | 1H  | Présentation de la maquette |
| Lundi 16/09  | 2H  | Analyse des retours sur la maquette + codage VBA |
| Lundi 16/09  | 30 min  | Analyse du Sprint + réflexion sur le prochain Sprint |
| Lundi 16/09 | 1H30 | Rédaction livrable |

## Premier Sprint

### Identification des tâches à automatiser

La première étape consiste à échanger avec mes collègues sur leur utilisation quotidienne d'Excel et leurs tâches récurrentes pour identifier les tâches qui pourraient être automatisées ou simplifiées avec des macros. C'est avec Corinne que j'ai identifié différentes manipulations à automatiser.

En résultat de ces échanges et réflexions, voici les objectifs possibles d'automatisation que nous avons identifiés :

- La saisie de devis sur Excel à partir des extractions faites d'un progiciel interne
- La vérification des documents administratifs du personnel présent sur le chantier
- Le suivi des demandes de badge d'accès au site
- les demandes de badges hebdomadaires pour les véhicules.

### Retours d'expériences de projets similaires

Ensuite j'ai recherché dans mon entourage mais aussi sur internet quelques retours d'expérience sur ce type de projets avec du VBA. Les principaux points d'attention qui résultent de ces retours d'expérience sont les suivants :

- Il faut fait attention à l'utilisateur final de l'outil que l'on met au point au cours du projet. Souvent, l'utilisateur final de l'outil n'est pas forcément à l'aise avec l'informatique et ce genre de programmes et de macros peuvent les perdre plus que les aider réellement.
- Parfois, le codage de la macro cause plus de prise de tête qu'il n'apporte de gain réel une fois au point.
- Il ne faut pas négliger la partie "design thinking". Si la macro n'est pas faite pour n'être utilisée qu'à titre personnel, il faut être vigilant à ne pas partir trop loin tête baissée dans le codage sans vérifier régulièrement que le résultat corresponde réellement aux attentes de(s) l'utilisateur(s) visé(s).

### Ma Phase d'idéation

Pour le sujet de saisie des devis, j'ai pensé à coder une macro de mise en forme des données. C’est la solution qui me paraît intéressante à creuser. En effet, il est possible d’extraire les données depuis le logiciel où arrivent les devis, les bons de commande et les factures. On peut facilement faire un copier-coller depuis cette extraction vers un excel. Le souci c’est que toutes les informations récupérées ne sont pas forcément pertinentes, il y a des colonnes en trop, d’autres pas dans le bon ordre, etc. C’est une perte de temps considérable de remettre à chaque fois ces données copiées dans une mise en forme exploitable pour l’utilisation qu’on veut avoir de ce tableur. Une première piste à creuser est donc une macro qui automatise cette mise en forme des tableaux à partir des extractions du logiciel.

Pour la vérification des documents administratifs, on a déjà mis en place un tableau dans lequel on renseigne la date d’expiration du document valide que l’on a plutôt que simplement indiquer s’il est « ok » ou non à la saisie du dossier. Aujourd’hui, ma collègue doit régulièrement vérifier ligne à ligne si les documents que l’on a sont toujours valides. En fonction du nombre d’ouvriers présents, cela peut être rapide comme très long. Il serait intéressant de mettre en place un bouton qui lance une macro de « vérification des documents à jours » qui renverrai à la fin une message box indiquant que toutes les pièces d’identité sont valides ou alors celles qui sont périmées le cas échéant (idem pour les visites médicales, etc). Cela rendrait la vérification beaucoup plus efficace. Il serait aussi intéressant de lister les données manquantes dans le tableau.

Pour les demandes de badge, on renseigne déjà la date à laquelle la demande a été faite, puis quand elle est acceptée on le renseigne aussi. Encore une fois, il serait sympa qu’un bouton associé à une macro recherche seul parmi tout le tableau les demandes qui ont été envoyées mais pas encore acceptées, pour savoir quels cas posent « problème » et faciliter les relances au bureau des badges.

### Le Maquettage

Pour commencer, avant de me lancer tête baissée dans le codage en VBA de programmes hyper compliqués et complets, il m’a semblé important de tester l’adhésion du public visé à la solution envisagée. J’ai donc en étape intermédiaire utilisé des fonctions excel que je connaissais un peu mieux pour faire des premiers tests de mes idées à ma collègue Corinne. Pour ce début j’ai commencé à travailler sur le suivi des documents administratifs. J’ai amélioré un peu le tableau existant pour commencer à y automatiser certaines vérifications, notamment la validité des pièces d’identité. J’ai commencé par ajouter une colonne de test qui compare la date de validité du document à la date du jour. Cette colonne renvoie vrai ou faux. En ajoutant une mise en forme conditionnelle verte ou rouge, j’ai pu voir que Corinne pouvait vérifier beaucoup plus rapidement si tout était encore valide. Mais elle doit encore parcourir elle-même tout le tableau.

Voici le retour d'expérience obtenu de cette maquette :

- Corinne m’a suggéré d’ajouter un intermédiaire « se périme bientôt » en plus des catégories "valide" et "périmé", comme ça elle peut mettre en garde les ouvriers concernés et leur boîte d’intérim.
- « Oh, tu pourrais me faire ça aussi avec les visites médicales ? »
- « Tu crois que ça pourrait mettre à jour les dates de contrat des intérims tout seul aussi » (-> Nouveau défi !)

### Analyse Post Mortem du Sprint

Je n'ai pas réalisé l'intégralité de ce que j'avais initialement prévu pour le premier sprint étant donné qu'à ce stade, je n'ai pas encore réussi à coder une solution viable en VBA pour répondre à un des problèmes efficacement. Le codage est en cours. Cela constituera le coeur du second sprint qui était déjà prévu de la sorte.

## Second Sprint
