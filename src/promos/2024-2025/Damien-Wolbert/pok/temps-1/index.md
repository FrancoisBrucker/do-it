---
layout: layout/pok.njk

title: "Outil de suivi de la montée en compétences individuelle sur Google Drive"
authors:
  - Damien WOLBERT

date: 2024-09-06

tags:
  - "temps 1"

résumé: Ce POK vise à mettre en place la maquette d'un outil opérationnel de suivi de la compétence individuelle au sein d'une organisation simple, en utilisant les différentes fonctionnalités et outils de Google Drive.
---

{% prerequis %}
**Niveau :** Basique
**Pré-requis:**
- Connaissance de base de Google AppScript, de Google Sheet et d'un Google Drive. (Approdondi en MON)
- Connaissance de base des enjeux de la compétence individuelle en entreprise. (Approfondi en première phase du projet à partir des connaissances déjà accumulées en stage et alterance)

{% endprerequis %}
{% lien %}

{% endlien %}

## Contexte

J'ai souvent constaté que le sujet du suivi des compétences des membres d'une orgnanisation est à la fois critique et délicat.
| Contexte | Structure | Observations |
|----------|-----------|--------------|
| Responsable RSE et chargé de mission SI | KSI Centrale Marseille | Les compétences ne sont pas clairement identifiées ou suivies dans chaque pôle. Ce qui rend plus diffcile la formation et donc l'activité de la structure.|
| Stage employé polyvalent | Mairie de Lunel-Viel (34) | Les managers ne connaissent pas les compétences nécessaire ou détenue par les personnes à leur charge. Ils n'ont donc pas de visibilité sur toutes leurs activités ou les activités qu'ils pourraient leur sous-traiter. |
| Alternant ingénieur électricien | Service support électricité, Engie Renouvelables | Le manager ne connait pas les réelles compétences de ses agents ce qui le contraint à les laisser gérer et chosisirs leurs missions et projets. Cela déséquilibre complètement le service (travail sur le même sujet en parralèle) et bloque toute possibilité de pérennité de la compétence au sein du service (aucun pré-requis ou plan de formation) |

Je trouve donc intéressant de me plonger dans ces problèmatiques afin d'analyser d'où proviennent les points de blocages des structures dans lesquelles j'ai évolué.

D'autre part, je n'ai jamais pû approfondir l'utilisation de Google Appscript et de toutes possibilités offertes par Google Drive. Je pourrai donc réaliser un certain nombre de parallèle entre ce languages de programmation et mes connaissance de VBA (Visual Basic fo Application) sur Excel.

## Cadrage

### Objectifs principaux

1. Identifier les enjeux du monitoring des compétences.
2. Identifier les fonctionnalités indispensables à l'implémentation d'un tel outil.
3. Identifier un format et une interface adaptés au plus grand nombre d'utilisateurs en utilisant des fonctionnalités simples de Google AppScript, Google Sheet, Google formular et Google Drive.
4. Identifier une architecture robuste sur Google Drive permettant d'ajouter des foncitonnalités au fur et à mesure.
5. Livrer une maquette fonctionnelle et testée à la fin des 20 heures allouées au POK.

### Monitoring du projet

Le suivi du projet a été réalisé sur un outil personnel développé spécialement pour le suivi des POK et MON. Le contenu est reporté ci-dessous.

#### Sprints back-logs

L'objectif final de ce POK est de fournir un dossier Google Drive contenant des outils automatisés de suivi de la compétence des membres d'une entreprise type à déterminée.

##### Sprint 1

**To-do**

- [x] Recueillir des informations sur le monitoring et le management de la compétence dans la littérature.
- [ ] Recueillir les besoins de différents acteurs responsables du suivi de la montée en compétence des membres de leur organisation.
  - [x] Au sein de KSI Centrale Marseille.
  - [ ] Au sein de différents service d'Engie Renouvelables.
  - [x] Au sein d'une organisation du secteur publique (TBD)
  - [x] Au sein d'une structure de formation.
- [ ] Analsyer les données recueillies à l'étape 2 et réaliser le CCTP de l'outil.
- [ ] Réaliser l'architecture fonctionnelle de l'outil.
- [ ] Préparer et tester les templates utilisés sur Google Sheet et/ou Google Doc et/ou Google formular.

**Horodatage**

| Date | Heures passées | Indications | Niveau d'efficacité |
| -------- | -------- |-------- | -------- |
| 11/09/2024 | 0.7h | Cadrage | Intermédiaire |
| 11/09/2024 | 2h | Recherche bibliographique | Elevé |
| 12/09/2024 | 1h | Création d'un questionnaire pour reccueil du besoin | Elevé |
| 13/09/2024 | 0.5h | Tentative de communication avec le responsable du référentiel centralien à Centrale | Elevé |
| 16/09/2024 | 1h | Finalisation du questionnaire + envoie | Elevé |
| 16/09/2024 | 3.7h | Recherche bibliographique | Elevé |

##### Sprint 2

**To-do**


**Horodatage**



## I. Les enjeux du suivi de la compétence individuelle

### I.1. Définitions et caractérisation

Dans son ouvrage *INGENIERIE DE FORMATION : Intégrez les nouveaux modes de formation dans votre pédagogie*, T. ARDOUIN explique que la définition même du mot compétence crée le débat. Il en donne la définition suivante à la page 119 :

{% info %}
**Déf. 1 :** La compétence est la mise en oeuvre de capacités en situation professionnelle qii permettente d'exercer convenablement une fonction ou une activité." [4].
{% endinfo %}

D'autre part, Cécile DEJOUX dans son ouvrage *Gestion des compétences et GPEC* sépare dès la défintion, compétences individuelles, collectives, organisationelles et territoriales. Dans ce contexte nous noterons la défintion suivante :

{% info %}
**Déf. 2 :** La compétence individuelle est la combianaison d'un ensemble de connaissances, savoir-faire et d'aptitudes qui dans un contexte donné, permettent d'aboutir à un niveau de performance attendu et validé.
{% endinfo %}

Lors de l'étude du besoin détaillée plus bas, j'ai demandé aux personnes intérrogées : Comment définissez vous "compétence individuelle" ? Il est intéressant de noter la pluralité des réponses et des points de vus.

{% info %}
**Déf. 3 : "** Savoir faire acquis par l'apprentissage ou la pratique.
**Déf. 4 : "** Aptitude à une tâche d'un individu.
{% endinfo %}

Je trouve la définition De C. DEJOUX intéressante car elle montre la diversité des compétences dans leur typologie. Dans son ouvrage [4] elle caractérise la compétence individuelle par 6 points :
1. Savoir-agir : Prend son sens par rapport à une action.
2. Finalisée : Prend son sens par rapport à un objectif et un résultat. On peut les mesurer et la normer.
3. Combinatoire : Se divise et sous-devise en unités.
4. Contingente : Dépends des outils et des conditions disponibles lors de sa mise en place.
5. Dynamique : Evolue continuellement.
6. Reconnue collectivement : Reconnue par un statut, une valeur financière...

D'autre part, elle mets en avant la dépendance de la compétence au contexte, au lieu, à la structure. Comme une compétence est reconnue collectivement, sa défintion et sa valeur varient en fonction du temps et de l'espace.

{% faire %}
Il faudra donc permettre à l'utilisateur de garder une grande felxibilité dans la façon de définir les compétences.
{% endfaire %}

Elle définit alors 4 catégories :
1. Les savoirs : Connaissances théotiques de bases, souvent associés à des diplomes ou des certificats. **ATTENTION : Je trouve que cette limitation aux diplômes dépend de la culture du pays et de l'organisation que l'on considère.**
2. Savoirs-faire : Aptitudes pratiques, capacité à ma maitriser quelque chose, à rendre le savoir opérationnel.
3. Savoir être : Aptitude sociale, innée ou acquise ; compétence comportementale interpersonnelle.
4. Compétences émotionnelles : Conscience et maitrise de soi et de ses relations avec les autres. Capacité à percevoir les émotions, les exprimer, les intégrer dans un processus de pensée, de compréhension, de raisonnement.

{% faire %}
Il faudra permettre à l'utilisateur de classer les types de compétences tout en fournissant un guide de classification.
{% endfaire %}

Cette dernière classification ne permet cependant pas à un manager de prioriser facilement une compétence au profit d'une autre (pour le recrutement ou la formation interne par exemple). On s'aperçoit notamment quand la caractérisation de C. DEJOUX, deux autres échelles sont à définir :

** Une échelle d'acquisition, de maitrise (caractéristique n°2):**
Au delè d'une échelle d'acquisition de la compétence, quantitative ou qualitative, il peut être intéressant de considérer le niveau d'autonomie d'un individu quant à la mise en application de cette compétence. Dans son ouvrage, T. ARDOUIN définit en page 120, 3 niveaux :
- A : Assiste et applique - Reproduction d'activité envisagées et organisées par d'autres.
- B : Intervient et produit - Production de donnée ou de modes de travail.
- C : Anime et conçoit - Réalisation de mode de travail et de donnée avec la responsabilité d'animé débats et groupes de travail.

{% faire %}
Il pourra être pertinent de mettre en place une échelle d'autonomie face à la tâche.
{% endfaire %}

** Une échelle de reconnaissance (caractéristique n°3) :**
Dans un article *Compétences individuelles et collectives" [3] du ministère de la transition écologique et de la cohésion des territoires, nous pouvons trouver des ressources présentant la compétence individuelle comme critique pour une organisation. Ainsi, on peut les classer les compétences à la fois par raport à son utilité immédiates mais aussi par rapport à son utilité stratégique, à moyene et long terme. 

{% faire %}
Il faudra permettre à l'utilisateur de définir des échelles d'importance actuelles et stratégiques.
{% endfaire %}

### I.2. Notions et outils à considérer

Mes recherches bibliographiques indiquent que certains outils sont a priori indispensable au suivi correcte de la compétence individuelle.

#### Référentiel métier et référentiel de compétence

D'après l'ouvrage *INGENIERIE DE FORMATION : Intégrez les nouveaux modes de formation dans votre pédagogie*, des outils importants du suivi de la compétence sont le référentiel métier et le référentiel de compétence. Le second découlant du premier ce qui donne parfois lieu à l'élaborationd 'un référentiel de compétence-métier.

{% details "Référentiel métier" %}
**Référentiel métier :** Description d'un poste tel qu'il est occupé et tel qu'il devrait être occupé d'après la vision stratégique de l'entreprise. 
Il définit notamment 4 types d'éléments :
- Missions : Finalité de l'emploi, indique le servie rendu à l’entreprise. Objectif de l’emploi par rapport à l’unité (équipe, service, etc…) dont il fait partie.
- Fonctions : Combinaison d’activités par thématique ou unité logique. Ex : Suivi des intervenants pour le responsable activité commerciale de KSI Centrale Marseille.
- Activités : Ce que doit faire la personne, exprimé sous forme de verbe d’action. Regroupe les tâches de même type.
- Tâches : Opérations élémentaires à effectuer à son poste de travail.
{% enddetails %}
{% details "Référentiel de compétences" %}
**Référentiel de compétence :** Déclinaison du référentiel métier en élements observables en fonction d'une méthode définie.
La méthode de définition des compétences est intrinsèque à la structure et à son activité.
{% enddetails %}

{% info %}
Le cahier des charges fonctionnel devra détailler et justifier une méthdologie de réalisation des référentiels métier chaque poste **ET** permettre une armonisation entre uex.
{% endinfo %}


#### Plan de développement individuel (PDI)

TBD

## II. Besoin fonctionnel

### II.1. Présupposés du besoin

La recherche bibliographique que j'ai réalisé m'a amené identifier plusieurs types de besoins : Esthétisme & accès et Fonctions.

#### A. Besoin esthétiques et accessibilité

| Id | Nom | Description |
|----|-----|-------------|
|**A.1.**| **Accessibilité administrateur** | **Informations visuelles, architecture simple, outil facilement pris en main.**|
|**A.2.**|**Accessibilité collaborateurs**| **Accès facile, présentation rapide des informations importantes.**|

#### B. Besoin fonctionnel

| Id | Nom | Description |
|----|-----|-------------|
|**B.1.** | **Besoin administrateur** | |
|B.1.1.| Référentiel métier et référentiel compétence | Pouvoir définir et modifier facilement le référentiel de compétences-métier de chaque collaborateur en armonisant la méthode de défintion des compétences. |
|B.1.2.| Suivi individuel | Visualiser les compétences de chacun des collaborateurs sur un fichier dédié en indiquant des niveaux d'évaluation pertinent et des objectifs temporels d'évolution |
|B.1.3.|Altertes||
|*B.1.3.1*|*Assurer un suivi régulier*|*Alerter les adminstrateur lorsque le suivi d'un collaborateur n'a pas été réalisé depuis longtemps.*|
|*B.1.3.2*|*Suivi des objectifs temporel*|*Alerter les adminstrateurs lorsque les échéances fixés sont imminentes.*|
|B.1.3.|Plan de développement individuel|Permettre la mise en place d'un plan de développement individuel pour chaque collaborateur|
|B.1.4.|Dashboard|Fournir un tableau de suivi général des services présentant les informations pertinentes au suivi régulier|
|**B.2.**| **Besoin collaborateur**| |
|B.2.1.|Consultation|
|*B.2.1.1.*|*Consultation du référentiel métier*|*Possibilité de consulter son référentiel de compétence avec suffisamment d'information et de clareté, sans pouvoir le modifier directement*|
|*B.2.1.2.*|*Consultation des niveaux de compétences*|*Possibilité de consulter l'évaluation du niveau de chacune de ses compétences ainsi que les échéances correspondantes, sans pourvoir la modifier directement.*|
|*B.2.1.3.*|*Consultation du plan de developpement individuel*|*Possibilité de consulter sont plan de développement individuel.*|
|B.2.2.1.|Demandes|
|*B.2.1.1.*|*Consultation du référentiel métier*|*Pouvoir réaliser une demande de formation*|
|*B.2.1.2.*|*Consultation du référentiel métier*|*Pouvoir réaliser une demande de modification de son référentiel de compétence-métier.*|
|*B.2.1.3.*|*Consultation du référentiel métier*|*Pouvoir réaliser une demande de son plan de développement individuel.*|


### II.2. Etude du besoin auprès d'usagers potentiels

Afin de réaliser un outil adaptable à plusieurs organisations et de hiérarchiser les fonctionnalités par importance, il a été necessaire de réaliser une étude sur le terrain. Par soucis de temps, je me suis orienté vers un format de formulaire en ligne. L'étude étant toujours en cours, les stastiques concernant la provenance des réponses ne sont pas présentées.

#### Questionnaire

{% details "Définition de compétence individuelle"%}
**Réponses**
{% enddetails %}

{% details "La compétence est validée par une certification ?"%}
{% details "Réponse attendue"%}
*Oui*
{% enddetails %}
{% details "Réponse réelle"%}
{% enddetails %}
{% enddetails %}

{% details "La compétence est validée par un diplôme ?"%}
{% details "Réponse attendue"%}
*Oui*
{% enddetails %}
{% details "Réponse réelle"%}
{% enddetails %}
{% enddetails %}

{% details "La compétence est validée par la recommandation d'un membre de notre réseau ?"%}
{% details "Réponse attendue"%}
*Non*
{% enddetails %}
{% details "Réponse réelle"%}
{% enddetails %}
{% enddetails %}

{% details "La compétence est validée par l'expérience professionnelle ?"%}
{% details "Réponse attendue"%}
*Oui*
{% enddetails %}
{% details "Réponse réelle"%}
{% enddetails %}
{% enddetails %}

{% details "La compétence est validée par un titre ?"%}
{% details "Réponse attendue"%}
*Non*
{% enddetails %}
{% details "Réponse réelle"%}
{% enddetails %}
{% enddetails %}

{% details "Mode de suvi ?"%}
{% details "Réponse attendue"%}
*Essentiellement par tableur excel et entretiens annuels*
{% enddetails %}
{% details "Réponse réelle"%}
{% enddetails %}
{% enddetails %}

{% details "Utilisation de plans de développement individuels ?"%}
{% details "Réponse attendue"%}
*Essentiellement non*
{% enddetails %}
{% details "Réponse réelle"%}
{% enddetails %}
{% enddetails %}

{% details "Si oui, à quelle fréquence le suivi est-il réalisé ?"%}
{% details "Réponse attendue"%}
*Suivi semestriel*
{% enddetails %}
{% details "Réponse réelle"%}
{% enddetails %}
{% enddetails %}

{% details "Utilisation d'un référentiel de compétence ?"%}
{% details "Réponse attendue"%}
*Essentiellement non*
{% enddetails %}
{% details "Réponse réelle"%}
{% enddetails %}
{% enddetails %}

{% details "Utilité d'un dashboard ?"%}
{% details "Réponse attendue"%}
*Indispensable (5/5)*
{% enddetails %}
{% details "Réponse réelle"%}
{% enddetails %}
{% enddetails %}

{% details "Fonctionnalité de création d'un PDI ?"%}
{% details "Réponse attendue"%}
*3/5*
{% enddetails %}
{% details "Réponse réelle"%}
{% enddetails %}
{% enddetails %}

{% details "Fonctionnalité de création d'un référentiel de compétence ?"%}
{% details "Réponse attendue"%}
*5/5*
{% enddetails %}
{% details "Réponse réelle"%}
{% enddetails %}
{% enddetails %}

{% details "Fonctionnalité d'altertes ?"%}
{% details "Réponse attendue"%}
*2/5*
{% enddetails %}
{% details "Réponse réelle"%}
{% enddetails %}
{% enddetails %}

{% details "Accès des collaborateur à leur suivi ?"%}
{% details "Réponse attendue"%}
*4/5*
{% enddetails %}
{% details "Réponse réelle"%}
{% enddetails %}
{% enddetails %}

### II.3. Formalisation du besoin fonctionnel

#### Fonctionnalités de base



#### Fonctionnalités souhaitables


#### Fonctionnalités additionnelles




## Bibliographie

[1] **DEJOUX, Cécile.** *Gestion des compétences et GPEC*, 2ème édition, DUNOD, 2013, Les topos

[2] **QUINN James Brian, ANDERSON Phili & FINKELSTEIN Sydney.** *La gestion du capital intellectuel : Comment tirer le meilleur parti des meilleurs*, Editions d'Organisation, 1996.

[3] CEDIP, Secrétariat Général-DRH-. « Compétences individuelles et collectives ». *Secrétariat Général - DRH - CEDIP*, 2 août 2022, https://www.cedip.developpement-durable.gouv.fr/competences-individuelles-et-collectives-a2141.html.

[4] **ARDOUIN, Thierry** *INGENIERIE DE FORMATION : Intégrez les nouveaux modes de formation dans votre pédagogie*, 5ème édition, 2017, DUNOD, Collection formation.

## REX