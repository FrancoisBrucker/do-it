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

L'AIPD peut être téléchargé ici même : [Clique-moi dessus !](../CNILModèles.pdf) (je viens de la supprimer sans faire exprès de mon ordi, donc pour le moment, c'est le modèle vide).

Mais pour résumer, la première partie sert à définir le périmètre de l'application MyCentraleAsso.

#### Respect des droit fondamentaux : 

Ensuite très vite, il convient d'étudier si le site web respecte les réglementations en relation avec les droits fondamentaux tel que le droit de rectification, le droit à l'oubli. Ainsi, on s'intéresse à quelle traitement des données est effectué pour ensuite se questionner sur la finalité, vérifier que le consentement est recueilli, vérifier quelle informations est récolté sur les différents individus. On résume cela dans un tableau qui indique pour chaque donnée si elle respecte  :

 - la Minimisation des données;
 - la Qualité des données;
 - Un fondement juridique;
 - Une finalité définie et explicite;

On y associe les mesures qui assure un droit.

#### Sécurité technique :

Ici, nous nous assurons de la mise en place des techniques informatiques nécessaires à la sécurité, la confidentialité des données traitées : chiffrement, backup, anonymisation des données, le monitoring, ...
On y décrit aussi la gouvernance, les procédures de gestion de projet, ...

Ensuite nous listons les risques potentiels qui pourraient nuire à l'association, les utilisateurs ou autres : Ici les risques principaux identifiés ont été :

 - la disparition des données;
 - un accès illégitime aux données;
 - une modification non désirée des données;


#### Les risques :

La disparition des données est peu probable grâce à la mise en place d'un stockage en RAID1 sur les serveur du GINFO et une partie est sauvegardée sur un serveur OVH.

Concernant un accès illégitime au données, on pense particulièrement à un ordinateur avec des accès privilégiés laissé ouvert. Pour remédier à cela, on préconise un rappel des bonnes pratiques de sécurité d'accès physiques aux installations ainsi que les pratiques de connexion pour diminuer la probabilité de ces événements, ainsi que la possible instauration d'un 2FA. De plus, on a vu plusieurs campagnes de phishing au sein de Centrale Marseille, donc un rappel des bonnes pratiques ne serait pas de trop.

Une modification non désirée des données pourrait arrivée suite un dysfonctionnement des librairies, ainsi on souhaite établir un ensemble de procédures annuelles menés par le responsable Réseau du GInfo pour mettre à jour les infrastructures et par les équipes de développement pour le code.

![Matrice des risques](../MatriceRisque.png)

Concernant les possibles mises en place de processus de chiffrement, d'anonymisation, vu l'application et l'ampleur de l'installation et les capacités de l'association, beaucoup de mesures sembleraient être trop importantes face aux risques.

### Conclusion

C'est un exercice très formateur, qui semble être essentielle pour travailler dans la protection des données. Cela nous force à nous poser des questions importantes pour assurer la pérennité des différentes infrastructures tout en couvrant divers domaines.