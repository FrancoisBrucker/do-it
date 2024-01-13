---
layout: layout/pok.njk

title: "Élaboration d'un outil de planification en low-code"
authors:
  - Agathe Rabachou

date: 2023-12-13

tags: 
  - "temps 2"
  - "low-code"
  - "analyse de données"
  - "planification"

résumé: Un POK ayant pour objectif de découvrir le low-code et de l'appliquer à un exemple concret en analyse de données.
---
## Introduction

Initialement l'objectif de ce POK était de découvrir le low-code, n'ayant pas suivi ce cours au temps 1 et ayant entendu des retours très positifs sur celui-ci. J'avais donc imaginé inventer un prétexte, site ou application, pour pouvoir apprendre et pratiquer. J'ai finalement trouvé un cas d'étude plus intéressant lorsqu'Henri m'a parlé d'une connaissance qui cherchait à refaire l'outil de planification de son entreprise en low-code. Cela me donnait un cas concret, avec un contexte et un réel besoin client, et je me suis donc lancée dans ce projet.

## Sprint 1

### Objectifs

- Découverte du sujet, contact avec le client, étude du fonctionnement actuel de l'entreprise et des problèmes qui en découlent, compréhension du besoin et mise en place d'un cahier des charges de l'outil à créer (5h) ;
- Comparaison des différents moyen de faire du low-code, choix de la ou des technologies à utiliser et prise en main de leur fonctionnement (3h) ;
- Premières réflexions sur la solution à mettre en place (2h).

### Réalisations

Pour commencer, j'ai pris contact avec le client pour réaliser un bilan de la situation existante, dont voici un compte rendu :

**Contexte** : La société est une ETI (Entreprise de Taille Intermédiaire) du domaine agricole. Son activité principale est constituée de prestations de paysagisme telles que la tonte de pelouse, le taillage d'arbres ou de haies ou encore le ramassage de feuilles. L'entreprise a environ 300 clients pour 600 sites à entretenir. Elle se compose de 9 équipes de 2 à 3 personnes. Dans chacune d'entre-elles un chef d'équipe est désigné. Chaque équipe a un nombre défini de sites et de clients à gérer, répartis en général par zones géographiques, matériel nécessaire aux travaux et habilitations et compétences des chefs d'équipes (autorisations pour certaines machines, permis remorque, CACES, habilitation électrique...).

**Problème** : De plus en plus de chefs d’équipe sont incapables d’organiser les tournées ou sont peu motivés et trichent sur les heures. Le management demande donc que les encadrants prennent en main l'organisation des tournées et imposent les chantiers à réaliser chaque jour.

**Organisation actuelle** : Les tournées sont organisées sur un tableau à feutres, les jours de la semaine en colonnes, les chefs d'équipe en lignes, et les cases sont complétées pour indiquer qui s'occupe quand de quel client ou secteur géographique. Ils ont également un tableau pour confirmer les travaux effectués, les semaines en colonnes, les sites en lignes, et les cases sont hachurées pour indiquer que la prestation a bien été réalisées. Enfin, les chefs d'équipes entrent leurs heures dans un ERP, chaque jour et pour chaque site.
Pour ce qui est de la solution actuelle de recensement des prestations, il s'agit d'un fichier Excel qui contient pour chaque prestation le client, le site, le chef d'équipe, le type de prestation, la fréquence et la durée d'intervention, le nombre de personnes et le matériel utilisé. L'entreprise est également en train de tester un outil Excel qui permet de comparer le nombre d'heures planifiées sur ce document avec le nombre d'heures réellement effectuées.

**Objectif de l'outil à développer** : L'outil à élaborer devra permettre de planifier les interventions à venir et de les réajuster selon les aléas, afin d'optimiser l'activité et de mieux contrôler les équipes. Parmi ces aléas on trouve régulièrement les absences, les intempéries, la casse de matériel ou encore les annulations du client. Pour gérer cette planification, il faudra prendre en compte les compétences et habilitations des chefs d'équipes, leur entente avec les autres membres, l'éloignement entre leur domicile et les sites de chantiers (que l'on essaiera de minimiser), les contraintes clients (horaires, jours, délais de prévenance...) et la possibilité pour les équipes de rentrer sur les sites (pour les clients industriels notamment, avec des questions de plan de prévention).
Voici quelques directives pour certains des aléas courants :
- En cas d'absence de dernière minute, on essaie de recomposer une équipe en faisant passer un second au rang de chef d'équipe pour une journée si nécessaire. Si ce n'est pas possible, on annule les chantiers planifiés ;
- Pour ce qui est des intempéries, si c'est un impératif l'équipe réalise la prestation, sinon le chantier est reporté. Si il y a un délai côté client le chantier doit être repositionné rapidement, sinon c'est plus aléatoire.

**Contraintes supplémentaires** :
- La solution proposée doit convenir à du personnel qui n'est pas forcément très à l'aise avec l'informatique, il faut donc qu'elle soit la plus simple possible ;
- Idéalement elle communiquerait avec l'ERP pour remplir la fonction de l'outil actuellement en développement ;
- Elle devrai rester facilement adaptable à tout changement effectué à la main en dernière minute.


Dans un deuxième temps s'est posée la question du ou des outils low-code à utiliser. J'ai donc fait des recherches sur les différentes technologies existantes pour déterminer ce qui conviendrait le mieux au cas d'étude. J'ai regardé différents tutoriels d'utilisation, entre autres de Microsoft Power Apps, Mendix ou Appian. Finalement, Airtable m'a semblé être la solution la plus intuitive et adaptée à l'analyse de données, et je prévois donc de me servir de cette plateforme. L'idée serait de l'utiliser pour la partie analyse des données et de garder Excel en ce qui concerne l'affichage de la planification et sa manipulation.
J'ai également commencé à me renseigner sur des solutions pour mettre en lien  l'ERP existant avec le nouveau système de planification, notamment avec des outils comme Zapier ou Make (anciennement Integromat), mais je n'ai pas assez poussé mes recherches pour choisir une solution en particulier, d'autant plus que je ne suis pas encore sûre d'avoir le temps d'implémenter cette fonctionnalité.

### Retours

Pour conclure ce premier sprint, j'ai à peu près réalisé les objectifs prévus dans le temps imparti (un peu moins de 10h en réalité). Je pense cependant que j'aurais pu passer moins de temps sur l'étude des outils low-code si j'avais fait des recherches de manières plus structurée et méthodique et sans me disperser comme j'ai pu le faire.
Malgré ma légère avance sur le sprint planning en terme de temps, je n'ai pas pu commencer le développement de la solution (qui me prendra je pense un peu plus de 10h) car j'ai reçu certaines informations plutôt tardivement relativement à la date de la première revue. Je pense donc que ce POK avoisinera bien les 20h au total mais de manière un peu déséquilibrée entre les deux sprints.

## Sprint 2

### Objectifs

- Finalisation de la réflexion autour du design et du fonctionnement final de la solution (1h) ;
- Développement de l'outil (8h) ;
- Tests et retours par le client (1h) ;
- Reprise de la solution si besoin (en plus).

### Réalisations



### Retours