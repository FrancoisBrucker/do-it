---
layout: layout/mon.njk

title: "Introduction au back-end par Django"

authors:
  - Jeffrey Edisah

date: 2023-01-04

tags:
  - 'temps 2'
  - 'info'
  - 'back'
  - 'python'
  - 'django'
---
<!-- début résumé -->

Découverte des principes du backend avec le framework Python Django
Pré-requis : Web Front 1

<!-- fin résumé -->

Ce MON fait suite à mon 1er MON Web Front 1. Après celui-ci, on peut écrire des pages webs plutôt simples et pas très dynamiques (quoique avec JavaScript beaucoup plus quand même). 
C'est très utile quand on veut seulement afficher des choses, mais pour faire des choses dynamiques ou bien récupérer et utiliser des données ce n'est pas très pratique. 
Je veux donc voir à travers ce MON comment faire des sites dynamiques qui permettent l'envoi ou la récupération de données avec les langages back-end et en particulier le framework Django du langage Python. 

Les ressources que j'utilise sont :

- [Les principes de la programmation coté serveur de Mozilla](https://developer.mozilla.org/fr/docs/Learn/Server-side)
- [Le tutoriel Django pour faire une application de sondages](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)
  
 J'utiliserai cette page pour vous montrer ce que je retire principalement de ces ressources.

 ## Pourquoi Django ?

 Avec la multitude de langages et de frameworks possibles, on peut me demander pourquoi Django. Tout d'abord, parce que je trouve la documentation très claire et exhaustive, ensuite parce que le framework a des outils déjà tout fait, ce qui permet de prendre un niveau d'abstraction au début et de vraiment comprendre les concepts facilement.
 Avec une ligne dans le terminal, on peut créer le template d'une application ou d'un projet avec toute la configuration nécessaire déjà en place, ce qui clarifie beaucoup les choses. A terme, on peut rentrer plus en détails sur chacune des options de configuration.


 ## La relation client-serveur

 Au coeur de la programmation backend, il y a la relation client-serveur, le client correspondant au navigateur sur votre machine, et le serveur à une machine distante sur lequel est déployé le site, où se trouve la base de données associée, etc...

 Le client et le serveur communiquent par un système de requêtes et de réponses, système régulé par le protocole HTTP. 
 Le client envoie des requêtes au serveur qui répond ensuite. Les réponses peuvent être des données de tout type, des pages webs, des fichiers JSON ou d'autres choses. 
 Les requêtes peuvent elles aussi contenir des fichiers et des données, elle contiennent également des **méthodes** qui renseignent sur le type d'action demander par le client. Ces méthodes sont principalement (la liste n'est pas exhaustive) :

 - GET, pour récupérer des données du serveur
 - POST, pour envoyer des données au serveur
 - PUT, pour mettre à jour des données du serveur
 - DELETE, pour supprimer des données du serveur

Ces méthodes-ci sont celles que l'on retrouve par exemple dans les API CRUD (CREATE, READ, UPDATE, DELETE) et correspondent à la grande majorité de ce qu'on peut être amené à utiliser dans le développement de sites.

La 1ère partie du tutoriel Django permet de se familiariser avec ces principes de requêtes et réponses, tandis que la ressource Mozilla nous en apprend plus sur le protocole HTTP, les en-têtes de réponse et les codes statuts (200, 404).

## Le principe de design MVC (Modèle-Vue-Contrôleur)

La plupart des frameworks et langage de développement coté serveur suivent le principe de design MVC, un principe de séparation du code en 3 parties : le modèle pour les données, la vue pour le front et les pages affichées à l'utilisateur, et le contrôleur pour tout traitement, connexion à la base de données, calcul, etc...

### La Vue

La vue correspond à ce qui est affiché à l'écran de l'utilisateur. La différence avec les pages purement front vues en Web Front 1 est que ces pages-ci peuvent afficher différentes informations selon le client qui affiche les pages, par le biais des sessions et des cookies. 
Ainsi les pages sont écrits à l'aide généralement d'un système de templates (Jinja pour Flask et Django) qui permet d'écrire des pages HTML de manière plus Python Friendly, et ainsi mettre des variables dans nos pages, faire des boucles, ou bien utiliser des conditions. 
C'est également à partir de la vue que l'on peut récupérer des données de nos utilisateurs, avec les formulaires par exemple. La 3ème et 4ème partie du tutoriel Django traite plus en détail des vues.

### Le Modèle

Le modèle sert à la représentation des données. Cette partie du site est généralement nécessaire pour les bases de données relationnelles et sert à définir nos bases de données dans le code plutôt qu'à devoir créer la table de données manuellement (même si il faut créer la base de données à priori).
En Django, cela se fait assez facilement avec le systèmes de classes de Python pour la Programmation Orienté Objet, chacun des attributs d'une classe modèle correspondant à une colonne distinct dans la table, et chaque classe correspondant à une table. la 2ème partie du tutoriel Django revient en détail sur ces connexions.

### Le Contrôleur

Ce qui correspond aux calculs de l'application ou de la page, connecte le modèle et la vue, le centre de traitement de la page. Généralement, la vue et le contrôleur sont écrites ensemble pour la plupart des fonctions simples.


## Sessions

L'une des choses qu'il est intéressante de faire avec les sites web est l'affichage de contenus différents selon les utilisateurs pour une même URL selon qui se connecte sur l'URL, par exemple les profils utilisateurs des réseaux sociaux ou autre.
Ceci est possible à l'aide des **cookies**, fichiers placés sur l'ordinateur des clients afin de reconnaître celui-ci. Cette notion est vu à travers la session administrateur dans le tutoriel.


## Conclusion

Ces deux ressources en tandem sont très appropriés à mon sens pour avoir une vision du backend en tant que débutant. Si les principes du backend sont déjà connus, le tutoriel Django permet d'acquérir rapidement les bases du framework et être opérationnel mais peut manquer de profondeur. Dans ce cas, les [guides Django](https://docs.djangoproject.com/en/4.1/topics/) sont plus appropriés selon ce que le développeur veut faire.