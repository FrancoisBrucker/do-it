a---
layout: layout/mon.njk

title: "MON 2.2 : Spring Boot et API REST"
authors:
  - Kévin BERNARD

date: 2024-12-16
tags: 
  - "temps 2"
  - "vert"
  - "java"
  - "spring"
  - "spring boot"
  - "api rest"
  - "maven"
  - "jpa"
  - "backend"

résumé: ""
---

{% prerequis %}
- Java : 2/3 📶
- Backend : 2/3 📶
{% endprerequis %}

{% lien %}
<b>SOURCES</b>
- [Vidéo Youtube de SuperSimpleDev, Backend web development - a complete overview](https://www.youtube.com/watch?v=XBu54nfzxAQ)
- [Vidéo Youtube de conaticus, What is the BEST Backend Language For You?](https://www.youtube.com/watch?v=nVPkwGqhfQI)
- [Vidéo Youtube de Visual Computer Science, What is Spring-Boot Framework? (explained from scratch)](https://www.youtube.com/watch?v=LSEYdU8Dp9Y)
- [Vidéo Youtube de SpringDeveloper, What Is Spring ?](https://www.youtube.com/watch?v=zvLZLFWrbAA)
- [Vidéo Youtube de KANHOUN ACADEMIE, Qu'est-ce que Spring Boot ?, What is Spring Boot?](https://www.youtube.com/watch?v=8xrR49iCW38&t=603s)
- [Vidéo Youtube de Steve Codes, Maven Vs Gradle - Which To Pick](https://www.youtube.com/watch?v=5P9cb0xWyO0)
- [Documentation Vscode, Spring Boot in Visual Studio Code](https://code.visualstudio.com/docs/java/java-spring-boot)
- [Définition d'une API REST sur Red Hat, Une API REST, qu'est-ce que c'est ?](https://www.redhat.com/fr/topics/api/what-is-a-rest-api)
- [Wikipédia, Définition architecture REST](https://fr.wikipedia.org/wiki/Representational_state_transfer)
- [Vidéo Youtube de IBM Technology, What is a REST API? ](https://www.youtube.com/watch?v=lsMQRaeKNDk)
- [Vidéo Youtube de Cameron McKenzie, Advanced Spring Boot Restful APIs Tutorial: Build a Full Spring Boot Web App](https://www.youtube.com/watch?v=9brw7UzFdTA)
- [Vidéo Youtube de Telusko, #17 Spring Data JPA](https://www.youtube.com/watch?v=GkkcZXF-mD8)
- [Vidéo Youtube de Cameron McKenzie, Spring Boot, JPA & Hibernate REST based CRUD Web Project with MySQL & Swagger](https://www.youtube.com/watch?v=Rel5ymzBBFE)
{% endlien %}

{% chemin %}
<b> POK & MON </b>
- [Mon de Amar](https://francoisbrucker.github.io/do-it/promos/2024-2025/Amar-Mbaye/mon/temps-2.2/)
- [MON de Manuela](https://francoisbrucker.github.io/do-it/promos/2024-2025/Manuela-Barreto/mon/temps-1.2/)
- [MON de Baptiste](https://francoisbrucker.github.io/do-it/promos/2024-2025/Baptiste-Audouin/mon/temps-1.1/)
- [POK de Kévin](https://francoisbrucker.github.io/do-it/promos/2024-2025/Bernard-Kevin/pok/temps-2/)
{% endchemin %}

## Table des matières

1. [Introduction](#section1)
2. [Le backend](#section2)
3. [Spring](#section3)
4. [Gradle/Maven](#section4)
5. [API REST](#section5)
6. [API REST dans Spring](#section6)
7. [Conclusion](#section7)

## 1. Introduction <a id="section1"></a>

Ce MON s'inscrit dans la continuité de mon projet pour mon POK 2. J'avais fait l'ébauche du frontend et je suis passé au backend que je voulais faire en Java.
Je me suis donc posé comme question :

<center><b>Comment faire un backend en Java pour gérer une to do list?</b></center>

Ce MON sera mon raisonnement pour répondre à cette question et les choses que j'ai apprises au fur et à mesure. Je veux que ce MON permette à d'autres de savoir si ils veulent travailler en Java en backend et qu'il leur serve de raccourci puisqu'ils seront quoi chercher et pourront s'inspirer de mon travail.

## 2. Le backend <a id="section2"></a>

Dans un premier temps j'ai cherché à comprendre ce qu'était le backend dans un site web.

On a le frontend qui va gérer le visuel que l'on voit sur un site web et le backend correspond à ce qui va enregistrer et gérer nos données sur ce site.

Grâce à la - [Vidéo Youtube de SuperSimpleDev, Backend web development - a complete overview](https://www.youtube.com/watch?v=XBu54nfzxAQ), j'ai pu revoir les bases déjà aborder en Linux avec François BRUCKER et les principaux langages utilisés.

Le backend s'apparente à gérer des requêtes pour manipuler les données de notre database.

J'avais déjà la théorie donc je me suis concentré sur la partie plus appliqué en suivant ces étapes :
- Choisir le langage dans lequel je veux coder : **Java**
- Le framework dans lequel je veux travailler : **Spring**
- Choisir le package manager (qui gère les dépendances/bibliothèque) : **Maven**
- Choisir la database : **MySQL**
- Créer une API REST pour communiquer avec mon frontend

## 3. Spring <a id="section3"></a>

Comme je savais que je voulais coder en Java, j'ai fait le choix du framework avec lequel travailler. Pour Java, le framework le plus populaire de loin est Spring qui est aussi le plus populaire sur les offres de stage que j'ai rencontré sur LinkedIn.

[Vidéo Youtube de conaticus, What is the BEST Backend Language For You?](https://www.youtube.com/watch?v=nVPkwGqhfQI)

### Qu'est-ce que Spring ?

Dans Spring, on a plein de "project" comme ils les appellent. Et j'ai eu beaucoup de mal à comprendre quoi était quoi surtout la différence entre Spring framework et Spring Boot. Ce que j'ai pu trouver c'est que :
- Spring Framework est la boîte à outils avec toutes les fonctionnalités de base d'un développement en Java.
- Spring Boot est une version préconfigurée de Spring Framework adaptée à l'utilisation par un développeur avec des dépendances déjà installées.
- Les "projects" sont des modules que l'on peut ajouter comme dépendances pour simplifier une utilisation spécifique dans le backend, par exemple Spring Data JPA pour la gestion des données ou Spring Security pour la sécurité des données.

Les sources qui m'ont aidé :
[Vidéo Youtube de KANHOUN ACADEMIE, Qu'est-ce que Spring Boot ?, What is Spring Boot?](https://www.youtube.com/watch?v=8xrR49iCW38&t=603s)

## 4. Gradle/Maven <a id="section4"></a>

Quand j'ai compris ce qu'était SpringBoot, j'ai essayé de l'installer dans l'environnement de VSCode. J'ai suivi la [Documentation Vscode, Spring Boot in Visual Studio Code](https://code.visualstudio.com/docs/java/java-spring-boot) pour le faire.

Une fois fait je me suis confronté au choix entre Maven et Gradle.

Les deux sont des outils pour build du Java, autrement dit ils sont ceux qui permettent que le bouton **Run** de lancer le backend. Il y a beaucoup d'étapes qu'ils vont gérer pour lancer le backend :
- test (de type par exemple)
- analyse de code
- scan et gestion des dépendances
- déployement sur un serveur cloud

La différence qui m'a intéressée dans l'utilisation de Gradle ou Maven a été leur popularité (= richesse de documentation, d'exemples). Maven est à ce jour plus populaire que Gradle même si ce dernier est plus performant pour build les applications et scale mieux que Maven.

[Vidéo Youtube de Steve Codes, Maven Vs Gradle - Which To Pick](https://www.youtube.com/watch?v=5P9cb0xWyO0)

## 5. API REST <a id="section5"></a>

Maintenant que je savais quel outil utilisé, je me suis intéressée sur comment gérer mes tâches, les modifier, en ajouter, en supprimer...

Pour cela il me fallait un moyen de communication avec mon frontend pour gérer mes tâches.

Une API est l'interface qui fera la communication entre mon backend et mon frontend via des requêtes et réponses.

Sauf que pour que le frontend et le backend se comprennent il faut qu'il parle la même langue.
Pour cela, on prend l'architecture REST qui définit de règles à respecter.

Une API REST est donc une API qui respecte l'architecture REST.

Je survole simplement le sujet car cela s'éloigne de mon sujet. 
J'ai récupéré ces informations des anciens MON et de vidéo sur le sujet :


## 6. API REST dans Spring <a id="section6"></a>

Je savais quel outil utilisé (Spring Boot avec Maven) et ce que je voulais faire : une API REST. Je me suis ensuite intéressé à comment créer une API REST dans Spring Boot.

### Controller

Première chose à faire, recevoir et traiter les requêtes de mon frontend (ajouter une tâche, en enlever une autre...) pour cela il me fallait un **Controller**.
Il reçoit les requêtes HTTP (POST, GET, PUT, DELETE, PATCH) et les lie avec la bonne fonction permettant d'interagir avec la base de donnée.

Spring nous simplifie la vie avec ``@RestController`` qui informe à notre backend nos intentions de créer un Controller qui respecte l'architecture REST.
Spring propose aussi plein d'outils pour nous faciliter la vie :
- ``@GetMapping("/path")`` + fonction : pour lui dire que l'on va exécuter la fonction si l'on reçoit une requête GET à l'adresse /path. (Avec les variantes ``@PostMapping("/path")``...)
- ``function(@RequestParam int nombre)`` : pour dire à notre backend d'aller chercher la variable ``nom`` dans les paramètres de la requête, idem pour ``@RequestBody`` mais pour le body de la requête.
- ``@GetMapping("/users/{id}")`` + ``public String getUserById(@PathVariable("id") Long userId)`` : quand on reçoit une requête GET à /users/variable on renvoie en fonction de quoi est égale variable. Pour cela on utilise ``@PathVariable(nom_variable)``

Je ne rentre pas dans les détails vous trouverez tout ce qu'il vous faut ici :

### Spring Data JPA

Alors, je savais comment recevoir mes requêtes mais il me fallait les fonctions qui interagiraient avec ma base de données. Pour cela, j'ai utilisé le module Spring Data JPA qui est créé pour cela.

D'un point de vue hors Spring, pour interagir avec une base de données on utilise un ORM (Object Relationnal Mapping) qui va gérer nos demandes de modification de la base de donnée. 
Par exemple, on va dire à l'ORM : "Hey, donne moi cet objet et range celui-la dans la base de donnée" et l'ORM se charger de faire les requêtes SQL.

Parmi les ORMs, le plus utilisé est Hibernate dans l'écosystème Java.
Dans Spring, JPA définit les règles de comportement d'une ORM, et Hibernate les applique pour interagir avec la base de données.

D'un point de vue pratique c'est dans l'interface *Object*Repository qui hérite de JpaRepository que l'on fait les fonctions d'interactions avec la table de donnée *Object*. Comme JpaRepository contient déjà des fonctions comme save, findbyID..., on n'a besoin que de rajouter des méthodes plus spécifiques, comme findByEmail(String email), si nécessaire.

Chaque fichier correspond à un objet de notre modèle sur Spring et chaque objet correspond à une table de données dans notre base de données.

### Connection à la base de données

J'ai mes fonctions CRUD et ma classe Task avec ses attributs

```Java
public class Task {
    private Long id;
    private String title;
    private boolean done;
```

Sauf que mes données n'étaient stockées nulle part. Il me fallait me connecter à ma base de données (en MySQL).
Pour cela j'ai fait la connection avec ma base dans ``src\main\resources\application.properties``:
```Java
# Database
spring.datasource.url = jdbc:mysql://localhost:3306/creature_site
spring.datasource.username = root
spring.datasource.password = password

# Actualisation de la base de données
spring.jpa.hibernate.ddl-auto = update
```

La dernière ligne ``spring.jpa.hibernate.ddl-auto = update
`` indique à Spring que quand je build mon backend, il faut ajouter mes classes comme tables de données dans ma base de données.
De base on a simplement la création d'un objet créé à partir d'une classe qui ajoute une nouvelle ligne à la table correspondante.

A noter qu'en fonction de votre base de données, il faut rajouter une dépendance dans ``pom.xml`` pour la connection. Dans mon cas, vu que j'utilisais MySQL :
```xml
		<dependency>
			<groupId>com.mysql</groupId>
			<artifactId>mysql-connector-j</artifactId>
			<scope>runtime</scope>
		</dependency>
```

En plus, il faut que je signale à Spring que mes classes sont des tables de données de ma base de données :

```Java
@Entity
public class Task {
  @Id
    private Long id;
    private String title;
    private boolean done;
```
---

{% lien %}
Le tutoriel que j'ai suivi :
- [Vidéo Youtube de Cameron McKenzie, Spring Boot, JPA & Hibernate REST based CRUD Web Project with MySQL & Swagger](https://www.youtube.com/watch?v=Rel5ymzBBFE)
Les autres sources qui m'ont aidé :
- [Vidéo Youtube de Cameron McKenzie, Advanced Spring Boot Restful APIs Tutorial: Build a Full Spring Boot Web App](https://www.youtube.com/watch?v=9brw7UzFdTA)
- [Vidéo Youtube de Telusko, #17 Spring Data JPA](https://www.youtube.com/watch?v=GkkcZXF-mD8)
{% endlien %}

## Conclusion <a id="section7"></a>

Pour répondre à ma question :

**Comment faire un backend en Java pour gérer une to do list?**

Grâce à ce MON, j'ai réussi à comprendre comment mettre en pratique mes connaissances sur le backend.
Je peux utiliser Spring Boot avec Maven pour coder une API REST connecté à ma base de données MySQL pour gérer mes tâches.

PS : Petit conseil de la fin, le cours de Java Gradle est vraiment bien fait pour revoir les bases de Java et appronfondir ses connaissjsons sur le sujet.