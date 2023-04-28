---
layout: layout/mon.njk

title: "Developpement Mobile avec Flutter"
authors:
  - Savinien Laeuffer
date: 2023-01-04

tags:
  - 'temps 2'
---

<!-- début résumé -->
Développement mobile avec Flutter (Drift et FlutterBase)
<!-- fin résumé -->

## Description

Ayant déjà fait du développement mobile en entreprise, j'ai pu apprendre à maitriser Flutter afin de développer des applications mobiles dans le secteur médical. Cependant tout mon stage s'est focalisé sur la partie front-end des applications mobiles et je n'ai pas pu m'instruire sur la partie back-end qui peut être aussi gérée par Flutter, et quelques plugins utiles. Comme je souhaite probablement trouver un stage dans ce domaine, il me faut acquérir des connaissances dans cette branche afin d'avoir un spectre large de compétences sur le développement mobile. Aussi cela m'aidera énormément pour le projet 3A qui traite aussi du développement mobile.

## Qu'est-ce que Flutter, Drift, Firebase ?

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

{% prerequis "Pré-requis" %}
Dans la suite de ce MON, on considère que Flutter et Dart sont acquis et qu'un projet est déjà créé. Ce tutoriel est destiné à un niveau déjà avancé en Flutter. 
Pour débuter Flutter, on peut se servir de la documentation officielle qui est suffisante et bien faite:
[Documentation de Flutter](https://docs.flutter.dev/)
{% endprerequis %}

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

Créons notre fichier tables.dart, où nous allons pouvoir créer directement en Dart notre classe utilisateur et une classe Category, qui définira plusieurs types d'utilisateurs.

```dart
import 'package:drift/drift.dart';

// Cette ligne affichera d'abord une erreur mais ce fichier se génèrera plus tard
part 'tables.g.dart';

class Users extends Table {
  IntColumn get id => integer().autoIncrement()();
  TextColumn get name => text().withLength(min: 6, max: 32)();
  TextColumn get surname => text().withLength(min: 6, max: 32)();
  TextColumn get email => text().withLength(min: 6, max: 32)();
  IntColumn get category => integer().nullable()();
}

@DataClassName('Category')
class Categories extends Table {
  IntColumn get id => integer().autoIncrement()();
  TextColumn get description => text()();
}

// Les lignes suivantes permettent de dire à Drift de créer les classes des bases de données à partir de ce qu'on a défini plus haut
@DriftDatabase(tables: [Users, Categories])
class MyDatabase extends _$MyDatabase {
}
```

{% info "Remarques" %}
- Attention, par défaut il n'est pas possible d'avoir une valeur null dans une colonne. Une erreur sera affichée si il manque une valeur lors de l'insertion dans la base de données.
Si on veut rendre une valeur nullable, on peut écrire comme suit:
```TextColumn get email => text().withLength(min: 6, max: 32)().nullable();```
- Si une table possède une colonne d'Integers avec une contrainte autoIncrement(), drift considèrera que ce sera la clé primaire par défaut. Si on veut changer la clé primaire on peut overrider cette clé.
{% endinfo %}


Maintenant que nos tables sont créées, il faut lancer la commande ```flutter pub run build_runner build``` afin que le code nécessaire se génère automatiquement. Une classe pour notre base de données et des classes pour nos entitées sont désormais créées.

Pour ouvrir notre base de données, on modifie le code précédent comme ceci:

```dart
// On ajoute les importations nécessaires à l'accès à la base de données
import 'dart:io';
import 'package:drift/native.dart';
import 'package:path_provider/path_provider.dart';
import 'package:path/path.dart' as p;

// On modifie notre classe MyDatabase
@DriftDatabase(tables: [Todos, Categories])
class MyDatabase extends _$MyDatabase {
  MyDatabase() : super(_openConnection());
  @override
  int get schemaVersion => 1;
}

LazyDatabase _openConnection() {
  return LazyDatabase(() async {
    // Crée un fichier db.sqlite qui va être stockée dans le téléphone
    final dbFolder = await getApplicationDocumentsDirectory();
    final file = File(p.join(dbFolder.path, 'db.sqlite'));
    return NativeDatabase.createInBackground(file);
  });
}
```

Notre base de données est créée. Il ne reste plus qu'à créer une instance de ```MyDatabase``` dans le fichier main de notre application.

```dart
Future<void> main() async {
  final database = MyDatabase();

  await database
      .into(database.categories)
      .insert(CategoriesCompanion.insert(description: 'my first category'));

  final allCategories = await database.select(database.categories).get();
  print('Categories in database: $allCategories');
}
```

##### Création de requêtes

Toutes les requêtes se définissent dans notre classe MyDatabase, elles se basent sur du SQL mais se rédigent intégralement en Dart.
Voici donc quelques requêtes afin de comprendre comment on peut les créer soi même.

Récupérer tous les users:

```dart
Future<List<Todo>> get allUsersEntries => select(users).get();
```

Récupérer 10 users avec un décalage (offset) de 5:

```dart
Future<List<Todo>> get getFirstTenUsersOffsetFive => (select(users)..limit(10, offset: 5)).get();
```

Trier les users par nom dans l'ordre alphabétique:

```dart
Future<List<Todo>> get getUsersOrderedByName => (select(users)..orderBy([(u) => OrderingTerm(expression: u.name)])).get();
```

Insérer un utilisateur:

```dart
Future<int> addUser(User entry) {
  return into(todos).insert(entry);
}
```

Update un utilisateur:

```dart
Future updateUser(User entry) {
  return update(users).replace(entry);
}
```

Trouver un utilisateur par son ID et le supprimer de la base de données:

```dart
Future deleteUserByID(int id) {
  return delete(users)..where((u) => u.id.equals(id));
}
```

## Firebase (FlutterFire)

Afin d'utiliser Firebase et pour pouvoir l'incorporer à notre application, il est avant tout nécessaire de se créer un compte Firebase sur le lien ci dessous:
[Site de Firebase](https://firebase.google.com/)

Une fois le compte créé, on ajoute un nouveau projet auquel on fournit le nom (identique à l'application créée). Dès que le projet est créé, on arrive sur notre tableau de bord. On peut désormais utiliser les fonctionalités proposées par Firebase.
Ici nous tenterons de nous servir des outils de base de données, donc Realtime Database.

##### Installation et initialisation de FlutterFire

Pour installer FlutterFire à notre projet flutter, comme précédemment il faut ajouter plusieurs packages aux dépences. On peut le faire rapidement à l'aide de la commande suivante:
```
flutter pub add firebase_core
```

Ensuite pour installer le CLI on lance:
```
dart pub global activate flutterfire_cli
```

Puis on lance cette dernière commande afin de configurer FlutterFire:
```
flutterfire configure
```

Un fichier ```firebase_options.dart``` se sera alors généré et contient toutes les options de configuration.

Il reste désormais à importer les packages dans les fichiers Dart adéquats, par exemple notre fichier ```main.dart```.

```dart
import 'package:firebase_core/firebase_core.dart';
import 'firebase_options.dart';
```

Et finalement, il faut initaliser FlutterFire dans notre fonction ```main```:

```dart
void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );
  runApp(MyApp());
}
```

##### Realtime database

Sur notre page d'accueil de projet sur Firebase, on trouve dans le menu "Créer" l'onglet Realtime Database. On peut se lancer, et créer notre base de données. On choisit l'emplacement et les règles, puis on la crée.

Dans notre application Flutter, on lance la commande:
```
flutter pub add firebase_database
```

Puis, pour rebuilder l'application:
```
flutter run
```

Maintenant, pour pouvoir utiliser Realtime Database dans notre projet, il suffit de l'importer et de créer une instance de FirebaseDatabase:
```dart
import 'package:firebase_database/firebase_database.dart';

FirebaseDatabase database = FirebaseDatabase.instance;
```





## Sources

- [Documentation Flutter](https://docs.flutter.dev/)
- [Material](https://m3.material.io/develop/flutter)
- [Documentation Drift](https://drift.simonbinder.eu/docs/)
- [Documentation Flutterfire](https://firebase.flutter.dev/docs/overview)