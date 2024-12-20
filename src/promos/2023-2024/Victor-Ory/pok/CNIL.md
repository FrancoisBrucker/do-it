---
layout: layout/pok.njk

title: "Ne pas devenir C nil avec la RGPD"
authors:
  - ORY Victor

date: 2024-09-19

tags:
  - 'temps 2'
  - 'Protection des données'
  - 'RGPD'
  - 'Intermédiaire'

---

{%details "Les ressources"%}

- [AIPD](https://www.cnil.fr/fr/RGPD-analyse-impact-protection-des-donnees-aipd)
- [RGPD conformité](https://www.cnil.fr/fr/me-mettre-en-conformite)

{%enddetails%}

## Objectifs

Ci-dessous sont énoncés les objectifs que je me suis fixés, notés en termes de difficulté sur une échelle de trois étoiles :

- Apprendre la méthode pour faire un [AIPD](https://www.cnil.fr/fr/RGPD-analyse-impact-protection-des-donnees-aipd); ★★☆☆☆
- Réaliser une [AIPD](https://www.cnil.fr/fr/RGPD-analyse-impact-protection-des-donnees-aipd)★★★★☆

*★★★☆☆* = Difficulté

## Première étape : Comprendre la méthode :

### le 25/11 :

- [Approfondir ses connaissances sur l'AIPD](https://www.cnil.fr/fr/ce-quil-faut-savoir-sur-lanalyse-dimpact-relative-la-protection-des-donnees-aipd)
  
Feedback : Excellent article introductif
Résumé des 3 étapes d'une AIPD :

1. Description détaillée des procédés et traitements utilisés.
2. Évaluation juridique, couvrant la proportionnalité, la nécessité, la finalité, les données et durées de conservation, l'information et les droits des personnes, etc.
3. Étude technique, évaluant la confidentialité et l'impact potentiel sur la vie privée.

Répond aux questions sur le quand, les exceptions, la définition, et les obligations de l'AIPD.

Une méthode détaillée est fournie à travers plusieurs [documents](https://www.cnil.fr/sites/cnil/files/atoms/files/cnil-pia-1-fr-methode.pdf), démontrant la conformité.

### Le 29/11 :

Lecture approfondie des dossiers de la CNIL dédiés à [la méthode](https://www.cnil.fr/sites/cnil/files/atoms/files/cnil-pia-1-fr-methode.pdf), [les modèles](https://www.cnil.fr/sites/cnil/files/atoms/files/cnil-pia-2-fr-modeles.pdf) et [les bases de connaissances](https://www.cnil.fr/sites/cnil/files/atoms/files/cnil-pia-3-fr-basesdeconnaissances.pdf).

### Le 11/12 : Préparation de l'AIPD

Je collecte les données nécessaires, les informations et les accès requis pour cette étude auprès de mes collègues du GInfo, notamment le Gitlab du GInfo.

Je suis donc prêt à entamer l'étude de cas en analysant une application développée par le GInfo : [MyCentraleAsso](https://my.centrale-assos.fr/), offrant un service d'annuaire, calendrier associatif et centralisation d'informations utiles.

## L'AIPD en question :

L'AIPD peut être téléchargé ici même : [Télécharger maintenant](../CNILModèles.pdf) (je viens de la supprimer sans faire exprès de mon ordi, donc pour le moment, c'est le modèle vide que je vais re-remplir dans les jours à venir).

Mais pour **résumer**, la première partie sert à définir le périmètre de l'application [MyCentraleAsso](https://my.centrale-assos.fr/).

#### Respect des droits fondamentaux :

Ensuite très vite, il convient d'étudier si le site web respecte les réglementations en relation avec les droits fondamentaux tels que le droit de rectification, le droit à l'oubli. Ainsi, on s'intéresse à quel traitement des données est effectué pour ensuite se questionner sur la finalité, vérifier que le consentement est recueilli, vérifier quelle information est récoltée sur les différents individus. On résume cela dans un tableau qui indique pour chaque donnée si elle respecte :

 - la Minimisation des données;
 - la Qualité des données;
 - Un fondement juridique;
 - Une finalité définie et explicite;

On y associe les mesures qui assurent un droit.
La plupart des droits fondamentaux sont assurés soit par un accès facile aux membres du GInfo qui pourront satisfaire la demande des informations sur moi ou bien de rectification des données.

#### Sécurité technique :

Ici, nous nous assurons de la mise en place des techniques informatiques nécessaires à la sécurité, la confidentialité des données traitées : chiffrement, backup, anonymisation des données, le monitoring, ...
On y décrit aussi la gouvernance, les procédures de gestion de projet, ...

Ensuite, nous listons les risques potentiels qui pourraient nuire à l'association, les utilisateurs ou autres : Ici les risques principaux identifiés ont été :

 - la disparition des données;
 - un accès illégitime aux données;
 - une modification non désirée des données;

Les données stockées sur un utilisateur :

  Nom, Prénom, Régime alimentaire , date de naissance, associations et postes, adresse, tél, promo entrante, carte NFC

L'ensemble des autres données sont + ou - des données personnelles toutefois une des questions a été de se demander si le régime alimentaire est une information sensible pour l'utilisateur.
Il s'est révélé que c'est une donnée de santé et qui est donc sensibles. [Donc quoi ?]
Une anonymisation des données serait possible et pourrait bénéficier à diminuer les risques de fuite de données, toutefois l'impact potentiel est dans la plupart des cas de campagnes de phishing ciblé, ou des publicités ciblées non sollicité.

#### Les risques :

La disparition des données est peu probable grâce à la mise en place d'un stockage en RAID1. Mais, dans le cas où les deux serveurs physiques, qui sont stockés au même endroit deviennent inutilisables, il serait cool d'avoir un backup automatisé sur un serveur OVH dans lequel nous stockerions les backups. Passer en RAID5 coûterait très cher et serai trop importante.

Concernant un accès illégitime au données, on pense particulièrement à un ordinateur avec des accès privilégiés laissé ouvert. Pour remédier à cela, on préconise un rappel des bonnes pratiques de sécurité d'accès physiques aux installations ainsi que les pratiques de connexion pour diminuer la probabilité de ces événements, ainsi que la possible instauration d'un 2FA. De plus, on a vu plusieurs campagnes de phishing au sein de Centrale Marseille, donc un rappel des bonnes pratiques ne serait pas de trop. L'anonymisation des données notamment, spécifiquement les données concernant les données de santé, pour diminuer l'impact en cas d'accès illégitime à nos données.

Une modification non désirée des données pourrait arrivée suite un dysfonctionnement des librairies, ainsi on souhaite établir un ensemble de procédures annuelles menés par le responsable Réseau du GInfo pour mettre à jour les infrastructures et par les équipes de développement pour le code.

![Matrice des risques](../MatriceRisque.webp)

Concernant les possibles mises en place de processus de chiffrement, d'anonymisation, vu l'application et l'ampleur de l'installation et les capacités de l'association, beaucoup de mesures sembleraient être trop importantes face aux risques.

## Conclusion

C'est un exercice très formateur, qui semble être essentiel pour travailler dans la protection des données. Cela nous force à nous poser des questions importantes pour assurer la pérennité des différentes infrastructures tout en couvrant divers domaines.
J'ai étudié une application du GInfo, cela implique une gestion spécifiques du développement, des capacités financières, des capacités humaines ce qui rend complexe la recommandation de mesures efficaces. Le cadre de cette application ne permettait pas vraiment de voir les violations horribles d'une entreprise et parfois le code seulement ne permettait pas forcément d'avoir toutes les informations concernant les backups, l'anonymisation, ... Je comprends mieux les problématiques autour de cela mais je sais pas si c'est exactement ce dans quoi je veux travailler plus tard mais j'aimerais définitivement l'intégrer dans mes questionnement professionnelles.


### Bibliographie : 

- [AIPD](https://www.cnil.fr/fr/RGPD-analyse-impact-protection-des-donnees-aipd)
- [RGPD conformité](https://www.cnil.fr/fr/me-mettre-en-conformite)