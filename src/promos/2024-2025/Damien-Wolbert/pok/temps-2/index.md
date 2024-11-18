---
layout: layout/pok.njk

title: "Modélisation d'un parc solaire sur Excel"
authors:
  - Damien WOLBERT

date: 1971-01-01

tags:
  - "temps 2"

résumé: Afin de pouvoir modéliser facilement un parc solaire avec un logiciel connu et utilisé par tous (Excel), ce POK me permettra de mettre en pratique mes connaissances en VBA et de mettre en place un outil permettant l'estimation des quantitatifs de câbles nécessaire la construction d'un parc solaire.
---

{% prerequis %}

- Programmation en VBA.
- Connaissance de la structure générale d'un parc solaire.

{% endprerequis %}
{% lien %}

Les lien utiles pour la compréhension de celui-ci.

{% endlien %}

Quelques phrases permettant de connaître, sans jargon ni blabla, le contenu de ce POK. On oubliera pas de donner :

- le niveau et les prérequis nécessaires en utilisant la balise [`prerequis`](/cs/contribuer-au-site/#prerequis)
- les autres POK & MON en rapport en utilisant la balise [`lien`](/cs/contribuer-au-site/#lien)

## Cadrage

### Objectifs principaux

1. Réussir à modéliser de manière graphique et visuelle un parc photovoltaïque.
2. Mettre en place un parcours utilisateur simple et agréable.
3. Ajuster le niveau de précision des estimations et outils au temps alloué au projet.

### Monitoring du projet

Le suivi du projet a été réalisé sur un outil personnel développé spécialement pour le suivi des POK et MON. Le contenu est reporté ci-dessous.

#### Back-log
##### Sprint 1

- [x] Réaliser le cadrage du projet
- [x] Sprint backlog 1
- [x] Brainstorming général
- [ ] Lister les fonctionnalités principales du système
- [ ] Parcours utilisateur rapide
- [ ] Définir les interfaces entre le système et l'utilisateur
- [ ] Lister les données d'entrées
- [ ] Trame des templates de chacune des interfaces
- [ ] Trame du template des données de sortie
- [ ] Mise au propre des templates des données d'entrée
- [ ] Mise au propre des templates des données de sortie
- [ ] Rédaction des fonctions permettant la création des templates d'inputs
- [ ] Rédiger le sprintbacklog 1 sur le site do-it
- [ ] Rédiger le CR du sprint 1 sur le site Do-it

| Date | Heures passées | Indications | Niveau d'efficacité |
| -------- | -------- | -------- | -------- |
***Total du sprint :***

##### Sprint 2

- [ ] Rédaction des fonctions informatiques permettant le calcul des distances sur la grille
- [ ] Lister les fonctions informatiques a priori nécessaires

| Date | Heures passées | Indications | Niveau d'efficacité |
| -------- | -------- |-------- | -------- |

***Total du sprint 2 :***
{% faire %}
**TOTAL POK 2 :**
{% endfaire %}

## Sprint 1

### Vocabulaire et fonctionnement d'un parc photovoltaïque

Afin de comprendre la suite de cet article, il est nécessaire de s'intier au monde du photovoltaïque ainsi qu'à son vocabulaire souvent anglophone.

{% details "Constitution générale d'un parc photovoltaïque" %}

{% enddetails %}


### Définition du cahier des charges

La rédaction du cahier des charges a été réalisée sur mon lieu d'apprentissage au côtés d'ingénieurs électriciens et civils.
{% note %}
Les limitations de VBA et Excel ont pausé un certain nombre de problèmes, notamment l'impossibilité de répondre à tous les besoins fromulés par les équipes de manière simple.
{% endnote %}

**Fonctionnalités principales**  
1. Positionner les éléments principaux du parcs de manière graphique :
   1. Stands
   2. String combiner boxes (SCB)
   3. Inverter transformer station (ITS)
   4. Tranchées par typologie
2. Positionner et caractériser les différentes strings
   1. Affecter les strings aux différentes SCB
   2. Méthode de racordement des strings : type de câble (section du conducteur), type de raccordement (aérien ou enterré)
3. Extraire les données du design créé de manière graphique sous forme d'une base de données exploitable.
{% note %}
J'ai préféré réaliser cette étude des fonctonctionnalités lors de moments informels afin d'éviter que les ingénieurs interrogés ne proposent trop de fonctionnalités et sortent du cadre de l'exercice.
{% endnote %}

**Données d'entrée**  
*Données dimensionnantes :*
- Inter-rangées : espace séparant les rangés sur dans leur longueur.
- Inter-stand : espace séparant les rangés dans leur largeur.
- Largeur des voies d'accès.
- Dimension des tranchées par typologie : tranchées pour câbles DC petite section, tranchées pour câbles DC grosse section.
- Dimensions des stands.
- Nombre de strings par stands.
- Nombre maximum de strings par SCB.

*Données de de designs :*
- Affectation des strings aux SCB.
- Positionnement des routes d'accès.
- Positionnement des tranchées.
- Positionnement des remontées de câble.

**Livrables fournis par l'outil :**  
1. Tableau complet permettant d'extraire les données de dimensionnement.
2. Carnet de câble.

### Parcours utilisateur





## Sprint 2
