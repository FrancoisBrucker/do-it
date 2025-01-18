---
layout: layout/mon.njk

title: "Origine et comparaison de langages de programmation"
authors:
  - Matthieu Dufort

date: 2024-09-06
tags: 
  - "temps 1"
  - "Novice"
  - "Langage de programmation"

résumé: "MON traitant des langages de programmation pour comprendre quand préférer un langage par rapport à un autre."
---

{% lien %}

- [TIOBE Index](https://www.tiobe.com/tiobe-index/)
- [RedMonk](https://redmonk.com/sogrady/category/programming-languages/)

{% endlien %}

Donner pour chacun des langages de programmation : l'origine, la raison de sa création, l'utilisation principale, les avantages et les inconvénient.

## Contenu

Pour commencer ce MON, j'ai tout d'abord commencé par chercher des sites référençant tous les langages car beaucoup me sont totalement inconnu. Je me suis ensuite basé sur les sites web en lien ci dessus afin d'en séléctionner une bonne partie et faire un inventaire.

Je vais donc commencer par traiter ces langages en cherchant pour chacun :

- Leur origine
- La raison de leur création
- Leur fonctionnement
- Les avantages
- Les inconvénients
- Leurs cas d'usages

## ![JavaScript](./JS.webp) Javascript

Ce langage a été créé par Brendan Eich en 1995 pour Netscape afin de permettre l'interactivité sur les pages web. Il est utilisé dans le cadre du développement web dans les applications du coté du client mais aussi du coté du serveur (Node.js). Il est indispensable pour le développement web moderne.

{% info %}

Netscape est le premier navigateur web commercial distribué à grande échelle. Il a inspiré Mozilla mais est devenu depuis obsolète.

{% endinfo %}

**Avantages** :

- Facile à apprendre pour les débutants.
- Exécuté dans tous les navigateurs, sans configuration supplémentaire.
- Grande communauté et écosystème de bibliothèques/frameworks (comme React, Angular).

**Inconvénients** :

- Failles de sécurité courantes (XSS, CSRF).
- Moins performant que d'autres langages compilés.
- Problèmes de compatibilité entre navigateurs.

*Niveau de difficulté d'apprentissage* : 2

## ![Python](./Python.webp) Python

Python a été créé par Guido van Rossum en 1991 afin de fournir un langage simple et lisible pour les tâches de scripting. Il est utilisé pour faire du développement web, de la datascience, du scripting et des automatismes. C'est un langage assez facile d'accès et il est donc très recommandé pour les débutants ou pour les projets multidisciplinaire (grâce à sa forte adaptabilité).

**Avantages** :

- Syntaxe claire et lisible.
- Large bibliothèque standard et écosystème (Pandas, NumPy, Django).
- Utilisé dans divers domaines (data science, web, IA).
  
**Inconvénients** :

- Performances inférieures par rapport à des langages compilés.
- Typage dynamique peut mener à des erreurs à l'exécution.
- Gestion de la mémoire peut être moins efficace.

*Niveau de difficulté d'apprentissage* : 2

## ![Java](./Java.webp) Java

Ce langage a été développé par Sun Microsystems en 1995 afin de créer un langage portable pour les appareils embarqués. Il est très utilisé pour le développement d'application d'entreprise, d'application Android ou pour tous les systèmes embarqués. Il permet de gérer des applications volumineuses ou des systèmes complexes.

**Avantages** :

- Portabilité grâce à la JVM (Java Virtual Machine, environnement java tournant sur un ordianteur à distance).
- Grande communauté et support commercial.
- Sécurité et gestion de la mémoire robustes.

**Inconvénients** :

- Verbosité du code, ce qui peut compliquer le développement.
- Performance inférieure à C/C++.
- Délai de démarrage plus long en raison de la compilation à la volée.

*Niveau de difficulté d'apprentissage* : 3

## ![C#](./C1.webp) C#

Le C est développé par Microsoft en 2000 dans le but de créer un langage moderne pour le développement sur la plateforme .NET. Il est utilisé pour le développement d'applications de bureau, de jeux mais aussi d'applications web. Par son fort lien avec Microsoft, il est recommandé pour les applications Windows et les applications d'entreprise

{% info %}

La Microsoft .NET comprend l'ensemble des produits microsoft pour rendre les applications portales sur internet. Il tourne sur un serveur web local qui permet de ne pas externaliser des données privées.

Elle comprend les sytèmes d'exploitations Microsoft, des moyens de communications, des bibliothèques logicielles, visual studio etc.

{% endinfo %}

**Avantages** :

- Syntaxe claire et moderne.
- Intégration avec Visual Studio et l'écosystème Microsoft.
- Support pour la programmation orientée objet et les fonctionnalités modernes (LINQ, async/await).

**Inconvénients** :

- Principalement lié à l'écosystème Microsoft.
- Moins populaire pour le développement web côté serveur (comparé à d'autres langages).
- Temps d'exécution plus long sur des systèmes non-Windows.

*Niveau de difficulté d'apprentissage* : 3

## ![PHP](./php.webp) PHP

Il est créé par Rasmus Lerdorf en 1994 afin de faire du développement web côté serveur. Il est donc utilisé dans le cadre du développement web et surtout pour la gestion de contenu (WordPress...). Il permet d'être efficace et rapide lors du développement d'une application web.

**Avantages** :

- Facile à déployer et à utiliser pour le développement web.
- Large écosystème de frameworks (Laravel, Symfony).
- Intégration facile avec des bases de données (MySQL, PostgreSQL).
  
**Inconvénients** :

- Moins sécurisé par défaut par rapport à d'autres langages.
- Typage faible et dynamique peut conduire à des erreurs.
- Moins performant pour des applications complexes par rapport à d'autres langages.

*Niveau de difficulté d'apprentissage* : 1

## ![C++](./C++.webp) C++

Développé par Bjarne Stroustrup en 1983, il est utilisé afin d'ajouter des fonctionnalités orientées objet à C. Les utilisations se rapproche donc du langage C : développement pour de systèmes, de jeux ainsi que d'application performante. Il est surtout utilisé pour ce dernier point car il est idéal pour répondre à un besoin de performances critiques.

**Avantages** :

- Performances élevées et contrôle bas niveau.
- Portabilité entre différentes plateformes.
- Utilisé dans des domaines exigeants comme le jeu et le système embarqué.
  
**Inconvénients** :

- Syntaxe complexe et difficile à apprendre.
- Gestion manuelle de la mémoire peut mener à des pertes.
- Erreurs de compilation parfois difficiles à déchiffrer.

*Niveau de difficulté d'apprentissage* : 3

## ![Ruby](./Ruby.webp) Ruby

Il est Créé par Yukihiro Matsumoto en 1995 afin de Créer un langage simple et agréable à utiliser. Il est utilisé pour faire des prototypes rapide et un peu de développement Web. Il est donc particulièrement idéal pour la réalisation de MVP (minimum viable product).

**Avantages** :

- Syntaxe élégante et lisible.
- Fortement axé sur la productivité.
- Large communauté et écosystème (bibliothèques).

**Inconvénients** :

- Performances inférieures par rapport à d'autres langages.
- Pas très populaire pour des applications d'entreprise.
- Moins de ressources pour les applications de bas niveau.

*Niveau de difficulté d'apprentissage* : 1

## ![TypeScript](./TypeScript.webp) TypeScript

Tout comme le C, ce langage est développé par Microsoft en 2012. Il cherche a améliorer JavaScript avec un typage statique. Il est donc utilisé aussi pour le développemnt d'application web mais plutôt sur des app plus complexe ou utilisant des framworks modernes (React...). Il est donc recommandé pour les grandes bases de codes.

{% info %}

Le typage statique consiste à définir les types des objets. Cela permet permet de détecter certaines erreurs avant le lancement du programme (erreur de type). Il est aussi possible alors de faire des optimisations en fonction du type. Enfin, le type étant toujours défini, il n'est plus nécessaire de le stocker et cela peut donc aussi gagner de la mémoire.

{% endinfo %}

**Avantages** :

- Typage statique qui aide à détecter les erreurs à la compilation.
- Compatibilité avec le code JavaScript existant.
- Large écosystème de bibliothèques et frameworks.

**Inconvénients** :

- Courbe d'apprentissage pour les développeurs JavaScript.
- Compilation nécessaire, ce qui peut ralentir le développement.
- Plus de complexité par rapport à JavaScript pur.

*Niveau de difficulté d'apprentissage* : 2

## ![Swift](./Swift.webp) Swift

Ce langage est développé par Apple en 2014 pour Remplacer Objective-C pour le développement iOS et macOS. Il est donc utilisé dans des développements pour iOS et macOS et est utilie dans le cadre de projet Apple. On pourrait l'assimiler au C de Microsoft mais du coté Apple.

**Avantages** :

- Syntaxe moderne et claire.
- Performances élevées et sécurité de la mémoire.
- Forte intégration avec les frameworks Apple.

**Inconvénients** :

- Moins de support pour des applications multiplateformes.
- Écosystème moins mature que certains autres langages.
- En constante évolution, ce qui peut introduire des incompatibilités.

*Niveau de difficulté d'apprentissage* : 2

## ![Go](./Go.webp) Go

Développé par Google en 2009, il permet de fournir un langage efficace pour le développement système. Il est utilisé pour le développement de serveurs, microservices et systèmes distribués principalement. Il est idéal pour une application qui a besoin de forte performance.

**Avantages** :

- Performances élevées grâce à la compilation native.
- Conception simple et syntaxe claire.
- Excellent support pour la concurrence.

**Inconvénients** :

- Moins de fonctionnalités orientées objet.
- Erreurs de compilation parfois peu informatives.
- Écosystème plus petit que d'autres langages plus établis.

*Niveau de difficulté d'apprentissage* : 2

## ![Kotlin](./Kotlin.webp) Kotlin

Développé par JetBrains et lancé en 2011, il a pour objectif de créer un langage moderne pour remplacer Java sur Android. Il sert donc pour des application Android mais aussi pour des applications backend. Il est particulièrement recommandé pour le développement d'application mobile moderne.

**Avantages** :

- Syntaxe concise et expressive.
- Interopérabilité avec Java.
- Sécurité des types pour réduire les erreurs de nullité.

**Inconvénients** :

- Moins de documentation et de ressources par rapport à Java.
- Performances légèrement inférieures à Java dans certains cas.
- Courbe d'apprentissage pour les développeurs Java.

*Niveau de difficulté d'apprentissage* : 2

## ![Rust](./Rust.webp) Rust

Ce langage est Développé par Mozilla et lancé en 2010. Il a pour objectifs de fournir un langage performant avec une gestion de la mémoire sécurisée. Il est utilisé pour le développement de système, d'application et de jeux performants. Il est donc idéal lorsque l'on recherche de la sécurité et de la performance pour une application.

**Avantages** :

- Sécurité de la mémoire sans ramasse-miettes.
- Performances élevées et contrôle bas niveau.
- Excellent support pour la concurrence.

**Inconvénients** :

- Courbe d'apprentissage abrupte pour les nouveaux développeurs.
- Syntaxe complexe et détaillée.
- Écosystème plus jeune avec moins de bibliothèques.

*Niveau de difficulté d'apprentissage* : 3

## ![Dart](./Dart.webp) Dart

Développé par Google et lancé en 2011, il permet de créer un langage pour le développement d'applications web et mobiles. Il est donc idéale pour les projets multiplateforme car il est aussi bien compatible mobile que web.

**Avantages** :

- Exécution rapide et performances élevées.
- Utilisé pour le développement d'applications multiplateformes.
- Syntaxe moderne et expressive.

**Inconvénients** :

- Moins de popularité et de ressources par rapport à d'autres langages.
- Courbe d'apprentissage pour les développeurs non familiers avec le paradigme orienté objet.
- Écosystème plus petit.

*Niveau de difficulté d'apprentissage* : 2

## ![Scala](./Scala.webp) Scala

Il est développé par Martin Odersky et lancé en 2003.Son objectif principale est de combiner la programmation orientée objet et la programmation fonctionnelle. Il est utilisé pour le traitement de données ainsi que pour la programmation d'applications d'entreprise. Il permet de traiter des problèmes complexes avec une forte performance.

**Avantages** :

- Prise en charge des paradigmes de programmation modernes.
- Exécution sur la JVM, ce qui offre une grande portabilité.
- Utilisé avec Apache Spark pour le traitement de données massives.

**Inconvénients** :

- Complexité de la syntaxe.
- Courbe d'apprentissage abrupte pour les développeurs Java.
- Moins de ressources et de communautés par rapport à d'autres langages populaires.

*Niveau de difficulté d'apprentissage* : 3

## ![Perl](./Perl.webp) Perl

Créé par Larry Wall en 1987 pour le traitement de texte et le scripting de système. Il est utilisé pour la réalisation de script, l'administration de système et le traitement de texte. Il est principalement recommandé dans le cadre de tache d'automatisation et dans les scripts rapide et peu complexe.

**Avantages** :

- Flexibilité et puissance pour le traitement de texte.
- Large communauté.
- Bon pour l'automatisation et les scripts.

**Inconvénients** :

- Syntaxe parfois difficile à lire.
- Moins de popularité par rapport à d'autres langages modernes.
- Courbe d'apprentissage pour les nouvelles fonctionnalités.

*Niveau de difficulté d'apprentissage* : 1

## ![R](./R.webp) R

Ce langage est développé par Ross Ihaka et Robert Gentleman en 1993 afin d'analyser des données et produire des graphiques. Il est idéal pour des projets de recherche et d'analyse de données dans les domaines d'analyse, de statistique et de science de la données.

**Avantages** :

- Outils puissants pour l'analyse de données et la visualisation.
- Large communauté dans le domaine statistique.
- Bibliothèques riches.

**Inconvénients** :

- Performances inférieures par rapport à d'autres langages.
- Moins adapté pour des applications générales.
- Syntaxe parfois déroutante pour les nouveaux utilisateurs.

*Niveau de difficulté d'apprentissage* : 2

## ![Shell scripting](./ShellScripting.webp) Shell scripting (Bash)

Crée par Brian Fox en 1987, il permet de fournir un interpréteur de commandes pour Unix. Il est très utile pour les administrateur système et les développeurs DevOps afin d'automatiser les taches système et pour faire des scripts de déploiment.

**Avantages** :

- Idéal pour l'automatisation des tâches système.
- Facile à utiliser pour des scripts simples.
- Exécution rapide pour des tâches répétitives.

**Inconvénients** :

- Limité pour des applications complexes.
- Difficultés de débogage.
- Syntaxe parfois déroutante pour les nouveaux utilisateurs.

*Niveau de difficulté d'apprentissage* : 1

## ![Elixir](./Elixir.webp) Elixir

Sorti par José Valim en 2011, c'est un langage fonctionnel pour la création d'applications évolutives. Il est utilisé pour les applications web et les systèmes distribués et est particulièrement idéal pour les applications nécessitant beaucoup de disponibilité.

**Avantages** :

- Basé sur l'architecture Erlang, ce qui le rend idéal pour la concurrence.
- Syntaxe claire et moderne.
- Excellente gestion des erreurs.

**Inconvénients** :

- Moins connu que d'autres langages.
- Moins de ressources et de bibliothèques.
- Courbe d'apprentissage pour les développeurs non familiers avec la programmation fonctionnelle.

*Niveau de difficulté d'apprentissage* : 2

## ![Lua](./Lua.webp) Lua

Ce language provient du Brésil et apparaît en 1993. Il veut mettre a dispoisition un langage léger et extensible pour intégrer des fonctionnalités dans des applications. Il permet le dévelopement de jeux et de système embarqué.

**Avantages** :

- Très léger et rapide.
- Facile à intégrer dans d'autres langages.
- Utilisé largement dans le développement de jeux.

**Inconvénients** :

- Moins de fonctionnalités par rapport à d'autres langages.
- Écosystème plus petit.
- Moins de popularité pour des applications générales.

*Niveau de difficulté d'apprentissage* : 1

## ![ObjectiveC](./ObjectiveC.webp) Objective-C

Il est développé par Brad Cox et Tom Love dans les années 1980.L'objectif de ce langage est de combiner la programmation orientée objet avec C. Il est fait pour le développement d'application MacOS et iOS. Il s'est aujourd'hui fait majoritairement remplacé par swift mais il reste utilisé pour les applications fonctionnant avec avant l'apparition de swift.

**Avantages** :

- Mature et largement utilisé pour les applications iOS.
- Large communauté et documentation.
- Compatibilité avec C et C++.

**Inconvénients** :

- Syntaxe plus complexe par rapport à Swift.
- Moins moderne que d'autres langages.
- En déclin avec l'émergence de Swift.

*Niveau de difficulté d'apprentissage* : 2

## ![SQL](./SQL.webp) SQL (Structured Query Language)

C'est un langage produit en 1970 par IBM qui permet de
gérer et interroger des bases de données relationnelles. Il est utilisé pour la gestion et l'analyse de base de données.

**Avantages** :

- Simplicité: Langage déclaratif qui permet de formuler des requêtes facilement.
- Standardisation: Utilisé par de nombreuses bases de données, comme MySQL, PostgreSQL, Oracle.
- Performance: Optimisé pour les opérations sur les données.

**Inconvénients** :

- Complexité des transactions: Peut devenir complexe avec des requêtes imbriquées.
- Manque de flexibilité: Moins adapté pour des données non structurées.
- Dépendance au schéma: Nécessite une structure de données bien définie.

*Niveau de difficulté d'apprentissage* : 1

## ![HTML](./HTML.webp) HTML (HyperText Markup Language)

Créé par Tim Berners-Lee au début des années 1990 afin de Structurer le contenu sur le web. Il est utilisé uniquement pour apporter de la structure à une page web mais ne permet aucun dynamisme sans l'utilisation d'autre langage.

**Avantages** :

- Standard: Langage de base pour la création de pages web.
- Facilité d'apprentissage: Syntaxe simple et intuitive.
- Interopérabilité: Fonctionne sur tous les navigateurs.

**Inconvénients** :

- Staticité: Ne permet pas d'interaction dynamique sans JavaScript.
- Limité dans la mise en forme: Doit être associé à CSS pour le style.
- Pas de logique de programmation: Pas conçu pour des logiques de calcul ou de décision.

*Niveau de difficulté d'apprentissage* : 1

## ![CSS](./CSS.webp) CSS (Cascading Style Sheets)

Ce langage est créé par le W3C en 1996 pour séparer le contenu et la présentation des pages web. Il se combine avec HTML en apportant le style sur la mise en forme.

**Avantages** :

- Séparation des préoccupations: Permet de séparer le style du contenu HTML.
- Contrôle du design: Facilite la mise en forme et le design des pages web.
- Responsive design: Permet de créer des designs adaptatifs pour différents appareils.

**Inconvénients** :

- Complexité: Peut devenir complexe avec des styles imbriqués et des sélecteurs avancés.
- Compatibilité entre navigateurs: Comportement peut varier selon le navigateur.
- Problèmes de performance: Styles lourds peuvent affecter le temps de chargement des pages.

*Niveau de difficulté d'apprentissage* : 1

## ![XML](./XML.webp) XML (eXtensible Markup Language)

Tout comme le CSS, il est Développé par le W3C dans les années 1990. Il a pour objectif de donner un format flexible pour le stockage et l'échange de données. Il permet la configuration d'application l'échange et le stockage de données

**Avantages** :

- Flexibilité: Peut être utilisé pour structurer une variété de données.
- Validation: Support pour des schémas et des DTD pour valider la structure des données.
- Interopérabilité: Utilisé dans de nombreux systèmes et applications.

**Inconvénients** :

- Verbosity: Plus lourd que JSON, ce qui peut entraîner une surconsommation de bande passante.
- Complexité: Peut être difficile à manipuler sans outils appropriés.
- Performance: Moins performant que des formats comme JSON pour des applications web modernes.

*Niveau de difficulté d'apprentissage* : 1

## ![JSON](./json.webp) JSON (JavaScript Object Notation)

Ce langage, similaire au XML est créé par Douglas Crockford dans les années 2000 afin de Fournir un format plus léger pour l'échange de données. Il permet donc de la même façon l'échange de données entre un serveur et un utilisateur ainsi que la configuration d'applications.

**Avantages** :

- Lisibilité: Format facile à lire et à écrire pour les humains.
- Interopérabilité: Utilisé dans de nombreux langages de programmation.
- Léger: Moins de surcharge que d'autres formats comme XML.

**Inconvénients** :

- Limitations de typage: Ne supporte pas les types de données complexes.
- Sécurité: Vulnérable aux attaques de type injection si mal utilisé.
- Pas de commentaires: Ne permet pas d'inclure des commentaires.

*Niveau de difficulté d'apprentissage* : 1

## ![Fortran](./Fortran.webp) Fortran (Formula Translation)

Créé en 1957 par IBM, sous la direction de John Backus. Il est développé pour effectuer les calculs scientifiques et l'ingénierie. Il excelle dans les calculs intensifs grâce à ses optimisations modernes. Il est massivement utilisé en physique, métérologie, chimie, astrologie et ingénierie pour la réalisation de calcul massif. Il est utilisé dans les super-computers pour la réalisation de simulation comme des simulation climat ou de mécanique des fluides. Il est indispensable pour tous les scientifiques travaillant ayant besoin de grande puissance de calcul

**Avantages** :

- Performances élevées pour les calculs numériques et les applications scientifiques.
- Simplicité pour les calculs mathématiques.
- Interopérabilité avec d'autres langages, peut facilement être intégré avec des langages modernes comme C et Python.

**Inconvénients** :

- Syntaxe est souvent considérée comme vieillissante et moins intuitive que les langages modernes.
- Écosystème limité
- Moins utilisé pour des applications générales, Fortran est très spécialisé pour les calculs scientifiques

*Niveau de difficulté d'apprentissage* : 2

## ![alt text](./COBOL.webp) COBOL (Common Business-Oriented Language)

Il est Créé en 1959 par le CODASYL (Conference on Data Systems Languages) sous la direction de Grace Hopper. COBOL a été conçu pour être un langage de programmation orienté vers les affaires  permettant la gestion de grandes quantités de données. Il est très utilisé dans les secteurs publiques, bancaire et financier pour gérer des grandes quantités de transaction. Il tourne sur des grands ordinateurs gérant des millions de transactions par jours.

**Avantages** :

- Système fiable et utilisé depuis très longtemps.
- Syntaxe très proche du langage naturel (anglais).
- Traitement des données volumineuses.
  
**Inconvénients** :

- Syntaxe verbeuse.
- Manque de développeurs.
- Technologie vieillissante.

*Niveau de difficulté d'apprentissage* : 2

## ![Scratch](./Scratch.webp) Scratch

Ce langage est créé en 2003 au MIT Media Lab par Mitchel Resnick afin d'avoir un langage de programmation visuel destiné à initier es enfants et les débutants. Il permet de créer des projets interactifs facilement sans syntaxe complexe. Il est donc utilisé dans l'éducation pour apprendre les concepts fondamentaux de la programmation. Il peut aussi servir à faire des jeux et services pour enfant.

**Avantages** :

- Facilité d'apprentissage.
- Approche créative et interactive.
- Large communauté de soutien.

**Inconvénients** :

- Limité à des projets simples.
- Manque de fonctionnalités avancées (pas de réseau, gestion de fichier, base de données etc...).
- Transition vers des langages textuels.

*Niveau de difficulté d'apprentissage* : 0

## ![Delphi](./Delphi.webp) Delphi

Delphi a été lancé en 1995 par Borland en tant qu'environnement de développement intégré (IDE) basé sur le langage Object Pascal. Delphi a été créé pour fournir une alternative rapide et efficace à la création d'applications sous Windows. Il combine la puissance du langage Pascal avec un IDE complet permettant le développement rapide d'applications (RAD). Il est très utlisé pour le développement d'application desktop sur windows. Il est possible aussi de faire des applications mobiles. Il permet de faire des interfaces complexes et de bien gérer les bases de données et sera donc majoritairement utilisé dans le cadre de projet ayant besoin de gérer ces deux choses.

**Avantages** :

- Développement rapide d'applications (composants visuels et ses outils intégrés).
- Cross-platform (Windows, macOS, iOS, Android et Linux).
- Excellente gestion des bases de données.

**Inconvénients** :

- Communauté réduite.
- Coût élevé.
- Pas aussi populaire dans les grandes entreprises, souvent remplacé par des langages plus modernes dans les grandes entreprises.

*Niveau de difficulté d'apprentissage* : 1

## ![VisualBasic](./VisualBasic.webp) Visual Basic

Visual Basic a été créé par Microsoft en 1991. il a été conçu pour permettre aux développeurs de créer facilement des applications Windows avec une interface graphique en utilisant un environnement de développement rapide. Il est principalement utilisé pour des applications de bureau. Il permet aussi l'optimisation d'office avec des macros (VBA). Il est aussi pratique pour faire des prototypes rapides. Il est donc utilisé pour des applications simple sans nécessité de performance.

**Avantages** :

- Facilité d'apprentissage.
- Permet de créer des interfaces graphiques complexes avec des outils visuels.
- Intégration avec Windows.

**Inconvénients** :

- Performance limitée
- Langage peu polyvalent
- Support décroissant, version obsolète et plus vraiment mis à jour.

*Niveau de difficulté d'apprentissage* : 1
