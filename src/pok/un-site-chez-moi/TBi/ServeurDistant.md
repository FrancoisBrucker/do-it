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
 - Deployer Artblog sur ovh1

## Backlog :

- Mettre en place une fenêtre permanente.
- Bonus : Mettre en place une base de données
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
{%attention%} Ce n'est pas une manière propre de faire sur un serveur de production car on copie tous le repo dans le serveur alors qu'il n'a besoin que de la branche main. Dans un chapitre suivant on recommence plus proprement. {%endattention%}

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

Pour lancer sur un autre port, on va d'abord vérifier qu'il est libre. Par exemple, on active le port 3000 avec `npm run start` et en lancant cette commande dans le Powershell : `Get-NetTCPConnection | where Localport -eq 3000 | select Localport,OwningProcess`, on voit qu'un processus écoute le port 3000. Si le port n'est pas écouté, rien ne s'affiche.

On vérifie que le port 8080 est libre puis on lance l'application sur ce port.

    npm run start
    Get-NetTCPConnection | where Localport -eq 8080 | select Localport,OwningProcess

La dernière commande renvoie : 

    Localport OwningProcess
  --------- -------------
     8080         17516

C'est prometteur. On passe sur le port 10438 qui sera utilisé sur ovh1.

### Faire du git proprement:

  Comme précisé précedement, on a copié l'entierté du repo dans le serveur de production. On oublie et on refait.
  On commence par supprimer l'ancien dossier. Je ne sais pas si il y a une bonne manière de le faire et je n'ai pas regardé. Ici, je supprime le dossier et tout ce qu'il y avait dedans, ce qui peut être dangereux.

  {%attention%} Si vous aviez des fichiers importants, tout va sauter, vérifiez 2 fois avant de lancer des commandes qui commencent par rm -r {%endattention%}
    // Dans ovh1 [...]/node
    rm -r artblog/

  Ensuite, on pull proprement le projet :

    git init
    git remote add origin https://github.com/TuncayBilgi/artblog.git
    git pull origin main

  Ici, seul la branche main est clonée sur le serveur. Il suffit de replacer le fichier .env et on peut potentiellement tester le site.
  Pou mettre le repo à jour sur le serveur il suffit de : 

    git fetch origin main
    git reset --hard origin/main
    git clean -fdx // attention cela surpimme tous les fichiers non présent dans la branche, notamment le fichier .env si il existe, cette        commande est optionnelle

  Ou plus simplement :

    git pull origin master

### Letsgo on test enfin :

Tous les préparatifs sont faits, il ne reste qu'à build l'application sur le serveur, puis la lancer :

    npm run build
    npm run start

{%attention%}Ne lancez pas d'applications en mode dev sur le serveur de production, et de manière générale, faites attention aux ports que vous allez utiliser.{%endattention%}

L'application est disponible sur internet à l'adresse `node.curcuma.ovh1.ec-m.fr` et tout marche correctement.

Problème, quand on ferme le terminale, l'application s'arrête.

### Lancer l'application de façon permanente :

En effet, exit le terminal tue tous les processus sur ovh1 qui ont été lancés depuis notre propre terminale. Ce n'est pas ce qu'on veut car ça signifie qu'on ne peut pas eteindre notre ordinateur sans que ça coupe l'application.

Il faut donc créer un terminale sur le serveur ovh1 qui ne s'éteigne pas quand on éteint celui de notre ordinateur. Sous les conseils de M.Brucker, on utilise simplement la commande screen qui permet de lancer des terminaux et des processus en tâche de fond.

    screen -S artblog // Nous emmene dans un nouveau terminale.
    npm run start
    // on tape Ctrl-A + D pour quitter le terminale
    
Et voila l'application tourne de façon permanente sur ovh1.


## Bilan premier sprint : 

J'ai réalisé le travail que j'avais prévu de faire car j'ai eu la chance de ne rencontrer aucun problème.
J'ai cependant été un peu léger sur la correction de bugs du site mais ça n'était pas la priorité et j'ai amplement le temps durant le second sprint.

### Pour le second sprint :

Je compte mettre de vrais articles sur le artblog pour que le site soit intéressant à visiter. De plus, je vais tenter de mettre en place une base de données juste pour me frotter à l'exercie et si possible, mettre en place une automatisation CI/CD qui permet de pull la dernière version stable sur ovh1 puis de build automatiquement.

# Second Sprint :
On va se faciliter la vie en écrivant un script qui va mettre à jour, sur ovh1, le site, en allant chercher la dernière version de artblog et en l'activant, ensuite on pourra lancer ce script depuis un pc distant via ssh.
Dans cette partie, on utilise git en ligne de commande.

## Git CLI :
On commence par mettre à jour notre projet : 

    git add .
    git commit
    git push
    git chechout main
    git merge dev

## Création du script :
La première version sera toute basique, on y inclus ces quelques commandes pour tester : 

    #!/bin/sh

    cd /home/curcuma/node/artblog

    git pull origin main
    npm install
    npm run build
    npm run start

    echo "Prod successfully started"

Ce script a de nombreux problèmes : 

- Il echo "Prod etc.." peu importe de l'état d'éxecution.
- Il ne sauvegarde pas les erreurs.
- Il n'y a aucun test d'effectué.
- Il lance le serveur de prod dans un terminal local, on va le détatcher avec screen.
- On ne peut que lancer tout d'un couop, le script n'est pas optimal si il faut juste redémarrer le serveur.

## Envoie du script :
On copy ce script sur le server avec scp :

    scp /chemin/local/publish.sh utilisteur@serveur:/chemin/distant

Cet envoie doit être effectuer à chaque modifications.

## On essaie maintenant d'executer le script via ssh :

    ssh nom_d_utilisateur@nom_du_serveur "bash /chemin/distant/publish.sh"
    
On a un echo : prod succelfully started, ça s'annonce bien. Quelques erreurs de script plus tard, j'ai une version qui fait ce que je demande.
On essaie maintenant d'améliorer le sustèmepoint par point.

## Creation d'un script pour lancer le script : 
Pas forcément utile mais un tout petit script permettrais de mettre à jour le script serveur puis de le lancer dans la foulée.
Je ne le fais pas car je prefère voir si il y a des erreurs.

Prepare_prod :

    scp publish.sh [...]
    ssh [...] /publish.sh


## Detachement du server dans un terminal en daemon :

on modifie le script : 

    screen -S artblog -dmS npm run start

Cette commande devrait lancer le serveur dans un processus deamon nommé artblog, qui sera toujours en route quand je rompt la liaison ssh.

{%attention%}Problème :  la commande screen -list ne référence pas le processus, je ne peux plus arreter mon serveur. C'est embêtant car impossible de lancer une nouvelle version du serveur si le port est pollué.{%endattention%}

### Debug mode :

On essaie de trouver le problème, pour commencer, le serveur est bien disponible sur node.curcuma.ovh1, ce qui veut dire que le screen à bien fonctionné.

On trouve le processus qui écoute sur mon port 10438 avec :

     ps -ef | grep artblog | awk '{print $2}'
     // cette commande liste les processus, ne garde que ceux qui s'appelent artblog et print l'id du process. on reçoit 304108

On kill le processus: 

    kill 34108
    
Cela à marché.

On l'inclut dans le script : d'abord on kill l'ancien process, ensuite on pourra en recréer un :

    ps -ef | grep artblog |head -n -1 | awk '{print $2}' | xargs kill -15
  
  {%info%}La commande se complique :

  - ps -ef : d'abord je récupere les processus
  - grep artblog : je prend ceux qui contiennent le mot artblog
  - head -n -1 | : je garde tous sauf la dernièere ligne, en effet la derniere ligne est la commande grep elle même et renvoie une erreur par la   suite
  - awk : je print que la deuxieme colonne qui correspond au PID
  - kill : je kill tous les process listés par le print awk.
  {%endinfo%}

### Retour au script :

Le script devient :

#!/bin/sh

    cd /home/curcuma/node/artblog

    git pull origin main
    npm install
    npm run build

    ps -ef | grep artblog | awk '{print $2}' | xargs kill -15
    screen -S artblog -dmS npm run start

    echo "Script ended"

On l'envoit et on test.

## Détacher le lancement du serveur du build :

On créer des options qui permettent ou non de build le serveur.

On crée l'option -h qui affiche de l'aide et -b qui lance le build. Par défaut, on lance un screen.

```

#!/bin/sh

function Build() {
  echo "Pulling from origin..."
  git pull origin main
  echo "Installing dependancies..."
  npm install
  echo "Building ..."
  npm run build
  
}


while getopts ":hb" opt; do
  case $opt in
    h)
      echo "This is the help section of the script test.sh"
      echo "Available options are:"
      echo "-h : display this help section"
      echo "-b : run the Build function"
      exit 0
      ;;
    b)
      Build
      exit 0
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
  esac
done

cd /home/curcuma/node/artblog

ps -ef | grep artblog | head -n -1 | awk '{print $2}' | xargs kill -15
screen -S artblog -dmS npm run start

echo "Script ended"

```

Mais à cause de je ne sais quoi le screen ne marche pas a travers ssh.
On essaie la même chose en utilisant tmux au lieu de screen.

On remplace les lignes liées a screen part 
```
tmux kill-session -t artblogDeamon
tmux new-session -d -s artblogDeamon "npm run start"

```

Et cela fonctionne !

On peut maintenant lancer publish.sh en ssh pour 

- afficher l'aide grâce à -h
- pull la version la plus récente sur git et build le projet grâce à -b
- et publier le serveur.

Tout cela avec par exemple `ssh curcuma@ovh1.ec-m.fr "bash ./node/artblog/publish.sh -h"`










    
    





