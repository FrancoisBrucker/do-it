---
layout: layout/post.njk

title: "GraphQL"
authors:
  - Nicolas BERT

---

<!-- début résumé -->
Interface d'API GraphQL avec Express, Prisma (ORM) et PostgreSQL
<!-- fin résumé -->

{% prerequis %}
**Niveau :** intermédiaire
**Prérequis :**
- Connaître le contexte de développement backend
- Connaître les bases du langage Javascript

*Pour la partie POC:*
- Avoir une version de Node.js installé sur sa machine
- Avoir Docker et Docker Compose sur sa machine (ou bien avoir une instance de PostgreSQL installée)
{% endprerequis %}

## GraphQL ou REST ?

### Les API REST

### Les API GraphQL

### Comparaison et synthèse

## Proof Of Concept

{% prerequis "Prérequis pour le POC :" %}
- Avoir une version de Node.js installé sur sa machine
- Avoir Docker et Docker Compose sur sa machine (ou bien avoir une instance de PostgreSQL installée)
{% endprerequis %}

Pour utiliser GraphQL, j'ai décidé d'utiliser un backend réalisé avec Express, connecté à une base de données PostgreSQL via l'ORM (Object Relation Mapping) [Prisma](https://www.prisma.io/). Il y aura ensuite une route statique renvoyant une page HTML afin d'indiquer la structure de la base de données (relations, entités ...) et une unique route d'API qui sera servie par GraphQL. Voici un petit schéma d'explications :

**Un beau schéma**

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
npm i express-graphql @graphql-tools/schema
~~~

**askip ça va marcher mais pas encore ^^**



