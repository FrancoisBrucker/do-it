---
layout: layout/mon.njk

title: "Pentest : environnement et outils"
authors:
  - Thibault Adelain

date: 2023-01-04

tags:
  - 'temps 2'
  - 'pentest'
  - 'securite informatique'
  - 'hacking'
---

<!-- début résumé -->
- Pentest : environnement et outils
- Niveau : débutant à intermédiaire

<!-- fin résumé -->

Rappel : Il faut avoir l'accord de la personne cible pour réaliser un pentest. Il faut s'en tenir à des pratiques éthiques et de ne pas utiliser ses connaissances pour causer des dommages ou enfreindre la loi.

## Pentest

Afin d'améliorer ses compétences en sécurité informatique, il est important d'avoir des connaissances défensives (comment se protéger face aux attaques), mais également offensives (comment attaquer un système). En effet, pour mieux comprendre comment protéger un système, il est primordial de connaître les vulnérabilités des systèmes et les méthodes d'attaque des hackers.

Ce MON est dédier à la mise en place d'un environnement pour réaliser des tests de pénétrations. Il nous permettra de pénétrer des systèmes en toute légalité, et d'améliorer nos compétences sans causer de tord à personne. Ainsi, nous pourrons mieux comprendre la méthodologie des hackers et apprendre de nombreuses méthodes de sécurisation des systèmes.

### Environnement : Machine virtuelle (VM), VirtualBox et autres...

Il va nous falloir mettre en place deux machines virtuelles : une VM attaquant, et une VM cible.

Il y a plusieurs raisons d'utiliser des machines virtuelles pour notre environnement de hacking. En voici quelques-unes :  

- Sécurité par l'isolation: en utilisant une machine virtuelle, nous pouvons créer un système d'exploitation "cible" séparé de notre ordinateur hôte, ce qui permet de mieux isoler les tests et d'éviter que les résultats ne soient influencés par des logiciels ou des paramètres sur notre machine hôte. Réciproquement, la machine virtuelle "cible", victime de l'attaque, peut également parfois contrer les attaques, et ainsi endommager la machine de l'attaquant, d'où l'importance d'avoir une VM attaquant et une VM cible. Cela permet de protéger notre  ordinateur et de ne pas causer de dommages à d'autres systèmes ou réseaux. De plus, nous pourrons isoler notre environnement de hacking sur un réseau virtuel, afin qu'aucune machine extérieure puisse influencer notre environnement.
- Plus généralement : Facilité de configuration des VM, coût (pas besoin d'acheter des ordinateurs), choix d'allocation des ressources...

Il existe plusieurs logiciels pour mettre en place des machines virtuelles sur sa machine. Parmi eux :

- La suite VMware.
- VirtualBox (open source).

Pour ce tuto, nous allons utiliser VirtualBox. VirtualBox est un hyperviseur de type 2, c'est à dire qu'il doit être installé sur un système d'exploitation hôte (l'OS de notre machine); cela qui va nous faciliter la tâche.

Suivez ce [tuto](https://www.youtube.com/watch?v=wX75Z-4MEoM&t=725s&ab_channel=NetworkChuck)  pour installer VirtualBox, ainsi que l'OS [Kali Linux](https://www.kali.org/) pour notre VM attaquant. Pourquoi une VM Kali Linux ? Tout simplement car elle aura des logiciels déjà préinstallés servant pour le hacking.

Cette VM sera notre machine de hacking : c'est avec elle que nous allons procéder à l'attaque.

Ensuite, il faut set-up la machine cible. Tout est expliquer dans ce [tuto](https://www.youtube.com/watch?v=mvsiuLzpx2E&ab_channel=NetworkChuck). Ce tuto nous propose une machine cible "[MrRobot](https://www.vulnhub.com/entry/mr-robot-1,151/)" disponible sur VulnHub.

VulnHub est un site Web qui fournit des machines virtuelles pré-configurées contenant des vulnérabilités de sécurité connues. Attention toutefois, les VM sont proposées par la communauté, il faut donc s'assurer qu'elles soient fiables avant de les installer. Pour vous aider à trouver les vulnérabilités, la communauté propose des commentaires, walkthrough...

Finalement, on a crée un environnement de hacking complétement isolé de tout réseau extérieur, avec une machine attaquant et une machine cible. On peut maintenant s'entraîner au pentest.

### Outils utiles pour le pentest

#### Phases d'un pentest

Les tests de pénétration sont généralement effectués en suivant plusieurs étapes. Souvent, les phases sont les suivantes :

- Reconnaissance: la phase de reconnaissance consiste à recueillir des informations sur la cible : adresse IP, nom de domaine, les ports ouverts, les services en fonctionnement... Cette étape peut être effectuée en utilisant des outils tels que [nmap](https://nmap.org/), outils d'OSINT ([Sublist3r](https://github.com/aboul3la/sublist3r))... Cette étape est cruciale et constitue une partie importante du pentest : plus on aura d'information sur la cible, plus l'angle d'attaque sera facile à définir.
- Scanning: la phase de scanning consiste à analyser en profondeur la cible pour identifier les vulnérabilités potentielles. Des outils comme nmap permettent de détecter des vulnérabilités, [Sqlmap](https://sqlmap.org/) pour les injections SQL...
- Exploitation: la phase d'exploitation consiste à utiliser les vulnérabilités identifiées pour accéder au système cible de manière non autorisée.
- Post-exploitation : vol de données, installation de logiciel malveillant, installation d'une backdoor... Cette phase n'est pas forcément effectué lors d'un pentest éthique, car lorsque l'on a accès au système, nous n'avons pas à réaliser d'actions malveillantes sur le client.
- Rapport au client.

#### Outils

Quelques outils proposés par Kasimir : <https://francoisbrucker.github.io/do-it/pok/KR/POK2/hacking/>

##### Maîtriser l'environnement Linux

Bien que Linux ne soit pas le seul système d'exploitation utilisé pour les serveurs, il est très populaire en raison de ses nombreux avantages en matière de stabilité, de sécurité, de personnalisation (distributions) et de coût (open source). Maîtriser l'environnement Linux est donc un atout pour le hacker éthique car cela lui permettra d'acquérir des connaissances utiles pour mener à bien ses tests de pénétrations. Par exemple, voici une suite de [tuto](https://www.youtube.com/playlist?list=PLIhvC56v63IJIujb5cyE13oLuyORZpdkL) pour débuter.

##### Nmap

[Nmap](https://nmap.org/) (Network Mapper) est un outil de sécurité informatique open source utilisé pour analyser les réseaux et les systèmes d'exploitation. Il permet de voir quels sont les hôtes actifs sur un réseau, de déterminer les services offerts par ces hôtes (les ports ouverts) et de détecter les vulnérabilités potentielles.

Avoir une information sur les ports est très utile pour savoir quelle service offre la machine cible : 80 ou 443 (http ou https => sûrement un server web), 22 (ssh => shell accessible à distance)...

Également, Nmap permet d'avoir des informations sur l'OS de la machine, les versions...

##### SqlMap

[Sqlmap](https://sqlmap.org/) est un outil open source de sécurité informatique utilisé pour détecter et exploiter les vulnérabilités d'injection SQL.

##### Wireshark

[Wireshark](https://www.wireshark.org/) est un logiciel open source de capture et d'analyse de trafic réseau. Il permet de capturer et d'afficher en temps réel le trafic réseau sur un ordinateur ou sur un réseau.

Wireshark est souvent utilisé par les administrateurs de réseau pour diagnostiquer et résoudre les problèmes de réseau, par les développeurs pour analyser et déboguer les applications réseau, mais aussi dans sécurité informatique pour analyser la sécurité des réseaux, les flux de données...

Il peut servir notamment a "espionner" un réseau (network sniffing) pour écouter les communications wifi non chiffrées.

#### Pour apprendre

CTF ([Rootme](https://www.root-me.org/), [HackTheBox](https://www.hackthebox.com/)...)

[VulHub](https://www.vulnhub.com/) pour télécharger sa VM cible et s'entraîner.

[Portswigger](https://portswigger.net/web-security) permet d'améliorer ses compétences en sécurité web / test de pénétrations web.

N'hésitez pas à explorer vous mêmes d'autres outils : l'univers du hacking est vaste et des méthodes sont créées tous les jours.

## Sources

[1] : The Ultimate Kali Linux Book: Perform Advanced Penetration Testing Using Nmap, Metasploit, Aircrack-ng, and Empire. By Glen D. Singh.