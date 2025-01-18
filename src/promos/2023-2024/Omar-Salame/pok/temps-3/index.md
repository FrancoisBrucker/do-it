---
layout: layout/pok.njk

title: "Optimisation de la Gestion des Ressources Humaines (SIRH)"
authors:
  - Omar Salame

date: 2024-02-14

tags: 
  - "temps 3"

résumé: Etude de cas sur l'optimisation de l'organisation interne d'une entreprise
---

## Table des matières
1. [Introduction](#section-1)
2. [Sprint 1](#section-2)
3. [Etude préliminaire](#section-3)
4. [Questionnaires](#section-4)
5. [Résultats](#section-5)
6. [Sprint 2](#section-6)
7. [Processus optimisés](#section-7)
8. [Cahier de charge](#section-8)


## Introduction<a id="section-1"></a>
### Présentation de l'entreprise
Un leader technologique mondial, avec plus de 190 000 employés répartis dans 127 sites de production et 12 grands centres techniques à travers le monde. Avec une présence dans 46 pays, ils relèvent les défis les plus complexes de la mobilité grâce à leur expertise approfondie en matière de logiciels et d'intégration de systèmes, offrant des solutions pertinentes pour leurs clients.
### Problématique
L'entreprise vise à améliorer la gestion des ressources humaines, en se concentrant spécifiquement sur la gestion de la main-d'œuvre, qui compte 2500 employés par usine. L'entreprise souhaite transformer les processus actuels de surveillance des données, qui sont manuels et intensifs, et qui concernent le contrôle de la présence, la gestion des absences, l'échange d'informations entre employés et employeurs, ainsi que la fourniture de documents administratifs. Elle prévoit d'identifier un outil adapté à ses besoins, capable de réduire de manière significative la dépendance actuelle à l'égard des processus manuels utilisés pour générer des informations de prévision et de budget.
Le nouveau système de gestion des ressources humaines devrait permettre aux ressources de concentrer l'essentiel de leur temps et de leurs efforts sur l'analyse des modèles et des tendances des données, afin de fournir des analyses pertinentes et à forte valeur ajoutée. Cela sera réalisé en réduisant considérablement le temps et les efforts nécessaires pour les activités manuelles et intensives en main-d'œuvre, telles que la collecte et la consolidation des données nécessaires, ainsi que le remplissage des feuilles de calcul, qui représentent la majeure partie du temps dans le processus actuel.

## Sprint 1<a id="section-2"></a>
| Tâche                                    | Description                                                                                                                                              | Durée estimée |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| Étude préliminaire et consultation      | Obtenir des informations générales sur l’entreprise, mettre en contexte la problématique, et formaliser la vision et les ambitions. (DSI et DRH ou DOSI)            | 1h            |
| Préparation et conception du questionnaire | - Sélectionner le modèle d’évaluation de la maturité digitale et opérationnelle approprié. <br> - Identifier les questions nécessaires pour mieux comprendre les processus actuels de gestion des ressources humaines. <br> - Créer un questionnaire adapté à chaque profil impliqué dans les processus RH (employés, gestionnaires, DRH, etc.). <br>  |2h|
| Conduite des entretiens                 | - Présenter le questionnaire et clarifier les points si nécessaire. <br> - Recueillir les réponses des parties prenantes de manière exhaustive et structurée.        | 3h            |
| Modélisation et cartographie des processus | - Analyser les données recueillies lors des entretiens et à partir des questionnaires. <br> - Identifier les différentes étapes des processus et les interrelations entre elles. <br> - Documenter les flux de travail, les décisions prises et les responsabilités associées à chaque étape. <br> - Utiliser le logiciel Bizagi pour représenter graphiquement les processus actuels. | 2h |
| Analyse des forces et faiblesses des processus | - Identifier les faiblesses, les inefficacités et les points de friction dans les processus de gestion des ressources humaines. <br> - Évaluer le niveau de maturité des processus actuels en termes de gestion des ressources humaines. <br> - Identifier les risques potentiels associés aux processus actuels et aux pratiques de gestion des ressources humaines. | 3h |

Total estimé : 11 heures

## Étude préliminaire<a id="section-3"></a>
### Choix du modèle
**Deloitte Digital Maturity Model**
Mon choix s'est porté vers le modèle de Deloitte, qui me semble être le plus pertinent pour les raisons suivantes : 

<img src="ddm.webp" width="700" height="550">

**Résultat attendu : Situer le cas d'étude dans l'un de ces niveaux puis proposer des recommandations personnalisées.**

{% details "Niveaux Digital Maturity Deloitte" %}
- **Niveau de base/initial** : À ce stade, l'entreprise commence tout juste à adopter des technologies digitales. Les initiatives digitales sont souvent sporadiques et fragmentées, et il peut y avoir une résistance au changement de la part des employés.
- **Niveau émergent** : À ce stade, l'entreprise commence à développer une vision plus claire de sa transformation digitale. Les initiatives sont mieux coordonnées et il y a une prise de conscience accrue de l'importance du numérique pour rester compétitif sur le marché.
- **Niveau consolidé** : À ce stade, l'entreprise a établi une base solide en matière de technologies digitales. Les processus sont de plus en plus intégrés et optimisés, et il y a une adoption généralisée des technologies digitales à travers l'organisation.
- **Niveau stratégique** : À ce stade, l'entreprise utilise le numérique de manière stratégique pour stimuler l'innovation, créer de nouveaux modèles commerciaux et améliorer l'expérience client. Il y a une culture d'innovation et d'expérimentation au sein de l'organisation.
- **Niveau transformationnel** : À ce stade, l'entreprise a complètement intégré le numérique dans son ADN. Elle est capable d'anticiper les tendances du marché et d'innover de manière continue pour rester en tête de la concurrence.
{% enddetails %}

## Questionnaires<a id="section-4"></a>
Pour avoir ce type de solution,  je prévois de conduire des entretiens avec les parties prenantes de ce projet pour mieux comprendre les enjeux métier, leurs procédures et leur SIRH actuel.
Personnes concernées par le questionnaires : DRH , DSI , Shift Leader.

{% details "Questionnaire DSI" %}
### Présentation du département

- Pouvez-vous présenter la composition de votre département en termes de nombre de collaborateurs par rapport au nombre d'employés de l'entreprise ?
- Quelles sont les activités clés de votre service?

### Description de vos activités et du SI

- Pouvez-vous me décrire la structure de votre SIRH? Ses différentes composantes et fonctions? Est-il modulable?
- Y a-t-il des systèmes tiers intégrés à votre SIRH?
- Quels sont les départements qui ont des interactions directes avec le SIRH?
- Comment sont gérés les accès aux données au sein de votre système d'information?
- Dans quelle étape intervient-il votre département dans la gestion des ressources humaines?
- Quels sont les projets en cours ou prévus à court terme dans votre périmètre ?

### Evaluation métier / SI sur votre périmètre

- Vos besoins métier sont-ils couverts par le SIRH actuel ?
- Quelles sont les principales forces du SIRH actuel ?
- À votre avis, quelles sont les principales faiblesses du SIRH actuel ?
- Quelles nouvelles fonctionnalités ou caractéristiques pensez-vous qu'il faudrait incorporer dans le SIRH ?
- Quelle est l'importance accordée à la sécurité dans votre système d'information?
{% enddetails %}

{% details "Questionnaire DRH" %}
### Présentation du département

- Pouvez-vous présenter la composition de votre département RH en termes de nombre de collaborateurs par rapport au nombre d'employés de l'entreprise ?
- Quelles sont les activités clés de votre service des ressources humaines ?

### Description de vos activités et du SI

- Comment le processus de demande de documents est-il géré ?
- Quel est l'approche de gestion de l'absentéisme ?
- Comment est réalisée la prévision des besoins en personnel dans votre organisation ?
- Quels flux d’informations sont impliqués dans vos tâches quotidiennes et avec quels départements? Sont-ils automatisés ?
- Quelles sont les fonctionnalités du SIRH actuel liées à votre métier ?
- Comment les tâches et les problèmes sont-ils priorisés au sein de votre département ?
- Quels sont certains problèmes récurrents rencontrés dans vos processus RH ?
- Quelles tâches nécessitent un temps et des ressources excessifs ? Y a-t-il un potentiel d'automatisation ?
- Quel est le délai de traitement des demandes, réalisation des tâches et l'achèvement des processus ?

### Evaluation métier / SI sur votre périmètre

- Vos besoins métier sont-ils couverts par le SIRH actuel ?
- Quels aspects de votre travail actuel vous satisfont et quels sont ceux que vous pensez nécessiter des améliorations ?
- Quels indicateurs clés de performance (KPI) sont actuellement dérivés de votre SIRH, et quelles données sont nécessaires pour leur mise en œuvre ?
- Quelles sont les principales forces du SIRH actuel ?
- À votre avis, quelles sont les principales faiblesses du SIRH actuel ?
- Quelles nouvelles fonctionnalités ou caractéristiques pensez-vous qu'il faudrait incorporer dans le SIRH ?

{% enddetails %}

{% details "Questionnaire Team/Shift Leader" %}
### Présentation du Département

- Pouvez-vous décrire en quoi consiste votre activité en tant que shift leader ?
- Pourriez-vous décrire une journée typique au sein de votre service en tant que shift leader ?

### Description des Activités et Interaction avec le SI

- Comment le processus de demande de documents est-il géré ?
- Quel est l'approche de gestion de l'absentéisme ?
- Comment organisez-vous la planification des shifts et l’affectation des employés, et comment communiquez-vous ce plan au sein de votre équipe ?
- Quels flux d’informations sont impliqués dans vos tâches quotidiennes et avec quels départements ?
- Comment maintenez-vous la communication avec les employés dont vous êtes responsable ?
- Quelles sont les fonctionnalités du SIRH actuel liées à votre métier ?
- Quels sont certains problèmes récurrents rencontrés dans vos processus RH ?
- Quelles tâches nécessitent un temps et des ressources excessifs ? Y a-t-il un potentiel d'automatisation ?

### Evaluation métier / SI sur votre périmètre

- Vos besoins métier sont-ils couverts par le SIRH actuel ?
- Quels aspects de votre travail actuel vous satisfont et quels sont ceux que vous pensez nécessiter des améliorations ?
- Quels indicateurs clés de performance (KPI) sont actuellement dérivés de votre SIRH, et quelles données sont nécessaires pour leur mise en œuvre ?
- Quelles sont les principales forces du SIRH actuel ?
- À votre avis, quelles sont les principales faiblesses du SIRH actuel ?
- Quelles nouvelles fonctionnalités ou caractéristiques pensez-vous qu'il faudrait incorporer dans le SIRH ?
{% enddetails %}


## Résultats<a id="section-5"></a>

### Modélisation et cartographie des processus

{% details "Process 1: Gestion des documents administratifs " %}
<img src="process1.webp" width="700" height="550">
{% enddetails %}
{% details "Process 2: Gestion de l'envoie des documents" %}
<img src="process2.webp" width="700" height="550">
{% enddetails %}
{% details "Process 3: Gestion de l'absentéisme" %}
<img src="process3.webp" width="700" height="550">
{% enddetails %}

### Analyse SWOT des processus
<img src="swot.webp" width="700" height="550">

### Schéma du HRIS existant
<img src="hris.webp" width="700" height="550">

### Niveau de maturité
Cette organisation se situe dans le deuxième niveau du modèle Deloitte Digital Maturity, c'est-à-dire le niveau émergent. Ils ont déjà une notion de l'importance de la digitalisation de leurs activités et de ce que cela peut apporter en termes de productivité et d'efficacité. Cependant, ils sont toujours au premier stade en termes de technologie. Les processus sont majoritairement manuels et la consolidation des données se fait sur Excel sans aucune communication entre les systèmes et les départements.

## Sprint 2<a id="section-6"></a>
| Tâche                                | Durée estimée |
|--------------------------------------|---------------|
| Modélisation du nouveau processus optimisé| 2h            |
| Rédaction du cahier de charge       | 4h            |
| Schéma directeur des projets        | 2h            |
| Validation                           | 1h            |

## Processus optimisés<a id="section-7"></a>

{% details "Process 1: Gestion des documents administratifs " %}
<img src="process1up.webp" width="700" height="550">
{% enddetails %}
{% details "Process 2: Gestion de l'envoie des documents" %}
<img src="process2up.webp" width="700" height="550">
{% enddetails %}

## Cahier de charge<a id="section-8"></a>
Après avoir révisé les procédures et examiné les standards internationaux des SIRH spécifiques à l'industrie, j'ai pu identifier les [fonctionnalités](https://docs.google.com/spreadsheets/d/1Ddm2TmfpYh1n6c5mJks5NtY0I2bxd2JW/edit#gid=49217966) clés nécessaires pour développer une solution conforme aux standards de l'industrie en termes de sécurité, d'automatisation et de gestion des données. Ces fonctionnalités essentielles comprennent des systèmes robustes de sécurité des informations pour protéger contre les accès non autorisés et les fuites de données, des outils d'automatisation pour rationaliser les processus RH et réduire les erreurs manuelles, ainsi que des capacités avancées d'analyse de données pour soutenir la prise de décision. J'ai ensuite compilé ces exigences fonctionnelles et non fonctionnelles dans un fichier Excel pour une référence facile et une meilleure organisation du développement du système.
{% prerequis "**Liste de ressources**"%}
- [Des Normes internationales ISO pour de meilleurs processus RH](https://myrhline.com/type-article/cest-quoi-ce-truc-normes-internationales-de-gestion-des-rh/#:~:text=La%20norme%20internationale%20ISO%2030405,et%20recruter%20de%20nouveaux%20talents.)
- [CNIL: Publication du référentiel relatif à la gestion des ressources humaines](https://www.cnil.fr/fr/publication-du-referentiel-relatif-la-gestion-des-ressources-humaines)
- [ISO 30409](https://cdn.standards.iteh.ai/samples/64150/b8074452346d426b8e56e4790625ffa5/ISO-30409-2016.pdf)
- [Discussion ChatGPT](https://chat.openai.com/share/06ec0a48-d710-4cce-b555-e61835c4bb0d)
{% endprerequis %}
 Je tiens à souligner plusieurs aspects cruciaux pour garantir un système performant et convivial. Tout d'abord, il est essentiel de permettre à chaque employé d'accéder facilement au SIRH, que ce soit depuis un kiosque dans l'usine, un ordinateur personnel ou même un smartphone. L'idée, c'est de rendre l'accès aux informations RH simple et accessible. Je souligne aussi l'importance  de garantir la sécurité des données personnelles de ses employés. Pour ce faire, l'utilisation d'identifiants tiers et d'une double authentification est essentielle. Cela permettra de protéger efficacement les informations sensibles, assurant ainsi la confidentialité et l'intégrité des données de l'entreprise et de ses collaborateurs. En mettant en place ces mesures de sécurité robustes, nous nous assurons que seules les personnes autorisées puissent accéder aux données du SIRH, renforçant ainsi la confiance et la tranquillité d'esprit de chacun.

 En ce qui concerne la **gestion des demandes de documents RH**, il est important de faciliter le processus pour les employés. Pouvoir demander et recevoir facilement les documents nécessaires, que ce soit pour leur propre consultation ou pour des démarches administratives, simplifierait grandement les tâches quotidiennes. Cela permettrait une gestion plus pratique et rapide des demandes, bénéficiant à la fois aux employés et à l'efficacité globale de l'entreprise.

Quant à la **gestion de la présence**, il est crucial que toutes les informations soient claires et standardisées pour éviter toute confusion. Une intégration en temps réel des données de présence de tous les systèmes serait très bénéfique. Cela permettrait à chacun d'être bien informé en temps réel sur qui est présent et qui ne l'est pas, assurant ainsi une gestion transparente et efficace des emplois du temps.
{% note %}
L'objectif principal est de détecter les absences le plus tôt possible. Ce que je propose est de vérifier dès le début de la tournée du bus ou du ramassage si quelqu'un est absent. Dans cette optique, nous distribuerions des badges aux employés, qu'ils utiliseraient pour scanner à leur entrée dans le bus. De cette manière, si un employé ne scanne pas son badge, nous saurions qu'il sera absent. Cette approche offrirait une marge de manœuvre plus importante et davantage de temps pour planifier le remplacement de cette personne.
{% endnote %}
### Risques
L'implémentation d'une nouvelle solution de SIRH peut soulever des préoccupations légitimes au sein de l'équipe. Il est important de reconnaître les défis potentiels auxquels les employés pourraient être confrontés. Ces défis peuvent entraîner une perte de temps et d'efficacité au lieu de les améliorer, ce qui va à l'encontre de l'objectif initial de la mise en œuvre.

L'un des risques majeurs est la **résistance au changement** de la part des employés. L'introduction d'un nouveau système peut perturber les habitudes de travail établies et susciter des inquiétudes quant à la nécessité de s'adapter à de nouvelles méthodes et procédures. Les employés peuvent craindre d'être **micro-gérés** ou **contrôlés de manière excessive**, ce qui peut entraîner une baisse de moral et une diminution de la motivation. Cette opposition au changement peut entraîner une adhésion limitée au nouveau système et, par conséquent, compromettre son efficacité globale.

De plus, il est crucial de reconnaître que tous les employés peuvent ne pas être à l'aise avec les technologies ou les **interfaces informatiques complexes**. Si la nouvelle solution de SIRH n'est pas conviviale ou si elle nécessite une courbe d'apprentissage importante, certains employés peuvent rencontrer des difficultés à l'utiliser correctement, ce qui entraînera des retards et des inefficacités supplémentaires.

Pour surmonter ces défis, il est essentiel d'adopter une **approche proactive** et inclusive. Il est nécessaire d'**impliquer les employés** dès le début du processus de mise en œuvre, en leur fournissant une formation adéquate et en les consultant sur leurs besoins et préoccupations. De plus, il est important de communiquer de manière transparente sur les raisons du changement et les avantages attendus pour les employés et l'entreprise dans son ensemble. 

[Drive de mon travail](https://drive.google.com/drive/folders/1UxRs99Mpo37_-gLLmpO96G_sKGVlFZNP?usp=drive_link)