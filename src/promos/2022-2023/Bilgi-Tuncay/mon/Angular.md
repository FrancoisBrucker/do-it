---
layout: layout/mon.njk

title: "Portfolio Angular"
authors:
  - Tuncay Bilgi

date: 2023-01-25

tags:
  - 'temps 2'
  - 'Angular'
  - 'Front'
---
# Résumé :

## Ressources :

- [MON Angular d'un camarade](/do-it/mon/AV/mons/web-front-1)
- [Documentation de Angular](https://angular.io/start)
- [Vidéo rapide sur le fonctionnement de base](https://youtu.be/G0bBLvWXBvc)
- [Documentation tailwind](https://v2.tailwindcss.com/docs)

## Pré-requis : 

{%prerequis 'Niveau intermédiaire '%}
Pré-requis :

- Introduction à html/css/js pour du Frontend
- Shell pour utiliser ssh/scp

 {%endprerequis%}

## Ce qu'on fait :

- 1- Installer Angular et Tailwind
- 2- Dev d'un portfolio à projets
- 3- Build et déploiement du projet sur un serveur distant

# Letsgo :

## 1 - Installer Angular et Tailwind :

Après avoir lu le MON d'antoine sur angular, on se lance.
Nous avons besoin d'installer deux frameworks. Un framwork, en javascript, est un ensemble d'outil permettant de coder plus facilement qu'en utilisant le classique combo HTML/CSS. Ici, on utilise un framework front :  Angular, et un framework de style : Tailwind.

- Angular permet de découper sa page html en composants réutilisables, et de les rendres facilement interactif avec un script JS.
- Tailwind permet d'appliquer du style à son site, c'est à dire le rendre beau.

{%details "Autres frameworks"%}
Front :
- React (le plus à la mode en 2023)
- Vue
- Svelte (le plus expérimentale)

Style :
- Bootstrap (le plus facile à utiliser)
- Pure
- Skeleton

{%enddetails%}

On installe donc nos frameworks :

- On met node.js à jour, sur windows, il faut aller l'installer sur un navigateur, pour linux, la librairie **n** permet de maintenir node à jour facilement depuis votre terminal.

- on installe le cli angular : `npm install -g @angular/cli `
{%attention%}Ne pas faire `npm install angular` cela installera une version obsolète d'angular que vous devrez supprimer pour éviter les conflits. le -g dans la commande installe le framework de façon globale, pas juste dans votre répertoire courant.{%endattention%}

- on initie le projet : `ng new projet`. Cela crée un projet avec la structure recommandée par Angular. 

- On installe tailwind dans le projet : [La documentation officiel est le meilleur tuto pour cela](https://tailwindcss.com/docs/guides/angular)

On a maintenant un projet Angular+Tailwind.

- On lance le projet pour voir à quoi il ressemble : `ng serve` puis sur un navigateur on tape : `localhost:4200`
Vous devriez tomber sur une page pré-remplie avec pleins de documentation pour apprendre angular. Personnellement je n'aime pas cette doc, je me suis appuyé sur les ressources citées plus haut.

## 2 - Dev le site de portfolio à projets.

Le but est de développer un site contenant une unique page web. Cette page web, comme un cv, va contenir des informations sur mon parcours et sur mes projets. Aussi, elle contiendra des éléments interactifs, des images, et des liens vers mes autres coordonnées accesibles depuis internet (de mes autres POK et MON par exemple).

En plus de cela, je veux que mon site soit **Responsive**. C'est à dire que l'affichage doit s'adapter à toute taille d'écran. C'est très peu évident à faire, c'est même fastidieu. Tailwind va nous aider un peu.

### Style

En regardant la doc de Tailwind, on voit que le framework propose de modifier nos balises HTML avec des noms de classes. Ces noms modifie le style de l'élement.
Par exemple `<p>Du texte blanc</p>` peut devenir `<p class="text-red-800">Du texte rouge</p>`.

Ces modifications peuvent être appliquées sous certaines conditions, notamment des conditions de taille d'écran.
Tailwind propose de divisé nos tailles d'écran en 4 catégories, que l'on peut sélectionner avec un préfixe:


- Aucun préfixe : Tous les écrans.
- sm: les tablettes
- md: grandes tablettes et petit ordinateurs
- lg: les pls grands écrans

Pour la documentation technique, allez sur leur site.

On peut alors avoir ceci : `<p class='text-white lg:text-red'> Ce texte est blanc sur téléphone mais rouge sur grand écran</p>`

On ce sert alors de ceci pour styliser nos components de façon responsive.

### Component

Comme dit plus haut, Angular marche avec des components.
Par exemple, si on a besoin d'un bouton, au lieu de le faire en plein milieu de notre page principale, on va créer un component Bouton que l'on va inserer dans la page principale. Comme ça, si on a besoind e plusieurs boutons similairs, au lieu de recopier le code completement à chaque fois, on replace simplement le component ailleurs. Par exemple :

```html
<body>
    <MonBouttonPersonalisé></MonBouttonPersonalisé>
    <MonBouttonPersonalisé></MonBouttonPersonalisé>
</body>
```

et à coté on a un fichier qui définit à quoi ressemble MonBouttonPersonalisé, ici un bouton qui quand cliqué, nous redirige sur unlien.fr :

```html
<div>
    <button>BOUTON</button>
    <a href='https://unlien.fr'><a>
</div>
```
Pour créer un component vide avec l'ossature désirée on tape `ng generate component nom-component`
On l'appelle dans un html avec la balise `<app-nom-component></app-nom-component>`.

En guise d'exemple plus concret, pour mon projet, j'ai plusieurs components : 

- app | L'endroit où je rassemble tous les components pour former la page
- header | Une barre tous en haut de la page, avec un titre et des liens vers mes coordonnées
- Leftside | Une barre à gauche avec des infos sur moi.  Chaque info est encapsulé dans un component LeftSection
- LeftSection | Un conteneur qui affiche des informations d'après un format précis et modulable
- Center | Le centre de la page qui contient un carousel d'image
- Carousel | Un carousel qui affiche des images de mes projets, il est interactif et codé à la main

Avec tout cela, on est en guise de créer une page internet. Elle est **reponsive** et le contenu peut être modifier sans revoir toute l'ossature du projet. Voici un apreçu :

 - Sur grand écran et sur Mobile :
<div style='display:flex'>
    <img src='./../images/monangular.png' >
    <img src='./../images/monangulartel.png' >
</div>

## 3 - Build et déploiement du projet sur un serveur distant

Pour aller plus loin, on va déployer notre page sur le serveur ovh du parcours Do-it.

{%details 'Se connecter à OVH1' %} Pour aller sur ovh1, il vous faut une clé ssh et un compte vous appartena,t. Pour cela, il faut aller voir M.Brucker, je ne détaille pas ici la démarche{%enddetails%}

Nous allons faire ce qu'on appelle **un site statique**. C'est un site dont le contenue ne change pas. Cest à dire que tous les utlisateurs verrons la même chose, et cette chose ne peut être mise à jour que si on modifie les fichiers du serveur.
C'est à mettre en opposition aux **sites dynamiques** qui possèdent une base de données et un programme qui peret d'afficher des choses différentes selon les utilisateurs, et de mettre à jour ces choses dans la base de données.

Les sites statiques sont très bien pour l'application qu'on en fait. C'est à dire qe je veu montrer la même chose à tous le monde, et je n'ai pas besoin de faire de mises à jour régulière du contenu.

En plus, OVH1 possède un répertoire particulier : www, qui permet de relier une page html directement sur internet.

## Build : 

Les serveurs web ne savent lire que trois choses : Le html, le css et le js. Nous avons un projet compliqué, avec plein de typescript, des "node_modules", des fichiers de configuration etc.. on ne peut pas mettre ça directement sur le serveur et s'attendre à ce que cela fonctionne.

On réalise une étape qu'on appelle la complilation (le build en anglais) qui permet de traduire tous nos fichiers et de nous sortir à la fin que les trois choses dont nous avons besoin : le html, le css et le js.

## Transfert

Sur angular on compile avec `ng build`. Cela créer des fichiers dans `./projet/dist`, dist pour distribution, c'est ça qu'on va mettre sur le serveur.

Pour mettre sur le serveur on utlise la commande 'scp' qui transfert des fichiers par ssh.

        scp -r ./dist epice@ovh1.ec-m.fr:/home/epice/www/

Cette commande copie tous ce qu'il y a dans dist pour le transferer dans le dossier www du compte epice sur ovh1.

Après cela, il suffit d'aller sur internet pour voir.

Dans mon cas :

    http://www.curcuma.ovh1.ec-m.fr


## Pour aller plus loin :

A chaque mise à jour du projet, il faut rebuild, puis recopier les fichiers. Cela peut être embêtant, je vous propose d'automatiser ça comme je le fais dans la deuxième partie de mon POK : Artblog déploiement.


 




