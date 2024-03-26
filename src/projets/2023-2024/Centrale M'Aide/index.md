---
layout: layout/projet.njk

title: "Centrale M'Aide"
authors:
  - Beguier Benoit
  - Beyaert Alexandre
  - Lalanne William
  - Ouzoulias Nicolas
---

Création d'un site de mise en relation des élèves centraliens pour déposer et répondre à des annonces.

Dernière mise à jour : 12/03/2024

## Description du projet
### Contexte

L'année dernière, alors qu'il s'apprêtait à partir en vacances, William  n'a trouvé personne qui pouvait s'occuper de son jardin en son absence (pas chez ses voisins, pas même chez ses amis).
**Résultat :** tout son potager est mort en son absence.

Nous souhaitions dans un premier temps créer une plateforme de mise en relation de particuliers pour la garde d'animaux et la gestion de jardins pendant une absence.

### Recadrage

Après réflexion et discussion avec Adèle, notre tutrice, nous avons décidé de recadrer le projet.

Nous nous concentrons sur un **public centralien uniquement**, ce qui nous permet de développer un projet plus **précis** et **répondant à une demande que nous connaissons tous.**

Nous nous basons ainsi sur un public clairement identifié et les personae seront correctement définis.

### Présentation du projet retenu

Nous souhaitons créer une **plateforme d'entraide entre centraliens**, du type Leboncoin, permettant à tout étudiant de déposer une annonce pour tout type de service.
Il peut s'agir d'un besoin :
- ponctuel de courte durée (prêt d'outils, déménagement, vends bureau) ;
- ponctuel de plus longue durée (entretien d'un potager pendant les vacances) ; 
- ou encore d'un besoin récurrent (prêt de matériel de sport)

Chaque centralien qui le souhaite dépose son/ses annonce(s) incluant description et informations pratiques : localisation, date, besoin... 

Les autres utilisateurs peuvent alors scruter les différentes annonces, rechercher celles proches de chez eux via un accès à la carte des colocs.

Après acceptation d'une annonce, le demandeur est invité à contacter l'accepteur sur Messenger.

### Et ça existe déjà ?

Oui, mais non... 
Les plateformes existantes (Allovoisins, Yoojo, etc...) ne proposent **que de la mise en relation entre particuliers et artisans ou dépanneurs, etc...** Les sercives restent tout à fait factuels or nous souhaitons **proposer un site Internet de confiance dédié uniquement aux centraliens favorisant l'échange et les interactions sociales.** La vie des centraliens s'en verra grandement améliorée.

Il existe également un groupe Facebook "Centrale bière au Bar'bu" qui permet de demander des services de la sorte mais la **page est inadaptée aux besoins :** les annonces se perdent dans le fil d'actu, les informations pratiques sont peu visibles, beaucoup de centraliens sont manquants, la page est peu gérée...

## Objectifs du projet

### Rendu final

Nous comptons rendre, d'une part : **un Site Low-Code / No-Code**. Il sera construit à partir de :
- Airtable : un outil permettant de gérer les bases de données, dans notre cas pour gérer les annonces, les utilisateurs et les favoris,
- Bubble : un outil de no-code permettant de créer une maquette fonctionnelle de notre site Web.

Ce site Low-Code / No-Code doit être fonctionnel et esthétique. Il doit permettre de naviguer sur les différentes pages :

- dépôt d'annonce
- sélection d'annonce
- chatbot
- ajout de favoris
- création du profil utilisateur...

**Le but étant d'exploiter au maximum les possibilités fournies par l'usage du Low-Code / No-Code de sorte à proposer en peu de temps un prototype avancé du futur site web.**

D'autre part : **un Site "dur"**. Ce site sera construit "à la main" avec :

- une partie front-end, fonctionnelle pour déposer une annonce, visualiser des annonces, échanger entre utilisateurs
- une partie back-end pour gérer les fichiers et données utilisateurs.

Le site "dur" sera une version partielle du site Low-Code / No-Code : seules les principales fonctionnalités seront présentes.
L'objectif étant cette fois-ci le développement de compétences en DevWeb.

### Compétences sollicitées

**Design de l'Interface (UI)**
Construction d'un site esthétiquement qualitatif, prise en main de l'outil Figma, travail de créativité.

**Expérience Utilisateur (UX)**
Construction d'un site intuitif, facile à prendre en main.

**Low-Code**
Prise en main de fonctionnalités Low-Code / No-Code grâce aux outils Airtable et Bubble afin de créer un prototype fidèle à la version finale souhaitée
Découverte des différentes fonctionnalités/interfaces visibles sur un site internet.

**Devweb Front-End**
Apprentissage HTML, CSS, JS
Utilisation des outils de développement pour comparer les scripts d'autres sites et s'en inspirer pour développer notre site

**Devweb Back-End**
Utilisation de Python/ Javascript / node au service des bases de données

**Gestion de projet**
Division et répartition des tâches dans la création d'un site
Utilisation de l'outil Notion afin de suivre l'avancée du projet

### TimeLine Projet

La TimeLine est vouée à évoluer et sera actualisée au cours du projet.

![Image Timeline](Gantt.png)

## Fonctionnalités et pages du site
La prise en main de notre site se doit d'être facile et rapide.
L'étude **Experience 2030** (menée par Futurum Research et SAS) montre qu'un internaute décide en quelques secondes de quitter un site Internet si celui-ci n'est pas ergonomique.

Voici les pages que nous souhaitons présenter sur notre site et leurs fonctionnalités

**Voici l'utilité de chacune de ces pages :**


|                              | **Description de la page** | **Informations que l'on y retrouve** |
|:----------------------------:|:-----------:|:----------------:|
| **Connexion et inscription** | Simple page d'accueil permettant de se connecter/s'inscrire sur le site | Notre slogan, quelques menus, boutons connexion/inscription |
| **Mon profil**               | Personnalisation et actualisation du profil | Nom, Prénom, Age non modifiables. |
| **Dépôt d'annonce**          | Depôt d'une annonce | Titre, descriptif, dates, localisation, annexes supplémentaires | 
| **Recherche d'annonce**      | Liste des annonces désposées et encore d'actu | Image illustrant l'annonce, Titre, Dates |
| **Description d'annonce**    | Description précise d'une annonce | Image, titre, description, localisation, profil du déposeur |
| **Mes annonces**             | Répertoire de mes différentes annonces | Liste des annonces avec image, titre, dates |
| **Favoris**                  | Annonces gardées dans les favoris | Liste des annonces en favori avec image, titre, dates (Si le déposant modifie une annonce ajoutée aux favoris par un autre utilisateur, ce dernier sera alerté) |
| **Carte des annonces**       | Carte interactive répertoriant les annonces et leur localisation | Carte intéractive (Annonces affiliées à une zone géographique et non une adresse précise pour préserver la sécurité des utilisateurs) |

#### Déconnexion

Quand un utilisateur se déconnecte, il est redirigé vers la page d'accueil du site.

## Développement du site web

### Low-code

Profitant du cours de Low-code proposé par Adèle Bourgeix, nous avons décidé de faire une première maquette de notre site pour se pencher sur les fonctionnalités intéressantes à implémenter et avoir un apperçu de chaque page pour par la suite refaire leur design.

### Connexion et inscription
Nous avons décidé de bâtir une interface utilisateur claire avec un nombre limité de boutons. Les boutons classiques *Se connecter* et *S'inscrire* sont les seuls mis en valeurs sur la page d'accueil.

Ces deux boutons renvoient vers une page d'identification fonctionnelle, qui gère les questions d'authentification et met à jour la base de données des identifiants/mots de passe. À titre d'exemple pour la maquette en low code, seuls le nom, l'adresse mail et le mot de passe suffisent à s'inscrire. *Il est possible que ces exigences évoluent dans le futur.*

| Page d'accueil | Connexion | Inscription |
|:--------:|:--------:|:--------:|
| ![Image page d'accueil MBM](MBM-homepage.png) | ![Image connexion](MBM-connection.png) | ![Image inscription](MBM-inscription.png) |


#### Menu déroulant

Nous avons implémenté un menu déroulant sur la droite de l'écran permettant à l'utilisateur de naviguer aisément vers les pages **importantes** de notre parcours utilisateur :
- Mon Profil
- Mes Annonces
- Mes Favoris
- Carte des Annonces
- Déconnexion

#### Dépôt d'une annonce

L'annonceur remplit un formulaire simple mais précis, présentant plusieurs fonctionnalités destinées faciliter son expérience :

- la sélection d'une date se fait avec un calendrier interactif
- le dépôt d'un fichier photo permettant d'ajouter des informations : "une image vaut 1000 mots", la photographie d'un potager sera probablement plus parlante qu'un paragraphe visant à le décrire...

Pour éviter toute erreur de missclick, une confirmation sera demandée après clic du bouton *Déposer mon annonce*.

#### Recherche des annonces

Inspirée des sites d'annonces, la page de recherche n'affiche que les éléments primordiaux de chaque annonce, elle se veut d'être impactante et lisible.
La sélection d'une annonce se fait d'abord sur sa mission (titre de l'annonce) puis, si celle-ci semble intéressante, sur les critères de dates et de localisation.

Lorsqu'un utilisateur est intéressé par une annonce, il peut la consulter pour avoir plus de détails et la mettre dans ses favoris. Il peut ensuite confirmer qu'il est disponible pour débuter la conversation avec l'annonceur.

| Page d'accueil | Dépôt d'annonce | Recherche d'annonce |
|:--------:|:--------:|:--------:|
| ![Image page d'accueil MBM](MBM-homepage.png) | ![Image dépot annonce](MBM-depot-annonce.png) | ![Image recherche annonce](MBM-recherche-annonce.png) |


### Design : Maquette Figma

Les premières fonctionnalités en low-code développées, nous profitons du cours de User Interface proposé par Valery Ly pour définir notre charte graphique.

Pour commencer, nous avons testé différents sets de couleurs afin d'en retenir quelques favoris.

Ensuite, nous travaillons sur l'achitecture et le design de la page recherche d'annonces. L'objectif est alors de compléter la charte graphique en choisissant la police d'écriture, les logos utilisés, les contours des annonces, la façon dont les images et annonces doivent être exposées...

Un premier jet est alors proposé. (cf image 2 du tableau ci-dessous)

Bien que nous soyons satisfaits de la clarté de la page, de sa facilité de lecture, de la façon dont ressortent les informations, ce premier design semble encore brouillon.
Le choix des logos manque de cohérence, peu d'annonces sont visibles sur un même écran, les couleurs sont à ajuster..

Un retrevail permet d'aboutir à un design bien plus satisfaisant. (cf image 3 du tableau ci-dessous)

| Choix des couleurs | Design annonces 1er jet | Design annonces 2nd jet |
|:--------:|:--------:|:--------:|
| ![Choix des couleurs](Figma1.png) | ![Design annonces](Figma2.png) | ![Design annonces](Figma3.png) |

L'architecture de la page choisie, nous testons les différents sets de couleurs sélectionnés pour en retenir un définitif et ainsi terminer notre charte graphique. En l'occurence, nous sélectionnons la Propal 1 rappelant la charte graphique de l'école.

| Propal 1 | Propal 2 | Propal 3 |
|:--------:|:--------:|:--------:|
| ![Figma Propal Design 1](FigmaPropal1.png) | ![Figma Propal Design 2](FigmaPropal2.png) | ![Figma Propal Design 3](FigmaPropal3.png) |

### Front-end

Nous avons créé l'ensemble des pages du site en HTML et avons ajouté un fichier .css pour le header qui est identique pour l'ensemble des pages du site.
Ce fichier permet de centraliser l'information, et modifier l'apparence du header des dfférentes pages aisément.

Nous avons également défini des classes et des styles pour les fonctionnalités suivantes :

- les boutons de connexion et de déconnexion
- le menu déroulant
- les grid qui recueillent l'ensemble des annonces
- les titres, les sous-titres, le corps de texte

Voici un apperçu des différentes pages :

#### Page de connexion/inscription

| Page initiale | Connexion (mdp incorrect) | Formulaire d'inscription (email déjà utilisé) |
|:--------:|:--------:|:--------:|
| ![Page d'accueil](Connexion.png) | ![Connexion](Connexion2.png) | ![Formulaire d'inscription](Inscription.png) |

Il est intéressant de remarquer qu'une erreur dans le mot de passe à la connexion ou que l'essai d'inscription avec une adresse mail déjà utilisée renvoient des erreurs permettant aux utilisateurs de corriger leur identification.

#### Répertoire et aperçu d'une annonce

| Annonces | Aperçu d'une annonce | Mes annonces | Mes favoris |
|:--------:|:--------:|:--------:|:--------:|
| ![Annonces](menu_deroulant.png) | ![Annonce](Annonce.png) | ![Mes annonces](mes_annonces.png) | ![Mes favoris](mes_favoris.png)| 

Le menu déroulant est présent sur toutes les pages du site une fois l'utilisateur connecté. Il permet d'accéder rapidement aux pages principales.

#### Dépôt d'une annonce et aperçu du profil

| Dépôt d'une annonce | Aperçu du profil | Modification d'une annonce | Modification du profil |
|:--------:|:--------:|:--------:|:--------:|
| ![Depôt d'une annonce](Depot_annonce.png) | ![Profil](mon_profil.png) | ![Modif annonce](modif_annonce.png) | ![Modif profil](modif_mon_profil.png) |

#### Carte des annonces

| Carte des annonces | Aperçu d'une annonce sur la carte |
|:--------:|:--------:|
| ![Carte des annonces](carte_annonces.png) | ![Aperçu d'une annonce](carte_une_annonce.png) |


### Back-end

## Perspectives d'avenir du site

### Business Plan

Etant donné le public centralien, le site internet est pour le moment considéré à but non lucratif.
Cependant, dans la mesure où celui-ci prendrait place dans la vie centralienne, il pourrait servir de vitrine aux publicités de certaines associations en l'échange de financement permettant par exemple d'entretenir le site en bonne et due forme.

### Sécurité de l'utilisateur

Il s'agit d'un sujet peu abordé au cours de notre projet - partant du principe qu'au sein du public centralien, il existe une relation de confiance - toutefois, la sécurité de l'utilisateur est évidemment une problématique centrale de ce site.
Des coordonées, adresses utilisateurs sont partagées à travers ce site et il est nécessaire de protéger ces données.

Il pourrait dès lors être intéressant de se pencher sur ces questions de sécurité et confidentialité des données dans un objectif d'amélioration du projet.

#### Fonctionnalités à développer

Notre site contient les fonctionnalités jugées les plus essentielles lors de nos campagnes utilisateurs. Des améliorations futures sont envisageables :

- un système de chat entre centraliens une fois l'annonce acceptée
- un système de notation des autres utilisateurs et des services rendus, incitant à la bienveillance de la communauté
- une page de confirmation lors du dépôt d'une annonce
- un espace de retour de la part des utilisateurs pour les développeurs