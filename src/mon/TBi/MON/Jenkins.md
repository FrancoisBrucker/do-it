---
layout: layout/post.njk

title: "Jenkins"
authors:
  - Tuncay Bilgi

tags: ['Jenkins','CI/CD']
---

# Jenkins, en théorie :

### Objectif :

Comprendre les besoins qui mènent à l'utilisation d'un outil comme Jenkins pour un developpeur fullstack, puis mettre en place un exemple pratique d'utilisation.

### Sujets abordés pendant le MON :

- Qu'est ce que Jenkins ?
- Pourquoi utiliser un tel outil ?
- Les bases
- Exemple d'utilisation concret sur un de mes projets.

{%prerequis%}
- Connaitre le contexte de devleppoment Fullstack.
- Git, Github Desktop marche aussi 
- [Docker](./../Docker).
- Un [projet Nodejs, React](./../../../../pok/un-site-chez-moi/TBi/Artblog) à portée de mains, la doc jenkins en fourni un.
- Avoir 10h de sa vie à donner à la science.
{%endprerequis%}

### Ressources utilisées : 
- [Documentation Jenkins](https://www.jenkins.io/doc/tutorials/)
- [Vidéo introductive sur les concepts](https://www.youtube.com/watch?v=LFDrDnKPOTg&ab_channel=Simplilearn)
- [Magnifique MON sur Docker](./../Docker) 
- [Excellent POK de blog en React](./../../../../pok/un-site-chez-moi/TBi/Artblog) ou [Incroyable POK de plagiat de la FDJ en Svelte](./../../../../)
## Continuous Delivery and Continuous Integration (CI/CD) : 

Ce sont des concepts de développement qui ont plusieurs but : 

 - Améliorer la qualité du code
 - Faciliter la vie des développeurs
 - Développer du code plus rapidement
 - Ajouter les dernières fonctionnalités le plus rapidement possible

Plus particulièrement, **la continuous integration** est l'ensemble de bonnes pratiques et d'outils qui permet de développer,tester et d'integrer le code dans une version prête à être déployée le plus souvent possible.
Traditionnelement, dans une équipe de développeur, la partie front et la partie Back pouvaient être développés par des personnens différentes et mises en communs queques fois avant de lancer des tests. Cette technique est innéficace car elle laisse le temps à des bugs ou des oncompatibilités de grandir sans que l'on s'en rend compte. En effet, si l'on test le système seulement une fois par mois, il est possible de se retroiver avec une version qui ne marche plus dutout et de perdre énormément de temps.
Des outils comme git, github action ou Jenkins permettent aux développeurs de mettre leurs codes en communs puis de lancer une batterie de test sur ce code plusieurs fois par jour. Grâce à cela, on évite la propagations de bugs et finalement, on gagne du temps.

Quand le code est testé est prêt à être déployé il ne reste qu'à ... le déployé!

**La continuous delivery** est l'ensemble d'outils et de pratiques qui permettent de déployer automatiquement la dernièere version fonctionelle du code sur le serveur de production. Cela permet do'ffrir au client une version qui soit toujours fonctionelle et qui possède les derniers ajouts, mises à jours correcctives ou même mises à jour de sécurité.
Onpeut par exemple imaginer une automatisation qui, toute les nuits, récupère toutes les fonctionnalités codées par les développeurs, les teste puis si tout fonctionne, les mets en commun dans une version à jour du code. Cette automatisation pourrait même déployer directement le code.
On appelle cela un *nightly build*.

{% info %}

Par exemple ce site de M.Brucker utilise de la CI/CD :
  - les élèves développent en collaboration grâce à github
  - A chaque commit sur la branche principale, le code est testé par Github action
  - Si les tests passent, le code est déployé sur le site github.io et la dernière version est disponnoble directement sans que M.Bricker est besoin de déployer quoi que ce soit lui-même

  Le problème avec cette manière de procéder est que l'on peut oush un commit monstreux qui détruit le site. Peut importe l'état des tests, le commit sera accepté et ik faudra réparer le code avant de pouvoir déployer le site à nouveau. 

{% endinfo %}

## Qu'est-ce que Jenkins?

{% info %} Une vidéo explicative [ici](https://www.youtube.com/watch?v=LFDrDnKPOTg&ab_channel=Simplilearn) {% endinfo %}

 L'idée est d'un tel outil est de mettre en place un environnement d'intégration continue. C'est à dire que le but est de créer un outil qui permet de developper, tester et pousser le code automatiquement, dès sa création. Par exemple, au lieu d'ajouter de nouvelles fonctionnalités sur notre site web, de faire un commit sur le repository, puis se rendre compte qu'il ne marche pas et corriger les bugs puis recommencer, on peut automatiser tout ça. Dans le meilleur des cas, à chaque nouvelle fonctionnalité, elle est automatiquement testée puis integrée dans une version viable du code, prête à être déployée. Si les tests détectent des erreurs ou des incompatibilités dans le code, la nouvelle fonctionnalité n'est pas integrée dans la branche principale et le développeur peut la retravailler sans jamais corrompre la version du code qui marche.

{%details "Des outils et des outils"%} 
- Bamboo
- Buildbot
- Apache Gump (pour Java)
- Travis CI (qui fonctionne avec Github)
- Github Action
- Jenkins
{%info%}Liste non exhaustive réalisée après quelques minutes sur google.{%endinfo%} 
{%enddetails%}


## La Pipeline Jenkins :

La pipelin, ou le workflow, est l'ensemble des étapes qui  gravitent autour de jenkins et qui permeteent de mettre en place l'intégration et le déploiement continue.

|Dev| => Commit -> Build -> Test -> Realase -> Deploy => |Production|

Cette pipeline peut être enclanché périodiquement comme avec un nightly build ou elle peut être enclanché à chaque commit.

# Jenkins, En pratique :

Nous allons mettre en place Jenkins avec un projet node.js, en suivant [le tutoriel officiel de la doc](https://www.jenkins.io/doc/tutorials/build-a-node-js-and-react-app-with-npm/). Le projet utilisé ne sera pas le projet de base proposé par la doc mais mon propre projet à moi, le POK Artblog.

## Lets-go

La Doc nous propose de créer une image Docker qui va servir de serveur CI, c'est à dire le serveur qui s'occupe de réaliser les tâches automatiques que l'on va mettre en place. Ici, on simule ce serveur sur notre ordinateur, en pratique ça peut être fait par un serveur dédié.
Je ne recopie pas la doc ici, seulement les subtilités que je recontres et les résultats.

### Le débuts des problèmes :

Le tutoriel de Jenkins utilise Docker:dind et les Networks de Docker. Ce sont des outils qui permettent de créer plusieurs containers et de les liées entre eux, le problème, je ne sais pas comment ça marche et je n'ai pas envie de savoir pour le moment. Je sais par contre utiliser Docker compose,qui est sensé faire la même chose mais plus simplment, j'essaie de me débrouiller avec ça.
En lisant la doc je vois que j'ai besoin de 3 services : 

  - Jenkins 
  - BlueOcean, un GUI pour jenkins
  - App, service qui va lancer mon instance node

J'écris un Docker-compose.yml qui invoque ces trois type de conteneur, avec des images que j'ai récupéré sur le site officel [DockerHub](https://hub.docker.com/)
Aussi, je pull les images avant de lancer le compose : 

    docker pull jenkins/jenkins
    docker pull jenkinsci/blueocean
    docker pull node-16alpine

{%attention%}Finalement je n'utilise pas l'image de blueocean, qui ne marche pas pour je ne sais quelle raison. Au lieu de cela, on installera le plugin BlueOcean directement dans l'instance jenkins.{%endattention%}

J'expose les ports utilisées par les applications, et je créer un volume.
Voila la tête du Docker-compose.yml :

    version: '3'
    services:
      jenkins:
        image: jenkins/jenkins:lts
       ports:
         - "8080:8080"
         - "50000:50000"
        volumes:
          - jenkins_home:/var/jenkins_home
        environment:
          JAVA_OPTS: "-Djenkins.install.runSetupWizard=false"

      nextjs:
       build: .
        command: npm run dev
        volumes:
         - .:/app
         - /app/node_modules
        ports:
          - "3000:3000"
        depends_on:
         - jenkins

    volumes:
      jenkins_home:

Il faut alors ajouter un dockerfile qui définit le build pour next.js, cf le MON Docker.
On installe Blueocean directement dans l'instance Jenkins.





