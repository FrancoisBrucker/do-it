---
layout: layout/mon.njk

title: "Déploiement de microservices en C# avec Docker"
authors:
  - Savinien Laeuffer
date: 2023-03-23

tags:
  - 'temps 3'
---

<!-- début résumé -->
Déploiement de microservices en C# avec Docker
<!-- fin résumé -->

## Description

Toujours dans le but de me former en C# pour mon stage de fin d'études, j'ai continué à apprendre ce langage en me formant plus particulièrement sur la notion de microservices dont je n'avais pas encore connaissaces. J'ai allé fait le lien rapidement avec Docker, mais plus particulièrement Docker Compose qui est plutôt adapté à l'architecture en microservice. Ici on se focalise sur le langage C# pour créer et exécuter les services d'API Web et le front-end, mais cela marcherait avec d'autres langages et frameworks.
Pour cela je me base sur le MON précédemment réalisé par Nicolas Bert au temps 2 ainsi que de toutes les sources qu'il a pu fournir en fin de MON. Pour la partie C#, un cours par Microsoft explique l'application d'une architecture de microservices au langage C# et les méthodes utiles.


#### Pré-requis

Afin de voir les bases en C# et .NET pour créer une API web, vous pouvez vous renseigner sur mon 2ème MON du temps 2, ou bien sur la documentation Microsoft Learn:
- [MON: C# et .NET (Bases, création d'une API)](../csharp/moncsharp.md)
- [Microsoft Learn](https://learn.microsoft.com/fr-fr/)

Comme nous avons déjà un cours de Docker lors de ce Temps 3, je me suis focalisé plus particulièrement sur Docker Compose. Pour des informations sur Docker, il faut suivre le cours adéquat.

#### Plan

1. Concept d'architecture de microservices
2. Rôle des conteneurs (Docker)
3. Génération d'un Dockerfile 
4. Utilité de Docker Compose
5. Resources

## Concept d'architecture de microservices

Le principe d'architecture de microservices est une méthode de développement logicielle qui consiste à décomposer une application en plusieurs parties que l'on appelle services. Chaque service est indépendant, de petite taille et possède sa propre fonction. Ils communiquent entre eux à l'aide d'API bien définies. Un scale-out, scale-in, des tests, peuvent être menés sur chacun des services indépendemment. 

<div style="width:100%;">
  <figure style="text-align:center">
    <img style="height:800px; margin-left: auto; margin-right: auto" src="../micro1.png">
    <figcaption>Architecture de microservices</figcaption>
  </figure>
</div>

Cela apporte plusieurs avantages:
- Une petite équipe de développement peut se focaliser sur un microservice sans avoir à se soucier de l'application entière
- L'architecture de microservices apportent une plus grande flexibilité lors du développement. En effet si quelque chose devait être amené à changer dans l'application, il suffit de se focaliser sur le service correspondant. Il est alors plus facile d'ajouter des fonctionnalité à notre application en travaillant par microservices.
- Le redéploiement de l'application entière n'est pas nécessaire si un changement a eu lieu au sein d'un service particulier
- Chaque service peut posséder ses propres frameworks, langages, les développeurs sont moins restreints quant aux technologies utilisées et peuvent donc se focaliser sur l'expérience de l'utilisateur plutôt que de se cantonner à ce qui est possible avec des technologies peut être non adaptées.

Les points négatifs sont moins nombreux mais toujours présents:
- L'ensemble forme un tout complexe et une équipe qui travaille sur un service spécifique ne peut pas modifier tous les services de l'application si les langages et frameworks utilisés ne leur sont pas connus.
- Le fait que plusieurs services communiquent entre eux à tout moment, cela peut créer des problèmes de latence dans le chargement de certaines informations.

L'architecture de microservices se différencie du schéma classique, appelé architecture monolithique. Le schéma suivant explique les différences entre ces deux approches:

<div style="width:100%;">
  <figure style="text-align:center">
    <img style="height:500px; margin-left: auto; margin-right: auto" src="../monolith.jpg">
    <figcaption>What Is Microservice Architecture?, Tomas Fernandez</figcaption>
  </figure>
</div>


## Rôle des conteneurs (Docker)

Dans notre cas, pour .NET, la conteneurisation de l'application est un moyen utile de travailler avec une architecture de microservices, malgré qu'elle ne soit pas la seule solution.

Les conteneurs permettent de créer un environnement d'exécution isolé et portable pour des applications logicielles. L'application, tout son contenu ainsi que toutes ses dépendances, sa configuration, sont empaquetées dans un conteneur. Celui-ci permet d'exécuter, de tester, de déployer l'application dans le système d'exploitation hôte.
L'avantage de travailler avec des conteneurs est de garantir une stabilité et sécurité puisque les conteneurs possèdent leur propre configuration et dépendance et sont isolés les uns des autres. Il est alors possible de déployer les applications rapidement et de manière fiable sans se soucier de l'environnement dans lequel elles sont déployées. Les modifications sont rapides et cela n'impacte pas les autres applications exécutées sur le même système.

Docker est un projet open source qui permet la création de ce types de conteneurs

<div style="width:100%;">
  <figure style="text-align:center">
    <img style="height:400px; margin-left: auto; margin-right: auto" src="../docker.jpg">
    <figcaption>Docker</figcaption>
  </figure>
</div>


## Génération d'un Dockerfile 

Microsoft Learn nous fournit un dépôt GitHub contenant un site web et une API back-end que l'on peut clôner afin de s'initier à la conteneurisation.
Ce repository est accessible à l'adresse suivate:
https://github.com/MicrosoftDocs/mslearn-dotnetmicroservices/

Dans VS Code, on ouvre le dossier `backend` et dans le fichier Dockerfile vide on colle le code suivant afin de le configurer:
```dockerfile
FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /src
COPY backend.csproj .
RUN dotnet restore
COPY . .
RUN dotnet publish -c release -o /app
```

En dessous de la dernière on ajoute les lignes suivantes et on enregistre le Dockerfile:
```dockerfile
FROM mcr.microsoft.com/dotnet/aspnet:6.0
WORKDIR /app
EXPOSE 80
EXPOSE 443
COPY --from=build /app .
ENTRYPOINT ["dotnet", "backend.dll"]
```

Dans le terminal, on accède au dossier contenant ce fichier et on créer l'image à partir de la commande suivante:
```bash
docker build -t backend1 .
```

Au bout d'un certant temps, l'image a été générée et on peut retrouver toutes les images sur notre ordinateur à partir de la commande
```bash
docker images
```

Si on veut exécuter l'API localement sur le port 5200 on utilise la commande
```bash
docker run -it --rm -p 5200:80 --name backendcontainer backend
```

On peut maintenant accéder à notre API à partir de la racine http://localhost:5200/

## Utilité de Docker Compose

Docker Compose est un outil opensource associé à Docker qui permet la gestion d'applications multi-conteneurs. C'est à dire qu'il facilite la gestion de plusieurs conteneurs Docker au sein d'une même application. Cet outil est adapté à l'architecture de multiservices puisque chaque service peut avoir son propre conteneur. Il permet notamment d'exécuter tous les services en une fois afin d'exécuter l'application toute entière.

<div style="width:100%;">
  <figure style="text-align:center">
    <img style="height:500px; margin-left: auto; margin-right: auto" src="../dockercompose.png">
    <figcaption>Architecture multi-conteneurs appliquée aux microservices</figcaption>
  </figure>
</div>

Un fichier YAML est utilisé avec Docker Compose afin de configurer les différents services d'une application.
Docker Compose est une fonctionnalité de Docker qui est installé par défaut lorsque l'on a Docker.

Dans VS Code, toujours dans le même répertoire, on peut trouver un fichier ```docker-compose.yml``` vide où l'on ajoute le code suivant:
```yml
version: '3.4'

services: 

  frontend:
    image: pizzafrontend
    build:
      context: frontend
      dockerfile: Dockerfile
    environment: 
      - backendUrl=http://backend
    ports:
      - "5902:80"
    depends_on: 
      - backend
  backend:
    image: pizzabackend
    build: 
      context: backend
      dockerfile: Dockerfile
    ports: 
      - "5000:80"
```

Ce code permet de créer la partie front-end du site inter dans un premier temps, et il indique à Docker quel est le chemin vers le Dockerfile du front-end afin de le générer. Un port est choisi pour la partie back-end.
Ensuite le service du back-end est créé et est généré à partir du Dockerfile créé précédemment.

Afin de générer les images conteneur, on utilise la commande ```docker-compose build``` dans notre terminal.
Finalement pour démarrer les deux services simultanément grâce à Docker Compose, on utilise la commande suivante:
```bash
docker-compose up
```

On peut donc accéder en local à notre site sur le port 5902 à l'adresse http://localhost:5902
Nous avons donc réussi à conteneuriser le service d'API et le front-end séparément et de les générer/exécuter simultanément grâce à Docker Compose


## Resources

- [MON de Nicolas Bert](https://francoisbrucker.github.io/do-it/mon/NB/mes-mon/microservices/)
- [Microservices Wikipedia](https://fr.wikipedia.org/wiki/Microservices)
- [What are microservices, Redhat](https://www.redhat.com/fr/topics/microservices/what-are-microservices)
- [Que sont les microservices ?, Microsoft Learn](https://learn.microsoft.com/fr-fr/training/modules/dotnet-microservices/2-what-are-microservices?ns-enrollment-type=learningpath&ns-enrollment-id=learn.dotnet.create-microservices-with-dotnet)