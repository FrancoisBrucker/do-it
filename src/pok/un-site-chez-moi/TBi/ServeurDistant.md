---
layout: layout/post.njk

title: "Artblog Déploiement"
authors:
  - Tuncay Bilgi

tags: ['pok']
---
{% prerequis %} 
- Connaissance de commandes UNIX : ssh,scp,ls,cat,touch etc...
- Accès ssh au serveur ovh1
- Avoir un projet à déployer

 {% endprerequis %}


# Déploiement sur un site distant.

Le but du POK est d'appréhender le déploiement de projets sur un serveur.
Ici, je vais spécifiquement déployer le site développé pendant le POK1 : Artblog, qui est un blog en Javascript, plus précisément, il utilise Next.js et la base de données est hébergée par un service cloud.

### Remarque :

Mon back étant hébergé sur un HeadlessCMS il n'y a pas besoin de déployer la BDD, je vais donc potentiellement créer un mini projet qui contient une BDD classique juste pour me frotter au déploiement complet d'une application.

## Objectifs finaux :

- Pouvoir acceder à mon site sur ovh1.
- Faire en sorte que le contenu se mette à jour sans nécéssiter de redéploiement.

# Gestion de Projet :

Organisation en deux sprints séparés par le point POK.

## Taches Premier sprint :

 - Explorer le serveur ovh1 pour voir comment marche le déploiement
 - Corriger les bugs majeurs du Artblog
 - Build une version du Artblog
 - Bonus : déployer un projet tout simple (Express + front + back + bdd) pour se faire les dents

## Backlog :

- Deployer Artblog sur ovh1
- Bonus : mettre en place une automatisation avec Jenkins.


# Premier sprint:

## Premiers pas

Le serveur est organisée de la même manière pour chaque compte. Mon compte est curcuma donc je prend cela pour exemple et je me concentre sur la partie node puisque le projet que je veut mettre en place est basé sur node.js :

_ Home
|_ Curcuma
 |_django
 |_ flask
 |_java
 |_node
  |_example.js
 |_ readme.txt

 Le **readme** contient les addresses à questionner selon le port que l'on veut atteindre.
 Dans notre cas, on vois dans le fichier `example.js` que l'on utilise le port 10438 et que pour communiquer à travers ce port, on doit envoyer nos requêtes à `node.curcuma.ovh1.ec-m.fr`.

 Avec la commande `node example.js` on lance le programme et on met donc en place notre serveur. Sur un navigateur, node.curcuma.ovh1.ec-m.fr nous renvoie `Hello World`.

 ## Mise en production du Artblog : 

 ### Mise en place du projet sur ovh1 :
{%attention%} Ce n'est pas une manière propre de faire ce que je veux faire sur un serveur de production car on copie tous le repo dans le serveur alors qu'il n'a besoin que de la branche main. Dans un chapitre suivant on recommance plus proprement. {%endattention%}

 Grâce à github, on va cloner le projet dans le dossier node.

 Sur ovh1,on vérifie qu'il y a git : 

    git --version

On clone ensuite notre projet dans le dossier node. Puisque le projet est publique, il n'y a rien de spéciale à faire, sous les conseils de Joe, on utilise directement le lien https. Puisque l'on à jamais utilisé git avec des commande et que nous somme par conséquent un peu nul, on lis la documentation avec `git --help` et on trouve ce qui nous intéresse `git clone` et `git help clone` pour toujours plus de documentation.

On clone :

    git clone https://github.com/TuncayBilgi/artblog.git

Cela créer un dossier artblog avec tous les fichiers nécéssaires dedans, sauf certains que je n'ai pas mis dans le git comme mes fichiers d'environnement qui possèdent les clés d'API.

Ensuite, on éxécute les commandes nécésaires à installer le reste des fichiers :

  npm install

Je copie-colle mon fichier d'environment :

    scp ./.env curcuma@ovh1.ec-m.fr/node


### Test de la mise en production sur mon ordinateur :

Avec Next.js, certaines commandes servent à la mise en production : 

    npm run dev // Lance le projet en mode développement en local
    npm run build // build le projet
    npm run start -p PORT //lance le serveur de production sur le port indiqué

On lance le build, après un certain temps il semble que tout marche, on peut alors essayer de lancer l'application sur un port différent que le port par défaut (3000) car on aura besoin de le faire sur ovh1.

### Changement de port :

Le serveur ovh1 nous octroie un port bien précis pour y mettre notre application. On ne peut donc pas lancer le programme sur n'importe quel port et surement pas le port par défaut. Pour le changer, cela dépend de la technologie utilisée. Avec un serveur node tout simple, il suffit de modifier le port dans le fichier js qui lance le processus. Pour nous, d'après la documentation, nous devon modifier la commande `npm run start`. Cela ce fait dans le fichier package.json où l'on rentre : 

    "start": "next start -p 8080"

Ce qui devrait lancer l'application sur le port 8080.

Pour lancer sur un autre port, on va d'abord vérifier qu'il est libre. Par exemple, on active le port 3000 avec `npm run start` et en lancant cette commande dans le powershell `Get-NetTCPConnection | where Localport -eq 3000 | select Localport,OwningProcess` on voit qu'un processus écoute le port 3000. Si le port n'est pas écouté, rien ne s'affiche.

On vérifie que le port 8080 est libre puis on lance l'application sur ce port.

    npm run start
    Get-NetTCPConnection | where Localport -eq 8080 | select Localport,OwningProcess

La dernière commande renvoie : 

    Localport OwningProcess
  --------- -------------
     8080         17516

C'est prometteur. On passe sur le port 10438 qui sera utilisé sur ovh1.

### Prétexte pour faire du git proprement:

  Comme précisé précedement, on à copier l'entierté du repo dans le serveur de production. On oublie et on refait.
  On commenc par surpimmer l'ancien dossier. Je ne sais pas si il y a une bonne manière de le faire et je n'ai pas regardé. Ici, je suprimme le dossier et tout ce qu'il y avait dedans, ce qui peut être dangereux.

  {%attention%} Si vous aviez des fichiers importants, tout va sauter, vérifiez 2 fois avant de lancer des commandes qui commencent par rm -r {%endattention%}
    // Dans ovh1 [...]/node
    rm -r artblog/

  Ensuite, on pull proprement le projet :

    git init
    git remote add origin https://github.com/TuncayBilgi/artblog.git
    git pull origin main

  Ici, seul la branche master traine sur le serveur. Il suffit de replacer le fichier .env et on peut potentiellement tester le site.
  Pou mettre le repo à jour sur le serveur il suffit de : 

    git fetch origin main
    git reset --hard origin/main
    git clean -fdx // attention cela surpimme tous les fichiers non présent dans la branche, notamment le fichier .env si il existe, cette        commande est optionnelle

  Ou plus simplement 

    git pull origin master

### Letsgo on test enfin :

Tous les préparatifs sont faits, il ne reste qu'à build l'application sur le serveur, puis la lancer :

    npm run build
    npm run start

{%attention%}Ne lancez pas d'applications en mode dev sur le serveur de production, et de manièere générale, faites attentioon aux ports que vous allez utiliser.{%endattention%}

L'application est disponible sur internet à l'adresse `node.curcuma.ovh1.ec-m.fr` et tout marche correctement.

Problème, quand on ferme le terminale, l'application s'arrête.

### Lancer l'application de façon permanante :

En effet, exit le terminal tue tous les processus sur ovh1 qui ont étés lancés depuis notre propre terminale. Ce n'est pas ce qu'on veut car ça signifie que je ne peux pas eteindre min ordinateur sans que ça coupe l'application.

Il faut donc créer un terminale sur le serveur ovh1 qui ne s'éteigne pas quand on éteint celui de notre ordinateur. On tente pour ça d'utiliser tmux, sous les conseils avisés de Nicolas Bert, le lead technique de DO IT.
    





