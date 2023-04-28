---
layout: layout/mon.njk


title: "MON 6 : Flux de données en temps réel : Kafka et Storm"
authors:
 - Thomas Pont

date: 2023-04-05

tags:
  - 'temps 3'
  - 'kafka'
  - 'storm'
  - 'data'
  - 'temps réel'
---


<!-- Début Résumé -->

Comment gérer des données en temps réel ?
<!-- Début Résumé -->

## Introduction

J'ai réalisé ce MON pour préparer mon stage dans lequel je vais faire de l'architecture de données et notamment devoir **récolter et traiter un grand nombre d'information en temps réel**.

Afin d'apprendre tout ceci, j'ai suivi le cours Openclassrooms [Gérer des flux de données en temps réel](https://openclassrooms.com/fr/courses/4451251-gerez-des-flux-de-donnees-temps-reel).

Le cours est divisé en plusieurs parties :

- Présentation des enjeux de la gestion des données en temps réel
- Kafka
- Storm

Ce MON nécessite de nombreux prérequis en **programmation objet** et en **ingénierie informatique** (connaissance de l'environnement UNIX, ...) et est d'un niveau **avancé**.

## Introduction aux données en temps réel et notion de synchronicité

De plus en plus de données sont aujourd'hui récoltées et certaines nécessitent un **traitement quasi instantané**. Par exemple des indicateurs médicaux ou des aides à la conduite nécessitent un traitement en temps réel.

Mais, le temps réel ne s'applique pas qu'à cela. Il faut également que les sites aient un **temps de réponse correct**. Or, de nombreux sites font appel à des services extérieurs pour la gestion de certaines choses (par exemple, pour savoir d'où viennent leurs utilisateurs). Mais il est très fréquent que ces services extérieurs puissent tomber en panne. Donc que faire en cas d'erreur ? Plusieurs solutions sont envisageables pour pallier à ça :

- renvoyer à l'utilisateur un **message d'erreur** : problématique car il ne pourra accéder au site
- **ignorer l'erreur** et l'utilisateur peut accéder à sa page : problématique car on ne peut plus savoir d'où il vient
- **renvoyer un message** au serveur à une fréquence *f* jusqu'à ce que le serveur remarche à nouveau.

Cette dernière solution permet de ne **pas perdre l'information** que l'on souhaite collecter sur l'utilisateur tout en lui permettant d'**accéder à notre site**.
Cependant, si les appels au serveur externes sont faits avant que la page s'affiche (donc de manière **asynchrone**), le **temps d'attente** pour le client peut être **très long**. Une solution est donc d'effectuer ces calculs de manière **asynchrone**.

![Schéma de l'asynchronicité](../image/Schéma6.1.png "Schéma explicatif asynchronicité")

*Source : Openclassrooms*

De manière à ce que ce système permette d'effectuer les actions en **quasi temps instantané** tout en étant **tolérant aux pannes** du serveur du service externe, deux éléments ont été ajouté. La **file d'attente de message** permet de stocker tous les messages et de les faire passer les uns après les autres. Le **traitement de flux de données** permet de traiter les messages les uns à la suite des autres.

Ainsi, les **points importants** d'un système de gestion de données en temps réel sont :

- Une faible latence ;
- Une file d'attente de messages qui avance rapidement ;
- Une tolérance aux pannes.

Plusieurs outils permettent tout ceci dont **Apache Kafka** et **Apache Storm**. Nous détaillerons leurs fonctionnements maintenant.

## Apache Kafka

Le but principal d'Apache Kafka est de fournir une **plateforme de streaming de données** distribuée, tolérante aux pannes et hautement évolutive pour les applications qui ont besoin de traiter des **flux de données en temps réel**. Kafka permet aux producteurs de publier des messages sur des topics et aux consommateurs de s'abonner à des topics pour consommer ces messages en temps réel.

Kafka est souvent utilisé pour du **traitement en temps réel**, du **traitement d'événements**, de l'**analyse de données** en continu, de la **surveillance** des infrastructures, de la **collecte de données de capteurs** ou encore de la **messagerie**.

Cela correspond à la partie **file de messages** détaillée précédemment. Kafka reçoit tous les messages et les redistribue aux bons services. Il fait office de "centre de distribution de messages".

![Schéma de Kafka](../image/Schéma6.2.png "Schéma explicatif Kafka")

*Source : Openclassrooms*

### Installation et commandes de base

L'installation est un peu compliqué sur Windows et pas toujours forcément bien détaillé dans les articles. Je recommande se plutôt regarder une vidéo comme [celle-ci](https://www.youtube.com/watch?v=BwYFuhVhshI). Toute la suite du cours OpenClassroom est fait pour un Linux. Je détaillerai ici comment faire avec un Windows.

Pour lancer Kafka, il faut lancer deux composants : **Zookeeper** et **Kafka**. Zookeeper permet de gérer les **clusters** de Kafka. On le lance à l'aide de la commande :

```bash
.\bin\windows\zookeeper-server-start.sh .\config\zookeeper.properties
```

On peut ensuite lancer le serveur Kafka comme ceci :

```bash
.\bin\windows\kafka-server-start.sh .\config\zookeeper.properties
```

On peut créer un topic appelé *topic1* (le port 9092 est le port par défaut utilisé mais il peut être modifié) :

```bash
.\bin\windows\kafka-topics.bat --create --bootstrap-server localhost:9092 --topic topic1
```

La commande suivante permet de lister les différents topics créés :

```bash
.\bin\windows\kafka-topics.bat --list --bootstrap-server localhost:9092
```

Remplacer *--list* par *--describe* permet d'avoir plus d'informations sur les partitions.

Il est dès lors possible de produire des messages pour cette partition grâce à la commande :

```bash
.\bin\windows\kafka-console-producer.bat --broker-list localhost:9092 --topic topic1
```

On peut dès lors entrer toutes les données que l'on souhaite.

On peut écouter les messages envoyés. Dans un autre terminal, on lance la commande :

```bash
.\bin\windows\kafka-console-consumer.bat --topic topic1 --bootstrap-server localhost:9092
```

On vérifie bien que quand on envoie des données, on les récupère dans ce second terminal.

### Utilisation

Dans la suite du tutoriel, on s'intéresse à la **gestion d'une flotte de vélo en temps réel**. Pour cela, on récupère les données de l'API Decault. Le but est d'afficher le delta du nombre de vélos dans les différentes stations. En suivant le tutoriel, on construit progressivement le projet souhaité. Toutes les étapes sont très clairement expliquées et les commentaires permettent de bien comprendre ce que l'on fait.

Jusque là, le code ne s'effectue que sur un serveur en local sur notre ordinateur. Pour des calculs avec plus de données et/ou plus complexe, il est possible de le **déployer sur plusieurs serveurs en parallèle** (ici tous sur notre ordinateur). Cela permet de répéter les informations et donc d'être **tolérant aux pannes des serveurs**. On crée un deuxième serveur :

```bash
$ vim config/server1.properties
broker.id=1  ## L'id doit être différent pour chaque server
listeners=PLAINTEXT://:9093  ## Chaque serveur est sur un port différent
log.dirs=/tmp/kafka-logs-1
```

De la même manière, on peut ajouter des serveurs Zookeeper pour qu'ils fonctionnent en parallèle.

### Projet

Par la suite, j'ai réalisé un mini-projet avec Storm. Le but est de savoir grâce à l'API précédemment utilisé quand une borne de vélo devient vide ou n'est plus vide.
Le code que j'ai réalisé est disponible sur [ce github](https://github.com/ThomasP04/MON6-Kafka).

## Apache Storm

On a vu à la partie précédente que Kafka permettait de faire la distribution des messages. Storm permet lui de les **traiter**.
Un site peut par exemple transmettre des logs sur ses visites (date et heure, url de la page visitée, ...). Tout ceci peut permettre de tirer beaucoup d'informations utiles (nombre de visite de chaque page, ...). Mais, ceci nécessite un travail préalable : décomposition de chaque ligne pour en **extraire les données** et **transmission** de ces données pour effectuer les calculs. A grande échelle, cela nécessite une **architecture distribuée** afin d'être résistant aux pannes.

### Présentation

Storm possède une architecture comme suit :

![Schéma de Storm](../image/Schéma6.3.png "Schéma explicatif Storm")

*Source : Openclassrooms*

Les messages ou **tuples** sont **créés** par des composants appelés *spouts*, qui sont configurés pour **lire les données**.
Une fois les tuples créés, ils sont envoyés à différents *bolts* pour être traités. Les *bolts* sont les composants de traitement de Storm, qui effectuent des **opérations sur les tuples** tels que des filtrages, des agrégations, des jointures, etc. Ils peuvent être configurés pour exécuter des tâches spécifiques en parallèle, afin de permettre le traitement de flux de données massifs.
Un même message peut être envoyé à plusieurs *bolts*. Cela permet à Storm d'être tolérant aux pannes (en cas de défaillance d'un *bolt* ou d'un nœud du cluster, le traitement des messages peut continuer sans interruption).
De plus, les *bolts* peuvent également émettre de nouveaux messages vers d'autres *bolts* pour effectuer des traitements supplémentaires sur les données.
Tout ce processus peut être **distribué** sur différentes machines.

### Conclusion

Le tutoriel d'Openclassroom permet de bien comprendre la théorie derrière la gestion de données en temps réel. Chaque point est bien détaillé et des exemples sont données. De plus, l'introduction de Kafka et Storm permet de tester et de voir ce qu'on peut réaliser en pratique.

## Liens

[Documentation de Kafka](https://kafka.apache.org/documentation/)
[Documentation de Storm](https://storm.apache.org/)
