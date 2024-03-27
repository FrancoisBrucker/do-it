---
layout: layout/mon.njk

title: "Test avec Jest"
authors:
  - Lucas Rioual

date: 1970-09-01

tags: 
  - "temps 3"
  - "javascript"
  - "jest"
  - "Express"

résumé: "Test"
---


{% prerequis %}
**Javascript**
{% endprerequis %}



## Introduction

L’objectif de ce MON est de me former sur les tests javascript.  Je souhaite me concentrer sur cette thématique car c’est quelque chose qui est primordial pour faire du code professionnel. 

Je vais m’attarder sur la biblothèque Jest qui permet de tester du code Javascript. Je vais utiliser le backend du projet Killer pour m’entrainer.

## Tester du code Javascript

Je voulais savoir comment tester l’API du projet Killer car pour l’instant, pour tester les différentes fonctionnalités, j’utilise l’interface de l’application. C’est long à tester une fonctionnalité mais surtout, il est difficile de tester une seule fonctionnalité à la fois. 
L’objectif est donc de pouvoir tester les différentes routes de l’API et s’assurer que le résultat renvoyé est bien celui attendu.

J’ai utilisé ces deux tuto :

- [https://saniaalikhan224.medium.com/mastering-api-testing-with-jest-node-js-express-and-mongodb-a-step-by-step-guide-bcd5f72e0d26](https://saniaalikhan224.medium.com/mastering-api-testing-with-jest-node-js-express-and-mongodb-a-step-by-step-guide-bcd5f72e0d26)
- [https://www.freecodecamp.org/news/how-to-test-in-express-and-mongoose-apps/](https://www.freecodecamp.org/news/how-to-test-in-express-and-mongoose-apps/)

Cela permet de tester une application Express qui communique avec une base de donnée Mongo DB.

Voici comment installer les dépendances nécessaire :

 

```bash
npm install --save-dev jest supertest 
npm install mongoose
```

- Jest : tester du code Javascript
- Supertest : permet de tester des routes et des endpoints
- Mongoose : communiquer avec la base de donnée

Ensuite, le but est de tester mon application sans tout casser. En effet, les tests permettront d’intéragir avec la base de donnée. Cependant, lorsqu’on effectue des tests, il ne faut pas modifier la vrai base de donnée qui est utilisé par l’application en production.
Pour cela, on crée un ficher .env qui stocke des variables d’environnement :

```bash
MONGODB_URI='url'
MONGODB_URI_TEST='url de test'
```

Comme ça on peut choisir quel url choisir n’importe où dans l’application

Ensuite on rajoute un script dans package.json :

```bash
"scripts": {
    "test": "jest"
  },
```

### Tester une route

Maintenant, je souhaite tester la route **POST** `/api/user/testUser`  qui permet d’ajouter un nouvel utilisateur dans la base de donnée avec le nom ‘testUser’.

Voici le code que j’ai qui permet de tester cette route : 

```jsx

describe("User API", () => {
  beforeAll(async () => {
    await mongoose.connect(process.env.MONGODB_URI_TEST);
  });

  afterAll(async () => {
    await mongoose.connection.close();
  });

  beforeEach(async () => {
    await User.deleteMany({})
    await Game.deleteMany({});
  });
  describe("POST /user", () => {
    it("doit créer un nouvel utilisateur", async () => {
      const response = await request(app)
        .post("/api/user/testUser")
        .send({ expoToken: "testToken" });
      expect(response.statusCode).toBe(200);
      expect(response.body).toHaveProperty("success", true);
      expect(response.body).toHaveProperty("userId");
    });
  });
});

```

Le code commence par définir une suite de tests avec **`describe("User API", () => { ... })`**. Cette suite de tests contient plusieurs hooks et blocs de tests.

- Le premier hook est **`beforeAll(async () => { ... })`**, qui est exécuté une seule fois avant tous les tests de la suite. Dans ce hook, la connexion à la base de données de test est établie en utilisant **`mongoose.connect(process.env.MONGODB_URI_TEST)`**.
- Le deuxième hook est **`afterAll(async () => { ... })`**, qui est exécuté une seule fois après tous les tests de la suite. Dans ce hook, la connexion à la base de données est fermée en utilisant **`mongoose.connection.close()`**.
- Le troisième hook est **`beforeEach(async () => { ... })`**, qui est exécuté avant chaque test de la suite. Dans ce hook, toutes les collections **`User`** et **`Game`** sont supprimées à l'aide de **`User.deleteMany({})`** et **`Game.deleteMany({})`**, respectivement.
- Ensuite, il y a un bloc de tests imbriqué pour tester la création d'un nouvel utilisateur en utilisant la méthode HTTP POST sur l'URL **`/api/user/testUser`**. Dans ce test, une requête HTTP est envoyée à l'application Node.js à l'aide de **`request(app).post("/api/user/testUser").send({ expoToken: "testToken" })`**. La réponse HTTP est ensuite vérifiée pour s'assurer que le code d'état est 200, que la propriété **`success`** est définie sur **`true`** et que la propriété **`userId`** existe dans le corps de la réponse.

Maintenant si on fait `npm run test`  on a ce resultat :

```bash
PS D:\Programmation\Ecm\Killer-back> npm run test

> killer-back@1.0.0 test
> jest

 PASS  test/user.test.js
  User API
    POST /user
      √ doit créer un nouvel utilisateur (280 ms)

Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
Snapshots:   0 total
Time:        1.952 s, estimated 8 s
Ran all test suites.
```

### Tester la modification d’un utilisateur

Ensuite, je souhaite tester la route PUT `/api/user/`{userId}  qui permet de modifier le surnom d’un utilisateur. Le problème, c’est qu’au début des tests, ma base de donnée est vide. J’ai donc crée 3 utilisateurs de test que j’évite de supprimer à la fin des test :

```jsx

const user1Id = "65fd4cbe4352edb5a9722609";
const user2Id = "65fd4cdb034e02d9b0920de8";
const user3Id = "65fd511875033da71380cc99";

describe("User API", () => {
  beforeAll(async () => {
    await mongoose.connect(process.env.MONGODB_URI_TEST);
  });

  afterAll(async () => {
    await mongoose.connection.close();
  });

  beforeEach(async () => {
    await User.deleteMany({
      _id: {
        $nin: [
          user1Id,
          user2Id,
          user3Id,
          
        ],
      },
    })
    await Game.deleteMany({});

  });

  describe("POST /user", () => {
    it("doit créer un nouvel utilisateur", async () => {
      const response = await request(app)
        .post("/api/user/testUser")
        .send({ expoToken: "testToken" });
      expect(response.statusCode).toBe(200);
      expect(response.body).toHaveProperty("success", true);
      expect(response.body).toHaveProperty("userId");
    });
    it("modifier le surnom de l'utilisateur", async () => {
      const response = await request(app)
        .put(`/api/user/${user1Id}`)
        .send({ expoToken: "testToken", userName: "Tom" });
      expect(response.statusCode).toBe(200);
      expect(response.body).toHaveProperty("success", true);
      expect(response.body).toHaveProperty("userId");
    });
    it("modifie le surnom de l'utilisateur mais l'id n'existe pas dans la base de donnée", async () => {
      const response = await request(app)
        .put("/api/user/65f58e6326c2f024807a6376")
        .send({ expoToken: "testToken", userName: "Tom" });
      expect(response.statusCode).toBe(200);
      expect(response.body).toHaveProperty("success", true);
      expect(response.body).toHaveProperty("userId");
    });
  });
});
```

## Conclusion

Il y a pleins d’autres routes à tester pour s’assurer que l’application fonctionne bien. Cependant je n’ai pas eu le temps de toutes les tester. J’ai mis pas mal de temps à faire fonctionner le premier test car j’avais des soucis pour me connecter à la base de donnée. Je n’ai pas eu le temps de passer les 10h sur ce MON. J’ai passé environ 6h sur la documentation et les exemples que j’ai présenté.



