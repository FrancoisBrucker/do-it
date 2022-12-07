---
layout: layout/post.njk

title: "Possible MON Temps 2 - Splunk"
authors:
  - Kasimir Romer

---
<!-- Début Résumé -->
Présentation rapide de Splunk
<!-- fin résumé -->

## Splunk
Splunk est un logiciel de gestion des logs. Il permet de collecter, indexer et rechercher des logs. Il permet aussi de visualiser les logs sous forme de graphiques.
Splunk est souvent utilisé par les équipes de sécurité informatique, car il est très puissant pour assembler les logs de différents systèmes et les rendre ainsi facilement consultables.
La formation de base "Splunk Fundamentals" devrait durer environ 10-12 heures, le volume serait donc très bien adapté au MON.

## Formation
### What is Splunk?
- get data from **any source** and add it to an index which can be searched
- **search** the index
- **visualize** the data
- **monitor** the data
- **alert** on the data

### Splunk Fundamentals
- three components: search head, indexer, forwarder
#### Search Head
This is the user interface, it is the place where you search the index and visualize the data.

#### Indexer
Takes the raw data and indexes it. The indexer is the place where the data is stored.

#### Forwarder
The forwarder is the component that collects the data from the sources and sends it to the indexer.

Data Pipeline: Input, Parsing, Indexing, Searching, Visualizing


## Sources
- https://education.splunk.com/free
- https://www.splunk.com/pdfs/training/splunk-education-student-handbook.pdf
- https://www.youtube.com/list=PLY2f3p7xyMiTUbUo0A_lBFEwj6KdH0nFy
