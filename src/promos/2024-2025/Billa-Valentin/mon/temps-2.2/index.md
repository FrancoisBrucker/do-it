---
layout: layout/mon.njk

title: "Redondance"
authors:
  - Valentin Billa

date: 2024-12-02

tags:
  - 'temps 1'
  - 'vert'  
  - 'débutant'
  - 'devops'
  - 'serveur'
  - 'RAID'
  - 'ZFS'

résumé: "Comparaison des technologies RAID et ZFS pour le stockage et la redondance de données"
---

{% prerequis %}
* Compréhension des bases du stockage (disques, partitions, systèmes de fichiers)
* Vocabulaire courant lié à la redondance et aux sauvegardes
{% endprerequis %}

## Objectifs

Récemment le GInfo a acquis de nouveaux serveurs, j'aide l'association dans l'élaboration de configurations de nos
périphériques de stockage dans l'objectif de mettre à disposition plusieurs dizaines de tera de stockage aux associations
étudiantes sans pour autant leur faire prendre le risque de perdre leurs données !

Dans ce MON, je souhaite donc explorer les différentes **technologies RAID** ainsi que **ZFS**,
afin de mieux comprendre leurs avantages, limites et applications dans la gestion de stockage de données. 

RAID est omniprésent dans les systèmes de stockage critiques, tandis que ZFS, avec son approche moderne,
est devenu un incontournable (entre autre recommandé à l'association par des membres de la DSI de l'école)
pour garantir intégrité et flexibilité dans le stockage.


{% note %}
**Mise en garde :**
Dans ce MON, lorsque nous parlons de "sécurité des données", nous nous référons **exclusivement à la protection contre la perte de données**.
L'encryption peut toujours être ajoutée par-dessus les solutions que je présenterais.

Même si votre serveur utilise des solutions comme RAID ou ZFS pour garantir la redondance des données, **cela ne remplace pas des sauvegardes régulières**.
Ces solutions protègent principalement contre les défaillances matérielles, mais elles ne couvrent pas les erreurs humaines,
les attaques logicielles ou les catastrophes physiques (incendie, inondation, etc.).  
**Avoir des sauvegardes (backups) reste crucial** pour assurer une protection complète.
Une recommendation généralement donnée est la [règle des 3-2-1](https://www.veeam.com/blog/321-backup-rule.html)
{% endnote %}

---

J'ai tout d'abord orienté mes recherches vers le RAID traditionnel puisque c'est ce que nous faisions déjà.

## Qu'est-ce que RAID ?

Le **RAID** (Redundant Array of Independent Disks) est une technologie permettant de combiner plusieurs disques physiques pour offrir des bénéfices en termes de :
- **Performance** (lecture/écriture plus rapide)
- **Redondance** (tolérance aux pannes)
- **Capacité** (agrégation des espaces de stockage).

{% info %}
RAID peut être implémenté via **hardware** (contrôleurs RAID dédiés) ou **software** (géré par le système d'exploitation).
{% endinfo %}

### RAID Hardware vs Software

- **RAID hardware** : Implémenté par un contrôleur RAID dédié (une carte contrôleur RAID). Le matériel gère directement les opérations RAID, soulageant le CPU principal.
- **RAID software** : Géré directement par le système d'exploitation (Linux `mdadm`, Windows Storage Spaces). Plus flexible et moins coûteux, mais légèrement plus gourmand en ressources CPU.

{% info %}
Les cartes RAID matérielles haut de gamme incluent une mémoire cache avec batterie pour améliorer les performances
d'écriture et sécuriser les données en cas de coupure de courant.
{% endinfo %}

Pour les nouveaux serveurs du GInfo, des Dell R740XD contiennent des cartes RAID matérielles de qualité
ce qui rendrait dommage l'utilisation de RAID logiciel. 

## Les niveaux de RAID les plus courants

### RAID 0 : **Striping**

- **Objectif** : Performances optimisées.
- **Principe** : Les données sont divisées et écrites simultanément sur plusieurs disques.
- **Inconvénient** : Aucune redondance. La perte d'un disque entraîne la perte totale des données.

```text
+-----+-----+-----+-----+
| D1a | D2a | D3a | D4a |   => Données écrites en parallèle
| D1b | D2b | D3b | D4b |
+-----+-----+-----+-----+
```

{% info %}
RAID 0 est principalement utilisé pour les besoins en vitesse pure où la sécurité des données est secondaire (ex : cache temporaire, montage vidéo).
{% endinfo %}

### RAID 1 : **Mirroring**

- **Objectif** : Redondance maximale.
- **Principe** : Les données sont dupliquées sur deux disques (miroir).
- **Avantage** : Tolérance à la panne d'un disque.
- **Inconvénient** : La capacité totale est limitée à celle d'un seul disque.

```text
+-----+      +-----+
| D1  |  =   | D1  |   => Les deux disques contiennent exactement les mêmes données.
| D2  |      | D2  |
+-----+      +-----+
```

### RAID 5 : **Striping avec parité**

- **Objectif** : Équilibre entre performances et redondance.
- **Principe** : Les données et les informations de parité (pour reconstruire les données) sont réparties sur au moins **3 disques**.
- **Avantage** : Tolérance à la panne d'un disque.
- **Inconvénient** : Reconstruction lente après une panne.

```text
+-----+-----+-----+
| D1  | D2  | P1  |  => Parité sur le 3ᵉ disque
| P2  | D3  | D4  |
+-----+-----+-----+
```

### RAID 6 : **Striping avec double parité**

- **Objectif** : Redondance améliorée.
- **Principe** : Semblable au RAID 5, mais avec deux blocs de parité. Tolérance à la panne de **2 disques**.
- **Inconvénient** : Nécessite au moins **4 disques** et entraîne des écritures plus lentes.

### Combinaisons : **RAID 10**

En RAID, une combinaison comme RAID 10 se lit comme du RAID 1 + 0, il faut lire de gauche à droite ie.
Un RAID 0 de disques virtuels en RAID 1.

- **Objectif** : Performances ET redondance.
- **Principe** : Combinaison de RAID 1 (mirroring) et RAID 0 (striping). Nécessite un nombre pair de disques (minimum 4).

```text
RAID 10 = RAID 1 (mirroring) + RAID 0 (striping)
+-----+-----+      +-----+-----+
| D1  | D2  |  =>  | D1  | D2  |
+-----+-----+      +-----+-----+
```

{% info %}
RAID 10 est souvent considéré comme la meilleure solution pour un compromis **performances/redondance**, malgré son coût élevé.
{% endinfo %}

---

Je suis tombé au cours de mes recherches sur des gens mentionnant ZFS, j'ai donc décidé d'investiguer dans 
cette direction.

## ZFS : une alternative au RAID

Le **ZFS** (Zettabyte File System) est à la fois un système de fichiers et un gestionnaire de volumes logiques
conçu pour garantir la **résilience des données**, la **flexibilité de gestion** et des **performances élevées**.
Développé initialement par Sun Microsystems, ZFS offre une approche intégrée pour gérer la redondance, la correction
d'erreurs, les snapshots et la compression des données.

{% info %}
ZFS gère lui-même la redondance (RAID-Z) et l'intégrité des données. Il n'a donc pas besoin d'un contrôleur RAID matériel.
{% endinfo %}

### Les concepts clés de ZFS

ZFS repose sur une hiérarchie de composants logiques et physiques qui permettent une gestion souple et redondante des données.

#### Pool de stockage (zpool)
Un **zpool** est l'unité de base de gestion du stockage dans ZFS.
Il regroupe un ensemble de disques physiques pour former une seule entité logique.

Un zpool est configuré pour offrir **la redondance**, **la performance** ou une combinaison des deux, 
selon la disposition des disques qu'il contient.

Les données et l'espace disponible sont automatiquement équilibrés dans le pool, ce qui élimine la gestion
traditionnelle des partitions.

#### Virtual Devices (vdevs)
Un **vdev** est une abstraction logique qui regroupe un ou plusieurs disques physiques.
Plusieurs types de vdevs peuvent être utilisés pour structurer un zpool :

- **Single Disk** : Pas de redondance, un seul disque (non recommandé).
- **Mirror** : Chaque disque d’un vdev contient une copie exacte des données. Offre une excellente redondance.
- **RAID-Z** : L’équivalent de RAID-5/6 dans ZFS, avec plusieurs niveaux :
    - **RAID-Z1** : Une parité (équivalent RAID-5).
    - **RAID-Z2** : Deux parités (équivalent RAID-6).
    - **RAID-Z3** : Trois parités, offrant une tolérance à trois pannes simultanées.

Certains disques peuvent être dédiés à des fonctions plus spécifiques, **L2ARC** (Cache de niveau 2) pour accélérer les
lectures fréquentes, ou **SLOG** (Separate Intent Log) pour améliorer les performances des écritures synchrones.
Ces fonctionnalités permettent d'optimiser les performances globales du système ZFS en tirant
parti de disques rapides (comme des SSD ou NVMe) en complément des disques principaux (HDD ou autres).

{% note %}
Il est difficile d'évaluer si une configuration ZFS va être bénéfique et les impacts sur la perfomance de notre
système sans tout simplement la tester. En effet en fonction des besoins, 
{% endnote %}

#### Système de fichiers et datasets
Une fois un zpool configuré, des **datasets** peuvent être créés pour organiser et gérer les données.

- **Compression** : ZFS applique une compression transparente pour économiser de l’espace.
- **Snapshots** : Des copies instantanées et immuables d’un dataset, idéales pour les sauvegardes.
- **Quota et réservations** : Gestion fine de l’espace alloué aux datasets.

### Pourquoi utiliser ZFS ?

- **Protection contre la corruption des données** : Grâce à un mécanisme de checksum, ZFS détecte et corrige automatiquement les erreurs silencieuses.
- **Snapshots et réplication** : Idéal pour des sauvegardes rapides et efficaces.
- **Évolutivité** : Conçu pour des systèmes allant de quelques gigaoctets à plusieurs exaoctets.
- **Gestion flexible des volumes** : Ajout ou remplacement de disques dans un pool sans interruption des services.

{% lien %}
- [What is ZFS - ItsFoss](https://itsfoss.com/what-is-zfs/)
- [What is ZFS and why should I want to use it ? - Reddit](https://www.reddit.com/r/linuxquestions/comments/3usjz8/what_is_zfs_and_why_should_i_want_to_use_it/)
{% endlien %}

---

## Solution adoptée

Pour l'instant voici la solution que nous avons décidé d'adopter avec le GInfo pour stocker nos données :

Système d'exploitation (Ubuntu 24.04):
  - Installé sur une petite partition (50-100 Go) des disques NVMe en RAID 1 via la carte BOSS.

Utilisation des NVMe RAID 1 restants (optionel) :
  - 50-100 Go : SLOG (ZFS Intent Log) pour améliorer les performances des écritures synchrones.
  - Espace restant : Volumes Docker ou cache L2ARC pour accélérer les lectures fréquentes.

Pool ZFS sur HDD :
*décision en partie influencée par un article nommé ["ZFS you should use mirror vdevs not raidz"](https://jrs-s.net/2015/02/06/zfs-you-should-use-mirror-vdevs-not-raidz/)*
  - Configuration en vdevs miroir pour performance, évolutivité, et redondance.
  - 1 disque configuré comme hot spare.
  - Compression activée (LZ4) et un dataset séparé pour les archives NextCloud.

Backups :
  - Réplication ZFS quotidienne vers un serveur de backup.

## Bibliographie

- [RAID - Wikipedia](https://fr.wikipedia.org/wiki/RAID_(informatique))
- [RAID Levels - ServerFault](https://serverfault.com/questions/19029/raid-levels-explained)
- [Introduction to ZFS](https://openzfs.github.io/openzfs-docs/)
- [ZFS Overview - Oracle](https://docs.oracle.com/cd/E23824_01/html/821-1448/gbbsh.html)
- [ZFS RAID-Z vs RAID - iXsystems Blog](https://www.ixsystems.com/blog/zfs-raid-z/)

### Communautés Reddit intéressantes
- [r/homelab](https://www.reddit.com/r/homelab/)
- [r/sysadmin](https://www.reddit.com/r/sysadmin)
- [r/DataHoarders](https://www.reddit.com/r/DataHoarder/)

{% note %}
Évidemment, il faut noter que Reddit est un réseau social, qui vient avec ses lots de bêtises et/ou mésinformations,
mais j'ai remarqué que ces communautés étaient plutôt bien modérées et une bonne source d'inspiration pour des questions
qui peuvent revenir souvent et auxquelles il serait difficile de répondre sans avoir tout simplement tenté la solution.
{% endnote %}
---
