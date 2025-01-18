---
layout: layout/mon.njk

title: "Maîtriser le Développement Back-End Web avec Node.js, Express et MongoDB"
authors:
  - Omar Salame

date: 2023-10-11

tags:
  - "temps 1"
  - "Developpement Web"
  - "Back-End"
  - "Node.js"
  - "Express"
  - "MongoDB"


résumé: "Mon travail vise à approfondir ma maîtrise du développement web côté serveur en utilisant des technologies telles que Node.js, Express, et MongoDB. Je compte utiliser ces connaissances dans mon POK."
---
{% prerequis %}
**Niveau** : Intermédiaire
**Prérequis** : Une connaissance en JavaScript, HTML et CSS
{% endprerequis %}

## Table des matières

1. [Introduction](#section-1)
2. [Node.js & Express](#section-2)
   - [Node.js](#subsection-1)
   - [Express](#subsection-2)
   - [Rest](#subsection-3)
3. [MongoDB](#section-3)
   - [Schema](#subsection-4)


## Introduction <a id="section-1"></a>

Le développement back-end, également appelé développement côté serveur, fait référence à la construction de la partie non visible des applications web, qui gère les données, la logique métier, et les interactions avec la base de données. Il est responsable de l'ensemble des opérations en coulisses qui permettent aux applications web de fonctionner. Le développement back-end se concentre sur la création de serveurs, la gestion des bases de données, le traitement des requêtes clients, et la fourniture de données dynamiques aux applications front-end. Il est essentiel pour assurer la fonctionnalité, la sécurité, et la performance des applications web.

J'ai choisis de développer de compétences en Node.js, Express, et MongoDB à travers le cours [Deep Dive Into Modern Web Development](https://fullstackopen.com/en/). Ce cours est une initiation au développement web avec JavaScript, composé de 12 sections, chacune exigeant environ 10 à 12 heures de travail. J'ai terminé la troisième section, qui aborde la programmation d'un serveur avec NodeJS et Express.

## Node.js & Express <a id="section-2"></a>
### **Node.js** <a id="subsection-1"></a>

On Commence par créer un modèle pour notre application en utilisant la commande ```npm init```. Vous devrez répondre aux questions posées par l'utilitaire, et le résultat sera la création automatique d'un fichier _package.json_ à la racine du projet, qui contient des informations sur le projet.

```js
{
  "name": "backend",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "Omar Salame",
  "license": "ISC"
}
```
Nous pouvons ensuite exécuter le programme sur _index.js_ directement avec Node à partir de la ligne de commande ```node index.js```, ou ```npm start```

Pour commencer, on transforme l'application en serveur web en modifiant les fichiers index.js comme suit :
```js
const http = require('http')

const app = http.createServer((request, response) => {
  response.writeHead(200, { 'Content-Type': 'text/plain' })
  response.end('Hello World')
})

const PORT = 3001
app.listen(PORT)
console.log(`Server running on port ${PORT}`)
```
Dans la première ligne, l'application importe le module serveur web intégré de Node. Le code utilise la méthode createServer du module http pour créer un nouveau serveur web. Un gestionnaire d'événements est enregistré sur le serveur, qui est appelé à chaque fois qu'une requête HTTP est effectuée à l'adresse du serveur http://localhost:3001. La réponse est renvoyée avec le code d'état 200, l'en-tête Content-Type est défini sur text/plain, et le contenu du site à renvoyer est défini sur Hello World. Le but principal du serveur back-end dans ce cours est de fournir des données brutes au format JSON au front-end.

```js
let notes = [
  {
    id: 1,
    content: "HTML is easy",
    important: true
  },
  {
    id: 2,
    content: "Browser can execute only JavaScript",
    important: false
  },
  {
    id: 3,
    content: "GET and POST are the most important methods of HTTP protocol",
    important: true
  }
]
const app = http.createServer((request, response) => {
  response.writeHead(200, { 'Content-Type': 'application/json' })
  response.end(JSON.stringify(notes))
})
```
La valeur application/json dans l'en-tête Content-Type informe le destinataire que les données sont au format JSON. Le tableau de notes est transformé en JSON à l'aide de la méthode JSON.stringify(notes).
<img src="js1.webp" width="700" height="550">

### **Express** <a id="subsection-2"></a>
Il est possible de mettre en œuvre notre code serveur directement avec le serveur web http intégré de Node. Cependant, cela devient fastidieux, en particulier lorsque l'application prend de l'ampleur. C'est la raison pour laquelle de nombreuses bibliothèques ont vu le jour pour faciliter le développement côté serveur avec Node. Une de ces bibliothèques est **Express**
Utilisons express en le définissant comme une dépendance du projet avec la commande : ```npm install express```
La syntaxe de notre application est differente pour utiliser Express:
```js
const express = require('express')
const app = express()

let notes = [
  ...
]

app.get('/', (request, response) => {
  response.send('<h1>Hello World!</h1>')
})

app.get('/api/notes', (request, response) => {
  response.json(notes)
})

const PORT = 3001
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`)
})
```
Afin que le navigateur se recharge automatiquement après avoir apporté des modifications, on peut utiliser
_nodemon_

### **Rest** <a id="subsection-3"></a>
Nous allons étendre notre application pour qu'elle fournisse la même API HTTP RESTful que json-server. REST, acronyme de Representational State Transfer, a été introduit en 2000 dans la thèse de Roy Fielding. REST est un style architectural conçu pour construire des applications web évolutives. Dans cette section, nous nous concentrons sur la compréhension typique des API RESTful dans les applications web, en se basant sur l'idée que des entités uniques, comme les notes dans notre application, sont appelées des ressources. Chaque ressource a une URL associée qui constitue son adresse unique. Une convention courante pour créer des adresses uniques consiste à combiner le nom du type de ressource avec l'identifiant unique de la ressource. Par exemple, si le type de ressource est défini comme "notes" et que l'identifiant de la note est 10, alors l'adresse unique de cette note est 'www.example.com/api/notes/10'. L'URL pour l'ensemble de la collection de toutes les ressources note est 'www.example.com/api/notes.'

```js
app.get('/api/notes/:id', (request, response) => {
  const id = Number(request.params.id)
  const note = notes.find(note => note.id === id)
  

  if (note) {
    response.json(note)
  } else {
    response.status(404).end()
  }
})
```
Dans cette section du cours, nous étendons notre application pour fournir une interface REST permettant d'opérer sur des notes individuelles. Nous commençons par créer une route pour récupérer une ressource unique, où l'adresse unique d'une note individuelle suit le format "notes/10" avec un numéro faisant référence à l'identifiant unique de la note. Nous utilisons la méthode app.get('/api/notes/:id', ...) pour gérer les requêtes HTTP GET de la forme "/api/notes/QUELQUECHOSE," où "QUELQUECHOSE" est une chaîne arbitraire.

En cas de succès, nous configurons le statut de la réponse avec la méthode status et renvoyons la réponse sans données grâce à la méthode end, car les API REST sont principalement destinées à un usage programmatique.

Si aucune note n'est trouvée, notre application renvoie un code d'erreur, mais ne renvoie rien à afficher dans le navigateur, conformément au fonctionnement des API REST. Cependant, il est possible de personnaliser le message d'erreur 404 pour fournir des indications sur la raison de l'erreur.

### **Communiquer des données**
On peut ensuite permettre l'ajout de nouvelles notes au serveur. Pour ajouter une note, il suffit de faire une requête HTTP POST à l'adresse http://localhost:3001/api/notes, en envoyant toutes les informations de la nouvelle note dans le corps de la requête au format JSON.
On modifie index.js:
```js
const express = require('express')
const app = express()


app.use(express.json())

//...


app.post('/api/notes', (request, response) => {
  const note = request.body
  console.log(note)
  response.json(note)
})
```
Ensuite, la requête POST peut être envoyée à l'aide du client REST

## MongoDB <a id="section-3"></a>

Pour stocker nos notes enregistrées indéfiniment, nous avons besoin d'une base de données. La raison de choisir MongoDB comme base de données réside dans sa moindre complexité par rapport à une base de données relationnelle. Vous pouvez installer et exécuter [MongoDB](https://www.mongodb.com/atlas/database) sur votre ordinateur.

On peut faire une première connexion à la base de donnée MongoDB avec le script suivant:

```js
const mongoose = require('mongoose')

if (process.argv.length<3) {
  console.log('give password as argument')
  process.exit(1)
}

const password = process.argv[2]

const url =
  `mongodb+srv://fullstack:${password}@cluster0.o1opl.mongodb.net/?retryWrites=true&w=majority`

mongoose.set('strictQuery',false)
mongoose.connect(url)

const noteSchema = new mongoose.Schema({
  content: String,
  important: Boolean,
})

const Note = mongoose.model('Note', noteSchema)

const note = new Note({
  content: 'HTML is Easy',
  important: true,
})

note.save().then(result => {
  console.log('note saved!')
  mongoose.connection.close()
})
```

Nous pouvons voir l'état actuel de la base de données de l'Atlas MongoDB à partir de Parcourir les collections, dans l'onglet Base de données.
<img src="mongo.webp" width="700" height="550">

### **Schema** <a id="subsection-4"></a>
Un schéma est un objet JSON qui définit la structure et le contenu de vos données.
Après avoir établi la connexion avec la base de données, nous définissons le schéma d'une note et le modèle correspondant :
```js
const noteSchema = new mongoose.Schema({
  content: String,
  important: Boolean,
})

const Note = mongoose.model('Note', noteSchema)
```

Ensuite, on peut créer un nouvel objet note à l'aide du modèle Note. Étant donné que les objets sont créés à l'aide de la fonction constructrice du modèle, ils possèdent toutes les propriétés du modèle, y compris des méthodes pour enregistrer l'objet dans la base de données.

L'enregistrement de l'objet dans la base de données se fait grâce à la méthode save, qui peut être accompagnée d'un gestionnaire d'événements à l'aide de la méthode *then*:
```js
const note = new Note({
  content: 'HTML is Easy',
  important: false,
})

note.save().then(result => {
  console.log('note saved!')
  mongoose.connection.close()
})
```

De la même façon nous pouvons récupérer des objets dans la base de données:
```js
Note.find({}).then(result => {
  result.forEach(note => {
    console.log(note)
  })
  mongoose.connection.close()
})
```


