---
layout: layout/pok.njk

title: "POK 1 : Création d'une application en No Code sur Adalo"
authors:
  - Lucie Le Boursicaud

date: 1970-09-01

tags: 
  - "temps 1"
  - "No-Code"
  - "Adalo"
  - "Application"
  - "Développement"

résumé: Ce POK a pour but d'utiliser un site de création d'application No Code "Adalo" pour créer une application qui permettra à des utilisateurs de visualiser des recettes de cuisine ainsi que d'en publier.
---
{%prerequis 'Niveau débutant'%} 
Aucun prérequis !  
{%endprerequis%}

# Sprint 1 
###### Objectifs du premier sprint
Fonctionalités à implémenter : 
+ [x] Authentification  - 1
+ [x] Pouvoir changer les informations de son profil  - 1
+ [x] Pouvoir visualiser une recette  - 2
+ [x] Pouvoir publier une recette  - 1
+ [x] Pouvoir se déconnecter  - 1

Autres éléments : 
+ [X] Avoir un design/visuel agréable - 3
+ [x] Travailler le parcours utilisateurs - 2

## Sommaire

1. Découverte d'Adalo
2. Idée de l'application 
3. Développement de l'application

## 1.Découverte d'Adalo
"Transformer des idées réelles en applications réeeles sans écrire une seule ligne de code", voici la promesse d'Adalo, un nouvel outil permettant de bâtir des applications web et mobiles sans coder.
Le but d'Adalo est de permettre à n'importe qui de construire une application de manière la plus simple possible. 
La première étape est évidemment de se créer un compte sur Adalo. Ensuite il faut créer une nouvelle application.
On peut choisir si l'on souhaite créer une application mobile ou responsive qui permettra un visuel adéquat si on utilise un ordinateur par exemple. Puis le site nous propose des thèmes ou bien de partir d'un visuel vide (c'est mon choix). Enfin on choisi le nom de l'application et les couleurs principales qui peuvent être modifiées plus tard.

<div style="display:flex" height = "50px">
<img src="createnewapp.png" height="30px"></div>
<div style="display:flex"><img src="choice.png"></div>
<div style="display:flex"><img src="choicename.png"></div>

Nous arrivons alors sur l'environnement d'Adalo qui se présente comme ceci : 

<div><img src="adaloenvi.png"></div>

A droite le bouton <strong>+</strong> nous permet d'ajouter des élements tels que du texte, des boutons, des listes ou encore des images et des formulaires... Lorsque l'on sélectionne un élément on peut le personaliser sur sa taille, sa forme, sa visibilité ou encore les actions qui en découlent lorsque l'on clique dessus.
<div><img src="branding.png"></div>
Le menu <strong>Branding</strong> permet de personnifier les coloris de l'application ainsi que la police principale.
<div><img src="screens.png"></div>
Le menu <strong>Screen</strong> permet de visualiser les différentes pages déjà créés et d'en ajouter de nouvelles.
<div><img src="database.png"></div>
Dans le menu <strong>Database</strong> on peut ajouter de nouvelles collections qui correspondent aux tables de données. On peut créer des liens entre les différentes tables et visualiser les données déjà enregistrées.
<div><img src="settings.png"></div>
Dans le menu <strong>Setting</strong> on peut changer le nom de l'application, définir si l'application à le droit d'être cloner ou non, obtenir une API d'accès ou encore supprimer l'application.
<div><img src="publish.png"></div>
Le menu <strong>Publish</strong> permet de publier son application (mais pour ça il faut payer).
<div><img src="analytics.png"></div>
Le menu <strong>Analytics</strong> permet d'avoir un apperçu du nombre d'utilisateurs qui se connecte à l'application ainsi que d'autres données qui ne seront pas utilise comme nous ne pourrons pas publier l'application.
<div><img src="versionhistory.png"></div>
Enfin le menu <strong>Version History</strong> permet d'enregistrer différentes versions de design, là aussi il faut avoir la version payante pour accéder à cette fonctionalité. 

## 2.Idée de l'application
J'ai décidé de réaliser une application de partage de recettes: <strong>Lucette | Recipes & Co</strong> afin de pouvoir garder en mémoire mes recettes et les partager à d'autres utilisateurs. 

[Lien vers l'application](https://lucie-le-boursicauds-team.adalo.com/les-recettes-de-lulu?_gl=1%2A19rdhxq%2A_ga%2AMTQyNTAyOTgxNC4xNjk1MDM4NjQ2%2A_ga_SWT45DV35L%2AMTY5NTQ5NTc1My4xMi4wLjE2OTU0OTU3NTMuNjAuMC4w&target=3hni4na11m72olt1r9567f5qe&params=%7B%7D)

##### Fonctionalités nécessaires
Afin de me donner des objectifs de réalisations voici la liste des fonctionalités qui devront être mise en place obligatoirement à la fin des 20h de projet :
+ [x] Authentification 
+ [ ] Fonctionalité de "mot de passe oublié"
+ [x] Pouvoir changer les informations de son profil
+ [x] Pouvoir visualiser une recette
+ [x] Pouvoir publier une recette
+ [~] Ajouter une recette a ses favoris 
+ [~] Pouvoir noter une recette

## 3.Développement de l'application
Pour commencer à developper l'application je me suis occupé du système d'inscription et d'authentification. Aucune difficulté avec Adalo puisque le site fait déjà la moitié du travail pour nous. Je me suis donc concentrée sur le design pour rentre l'application joli dès la première interraction avec l'utilisateur.

<div style="display:flex">
<div><img src="login.png"></div>
<div><img src="signup.png"></div>
</div>

Ensuite j'ai créé de nouvelles collections dans la database : Recettes et Categories.
Une fois créer j'ai donc pu mettre en place un formulaire permettant la création d'une nouvelle recette. 
La encore Adalo permet un gain de temps important en proposant des formulaires tout fait dans lequel on peut décider quel champs doit apparaitre, si il est obligatoire ou non, ect... 

<div style="display:flex">
<div><img src="addrecipes.png"></div>
<div></div>
</div>

J'ai donc créer plusieurs recettes via ce formulaire puis j'ai créé la page d'accueil permettant à l'utilisateur de visualiser des recettes suggérées et de faire une recherche si celui-ci a déjà une idée de ce qu'il veut tester. 

<div style="display:flex">
<div><img src="homapge.png"></div>
<div></div>
</div>

Lorsque l'utilisateur clique sur l'un des recettes, il est renvoyé vers une nouvelle page de visualisation de la recette qu'il a choisi. Les différentes imformations de la recette y sont inscrites ainsi que les étapes de la recette.
Si l'utilisateur est le créateur de la recette alors il apprait une icone permettant de modifier la recette si celui-ci le désire.

<div style="display:flex">
<div><img src="recipes.png"></div>
<div></div>
</div>

Une fois cette partie réalisé je me suis consacrée à la page de profil de l'utilisateur. On y découvre ses informations qu'il peut modifier si nécessaire ainsi que les recettes qu'il a publié, elles aussi modifiables.

<div style="display:flex">
<div><img src="myprofile.png"></div>
<div></div>
</div>

Pour que le parcours utilisateur soit le plus agréable possible j'ai ajouté la bar de navigation. Lorsque l'utilisateur clique sur l'une des icones il est redirigé vers la page corresponsante. 

# Sprint 2
###### Objectifs du deuxième sprint
Fonctionalités à implémenter : 
+ [ ] Fonctionalité de "mot de passe oublié"
+ [~] Ajouter une recette a ses favoris 
+ [~] Pouvoir noter une recette
+ [ ] Pouvoir laisser un avis sur une recette
+ [ ] Avoir des badges en fonction du nombre de recettes publiées
+ [ ] Pouvoir partager une recette 
+ [ ] Ajouter une liste d'ingrédient pour chaque recette avec les quantités adéquates

## Sommaire

1. Développement de l'application
2. Conclusion 
