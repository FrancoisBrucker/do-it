---
layout: layout/mon.njk

title: "MON 2.2 - Programmation Orientée Objet (POO)"
authors:
  - Inès Kebbab

date: 2024-11-20
tags: 
  - "temps 2"
  - "info"
  - "POO"

résumé: "Bases de la POO avec Python, quelles différences avec la POO en C/C++ ?"
---

L'objectif de ce MON est de comprendre les bases de la Programmation Objet à partir du cours de M. Brucker. Ce cours utilisant Python et ayant suivi l'électif sur le C++ en 2A, je souhaite identifier les différences possibles.

Aussi, l'objectif est de comprendre dans quels cas utilsés de la programmation orientée objet est recommandée, les liens et différences avec d'autres langages dits "non typés", des langages de programmation "impérative" VS "fonctionnelle", ou de programmation évenementielle (n'ayant jamais mis de définition sur chacun de ces termes).

*indiquer les MON/POK en lien*

## Contenu

### Défintions et différences entre les types de langages
En commençant mon étude, je me suis rendue compte que j'étais très confuse sur les différences et les significations entre les termes énoncés ci-dessus, j'opposais par exemple programmation orientée objet et langage non typé. Pour commencer, je propose de refaire un point sur les définitions et cas d'usages.

#### Programmation Orientée Objet et cas d'usages

La programmation objet est un principe de programmation utilisé par la quasi-totalité des langages de programmation (avec des nuances et subtilités entre eux). Elle respose sur l'objectif d'écrire du code qui soit :
- facile à lire
- maintenable
- facile à étendre en ajoutant des fonctionnalités

La programmation orientée objet est souvent opposée à la programmation fonctionnelle dans laquelle les instructions n'ont pas besoin de suivre un ordre particulier lors de l'exécution pour qu'elle réussisse.

**Quels langages sont basés sur de la POO ?**
En fait il est utilisé dans une très grande partie des langages que j'utilise déjà, et notamment JavaScript, C++, Java et Python.

**Pourquoi et quand utiliser de la POO ?**

La POO présente les avantages suivants :

- Cela favorise la factorisation du code (on ne se répète pas) : on ne définit ses méthodes qu'une seule fois dans les classes.
- Lisibilité avec la notation . : on sait clairement à qui s'applique telle ou telle méthode
- Compartimentation du code : chaque partie du code et chaque opération est compartimentée, ce qui permet de les tester et des améliorer indépendamment du reste du code.
- Plutôt que de créer un gros programme complexe, on crée plein de petits programmes indépendants (les objets) qui interagissent entre eux.

La **programmation fonctionnelle** s’inspire dans son écriture des fonctions mathématiques, et a une application plus abstraite. Elle est donc très appréciée pour manipuler et analyser de gros volumes de données mais moins pertinente pour développer une application utile au quotidien. 

Un troisième type de programmation, la **programmation procédurale**, est une méthode qui procède à une analyse descendante pour résoudre un problème, en décomposant le problème en sous-problèmes jusqu’à ce que des actions très simples, aussi appelées procédures, soient identifiées. Cette méthode de programmation peut être très lourde, surtout sur des projets complexes. Elle est adaptée pour des programmes courts.

La POO est donc la méthode à privilégier pour écrire des programmes de taille importante, avec des données complexes.

#### Kézako un langage typé fortement ou faiblement ?
Une fois encore, la nuance dépasse le "typé" ou "non typé". 

Un langage **fortement typé** (comme PHP) va vérifier à la compilation la cohérence entre les données et les types des objets. Cela permet de prévenir les erreurs à l'exécution, comme des erreurs de calcul et des exceptions. Ces langages sont a priori moins permissifs et demandent donc plus de rigueur.

Avec un langage à **typage dynamique** (comme Python ou JavaScript), le typage est affecté au moment de l'exécution du code. Il permet d'être plus souple et rapide pour coder, d'autant plus que les développeurs peuvent manquer d'informations sur le type de la donnée ; néanmoins, cela rend plus difficile le debug. Cela a aussi un impact sur la consommation de mémoire et temps de processeur.

Un langage dit **non typé, ou faiblement typé**, se préoccupe peu des types. Cela offre de la flexibilité sur la manipulation des données. Il y a aussi une notion **d'inférences de types** pour permettre dans des langages typés de demander au compilateur de déterminer le type (une fonctionnalité à utiliser avec modération).

#### Programmation déclarative VS impérative

Dans un système impératif, les variables doivent être définies, remplies, ajoutées, formatées et affichées, etc. et on se concentre sur le *comment*. (ex. Python, PHP, Java, JavaScript, C++)

Dans le système déclaratif, on se concentre sur le contenu et le *quoi*. Par exemple, les pages HTML sont déclaratives car elles décrivent ce que contient une page (texte, titres, paragraphes, etc.) et non comment les afficher (positionnement, couleurs, polices de caractères…). (Ex. HMTL)

#### Kézako : les autres définitions  

**Programmation événementielle**

> La programmation événementielle est un paradigme de programmation très utiliser dans les interfaces graphiques. Cette méthode consiste à réagir à des événements issus du programme comme de cliquer sur un bouton, appuyer sur une touche, etc.
[Source](https://francoisbrucker.github.io/cours_informatique/cours/coder-et-d%C3%A9velopper/programmation-%C3%A9v%C3%A8nementielle/)

**Langage interprété VS natif**

Un langage interprété nécessite un interpréteur pour pouvoir exécuter le code. (ex. Python, HTML).


### Les notions de bases de la POO

Pour reprendre la programmation Orientée Objet sur de bonnes bases, j'ai suivi le cours de F. Brucker utilisant Python et trouvable au lien suivant : [Programmation Objet](https://francoisbrucker.github.io/cours_informatique/cours/coder-et-d%C3%A9velopper/programmation-objet/)

#### Ce qu'il faut en retenir, dans l'esprit de la POO

- **Objets** (avec attributs et méthodes) et **classes** + constructeur
- **Diagramme UML** (représentation des classes, leurs attributs et méthodes)
- **Composition et agrégation** pour lier des classes entre elles :
  - **agrégation:** les objets sont créés en dehors de la classe (ex. piles et télécommande).
  - **composition:** les objets sont créés au sein de la classe qui les utilise (ex. livre et pages).
- **Copie et modification d'objets,** liens et impacts sur la définition et le choix des méthodes (en utilisant de préférence des objets non modifiables).
- **Héritage:** organiser et réutiliser des classes, à condition que les classes "filles" soit plus spécifique que celle "mère" (ex. classe mère "Personne" / classes filles "Etudiant" ou "Enseignant"). 
  - L'objectif est qu'une majorité des méthodes est réutilisée pour la classe fille, et non que la totalité des méthodes soient réécrites dans la classe fille.
  - Intérêt dans le cadre de l'usage d'une bibliothèque.
  - Notion de hiérarchie de classes (racine, *mro* en Python) : on peut définir une classe "object" de laquelle héritera toutes les autres classes pour créer des méthodes et comportements par défaut.
  - Héritage multiple : conflits dans les méthodes. => Usage de composition.
- **Design Patterns**, notion que j'ai découverte à la fin du cours.

> Les design patterns, ou façons de faire, sont pour ainsi dire de l'algorithmie objet : ils permettent de résoudre nombre de problèmes courants en développement et d'éviter les erreurs classiques, aussi appelées **anti-pattern**. 
> 
> Il existe 3 grands types de design pattern: 
> 
> - les types creational qui créent des objets.
> 
> - les types structural qui mettent les objets en relation.
>
> - les types behavioural qui regroupent les objets ayant même comportement.


Le cours aborde aussi le test son code. J'ai noté le point de vigilence suivant avec la POO :
> Attention, dans la mesure du possible ne pas utiliser les attributs de classes. 
> On ne vérifie que les résultats de la méthode, pas comment l'objet stocke ses informations.
>
> Chaque méthode doit être testé.
>
> Chaque test doit être indépendant.


#### Avantages et inconvénients de la POO

✅ Les avantages :
- Bien pour modéliser des comportements réels et des programmes complexes, grâce à des termes explicites/modulables (pour le développement d'outils métiers par exemple);
- Langage robuste.


❌ Les inconvénients :
- Héritage - Tomber en désuétude ? et des ressources parfois désuettes
- Peu intuitive : Elle sera moins facile d'accès que l'approche procédurale, généralement la première à être apprise lorsqu'on débute, ou l'approche fonctionnelle qui parlera tout de suite aux matheux. 
- Exigeante : La POO demande une grande rigueur dans le code pour que ses concepts s'appliquent correctement.

#### Comparaison Python VS C++
🐍 **Python:** 

- Langage polyvalent et qui n'est pas limité à la POO ;
- Facile à apprendre ; 
- Usage de conventions (`self` le 1er paramètre de chaque méthode, `__init__`) ;
- Fonction de propriétés
- Lorsque vous souhaitez créer des programmes faciles à modifier et à maintenir au fil du temps.

🧮 **C++:** 
- Le langage est plus rapide à exécuter, car il s'agit d'un langage compilé ;
- Il demande du temps pour bien apprendre ;
- C'est un "vieux" langage, les recherches en ligne peuvent donc fournir des informations désuettes voire obsolètes.

### Conclusion du MON
J'ai apprécié lors de ce MON revoir les bases de la programmation orientée objet avec des exemples concrets et clairs.

De plus, cela m'a permis de refaire un point sur les définitions sur les différentes typologies de programmation.