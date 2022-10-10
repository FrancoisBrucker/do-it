---
layout: layout/post.njk

title: "Dev Web 2"
authors:
  - Gabriel BARBE

---
<!-- Début résumé -->
<!-- Fin résumé -->
Poursuite du Javascript dans un premier temps avec les chapitres : 
 - [Programmation orienté objets]
 - [Découverte des API web]
 Ces chapitres proviennent du site Mozilla.developer.org et font suite à mon premier MON sur JavaScript. (4h30/5h)
 
### Programmation orienté objet 

1. Les bases de JS orientés objet. 
Dans ce chapitre nous sommes inités à ce qu'est un objet, comment ils sont construits ainsi que leurs différentes notations. 
Un objet est une collection de variable et de fonctionalités. 
```bash
       var personne = {
        nom: ['Jean', 'Martin'],
        age: 32,
        sexe: 'masculin',
        interets: ['musique', 'skier'],
        bio: function() {
          alert(this.nom[0] + ' ' + this.nom[1] + ' a ' + this.age + ' ans. Il aime ' + this.interets[0] + ' et ' + this.interets[1] + '.');
        },
        salutation: function() {
          alert('Bonjour ! Je suis ' + this.nom[0] + '.');
        }
      };
```

2. Prototypes objet.
Ici, nous détaillons un peu plus le prototypage, les méthodes, la notion d'héritage ainsi que les constructeurs. <br>
Le prototypage permet d'hériter des attributs et des méthodes d'autres objets : ci-dessous, personne1 est construit à partir de Personne. 
```bash
    function Personne(prenom, famille, age, genre, interets) {
        this.nom = {
          'prenom': prenom,
          'famille' : famille
        };
        this.age = age;
        this.genre = genre;
        this.interets = interets;

    let personne1 = new Personne('Jean', 'Biche', 32, 'neutre', ['musique', 'tricot', 'boxe']); //personne1 hérite des attributs de Personne()
```
Nous avons aussi vu comment modifier ce prototypage selon la chaine de prototypage. Tous les objets hérite des prototypes de 'Object()' qui est l'objet original disons.  <img src='Chaine prototypage.png'/><br>
Nous pouvons aussi rajouter des méthodes à notre constructeur 'Personne' avec la structure : 
```bash
Personne.prototype.aurevoir = function() {
  alert(this.nom.prenom + ' est sorti. Au revoir !');
}
```

3. Heritage au sein de JS

Nous voyons ici l'héritage et les constructeurs de manière plus précise et plus concrète. Dans l'exemple ci-dessous, nous créons un objet Professeur qui hérite des attributs de Personne. Nous y rajoutons ensuite un attribut et les deux dernières lignes servent à attribuer les méthodes de Personne à Professeur. 
```bash
 function Professeur(prenom, nom, age, genre, interets, matiere) {
  Personne.call(this, prenom, nom, age, genre, interets);

  this.matiere = matiere;
}
Professeur.prototype = Object.create(Personne.prototype);
Professeur.prototype.constructor = Professeur;
```
Nous voyons ensuite comment attribuer une nouvelle méthode ou encore modifier une méthode de Personne pour notre nouvel objet. 
```bash
Professeur.prototype.saluer = function() {
  var prefix;

  if (this.genre === 'mâle' || this.genre === 'Mâle' || this.genre === 'm' || this.genre === 'M') {
    prefix = 'M.';
  } else if (this.genre === 'femelle' || this.genre === 'Femelle' || this.genre === 'f' || this.genre === 'F') {
    prefix = 'Mme';
  } else {
    prefix = '';
  }

  alert('Bonjour. Mon nom est ' + prefix + ' ' + this.nom_complet.nom + ', et j\'enseigne ' + this.matiere + '.');
};
```
4. Json

Le JSON est un moyen de stocker des objets et leurs propriétés afin de les réutiliser dans différents codes, et pas uniquement des codes JS !<br>
Cela peut aussi être un tableau ou une suite de caractères ou de nombres. 
Nous voyons aussi une méthode de récupération de JSON sur github grâce à l'API XMLHttpRequest.
```bash
var requestURL = 'https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json';
var request = new XMLHttpRequest();
request.open('GET', requestURL);
```
Nous voyons aussi un exemple permettant de créer une page web grâce aux données récoltées sous format JSON, cet exemple est particulièrement intéressant pous son mélange CSS et JS dans la structure "document.createElement"<br> 
<img src='json-superheroes.png'/>