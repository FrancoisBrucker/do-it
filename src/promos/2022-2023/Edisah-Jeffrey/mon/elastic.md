---
layout: layout/mon.njk

title: "Monitoring avec la stack Elastic (ELK)"

authors:
  - Jeffrey Edisah

date: 2023-01-25

tags:
  - 'temps 2'
  - 'info'
  - 'monitoring'
  - 'base de donnees'
---

<!-- début résumé -->

Introduction à l'Elastic Stack (Elasticsearch, LogStash, Kibana) à des fins de monitoring. ElasticSearch peut également être utilisé dans d'autres contextes.

<!-- fin résumé -->

[Tutoriel de Grafikart (daté)](https://grafikart.fr/tutoriels/elastic-stack-elk-980)
[Documentation Elastic](https://www.elastic.co/guide/index.html#viewall)

## Le Monitoring, c'est quoi ?

Avec une utilisation démocratisée des services clouds(Logiciels Saas, service Google Cloud, AWS, Azure), les différents acteurs (développeurs, utilisateurs, admin sys) doivent être rapidement à jour sur les différents outils qu'ils utilisent, que ce soit les logiciels, les infrastructures, les serveurs, etc.

Dans ce contexte, des outils se sont démocratisées actuellement pour la surveillance, ou bien monitoring, des différents services pour les concepteurs des applications et plateformes, que ce soit les serveurs, les applications, les infrastructures mises en place, les pipelines, les données de sécurité, etc. Ces outils sont des **Application Performances Management(APM)**. Parmi ces outils il y a par exemple :

- Datadog
- DynaTrace
- Splunk, avec un [MON de Kasimir à ce sujet orienté logs de sécurité](../../../KR/MON2-1/)
- ce dont on va parler plus précisément dans ce MON, la stack Elastic (anciennement ELK)


## Elastic Stack

Nous verrons plus en détail la stack Elastic car elle est open source et met en commun de nombreux outils qui peuvent être utiles. Nous allons commencer par faire une présentation de ces différents outils et ensuite les tester sur un projets exemple.

### Elasticsearch

Au coeur de la stack, il y a Elasticsearch, une base de données non relationnelles qui permet des recherches efficaces et rapides.

### Logstash

Un logiciel servant à parser et agréger différents logs pour ensuite les mettre à disposition d'ElasticSearch

### Kibana

Un logiciel de visualisation pour représenter visuellement les différents indicateurs et métriques choisies et définir des seuils d'alerte.

### Beats

Un agent chargé de récupérer les logs et les envoyer dans Elasticsearch. Composé de plusieurs agents pour différents types de fichiers, cet outil peut être utiliser seul ou bien en complément de Logstash.

## Mes tests

Je vais tout d'abord tester les différents logiciels sur le cloud. Si ces tests sont concluants, je testerai alors la stack localement sur une machine virtuelle Linux.

### Test cloud

La mise en place est très simple, avec un essai gratuit du Cloud de 14 jours idéal pour faire mes tests. Le déploiement est assez simple à mettre en place, avec un choix de différents serveurs, services et localisations. Une fois le serveur mis en place on peut alors lancer les différents tests. Mes tests se portent principalement sur Elasticsearch.

#### Ingestion de données

La 1ère phase pour pouvoir utiliser Elasticsearch est tout d'abord de lui injecter des données. Ceci peut être fait de plusieurs manières (Beats ou Logstash par exemple) mais également à l'aide d'API pour les données issues d'autres bases de données (MongoDB, MySQL, Postgre, etc), ou bien de web crawlers, qui scrapent des données sur les sites internet, sous réserve de leur fournir un entry point. 

Ces données sont ensuite placées dans un index qui est exploitable par les autres applications de la stack.

J'ai donc utilisé un web crawler pour récupérer des données du site NBA Stats. J'ai pu récupérer différents headers de différentes pages avec leur body, etc...

#### Visualisation avec Kibana

Les données une fois ingérés sont très facilement exploitables sur Kibana, ou la création de Dashboard et de graphiques est extrêmement simple, avec différentes options de visualisation disponible, une mise en place très simple, et un résultat très propre en seulement 5 min.



### Test local

#### Machine Virtuelle

Pour faire le test local, je vais installer **Vagrant**, outil utile pour tester des builds ou conteneuriser des environnements sur sa propre machine, et [VirtualBox](../../../TA/pentest/) (Vous trouverez à ce lien un MON de Thibault qui utilise VirtualBox pour faire des pentests entre machines virtuelles)

Un tutoriel pour devenir opérationnel vite en Vagrant est disponible [ici](https://developer.hashicorp.com/vagrant/tutorials/getting-started)

#### Tutoriel Grafikart

J'ai suivi le tutoriel de Grafikart jusqu'à un certain point, et j'ai dû également consulter la documentation Elastic pour certains éléments car le tutoriel date de 5 ans. Mais je n'ai pas pu lancer Elasticsearch sur ma machine virtuelle dans les temps.

Mes tests se sont donc pour l'instant cantonner au cloud. Je terminerai ce tutoriel après la présentation.

## Conclusion

Pour conclure, la stack Elastic est une stack très performante en terme de rapidité de recherche, bien que gourmande en ressources. Elle permet en cloud du moins de suivre n'importe quelle métriques que l'on ingère, et de les visualiser avec une très grande facilité, ce qui facilite pour les logs la vision de problèmes (une augmentation du nombre de requêtes, que ce soit en terme de performances ou de sécurité, des erreurs fréquentes, etc)

Dans tous les cas, le monitoring prendra de plus en plus de place dans le cycle de vie d'une application.
