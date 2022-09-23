---
layout: layout/post.njk

title: "Web Front 1"
authors:
  - Antoine Varnerot

---

<!-- début résumé -->
Framework Angular
<!-- fin résumé -->

## Description

Pour ce MON, étant donné que j’ai fait un stage en développement web, j’ai décidé d’utiliser les 10h de temps en autonomie pour reprendre les quelques connaissances que j’avais du framework Angular et de les approfondir. J’ai choisi ce framework car il fait partie de la stack utilisé dans mon alternance.


## Premiers pas

### 1. Installations

Sur un terminal, installer le CLI d'Angular (Command Line Interface) à l'aide de npm. 

`npm install -g @angular/cli`

<mark>Note : -g signifie qu'on installe Angular "globalement" sur l'ordinateur et qu'on aura pas à le réinstaller pour chaque projet</mark>

### 2. Créer un projet

Pour créer un projet, on écrit dans le terminal et à l'endroit voulu :
`ng new mon-projet`

<mark>Note : ng fait référence à Angular et sera l'abréviation à utiliser pour toutes les autres commandes que l'on va utiliser.</mark>

Cette commande va créer un dossier avec plusieurs fichiers mais celui qui va le plus nous intéresser est le dossier src (source). C'est ce dossier que l'on va modifier et où on va coder notre site. Voici l'arborescence de ce dossier :

```bash
src
    ├── app
    ├── assets
    ├── environnements
    ├── index
    ├── main
    ├── styles
    .
    .
    .

```

Pour visualiser son site, il faut le lancer sur un serveur. Dans un terminal ouvert au dossier du projet, lancez la commande :
`ng new mon-projet`
Ensuite rendez-vous à l'adresse http://localhost:4200/ et ceci devrait s'afficher :

<img src="../../assets/Angular-init.png">

C'est la page qu'Angular génère de base quand on crée un projet.



