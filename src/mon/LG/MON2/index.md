---
layout: layout/post.njk

title: "MON 2:Web Front 1"
authors:
  - Louise Gacoin

---
Mes objectifs pour ce MON sont:
- Améliorer ma maitrise du langage de l'informatique
- Apprendre les bases du HTML
- Apprendre les bases du CSS
- Coder un site simple
- Si temps, apprendre les bases du Java Script

## 0. Le langage informatique pour les débutants


## 1. Débuts avec Html

J'ai suivi les cours de https://www.internetingishard.com/ qui sont très bien fait et accessibles aux débutants.

Pour commencer un projet, il faut créer un dossier dédié et l'ouvrir avec Visual Studio Code ( ou autre éditeur de texte de votre choix). Ensuite créer un fichier avec l'extension.html. Le squelette de base est le suivant:

```html
<!DOCTYPE html> <!--c'est un doc html-->
<html>
	<head>  <!-- contient les informations de la page, non visibles sur celle ci-->
		<meta charset="utf-8"/> <!-- permet d'afficher tous les caractères spéciaux-->
		<title> Survivre face à un Ours</title>
	</head>
	<body> <!-- le contenu visible de la page -->
  </body>
</html>
```

Sur ce site, je vais expliquer comment réagir lors d'un face à face avec un ours.
Il y aura donc 2 paragraphes principaux et des images :

```html
<!DOCTYPE html> 
<html>
	<head>  
		<meta charset="utf-8"/> 
		<title> Survivre face à un Ours</title>
	</head>
	<body> 
    <h1> Survivre face à un ours </h1> <!-- titre de ma page-->
    <!--Introduction-->
    
    <h2> Face à un ours noir </h2>
    <h3> Commment les reconnaitre?<h3> 
    <!--blabla...-->
    <h3> Commment réagir?<h3> 
    <!--blabla...-->  
    
    <h2> Face à un ours brun ou Grizzly </h2>
    <h3> Commment les reconnaitre?<h3> 
    <!--blabla...-->
    <h3> Commment réagir?<h3> 
    <!--blabla...-->  
  </body>
</html>
```

En remplissant les blabla... avec du texte et des images on arrive au site suivant :


J'ai aussi ajouté des listes ainsi que des liens vers une boutique de spray anti ours.

Il faut maintenant mettre en forme tous cela avec CSS.

