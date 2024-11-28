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

{%prerequis '**MON débutant**'%}
- Utiliser un navigateur web
- Travail en équipe
{%endprerequis%}

{% lien '**Liens utiles**'%}
- [Stack Overflow Developer Survey 2024](https://survey.stackoverflow.co/2024)
- [POK déploiement automatisé de l'environnement de développement pour une équipe](../../pok/temps-1/)
- [MON sécurisation de l'environnement de développement](../temps-1.2/)
{% endlien %}

<script type="module">
  // Mermaid configuration
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true });
</script>
<style>
  section.optional {
    background-color: #f9f9f9;
    border-left: 4px solid #ccc;
    padding-left: 1em;
  }
  img.icon {
    width: 45px;
    height: 45px;
    border: none;
  }
  img.banner {
    width: min(45vw, 300px);
    border: none;
  }
</style>

## Table des matières<a name="table-des-matières"></a>
1. [Introduction](#introduction)
    1. [Le Développeur](#le-développeur)
2. [Outils au poste](#outils-au-poste)
    1. [Système d'exploitation](#système-dexploitation)
    2. [Navigateur](#navigateur)
    3. [IDE](#ide)
    4. [Terminal](#terminal)
    5. [Gestionnaire de versions](#gestionnaire-de-versions)
    6. [Langages de programmation](#langages-de-programmation)
    7. [Conteneuristation](#conteneurisation)
3. [Outils partagés](#partagés)
    1. [Communication](communication)
    2. [Partage de code source](#partage-de-code-source)
    3. [Gestion de projet](#gestion-de-projet)
    4. [Stockage d'artefacts](#stockage-dartefacts)
    5. [Qualimétrie Logicielle](#qualimétrie-logicielle)
4. [Conclusion](#conclusion)
5. [Lexique](#lexique)

## Introduction<a name="introduction"></a>
Dans le monde du développement logiciel, une équipe doit disposer d'un ensemble d'outils permettant assurer l'efficacité et la qualité de son travail. Ces outils sont essentiels non seulement pour **coder**, mais aussi pour **partager** et **gérer** le code, **communiquer** efficacement, **analyser** et **tester** les applications, ainsi que pour **déployer** des solutions **robustes**. Cette section vise à offrir un aperçu détaillé des outils incontournables qui facilitent chaque aspect du processus de développement.

L'objectif est de vous fournir une vue d'ensemble des outils et pratiques qui sont cruciaux pour le bon fonctionnement d'une équipe de développement, afin que vous ne soyiez pas perdu lorsque vous rejoindrez une équipe de développement.

Toutes les informations concernants les habitudes des développeurs seront tirées des résultats du sondage [Stack Overflow Developer Survey 2024](https://survey.stackoverflow.co/2024)

Pour ceux qui souhaitent avoir un aperçu concret: Une implémentation de ces outils est réalisée dans mon [POK sur le déploiement automatisé de l'environnement de développement pour une équipe](../../pok/temps-1/).

### Le Développeur<a name="le-développeur"></a>
Le développeur est une créature étrange qui passe la majeure partie de son temps à écrire du code, à résoudre des problèmes et à boire du café. Il est souvent solitaire, mais il peut aussi travailler en équipe. Il est passionné par la technologie et aime apprendre de nouvelles choses. Il est curieux, créatif et persévérant. Il est capable de passer des heures à chercher une solution à un problème, sans jamais abandonner. Il est un peu geek, un peu artiste, un peu scientifique. Il aime les défis et les puzzles. Il n'aime pas les bugs, les retards, les réunions et les gens en général. Il est un peu bizarre, mais c'est ce qui fait son charme.

C'est généralement quelqu'un qui a des habitudes et qui aime personnaliser son environnement de travail, il ne faut donc pas le brusquer en lui imposant des outils qu'il n'aime pas. Il est important de lui laisser le choix de ses outils, tout en lui fournissant des recommandations et des bonnes pratiques.

<section class="optional">

## Outils au poste<a name="outils-au-poste"></a>
<p style="background-color: #ffb1a8; border: 2px solid #ba1300; padding: 10px; border-radius: 10px">
<em>Cette section sert uniquement pour votre culture personnelle.</em><br>
Vous trouverez ici une liste de recommandations basées sur les habitudes des développeurs.<br>
Il est important de rappeler qu'<b>il vaut mieux laisser le choix des outils du poste de travail à chaque développeur</b>, en fonction de ses préférences et de ses besoins.
</p>

Un développeur a besoin d'un ensemble d'outils pour travailler efficacement. Ces outils sont installés sur le poste de travail de chaque développeur et sont essentiels pour coder, tester et déployer des applications.

Il est essentiel qu'un développeur puisse tester son code localement avant de le partager avec l'équipe. Premièrement car il est timide et n'aime pas que l'on puisse voir que ce qu'il fait ne fonctionne pas tout de suite. Pour cela, il doit disposer d'un environnement de développement complet, incluant un éditeur de texte, un terminal, un gestionnaire de versions, des langages de programmation, des outils de virtualisation et de conteneurisation.

### Système d'exploitation<a name="système-dexploitation"></a>
**Définition**: Le système d'exploitation (OS), c'est le logiciel qui permet à un ordinateur de fonctionner. Il gère les ressources matérielles de l'ordinateur, comme le processeur, la mémoire, le disque dur, etc. Ca lui qui permet de lancer des applications, de lire des fichiers, de se connecter à internet, etc.

Les résultats du [sondage OS](https://survey.stackoverflow.co/2024/technology#1-operating-system) donne la part des développeurs qui ont utilisé chaque OS de manière extensive au cours de l'année, dans le cadre professionnel:
<pre class="mermaid" style="background-color: transparent">
%%{init: {'theme': 'dark'}}%%
xychart-beta horizontal
  x-axis ["Linux", "Windows", "MacOS", "WSL"]
  y-axis "" 0 --> 65
  bar [57.3, 47.6, 31.8, 16.8]
</pre>

<div style="display: flex; flex-wrap: wrap; justify-content: center;">
  <img class="icon" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Tux.svg/1200px-Tux.svg.png" alt="Linux" title="Linux">
  <img class="icon" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Windows_icon.svg/256px-Windows_icon.svg.png" alt="Windows" title="Windows">
  <img class="icon" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/MacOS_logo_%282017%29.svg/512px-MacOS_logo_%282017%29.svg.png" alt="MacOS" title="MacOS">
</div>

En règle générale, les développeurs préfèrent utiliser tout ce qui n'est pas Windows, car c'est plus stable, plus rapide, plus sécurisé. Un autre avantage est que ces systèmes d'exploitation sont hautement personnalisables, ce qui permet de les adapter à ses besoins.\
Le départage entre MacOS et Linux se fait en fonction des préférences personnelles de chacun, et surtout en fonction des préférences pécuniaires de l'entreprise, car fournir une flotte de Macs à tous les développeurs coûte beaucoup plus cher que de fournir des PC sous Linux.

### Navigateur<a name="navigateur"></a>
**Définition**: Un navigateur web est un logiciel qui permet de consulter des sites web. Il permet de lire du texte, de regarder des images, de regarder des vidéos, de remplir des formulaires, etc.

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

<div style="display: flex; flex-wrap: wrap; justify-content: center;">
  <img class="icon" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Google_Chrome_icon_%28September_2014%29.svg/1024px-Google_Chrome_icon_%28September_2014%29.svg.png" alt="Google Chrome" title="Google Chrome">
  <img class="icon" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Microsoft_Edge_logo_%282019%29.png/600px-Microsoft_Edge_logo_%282019%29.png" alt="Microsoft Edge" title="Microsoft Edge">
  <img class="icon" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Firefox_logo%2C_2019.svg/800px-Firefox_logo%2C_2019.svg.png" alt="Mozilla Firefox" title="Mozilla Firefox">
  <img class="icon" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Safari_browser_logo.svg/1024px-Safari_browser_logo.svg.png" alt="Safari" title="Safari">
</div>

Sur chacun de ces navigateurs, il est possible d'installer des extensions qui permettent d'ajouter des fonctionnalités supplémentaires. Certaines des extensions  populaires sont:
- [uBlock Origin](https://ublockorigin.com/): Bloqueur de publicités
- [Bitwarden](https://bitwarden.com/): Gestionnaire de mots de passe sécurisé
- [Dark Reader](https://darkreader.org/): Mode sombre pour les sites web
- [Grammarly](https://www.grammarly.com/): Correcteur orthographique et grammatical

Il est aussi possible (au niveau de l'entreprise ou du développeur) d'appliquer un profil de sécurité pour limiter les risques de sécurité liés à la navigation web. Tous les navigateurs modernes proposent des fonctionnalités de sécurité avancées, comme la protection contre le pistage, le blocage des publicités, le blocage des scripts malveillants, etc.

Il n'y a donc pas de navigateur idéal, chacun a ses avantages et ses inconvénients. Il est donc important de choisir un navigateur qui correspond à ses préférences, plutôt que de suivre la tendance.

### IDE<a name="ide"></a>
**Définition**: Un IDE (Integrated Development Environment) est un logiciel qui regroupe un ensemble d'outils pour faciliter le développement logiciel. Il permet d'écrire du code, de le compiler, de le déboguer, de le tester, etc.

Les résultats du [sondage IDE](https://survey.stackoverflow.co/2024/technology#1-integrated-development-environment) montre que les développeurs ont utilisé au moins une fois dans l'année, dans le cadre professionnel:
<pre class="mermaid" style="background-color: transparent">
%%{init: {'theme': 'forest'}}%%
xychart-beta horizontal
  x-axis ["Visual Studio Code", "Visual Studio", "IntelliJ IDEA", "Notepad++", "Vim", "Android Studio", "PyCharm", "Jupyter Notebook/JupyterLab", "Neovim", "Sublime Text", "Eclipse"]
  y-axis "" 0 --> 80
  bar [73.6, 29.3, 26.8, 23.9, 21.6, 16.1, 15.1, 12.8, 12.5, 10.9, 9.4]
</pre>

<div style="display: flex; flex-wrap: wrap; justify-content: center;">
  <img alt="Visual Studio Code" class="icon" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Visual_Studio_Code_1.35_icon.svg/langfr-1024px-Visual_Studio_Code_1.35_icon.svg.png" title="Visual Studio Code">
  <img alt="Visual Studio" class="icon" src="https://upload.wikimedia.org/wikipedia/commons/2/2c/Visual_Studio_Icon_2022.svg" title="Visual Studio">
  <img alt="IntelliJ IDEA" class="icon" src="https://upload.wikimedia.org/wikipedia/commons/9/9c/IntelliJ_IDEA_Icon.svg" title="IntelliJ IDEA">
  <img alt="Eclipse" class="icon" src="https://cdn.worldvectorlogo.com/logos/eclipse-11.svg" title="Eclipse">
  <img alt="Notepad++" class="icon" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Notepad%2B%2B_Logo.svg/langfr-120px-Notepad%2B%2B_Logo.svg.png" title="Notepad++">
  <img alt="Vim" class="icon" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Vimlogo.svg/langfr-150px-Vimlogo.svg.png" title="Vim">
  <img alt="Android Studio" class="icon" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Android_Studio_Logo_%282023%29.svg/langfr-120px-Android_Studio_Logo_%282023%29.svg.png" title="Android Studio">
</div>
Jusqu'à récemment, les 3 IDE les plus populaires étaient Visual Studio Code, IntelliJ IDEA et Eclipse. Mais depuis quelques années, Visual Studio Code a pris une longueur d'avance sur ses concurrents, grâce à sa simplicité, sa légèreté, sa rapidité et sa richesse en extensions, le fait qu'il soit gratuit. Il permet notamment l'intégration d'IA pour la complétion de code, le refactoring, le débogage.
Il est devenu l'IDE de référence pour de nombreux développeurs, quel que soit le langage de programmation utilisé.

D'un autre côté, Eclipse est en perte de vitesse, car il est perçu comme étant trop lourd, trop complexe, trop lent et trop peu personnalisable. Il est encore utilisé dans certaines entreprises, notamment celles qui développent en Java, mais il est en train d'être remplacé par IntelliJ IDEA.

Les outils de JetBrains (IntelliJ IDEA, PyCharm, WebStorm, etc.) sont toujours très populaires, aussi riche en extensions, très performants (sans IA) sur la complétion de code, le refactoring, le débogage, etc. Ils permettent aussi l'intégration d'IA par dessus les fonctionnalités déjà existantes. Mais ils sont payants, ce qui peut être un frein pour certaines entreprises. Ils sont souvent utilisés par les développeurs qui travaillent sur des projets complexes, qui nécessitent des fonctionnalités avancées.

Il n'est pas rare de voir des développeurs utiliser plusieurs IDE en même temps, en fonction du langage de programmation, du projet, de l'équipe, etc. Il est donc important de choisir un IDE qui correspond à ses besoins, plutôt que de suivre la tendance.

### Terminal<a name="terminal"></a>
**Définition**: Un terminal est un logiciel qui permet d'interagir avec le système d'exploitation en ligne de commande. Il permet de lancer des programmes, de manipuler des fichiers, de gérer des processus, etc.

Chaque poste de travail est livré avec un terminal par défaut, mais il est possible d'installer des terminaux plus avancés, comme [Hyper](https://hyper.is/), [iTerm2](https://iterm2.com/), [Windows Terminal](https://aka.ms/terminal), etc. Ces terminaux offrent des fonctionnalités supplémentaires, comme la coloration syntaxique, la complétion automatique, la gestion des onglets, etc.

Il existe des outils permettant d'améliorer l'expérience du développeur sur le terminal, permettant de le personnaliser à la fois visuellement et fonctionnellement.
- [Oh My Zsh](https://ohmyz.sh/): Framework de configuration pour Zsh (ne fonctionne pas sur Windows)
- [Starship](https://starship.rs/): Prompt minimaliste, rapide et hautement personnalisable (fonctionne sur tous les systèmes d'exploitation)

### Gestionnaire de versions<a name="gestionnaire-de-versions"></a>
**Définition**: Un gestionnaire de versions est un logiciel qui permet de gérer les différentes versions d'un projet. Il permet de suivre les modifications apportées au code, de revenir en arrière, de fusionner des branches,...

Il n'y a pas de débat sur le fait que Git est le gestionnaire de versions le plus populaire, avec une part de marché de 89.48% en 2024. Il est utilisé par la plupart des développeurs, quel que soit le langage de programmation, le projet, l'équipe, etc. Il est rapide, fiable, sécurisé, flexible, distribué, etc. Il permet de travailler en mode déconnecté, de gérer des branches, de fusionner des branches, de réécrire l'historique, etc.

Pensez donc à installer Git sur votre poste de travail, et à vous familiariser avec les commandes de base, comme `git clone`, `git add`, `git commit`, `git push`, `git pull`, `git merge`, `git rebase`, etc.

### Langages de programmation<a name="langages-de-programmation"></a>
**Définition**: Un langage de programmation est un langage formel qui permet de décrire des algorithmes et de les exécuter sur un ordinateur. Il existe des centaines de langages de programmation, chacun ayant ses avantages et ses inconvénients.

Il faut penser à installer les langages et compilateurs nécessaires pour travailler sur les projets en cours. Pas de recommandation particulière, chaque langage a ses avantages et ses inconvénients, il est donc important de choisir un langage qui correspond à ses besoins, plutôt que de suivre la tendance.

<div style="display: flex; flex-wrap: wrap; justify-content: center;">
  <img class="icon" src="https://cdn.iconscout.com/icon/free/png-256/free-java-59-1174952.png?f=webp" alt="Java" title="Java">
  <img class="icon" src="https://upload.wikimedia.org/wikipedia/commons/1/18/ISO_C%2B%2B_Logo.svg" alt="C++" title="C++">
  <img class="icon" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/2048px-Unofficial_JavaScript_logo_2.svg.png" alt="JavaScript" title="JavaScript">
  <img class="icon" src="https://raw.githubusercontent.com/docker-library/docs/01c12653951b2fe592c1f93a13b4e289ada0e3a1/python/logo.png" alt="Python" title="Python">
  <img class="icon" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Go_Logo_Aqua.svg/1920px-Go_Logo_Aqua.svg.png" alt="Go" title="Go">
  <img class="icon" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Rust_programming_language_black_logo.svg/480px-Rust_programming_language_black_logo.svg.png" alt="Rust" title="Rust">
  <img class="icon" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/PHP-logo.svg/711px-PHP-logo.svg.png" alt="PHP" title="PHP">
</div>

### Conteneurisation<a name="conteneurisation"></a>
**Définition**: La conteneurisation est une technique qui permet d'isoler une application et ses dépendances dans un conteneur isolé en dehors de son système d'exploitation. Cela permet de garantir que l'application fonctionne de la même manière, quel que soit l'environnement dans lequel elle est exécutée. C'est une technique très utilisée dans le développement logiciel moderne.

Les conteneurs sont devenus un outil incontournable pour les développeurs, car ils permettent de créer des environnements de développement reproductibles, portables, légers, sécurisés. Ils permettent principalement de tester des applications dans des environnements isolés, de déployer des applications dans des environnements hétérogènes, de gérer des applications à grande échelle.

Le [Sondage sur les outils](https://survey.stackoverflow.co/2024/technology#1-other-tools) montre que 58.7% des développeurs professionnels ont utilisé au moins une fois dans l'année, dans le cadre professionnel, un outil de conteneurisation.

#### Les outils

<div style="display: flex; flex-wrap: wrap; justify-content: center;">
  <img class="banner" src="https://upload.wikimedia.org/wikipedia/commons/7/70/Docker_logo.png" alt="Docker" title="Docker">
  <img class="banner" src="https://upload.wikimedia.org/wikipedia/commons/9/9a/Podman-logo-orig.png" alt="Podman" title="Podman">
</div>

#### Docker
L'outil de conteneurisation le plus populaire est Docker, avec une part de marché de 83.03% en 2024. Il est utilisé par la plupart des développeurs, quel que soit le langage de programmation. Il est rapide, fiable, sécurisé, flexible. Attention cependant car docker est un outil sous license propriétaire, il est donc important de bien lire les conditions d'utilisation avant de l'utiliser.

#### Podman
Une alternative open-source à Docker est Podman, il est compatible avec les images Docker et permet de gérer des conteneurs de la même manière que Docker.


Tous ces outils sont essentiels pour un développeur. Il faut veiller à maintenir ces outils, ainsi que le poste à jour pour garantir la sécurité et la stabilité du poste de travail.
</section>

## Outils partagés<a name="partagés"></a>
Les outils partagés sont des outils qui permettent à une équipe de travailler ensemble, de partager des informations, de collaborer sur des projets, de communiquer efficacement, de gérer des tâches, de suivre des projets, de déployer des applications et de surveiller leur bon fonctionnement.

Le [Sondage sur les outils de suivi des travaux & documentation](https://survey.stackoverflow.co/2024/technology#1-asynchronous-tools) donne les résultats suivants parmis les développeurs professionnels:

<pre class="mermaid" style="background-color: transparent">
%%{init: {'theme': 'forest'}}%%
xychart-beta horizontal
  x-axis ["Jira", "Confluence", "Markdown file", "Trello", "Azure Devops", "Notion", "GitHub Discussions", "Miro", "Obsidian"]
  y-axis "" 0 --> 65
  bar [57.5, 35.3, 27.7, 18.9, 18.3, 18.1, 16.2, 14.9, 11.8]
</pre>

Ces résultats seront détaillés dans les sections suivantes.

### Communication<a name="communication"></a>
La communication est un élément clé pour le bon fonctionnement d'une équipe.\
Au sein d'une équipe de développement, les développeurs ont besoin de pouvoir communiquer de manière fluide et efficace, que ce soit pour partager des informations, poser des questions, résoudre des problèmes, prendre des décisions. Il existe de nombreux outils de communication qui permettent de faciliter la collaboration au sein d'une équipe.\
Les résultats du [sondage sur les outils de communication](https://survey.stackoverflow.co/2024/technology#1-synchronous-tools) met en lumière une diversité d'outils utilisés par les développeurs professionnels:

<pre class="mermaid" style="background-color: transparent">
%%{init: {'theme': 'default'}}%%
xychart-beta horizontal
  x-axis ["Microsoft Teams", "Slack", "Zoom", "Google Meet", "Discord", "WhatsApp", "Telegram", "Skype",  "Google Chat", "Signal"]
  y-axis "" 0 --> 60
  bar [56.2, 49.1, 39.8, 39.1, 33.6, 28.8, 19.4, 12.5, 11.1, 11]
</pre>

Ces outils permettent de communiquer de différentes manières, que ce soit par chat, par appel vidéo, par email, par téléphone, etc. Il est important de choisir un outil de communication qui correspond aux besoins de l'équipe. De plus il faut s'assurer que les outils de communication utilisés sont **sécurisés**, **fiables**, **faciles à prendre en main** pour les nouveaux arrivants, **simples** à utiliser, **compatibles** avec les autres outils de l'équipe. Ils ne doivent pas être intrusifs, ne pas être trop bruyants, ne pas être trop lents, ne pas être trop lourds.

#### Outils propriétaires
Parmis les outils de communication, on remarque une domination dans le monde professionnel par les logiciels propriétaires (Microsoft Teams, Slack, Zoom, Google Meet & Chat, Skype, Discord, WhatsApp). Ils sont souvent choisis pour leur simplicité d'utilisation, leur compatibilité (pour intégration) avec les autres outils de l'entreprise, leur support technique, leur sécurité, leur fiabilité, leur performance, leur évolutivité, leur mise à jour régulières.

<div style="display: flex; flex-wrap: wrap; justify-content: center;">
  <img class="icon" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Microsoft_Office_Teams_%282018%E2%80%93present%29.svg/langfr-110px-Microsoft_Office_Teams_%282018%E2%80%93present%29.svg.png" alt="Microsoft Teams" title="Microsoft Teams">
  <img class="icon" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Slack_Icon.png/1024px-Slack_Icon.png" alt="Slack" title="Slack">
  <img class="icon" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Zoom_Logo_2022.svg/langfr-1920px-Zoom_Logo_2022.svg.png" alt="Zoom" title="Zoom">
  <img class="icon" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Google_Meet_icon_%282020%29.svg/292px-Google_Meet_icon_%282020%29.svg.png" alt="Google Meet" title="Google Meet">
  <img class="icon" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/WhatsApp.svg/1024px-WhatsApp.svg.png" alt="WhatsApp" title="WhatsApp">
  <img class="icon" src="https://cdn.prod.website-files.com/6257adef93867e50d84d30e2/636e0a69f118df70ad7828d4_icon_clyde_blurple_RGB.svg" alt="Discord" title="Discord">
  <img class="icon" src="https://secure.skypeassets.com/content/dam/scom/legal/brand-guidelines/skype-icon.svg" alt="Skype" title="Skype">
</div>

#### Outils open source
Il existe des alternatives open source à ces outils, qui sont souvent plus **respectueuses de la vie privée** et de la **sécurité des données**. Ces alternatives offrent souvent les mêmes fonctionnalités avec parfois une moins bonne intégration avec les autres outils de l'entreprise, un support technique moins réactif et des mises à jour moins fréquentes. Il faut donc peser le pour et le contre avant de choisir un outil de communication.

<div style="display: flex; flex-wrap: wrap; justify-content: center;">
  <img class="icon" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Telegram_2019_Logo.svg/1024px-Telegram_2019_Logo.svg.png" alt="Telegram" title="Telegram">
  <img class="icon" src="https://signal.org/brand/assets/logo_min_size.png" alt="Signal" title="Signal">
  <img class="icon" src="https://mattermost.com/wp-content/uploads/2024/06/mattermost-logomark.svg" alt="Mattermost" title="Mattermost">
  <img class="icon" alt="Mumble" title="Mumble" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Icons_mumble.svg/langfr-1024px-Icons_mumble.svg.png">
</div>

### Partage de code source<a name="partage-de-code-source"></a>
**Définition**: Le partage de code source, c'est partager sur une plateforme centralisée le code source d'un projet, pour permettre à l'équipe de travailler ensemble, de suivre les modifications apportées au code, de revenir en arrière, de fusionner des branches, de gérer des conflits, et toute autre tâche liée à la gestion des versions.\
C'est l'élément central du travail d'une équipe de développement.

Les fonctionnalités attendues d'une plateforme de partage de code source sont:
- Hébergement du code source
- Gestion de toutes les tâches associées à git (versions, branches, commits, tags, releases, merges,...)
- Gestion des issues (tâches à réaliser, bugs à corriger, améliorations à apporter,...)
- CI/CD: Intégration continue et déploiement continu (automatisation des tests, des builds, des déploiements,...)
- Wiki: Documentation du projet
- Contrôle d'accès
- Self-hosting (OPTIONNEL): Possibilité d'héberger la plateforme sur ses propres serveurs

<div style="display: flex; flex-wrap: wrap; justify-content: center;">
  <img class="icon" src="https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png" alt="GitHub" title="GitHub">
  <img class="icon" src="https://images.ctfassets.net/xz1dnu24egyd/1IRkfXmxo8VP2RAE5jiS1Q/ea2086675d87911b0ce2d34c354b3711/gitlab-logo-500.png" alt="GitLab" title="GitLab">
  <img class="icon" src="https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/44_Bitbucket_logo_logos-512.png" alt="Bitbucket" title="Bitbucket">
  <img class="icon" src="https://www.svgrepo.com/show/448271/azure-devops.svg" alt="Azure Devops" title="Azure Devops">
  <img class="icon" src="https://seeklogo.com/images/S/sourceforge-logo-0372412E49-seeklogo.com.png" alt="SourceForge" title="Sourceforge">
</div>

### Gestion de projet<a name="gestion-de-projet"></a>
**Définition**: La gestion de projet, c'est l'ensemble des activités qui permettent de planifier, d'organiser, de suivre, de contrôler et de clôturer un projet.\
C'est un élément essentiel pour garantir le bon déroulement d'un projet, pour respecter les délais, les coûts, la qualité, les risques, les parties prenantes, les objectifs, les contraintes, les ressources, les livrables, les dépendances, les priorités, les changements, les problèmes, les conflits, les décisions, les actions, les réunions, les rapports, les documents, les outils, les méthodes, les normes, les bonnes pratiques, les leçons apprises, les succès, les échecs, les améliorations, les innovations, les évolutions, les révolutions.

La plupart des plateformes de partage de code source offrent des fonctionnalités plus ou moins avancées de gestion de projet. Cependant elles peuvent être *difficiles à prendre en main pour le reste de l'équipe* qui n'est pas développeur, elles peuvent aussi *manquer de fonctionnalités avancées* de gestion de projet.\
En fonction de la composition de l'équipe et des besoins du projet, il peut être intéressant de choisir un outil de gestion de projet dédié, qui offre des fonctionnalités plus avancées, plus intuitives, plus adaptées à la gestion de projet.

<div style="display: flex; flex-wrap: wrap; justify-content: center;">
  <img class="icon" src="https://cdn-icons-png.flaticon.com/512/5968/5968875.png" alt="Jira" title="Jira">
  <img class="icon" src="https://cdn-icons-png.flaticon.com/512/5968/5968793.png" alt="Confluence" title="Confluence">
  <img class="icon" src="https://cdn-icons-png.flaticon.com/256/174/174874.png" alt="Trello" title="Trello">
</div>

### Stockage d'artefacts<a name="stockage-dartefacts"></a>
**Définition**: Le stockage d'artefacts, c'est stocker sur une plateforme centralisée les artefacts d'un projet, pour permettre à l'équipe de délivrer du contenu utilisable marquant l'avancement du projet.

Les artefacts peuvent être:
- Des binaires (exécutables, jar, war, dll,...)
- Des images (pour des conteneurs)
- Des fichiers (configurations, scripts, modèles, données, images, vidéos,...)
- Des documents (spécifications, manuels, guides, tutoriels, articles, présentations, rapports,...)

Les fonctionnalités attendues d'une plateforme de stockage d'artefacts sont:
- Hébergement des artefacts
- Contrôle d'accès
- Versionning
- Scan antivirus (OPTIONNEL)
- Chiffrement (OPTIONNEL)
- Self-hosting (OPTIONNEL)

<div style="display: flex; flex-wrap: wrap; justify-content: center;">
  <img class="icon" src="https://cdn.prod.website-files.com/5f10ed4c0ebf7221fb5661a5/5f2af61146c55b6e172fa5b3_NexusRepo_Icon.png" alt="Nexus Repository" title="Nexus Repository">
  <img class="icon" src="https://min.io/resources/img/logo/MINIO_Bird.png" alt="MinIO" title="MinIO">
  <img class="icon" src="https://goharbor.io/img/logos/harbor-icon-color.png" alt="Harbor" title="Harbor">
  <img class="icon" src="https://user-images.githubusercontent.com/19695083/73797283-9f75c100-477d-11ea-8ad2-ad9da73aa83d.png" alt="Artifactory" title="Artifactory">
  <img class="icon" alt="GitHub Packages" src="https://github.githubassets.com/assets/icon-integration-d8116306cd00.png" style="background-color: #000" title="GitHub Packages">
  <img class="icon" alt="Quay" src="https://avatars.githubusercontent.com/u/38353654?s=280&v=4" title="Quay">
</div>

### Qualimétrie Logicielle<a name="qualimétrie-logicielle"></a>
**Définition**: La qualimétrie logicielle, c'est l'ensemble des activités qui permettent d'analyser la qualité d'un logiciel, de détecter les défauts, les erreurs, les bugs, les vulnérabilités, les failles, les incohérences, les incompatibilités, les inefficacités. Cela repose sur 2 piliers:
- **L'analyse statique**: Analyse du code source sans l'exécuter (lint)
- **L'analyse dynamique**: Analyse du code source en l'exécutant (test)

Lorsque le travail est bien fait, ces outils sont directement intégrés tout au long du processus de développement, dans ce qu'on appelle des pipelines CI/CD (Continuous Integration/Continuous Deployment). Ainsi chaque modification du code est automatiquement analysée et testée, puis validée. Cela permet de détecter les erreurs le plus tôt possible, de les corriger rapidement, de garantir la qualité du code, de réduire les risques, de gagner du temps, de gagner de l'argent, de gagner en confiance, de gagner en compétitivité.

Les fonctionnalités attendues d'une plateforme de qualimétrie logicielle sont:
- Analyse statique
- Analyse dynamique
- Calcul de métriques de qualité
- Génération de rapports de qualité, contenant des recommandations pour améliorer la qualité du code
- Intégration avec les outils de partage de code source
- Intégration avec les outils de gestion de projet (OPTIONNEL)
- Self-hosting (OPTIONNEL)

<div style="display: flex; flex-wrap: wrap; justify-content: center;">
  <img class="icon" src="https://seeklogo.com/images/S/sonarqube-logo-AF25541AAF-seeklogo.com.png" alt="SonarQube" title="SonarQube">
  <img class="icon" src="https://cdn.icon-icons.com/icons2/2699/PNG/512/codeclimate_logo_icon_168368.png" alt="CodeClimate" title="CodeClimate">
  <img class="icon" src="https://seeklogo.com/images/C/codacy-logo-1A40ABD314-seeklogo.com.png" alt="Codacy" title="Codacy">
  <img class="icon" src="https://0701.static.prezi.com/preview/v2/mwt4bgg45itta6meht7byw7qzh6jc3sachvcdoaizecfr3dnitcq_3_0.png" alt="SQuORE" title="SQuORE">
</div>

## Conclusion<a name="conclusion"></a>
Il existe une quantité impressionnante d'outils pour les développeurs. Chaque outil répond à des problématiques spécifiques et s'intègre plus ou moins gracieusement dans un écosystème déjà existant.

La technologie choisie n'est jamais une fin en soi, mais un moyen de répondre à un besoin. Il ne faut jamais s'enfermer dans un outil, mais être prêt à changer si un outil plus adapté se présente.

Il faut savoir choisir les outils qui correspondent le mieux aux besoins de son équipe en s'adaptant aux contraintes de budget et de fonctionnalités. Il est important de ne pas se laisser influencer par les tendances, mais de choisir des outils qui sont adaptés à ses besoins.

## Lexique<a name="lexique"></a>
- **IDE**: Integrated Development Environment
- **CI/CD**: Continuous Integration/Continuous Deployment, c'est une pratique de développement logiciel qui consiste à automatiser les tests et le déploiement d'une application à chaque modification du code source.
- **self-hosting**: Hébergement par soi-même, c'est-à-dire installer et gérer soi-même l'outil sur ses propres serveurs.
- **lint**: Analyse statique du code source pour détecter les erreurs, les incohérences, les incompatibilités, les inefficacités.
- **pipeline**: Ensemble de tâches automatisées qui permettent de construire, tester, déployer une application.
