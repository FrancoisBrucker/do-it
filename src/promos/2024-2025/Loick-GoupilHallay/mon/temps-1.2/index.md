---
layout: layout/mon.njk

title: "La sécurisation de l'environnement de développement"
authors:
  - Loïck Goupil-Hallay

date: 2024-10-13

tags:
  - 'temps 1'
  - 'dev'
  - 'cyber'
---

{%prerequis 'MON avancé'%}
- [L'environnement de développement idéal](../temps-1.1/)
- Réseau
{%endprerequis%}

{% lien %}
- [ANSSI](https://cyber.gouv.fr)
- [POK déploiement automatisé de l'environnement de développement pour une équipe](../../pok/temps-1/)
{% endlien %}

<script type="module">
  // Mermaid configuration
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true });
</script>
<style>
  section.optional {
    background-color: #f9f9f9;
    border-left: 4px solid #ccc;
    padding-left: 1em;
  }
  img.icon {
    width: 45px;
    height: 45px;
    border: none;
  }
  img.banner {
    width: min(45vw, 300px);
    border: none;
  }
</style>

## Table des matières<a name="table-des-matières"></a>
1. [Introduction](#introduction)
2. [Durcissement du poste de travail](#durcissement-du-poste-de-travail)
    1. [Durcissement Hardware](#durcissement-hardware)
        1. [BIOS/UEFI](#bios-uefi)
        2. [Chiffrement du disque dur](#chiffrement-du-disque-dur)
        3. [Authentification forte](#authentification-forte)
    2. [Durcissement du système d'exploitation](#durcissement-du-système-dexploitation)
        1. [Configuration bootloader & kernel](#configuration-bootloader-kernel)
        2. [Mises à jours](#mises-à-jour)
        3. [SSH, Réseau & firewall](#ssh-réseau-firewall)
        4. [Gestion des comptes utilisateurs](#gestion-des-comptes-utilisateurs)
            1. Mots de passe forts
            2. Niveaux de privilèges
3. [Zero Trust](#zero-trust)
    1. [Moindre privilège](#moindre-privilège)
    2. [Sécurisation des accès](#sécurisation-des-accès)
    3. [Sécurisation des flux](#sécurisation-des-flux)
4. [Former les développeurs](#former-les-développeurs)
    1. [Chiffrement](#chiffrement)
    2. [Gestion des secrets](#gestion-des-secrets)
    3. [Supply Chain & Dépendences vulnérables](#supply-chain)
    4. [Secure Coding](#secure-coding)
    5. [Logging & Monitoring](#logging-monitoring)
    6. [Réponse aux incidents](#réponse-aux-incidents)
    7. [Risques légaux](#risques-légaux)
5. [Réseau](#réseau)
    1. [TLS](#tls)
    2. [Proxy](#proxy)
    3. [Firewall](#firewall)
6. [Conclusion](#conclusion)
7. [Lexique](#lexique)

## Introduction<a name="introduction"></a>
La sécurisation de l'environnement de développement est un enjeu majeur pour les entreprises. Les **piratages informatiques** et **brèches de données** sont des risques réels qui ont des conséquences désastreuses en terme <u>financier</u>, de risques <u>légaux</u> mais surtout en terme de <u>réputation</u>.

Les développeurs manipulent des **données sensibles** et des **outils critiques** pour l'entreprise. Le plus souvent ces données sont manipulées "automatiquement" par les programmmes, publiées sur des dépôts, stockées dans des bases de données... Le développeur ne les voit pas directement mais elles sont bien présentes et sont des cibles.

Il est essentiel de sensibiliser les développeurs à la sécurité informatique et de mettre en place des mesures pour protéger les données et les outils de développement.

<section class="optional">

## Durcissement du poste de travail<a name="durcissement-du-poste-de-travail"></a>
<p style="background-color: #ffb1a8; border: 2px solid #ba1300; padding: 10px; border-radius: 10px">
<em>Cette section sert uniquement pour votre culture personnelle.</em><br>
Vous trouverez ici une liste de recommandations basées sur les recommandations de l'ANSSI pour sécuriser un poste de travail.
</p>
Le poste de travail du développeur est une cible privilégiée pour les attaquants. Il est l'un des vecteurs d'attaque les plus courants, car les erreurs sont souvent humaines lorsqu'un piratage est réalisé.

Il existe des guides pour chaque système d'exploitation publiés par des organismes de sécurité informatique. Par exemple, l'ANSSI publie des guides de bonnes pratiques pour la sécurité des systèmes d'information:
- [Linux](https://cyber.gouv.fr/publications/configuration-recommendations-gnulinux-system)
- [Windows](https://cyber.gouv.fr/sites/default/files/2022-09/anssi-guide-recommandations_securite_journalisation_systemes_microsoft_windows_environnement_active_directory.pdf)

Voyons ensemble quelques bonnes pratiques pour **durcir** le poste de travail.

### Durcissement Hardware<a name="durcissement-hardware"></a>
La première étape pour sécuriser un poste de travail est de **s'assurer que le matériel est sécurisé**. Voici quelques bonnes pratiques pour sécuriser le matériel dès le départ

#### BIOS/UEFI<a name="bios-uefi"></a>
Le BIOS/UEFI est le premier logiciel qui s'exécute lors du démarrage de l'ordinateur. Vous pouvez y accéder en appuyant sur une touche spécifique propre à chaque constructeur (F2, F10, F12, DEL...) au démarrage.

Il est essentiel de **protéger le BIOS/UEFI** pour empêcher les attaquants de le modifier. Pour se faire, il est recommandé de:
- **définir un mot de passe** pour accéder au BIOS/UEFI
- **désactiver le démarrage sur les périphériques amovibles**
- **activer le Secure Boot** pour empêcher le démarrage de logiciels non signés / non autorisés
- **mettre à jour le BIOS/UEFI** régulièrement

#### Chiffrement du disque dur<a name="chiffrement-du-disque-dur"></a>
Le chiffrement consiste à **protéger les données** en les transformant en un format illisible sans la clé de déchiffrement. Il est recommandé de **chiffrer le disque dur** pour protéger les données en cas de vol ou de perte de l'ordinateur. Le chiffrement peut être réalisé avec des outils comme BitLocker (Windows) ou FileVault (macOS) ou LUKS (Linux).

Le disque dur chiffré <u>nécessite</u> un mot de passe pour être déverrouillé, il est essentiel de choisir un **mot de passe fort** ET de ne pas l'oublier, car il est <u>impossible</u> de récupérer les données sans lui. Le chiffrement est généralement réalisé durant l'installation du système d'exploitation, car il est <u>difficile de chiffrer un disque dur déjà utilisé sans perdre les données</u>.

#### Authentification forte<a name="authentification-forte"></a>
L'authentification forte consiste à **utiliser plusieurs facteurs d'authentification** pour se connecter à un système. Par exemple, un mot de passe et un code envoyé par SMS. Le deuxième facteur d'authentification peut aussi être un élément physique comme une clé USB ou un token.

Les systèmes d'exploitation modernes proposent des solutions d'authentification forte comme [Windows Hello](https://www.microsoft.com/fr-fr/windows/tips/windows-hello) (reconnaissance faciale) ou [Touch ID](https://support.apple.com/fr-fr/105095) (reconnaissance d'empreinte digitale). Les éléments physiques comme les clés USB ou les tokens sont souvent utilisés pour l'authentification forte dans les entreprises. Il s'agit par exemple de la clé [YubiKey](https://www.yubico.com), de la carte à puce ou du token OTP. Tous ces éléments peuvent être déployés (longtemps) après l'installation du système d'exploitation. Ils sont souvent gérés par un service d'**authentification centralisé**.

Cette méthode est **plus sécurisée** que l'authentification par mot de passe seul, car il est plus difficile pour un attaquant de compromettre plusieurs facteurs d'authentification. Cependant elle peut générer de la **frustration** et être **contraignante** pour les utilisateurs.

### Durcissement du système d'exploitation<a name="durcissement-du-système-dexploitation"></a>
Le système d'exploitation est le logiciel qui permet à un ordinateur de fonctionner. Il est essentiel de **sécuriser le système d'exploitation** pour protéger les données et les outils de développement des accès non autorisés.

#### Configuration bootloader & kernel<a name="configuration-bootloader-kernel"></a>
Il est recommandé de **configurer le bootloader** pour empêcher les modifications non autorisées du système d'exploitation. Par exemple, il est possible de **désactiver le mode de récupération** pour empêcher les attaquants de contourner les mesures de sécurité.

Il est également recommandé de **configurer le kernel** pour limiter les attaques de type **Kernel Exploit**. Notamment, il est recommandé de **désactiver les modules non utilisés** pour réduire la surface d'attaque.

Nous n'entrerons pas dans le détail car l'application de ces mesures nécessite des compétences avancées en sécurité informatique. Vous pouvez néamoins suivre le [guide de l'ANSSI pour sécuriser un système Linux](https://cyber.gouv.fr/publications/configuration-recommendations-gnulinux-system) afin de comprendre comment sécuriser un kernel (pas seulement Linux).

#### Mises à jours<a name="mises-à-jour"></a>
L'une des premières choses à faire lorsque l'on reçoit son nouveau poste de travail est de **mettre à jour** le système d'exploitation et les logiciels installés.

Il est essentiel de **mettre à jour régulièrement** le système d'exploitation et les logiciels pour **corriger les failles de sécurité**. Les mises à jour de sécurité sont publiées régulièrement par les éditeurs de logiciels pour corriger les failles de sécurité découvertes. Il est recommandable de **configurer les mises à jour automatiques** pour s'assurer que le système est toujours à jour. Attention cependant aux [incidents de type Crowdstrike](https://en.wikipedia.org/wiki/2024_CrowdStrike-related_IT_outages) qui peuvent être causés par des mises à jour automatiques.

#### SSH, réseau & firewall<a name="ssh-réseau-firewall"></a>
Il est recommandé de **désactiver le service SSH** si vous n'en avez pas besoin. Le service SSH est souvent utilisé pour accéder à une machine à distance, mais il peut être une porte d'entrée pour les attaquants s'il est mal configuré.

Il est également recommandé de **configurer un firewall** pour contrôler le trafic réseau entrant et sortant. Un **firewall** permet de **filtrer le trafic réseau** entrantes et sortantes. Il suit des **règles de filtrage** définies par l'administrateur pour autoriser ou bloquer le trafic réseau. C'est un bon moyen d'empêcher votre extension VSCode de communiquer avec Pyongyang.

Il est enfin recommandé de **désactiver les services réseau non utilisés** pour réduire la surface d'attaque. Par exemple, si vous n'utilisez pas le service FTP (privilégiez SFTP), IPv6 ou le partage de fichiers, il est recommandé de les désactiver.

Il faut paramétrer l'IPv4 et l'IPv6 pour qu'ils soient **sécurisés** et **privés**. Il est recommandé de **désactiver l'IPv6** si vous n'en avez pas besoin, car il peut être une porte d'entrée pour les attaquants.

#### Gestion des comptes utilisateurs<a name="gestion-des-comptes-utilisateurs"></a>
La gestion des utilisateurs est un élément clé de la sécurité du système d'exploitation. Il est recommandé de **créer des comptes utilisateurs** pour chaque utilisateur et de **limiter les privilèges** des comptes utilisateurs. Il est également recommandé de **désactiver les comptes inutilisés** pour réduire la surface d'attaque.

##### Mots de passe forts
Il est essentiel de **choisir des mots de passe forts** pour les comptes utilisateurs. Un mot de passe fort est un mot de passe qui est difficile à deviner pour un attaquant. Il est recommandé d'utiliser des mots de passe longs, composés de lettres majuscules et minuscules, de chiffres et de caractères spéciaux.

L'ANSSI met régulièrement à jour son [guide d'authentification multifacteur et mots de passe](https://cyber.gouv.fr/sites/default/files/2021/10/anssi-guide-authentification_multifacteur_et_mots_de_passe.pdf) pour vous aider à choisir un bon mot de passe, robustes vis-à-vis des évolutions technologiques.

##### Niveaux de privilèges
Par défaut, les systèmes d'exploitation n'ont que 2 niveaux de privilèges: **administrateur** et **utilisateur**. Pour compléter ces niveaux, il est recommandé de **créer des groupes** pour regrouper les utilisateurs avec des privilèges similaires. Par exemple, un groupe "développeurs" pour les utilisateurs qui ont besoin d'accéder aux outils de développement.

L'idée est d'avoir le moins de véritables administrateurs possible, et de donner les privilèges les plus bas nécessaires pour effectuer le travail. C'est le principe du **moindre privilège**.

Pour les utilisateurs qui ont besoin d'un accès administrateur, il est recommandé de mettre en place un suivi des actions effectuées par ces utilisateurs pour **détecter les abus**.

#### Fichiers et répertoires<a name="fichiers-et-répertoires"></a>
Pour protéger ses données, il est recommandé de **chiffrer les fichiers sensibles**. Le chiffrement des fichiers sensibles permet de protéger les données en cas de vol ou de perte de l'ordinateur. Il est également recommandé de **sauvegarder régulièrement les fichiers** pour éviter de les perdre en cas de panne de disque dur.

De plus, il est recommandé de **limiter les accès aux fichiers et répertoires** en fonction des besoins de chaque utilisateur. Il est recommandé de **définir des permissions** pour chaque fichier et répertoire pour contrôler qui peut accéder aux données. Les systèmes d'exploitation modernes permettent de définir des **ACL** (Access Control Lists) pour contrôler les accès aux fichiers et répertoires.
(par exemple, `chmod` et `chown` sous Linux)

</section>

## Zero Trust<a name="zero-trust"></a>

## Lexique<a name="lexique"></a>
- **Piratage informatique**: Action de s'introduire dans un système informatique sans autorisation.
- **Brèche de données**: Fuite de données personnelles ou sensibles.
- **Système d'exploitation**: Logiciel qui permet à un ordinateur de fonctionner.
- **BIOS/UEFI**: Logiciel qui s'exécute lors du démarrage de l'ordinateur.
- **Secure Boot**: Fonctionnalité qui empêche le démarrage de logiciels non signés.
- **Chiffrement**: Procédé de cryptographie qui consiste à transformer un message clair en un message chiffré.
- **Authentification forte**: Utilisation de plusieurs facteurs d'authentification pour se connecter à un système.
- **OTP**: One-Time Password, mot de passe à usage unique.
- **Bootloader**: Logiciel qui permet de charger le système d'exploitation.
- **Kernel**: Noyau du système d'exploitation.
- **Kernel Exploit**: Attaque qui exploite une faille dans le noyau du système d'exploitation.
- **ACL**: Access Control List, liste de contrôle d'accès.
- **IPv4**: Protocole de communication utilisé sur Internet.
- **IPv6**: Protocole de communication utilisé sur Internet.
- **FTP**: File Transfer Protocol, protocole de transfert de fichiers.
- **SFTP**: Secure File Transfer Protocol, protocole de transfert de fichiers sécurisé.
- **SSH**: Secure Shell, protocole de communication sécurisé pour accéder à un ordinateur à distance.
- **Zero Trust**: Modèle de sécurité informatique qui ne fait confiance à aucun utilisateur ou appareil à l'intérieur ou à l'extérieur du réseau.
- **Moindre privilège**: Principe de sécurité informatique qui consiste à accorder à chaque utilisateur les privilèges les plus bas nécessaires pour effectuer son travail.
- **Chiffrement**: Procédé de cryptographie qui consiste à transformer un message clair en un message chiffré.
- **Gestion des secrets**: Pratique de sécurité informatique qui consiste à protéger les informations sensibles.
- **Supply Chain**: Chaîne d'approvisionnement, ensemble des acteurs qui interviennent dans la production et la distribution d'un produit.
- **Secure Coding**: Pratique de développement logiciel qui vise à produire du code sûr et fiable.
- **Logging & Monitoring**: Pratique de sécurité informatique qui consiste à surveiller et enregistrer les événements d'un système.
- **Mises à jour**: Processus de maintenance informatique qui consiste à appliquer les correctifs de sécurité.
- **TLS**: Protocole de sécurisation des échanges sur Internet.
- **Proxy**: Serveur intermédiaire qui sert d'intermédiaire entre les utilisateurs et les serveurs.
- **Firewall**: Dispositif de sécurité informatique qui contrôle le trafic réseau.
