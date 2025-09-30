---
layout: layout/mon.njk

title: "MON 3.1 - Bases de JAVA"
authors:
  - Inès Kebbab

date: 2024-12-17
tags: 
  - "temps 3"
  - "info"
  - "Java"
  - "Débutant"

résumé: "Découverte des bases du développement web en Java. Pour quels cas d'usages utiliser ce langage ?"

---

En commençant ce MON, il fallait se rendre à l’évidence : j’avais un maigre souvenir de ce qu’on avait vu en 1A, et je suis frustrée de n’avoir fait aucun projet concret en Java.

🎯 **Objectifs :** 

- Comprendre le serveur SpringBoot que j’ai utilisé lors de mon POK2 et essayé de le faire marcher !
- Faire un projet concret (et aller au delà des notions Java et POO).

🧠 Utile d’avoir revu les bases de la POO avec Python en amont (héritage, polymorphisme) - cf mon MON.


📚 **POK&MON en lien :**


[(POK) Sarah Sebastien](https://francoisbrucker.github.io/do-it/promos/2023-2024/Sarah-Sebastien/pok/temps-2/) ; [Nicolas Ouzoulias](https://francoisbrucker.github.io/do-it/promos/2023-2024/Ouzoulias-Nicolas/mon/temps-1.1/) ; [Agathe Rabachou](https://francoisbrucker.github.io/do-it/promos/2023-2024/Agathe-Rabachou/mon/temps-3.2/) ; [Vladimir Jeantroux](https://francoisbrucker.github.io/do-it/promos/2023-2024/Vladimir-Jeantroux/mon/temps-3-1/) (+ avancé) ; [Samy Diafat](https://francoisbrucker.github.io/do-it/promos/2023-2024/Diafat-Samy/mon/temps-2-2/) ; [Kevin Bernard](https://francoisbrucker.github.io/do-it/promos/2024-2025/Bernard-Kevin/mon/temps-2.2/)

# Java, pourquoi ?

### **Quoi faire avec Java, quel potentiel ?**

Voici ce qu’as présenté Valentin dans son MON Lexique :

> Java est un langage de programmation orienté objet et compilé. […]
> 
> 
> Connu pour sa portabilité grâce à la machine virtuelle Java (JVM), il permet d’écrire une fois du code et de l’exécuter sur n'importe quel système d'exploitation. […]
> 
> Il est particulièrement prisé pour les applications d’entreprise, les systèmes distribués, et les applications Android.
> 
> *Source : [MON “Lexique” de Valentin](https://francoisbrucker.github.io/do-it/promos/2024-2025/Billa-Valentin/mon/temps-1.2/)*
> 

De plus, il est intéressant de connaître Java pour utiliser aussi le développement Android, le langage Kotlin étant largement dérivé du Java: 

> Kotlin est un langage de programmation moderne, concis, et polyvalent qui fonctionne également sur la JVM, tout en étant compatible avec Java. Kotlin est un langage à typage statique et un des principaux langages utilisés pour le développement Android. Il offre de nombreuses améliorations par rapport à Java, telles que la null safety, les lambdas, et une syntaxe plus compacte, ce qui le rend plus agréable à utiliser pour les développeurs tout en réduisant les risques d'erreurs.
> 

Qu’est-ce que cela signifie ?

- Sur Java, il est compliqué d’avoir une valeur nulle par défaut, cela pourrait être source d’erreur. Cela sera plutôt géré par le type “Optional”.
- Pour compenser les contraintes de la programmation objet, les expressions lambda permettent de définir une méthode en dehors d’une classe et permettent de passer une fonction en paramètre d'une méthode. Cela permet d’économiser du code.

### **Quelques chiffres et usages :**

[Source](https://jetbrains.developpez.com/actu/309040/Les-chiffres-cles-de-la-communaute-Java-types-de-logiciels-developpes-secteurs-d-activite-versions-EDI-framework-JetBrains-dresse-le-portrait-du-langage-en-2020/)

- **Pourcentages de développeurs dans chaque pays qui utilisent Java comme langage principal :**
    - La Chine et la Corée du Sud ont les valeurs les plus élevées à environ 51 % et 50 % respectivement en 2020.
    - Les raisons pour lesquelles Java est probablement si populaire dans les 6 premiers pays incluent l'utilisation gratuite de Java, le support gouvernemental et l'open source. C'est notamment le cas de la Chine, de l'Espagne et du Brésil. C'est la base du développement mobile Android en Chine et en Inde, et l'embauche de personnel offshore pour créer des applications mobiles en Java est très répandue, ce qui pourrait expliquer le pic d'utilisation en Inde.
    - Seulement 29% des développeurs l’utilisaient en langage principal en France.
- Selon le *State of the Developer Ecosystem Survey 2020*, **plus d'un tiers des développeurs professionnels utilisent Java comme langage principal** et Java reste le **deuxième langage principal** parmi les développeurs professionnels après JavaScript.

> La plupart des services en entreprises comptent sur Java pour les faire fonctionner. Ce n'est pas seulement le secteur informatique - presque toutes les entreprises, que ce soit dans la distribution, la fabrication ou la banque, ont des services informatiques dans le cadre de leur infrastructure, et ces services, tels que la paie ou la gestion des stocks, sont généralement construits avec Java dans le backend. Java est donc beaucoup utilisé par les développeurs professionnels qui travaillent pour ces entreprises. »
> 
- **Types de logiciels développés avec Java :**
    - À 52 %, les services Web sont la sphère la plus populaire où Java est utilisé selon les résultats de *l'état de l'écosystème des développeurs 2020*.
    - Mais il est aussi beaucoup utilisé pour de la data science, des bases de données et du stockage de donnée.

**Conclusion :**  Java est un langage très répandu et très polyvalent.

## Comment ça marche ?

> *Open Classroom*
> 
> 
> Cela signifie que le code écrit par les développeurs doit subir une transformation avant de pouvoir être exécuté.
> 
> En l'occurrence, le code Java est **compilé** et l’on obtient du **bytecode**. Le bytecode est ensuite exécutable par une **Java Virtual Machine** (JVM).
> 
> Pour pouvoir compiler un code Java, un développeur va utiliser un **Java Development Kit** (JDK).
> 
> Complétons ce tableau avec le **Java Runtime Environment** (JRE) qui permet d’exécuter un programme codé en Java déjà compilé.
> 

## Les frameworks Java

**Mais au fait, c’est quoi un framework concrètement?**

C’est une boîte à outil pour les développeurs. Un framework propose une bibliothèque de fonctionnalités dans laquelle piocher selon les besoins et permet ainsi de gagner du temps pour ne pas tout redévelopper systématiquement.

Il peut aussi permettre d’avoir un standard ou un cadre commun pour construire un projet. Cela permet donc d’avoir une logique commune pour développer, définir les objets, les fonctions... Selon les frameworks, il pourra aussi y avoir des optimisations de performance.

Dans un projet, on va généralement utilisé plusieurs frameworks : il est donc important à l’étape de cadrage de bien identifier les différents besoins du SI pour qu’il y ait une bonne intégration.

**Les frameworks populaires**

Toujours issu du MON Lexique de Valentin Billa, voici les frameworks populaires de Java 

> *Source : [MON “Lexique” de Valentin](https://francoisbrucker.github.io/do-it/promos/2024-2025/Billa-Valentin/mon/temps-1.2/)*
> 
> - **Spring** : Un framework pour créer des applications Java d'entreprise robustes, évolutives et sécurisées.
> - **Hibernate** : Une bibliothèque de mappage objet-relationnel (ORM) qui facilite les interactions avec les bases de données.
> - **JavaFX** : Une bibliothèque pour créer des interfaces graphiques modernes et dynamiques.

**Struts :** le framework permet d’étendre les API Java en JSP (JavaServer Pages ou Jakarta Server Pages), selon l’architecture JSP. Le JSP c’est une technologie qui permet d’écrire du code Java au cœur d’un script HTML pour créer des pages web dynamiques.

> **C’est quoi l’architecture MVC ?** L’architecture Modèle-Vue-Contrôleur (MVC) est destiné aux interfaces graphiques et elle permet de séparer les responsabilités pour améliorer la clarté et la maintenabilité de l'application. Elle est très populaire pour la création d’applications web.

**JSF (JavaServer Faces) :** framework open source qui permet de développer des applications web. 

**Spring :** j’ai compris que Spring est notamment utilisé pour pour la sécurité, mais le framework est très complet car il simplifie la création de nombreux projets (cloud, API, base de données, micro-services, serveurs d’authentification…). Il est open source et régulièrement mis à jour.

**Spark :** utilisé en data science et machine learning, pour ses performances et vitesse - open source.

**Dropwizard:** c’est un Framework pour développer des services web “RESTful” performant.  Il permet de créer des API en Java notamment.

> Un webservice REST c’est une solution qui va permettre d’échanger des données sur Internet en effectuant des requêtes HTTP à un serveur de manière sécurisée. Concrètement, REST API c’est le format d’API le plus fréquent sur le web.

**Apache Tomcat :** régulièrement vu pendant mes recherches, ce n’est pas un Framework mais un logiciel de serveur d’application web, conçue pour les applications développées en Java. Il permet de gérer les servlets,  une classe Java pour gérer les données dynamiquement dans un serveur HTTP et de compiler les pages JSP.

En conclusion, de nombreux frameworks Java permettent de simplifier la création d’applications Web.

### Spring : comment ça marche ?

Spring est un framework open source largement utilisé. Il permet d’avoir des templates pour de nombreux projets en Java, de manière sécurisée. Il a une large bibliothèque de projets, pour créer des projets cloud comme des applications web ou des API en quelques minutes, et il permet de simplifier notamment la création d’objets et de classes ou la gestion des dépendances . 

Spring Boot va permettre d’initialiser un projet et créer toutes les fondations et les bases pour construire plus rapidement son projet. Cela facilite la configuration d’un projet en quelques minutes, et la version par défaut va nécessiter d’apporter peu de modifications pour des utilisations simples.

Si le fond est le même, la différence principale entre le framework Spring et Spring Boot, c’est que Spring Boot est une brique dédiée du framework qui va permettre de s’épargner la configuration de la création d’objets et simplifier comment pointer les classes Java pour lesquelles il sera nécessaire de simplifier et gérer pour nous la créations d’objets.

Un des défauts de Spring Boot, c’est qu’il installe par défaut de nombreuses librairies dont on pourrait ne pas avoir besoin par la suite. De plus, si l’on souhaite vraiment avoir un contrôle plus fin sur sa configuration Java, il semble plus intéressant d’utiliser Spring.

[Vidéo explicative 1](https://www.youtube.com/watch?v=Zxwq3aW9ctU&ab_channel=Telusko) / [Vidéo explicative 2](https://www.youtube.com/watch?v=L0v_3MzC1io&ab_channel=Telusko)

# Zoom théorique

- **La syntaxe**
    
    > Cependant contrairement à Python, le Java est plus exigeant en termes de syntaxe et rien que le fait de devoir utiliser le " **`;`** " et les " **`{}`** " de manière si fréquente n'est pas facile au début et il faut s'y habituer.
    De plus, un programme Java est structuré en **packages** et en **classes**, et aucun code n'est écrit en dehors d'une classe ce qui signifie que toutes les fonctions sont des **méthodes**.
    > 
- **Les méthodes**
    - La méthode **try/catch** est une méthode qui permet de gérer des exceptions pour éviter les bugs. L'idée est d'essayer d'exécuter un morceau de code, et d'en prévoir un autre qui s'exécute dans le cas où le premier génère une erreur.
    - Accesseurs : getters et setters. On les définit dans les classes.
- **Les astuces**
    - Prendre l’habitude de créer des classes public (plutôt que privé).



# Mini-projet Morpion

## Installation

Même si cela semble simple, il faut déjà réussir à installer le JDK. J’ai choisi une version open source, qui ne nécessite pas de licence Oracle, avec OpenJDK 25 disponible à ce lien : [OpenJDK 25](http://jdk.java.net/25/).

Il faut ensuite réussir à modifier le Path pour bien utiliser la dernière version disponible sur l’appareil.

Pour savoir comment choisir son JDK, j’ai trouvé cette [ressource](https://whichjdk.com/) très utile : par exemple, il existe des JDK spécifiques pour créer des applications Java pour un certain support (ex. Microsoft Azure, serveurs SAP…).

## Tuto 1

J’ai regardé ce [premier tuto](https://www.geeksforgeeks.org/tic-tac-toe-game-in-java/) pour créer un Morpion, mais il n’était pas assez détaillé. Cependant, il m’a permis de découvrir le concept de switch : lorsqu’on peut avoir plusieurs branches à tester, plutôt que d’utiliser les techniques classique “if-else-if”, on peut décrire plus finement chaque des solutions. Aussi, je suis assez surprise de la structure de ce programme car j’ai du créer une classe qui fonctionne comme un programme et que nous pouvons exécuter pour lancer le jeu après compilation.

En fait, cette méthode est exécutable grâce à la présence de l’exécutable “main”. Tout le code fonctionnel et qui exige une interaction avec l’utilisateur doit être dans cette méthode.

```java
public class TicTacToe {

  public static void main(String[] args) 
  {
  }
}
```

## Tuto 2

Avec ce [site](https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/learn-Java-tic-tac-toe-game-app-program-source-code-beginner-multi-array), j’ai déjà mieux compris ce qui était nécessaire pour créer le jeu, car le tuto est pas à pas.

Au final, j’étais surprise de voir 

## Démarche

Comme toujours, mon principal défaut est de vouloir tout faire d’un coup. J’ai alors découper la tâche en plus petite brique pour réaliser le code (je me suis appuyée sur les différentes étapes de cette [présentation](https://prezi.com/ei0hysnzco_f/comment-creer-un-jeu-de-morpion-sur-java/)).

En Java :

- **Tâche 1 - Décomposer la partie algorithmique :** concrètement, il faut un tableau, qui est vide initialement ; les cases vides sont remplies de X ou O (tour à tour), en fonction de la demande du joueur. Il faut à chaque tour vérifier dans le tableau s’il y a un gagnant (en analysant si une ligne ou colonne présente une valeur adaptée).
- **Tâche 2 : Créer une grille :** pour créer le tableau, on initie un tableau 3x3, chacune des 9 cases est initialisée avec un chiffre (pour un identifiant unique).
- **Tâche 3 - Afficher la grille :** il s’agit ici d’appeler une méthode qui va imprimer le tableau avec `System.*out*.println()` . On peut l’imprimer ligne par ligne.
- **Tâche 4 - Afficher les règles du jeu :** de la même façon, on imprime dans la console le texte souhaité, avec éventuellement la variable pour indiquer le joueur dont c’est le tour.
- **Tâche 5 - Demander aux joueurs sur quelles cases ils veulent jouer :** pour cela, on utilise la fonction Java util “Scanner” qui permet d’entrer un input par le joueur.

```
  var scanner = new java.util.Scanner(System.in);
  var input = scanner.nextInt();
```

- **Tâche 6 - Placer leurs pions X ou O dans la grille:** il faut ensuite récupérer le numéro de case et modifier le tableau dans la case correspondante. Il faut donc ajouter une variable qui permet de traquer le joueur dont c’est le tour (et qui sera modifier à chaque tour).
- **Tâche 7 - Déterminer s’il y a un gagnant :** on va venir tester à chaque tour si une des 8 combinaisons de colonne/ligne/diagonale remplit la condition pour gagner.
- **Tâche 8 - Afficher un message pour le gagnant :** idem que l’étape 4.
- **Tâche 9 - Déterminer s’il n’y a pas de gagnant :** on implémente un compte de nombre de tours. A chaque début de boucle, on teste si ce compteur est plus petit que 9 - si non, toutes les cases on était remplie et on sort de la boucle.
- **Tâche 10 : Afficher un message s’il n’y a pas de gagnant.** Idem étape 4

Pour l’interface graphique :

- Tâche 11 : Créer une grille à l’aide de boutons
- Tâche 12 : Placer le pion X ou O lorsque le joueur appuie sur l’une des cases

### Interface graphique

**Interface graphique : oui, mais comment ?**

> Après recherches, j'ai trouvé qu'il existait trois API de mise en oeuvre d'interfaces graphiques proposées par l'environnement Java :
> 
> - **AWT (Abstract Window Toolkit)**
> - **Swing**
> - **JavaFX**
> 
> *Source : POK 2 - Sarah Sebastien*

J’ai essayé de faire tourner la librairie JavaFX sans succès. J’ai néanmoins pu faire mes recherches sur son fonctionnement.

Pour créer une application et une interface, on va utiliser la classe Application. Chacune des interfaces créées en java va alors commencer avec :

```java
public class TicTacToeApp extends Application {...}
```

On doit créer une fenêtre dans cette application avec `start(Stage stage)`  . La classe Stage est la classe la plus haute dans JavaFX car elle gère l’ouverture d’une ou plusieurs fenêtres, ainsi que le contenu (c’est l’équivalent de la balise HTML dans un fichier HTML).

On peut ensuite utiliser la classe Scene pour créer un container (le fond) et une Grid pour créer une grille. Pour ouvrir et afficher la fenêtre, on peut ainsi utiliser `stage.show();` .

On va ensuite remplir chacune des cases de la grille avec un objet de la classe Button (bouton). Quand on va jouer, on peut définir qu’à la sélection, on désactive le bouton pour qu’il ne soit plus choisi.

💡 **Ressources:**
[Démarche](https://prezi.com/ei0hysnzco_f/comment-creer-un-jeu-de-morpion-sur-java/) / [Tuto Morpion avec une IA](https://www.toolify.ai/fr/ai-new-fr/le-clbre-jeu-du-morpion-avec-une-ia-ralise-en-java-partie-1-construire-la-logique-574182) / [Tuto 2](https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/learn-Java-tic-tac-toe-game-app-program-source-code-beginner-multi-array)


# **Conclusion**

Si j’avais eu plus de temps, j’aurais aimé explorer le fonctionnement et tester Springboot avec le tuto  : [Spring Framework and Spring Boot Tutorial with Project | 5H25](https://www.youtube.com/watch?v=-Fe0zk-F4OA&ab_channel=Telusko).

J’ai également regardé comment peut être utilisé Java pour le développement web : la plupart des usages se concentre sur la création d’API ou de communication de la page web avec le serveur, mais on n’intègre pas de Java (ou de JSP) directement dans un code HTML à l’instar de JavaScript.

J’ai beaucoup appréciée cette découverte de langage et explorer l’étendu des possibilités du Java. Je pense mieux comprendre la place du Java dans l’écosystème de développement et ses grandes logiques.

Je pense néanmoins moins l’utiliser dans mes projets persos dans le futur proche, car il est possible de réaliser des API dans d’autres langages dans lesquels je me sens plus à l’aise (comme Python) et que je n’ai pas encore besoin de veiller à produire une application sécurisée. 

Ce MON m’a fait me poser la question plus générale: **comment apprendre un nouveau langage rapidement?** Voici quelques conseils que j’ai pu trouvé et que je pourrais appliquer dans le futur lorsque je prendrais en main un nouveau langage :

- Tour d’horizon du sujet / découverte. D’abord : s’imprégner un max des différentes ressources (lire des articles en diagonale, regarder des vidéos en x2…). Pour dégrossir et démystifier.
- Faire une mind map pour organiser les notions, qu’on veut apprendre.
- Regarder des ressources plus concrètes :
    - Commencer par de la pratique et des projets !
    - Toujours mettre en pratique et écrire les choses (pour les retenir, pas les copier coller)
    - Pas forcément finir les projets, ne pas essayer de faire que ça soit parfait.
    - Si besoin de quelque chose, on voit dans ses notes/mind map de quoi on a besoin.
- Cheats sheets par langage pour avoir les infos les plus utiles au quotidien : 80/20


**Les ressources du MON**

Cours OpenClassroom : il ne pas dans le vif du sujet, je ne l'ai pas trouvé intéressant et vite délaissé.

Vidéos recommandées par le POK de Sarah de la chaîne [FormationVidéo](https://www.youtube.com/formationvideo8)