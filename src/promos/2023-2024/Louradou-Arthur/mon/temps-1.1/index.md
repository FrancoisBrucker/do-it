---
layout: layout/mon.njk

title: "Pentest et Cybersécurité"
authors:
  - Arthur Louradou

date: 2023-09-27

tags: 
  - "temps 1"
  - "cyber"
  - "pentest"
  - "security"
  - "web"
  - "sql"
  - "injection"

résumé: "Ce MON détaillera le parcours d'un développeur qui souhaite en apprendre plus sur la sécurité des applications qu'il déploie."
---

<br />
{% attention "*Disclaimer*" %}

 Ce projet d'autoformation traite de cybersécurité.
 Les informations fournies dans cette page sont adressées à des fins éducatives uniquement. Il est essentiel de respecter les lois locales et d'obtenir l'accord du propriétaire de la machine cible avant d'entreprendre toute activité de pentest ou de hacking. L'autoformation en cybersécurité doit être entreprise de manière éthique et légale, dans le respect de la vie privée et de la propriété intellectuelle d'autrui.

{% endattention %}

## Table des matières
- [Objectifs](#objectifs)
- [Prérequis et documentation préalable](#prerequis)
- [Openclassrooms - Réalisez un test d'intrusion web](#mooc)
  - [Introduction](#mooc-intro)
  - [Posture du Pentester & Éthique du Hacker](#mooc-posture)
  - [Cadrage du besoin de test d’intrusion](#mooc-cadrage)
  - [Environnement de travail](#mooc-environnement)
  - [Techniques](#mooc-techniques)
  - [Chiffrement, Cryptographie](#mooc-chiffrement)
  - [Protocoles et Suites de Chiffrement](#mooc-protocoles)
  - [Utilisation d’un Proxy d’Interception](#mooc-proxy)
  - [Attaques par Dictionnaire](#mooc-dictionnaire)
  - [Pour finir sur le MOOC](#mooc-conclusion)
- [Autres MONs](#intralinks)
- [Regard critique et ouverture](#ouverture)
- [Ce que j’ai appris durant ce MON](#conclusions)

## Objectifs du MON { #objectifs }

Ce premier MON de l’année portera sur la cybersécurité et plus particulièrement sur le Pentest (test de pénétration). Initialement, l’objectif est d’effectuer des exercices pratiques sur des plateformes en ligne comme HackTheBox ou Root-Me, qui sont des bons moyens de se former dans le domaine de la cybersécurité par la pratique et de façon autodidacte. Nous affinerons par ailleurs le besoin en se documentant sur le sujet du MON. Ainsi, mes différentes lectures m’ont mis sur la voie d’un MOOC d’Openclassrooms dont la lecture et l’intégration m’a permis de mieux cerner les besoins de l’exercice.

Le cours Openclassrooms contient différents sujets tels que le test d'intrusion, la posture du pentester, la reconnaissance active, l'utilisation de Nmap, les recherches d'exploits, le chiffrement et la cryptographie ou encore l'attaque d'une application web.

Je complèterai les outils apportés par le cours de lectures d’autres MONs *(le mot MON s’accorde-t-il ?)* d’élèves d’années précédentes et des parties qui me paraissent pertinentes.

Finalement, je prendrai soin d’adopter une posture critique sur les acquis de ce MON à l’issue de celui-ci pour recommander ou non au lecteur de ce lancer dans cette démarche.

C’est parti ? 😉

## Prérequis et documentation préalable { #prerequis }

Pour donner un ordre d’idée du niveau nécessaire à la lecture de ce document, il ne nécessite pas de connaissances en cybersécurité mais une appétence pour le monde Linux et surtout pas de réticence pour la ligne de commande ! Il intéressera les développeurs désireux d’en savoir plus sur leur environnement de travail et il sensibilisera aux enjeux de la cyber dans les entreprises.

J’ai cherché des ressources intéressantes avant de faire mes recherches sur la cybersécurité. L’objectif de ce MON est initialement de s’entrainer sur des plateformes pour obtenir des outils et connaitre les vecteurs d’attaque. Cet objectif est partiellement rempli par le MOOC d’Openclassrooms puisqu’il intègre une partie pratique sur Root-Me nécessitant l’installation de Kali Linux sur une machine virtuelle. C’est aussi pour avoir une vision plus professionnelle du métier de pentester que ce cours semble utile. Alors lançons nous ! Je vais résumer dans la suite de ce document ma prise de note en sélectionnant les parties les plus utiles d’un point de vue technique.

## Openclassrooms - Réalisez un test d'intrusion web { #mooc }

{% info %}
La partie qui suit va résumer une prise de note du cours d'OpenClassrooms que vous pourrez retrouver ici : [Prise de note Openclassrooms](./prise_de_note_oc).
{% endinfo %}

### Introduction { #mooc-intro }

Le test d'intrusion, également connu sous le nom de Pentest, constitue une composante essentielle de la sécurité informatique. Il vise à évaluer la sécurité d'un système ou d'une application. Une analogie courante consiste à considérer les différentes approches de test en termes de niveaux de connaissance, tels que la boîte noire, la boîte grise et la boîte blanche.

Il existe plusieurs méthodes pour tester la sécurité d'un système, dont le "bug bounty", la "red team", et le "test d'intrusion".

### Posture du Pentester & Éthique du Hacker { #mooc-posture }

Il est essentiel de comprendre que le terme "hacker" ne se réfère pas nécessairement à des intentions malveillantes. Les pentesters adoptent une approche créative et réfléchie pour identifier les vulnérabilités d'un système. Dans le cadre de ce cours, toutes les activités sont menées de manière légale, à condition qu'elles soient effectuées avec l'autorisation appropriée.

La qualité principale d'un pentester est l'autodidaxie, c'est-à-dire la capacité à apprendre de manière autonome. Cette compétence est particulièrement valorisée et recherchée par les professionnels de la sécurité informatique, et elle est étroitement surveillée par les MON de Do_It !

N'hésitez pas à me fournir la suite de vos notes si vous souhaitez que je les convertisse également en Markdown.

### Cadrage du besoin de test d’intrusion _(skip)_ { #mooc-cadrage }

<aside>
🧑🏻‍💻 À ce stade, il me parait assez prématuré de parler de client, organisation et budget sans même avoir développé de compétences techniques. Je vais donc avancer dans le cours pour passer aux parties les plus intéressantes pour les objectifs de ce MON.

</aside>

### Environnement de travail { #mooc-environnement }

{% info %}
Conseil : Prendre des notes de tout ce que l’on fait pour la traçabilité et se couvrir légalement.

{% endinfo %}

Par le passé, j'avais commencé à prendre des notes sur les outils utilisés avec HackTheBox. Cela inclut l'installation de Kali Linux, la mise à jour de VirtualBox, et le démarrage de la machine déjà installée.

### Techniques { #mooc-techniques }

#### Google Dorks

Les Google Dorks sont des techniques de recherche en source ouverte utilisées pour vérifier si des mots de passe ou des jetons ne sont pas exposés dans des documents publics sur Internet. Il est possible de raffiner ces recherches en utilisant des mots clés spécifiques, tels que `site:root-me.org`, `ext:pdf`, ou `"password"`. Vous pouvez recenser les failles trouvées dans Google en visitant https://www.exploit-db.com/google-hacking-database.

#### OSINT (Renseignement en Source Ouverte)

L'OSINT, ou renseignement en source ouverte, implique la recherche d'informations à partir de sources accessibles publiquement. Cela peut inclure la recherche d'adresses e-mail, de domaines, la consultation de dépôts Github, ou la détection de fuites de bases de données. Cette tâche peut être effectuée manuellement ou à l'aide d'outils spécialisés tels que [theHarvester](https://github.com/laramies/theHarvester), [recon-ng](https://github.com/lanmaster53/recon-ng), et des recherches plus approfondies sur le Darknet.

Un autre outil utile que j'avais déjà utilisé pour des recherches sur moi-même est [epieos.com](https://epieos.com/), qui permet de retrouver tous les comptes associés à une adresse e-mail ou à un numéro de téléphone.

#### Reconnaissance Active

La reconnaissance active implique l'utilisation d'outils techniques pour explorer plus en profondeur le système d'information d'une entreprise. Cela comprend l'examen du registre whois, l'énumération des domaines, le grattage des URL trouvées dans chaque domaine, l'analyse des certificats TLS (Transport Layer Security), et la vérification de l'historique DNS.

Un outil complet pour l'exploration est [OWASP Amass](https://github.com/OWASP/Amass) d'OWASP, disponible sur Kali Linux.

#### Nmap

{% note %}

Ayant déjà utilisé Nmap, cette partie a peut-être un niveau de difficulté plus important puisque je ne détaille pas son fonctionnement. Vous pouvez vous référer [au chapitre](https://openclassrooms.com/fr/courses/7727176-realisez-un-test-dintrusion-web/7916261-identifiez-les-points-d-entree-sur-le-serveur-cible-sous-jacent) pour en savoir plus.

{% endnote %}

- **Sans paramètre (= Scan SYN) :**
  1. Résout le nom DNS de l'hôte.
  2. Ping l'hôte.
  3. Si l'hôte répond, réalise un “SYN scan”.
  4. Ne scanne que les 1 000 premiers ports les plus connus sur les 65 535 possibles.
  5. Ne fait pas de détection du service en écoute.

{% info %}
N’envoie qu’un paquet SYN et attend la réponse SYN+ACK.
N’envoie jamais le ACK ou le RST.
La connexion reste donc ouverte chez le serveur, jusqu’au timeout !
{% endinfo %}

- **Option `-p` :** Scan des ports dans une plage de 0-65535
- **Option `-sV` :** Vérifie le service en écoute et sa version
- **Option `-oA` :** Pour enregistrer les résultats dans un format spécifique, dans l’exemple `-oA metasploit2`.

Il conviendrait de mettre en pratique les différentes options de Nmap car cet outil est à la base de toute investigation en pentest.

#### Recherche des exploits à l’issue du scan

Dans un premier temps, vous pouvez effectuer des recherches avec Google.

Ensuite, vous pouvez utiliser des outils spécialisés tels que [CVE Mitre](https://cve.mitre.org/index.html) ou [CVE Details](https://www.cvedetails.com/) qui fournissent des détails sur les CVE (Common Vulnerability Exposure) répertoriées.

{% info %}
**UTM (Unified Threat Management) :**
Logiciel qui peut fausser le résultat des scans lorsqu’ils détectent qu’ils sont scannés, entre autres !
{% endinfo %}

### Chiffrement, Cryptographie { #mooc-chiffrement }
#### Communication TLS

La communication TLS (Transport Layer Security) représente les échanges sécurisés entre un client et un serveur. Elle est essentielle pour garantir la confidentialité et l'intégrité des données transitant sur le réseau.

<img src="https://user.oc-static.com/upload/2022/07/21/16584160662712_FR_7727176_Intrusion-Web_Static-Assets_p2c4-1a.png" width="450px" alt="Schéma HTTPS">


#### Failles dans le Chiffrement

Lors de l'évaluation de la sécurité, il est crucial de rechercher d'éventuelles failles dans le chiffrement.

#### Outils pour l'Évaluation du Chiffrement

Pour évaluer le chiffrement, plusieurs outils sont disponibles :

- [SSL Labs](https://www.ssllabs.com/ssltest/)
- [sslscan](https://github.com/rbsec/sslscan)
- [testssl.sh](https://github.com/drwetter/testssl.sh)

Ces outils permettent d'analyser la sécurité de la communication TLS et d'identifier les éventuelles vulnérabilités.

### Protocoles et Suites de Chiffrement { #mooc-protocoles }

#### Définitions

Il existe plusieurs protocoles de chiffrement utilisés dans la communication HTTPS, tels que SSL v2, SSL v3, TLS v1.0, TLS v1.1, TLS v1.2 et TLS v1.3. Cependant, seuls certains sont recommandés pour une utilisation sécurisée.

Chaque protocole dispose d'une liste de suites de chiffrement compatibles, suivant ce format :

`<algorithme d'échange de clé>-<algorithme d'authentification>-<algorithme de chiffrement symétrique et taille de clé>-<algorithme de signature>`

Par exemple : `ECDHE-RSA-AES128-GCM-SHA256`

- `ECDHE` est utilisé pour l'échange de clés.
- `RSA` est employé pour l'authentification.
- `AES-128` est le chiffrement symétrique utilisé.
- `GCM` représente le mode d'opération du chiffrement par bloc.
- `SHA-256` est l'algorithme de signature.

#### Installation et Utilisation de SSLscan

Si vous souhaitez utiliser SSLscan, vous pouvez suivre ces étapes :

1. Clonez le projet depuis Github.
2. Lisez la documentation fournie pour comprendre comment utiliser l'outil.

Dans un exemple de test réalisé sur root-me, il a été observé que tous les protocoles utilisés étaient anciens et vulnérables. Il est recommandé de mettre à jour OpenSSL sur le serveur vulnérable pour renforcer la sécurité.

### Utilisation d’un Proxy d’Interception { #mooc-proxy }

Un proxy d'interception, similaire à un VPN, est chargé de surveiller le trafic réseau vers l'application que vous analysez. Un outil utile pour cela est **Burp Suite Community**.

{% info "Installation" %}

Consultez le tutoriel pour configurer le proxy. Ensuite, regardez des vidéos tutorielles sur l'outil pour comprendre comment le configurer et découvrir ses fonctionnalités.

{% endinfo %}

Onglets utiles : Intruder pour automatiser les requêtes et mener plusieurs fois la même attaque dans le scope, Repeater pour rejouer une requête avec des paramètres différents.

J’ai pu utiliser l'outil Intruder avec un dictionnaire de chemins courants (index, index.php, …) pour tester un à un tous ces chemins et réussir le challenge disponible à l'adresse : [Root-Me Challenge](https://www.root-me.org/fr/Challenges/Web-Serveur/Fichier-de-sauvegarde)

### Attaques par Dictionnaire { #mooc-dictionnaire }

Outil : [SecLists](https://github.com/danielmiessler/SecLists)

Après l'installation avec `sudo apt install seclists`, vous aurez accès à des listes de dictionnaires dans le répertoire `/usr/share/seclists/`.

De nombreuses listes de dictionnaires sont disponibles sur Internet, comme celles utilisées dans le précédent challenge : [Liste de Dictionnaires](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/PHP.fuzz.txt)


### Pour finir sur le MOOC { #mooc-conclusion }

J’ai fais le choix de dévier du cours d’Openclassrooms pour peaufiner les recherches sur d’autres supports concernant le Pentest et la cybersécurité, et faire quelques chalenges sur HackTheBox.

Je terminerai ce cours sur mon temps libre car il reste du contenu qui semble intéressant à parcourir ainsi que d’autres outils à découvrir.

## Autres MONs { #intralinks }

Après avoir parcouru le travail des années précédentes, je recommande chaudement [le MON de Jean-Baptiste sur les injections SQL](../../../../2022-2023/Durand-Jean-Baptiste/mon/SQLinjection) ! Il détaille notamment [comment installer Burpsuite](../../../../2022-2023/Durand-Jean-Baptiste/mon/SQLinjection/#h3) et donne des liens vers WebSecurityAcademy pour tester des attaques par injection SQL.

## Regard critique et ouverture { #ouverture }

Finalement, ce premier MON a été une expérimentation du travail d’auto-formation sur un sujet méconnu ou étudié en surface par le passé pour ma part.

L’objectif initial était de faire un maximum d’exercices pratiques sur des machines distantes. À mon sens, les 10h consacrées à ce projet de formation n’ont pas suffit à intégrer de façon durable des connaissances. J’entends pas là : graver ces connaissances en mémoire à long terme. En revanche, en travaillant sur le MOOC, j’ai pu découvrir plusieurs choses. D’abord, des outils qui seront utiles pour la réalisation de pentests dans le futur à la relecture de ces notes. Ensuite, un point de vue de professionnel du secteur expliquant son métier avec tout le recul imposer par le fait de donner cours à des néophytes.

Pour terminer, les risques cyber sont de plus en plus pris au sérieux par les entreprises, mais sont encore sous estimés à l’échelle individuelle. Mes dernières lectures m’ont conduit au visionnage de plusieurs vidéos que je souhaite partager pour la sensibilisation à ces enjeux. La première traite de la criticité des failles dans les systèmes de Microsoft et la seconde détaille une attaque gouvernementale menée par le passé et analysée par la communauté de hacking mondiale.
* [Youtube : Microsoft menace la sécurité nationale](https://www.youtube.com/watch?v=v66YDx7U6V0)
* [Youtube : Comment hacker une centrale nucléaire ?](https://www.youtube.com/watch?v=iW1w3WSpBLI)

Voici enfin une excellente chaine Youtube de vulgarisation sur les sujets cyber : [Waked XY](https://www.youtube.com/@wakedxy).

## Ce que j’ai appris durant ce MON { #conclusions }

- Apprendre a propos d’un sujet en auto-formation
- La vision d’un pentester et sa relation avec un client (peu présenté dans cette restitution car plus éloigné des objectifs du MON)
- Des outils techniques utilisables avec Kali Linux, documentés durant cette prise de note
- Une mise en pratique avec des cas concrets
- Que le pentest est un domaine extrêmement large, qui n’est qu’une partie de la cybersécurité
