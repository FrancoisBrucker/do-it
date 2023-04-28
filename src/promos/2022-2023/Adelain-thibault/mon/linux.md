---
layout: layout/mon.njk

title: "Linux : Linux Essentials"
authors:
  - Thibault Adelain

date: 2023-03-23

tags:
  - 'temps 3'
  - 'linux' 
  - 'formation'
---

<!-- début résumé -->
- Linux : Linux Essentials
- Niveau : débutant
<!-- fin résumé -->

Lien de la formation :

- <https://www.netacad.com/courses/os-it/ndg-linux-essentials>
- <https://www.netdevgroup.com/online/courses/linux/linux-essentials>

Pour ce MON, j'ai choisi de réaliser une formation Linux élaborée par le [*Network Development Group (NDG)*](https://www.netdevgroup.com/). Cette formation est accessible gratuitement sur leur [site](https://www.netdevgroup.com/online/courses/linux/linux-essentials) ou sur [*Cisco Networking Academy*](https://www.netacad.com/courses/os-it/ndg-linux-essentials).

## Motivation

Il est important d'apprendre les bases des systèmes Linux pour de nombreuses carrières. En particulier, en cybersécurité :

- De nombreux outils de sécurité, tels que les outils d'analyse de vulnérabilité, les outils de test de pénétration et les outils de surveillance de réseau, sont disponibles uniquement sur des plates-formes Linux.
- Les systèmes Linux sont généralement considérés comme plus sécurisés que les systèmes d'exploitation Windows en raison de leur architecture robuste.
- Les serveurs et les équipements réseaux sont souvent sous Linux, donc l'administration et la sécurisation nécessite des compétences sur cet OS.
- Les systèmes Linux offrent une grande flexibilité et une personnalisation approfondie et donc permettent de sécurisé son environnement de travail au besoin.
- ...

Mais la formation s'applique à tous les métiers utilisant linux de près ou de loin.

## Présentation de la formation

Cette formation balaye toutes les bases de Linux. Elle a pour but d'enseigner les compétences minimales nécessaires à des carrières en rapport avec le réseau, le développement logiciel ou l'administration système Linux. Ce cours s'aligne sur le *Linux Essentials Professional Development Certificate* de [LPI](https://www.lpi.org/our-certifications/linux-essentials-overview).

Ce cours comporte 18 chapitres, dont chacun comporte un lab et un exam. Il y a en plus un mid-exam + exam final. Vous avez accès a une VM Linux en permanence pour le cours ce qui permet de s'exercer en permanence.

La formation est en anglais.

## Ressenti

Cette formation est dense et riche d'informations (dure normalement 70 heures). Heureusement, beaucoup des notions m'étaient déjà familières et j'ai pu rapidement passer sur le début.

J'ai trouvé surtout intéressant la deuxième partie, après le middle-exam, en particulier :

- Scripting. Je vous renvoie au MON de Thomas sur [bash](https://francoisbrucker.github.io/do-it/mon/TP/mons/bash/).
- Computer hardware : *"En gardant les machines virtuelles à l'esprit, il est impératif de comprendre ce qui constitue le matériel physique d'un ordinateur. Si vous ne comprenez pas quels sont les composants d'un ordinateur, comment ils sont intégrés et communiquent entre eux, et comment un ordinateur doit fonctionner, vous ne pouvez pas installer, configurer, administrer, sécuriser ou dépanner correctement un système."*
- Where data is stored : gestion des processus, de la mémoire, des partitions.
- Network configuration : commandes et fichiers de configuration réseau.
- Users : gestion des utilisateurs.
- Ownership and Permissions + Special directories and files : permissions, setuid, setgid, stickybit, *hard links / soft links*.

### Source

- <https://www.netdevgroup.com/online/courses/linux/linux-essentials>
