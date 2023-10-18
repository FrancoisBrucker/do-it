---
layout: layout/mon.njk

title: "Cryptographie et sécurité des données"
authors:
  - Arthur Louradou

date: 2023-09-18

tags: 
  - "temps 1"
  - "cyber"
  - "cryptographie"
  - "security"
  - "web"
  - "sql"

résumé: "Ce MON s’inscrit dans la continuité du précédent, où nous étudions la cybersécurité sous le prisme des tests d’intrusion (pentest). En particulier, nous détaillerons les bonnes pratiques en matière de sécurité dans les bases de données."
---

## Prérequis

La lecture de ce MON nécessite une appétence pour la cybersécurité mais ne nécessite pas de base solide en cryptographie. En revanche, il est recommandé de connaitre l’architecture des applications web, soit la distinction entre Back-End, Front-End et base de donnée qui s’opère dans la plupart des systèmes d’information à visée web.

## Objectifs du MON

Mon collègue Assane a développé une application de prise de note en ligne avec des fonctionnalités user-friendly pour répondre à des besoins non comblés par les applications du marché. Avec sa solution dont nous pouvons consulter le code à l’heure actuelle (à [cette adresse](https://github.com/assanediouf18/ginfo_notes) ?), il est possible de stocker des informations comme du texte, de la vidéo ou des images sur son serveur distant. Cependant, durant nos discussions, nous nous posions la question de la sécurité autour des données des utilisateurs.

L’objectif de ce MON est de comprendre l’état de l’art en matière de sécurité informatique sur les solutions web et Cloud, puis d’étudier les principes cryptographiques servant à ces usages.

Ce MON s’inscrit dans la continuité du précédent (lien), où nous étudions la cybersécurité sous le prisme des tests d’intrusion (pentest).

## Autres MONs

[Thibault - Hachage et chiffrement](https://francoisbrucker.github.io/do-it/promos/2022-2023/Adelain-thibault/mon/HachageChiffrement/)

## État de l’art sur la sécurité des bases de données

En référence au document de l’ANSSI [[4]](#bibliographie). Plusieurs principes sont exposés, comme le fait de traiter la sécurité dès le début du développement d’une application web pour à la fois réduire les couts et maintenir une sécurité jusqu’au déploiement. Ensuite, il es important de noter que la défense contre les menaces n’est pas à cantonner au simple périmètre de l’application. Les vulnérabilités internes pourraient en effet être exploitées en cas de défaillance des différents points d’entrée. Il est donc important de réduire au maximum les privilèges au strict minimum et dans l’ensemble de l’application, notamment sur les APIs.

La liste des bonnes pratiques donne aussi la possibilité de mettre en place des buts bounty pour permettre aux hackers éthiques de tester la sécurité de sa solution dans un cadre réglementaire strict.

### TLS

Abordé dans le précédent MON, nous allons entrer dans le détail de ce type de sécurité qui fait partie du protocole HTTPS. Les recommandations de l’ANSSI sont aussi claires et sont référencées en [[5]](#bibliographie). Le processus d’échange de clés asymétrique puis symétrique y est schématisé et détaillé en fig 1.1 et 1.2.

Pour rentrer un peu dans le détail, le protocole TLS 1.2 a été abandonné pour des raisons de sécurité et l’architecture du handshake (séquence de premiers échanges entre client et serveur) a été repensée pour n’avoir qu’un seul échange non chiffré entre les deux parties dans la version 1.3.

#### Les certificats

Durant la négociation TLS, soit le premier échange, sont envoyés des clés publiques associées au nom de domaine de l’envoyeur. Ces clés publiques sont des certificats répondant à une certaine norme (X.509) et présents dans les systèmes d’exploitation Apple, Microsoft ou Debian.

#### Vulnérabilités

**Protection contre les vulnérabilités XSS**

Les vulnérabilités XSS (Cross-Site Scripting) peuvent compromettre la sécurité d'un site web en permettant à des attaquants d'injecter des scripts malveillants dans les pages consultées par les utilisateurs. Ces failles sont explorés dans d’autres MON comme [celui de Thibault](https://francoisbrucker.github.io/do-it/promos/2022-2023/Adelain-thibault/mon/FaillesWeb/). Pour se protéger contre les attaques XSS, il faut valider et encoder correctement les données provenant des utilisateurs avant de les afficher.

Ensuite, la mise en place d'une Content Security Policy (CSP) constitue une défense de plus contre les attaques XSS en restreignant les sources à partir desquelles les ressources peuvent être chargées sur un site web.

Enfin, CORS définit des politiques qui permettent ou restreignent les requêtes effectuées à partir d'une page web vers un autre domaine. Les développeurs doivent inclure des systèmes de jeton d’autorisation dans les demandes effectuées au serveur pour garantir un niveau de permission nécessaire à toute personne consultant une ressource.

### Protection de la base de données

Pour entrer dans le vif du sujet, voici ce que l’on peut lire dans les différentes sources mentionnées pour sécuriser sa base de donnée et répondre à la question d’Assane.

D’abord, les Systèmes de Gestion des Bases de Données (SGDB) offrent souvent des fonctionnalités de chiffrement de la base de données en elle même. Il est important de savoir où se situe la clé de déchiffrement de la base pour maximiser la compréhension des vecteurs d’attaque. Il est aussi possible en fonction du SGDB de chiffrer ses tables par colonnes, rendant plus difficile la compromission de clés.

Bien sur, il est important d’adopter une stratégie robuste de gestion des clés. Pour cela, il faut augmenter au maximum les niveaux de privilège nécessaire à l’accès à ces clés (pourquoi le PDG en aurait-il besoin ?). C’est en se posant ces questions que l’on établit une stratégie efficace de gestion des clés.

Enfin, dans le Cloud, des outils existent pour construire une stratégie de stockage des données efficace et résiliante, comme le **[AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc&wa-guidance-whitepapers.sort-by=item.additionalFields.sortDate&wa-guidance-whitepapers.sort-order=desc)** ou le **[Microsoft Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/)**.

### Mise en pratique

J’ai effectué au cours de ce MON un challenge HackTheBox sur la cryptographie, en inversant une sorte de chiffrement de César en python. La correction du challenge est détaillée sur [cet article Medium](https://medium.com/@grumpyTofu/babyencryption-technical-analysis-hack-the-box-cryptography-9114bf06701a) et est assez instructive pour les façons de décrypter des données. [Décrypter : pas déchiffrer](https://blog.cellenza.com/securite-2/decrypter-nest-pas-dechiffrer/), car ici l’objectif est bien de trouver le code sans la clé de chiffrement.

Finalement, ce challenge a mis en lumière que l’on peut passer du temps à tester la sécurité informatique d’une application web, puisqu’avant de lire la solution, j’ai essayé toutes sortes de méthodes sans oser l’attaque par force brute. Finalement, en local sur sa machine, il n’y a pas de limite pour pratiquer la force brute, si ce n’est celle de l’imagination du pentester.

J’ai par ailleurs parcouru d’autres challenges qui ne valent pas forcément la peine d’être détaillés ici car ils étaient plus éloignés du sujet. Un conseil : allez lire quelques challenges sur [HackTheBox](https://www.hackthebox.com/) ou bien [Root-Me](https://www.root-me.org/), c’est très instructif !

## Regard critique et ouverture

À la lecture des documents de l’ANSSI, nous découvrons que la sécurité des bases de données repose avant tout sur la sécurité des applications et des voies de communication. Ce MON a donc pris un tournant plus ciblé sur ce type d’attaques par rapport à ce qui était prévu initialement.

Il aurait été probablement instructif de creuser d’avantage le sujet des bases de données.

## Ce que j’ai appris durant ce MON

Tout d’abord, j’ai appris à lire de a documentation technique et en particulier celle de l’ANSSI, ce qui ne m’était jamais arrivé précédemment alors même que ces ressources sont capitales pour avoir connaissance des attaques et des menaces qui gravitent autour des applications que nous développons et utilisons.

Ensuite, concernant la sécurité des bases de données, j’ai pu prendre connaissance des bonnes pratiques pour la gestion des clés de chiffrement.

Pour terminer, j’ai eu l’occasion de m’entrainer pendant quelques temps sur des exercices pratiques en cybersécurité.

Je recommande d’aller voir les sources qui sont très instructives ainsi que d’en regarder les vidéos.

Assane, j’ai donc la réponse pour ton application de prise de notes : lis ce MON !

## Bibliographie { #bibliographie }

[1] https://www.cnil.fr/fr/securite-chiffrer-garantir-lintegrite-ou-signer

[2] Lisez le cours d’Ops de 3A pour l’essentiel de la cryptographie : [https://francoisbrucker.github.io/cours_informatique/cours/système/cryptographie/](https://francoisbrucker.github.io/cours_informatique/cours/syst%C3%A8me/cryptographie/)

[3] Tier List des mauvaises pratiques en base de donnée : https://youtu.be/qgpsIBLvrGY?si=thbilRdKPaUnBPFS

[4] ANSSI recommandations web : https://www.ssi.gouv.fr/guide/recommandations-pour-la-securisation-des-sites-web/

[5] ANSSI TLS : https://www.ssi.gouv.fr/guide/recommandations-de-securite-relatives-a-tls/

[6] Vidéo de Cocadmin sur la sécurité des serveurs, selon les recommandations de la NSA : https://www.youtube.com/watch?v=UmbndsZFIUE

[bonus] Sécurité Wifi et recommandation de l’ANSII
https://www.ssi.gouv.fr/guide/recommandations-de-securite-relatives-aux-reseaux-wifi/
