---
layout: layout/pok.njk

title: "POK 1 : Création d'une application en No Code sur Adalo"
authors:
  - Lucie Le Boursicaud

date: 1970-09-01

tags: 
  - "temps 1"

résumé: Ce POK a pour but d'utiliser un site de création d'application No Code que je ne connais pas pour créer une application qui permettra à des utilisateurs de visualiser des recettes et d'en publier.
---
{%prerequis 'Niveau débutant'%} 
Aucun prérequis !  
{%endprerequis%}

## Sommaire

1. Découverte d'Adalo
2. Idée de l'application 
3. Développement de l'application
4. Conclusion sur l'outil utilisé

## 1.Découverte d'Adalo
"Transformer des idées réelles en applications réeeles sans écrire une seule ligne de code", voici la promesse d'Adalo, un nouvel outil permettant de bâtir des applications web et mobiles sans coder.
Le but d'Adalo est de permettre à n'importe qui de construire une application de manière la plus simple possible. 
La première étape est évidemment de se créer un compte sur Adalo. Ensuite il faut créer une nouvelle application.

## 2.Idée de l'application
J'ai décidé de réaliser une application de partage de recettes: <strong>Lucette | Recipes & Co</strong> afin de pouvoir garder en mémoire mes recettes et les partager à d'autres utilisateurs. 

[Lien vers l'application](https://lucie-le-boursicauds-team.adalo.com/les-recettes-de-lulu?_gl=1%2A19rdhxq%2A_ga%2AMTQyNTAyOTgxNC4xNjk1MDM4NjQ2%2A_ga_SWT45DV35L%2AMTY5NTQ5NTc1My4xMi4wLjE2OTU0OTU3NTMuNjAuMC4w&target=3hni4na11m72olt1r9567f5qe&params=%7B%7D)

##### Fonctionalités nécessaires
Afin de me donner des objectifs de réalisations voici la liste des fonctionalités qui devront être mise en place obligatoirement à la fin des 20h de projet :
+ Authentification 
+ Fonctionalité de "mot de passe oublié"
+ Pouvoir changer les informations de son profil
+ Pouvoir visualiser une recette
+ Pouvoir publier une recette
+ Ajouter une recette a ses favoris 
+ Pouvoir noter une recette

##### Fonctionalités supplémentaires optionnelles
Une fois toutes ses fonctionalités mises en place, le temps restant sera consacré à d'autres fonctionalités : 
+ Pouvoir laisser un avis sur une recette
+ Avoir des badges en fonction du nombre de recettes publiées
+ Pouvoir partager une recette 
+ Ajouter une liste d'ingrédient pour chaque recette avec les quantités adéquates

## 3.Développement de l'application
Pour commencer à developper l'application je me suis occupé du système d'inscription et d'authentification. Aucune difficulté avec Adalo puisque le site fait déjà la moitié du travail pour nous. Je me suis donc concentrée sur le design pour rentre l'application joli dès la première interraction avec l'utilisateur.

<div style="display:flex">
<div><img src="login.png"></div>
<div><img src="signup.png"></div>
</div>

Ensuite j'ai créé de nouvelles collections dans la database : Recettes et Categories.
Une fois créer j'ai donc pu mettre en place un formulaire permettant la création d'une nouvelle recette. La encore Adalo permet un gain de temps important en proposant des formulaires tout fait dans lequel on peut décider quel champs doit apparaitre, si il est obligatoire ou non, ect... J'ai donc créer plusieurs recettes via ce formulaire puis j'ai créé la page d'accueil permettant à l'utilisateur de visualiser des recettes suggérées et de faire une recherche si celui-ci a déjà une idée de ce qu'il veut tester. 

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
Pour que le parcours utilisateur soit le plus agréable possible j'ai ajouté la bar de navigation. Lorsque l'utilisateur clique sur l'une des icones il est redirigé vers la page corresponsante. 
