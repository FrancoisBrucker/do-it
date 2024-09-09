---
layout: layout/mon.njk

title: "L'environnement de développement idéal pour une équipe"
authors:
  - Loïck Goupil-Hallay

date: 2024-09-05

tags:
  - 'temps 1'
  - 'Développement'
  - 'Environnement de développement'

résumé: "Introduction à l'environnement de développement idéal pour une équipe"
---

{%prerequis 'MON débutant'%}
Savoir ce qu'est un ordinateur et utiliser un navigateur web
{%endprerequis%}


<script type="module">
  // Mermaid configuration
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true });
</script>

# L'environnement de développement idéal pour une équipe

## Table des matières<a name="table-des-matières"></a>
1. [Introduction](#introduction)
    - [Le Développeur](#le-développeur)
2. [Outils au poste](#outils-au-poste)
    - [Système d'exploitation](#système-dexploitation)
    - [Navigateur](#navigateur)
    - [IDE](#ide)
    - [Terminal](#terminal)
    - [Gestionnaire de versions](#gestionnaire-de-versions)
    - [Langages de programmation](#langages-de-programmation)
    - [Conteneuristation](#conteneurisation)
3. [Outils partagés](#partagés)
    - [Communication](communication)
    - [Partage de code](#partage-de-code)
    - [Gestion de projet](#gestion-de-projet)
    - [Outils de CI/CD](cicd)
4. [Outils de stockage](stockage)
    - [Stockage de données](#outils-de-stockage-de-données)
    - [Stockage d'artefacts](#outils-de-stockage-dartefacts)
5. [Outils de monitoring](#outils-de-monitoring)
    - [Monitoring applicatif](#monitoring-applicatif)
    - [Monitoring système](#monitoring-système)
    - [Monitoring réseau](#monitoring-réseau)
    - [Monitoring de logs](#monitoring-de-logs)
6. [Qualimétrie Logicielle](#qualimétrie-logicielle)
    - [Analyse de code](#analyse-de-code)
    - [Tests](#tests)
    - [Déploiement](#déploiement)
7. [Conclusion](#conclusion)

## Introduction<a name="introduction"></a>
Dans le monde du développement logiciel, une équipe doit disposer d'un ensemble d'outils permettant assurer l'efficacité et la qualité de son travail. Ces outils sont essentiels non seulement pour coder, mais aussi pour partager et gérer le code, communiquer efficacement, analyser et tester les applications, ainsi que pour déployer des solutions robustes. Cette section vise à offrir un aperçu détaillé des outils incontournables qui facilitent chaque aspect du processus de développement.

L'objectif est de vous fournir une vue d'ensemble des outils et pratiques qui sont cruciaux pour le bon fonctionnement d'une équipe de développement, afin que vous ne soyiez pas perdu lorsque vous rejoindrez une équipe de développement.

Toutes les informations concernants les habitudes des développeurs seront tirées des résultats du sondage [Stack Overflow Developer Survey 2024](https://survey.stackoverflow.co/2024)

### Le Développeur<a name="le-développeur"></a>
Le développeur est une créature étrange qui passe la majeure partie de son temps à écrire du code, à résoudre des problèmes et à boire du café. Il est souvent solitaire, mais il peut aussi travailler en équipe. Il est passionné par la technologie et aime apprendre de nouvelles choses. Il est curieux, créatif et persévérant. Il est capable de passer des heures à chercher une solution à un problème, sans jamais abandonner. Il est un peu geek, un peu artiste, un peu scientifique. Il aime les défis et les puzzles. Il n'aime pas les bugs, les retards, les réunions et les gens en général. Il est un peu bizarre, mais c'est ce qui fait son charme.

C'est généralement quelqu'un qui a des habitudes et qui aime personnaliser son environnement de travail, il ne faut donc pas le brusquer en lui imposant des outils qu'il n'aime pas. Il est important de lui laisser le choix de ses outils, tout en lui fournissant des recommandations et des bonnes pratiques.

## Outils au poste<a name="outils-au-poste"></a>
<p style="background-color: #ffb1a8; border: 2px solid #ba1300; padding: 10px; border-radius: 10px">
Cette section sert uniquement pour votre culture personnelle.<br>
Vous trouverez ici une liste de recommandations basées sur les habitudes des développeurs.<br>
Il est important de rappeler qu'<b>il vaut mieux laisser le choix des outils du poste de travail à chaque développeur</b>, en fonction de ses préférences et de ses besoins.
</p>

Un développeur a besoin d'un ensemble d'outils pour travailler efficacement. Ces outils sont installés sur le poste de travail de chaque développeur et sont essentiels pour coder, tester et déployer des applications.

Il est essentiel qu'un développeur puisse tester son code localement avant de le partager avec l'équipe. Premièrement car il est timide et n'aime pas que l'on puisse voir que ce qu'il fait ne fonctionne pas tout de suite. Pour cela, il doit disposer d'un environnement de développement complet, incluant un éditeur de texte, un terminal, un gestionnaire de versions, des langages de programmation, des outils de virtualisation et de conteneurisation.

### Système d'exploitation<a name="système-dexploitation"></a>
**Définition** : Le système d'exploitation (OS), c'est le logiciel qui permet à un ordinateur de fonctionner. Il gère les ressources matérielles de l'ordinateur, comme le processeur, la mémoire, le disque dur, etc. Ca lui qui permet de lancer des applications, de lire des fichiers, de se connecter à internet, etc.

Les résultats du [sondage OS](https://survey.stackoverflow.co/2024/technology#1-operating-system) montre que les développeurs ont utilisé au moins une fois dans l'année, dans le cadre professionnel:
<pre class="mermaid" style="background-color: transparent">
%%{init: {'theme': 'dark'}}%%
xychart-beta horizontal
  x-axis ["Linux (Toutes distributions)", "Windows", "MacOS", "Windows Subsystem for Linux"]
  y-axis "" 0 --> 65
  bar [57.3, 47.6, 31.8, 16.8]
</pre>

En règle générale, les développeurs préfèrent utiliser tout ce qui n'est pas Windows, car c'est plus stable, plus rapide, plus sécurisé. Un autre avantage est que ces systèmes d'exploitation sont hautement personnalisables, ce qui permet de les adapter à ses besoins.\
Le départage entre MacOS et Linux se fait en fonction des préférences personnelles de chacun, et surtout en fonction des préférences pécuniaires de l'entreprise, car fournir une flotte de Macs à tous les développeurs coûte beaucoup plus cher que de fournir des PC sous Linux.

### Navigateur<a name="navigateur"></a>
**Définition** : Un navigateur web est un logiciel qui permet de consulter des sites web. Il permet de lire du texte, de regarder des images, de regarder des vidéos, de remplir des formulaires, etc.

Il existe 3 familles de navigateurs web:
- Les navigateurs basés sur Chromium (Google Chrome, Microsoft Edge, Opera, Brave, Vivaldi, etc.)
- Les navigateurs basés sur Gecko (Mozilla Firefox)
- Les navigateurs basés sur WebKit (Safari)

Pour les postes de travail, les parts de marché sont les suivantes:
<pre class="mermaid" style="background-color: transparent">
%%{init: {'theme': 'forest', 'themeVariables': {'pie1': '#3498db', 'pie2': '#e74c3c', 'pie3': '#2ecc71', 'pie4': '#f39c12'}}}%%
pie
  "Chromium" : 81.24
  "Firefox" : 6.64
  "Safari" : 8.79
  "Autres" : 3.33
</pre>

Sur chacun de ces navigateurs, il est possible d'installer des extensions qui permettent d'ajouter des fonctionnalités supplémentaires. Certaines des extensions  populaires sont:
- [uBlock Origin](https://ublockorigin.com/): Bloqueur de publicités
- [Bitwarden](https://bitwarden.com/): Gestionnaire de mots de passe sécurisé
- [Dark Reader](https://darkreader.org/): Mode sombre pour les sites web
- [Grammarly](https://www.grammarly.com/): Correcteur orthographique et grammatical

Il est aussi possible (au niveau de l'entreprise ou du développeur) d'appliquer un profil de sécurité pour limiter les risques de sécurité liés à la navigation web. Tous les navigateurs modernes proposent des fonctionnalités de sécurité avancées, comme la protection contre le pistage, le blocage des publicités, le blocage des scripts malveillants, etc.

Il n'y a donc pas de navigateur idéal, chacun a ses avantages et ses inconvénients. Il est donc important de choisir un navigateur qui correspond à ses préférences, plutôt que de suivre la tendance.

### IDE<a name="ide"></a>
**Définition** : Un IDE (Integrated Development Environment) est un logiciel qui regroupe un ensemble d'outils pour faciliter le développement logiciel. Il permet d'écrire du code, de le compiler, de le déboguer, de le tester, etc.

Les résultats du [sondage IDE](https://survey.stackoverflow.co/2024/technology#1-integrated-development-environment) montre que les développeurs ont utilisé au moins une fois dans l'année, dans le cadre professionnel:
<pre class="mermaid" style="background-color: transparent">
%%{init: {'theme': 'forest'}}%%
xychart-beta horizontal
  x-axis ["Visual Studio Code", "Visual Studio", "IntelliJ IDEA", "Notepad++", "Vim", "Android Studio", "PyCharm", "Jupyter Notebook/JupyterLab", "Neovim", "Sublime Text", "Eclipse"]
  y-axis "" 0 --> 80
  bar [73.6, 29.3, 26.8, 23.9, 21.6, 16.1, 15.1, 12.8, 12.5, 10.9, 9.4]
</pre>

Jusqu'à récemment, les 3 IDE les plus populaires étaient Visual Studio Code, IntelliJ IDEA et Eclipse. Mais depuis quelques années, Visual Studio Code a pris une longueur d'avance sur ses concurrents, grâce à sa simplicité, sa légèreté, sa rapidité et sa richesse en extensions, le fait qu'il soit gratuit. Il permet notamment l'intégration d'IA pour la complétion de code, le refactoring, le débogage, etc.\
Il est devenu l'IDE de référence pour de nombreux développeurs, quel que soit le langage de programmation utilisé.

D'un autre côté, Eclipse est en perte de vitesse, car il est perçu comme étant trop lourd, trop complexe, trop lent et trop peu personnalisable. Il est encore utilisé dans certaines entreprises, notamment celles qui développent en Java, mais il est en train d'être remplacé par IntelliJ IDEA.

Les outils de JetBrains (IntelliJ IDEA, PyCharm, WebStorm, etc.) sont toujours très populaires, aussi riche en extensions, très performants (sans IA) sur la complétion de code, le refactoring, le débogage, etc. Ils permettent aussi l'intégration d'IA par dessus les fonctionnalités déjà existantes. Mais ils sont payants, ce qui peut être un frein pour certaines entreprises. Ils sont souvent utilisés par les développeurs qui travaillent sur des projets complexes, qui nécessitent des fonctionnalités avancées.

Il n'est pas rare de voir des développeurs utiliser plusieurs IDE en même temps, en fonction du langage de programmation, du projet, de l'équipe, etc. Il est donc important de choisir un IDE qui correspond à ses besoins, plutôt que de suivre la tendance.

### Terminal<a name="terminal"></a>
**Définition** : Un terminal est un logiciel qui permet d'interagir avec le système d'exploitation en ligne de commande. Il permet de lancer des programmes, de manipuler des fichiers, de gérer des processus, etc.

Chaque poste de travail est livré avec un terminal par défaut, mais il est possible d'installer des terminaux plus avancés, comme [Hyper](https://hyper.is/), [iTerm2](https://iterm2.com/), [Windows Terminal](https://aka.ms/terminal), etc. Ces terminaux offrent des fonctionnalités supplémentaires, comme la coloration syntaxique, la complétion automatique, la gestion des onglets, etc.

Il existe des outils permettant d'améliorer l'expérience du développeur sur le terminal, permettant de le personnaliser à la fois visuellement et fonctionnellement.
- [Oh My Zsh](https://ohmyz.sh/): Framework de configuration pour Zsh (ne fonctionne pas sur Windows)
- [Starship](https://starship.rs/): Prompt minimaliste, rapide et hautement personnalisable (fonctionne sur tous les systèmes d'exploitation)

### Gestionnaire de versions<a name="gestionnaire-de-versions"></a>
**Définition** : Un gestionnaire de versions est un logiciel qui permet de gérer les différentes versions d'un projet. Il permet de suivre les modifications apportées au code, de revenir en arrière, de fusionner des branches,...

Il n'y a pas de débat sur le fait que Git est le gestionnaire de versions le plus populaire, avec une part de marché de 89.48% en 2024. Il est utilisé par la plupart des développeurs, quel que soit le langage de programmation, le projet, l'équipe, etc. Il est rapide, fiable, sécurisé, flexible, distribué, etc. Il permet de travailler en mode déconnecté, de gérer des branches, de fusionner des branches, de réécrire l'historique, etc.

Pensez donc à installer Git sur votre poste de travail, et à vous familiariser avec les commandes de base, comme `git clone`, `git add`, `git commit`, `git push`, `git pull`, `git merge`, `git rebase`, etc.

### Langages de programmation<a name="langages-de-programmation"></a>
**Définition** : Un langage de programmation est un langage formel qui permet de décrire des algorithmes et de les exécuter sur un ordinateur. Il existe des centaines de langages de programmation, chacun ayant ses avantages et ses inconvénients.

Il faut penser à installer les langages et compilateurs nécessaires pour travailler sur les projets en cours. Pas de recommandation particulière, chaque langage a ses avantages et ses inconvénients, il est donc important de choisir un langage qui correspond à ses besoins, plutôt que de suivre la tendance.


### Conteneurisation<a name="conteneurisation"></a>
**Définition** : La conteneurisation est une technique qui permet d'isoler une application et ses dépendances dans un conteneur isolé en dehors de son système d'exploitation. Cela permet de garantir que l'application fonctionne de la même manière, quel que soit l'environnement dans lequel elle est exécutée. C'est une technique très utilisée dans le développement logiciel moderne.

Les conteneurs sont devenus un outil incontournable pour les développeurs, car ils permettent de créer des environnements de développement reproductibles, portables, légers, sécurisés. Ils permettent principalement de tester des applications dans des environnements isolés, de déployer des applications dans des environnements hétérogènes, de gérer des applications à grande échelle.

L'outil de conteneurisation le plus populaire est Docker, avec une part de marché de 83.03% en 2024. Il est utilisé par la plupart des développeurs, quel que soit le langage de programmation. Il est rapide, fiable, sécurisé, flexible. Attention cependant car docker est un outil sous license propriétaire, il est donc important de bien lire les conditions d'utilisation avant de l'utiliser.\
Une alternative open-source à Docker est Podman, il est compatible avec les images Docker et permet de gérer des conteneurs de la même manière que Docker.


Tous ces outils sont essentiels pour un développeur. Il faut veiller à maintenir ces outils, ainsi que le poste à jour pour garantir la sécurité et la stabilité du poste de travail.
