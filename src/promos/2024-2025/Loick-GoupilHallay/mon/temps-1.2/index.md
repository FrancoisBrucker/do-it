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

<head>
  <link rel="icon" href="https://github.com/BoxBoxJason/resume/blob/d07f37a66e2a583832533a10a9a4bf73b020be6f/src/assets/avatar.png?raw=true" type="image/x-icon">
</head>

{%prerequis '**MON avancé**'%}
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
  mermaid.registerIconPacks([
  {
    name: 'carbon',
    loader: () =>
      fetch('https://unpkg.com/@iconify-json/carbon/icons.json').then((res) => res.json()),
  },
  {
    name: 'tabler',
    loader: () =>
      fetch('https://unpkg.com/@iconify-json/tabler/icons.json').then((res) => res.json()),
  },
  {
    name: 'emojione',
    loader: () =>
      fetch('https://unpkg.com/@iconify-json/emojione/icons.json').then((res) => res.json()),
  },
  ]);
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
        - [BIOS/UEFI](#bios-uefi)
        - [Chiffrement du disque dur](#chiffrement-du-disque-dur)
    2. [Durcissement Logiciel & Système d'Exploitation](#durcissement-logiciel-système-dexploitation)
        - [Configuration bootloader & kernel](#configuration-bootloader-kernel)
        - [Mises à jours](#mises-à-jour)
        - [SSH, Réseau & firewall](#ssh-réseau-firewall)
        - [Gestion des comptes utilisateurs](#gestion-des-comptes-utilisateurs)
            - [Mots de passe forts](#mots-de-passe-forts)
            - [Authentification forte](#authentification-forte)
            - [Niveaux de privilèges](#niveaux-de-privilèges)
3. [Zero Trust](#zero-trust)
    1. [Moindre privilège](#moindre-privilège)
    2. [Sécurisation des accès](#sécurisation-des-accès)
        - [Politique d'authentification de l'entreprise](#politique-dauthentification-de-lentreprise)
        - [Politique de PKI](#politique-de-pki)
    3. [Sécurisation des flux](#sécurisation-des-flux)
        - [Firewall](#firewall)
        - [DMZ](#dmz)
        - [Proxy](#proxy)
4. [Former les développeurs](#former-les-développeurs)
    1. [Chiffrement](#chiffrement)
    2. [Signature](#signature)
    3. [Gestion des secrets](#gestion-des-secrets)
    4. [Supply Chain & Dépendances vulnérables](#supply-chain)
    5. [Secure Coding](#secure-coding)
    6. [Logging & Monitoring](#logging-monitoring)
    7. [Réponse aux incidents](#réponse-aux-incidents)
    8. [Risques légaux](#risques-légaux)
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


### Durcissement Logiciel & Système d'Exploitation<a name="durcissement-logiciel-système-dexploitation"></a>
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

Il est également recommandé de **configurer un pare-feu** pour contrôler le trafic réseau entrant et sortant. Un **pare-feu** permet de **filtrer le trafic réseau** entrant et sortant. Il suit des **règles de filtrage** définies par l'administrateur pour autoriser ou bloquer le trafic réseau. C'est un bon moyen d'empêcher votre extension VSCode de communiquer avec Pyongyang.

Il est enfin recommandé de **désactiver les services réseau non utilisés** pour réduire la surface d'attaque. Par exemple, si vous n'utilisez pas le service FTP (privilégiez SFTP), IPv6 ou le partage de fichiers, il est recommandé de les désactiver.

Il faut paramétrer l'IPv4 et l'IPv6 pour qu'ils soient **sécurisés** et **privés**. Il est recommandé de **désactiver l'IPv6** si vous n'en avez pas besoin, car il peut être une porte d'entrée pour les attaquants.

#### Gestion des comptes utilisateurs<a name="gestion-des-comptes-utilisateurs"></a>
La gestion des utilisateurs est un élément clé de la sécurité du système d'exploitation. Il est recommandé de **créer des comptes utilisateurs** pour chaque utilisateur et de **limiter les privilèges** des comptes utilisateurs. Il est également recommandé de **désactiver les comptes inutilisés** pour réduire la surface d'attaque.

##### Mots de passe forts<a name="mots-de-passe-forts"></a>
Il est essentiel de **choisir des mots de passe forts** pour les comptes utilisateurs. Un mot de passe fort est un mot de passe qui est difficile à deviner pour un attaquant. Il est recommandé d'utiliser des mots de passe longs, composés de lettres majuscules et minuscules, de chiffres et de caractères spéciaux.

L'ANSSI met régulièrement à jour son [guide d'authentification multifacteur et mots de passe](https://cyber.gouv.fr/sites/default/files/2021/10/anssi-guide-authentification_multifacteur_et_mots_de_passe.pdf) pour vous aider à choisir un bon mot de passe, robustes vis-à-vis des évolutions technologiques.

##### Authentification forte<a name="authentification-forte"></a>
L'authentification forte consiste à **utiliser plusieurs facteurs d'authentification** pour se connecter à un système. Par exemple, un mot de passe et un code envoyé par SMS. Le deuxième facteur d'authentification peut aussi être un élément physique comme une clé USB ou un token.

Les systèmes d'exploitation modernes proposent des solutions d'authentification forte comme [Windows Hello](https://www.microsoft.com/fr-fr/windows/tips/windows-hello) (reconnaissance faciale) ou [Touch ID](https://support.apple.com/fr-fr/105095) (reconnaissance d'empreinte digitale). Les éléments physiques comme les clés USB ou les tokens sont souvent utilisés pour l'authentification forte dans les entreprises. Il s'agit par exemple de la clé [YubiKey](https://www.yubico.com), de la carte à puce ou du token OTP. Tous ces éléments peuvent être déployés (longtemps) après l'installation du système d'exploitation. Ils sont souvent gérés par un service d'**authentification centralisé**.

Cette méthode est **plus sécurisée** que l'authentification par mot de passe seul, car il est plus difficile pour un attaquant de compromettre plusieurs facteurs d'authentification. Cependant elle peut générer de la **frustration** et être **contraignante** pour les utilisateurs.

##### Niveaux de privilèges<a name="niveaux-de-privilèges"></a>
Par défaut, les systèmes d'exploitation n'ont que 2 niveaux de privilèges: **administrateur** et **utilisateur**. Pour compléter ces niveaux, il est recommandé de **créer des groupes** pour regrouper les utilisateurs avec des privilèges similaires. Par exemple, un groupe "développeurs" pour les utilisateurs qui ont besoin d'accéder aux outils de développement.

L'idée est d'avoir le moins de véritables administrateurs possible, et de donner les privilèges les plus bas nécessaires pour effectuer le travail. C'est le principe du **moindre privilège**.

Pour les utilisateurs qui ont besoin d'un accès administrateur, il est recommandé de mettre en place un suivi des actions effectuées par ces utilisateurs pour **détecter les abus**.

#### Fichiers et répertoires<a name="fichiers-et-répertoires"></a>
Pour protéger ses données, il est recommandé de **chiffrer les fichiers sensibles**. Le chiffrement des fichiers sensibles permet de protéger les données en cas de vol ou de perte de l'ordinateur. Il est également recommandé de **sauvegarder régulièrement les fichiers** pour éviter de les perdre en cas de panne de disque dur.

De plus, il est recommandé de **limiter les accès aux fichiers et répertoires** en fonction des besoins de chaque utilisateur. Il est recommandé de **définir des permissions** pour chaque fichier et répertoire pour contrôler qui peut accéder aux données. Les systèmes d'exploitation modernes permettent de définir des **ACL** (Access Control Lists) pour contrôler les accès aux fichiers et répertoires.
(par exemple, `chmod` et `chown` sous Linux)

</section>

## Zero Trust<a name="zero-trust"></a>
Le [modèle Zero Trust](https://cyber.gouv.fr/publications/le-modele-zero-trust) est un modèle de sécurité informatique qui consiste à ne **faire confiance à aucun utilisateur ou appareil à l'intérieur ou à l'extérieur du réseau**. Cela va à l'encontre du modèle habituel de confiance implicite, où les utilisateurs et les appareils à l'intérieur du réseau sont considérés comme sûrs.\
C'est un modèle de sécurité qui définit **l'ensemble de l'architecture de sécurité** d'une entreprise. Par conséquent il est difficile à mettre en place et nécessite une **réflexion globale**. Il est encore plus compliqué de transformer un système existant en un système Zero Trust.

Ce modèle repose sur plusieurs principes clés

### Moindre privilège<a name="moindre-privilège"></a>
Le principe du **moindre privilège** consiste à accorder à chaque utilisateur les **privilèges les plus bas nécessaires** pour effectuer son travail.

Cela signifie que:
- L'accès aux ressources repose uniquement sur le **besoin d'en connaître** de l'utilisateur
- L'accès donné est le **plus faible possible** permettant tout de même à l'utilisateur de réaliser son travail
- Les demandes d'accès sont **contrôlées et traçables**. Si possible elles sont **automatiques** pour éviter les erreurs humaines et la frustration des utilisateurs
- Les accès sont **révoqués** dès que l'utilisateur n'en a plus besoin
- Il y a une **surveillance** (automatique ou non) pour détecter les abus, les anomalies et les erreurs
- La politique de sécurité est **appliquée**, **contrôlée** et **(r)évaluée** régulièrement

### Sécurisation des accès<a name="sécurisation-des-accès"></a>
La **sécurisation des accès** consiste à **authentifier** et **autoriser** les utilisateurs et les appareils avant de leur donner accès aux ressources.

Concrètement, d'après le [Guide de d'administration système de l'ANSSI](https://cyber.gouv.fr/sites/default/files/2018/04/anssi-guide-admin_securisee_si_v3-0.pdf), pour une entreprise / équipe, cela passe par:

#### Politique d'authentification de l'entreprise<a name="politique-dauthentification-de-lentreprise"></a>
L'entreprise doit mettre en place une **politique d'authentification** pour définir les règles d'authentification des utilisateurs sur leurs postes physiques. Cette politique doit inclure:
- **Authentification robuste**
- **Authentification forte**
- **Rotation régulière des mots de passe**
- Déployer et maintenir des moyens de **gestion centralisée des identités et des accès** tels que des [LDAP](https://www.redhat.com/fr/topics/security/what-is-ldap-authentication), des [Active Directory](https://learn.microsoft.com/fr-fr/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview), des [SSO](https://www.oracle.com/fr/security/qu-est-ce-qu-un-sso/) ([SAML](https://fr.wikipedia.org/wiki/Security_assertion_markup_language) ou [OIDC](https://fr.wikipedia.org/wiki/OpenID_Connect))
- Utiliser des **certificats** pour l'authentification

#### Politique de PKI<a name="politique-de-pki"></a>
La [PKI](https://cpl.thalesgroup.com/faq/public-key-infrastructure-pki/what-public-key-infrastructure-pki) (Public Key Infrastructure) est un ensemble de technologies et de procédures qui permettent de gérer les clés et les certificats numériques. Ces certificats numériques sont utilisés pour **authentifier** les utilisateurs et les appareils. Ils sont aussi utilisés pour **chiffrer** les communications entre les utilisateurs et les ressources. Ou encore pour **signer** les données pour garantir leur intégrité.

Les certificats numériques sont délivrés par une **autorité de certification** (CA) qui atteste de l'identité de l'utilisateur ou de l'appareil. Il est essentiel de mettre en place une **politique de PKI** pour définir les règles de gestion des certificats numériques.

### Sécurisation des flux<a name="sécurisation-des-flux"></a>
La **sécurisation des flux** consiste à **chiffrer** les communications entre les utilisateurs et les ressources pour protéger les données des attaques de type [Man In The Middle](https://fr.wikipedia.org/wiki/Attaque_de_l%27homme_du_milieu). Il est recommandé d'utiliser des protocoles de sécurisation des échanges comme **SSL** ou **TLS** pour chiffrer les communications. Cela permet de garantir la **confidentialité** et l'**intégrité** des données. Pour les développeurs, il est recommandé d'utiliser des protocoles de transfert de fichiers sécurisés comme **SFTP** pour transférer des fichiers en toute sécurité.

Il est également recommandé de **surveiller les flux** pour détecter les anomalies et les attaques. La surveillance des flux permet de détecter les attaques en temps réel et de réagir rapidement pour les contrer. Cela passe par la mise en place de systèmes de logging et de monitoring.

#### Firewall<a name="firewall"></a>
L'entreprise peut (et doit) mettre en place un **firewall** pour contrôler le trafic réseau entrant et sortant de l'entreprise. Ce firewall est un appareil physique ou un logiciel qui filtre le trafic réseau pour l'ensemble de ses utilisateurs. Il est au dessus des firewalls logiciels installés sur les postes de travail.\
C'est une couche de sécurité supplémentaire qui permet de bloquer certaines communications non autorisées ou encore des attaques de type [DDOS](https://cyber.gouv.fr/publications/comprendre-et-anticiper-les-attaques-ddos)

#### DMZ<a name="dmz"></a>
La **DMZ** (Demilitarized Zone) est une zone du réseau qui est isolée du reste du réseau de l'entreprise. C'est une zone de sécurité intermédiaire entre le réseau interne et le réseau externe. Elle permet de **limiter les risques** en cas de compromission d'un serveur dans la DMZ. Elle est utilisée pour héberger des services accessibles depuis l'extérieur de l'entreprise, comme un site web ou un serveur de messagerie. La DMZ est une couche de sécurité supplémentaire qui permet de protéger les ressources sensibles de l'entreprise. Elle est souvent utilisée pour héberger des services qui nécessitent un accès depuis l'extérieur de l'entreprise, ou pour connecter des réseaux de confiance différents. Cela peut aussi faire office de **sandbox** pour les développeurs. Ou encore être utilisé pour héberger un **proxy** ou un **firewall**.

<pre class="mermaid" style="background-color: transparent">
%%{init: {'theme': 'forest'}}%%
architecture-beta
    group intranet(carbon:chart-network)[Intranet]
    service server1(server)[Server 1] in intranet
    service server2(server)[Server 2] in intranet

    group dmz(cloud)[DMZ]
    service firewall(carbon:firewall-classic)[Firewall] in dmz
    service proxy(carbon:server-proxy)[Proxy] in dmz
    service webserver(carbon:server-dns)[Web Server] in dmz
    service mailserver(carbon:mail-all)[Mail Server] in dmz

    server1:T <--> L:proxy
    server1:R <--> L:webserver
    server1:B <--> L:mailserver

    group internet(tabler:world-www)[Internet]
    service china(emojione:flag-for-china)[Unsuspicious server] in internet

    proxy:R <--> T:firewall
    webserver:R <--> L:firewall
    mailserver:R <--> B:firewall

    firewall:R <--> L:china
</pre>

#### Proxy<a name="proxy"></a>
Un **proxy** est un serveur intermédiaire qui sert d'intermédiaire entre les utilisateurs et les serveurs. Il permet de **filtrer** les communications pour contrôler l'accès aux ressources. Il peut être utilisé pour **bloquer** les sites web malveillants, **contrôler** les accès aux ressources sensibles ou **accélérer** les communications. Il est recommandé de mettre en place un proxy pour contrôler le trafic réseau et protéger les utilisateurs des attaques.

## Former les développeurs<a name="former-les-développeurs"></a>
En supposant que l'entreprise ait mis en place tous les moyens mentionnés ci-dessus pour protéger son SI, elle reste toujours vulnérable aux attaques. Les attaques ont quasiment toujours lieu à cause d'une **erreur humaine**. Il est donc essentiel de **sensibiliser** les développeurs à la sécurité informatique et de les former aux bonnes pratiques de sécurité. Ces bonnes pratiques doivent être appliquées dès le début du développement et tout au long du cycle de vie du logiciel. Elles s'appliquent à l'utilisation du poste de travail, mais surtout aux principes de développement.
Voici quelques points essentiels à aborder avec eux.

### Chiffrement<a name="chiffrement"></a>
Le **chiffrement** est un élément clé de la sécurité informatique. Il permet de **protéger les données** en les transformant en un format illisible sans la clé de déchiffrement. Concrètement, il est recommandé de **chiffrer les données sensibles** tels que les mots de passe, les clés privées, les données personnelles, le code sensible, les artefacts, les fichiers de configuration, les secrets, les tokens, les certificats, les clés de chiffrement, les clés de signature, les clés de session, les clés de stockage, les clés de base de données. En bref, tout ce qui représenterait un risque s'il était exposé.

Il est également recommandé de **chiffrer les communications** entre les utilisateurs et les ressources pour protéger les données. Pour les développeurs, cela signifie utiliser des protocoles de communication sécurisés comme **SSL**(Secure Socket Layer) ou **TLS**(Transport Layer Security) pour chiffrer les communications. Ils doivent mettrent en place des protocoles de transfert de fichiers sécurisés comme **SFTP** pour transférer des fichiers en toute sécurité. Tous les serveurs web doivent être configurés pour utiliser **HTTPS**. Les mots de passe doivent être **hashés** avant d'être stockés dans la base de données.

Evidemment, les clés de chiffrement doivent être **robuste** pour se protéger des attaques de type **brute force**. Il est recommandé de **générer des clés de chiffrement aléatoires** et de les stocker dans un **coffre-fort** ou un **service de gestion des secrets**.

### Signature<a name="signature"></a>
La **signature** est un autre élément clé de la sécurité informatique. Elle permet de **garantir l'intégrité** des données en les signant avec une clé privée. La signature permet de vérifier que les données n'ont pas été modifiées depuis leur signature. Concrètement, les développeurs doivent vérifier les **signatures des fichiers** qu'ils téléchargent pour s'assurer de leur intégrité. Ils doivent également **signer** les composants logiciels qu'ils produisent, les artefacts, les fichiers de configuration, les secrets, les tokens, les certificats, les clés de chiffrement, les clés de signature, les clés de session, les clés de stockage, les clés de base de données. En bref, tout ce qui nécessite d'être tracé et vérifié.

### Gestion des secrets<a name="gestion-des-secrets"></a>
La **gestion des secrets** est un élément essentiel de la sécurité informatique. Les secrets sont des informations sensibles comme les mots de passe, les clés privées, les données personnelles, les tokens, les certificats, les clés de chiffrement, les clés de signature, les clés de session, les clés de stockage, les clés de base de données. On retrouve là les mêmes éléments que pour le chiffrement et la signature. Les secrets doivent être **protégés** et **gérés** de manière sécurisée pour éviter les fuites dangereuses.

Pour cela il est pratique courante d'utiliser un **service de gestion des secrets** comme [Vault](https://www.vaultproject.io), [Keycloak](https://www.keycloak.org), [AWS Secrets Manager](https://aws.amazon.com/fr/secrets-manager/), [Azure Key Vault](https://azure.microsoft.com/fr-fr/services/key-vault/), [Google Secret Manager](https://cloud.google.com/secret-manager). Ces services permettent de stocker les secrets de manière sécurisée et de les **distribuer** aux applications de manière sécurisée. Ils permettent également de **générer des clés de chiffrement aléatoires** et de les stocker.

Ces secrets NE DOIVENT PAS être stockés directement dans le code source, tous les gestionnaires de code source moderne permettent de **masquer** les secrets et de les remplacer uniquement lors de l'exécution des pipelines de CI/CD et du code.\
Il ne doivent pas non plus être partagés par email, par chat, par téléphone, ou tout autre moyen de communication non sécurisé.

### Supply Chain & Dépendances vulnérables<a name="supply-chain"></a>
La **supply chain** est l'ensemble des acteurs qui interviennent dans la production et la distribution d'un produit. Dans le domaine du développement logiciel, la supply chain concerne les **dépendances** utilisées par les développeurs pour construire leur logiciel. Ces dépendances peuvent être des **bibliothèques**, des **modules**, des **packages** ou des **frameworks**.\
Il est essentiel de s'assurer de la **sécurité** de la supply chain pour éviter les attaques. Pour cela, il faut d'abord **vérifier la provenance** des dépendances pour s'assurer qu'on ne télécharge pas le code d'un éditeur malveillant (chinois ou russe en général). Il faut ensuite **vérifier la signature** des dépendances pour s'assurer de leur intégrité. Enfin, il faut se renseigner sur les **CVE** (Common Vulnerabilities and Exposures) des dépendances pour s'assurer qu'elles ne contiennent pas de failles de sécurité connues.

Tout cela permettra peut-être d'éviter de rajouter une ou deux backdoors externes dans votre application. C'est toujours mieux de les ajouter soi-même 😁.
<img class="banner" src="https://programmerhumor.io/wp-content/uploads/2024/06/programmerhumor-io-linux-memes-backend-memes-68da01bbf306b33.jpe" alt="Modern Digital Product">

### Secure Coding<a name="secure-coding"></a>
Le **Secure Coding** est un ensemble de bonnes pratiques de développement logiciel permettant de produire du code le plus sûr et fiable possible. Il repose sur un ensemble de standards et de règles de sécurité à respecter lors du développement d'un logiciel. Ces règles permettent de réduire les risques de failles de sécurité et d'erreurs de programmation.

Il existe de nombreux standards de Secure Coding comme:
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [NIST Secure Coding Standards](https://csrc.nist.gov/projects/ssdf)
- [MISRA](https://misra.org.uk/)
- [ISO/IEC 27001](https://www.iso.org/standard/54534.html)

Ces standards définissent les bonnes pratiques de développement logiciel à respecter pour garantir le maximum de sécurité. Ils ne sont pas absolus et doivent être adaptés à chaque contexte. Les entreprises définissent souvent leur propre standard en se basant sur ces standards de référence.

Les bonnes pratiques de Secure Coding incluent:
- **Validation des entrées** pour éviter les attaques d'injection
- **Échappement des sorties** pour éviter les attaques XSS
- **Gestion des erreurs** pour éviter les fuites d'informations sensibles
- **Contrôle d'accès** pour limiter l'accès aux ressources
- **Chiffrement** pour protéger les données sensibles
- **Gestion des sessions** pour éviter les attaques CSRF
- **Mises à jour régulières** pour corriger les failles de sécurité

### Logging & Monitoring<a name="logging-monitoring"></a>
Comme il n'est pas toujours possible d'empêcher les attaques, il est à minima nécessaire de pouvoir retrouver où elles ont eu lieu. Pour cela, il est essentiel de **surveiller** et **enregistrer** les événements d'un système. Cela permet de **détecter les attaques** en temps réel et de réagir rapidement pour les contrer. Cela permet également de **tracer les actions** des utilisateurs pour détecter les abus et les anomalies.

Pour un développeur, cela signifie qu'il doit mettre en place dans sa logique de code des **logs** pour enregistrer les événements importants. Ces logs doivent être **conservés** et **consultables** pour permettre de retracer les actions des utilisateurs. Il est recommandé de **mettre en place un système de logging centralisé** pour centraliser les logs et les consulter facilement.\
Il doit aussi implémenter du **suivi** de l'état de son application pour détecter les erreurs et les anomalies. Cela passe par des **health checks**, des **metrics**, des **traces** et des **logs**.\
Dans le meilleur des mondes, il doit mettre en place des **alertes** pour être prévenu en cas d'anomalie.

### Réponse aux incidents<a name="réponse-aux-incidents"></a>
Enfin, il est essentiel de **préparer une réponse aux incidents** pour réagir rapidement en cas d'attaque. Il faut définir des plans d'action pour **réagir** aux attaques, se débarasser des attaquants, **identifier** puis **réparer** les dégâts; repérer les **données compromises** et les **fuites**. Il faut également **communiquer** avec les utilisateurs et les autorités pour les informer de l'incident et des mesures prises pour le résoudre.

Ensuite, il faut **analyser** l'incident pour comprendre comment il a eu lieu et comment l'éviter à l'avenir. Il faut **mettre en place des mesures correctives** pour éviter que l'incident se reproduise. Bien évidemment, le cas idéal serait de **mettre en place des mesures préventives** pour anticiper les attaques et les contrer avant qu'elles ne se produisent.

### Risques légaux<a name="risques-légaux"></a>
Un point important de la sensibilisation du développeur consiste à l'informer des risques légaux encourus par l'entreprise mais aussi par lui-même en cas de non-respect des règles de sécurité. Les entreprises sont soumises à des **obligations légales** en matière de sécurité informatique. Elles doivent respecter des **normes** et des **règlements** pour protéger les données des utilisateurs.\
Une faille de sécurité peut entraîner des **sanctions** financières, des **poursuites judiciaires** et une **perte de confiance** des utilisateurs. Les développeurs peuvent également être tenus **responsables** en cas de faille de sécurité. Ils doivent comprendre qu'ils ont un rôle essentiel à jouer dans la sécurité de l'entreprise et qu'ils doivent respecter les règles de sécurité pour éviter tout problème avec la justice.

## Conclusion<a name="conclusion"></a>
La sécurité informatique est un enjeu majeur pour les entreprises, <u>même si elles ne produisent pas des services numériques</u>. La sécurité informatique est un domaine complexe qui nécessite des compétences avancées en informatique et en sécurité. Les entreprises ont des services **SRE** (Site Reliability Engineering) ou des **DSI** (Direction des Systèmes d'Information) qui sont chargés de mettre en place les mesures de sécurité nécessaires pour protéger le SI de l'entreprise.

La sécurité coûte cher, mais les conséquences d'une faille de sécurité peuvent être encore plus coûteuses. Il est donc essentiel d'investir dans la sécurité informatique pour protéger les données de l'entreprise, sa réputation et éviter les attaques.

Enfin n'oubliez pas que la <u>sécurité informatique est l'affaire de tous</u>. Les développeurs ont un rôle essentiel à jouer dans la sécurité de l'entreprise. Ils doivent être sensibilisés à la sécurité informatique et formés aux bonnes pratiques de sécurité. Ils doivent respecter les règles de sécurité et mettre en place les mesures de sécurité nécessaires pour protéger les données de l'entreprise.

## Lexique<a name="lexique"></a>
- **Piratage informatique**: Action de s'introduire dans un système informatique sans autorisation.
    - **Kernel Exploit**: Attaque qui exploite une faille dans le noyau du système d'exploitation.
    - **Man In The Middle**: Attaque qui consiste à intercepter et modifier les communications entre deux parties.
    - **Phishing**: Technique d'attaque qui consiste à tromper les utilisateurs pour obtenir des informations sensibles.
    - **DDOS**: Distributed Denial of Service, attaque qui vise à rendre un service indisponible en saturant les serveurs.
    - **Brute Force**: Attaque qui consiste à essayer toutes les combinaisons possibles pour trouver un mot de passe.
    - **Backdoor**: Porte dérobée, faille secrète dans un logiciel qui permet à un attaquant d'accéder au système.
    - **Injection**: Attaque qui consiste à injecter du code malveillant dans un système.
    - **Brèche de données**: Fuite de données personnelles ou sensibles.
    - **CVE**: Common Vulnerabilities and Exposures, base de données des vulnérabilités connues.
- **Ordinateur**
    - **BIOS/UEFI**: Logiciel qui s'exécute lors du démarrage de l'ordinateur.
    - **Secure Boot**: Fonctionnalité qui empêche le démarrage de logiciels non signés.
    - **Bootloader**: Logiciel qui permet de charger le système d'exploitation.
    - **Système d'exploitation**: Logiciel qui permet à un ordinateur de fonctionner.
    - **Kernel**: Noyau du système d'exploitation.
- **Authentification**: Processus qui permet de vérifier l'identité d'un utilisateur.
    - **Mots de passe forts**: Mots de passe difficiles à deviner pour un attaquant.
    - **Authentification forte**: Utilisation de plusieurs facteurs d'authentification pour se connecter à un système.
    - **OTP**: One-Time Password, mot de passe à usage unique.
    - **LDAP**: Lightweight Directory Access Protocol, protocole d'accès à un annuaire.
    - **Active Directory**: Service d'annuaire de Microsoft.
    - **SSO**: Single Sign-On, authentification unique.
    - **SAML**: Security Assertion Markup Language, langage de balisage d'assertion de sécurité.
    - **OIDC**: OpenID Connect, protocole d'authentification.
- **Protocoles Informatiques**: Ensemble de règles qui permettent à des appareils de communiquer entre eux.
    - **IPv4**: Protocole de communication utilisé sur Internet.
    - **IPv6**: Protocole de communication utilisé sur Internet.
    - **FTP**: File Transfer Protocol, protocole de transfert de fichiers.
    - **SFTP**: Secure File Transfer Protocol, protocole de transfert de fichiers sécurisé.
    - **SSH**: Secure Shell, protocole de communication sécurisé pour accéder à un ordinateur à distance.
    - **SSL**: Secure Sockets Layer, protocole de sécurisation des échanges sur Internet.
    - **TLS**: Transport Layer Security, protocole de sécurisation des échanges sur Internet.
- **Zero Trust**: Modèle de sécurité informatique qui ne fait confiance à aucun utilisateur ou appareil à l'intérieur ou à l'extérieur du réseau.
    - **Moindre privilège**: Principe de sécurité informatique qui consiste à accorder à chaque utilisateur les privilèges les plus bas nécessaires pour effectuer son travail.
    - **ACL**: Access Control List, liste de contrôle d'accès qui définit les permissions d'accès aux fichiers et répertoires.
- **Principes de sécurité**
    - **Secure Coding**: Pratique de développement logiciel qui vise à produire du code sûr et fiable.
    - **Logging & Monitoring**: Pratique de sécurité informatique qui consiste à surveiller et enregistrer les événements d'un système.
    - **Mises à jour**: Processus de maintenance informatique qui consiste à appliquer les correctifs de sécurité.
    - **Gestion des secrets**: Pratique de sécurité informatique qui consiste à protéger les informations sensibles.
    - **Chiffrement**: Procédé de cryptographie qui consiste à transformer un message clair en un message chiffré.
    - **SandBox**: Environnement isolé qui permet d'exécuter des applications de manière sécurisée.
- **PKI**: Public Key Infrastructure, infrastructure de gestion des clés et des certificats numériques.
    - **Certificat numérique**: Document électronique qui atteste de l'identité d'une personne ou d'une entité.
    - **Autorité de certification**: Entité qui délivre les certificats numériques.
- **Supply Chain**: Chaîne d'approvisionnement, ensemble des acteurs qui interviennent dans la production et la distribution d'un produit.
- **Réseau**: Ensemble d'appareils interconnectés qui permettent de communiquer entre eux.
    - **DMZ**: Demilitarized Zone, zone du réseau isolée du reste du réseau de l'entreprise.
    - **Proxy**: Serveur intermédiaire qui sert d'intermédiaire filtrant entre les utilisateurs et les serveurs.
    - **Firewall**: Dispositif de sécurité informatique qui contrôle le trafic réseau, permettant de filtrer les communications.
