---
layout: layout/post.njk

title: "Developpement Mobile avec Flutter"
authors:
  - Savinien Laeuffer

---

<!-- début résumé -->
Développement mobile avec Flutter (Drift et FlutterBase)
<!-- fin résumé -->

## Description

Ayant déjà fait du développement mobile en entreprise, j'ai pu apprendre à maitriser Flutter afin de développer des applications mobiles dans le secteur médical. Cependant tout mon stage s'est focalisé sur la partie front-end des applications mobiles et je n'ai pas pu m'instruire sur la partie back-end qui peut être aussi gérée par Flutter, et quelques plugins utiles. Comme je souhaite probablement trouver un stage dans ce domaine, il me faut acquérir des connaissances dans cette branche afin d'avoir un spectre large de compétences sur le développement mobile. Aussi cela m'aidera énormément pour le projet 3A qui traite aussi du développement mobile.

## Qu'est-ce que Flutter, Floor, Firebase ?

##### Flutter

***Flutter*** est un **framework open source**  développé par Google utilisé dans la **création d'applications mobiles** Android mais aussi iOS. Il est basé sur le langage **Dart** aussi créé par Google, et se compile assez vite selon l'application que l'on fait. Il permet de construire des interfaces utilisateurs très esthétique et très rapidement grâce à un système de composants (components) déjà inclus dans Flutter mais qui sont tout aussi personnalisables (à la manière de Bootstrap pour le développement web)

<div style="width:100%;">
  <figure style="text-align:center">
    <img style="height:200px; margin-left: auto; margin-right: auto" src="../flutter.png">
    <figcaption>Logo de lutter</figcaption>
  </figure>
</div>

Je note deux avantages majeurs de ce framework:
- Tout d'abord il permet de développer des applications en même temps pour Android et iOS avec le **même code**. 
- Aussi, une fonctionnalité "Hot Reload" est disponible et facilite énormément le développement. Au lieu de compiler, ou de relancer l'application pour afficher les changements de code que l'on a fait, le bouton Hot Reload permet automatiquement d'**actualiser l'application** sur la vue que l'on est en train de consulter. Malheuremsent cela ne marche pas tout le temps lorsque l'on travaille sur la partie back-end, notamment les bases de données où il faut souvent désinstaller l'application et la réinstaller pour retrouver une BDD vierge.

##### Drift

***Drift***, anciennement Moor, est une librairie Flutter basé sur SQLite. Il fournit à nos applications mobiles un **système de persistence de données**. Drift a beaucoup d'avantages par rapport à une simple librairie comme SQFlite (SQlite pour Flutter):
- Un système de streaming des données: dès qu'une donnée change, le système est notifié et actualisé sans requête supplémentaire
- Une gestion des types plus pratique et efficace
- Une API en Dart qui permet d'écrire des requêtes plus simples sans passer par du SQL.

##### Firebase

***Firebase*** est une plateforme de développement d'application créée par Google qui va nous fournir les outils nécessaires à la **création d'une base de données sur un serveur** afin de stocker nos données d'applications.
***Flutterfire*** est le **package** faisant le lien entre Firebase et nos applications mobiles en Flutter que nous allons installer afin de stocker sur le serveur nos données stockée localement grâce à Drift.

<div style="width:100%;">
  <figure style="text-align:center">
    <img style="height:200px; margin-left: auto; margin-right: auto" src="../flutterfire.png">
    <figcaption>Flutter et Firebase</figcaption>
  </figure>
</div>

## Persistence des données (Drift)

##### Installation de Drift

Pour installer Drift à notre projet flutter, il faut ajouter plusieurs packages aux dépences dans notre fichier ```public.yaml```:

```yaml
dependencies:
  drift: ^2.2.0
  sqlite3_flutter_libs: ^0.5.0
  path_provider: ^2.0.0
  path: ^1.8.2

dev_dependencies:
  drift_dev: ^2.2.0+1
  build_runner: ^2.2.1
```

On télécharge et installe finalement les packages en lançant dans notre terminal la commande ```flutter pub get``` (si problème avec des packages déjà existant, on peut lancer ```flutter clean``` avant)

##### Déclarer les tables


## Sources

- [Documentation Flutter](https://docs.flutter.dev/)
- [Material](https://m3.material.io/develop/flutter)
- [Documentation Drift](https://drift.simonbinder.eu/docs/)
- [Documentation Flutterfire](https://firebase.flutter.dev/docs/overview)