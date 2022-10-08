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