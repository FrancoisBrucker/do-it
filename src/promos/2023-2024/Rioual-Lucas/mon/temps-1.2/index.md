---
layout: layout/mon.njk

title: "Développement Back-end"
authors:
  - Lucas Rioual

date: 1970-09-01

tags: 
  - "temps 1"
  - "Node.js"
  - "backend"

résumé: "Introduction au Back-end avec Node.js et Express"
---


{% prerequis %}
**Notions abordées** : Node.js, Express, MongoDB
**Niveau** : Débutant
{% endprerequis %}

L'objectif de ce Mon est de me familiariser avec la notion de **backend**. Ce MON s’adresse à toutes les personnes qui, comme moi, n’ont aucune connaissance en backend.
Voici le lien de [mon repo Github](https://github.com/LucasRioual/Back) correspondant au [tuto OpenClassRoom](https://openclassrooms.com/fr/courses/6390246-passez-au-full-stack-avec-node-js-express-et-mongodb).


## Ressources utilisées

Pour ce MON, j'ai utilisé :
* Le [cours](https://francoisbrucker.github.io/cours_informatique/cours/web/) de Mr Brucker
* Cette [formation OpenClassRoom](https://openclassrooms.com/fr/courses/6390246-passez-au-full-stack-avec-node-js-express-et-mongodb)
* Ce [site internet](https://fullstackopen.com/fr/) 

## Sommaire

- Qu’est ce que le **backend** ?
- Comment construire son backend avec Node.js et Express
- La différence entre une application web en développement et en production.

## Qu’est ce que le backend ?

Pour comprendre ce qu’est le backend d'une application web, il faut bien saisir comment une application web fonctionne. 

On peut séparer une application web en 2 parties : 

- Le coté client (navigateur internet) : **frontend**
- Le coté serveur : **backend**

Lorsqu’on développe une application web, il faut bien comprendre qu'il y a une partie du code qui va s’exécuter sur le navigateur internet du client (HTML, CSS, JavaScript) et une autre partie qui va s’exécuter sur un serveur distant.

Le backend s’occupe de nombreuses tâches cruciales comme : 

- **La gestion des données** : Créer, lire, modifier ou supprimer des données (CRUD en anglais)
- **La logique métier**
- **La communication**
- **La sécurité**

### Communication entre le front et le back

La communication entre le front et le back se gère à l'aide de **requête HTTP**. On peut résumer un backend comme un programme qui écoute les requêtes HTTP et qui renvoie la bonne réponse.

Lorsque l’utilisateur interagit avec l’application web (si il appuie sur un bouton par exemple), le frontend envoie une requête HTTP au serveur. Le backend reçoit cette requête et commence à la traiter. Il examine la demande et effectue les opérations nécessaires. Ensuite le backend renvoie la réponse voulue (généralement en JSON). 

Plus précisément, cette communication se fait au travers d’**API** (interface de programmation d'application) qui définissent les différentes routes.

{% prerequis %}
Une route est une déclaration qui associe une URL spécifique à un ensemble d'instructions qui doivent être exécutées lorsque cette URL est accédée par un client.
{% endprerequis %}

Voici un exemple de configuration de route avec express :  

```jsx
app.use('/api/stuff', (req, res, next) => {
  res.json({ message: 'Votre requête a bien été reçue !' });
});
```

Ici, lorsqu’une requête HTTP est envoyé à la route  **http://localhost:8000/api/stuff**, le serveur envoie une réponse au format JSON qui est : “Votre requête a bien été reçue !”.

## Construire son backend avec Node.js et Express

Pour apprendre concrètement comment mettre en place un serveur avec [Node.js](https://nodejs.org/fr). J'ai suivi le [tuto d'OpenClassRoom](https://openclassrooms.com/fr/courses/6390246-passez-au-full-stack-avec-node-js-express-et-mongodb). Si comme moi, vous n'avez aucune connaissance en backend, je ne vous conseille pas de suivre ce tuto. On ne comprend pas bien comment le frontend interagit avec le backend et je trouve que certaines notions ne sont pas claires pour les débutants. 

J’ai donc trouvé [un autre tuto](https://fullstackopen.com/fr/) qui, je trouve, est beaucoup plus claire. En plus, il repart vraiment des bases pour bien appréhender le développement web. Après avoir lu  [la partie 3](https://fullstackopen.com/fr/part3), j’ai pu mieux appréhender le tuto d’openclassroom. Je conseille aussi de lire [la partie 0](https://fullstackopen.com/fr/part0) qui explique comment fonctionne une application web traditionnelle.

Revenons au tutoriel d’Openclassroom. On y apprend comment créer un serveur avec Node.js et Express.

{% prerequis %}
**Node.js** est un environnement d'exécution qui permet d'exécuter du code JavaScript côté serveur. 

**Express** est un framework web pour Node.js. Il simplifie le processus de création d'applications web coté serveur et d'API.
{% endprerequis %}

L’installation de ces outils est bien expliquer dans cette [partie](https://openclassrooms.com/fr/courses/6390246-passez-au-full-stack-avec-node-js-express-et-mongodb/6466206-configurez-votre-environnement-de-developpement).

Cependant, j’ai eu un problème lors de l’installation de nodemon (outil qui redémarre automatiquement notre serveur lorsqu’il détecte un changement).

Si vous avez cette erreur :

```jsx
nodemon : Impossible de charger le fichier C:\Users\utilisateur\AppData\Roaming\npm\nodemon.ps1, car l’exécution de scripts est désactivée sur ce système. Pour plus 
d’informations, consultez about_Execution_Policies à l’adresse https://go.microsoft.com/fwlink/?LinkID=135170.
Au caractère Ligne:1 : 1
+ nodemon server
+ ~~~~~~~
    + CategoryInfo          : Erreur de sécurité : (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```

sur Windows, il faut ouvrir le powershell en admin et écrire :

```jsx
Set-ExecutionPolicy RemoteSigned
```

Ensuite le tuto explique bien la notion de middleware et comment gérer les routes avec Express. Il explique aussi comment bien organiser son backend pour en faciliter la compréhension et la gestion. On sépare notre code en différentes couches.

```jsx

│   app.js
│   package-lock.json
│   package.json
│   server.js
├───controllers
│       stuff.js
│       user.js
│
├───models
│       thing.js
│       user.js
└───routes
        stuff.js
        user.js
```

- **Models** : pour définir les schémas de base de données (ici on utilise MongoDB)

```jsx
//models/thing.js
const mongoose = require('mongoose');

const thingSchema = mongoose.Schema({
  title: { type: String, required: true },
  description: { type: String, required: true },
  imageUrl: { type: String, required: true },
  userId: { type: String, required: true },
  price: { type: Number, required: true },
});

module.exports = mongoose.model('Thing', thingSchema);
```

Ici on créer un schéma de donnée qui représente un objet quelconque à vendre

- **Routes** : pour définir les routes de l'application

```jsx
//routes/stuff.js
const express = require('express');
const router = express.Router();

const stuffCtrl = require('../controllers/stuff');

router.get('/', stuffCtrl.getAllStuff);
router.post('/', stuffCtrl.createThing);
router.get('/:id', stuffCtrl.getOneThing);
router.put('/:id', stuffCtrl.modifyThing);
router.delete('/:id', stuffCtrl.deleteThing);

module.exports = router;
```

Ici, on s’occupe des différentes routes ayant pour racine **/api/stuff**(définis dans le fichier app.js)

```jsx
//app.js
const stuffRoutes = require('./routes/stuff');
app.use('/api/stuff', stuffRoutes);
```

- **Controllers** : pour gérer la logique métier

```jsx
const Thing = require('../models/thing');

exports.createThing = (req, res, next) => {
  const thing = new Thing({
    title: req.body.title,
    description: req.body.description,
    imageUrl: req.body.imageUrl,
    price: req.body.price,
    userId: req.body.userId
  });
  thing.save().then(
    () => {
      res.status(201).json({
        message: 'Post saved successfully!'
      });
    }
  ).catch(
    (error) => {
      res.status(400).json({
        error: error
      });
    }
  );
};
```

Ici on développe les fonctions associées à chaque **route**. J’ai affiché que la fonction qui permet de créer un nouvel élément dans la base de donnée.

Enfin, il y a quelque chose que je n’avais pas compris dans ce tuto.

La partie frontend s’exécute sur un serveur local en tapant (**npm run start**) qui est différent du serveur Node que nous créons.

Pour comprendre pourquoi le frontend et le backend tourne sur deux serveurs différents, il faut comprendre comment une application web fonctionne en production. Car ici nous sommes dans un environnement destiné au développement. En effet, en production, on utilise un autre serveur que Node.js pour servir les fichiers statiques (par exemple, Nginx). En effet, on peut utiliser un serveur intermédiaire entre le client et Node.Js qui écoute les requêtes HTTP. Si la requête demande un fichier statique, Nginx renvoie directement le fichier associé, sinon il redistribue la requête vers Node.js.

{% prerequis %}
Les fichiers statiques sont les fichiers utilisés pour le frontend (html, css, js, images, police).
{% endprerequis %}

## Conclusion

Ce MON m’a permis d’éclaircir certaines notions de backend. J’ai mis beaucoup de temps au début à essayer de comprendre comment fonctionner un application web. Une fois ce travail effectué, j’ai pu mieux appréhender la mise en pratique.

