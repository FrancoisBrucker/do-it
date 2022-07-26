---
layout: layout/post.njk

title: "Serveur Distant"
authors:
  - Gabriel BARBE

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
<img src="C:\do-it\src\pok\GB\POK\images\routes.png"/>

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
- Rajouter des routes pour amener aussi la partie de timothée sur le serveur 

