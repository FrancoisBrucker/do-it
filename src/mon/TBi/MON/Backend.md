---
layout: layout/post.njk

title: " Application Web : Comprendre et/ou Mettre en place "

authors:
  - Tuncay Bilgi

tags: ['Backend']
---

<!-- début résumé -->

Savoir comment fonctionne une application Web et enfin comprendre les geeks qui parlent dans un lexique obscure. Mettre en place sa propre application complexe.

<!-- fin résumé -->

Ce MON est un cours sur le Developpement Web, il se concentre sur ce qu'on appelle le Backend. Vous pourrez y apprendre la théorie et aussi la pratique avec la mise en place de votre propre application, plus complexe q'une simple page statique.

Dans ce MON, nous allons voir comment mettre en place une application complete, avec une interface, base de données et un service d'authentification. Nous allons nous concentrer sur ce qu'on appelle le Backend. Je vous presenterais les grands principes d'une application web, et plus précisément, comment structurer un Backend pour qu'il soit maintenable et lisible.
Dans la mesure du possible, tout sera fait proprement. Le but est d'apprendre à structurer un Backend.
Dans un prochain MON, on s'appuiera sur cette application pour tester des classiques de cybersécurité.

{%attention%} Je vous présente une manière de faire les choses, il y en à d'autres et je ne garantie pas que la mienne soit parfaite. Je ne me préoccupe pas de programation par les tests.{%endattention%}

{%details 'Mots clés expliqués dans ce cours'%}
- Frontend, Backend, Base de données
- Framework
- HTML,CSS,JS
- style,layout
- API, REST, ORM, CRUD
- Requêtes
{%enddetails%}

### Ressources :

- Les documentations : 
    - [Nodejs]
    - [Expressjs]
    - [TypeORM]
    - [React]

### Prérequis :

-  Pour la théorie : Avoir un ordinateur, une connexion internet, l'eau courante
- Pour la pratique : Avoir une première expérience avec le developpement web.

### Etapes : 
- Comment marche une application web
- Initialisation du projet : 
  - Frontend
  - Backend
  - Base de données
- Architecture du BackEnd
- Mise en place d'une entitée Account
- Mise en place d'un token de connection

## Comment marche une application web:

### De quoi est constituée une application web ?

Pour notre application, nous avons besoin de trois briques :
Frontend - Backend - Base de données

Ces trois parties ont leurs rôle bien défini :

- Le Frontend est la partie du code qui est présentée à l'utilisateur. C'est le programme qui va afficher ce que l'utlisateur voit et ce avec quoi il va interagir. Le Frontend est envoyé à l'utilisateur, il est donc executé par sa propre machine. Quand vous afficher une page sur intrnet, c'est votre ordinateur qui fait le travail d'afficher les boutons, de regarder quels boutons sont cliqués, de changer de page etc...

- Le Backend est la partie du code qui manipule les fonctionalités complexes, et qui ne concernent pas directement l'affichage. C'est le programme qui va exectuer des fonctions qui permettent de répondre aux attentes de l'utilsateur. Le backend reste sur le serveur, il est executé par celui-ci, contrairement au frontend. Si vous avez une application web qui propose d'interagir avec une IA, l'utilisateur va interagir à travers le frontend, mais l'IA elle même, sera gerée par le Backend.

- La base de donnée, qui permet de stocker des données persistantes. Elle reste sur le serveur, et encor plus, on veut qu'elle soit impénétrable, car nous voulons conserver et cacher les données importantes à notre systèmes, ou les données privées qui concernent nos utilisateurs.

Ces parties communiquent entre elles à travers ce qu'on appelle des requêtes. Le frontend envoie des requêtes au backend, qui lui répond, en lui envoyant une réponse. Pour ecrire cette réponse, le backend peut aller chercher des données dans la base de données. Pour ce faire, il va la questionner, avec language spécifique comme du SQL par exemple.

#### Exemple concret et à la mode en 2023 ChatGPT :

L'utilisateur interagit avec une page qui permet de poser une question à l'IA ChatGPT. Cette page est le frontend, qui est executée par son ordinateur. Quand il rentre sa question et qu'il appuie sur le bouton envoyer, son ordinateur va envoyer une requête au Backend de CHatGPT, qui tourne sur les serveurs de OpenAI. 

Ce backend, va récuperer la question, et la passer à travers l'IA pour avoir une réponse. Il va ensuite renvoyer cette réponse au frontend pour qu'elle soit affichée à l'utilisateur. Enfin, quand l'utilisateur à fini d'interagir, le backend va formatter les données de l'utilisateur : Le nom de compte, la question posée, la réponse renvoyée etc.. et il va placer ces données dans la base de données pour qu'elles y restent longtemps.

La prochaine fois que l'utilisateur vient sur le site de ChatGPT, sans qu'il ait besoin d'interagir, le front va envoyer une requête au back, qui lui demande de récuperer les données de l'utilisteur, le back s'éxecute , va chercher ce qu'il faut dans la base de données, et les donnes au frontend pour que cela soit affiché et que l'utilisateur puisse reprendre une ancienne conversation.

### Les attentes différentes remplies par les trois parties d'une application :

Ces trois parties ayant des rôles bien différents, leurs code n'a rien à voir. Coder du Frontend ne ressemble pas à coder du backend, on n'utilise pas les mêmes fonctions, on ne se pose pas les mêmes questions, et parfois, on n'utilise même pas le même language de programation.
Par exemple : 

- Le frontend à beson d'être du code qui puisse être lu par les navigateurs web.
- Le backend à besoin d'être du code relativement efficace, qui réalise le travail sans gaspiller de ressources et de façon consistente pour tous les utilisteurs.
- La Base de données doit pouvoir être questionnée, on doit pouvoir y retrouver les infrmations nécéssaires facilement.

Pour répondre à ces besoins différents, on utilise d'abords des languages différents :

- Les navigateurs ne comprennent que le HTML, le CSS, le JavaScript et le Webassembly, il est donc impératif de choisir ses languages.
- Pour être efficace, on utilise des languages orientés objet, stables, qui s'executent rapidement, et qui sont potentiellement typés. On utilise le plus souvent du Javascript, du Typescript, du php, du Java, du C# ou dans une moindre mesure, du Python.
- Les bases de données communiquent à travers un language : souvent du SQL ou du grapheQL. Elles ont cependnt toutes leurs particularités et pour cela elles modifie le langage de base, on dit qu'elles utilisent un dialect.

Aussi, pour répondre à ses besoins, on utilise des principes différents :

- Pour le frontend, on pense à l'UI/UX et à la legerté de l'application. On veut envoyer le strict nécéssaire à lu'ilisateur pour que ça s'affiche vite.
- Pour le Backend, on veut de l'efficacité, des temps d'executions bas, la possibilité de gêrer des centaines d'utilisateurs simultanés de façon sécurisée. Pour cela, on pense à l'algorythmie et à la cybersécurité.


### En pratique :

#### Les languages :

Comme dit plus haut, différents besoins, différents languages.
Voici quelques languages couremment utilisés, et une introduction sur leur fonctionnement.

  - HTML,CSS :
Ce couple forme un language qui permet d'afficher des pages sur un navigateur web.
Le html décrit le Layout, c'est à dire toutes les données qui seront affichées, et ouù elles seront affichés. Par exemple une page contient un titre, un paragraphe, un bouton en bas de page etc...
Le CSS décrit le style avec lequel ces données sont affichées. On y décrit quels sont les tailles des paragraphes, la couleur des boutons, la police utilisée etc..

  - Javascript (Js) :
Langage incontournable du developpement web. Le javascript sert en premier lieux à injecter de l'interactivité dans les pages web. Il à le mérite d'être un des seuls langages que tous les navigateurs comprennent, avec les deux citées plus haut. Si un bouton doit incrémenter un compteur, si il faut envoyer une requête au backend, cela se fera avec du javascript. Ce langage est aussi utilisé pour du Backend.

  - Python :
Le python à le mérite d'être simple à appréhender. Il possède des librairies qui facilitent d'autant plus la création de site web. Malheureusement, ce n'est pas un language compris par les navgateurs web, il n'est donc utilisé que pour le backend. Sont utilisation est cependant restrainte. En effet, le langage est lent est gourment en ressources, l'inverse de ce dont en a besoin en Backend.

  - Typescript (ts) :
Language récent qui est un Superset du Js. C'est à dire que c'est du Javascript avec des fonctionnalités en plus. Ces fonctionalités sont principalement les types. Ts est donc un langage typé, c'est à dire que pour définir une variable, il faut lui donner un type qui ne peut pas être changé. Ce language est utilisé autant en Front qu'en Back puisque qu'il est compilé en Javascript. C'est à dire qu'à partir du code en TS, un compilateur va créer un nouveau code en Js. Ce langage est de plus en plus utilisé par les développeur javascript car il facilite le développement. 

- JSON : 
Format de données utilisé par les applications web pour communiquer.

#### Les API :

Pour communiquer entre eux, le Backend et le frontend utilisent des requêtes.
Une requête est un message que le Front va envoyer au Back, ce message va enclancher une fonction dans le back qui finalement, envoie une réponse au front.

Pour pouvoir échanger des requêtes, les programmes doivent être d'accord sur le format des données à échanger. Un de ces format et l'API.
Une API REST est un ensemble de message, que le navugateur peut envoyer à un serveur. Le serveur, si il implémente cette API, doit être en mesure de recevoir le message, de le comprendre et de répondre.

Les API REST s'articulent autour de deux principaux types de messages : GET | POST
Le GET permet au Frontend d'indiquer au Back qu'il lui demande une information. Cele peut être une information de la base de donnée ou une information qui résulte d'in traitement.

Le POST permet au Frontend d'envoyer une donnée au Back, qui pourra ensuite la traiter et l'envoyer à la base de donnée si nécéssaire.

Pour que le serveur puissent traiter les requêtes, ils doivent mettre en place des fnctions qui execute la rêquete. Par exemple si le front demande de créer un nouvel utilisateur à partir d'un nom et d'un mot de passe, le back doit avoir une fonction qui prend un nom et un mot de passe et qui créer un utilisateur avec.
Ces fonction essentielles appartiennent au CRUD : Create READ Update Delete. Le serveur doit savoir faire les 4 pour dire qu'il implémente une API Rest (ou Restful pour l'adjectif).

Faire ce CRUD pour chaque type de données différentes dans le back est d'un ennui mortel, heureusement, il existe des frameworks, qui le font automatiquement pour nous.


#### Les frameworks :

Toutes les applications web possèdent des points communs. Elles proposent par exemple un programme qui tourne en continue et qui écoute les requêtes d'un utilisateur, elles permettent à l'utlisateur de cliquer sur une page et que ce clique soit pris en compte etc..

Au lieu de réinventer la roue depuis zéro et de coder ces fonctionnalités à chaque application, les développeurs ont inventés ce qu'on appelle un framework.

Les frameworks sont des environnements de programation. L'équivalent d'une librairie python. Il permettent de mettre en place rapidement tout ce qui est nécéssaire au programme que l'on veut coder.

Il y a des framworks pour le frontend, des frameworks pour le backend et enfin des frameworks qui allient les deux ensembles, ce qu'on appelle un Meta Framework.

{%details 'Frameworks Front'%}{%enddetails%}
{%details 'Frameworks Back'%}{%enddetails%}
{%details 'Meta Frameworks'%}{%enddetails%}

Les Frameworks sont **opniated** à un certains degré. C'est à dire qu'ils ont une opinion surles manières de faire. Par exemple, faut-il séparer clairement certains composant où les utliser ensemble ? Faut-il écrire une fonction d'une manière ou d'une autre ?

Il est important de choisir un framework dont on supporte les opinions car si on essaye d'aller contre le framework, cela complique énormément la tâche du codeur, alors que l'on veut la faciliter.
Certains frameworks sont par conception très libre. Il y a par exemple Node.js, qui laisse une immense libertée aux utilisateurs. C'est le framework à la base de tous les autres Fraework backend et frontend javascript, à la base de npm.

Pour gerer quels frameworks on utilise, les installer, les mettres à jour etc... on utilise npm. Les commandes npm sont rentrées dans le terminale de commande et permettent gèrer nos projets.

Par exemple si je crée un projet avec certains frameworks, et que quelqu'un veut l'utiliser, il doit d'abord tout installer de la même manière que je l'ai fait sur mon ordinateur. Pour faciliter la tâche, il existe `npm install` qui permet de faire ça d'un coup, magiquement.

##### Exemples :

- Frontend :
[ReactJS]() et [Angular]() nous proposent de créer des composants, qui seront inserés dans une page html et envoyés à l'utilisateur. Ils ont des opnions différentes.
Angular prône une séparation totale des fonctions. La page html ne s'occupe que de l'affichage, le fichier js (javascript) s'occupe de l'interactivitée. Chaque composant est défini par une classe et on doit donc faire attentions à certaines problématiques lié à cela. La communication entre le html et le js est gérée par des fonctions propre à Angular.

React prône plus de flexibilité. Les pages sont en jsx, qui est une fusion de html et de js. Cette page affiche des composants qui sont aussi en jsx et on peut y placer si nécéssaire l'interactivitée. Aussi, les composants sont des fonctions, et ils interagissent entre avec des hooks, des fonctions préconstruites. 

Comme on peut le voir, les deux frameworks répondent aux mêmes besoins, d'une manière (parfois subtilement) différente.

- Backend :
[Sequelize]() et [TypeORM]() sont deux ORMS différents. Un ORM est un framework qui permet de connecter les fonctions ou les objets das notre programme, aux données dans une base de données.
Sequelize nous permet de faire cela en js, et laisse de la liberté au prgrammeur de choisir comment organiser son code.
TypeORM nous force à suivre l'architecture classique d'un backend(que l'on verra plus bas). En plus de cea, il utilise Typescript, qui nous oblige à avoir un language typé (de type Java ou C#). Les types et l'architecture apportent une certaine lourdeur, mais permettent d'avoir un programme solide, plus simpe à maintenir en équipe.

#### Quels Framework utiliser ?

Pour mettre en place ces trois composantes d'un application, nous pouvons : 

  - Ecrire du code à la volée, ne pas utiliser de framework.
  - séparer le code de sorte à avoir trois services, qui fonctionnement en parallèle.
  - Utiliser un Méta-framework, qui permet de regrouper les différentes parties d'une façon cohérente et controllée.

  La première idée est la plus mauvaise idée que vous n'ayez jamais eu de votre vie. On utilise forcément un framework quelquepart, sinon cotre site ressemblera à un blog des années 2000. En plus de cela, vous allez probalement mettre du code n'importe où, ne pas créer de Backend et tout envoyer à l'utilisateur, qui pourra ensuite hacker vos données et vous les revendres alors qu'elles vous appartiennent.

  La deuxième idée et la manière classique de faire les choses, on choisit un framework pour le front , un autre pour le back et on code nos deux parties différentes de façon indépendante. C'est la méthode utilisé dans le projet [FirePixel]() ou dans le POK [Jeu de Grattage](). Cela permet d'avoir un code structuré, qui envoie seuement le nécéssaire à l'utilisateur, qui est relativement protéger contre les cyberattaques (si on respecte les indications du framework). En plus de cela, on peut travailler en équipe sur le projet de manière plus fluide. Certains devs peuvent avancer le front pendan que d'autre avancent le Back, il n'y a pas de conflits car les fichiers sont séparés.

  La troisème idée est plus récente, le plus gros avantage est de ne as avoir à réfléchir. Les Méta Framework sont les plus opiniated de tous,a tels points qu'ils ont même une opinion sur les frameworks que vous devez utiliser. Cela à des avantages, ça permet de ne pas avoir à trouver les frameworks soit même, mais aussi, ces Metaframeworks garantissent une grande compatibilité entre les différents composants de l'applications, et une grande simplicité d'utilisation. Je le conseille au débutant qui ne savent pas quels frameworks utilisé, et aussi aux developpeurs confirmés qui connaissent déjà un farework inclus dans le ackage et qui veulent étendre leurs possibiltés.

  ## Mise en place d'une application : 

  ### Initialisation du projet :

  On commence par se placer dans un dossier vièrge que l'on ouvre dans un éditeur de code (VS code pour moi). On peut faire un git init, voici d'ailleurs le [lien du repository git de ce projet sur mon github](). N'hésitez pas à aller regarder le code directement là-bas, je ne vais pas le copier-coller ici.
  On aura deux dossiers principaux : 
  - Frontend
  - Backend

  En dehors de ces deux fichiers, on viendra placer les fichiers utiles pour la globalité du projet, comme un fichier .env qui possède des variables d'environment, un fichier .gitignore etc..

  #### Frontend :
  On choisit d'utiliser le framework Reactjs, on initialise donc un projet React :
  `npm `

  le front peut être lancé sur le port par défaut 5432 grâce à la commande :
  `npm run dev`

  On ne s'occupe pas plus du front ici, reférez vous à des MON tels que [Angular]() [Angular2]() [React]().

  #### Backend :
  On utlise les Frameworks suivants :

  - Node/Express pour le serveur
  - TypeORM en tant qu'ORM

  on initialise le projet de cette manière :

  `npm `

  On peut y voir plusieurs dossiers, on y revient dans le chapitre d'après.

  #### Base de données :

  On met en place une base de données PostgreSQl. Elle est hébergée à travers un conteneur docker. Je vous invite à voir le [MON Docker]() et/ou de copier coller mon fichier [docker-compose]().
  Vous pouvez aussi mettre en place votre base de données vous même.

  Le plus important est de modifier le fichier data-source.ts . Ce fichier rassemble toutes les informations liées à la conexion à votre base de données. Il est appelé dans les différentes controleurs.
  
  ### Architecture du Backend :



