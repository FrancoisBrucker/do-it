---
layout: layout/pok.njk

title: "Serveur Distant"
authors:
  - Gabriel BARBE

date: 2023-01-04

tags:
  - 'temps 2'
---
<!-- Début Résumé -->
POK visant à reproduire le site effectué dans le temps mais sur un serveur distant et en y rajoutant du back-end. 
<!-- Fin Résumé -->
# Organisation
Dans un premier temps, ajouter du back-end grâce au MON suivi sur le site de M. Brucker puis dans un second temps l'implémenter sur un serveur distant. 
TO do-list : 
Sprint 1 : 
- Ramener le site sur l'ovh 
- Gérer des cookies pour implémenter une page de connexion
<br> 
Sprint 2 :
- Insérer une base de donnée
- Gérer le backend en node
- Si le temps le permet voir un peu pour la sécurité  

### Nouveau projet Express 
Pour le développement du projet, j'ai choisi de le faire via Express car c'est ce que recommandait M. Brucker et donc dans un premier temps je crée un nouveau projet à l'adresse http://localhost:3000/. <br>
Concernant la base de données et le langage associée à utiliser, j'ai longtemps hésité mais j'ai finalement décidé de suivre l'exemple associé à Express sur "http://developer.mozilla.org" et donc d'utiliser l'ORM Mongoose associée à une base de données MangoDB.
Mon code est disponible sur [Mon Github].(https://github.com/gabrielbarbe00/POK/tree/main/POK_2/express-PFCback)

### Création de la base de données 
Afin de compléter mon premier site, j'ai eu pour idée d'ajouter une option permettant de sélectionner un champion et un pays : ainsi J1 sera désigné par le champion Zidane ou le pays Brésil. Le but est donc de créer une base de données avec 5 champions et 5 pays. J'ai repris en grande partie le code visible sur [mon MON](../../../mon/GB/Mons/coteweb) que j'ai personnalisé afin d'y mettre mes exigences. Le champion devra donc avoir les caractéristiques "nom", "prénom" et "numéro" ; le pays, lui, sera associé aux caractéristiques "nom" et "couleur". Ci-dessous le code concernant le champion : 
```bash
const mongoose = require("mongoose");

const Schema = mongoose.Schema;

const JoueurSchema = new Schema({
  first_name: { type: String, required: true, maxLength: 100 },
  family_name: { type: String, required: true, maxLength: 100 },
  number:{ type: Number, required: true, maxLength:2},
});

JoueurSchema.virtual("name").get(function () {
  // To avoid errors in cases where an author does not have either a family name or first name
  // We want to make sure we handle the exception by returning an empty string for that case
  let fullname = "";
  if (this.first_name && this.family_name) {
    fullname = `${this.family_name}, ${this.first_name}`;
  }
  if (!this.first_name || !this.family_name) {
    fullname = "";
  }
  return fullname;
});

JoueurSchema.virtual("url").get(function () {
  return `/catalog/joueur/${this._id}`;
});

// Export model
module.exports = mongoose.model("Joueur", JoueurSchema);
```
```bash
function JoueurCreate(first_name, family_name, number, cb) {
  joueurdetail = {first_name:first_name , family_name: family_name, number:number}
  
  var joueur = new Joueur(joueurdetail);
       
  joueur.save(function (err) {
    if (err) {
      cb(err, null)
      return
    }
    console.log('New Joueur: ' + joueur);
    joueurs.push(joueur)
    cb(null, joueur)
  }  );
}
```
### Routes 

Nous en arrivons ici à la partie création des routes pour notre site sur le serveur. En premier lieu, nous crééons un dossier "controllers" où l'on mettra,  pour chaque fichier de notre base de donées, les requêtes de création, d'affichages, de supression etc. Ensuite, nous crééons un fichier javascript "catalog.js" où l'on définit les routes de notre site à proprement parlé. J'obtients donc les routes suivantes : 
- http://localhost3000/catalog
- http://localhost:3000/catalog/pays
- http://localhost:3000/catalog/joueurs
- http://localhost:3000/users
Ici, la route "catalogue" n'a pas de sens en soi, j'ai simplement utilisé des fichiers similaires à mon cours afin de ne pas me perdre. Les routes pays et joueurs sont pour le moment vide car on n'y a pas encore implenté la base de données. 
 <img src="./../Images/routes.png" alt='routes'/>

### Etablissement des premières pages 

On arrive donc à une partie plus intéressante, celle de la liaison entre ma première partie, le front-end, et mon site actuellement hébérgé sur un serveur. 
Pour ce faire, nous utilisons pug (choix par défaut du cours que je regrette un peu à ce moment car je dois réadapter certains de mes codes sources).<br>
Dans les dossiers créés lors de l'utilisation d'express, nous avons un dossier "views". Comme son nom l'indique, celui-ci contiendra les interfaces vus par l'utilisateur. J'implémente donc mon code html "PFC" dans le fichier "index.pug". C'est à ce moment que cela se complique car bien que pug reprend complétement l'idée de html, il y'a tout de même de nombreux changements à opérer dans un langage que je ne connais pas. 

# Fin du sprint 1 
### Ce qu'il reste à faire 
Comme on peut le voir, il reste de nombreuses choses à effectuer, j'ai désormais plus de visibilité sur l'ensemble du projet : 
- Adapter mon script afin que le site marche comme avant
- Je pense à modifier la base de données afin que celle-ci soit juste un historique des anciens coups car l'objectif initiale demanderait beaucoup de changement sur le front et me limiterai dans la suite des évènement. 
- Ramener le site sur l'ovh une fois que tout cela sera fait 
- Insérer une page de connexion
- Sécurité si le temps me le permet mais cela me parait compliqué. 

# Début du sprint 2 
Le script remarche comme avant, j'ai simplement eu à effectuer une traduction html -> pug (des sites s'en occupent, c'est beaucoup plus facile du coup)
### Changement base de donnée
Commme évoqué précedemment j'ai finalement opté pour un changement de base afin d'établir un historique des coups joués. Dans un premier temps, je me contente de rentrer moi-même les coups afin d'avoir une page propre avec des données puis dans un second temps, je les actualiserai avec les données issues de mon site. <br>. 
J'ai donc commencé par recréer des routes notamment la route (/historique). 
J'ai ensuite modifié tous mes fichiers afin de créer la nouvelle base de donnée avec les donnnées intéressantes : le dit coup et la date à laquelle il a été effectué. Je crée donc un nouveau schéma dans un fichier "coup.js", dans le dossier "models", où j'insère mon schéma : 
```bash
const mongoose = require("mongoose");

const Schema = mongoose.Schema;

const CoupSchema = new Schema({
  name: { type: String, required: true, maxLength: 100 },
  date: { type: Date, default: Date.now() },
});

CoupSchema.virtual("url").get(function () {
  return `/coup/${this._id}`;
});

// Export model
module.exports = mongoose.model("Coup", CoupSchema);
```
Je crée ensuite un nouveau fichier historiqueController.js afin de rentrer les fonctions en lien avec ma base de donnée
```bash
const { body, validationResult } = require("express-validator");

const Coup = require("../models/coup");
const async = require("async");

// Display list of all Books.
exports.coup_list = function (req, res, next) {
    Coup.find()
    .populate("date")
      .exec(function (err, list_coups) {
        if (err) {
          return next(err);
        }
        //Successful, so render
        res.render("coup_list", { title: "Historique de coup", coup_list: list_coups });
      });
  };
  ```
Cette fonction sert simplement à implémenter la liste de coup sur mon site, il ne reste plus qu'à créer un fichier .pug où je fais le front. Je débute par un fichier très rudimentaire : 
```bash
extends layout

block content
  h1= title
  
  ul
  each coup in coup_list
    li 
      p #{coup.name} 
      | #{coup.date}

  else
    li There are no authors.
```
Ma page historique ressemble alors à cela : <img src="./../Images/Historique.png" alt='routes'/>
En y appliquant le design de mon site et quelques touches de CSS en plus, on obtient : <img src="./../Images/Data.png" alt='routes'/>

### Mise à jour de la base de données
Il me reste maintenant à actualiser l'historique à chaque coup jouer, c'est une manipulation qui me prend beaucoup de temps et que je n'ai toujours pas réussi à l'heure actuelle. En effet, le problème est que mon script utilise la fonction "appenchild" pour faire apparaitre la liste de coups et que mes variables "pierre", "feuille" et "ciseaux" ne semblent pas être déclarées. Ainsi, lorsque je veux mettre ma base de données à jour avec une fonction dans le fichier "coup.js", le terminal me renvoi que la variable "pierre" n'est pas déclarée : 
```bash
pierre.addEventListener('click', function(){
  mongoose.model("Coup", CoupSchema).findOneAndUpdate({name:'Pierre'}, {date}, function(err, utilisateur)
  {
    if (err) return handleError(err);
  })
});
```
J'avoue avoir beaucoup de mal à passer cette étape, j'ai même fini par demander à ChatGPT si il savait comment faire et il m'a donné un code présentant exactement le même problème de variable. Il utilisait pourtant aussi la fonction "appenchild()" pour faire apparaitre sa variable.
<br>
J'ai aussi essayé de rentrer cette fonction directement dans mon fichier script comme ça j'évite ce problème.  

### Mise du site sur l'ovh 
J'ai suivi en grande partie le [POK de Tuncay](https://francoisbrucker.github.io/do-it/pok/un-site-chez-moi/TBi/ServeurDistant/) qui fournit un très bon tutoriel pour cette partie. Néanmoins, mon camarade a déployé son site en utilisant node et j'ai utilisé express pour le faire, ce qui mène à quelques différences. 
Pour commencer on se connecte via ssh à l'ovh. On y clone ensuite le répo github du projet dans le dossier "node" :  
```bash 
git clone https://github.com/gabrielbarbe00/POK.git
```
Il faut ensuite indiquer au programme qu'il doit se lancer sur le port que l'on m'a assigné. Cet objectif est réalisé d'une manière très spécifique à express, il suffit d'ajouter deux lignes dans le fichier "app.js" :
```bash
const port = 10408

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
```
Ainsi, l'application se lance désormais sur le bon port et tourne sur l'ovh, objectif accompli ! Il ne nous reste plus qu'à ouvrir un terminal virtuel tournant en continu afin que notre serveur ne se ferme pas dès que nous quittons le ssh.
On rentre donc la commande suivante : 
```bash
screen -S PFC
```
On lance l'application puis nous quittons le terminal avec la commande CTRL A + D. 
Le site est disponible à [cette adresse](http://node.coriandre.ovh1.ec-m.fr)

## Feedback
Je dois avouer que la gestion du "back-end" m'a nettement moins parlé que celle du "front", je suis content d'avoir effectué ce POK pour m'en rendre compte. Je pense que les deux aspects du site sont en pratique très différent à coder, néanmoins ce projet était très formateur ne serait-ce que dans la compréhension de ce qu'est un site web. Je suis tout de même très déçu de n'avoir pu outrepasser le problème de mise à jour de l'historique, surtout que cela m'a pris énormément de temps que je n'ai pas pu passer à développer une page de connexion par exemple. 