---
layout: layout/pok.njk

title: "POK 3 - données et risques"
authors:
  - Schultz Mathis

date: 2024-02-28

tags: 
  - "temps 3"
  - "data"
  - "cybersécurité"

résumé: Le but de ce POK est d'analyser les risques de la data
---

<h2 id="h1"> Introduction </h2>

Le but de ce pok est de s'intéresser aux enjeux de cybersécurité au travers d'une approche sociétale.
J'ai commencé par une introduction à la cybercriminalité sur [Open Classroom 1](https://openclassrooms.com/fr/courses/8028761-decouvrez-lunivers-de-la-cybersecurite), que j'ai complété avec des recherches de documentations et quelques informations du cours de cybersécurité du temps 3.
Pour le second sprint j'ai aussi prévu un cours de cryptographie pour entrer plus profondément dans le sujet via [Open Classroom 2](https://openclassrooms.com/fr/courses/1757741-securisez-vos-donnees-avec-la-cryptographie).

<h2 id="toc"> Table des matières </h2>

- [Introduction](#h1)
- [Table des matières](#toc)
- [Organisation des sprints](#sprint)
- [Sprint 1](#h2)
- [Sprint 2](#h3)
- [Conclusion](#h4)
- [Liens utiles](#liens)

<h2 id="sprint"> Organisation des sprints </h2>

**Objectif du premier sprint**

- Histoire de la cybercriminalité. (le rôle de la Russie et la stratégie actuelle)
- État actuel de la cybercriminalité. (les méthodes utilisées, une course sans fin ?)
- Chiffrer son impact. (économique, social, politique et environnemental ?)

**Objectif du second sprint**

- Les stratégies des géants du numérique (l'inter-connectivité, la complexification et la centralisation de la data)
- Les bonnes pratiques des développeurs.
- Les bonnes pratiques des utilisateurs.

<h2 id="h2"> Sprint 1 </h2>

**Histoire de la cybercriminalité.**

**État actuel de la cybercriminalité. (les méthodes utilisées, une course sans fin ?)**

- L'homme, le maillon faible de la sécurité ?

Les géants d'internet qui ont pour coeur de métier l'IT ne sont pas épargné, voici un aperçu de l'histoire d'Uber, qui illustre la faiblesse de l'homme dans la cybersécurité :

Dans une conversation avec le chercheur en cybersécurité Corben Leo, le hacker a révélé avoir obtenu l’accès aux systèmes de Uber à l’aide d’identifiants de connexion obtenus auprès d’un employé grâce à l’ingénierie sociale. Il s’est fait passer par un membre de l’équipe IT de l’entreprise afin de piéger sa victime.

C’est ce qui lui a permis d’accèder à un VPN interne de l’entreprise, puis de trouver les scripts PowerShell sur l’intranet d’Uber contenant les identifiants de gestion d’accès. Il a ainsi pu infiltrer les comptes AWS et G Suite.

Le 19 septembre 2022, Uber a précisé que le hacker a en fait acheté le mot de passe d’un sous-traitant sur le Dark Web. Les identifiants du sous-traitant en question auraient été exposés par un malware ayant infecté son laptop.

Le cybercriminel aurait ensuite tenté à plusieurs reprises de se connecter au compte. Toutefois, grâce à l’authentification à deux facteurs, le sous-traitant recevait une requête d’approbation à chaque tentative et bloquait l’accès en refusant. Malheureusement, il a finalement accepté l’une des requêtes et le hacker a pu se connecter.

- le chiffrement RSA : pilier fragile d'internet

Le chiffrage RSA est utilisé dans de nombreux domaines numériques au quotidien. À titre d’exemple, les protocoles de communication HTTPS (Hypertext Transfer Protocol Secure) ou encore les certificats SSL sont la plupart du temps sécurisés à l’aide d’un chiffrage RSA. Un système de chiffrement RSA permet également d’encoder les emails ou messages d’une boîte de messagerie, des données d’images ou même un disque dur. Sans la clé de chiffrement RSA nécessaire, il serait trop long de décoder ces données, même avec la puissance de calcul la plus élevée qui soit. Ce processus est donc considéré comme étant relativement sécurisé.

Le principal problème de ce système réside dans la simplicité théorique à le décoder. En effet, la protection réside sur le fait que le temps de calcul est trop long pour être réalisé actuellement. Cependant, une méthode utilisé pour outrepasser ce système est d'accumuler un grand nombre de communication chiffrer et de les stocker pour plus tard, lorsque la technologie sera suffisamment rapide pour les décoder. On pourrait penser que le temps que cela se produise, l'information sera obsolète. Cependant, des informations tels que les données bancaires, données personnelles ou mot de passe sont souvent utilisé longtemps.

- Le rôle des ordinateurs quantiques

Le rôle des ordinateurs quantique pourrait mettre fin au chiffrement RSA. En effet, suite aux différents concours de chiffrement, il a été démontré que des algorithmes quantiques peuvent décoder très rapidement le chiffrement RSA via notamment l'algorithme de SHOR.  
Il faut tout de même noter que ces ordinateurs ne sont pas encore industrialisable à cause des contraintes de température des supraconducteur. De plus, de nouvelle méthode de chiffrement sont déjà prête pour être mise en place si les ordinateurs quantique se répande.

**Chiffrer son impact. (économique, social, politique et environnemental ?)**

- Le rôle des cryptomonaies

Le montant des cyberattaque via ransomware en 2023 a simplement atteint 1,1 milliards de dollars en cryptomonaies. En effet, les cryptomonaies ont un gros avantage, elles sont difficile à tracer, et ne sont pas sous la tutelle d'une banque étatique, donc impossible à inspecter.

![Montant des ransomwares](image.png)

- La data, un nerf de la guerre ?

Les nouvelles entreprises sont pour beaucoup des services internet : Amazon, Uber Eats, Tik Tok, Cloud. Elles ont toutes en commun une stratégie basée sur la donnée, qui consiste à toucher le publique le plus large possible et à collecter un maximum de données. Certains vont se servir des données pour améliorer leur service via des suggestion ou plus simplement vendre les données. Ces données sont normalement anonymisée pour être vendu. Ainsi, on peut collecter énormément de données légalement sur internet. Jusque là il n'y a pas de faille majeur de sécurité. Cependant, si l'entreprise qui vend les données subit une attaque qui permet de faire le lien entre un profil et une personne on peut facilement se retrouver avec une gigantesque base de données qui n'est plus anonyme. De plus, si cela se réalise sur une entreprise, via l'interconnectivité des services "se connecter avec mon compte google", alors on peut acheter les données d'un autre service et être capable de le recouper à notre base de données.

- La data, au coeur des débats politiques et les Fakenews.

Comment est-ce que ces données peuvent-elles avoir autant de valeur ?  
Il y a tout d'abord l'utilisation du ciblage publicitaire à des fins moralement discutable. Comme par exemple mettre en avant un dictateur, soutenir une guerre, favoriser un candidat à des élections en montrant des fakenews nuisant aux adversaires.  
La seconde problématique réside dans les attaques au phishing : nous recevons régulièrement des mails de A..maZ00n3 ou Chr0noppost, qui ne ressemble à rien. Cependant si vous commencez à ajouter "Bonjour Mathis Schultz" puis des recommendations d'article que j'ai vraiment consulté, ainsi qu'une promotion en or, une "vente flash". ou alors si le mail indique mon numéro client ? Mes chiffres de sécurité sociale ? Il est raisonnable de penser qu'une grande part de la population se fasse avoir.

<h2 id="h3"> Sprint 2 </h2>

**Les stratégies des géants du numérique (l'inter-connectivité, la complexification et la centralisation de la data)**

- Des Objets toujours plus connecté
- Des systèmes impossible à sonder (IA) ?
- Qui utilise et possède de la donnée ?
- Cloud VS On premise
- Payer ? Un moyen de se soustraire à la donnée ?

**Les bonnes pratiques des développeurs.**

- Des systèmes orienté sécurité
- La modération de la data
- La protection de l'utilisateur

**Les bonnes pratiques des utilisateurs.**

- les gestionnaires de mdp ? Une vraie solution ?
- Le rôle des VPN ?
- Quelques outils pour se protéger

<h2 id="h4"> Conclusion </h2>

<h2 id="liens"> Liens utiles </h2>

● Le site de l’[ANSSI](https://cyber.gouv.fr) avec des ressources en français, et en particulier le guide d’hygiène informatique, utile pour connaître les sujets de sécurité les plus critiques à mettre en œuvre pour une organisation, ou tout document de la catégorie bonnes pratiques ;
● Le site [cybermalveillance.gouv.fr](https://www.cybermalveillance.gouv.fr) fournit des conseils et des informations pour se protéger contre les cyberattaques et savoir y réagir ;
● Le site de l’[ENISA](https://www.enisa.europa.eu) avec des ressources disponibles en français et de nombreuses langues européennes ;
● Le site du [NCSC](https://www.ncsc.gov.uk) avec des ressources disponibles uniquement en anglais ;
● Le site du [CCB](https://ccb.belgium.be/fr) avec des ressources disponibles en français et anglais ;
● Le site du [CISA](https://www.cisa.gov) avec des ressources disponibles uniquement en anglais.
[Open Classroom 1](https://openclassrooms.com/fr/courses/8028761-decouvrez-lunivers-de-la-cybersecurite)
[Open Classroom 2](https://openclassrooms.com/fr/courses/1757741-securisez-vos-donnees-avec-la-cryptographie)