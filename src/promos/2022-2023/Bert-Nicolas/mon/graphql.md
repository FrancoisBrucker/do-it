---
layout: layout/mon.njk

title: "GraphQL"
authors:
  - Nicolas BERT

tags:
  - 'temps 2'

date: 2023-01-25
---

<!-- début résumé -->
Interface d'API GraphQL avec Express, Prisma (ORM) et PostgreSQL
<!-- fin résumé -->

{% prerequis %}
**Niveau :** intermédiaire/avancé
**Prérequis :**
- Connaître le contexte de développement backend
- Connaître les bases du langage Javascript

*Pour la partie POC:*
- Avoir une version de Node.js assez récente installé sur sa machine
- Avoir Docker et Docker Compose sur sa machine (ou bien avoir une instance de PostgreSQL installée)
{% endprerequis %}


{% info %}
Le dépot GitHub du POC : https://github.com/nbert71/graphql-express
{% endinfo %}

## GraphQL ou REST ?

{% info "Qu'est-ce qu'une **API** ?" %}
Selon la CNIL, une **API** (*application programming interface* ou « interface de programmation d’application ») est une interface logicielle qui permet de « connecter » un logiciel ou un service à un autre logiciel ou service afin d’échanger des données et des fonctionnalités.

<img src="./../images/api.png" style="border-width: 0;" />

Une API va alors exposer des **routes** (que l'on appelle aussi **endpoints** en anglais) afin que le client puisse dialoguer avec les services. Il existe différentes manières de structurer les routes: ici nous allons parler des API REST et des API GraphQL.
{% endinfo %}

### Les API REST

Une API REST (*Representational State Transfer*) est une architecture de développement d'API qui utilise les différentes méthodes HTTP (GET, POST, PUT, DELETE, PATCH ...) pour interagir avec les autres services (généralement les bases de données). Ces différentes méthodes vont être exposées sur une même route ou sur des routes distinctes et vont répondre au client avec des [status code](http://http.cat) afin d'indiquer si la requête c'est bien passée ou s'il y a eu des erreurs. Les API REST sont très utilisées pour construire des applications web et mobiles car elles sont simples à utiliser et mettre en place. Les données transmises au client sont souvent au format JSON.

<img src="./../images/api_rest.png" style="border-width: 0; width: 100%;" />

Chaque méthode HTTP permet d'effectuer des actions bien particulières. Voilà un exemple pour expliquer les méthodes les plus utilisées.

<img src="./../images/rest_methods.png" />

Ainsi, en suivant les routes de l'image ci-dessus, en appelant *"/posts"* en méthode GET, l'API nous répondra en nous donnant la liste de tous les posts. Si j'envoie une requête POST à *"/posts"* en mettant des données dans ma requête je vais créer dans la base de données un post...

Pour plus d'informations, je vous invite à consulter [https://phauer.com/2015/restful-api-design-best-practices/](https://phauer.com/2015/restful-api-design-best-practices/).


### Les API GraphQL

Le modèle d'API GraphQL est une autre manière de structurer les routes. Il n'y a en général qu'**un seul endpoint** qui est de type **POST** et c'est le client qui, en paramètres de la requête POST va définir les données qu'il souhaite obtenir. On gagne ainsi en flexibilité en permettant au client d'obtenir ce qu'il a besoin sans être figé par un modèle REST.

<img src="./../images/rest_graphql.png" style="border-width: 0;" />
<img src="./../images/REST-and-GraphQL.png" style="border-width: 0;" />

### REST ou GraphQL ? Avantages et inconvénients 

Il s'agit donc d'un autre paradigme pour la construction d'API qui a ses avantages et ses inconvénients par rapport aux API REST :

- ✅ **Flexibilité** : les API GraphQL permettent aux clients de demander des donnée spécifiques plutôt que de recevoir un format de données prédéfini, cela offre donc une grande flexibilité pour les développeurs.
- ✅ **Spécificité** : les API GraphQL permettent de demander plusieurs donner en une seule requête alors qu'il en aura fallu plusieurs dans le cas d'un modèle REST.
- ✅ **Évolutivité** : GraphQL est conçu pour évoluer avec les besoins du client et lui permet de faire des manipulations spécifiques telles que les opérations en lots ou bien les subscriptions pour les données en temps réel.

- ❌ **Apprentissage** : GraphQL est un langage d'API complètement différent, il peut donc être difficile pour les développeurs de s'adapter.
- ❌ **Débogage** : le débogage est plus difficile à cause de la flexibilité des requêtes.
- ❌ **Support** : GraphQL est très largement moins utilisé que REST, il y a donc moins de bibliothèques, frameworks et documentations ...

## Proof Of Concept

{% prerequis "Prérequis pour le POC :" %}
- Avoir une version de Node.js installé sur sa machine
- Avoir Docker et Docker Compose sur sa machine (ou bien avoir une instance de PostgreSQL installée)
{% endprerequis %}

Pour utiliser GraphQL, j'ai décidé d'utiliser un backend réalisé avec Express, connecté à une base de données PostgreSQL via l'ORM (Object Relation Mapping) [Prisma](https://www.prisma.io/). Il y aura ensuite une route statique renvoyant une page HTML afin d'indiquer la structure de la base de données (relations, entités ...) et une unique route d'API qui sera servie par GraphQL. Voici un petit schéma d'explications :

<img src="./../images/graphql-archi.png" />

Nous allons désormais voir pas à pas comment créer un tel projet.

### Initialisation du projet Express

Nous allons donc initialiser un projet **npm** puis installer quelques librairies dont `express`.

```bash
mkdir graphql-express
cd graphql-express
npm init -y
npm i express dotenv dotenv-expand nodemon
```

Nous allons ensuite créer le fichier `.env` qui contiendra toutes les variables d'environnement du projet. Nous le compléterons au fur et à mesure. Pour l'instant, écrivez-y :

```
NODE_PORT=3000
```

Créons ensuite le fichier `index.js`qui contiendra la configuration express.

```javascript
require('dotenv').config()

const express = require('express')

const app = express()
const port = process.env.NODE_PORT  // on récupère la variable NODE_PORT définie dans le fichier .env

app.get('/', (req, res) => {
  res.send('Hello World')
})

app.listen(port, () => {
  console.log(`The app is running on port ${port}`);
})
```

Allons désormais dans le fichier `package.json` pour y écrire la commande de lancement du projet :

~~~json
{
  ...
  "scripts": {
    "start": "node index.js",
    "dev": "nodemon index.js"
  },
  ...
}
~~~

*Ici, la commande `npm run dev`sert uniquement à recharger automatiquement le serveur lorsqu'il y a une modification, c'est pour cela qu'on ne l'utilise qu'en dev.*
Lançons `npm run dev`, aller sur [localhost:3000](localhost:3000) et vous devriez voir un magnifique Hello World ! 

### Mise en place de PostgreSQL via docker compose

Afin d'éviter d'avoir à installer une instance de PostgreSQL sur la machine, on va utiliser la version plus rapide avec docker compose. Si jamais vous ne connaissez pas docker, vous pouvez consulter le [magnifique MON de Tunçay sur Docker](/do-it/mon/TBi/MON/Docker). Voilà le fichier `docker-compose.yml` qu'il faut créer à la racine.

~~~yml
version: '3.8'

services:
  db:
    image: postgres:13-alpine
    container_name: db
    ports:
      - "${PG_PORT}:5432"
    environment:
      POSTGRES_DB: ${PG_DB}
      POSTGRES_USER: ${PG_USER}
      POSTGRES_PASSWORD: ${PG_PASSWORD}
    volumes:
      - db_data:/var/lib/postgresql/data

volumes:
  db_data:
~~~

On voit que le service `db`a besoin de variables d'environnement (POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD ainsi que le port). Au lieu d'écrire directement les valeurs de ces variables dans le fichier, nous allons les écrire dans le `.env`.

~~~
# Database connection
PG_PORT=5432
PG_DB=graphql-db
PG_USER=admin 
PG_PASSWORD=password
DATABASE_URL=postgresql://${PG_USER}:${PG_PASSWORD}@localhost:${PG_PORT}/${PG_DB}
~~~

On crée également grâce à la librairie `dotenv-expand` la variable d'environnement composée `DATABASE_URL`dont nous allons avoir besoin plus tard.

Afin de lancer le service PostgreSQL, il suffit juste de lancer la commande `docker compose up -d` en ayant au préalable lancer Docker.

### Mise en place du schéma de base de données et manipulations Prisma

Pour communiquer avec la base de données j'ai choisi un ORM que je ne connaissais pas [Prisma](https://www.prisma.io/). Nous allons donc installer la CLI de Prisma en dev ainsi que le client Prisma.

~~~bash
npm i -D prisma 
npm i @prisma/client
~~~

Nous allons désormais initialiser Prisma avec `npx prisma init`. Cela crée un dossier `prisma` avec un fichier `schema.prisma` que nous allons modifier.

~~~javascript
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}
~~~

Nous allons ensuite spécifier notre schéma de base de données dans le fichier `schema.prisma`.

~~~
model Post {
  id        Int      @id @default(autoincrement())
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
  title     String   @db.VarChar(255)
  content   String?
  published Boolean  @default(false)
  author    User     @relation(fields: [author_id], references: [id])
  author_id  Int
}

model Profile {
  id     Int     @id @default(autoincrement())
  bio    String?
  user   User    @relation(fields: [user_id], references: [id])
  user_id Int     @unique
}

model User {
  id      Int      @id @default(autoincrement())
  email   String   @unique
  name    String?
  posts   Post[]
  profile Profile?
}
~~~

On va désormais créer une migration et l'appliquer en même temps à la base de données avec `npx prisma migrate dev --name init`.

{% info %}
**Quelques commandes Prisma à connaître :**
- `npx prisma validate`: permet de vérifier si le schéma Prisma est correct
- `npx prisma studio` : lance une interface web pour visualiser le contenu de la base données
- `npx prisma db pull` : récupère le schéma existant dans la base de données et met à jour le schéma Prisma
- `npx prisma db push` : met à jour la base de données à partir des données du schéma Prisma
- `npx prisma migrate dev --name my_migration` : crée un fichier de migration comportant les derniers changements du schéma Prisma et applique ce changement à la base de données
- `npx prisma migrate reset` : réinitialise la base de données et applique toutes les migrations
- `npx prisma migrate deploy` : applique les dernières migrations en cours à la base de données
- `npx prisma generate`: permet de modifier le PrismaClient (outil utilisé dans le backend pour envoyer des requêtes) afin qu'il soit à jour avec le schéma de db
{% endinfo %}

A ce stade en lançant la commande `npx prisma studio`nous devrions voir nos tables avec les différents champs.

<img src="./../images/prisma-studio.png" />

{% attention %}
Il faut faire attention aux pratiques que l'on souhaite avoir. Il est possible de travailler uniquement avec le schéma Prisma et faire des `db push`cependant des changements plus important en base de données pourrait être critique en production, c'est pour cela que l'on utilise les migrations.

Selon moi, à chaque modification du schéma de base de données, on modifie le schéma Prisma et on lance `npx prisma migrate dev --name "ma migration"`.
{% endattention %}

### Création de fausses données

Nous allons désormais créer un fichier de fausses données à charger dans la base de données. Ce fichier s'appelle `prisma/seed.js`.
Afin de pouvoir charger ces fausses données nous devons modifier le `package.json`.

~~~json
{
  ...
  "prisma": {
    "seed": "node prisma/seed.js"
  }
}
~~~

### Installation de GraphQL et paramétrisation

Comme nous l'avons au début de ce MON, GraphQL est un langage de requête API. Pour fonctionner, nos serveur express a besoin d'un serveur GraphQL afin d'interpréter les requêtes et les transformer en requête Prisma qui les transformera ensuite en requête SQL. Nous allons utiliser `express-graphql`.

~~~bash
npm i express-graphql graphql
~~~

GraphQL fonctionne avec des types, des queries et des mutations. Ici nous allons montrer en exemple la class User. On commence pas créer un type User qui va définir les types de données que nous allons renvoyer au client.

~~~js
const UserType = new GraphQLObjectType({
    name: "User",
    fields: () => ({
        id: {type: GraphQLInt},
        email: {type: GraphQLString},
        first_name: {type: GraphQLString},
        last_name: {type: GraphQLString},
        posts: {type: GraphQLList(PostType)},
        profile: {type: ProfileType}
    })
})
~~~

On peut ensuite définir une query associée qui permet de récupérer la liste de tous les users.

~~~js
const RootQuery = new GraphQLObjectType({
    name: "RootQueryType",
    fields: {
        getAllUsers: {
            type: GraphQLList(UserType),
            async resolve(parent, args) {
                return await prisma.user.findMany()
            }
        }
    }
})
~~~

On met en place ensuite la mutation pour créer un user.

~~~js
const Mutation = new GraphQLObjectType({
    name: "Mutation",
    fields: {
        createUser: {
            type: UserType,
            args: {
                email: {type: GraphQLString},
                first_name: {type: GraphQLString},
                last_name: {type: GraphQLString},
            },
            async resolve(parent, args) {
                await prisma.user.create({data: {
                    email: args.email,
                    first_name: args.first_name,
                    last_name: args.last_name
                }})
                return args
            }
        }
    }
})
~~~

On crée ensuite le schéma GraphQL qui va nous permette de gérer les requêtes et la route Express associée.

~~~js
const schema = new GraphQLSchema({query: RootQuery, mutation: Mutation})

app.use('/api', graphqlHTTP({
    schema,
    graphiql: true
}))
~~~

{% info %}
L'option `graphiql: true`nous permet d'avoir un GUI sur la route *"/api"* et ainsi pour voir faire les requêtes plus simplement pour la période de test.
{% endinfo %}

Testons désormais notre api !

~~~graphql
# je demande la liste de tous les users et pour chaque user je veux son mail son nom et son prénom
query {
    getAllUsers {
        email
        first_name
        last_name
    }
}
~~~

Le serveur répond alors :
~~~json
{
  "data": {
    "getAllUsers": [
      {
        "email": "alice@prisma.io",
        "first_name": "Alice",
        "last_name": "Prisma"
      },
      {
        "email": "bob@prisma.io",
        "first_name": "Bob",
        "last_name": "Prisma"
      }
    ]
  }
}
~~~

On teste maintenant la mutation !

~~~graphql
mutation {
  createUser(email: "mrbean@email.com", first_name:"Harry", last_name:"Cover"){
    email
    first_name
    last_name
  }
}
~~~

Le serveur répond alors :

~~~json
{
  "data": {
    "createUser": {
      "email": "mrbean@email.com",
      "first_name": "Harry",
      "last_name": "Cover"
    }
  }
}
~~~

On peut ainsi continuer et créer d'autres requêtes....

## Conclusion

Pour conclure, GraphQL est un langage de requête API qui est assez novateur. Toutes les requêtes client sont des requêtes POST et se font sur un seul endpoint. Je pensais qu'il suffisait d'exposer ses données sur une route et que le client pouvait ensuite demander n'importe quoi sous le format qu'il veut mais en fait le développeur doit quand même tout définir à la main comme à la manière d'une API REST. Ainsi, GraphQL est censé apporter de la flexibilité aux développeurs mais le travail reste tout aussi fastidieux qu'une API REST, voire plus...


## Sources

- https://openclassrooms.com/fr/courses/6573181-adoptez-les-api-rest-pour-vos-projets-web/6816951-initiez-vous-au-fonctionnement-des-api
- https://blog.hubvisory.com/blog/api-rest-comment-ca-fonctionne-et-pourquoi-l-utiliser/
- https://stackoverflow.com/questions/73103901/api-endpoint-for-a-single-item-post-vs-put
- https://medium.com/nerd-for-tech/graphql-vs-restful-e1a99fd14285
- https://kinsta.com/fr/blog/graphql-vs-rest/