---
layout: layout/pok.njk

title: "POK2 - Pass' Diplôme"
authors:
  - Inès Kebbab

date: 2024-10-16

tags:
  - "temps 2"
  - "info"
  - "gestion de projet"
  - "management SI"

résumé: Ce second POK réalisé en collaboration avec Alix Duréault a pour objectif de réaliser un SI pour suivre et communiquer les items de diplomation, en collaboration avec la formation de l'école.
---

[Lire ici la deuxième partie de ce POK réalisée par Alix.](../../../../../Alix-Dureault/pok/temps-2/)

Autres POK ou MON en lien :
[MON 3.1 : Débuter avec React.js, Thomas DUROY](../../../../2022-2023/Duroy-Thomas/mon/MON_3.1/)


## Objectifs

L'objectif de ce POK est de réaliser un système d'information sur un exemple concret, via une base de données (excel et site internet) tout en respectant des contraintes RGPD. Concrètement, les élèves doivent pouvoir consulter les éléments qui les concernent exclusivement.

Ce projet a aussi pour but d'observer les enjeux de management de l'information au sein des services de l'école dans le cadre d'un projet, notamment pour la mise en place d'un process qui se veut durable.

À noter, nous nous sommes engagées en termes de moyens et non de résultat.

## Tâches

#### Sprint 1 - Structuration de la base de donnée
1. [X] Réalisation d'un excel et étude de l'automatisation possible
2. [X] Réalisation d'une maquette du site souhaité
3. [X] Etude des technologies compatibles avec la DSI de Centrale
4. [X] Initialisation d'une base de données test.

*NB: A posteriori, l'automatisation totale de la base de données et du partage d'un excel ne semble pas possible voire souhaitable.*

#### Sprint 2 - Ajout des autres blocs et informations
1. [ ] Front-end du site (fait par Alix)
2. [/] Back-end du site (+ connexion au CAS si accepté par la DSI)
3. [ ] Mise en conformité RGPD
4. [/] Proposition du nouveau process aux équipes
5. [ ] Communication à destination des élèves sur le projet


## Contenu

### Premier Sprint

#### Expression du besoin et management de l'information au sein de l'école

En commençant le projet, nous savions qu'un excel existait et assurait (en partie) le suivi des éléments de diplomation des élèves. Du coté des élèves, la besoin avait été exprimé il y a quelques mois par un ancien élu du CE.

Nous avons pu organiser un point avec le personnel administratif qui sont concernés dans le report des éléments de suivi. Il est ressorti que le SI actuel n'était pas optimisé pour leurs usages :
- Relance des élèves difficile;
- Manque de vision et consolidation des éléments avant la préparation du jury 3A ;
- Confusion sur les responsables de certaines données du fichier ;
- Complexité des éléments de l'excel et données.

Aussi, pour ne pas créer un outil parfait pour les élèves mais irréaliste côté administration (par rapport à la fourniture des données), nous les avons challenger pour mieux cerner leurs contraintes (outil et excel facilement modulable). Nous avons aussi pu mettre la priorité sur la partie "rendre visible aux élèves les informations" plutôt que de se concentrer sur l'automatisation d'un document au service de la direction de formation (les compétences étant a priori déjà présente).

Nous avons cartographier les éléments de diplomation à communiquer (offrant une vision d'ensemble utile pour l'ensemble des participantes) et il nous a été fourni un jeu de fausses données anonymisées pour tester notre projet.

#### Contraintes techniques et fonctionnelles

Avec la DSI, nous avons aussi pu mieux comprendre les contraintes techniques et fonctionnelles pour le projet (choix du langage, technique de base de données,...) pour optimiser la pérennisation du projet après notre départ à Centrale (soit via un accord avec le GInfo, ou pour de la maintenance avec les compétences déjà existantes de la DSI). Nous avons aussi convenu qu'il serait plus simple d'écraser la base de données à chaque import de fichier (en CSV) pour commencer. 

Nous avions un référent sur ce projet au sein de la DSI : Clément Leneuveu.

#### Maquette UI/UX

Pour penser le parcours utilisateur, j'ai pu m'appuyer sur la première maquette réalisée par Alix pour l'améliorer. Celle-ci a notamment pu récupérer des retours d'élèves sur lesquels j'ai pu me baser pour améliorer notre interface.

Comme nous avions conscience de la durée courte que nous avions pour réaliser le projet et de nos compétences pour les coder, nous avons décidé de prioriser les fonctionnalités sur le test de la page de connexion et l'import / lecture et affichage d'une ligne du fichier CSV. Alix s'est chargé de la partie Front de la page d'affichage.

#### Analyse Post Mortem du sprint 1

Je ne suis pas satisfaite de ce sprint 1 pour plusieurs raisons :
- Je n'ai pas réussi à caler mes heures de travail sur le temps imparti (en partie à cause de mes cours et de contraintes personnelles). J'espérais initalement avancer pendant la semaine de FM Entrepreneuriat, sans succès.
- J'ai eu beaucoup de mal à apprendre à utiliser React : je ne me sens toujours pas à l'aise avec. Si je sens le potentiel de ce langage, je suis frustrée pour le moment car j'ai l'impression d'utiliser les mêmes concepts qu'en HTML/CSS/JS mais en "pas tout à fait".

Je trouve que le travail que l'on a mené avec Alix était complémentaire et permet d'avoir une vision "extérieure" sur son travail qui est agréable. 

Finalement, même si nous avons pu remplir les objectifs que je m'étais fixée : ils étaient peut-être sous-dimensionnés mais ils ne prenaient pas en compte l'apprentissage de React qui me prend du temps. Je pense que je sous-estime encore trop le temps que cela me demande d'apprendre à coder. Je ne pense pas avoir de facilité sur le sujet ce qui est frustrant (bien que challengeant).

J'observe aussi que la part de réunion est importante mais finalement, cela semble cohérent avec un travail de PM ou PO ou au vu de la phase "expression et définition du besoin".

### Second Sprint

#### Finalisation de la maquette

J'ai pu ajouter des éléments ou penser à des fonctionnalités utiles pour les gestionnaires sur la base des écrans que nous avions déjà identifié (vue pour tester une vue élève et l'affichage des données, historique et export des derniers imports, gestionnaire des droits d'administration). Nous avons aussi pu ajouter une page d'accueil pour les utilisateurs qui ne viendraient pas de l'ENT ou qui ne seraient pas déjà connecté (une page FAQ, à l'instar du site des stages).

NB. Les données finales de l'excel concernant la mobilité est à revoir après échange avec C. Musy : en effet, il est intéressant de suivre comment les élèves ont effectué leur mobilité (SMA, SSE, autre) pour la préparation de la remise des diplômes.

#### Mise en place des fondations pour le "back" (BDD, connexion, sécurisation des données)

Lors de notre entretien avec Clément Leneuveu, nous avons présenté nos avancées et choix techniques à notre référent. Nous avons vu ensemble :
- La question d'une base de donnée pour le projet. Celle-ci ne semble pas nécessaire pour le moment, nous pouvons enore nous en sortir avec la lecture et le stockage du fichier CSV directement via React.
  
- L'utilisation d'une connexion au CAS (avec un client React et un lien avec un serveur Test en Java utilisant SpringBoot). Il nous a expliqué quelles étaient les informations transmises dans un ticket CAS lors de connexion, la gestion des droits (droits pour un service VS droits nominatifs...). Les données récoltées pourront être croisées avec notre excel de données via un pivot (ici le numéro étudiant).

- La gestion des gestionnaires et administrateurs : la piste la plus prometteuse serait la configuration des droits dans un fichier XML ou JSON dans les fichiers config.

#### Connexion au serveur CAS, création d'une page de connexion et d'un form pour import du CSV

Pour l'import du fichier CSV et la lecture avec React, j'ai identifié trois pistes de solutions :
- La librairie Papa Parse, qui est régulièrement revenu dans mes recherches ;
- La fonction FileReader (qui semble limité au parcours d'un fichier clairement choisi par l'utilisateur) ;
- Avec Refine, un "meta-framework" React pour développer des applications.

La solution qui semble la plus pertinente à explorer semble donc d'utiliser la librairie PapaParse dans le cadre de notre projet.

J'ai testé des bouts de code pour tester l'import d'un fichier CSV, mais n'arrivant pas à créer des routes et URLs cohérentes sur l'app React, je n'arrivais pas à un résultat plus satisfaisant qu'un bouton non cliquable... 

De même, j'ai essayé de créer une page d'accueil ou avec un formulaire de connexion, mais les liens avec les autres pages empêcher l'application de se build correctement.

J'en suis arrivée à la conclusion qu'il fallait que je reprenne plus méthodiquement la construction de l'app et des fonctionnalités ; il me faut aussi revoir plus en profondeur les principes de base d'une app en React sur lesquels je me suis peu penchée.


Pour le serveur CAS, je me suis appuyée sur les ressources fournies par la DSI. J'ai installé le nécessaire, avec les versions nécessaires de Java, Apache Ant, Apache Maven et Tomcat. Si j'ai rapidement réussi à lancer le client React, j'ai mis près de 2h avant de réussir à lancer le serveur SpringBoot (l'API). Néanmoins, malgré de nombreuses tentatives pour débugger, je n'ai pas visiblement pas encore réussi à faire communiquer le front et le back.

J'obtiens l'erreur suivante :  `Error occurred while trying to proxy: localhost:3000/`.

Une piste à explorer pour avancer est d'étudier les problèmes de CORS avec React pour autoriser (si ce n'est pas déjà le cas) la communication entre deux adresses en localhost.

#### Rattrapages Sprint 1
Tout d'abord, pour rattraper le retard sur le sprint 1, il me reste 3h30 à consacrer à ce travail (jeudi et vendredi). Voici ma to do list à titre indicative :

1. [] Faire le routing URL et une navigation avec 3 pages vierges (accueil, import, gestionnaire de droits) et celle de visualisation des élèves.

2. [] Pour la page upload : télécharger un CSV, lire et stocker les données CSV (éventuellement, comprendre comment garder l'historique des 3 derniers fichiers dans un JSON par exemple et le téléchager).

3. [] Pour la page "Eleve" : affichage conditionnel sur l'exemple d'un élève.

4. [] Résoudre le problème de connexion au CAS avec la DSI.

5. [] Modifier l'excel par rapport à la mobilité internationale.

### Conclusion et suites possibles

Concernant le projet, il semble pertinent de le continuer (pour ma part en dehors d'un POK&MON) pour le pérenniser car il est utile. Je trouve cela motivant de travailler sur un projet qui fait sens, auquel je souhaitais depuis plusieurs mois consacrer du temps sans le trouver et d'apprendre des notions techniques pour lui permettre de voir jour. 

Pour la pérennisation, il reste encore de nombreuses étapes :
- Faire marcher la connexion CAS (on y est presque ! plus qu'un petit effort...);
- Gestion des droits selon le compte ;
- Rédiger la documentation du projet (et formaliser la partie RGPD);
- Pérenniser le projet avec un accord avec le GInfo ;
- Déploiement du site sur les serveurs du CRI (ou du GInfo);
- Communication auprès des élèves.

#### Ce que j'ai appris :
Pour ma part, je ne me sens pas encore à l'aise avec React mais je souhaite persévérer pour comprendre les bases et arriver à produire un front et des fonctionnalités correctes.

J'ai appris à me questionner sur le besoin en base de données, et plus globalement sur l'organisation d'un SI au sein d'une organisation. J'ai aimé découvrir le fonctionnement d'une DSI sur un exemple concret et observer leurs interactions avec un service opérationnel.

#### Les erreurs à éviter :

J'ai observé que j'ai tendance à m'éparpiller sur les projets dès que je rentre dans le code : je souhaite tout faire d'un coup, sans me poser avant de me lancer. 

Plus la tâche me semble complexe, plus celle-ci me semble insurmontable : hors, dès que j'ai réfléchi pour redécouper la tâche "Back" en plusieurs sous-tâches priorisées et ordonnées, cela m'a permis d'avoir une vision pour avancer plus sereinement.

Je pense qu'il faut aussi savoir s'arrêter plus tôt dès que l'on bloque et oser demander de l'aide (ou a minima laisser décanter). 


### Horodatage

| Date | Heures passées | Indications |
| -------- | -------- |-------- |
|  **Sprint 1** | | 6H45/10H ⚠️ |
| 08/10/24 | 1H | Réunion de cadrage - Expression du besoin fonctionnel - Formation |
| 23/10/24 | 1H | Réunion de cadrage "technique" - DSI |
| 14/11/24 | 15min | Retours/validation de l'excel |
| 16/11/24 | 1H30 | Formation à React |
| 17/11/24 | 1H30 | Maquette Figma |
| 18/11/24 | 30min | Echange projet avec Alix |
| | 1H | Point de mi-projet avec C. Musy |
|  **Sprint 2** | | 10H/10H |
| 07/12/24 | 2H | Finalisation de la maquette (tests avec icônes, design unique...) + retours élèves |
| 09/12/24 | 1H | Point suivi avec C. Musy |
| 12/12/24 | 1H30 | Point technique avec C.Leneveu (connexion CAS, BDD) |
| 14/12/24 | 1h | Recherches et test import et lecture d'un fichier CSV avec React |
| 16/12/24 | 1h30 | Back : Test Page de Connexion / Connexion via CAS (installation Java pour SpringBoot, test client React) - blocage sur le lancement du serveur |
| 17/12/24 | 1H30 | Back : Test Connexion via CAS  |
| 18/12/24 | 1H30 | Rédaction rendu POK |