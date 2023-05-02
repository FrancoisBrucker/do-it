---
layout: layout/pok.njk

title: "POK 2: Mon site chez moi"
authors:
  - Thomas Duroy 

date: 2023-01-04

tags:
  - 'temps 2'
  - 'Front'
  - 'Back'
---

### But : Coder un site en local

Pour ce projet, je compte illustrer la dualité de mon parcours en développant un site, focalisé sur du front-end, répertoriant mes projets Data/IA et Dev sur leurs propres pages comme une sorte de mini [github](https://github.com/ThomasDGH/POK_2/).

## Plan du POK

1. Établir l'architecture du site

2. Styliser les différentes pages

3. Trouver une idée de service faisable par une API back-end

4. Mettre en place une API back-end grâce à mon MON 2.2

5. Connecter l'API à une base de données

## Sprint 1

### Compétences/Objectifs à atteindre

- Établir la structure du site web [x]

- Revoir/approfondir base de html/js/css avec mon premier MON [~]

- Faire un repérage des différents éléments que je désire implémenter (ex: un carrousel) [x]

- Établir les connexions entre les différentes pages (vides pour le moment) [x]

- Coder la page d'accueil [~]

- Entamer le développement des pages "Dev" et "Data" [ ]

### Difficultés rencontrées

- Démarrage lent/peu d'aise dans le développement du site au départ

- Maîtrise des différents paramètres de CSS difficile

### Analyse des écarts

- Peu temps entre le début du temps 2 et le premier point POK pour à la fois fonder des bases solides en HTML/CSS/JS et se consacrer au POK.

### To-Do pour sprint 2

- Finaliser la page d'accueil

- Coder les pages "Dev" et "Data"

- Lisser le style css

- Faire un repérage des améliorations (back-end notamment)

## Sprint 2

### Compétences/Objectifs à atteindre

- Finaliser l'ensemble du front-end [x]

- Ajouter une page requête [x]

- Connecter front et back end [x]

- API totalement opérationnelle [~]

- Connexion à une base de donnée [~]

### Difficultés rencontrées

- Le carrousel que j'ai présenté dans mon MON 2.1 n'était pas pratique à manipuler et j'ai dû me rabattre sur une solution similaire proposée par [le Designer du Web](https://www.youtube.com/watch?v=14xcmpCvG7Q&t=129s&ab_channel=LeDesignerduWeb-%C3%89coleduWeb) car, pensant avoir ce qu'il fallait, c'était un des derniers éléments que je voulais implémenter avant de passer au back-end.

- Au moment de lier front et back end, je me suis aperçu que je n'avais aucune idée comment faire. Des recherches ont palier à ce problème mais d'autres sont apparus, comme des soucis de CORS (cross-origin resource sharing).

### Analyse des écarts

- Même si mon API RESTful est fonctionnelle, je n'utilise pas les méthodes autres que GET et POST pour afficher des propositions de projets.

- Avec mon MON 2.2, j'ai suivi un tutoriel pour mettre en place un middleware connecté à une base de donnée. Cependant, pour mon POK, la base de donnée n'était pas prioritaire et j'ai manqué d'un peu de temps, d'où son absence pour le moment.

### Ajustements

- Pour palier à un problème CORS rencontré, j'ai dû utiliser le module "CORS". Cependant, je sais que les autorisations doivent être le plus restrictives et je ne sais pas trop ce que fait le module.

- Complexifier le service du site pour pouvoir utiliser l'API dans tout sa capacité.

- Connecter une base de données à mon API pour avoir des propositions de projets persistantes.

## Rendu final

Le site présente une page d'accueil composée d'une partie Data/IA, d'une partie Dev et d'un bouton de requête.

![Image accueil](aperçu%20POK%201.png)

En cliquant sur l'une ou l'autre des moitiés Data/Dev, on accède à un carrousel des projets correspondants.
![Image Carrousel](aperçu%20POK%203.png)

En cliquant sur le bouton de proposition, on accède à un  formulaire et mon API back-end s'occupe de trier et d'afficher le propositions de projets.

![Image formulaire](aperçu%20POK%202.png)

## Bilan

Je suis content du site et de ce que j'ai pu produire pendant ces 20h de projet. Même si le design laisse à désirer, je suis satisfait du rendu général. De plus, le service, bien que minime, convient aux attentes que j'en avais.

J'ai maintenant plus d'aisance en HTML/CSS/JS et je pense que pour obtenir un site propre et complet, il ne manque plus qu'un peu de pratique.
