---
layout: layout/pok.njk

title: "Scraping d'une page internet pour faire de la data visualisation"
authors:
  - Ménager Jeanne

date: 1971-01-01

tags: 
  - "temps 2"
  - "Scraping"
  - "Python"
  - "BeautifulSoup"

résumé: Je vais apprendre à faire du scraping et l'utiliser pour récupérer des statistiques de football et en faire de la data visualisation
---

{% prerequis %}

Avois quelques bases en python
{% endprerequis %}
{% lien %}

[Vidéo pour apprendre le scraping](https://www.youtube.com/watch?v=sOAZpHDEdkg&t=276s) \
[Site de statistiques sportives](https://www.sofascore.com/fr/) \
[GitHub](https://github.com/jeanne-mngr/POK2)

{% endlien %}

## Sprint 1 

### Tâches
[X] Apprendre les bases du scraping \
[X] Faire quelques exercices simples pour essayer de récupérer des infos\
[X] Essayer de récupérer des informations sur sofascore

### Qu'est-ce que le scraping ? 
  Le scraping consiste à récupérer grace à un programme informatique des données sur un site internet. Cela peut notamment permettre de récupérer beaucoup de données en un temps limité. \
  Le scraping est autorisé sous certaines conditions : \
    - La quantité de données récupérées doit être raisonnable\
    - La données récupérées doit être accessible gratuitement\
    - On ne peut pas utiliser la donnée récupérer pour faire des la concurrence au site ciblé (par exemple, le bon coin avait été victime de scraping mal-intentionné de la part d'un autre site qui mettait donc en ligne exactement les mêmes annonces que le bon coin)

### Trouver des informations sur une page web : 

Dans la vidéo que j'ai visionné pour apprendre les bases du scraping, j'ai pu apprendre à utiliser **Requests** et **BeautifulSoup**. L'utilisation de ces librairies n'est pas très difficile, il faut cibler les éléments présents dans le html, que l'on peut identifier grâce aux outils de developpement présents dans la plus part des navigateur (attention pas sur safari).\
En ciclant les éléments, on peut accéder aux informations souhaitées, mais il faut faire attention à la façon dont on cible chaque information : par exemple pour récupérer UN lien, il ne faut pas cibler le premier lien trouver sur la page car même si pour l'instant il est unique, ce ne sera pas toujours le cas. 

### Getsion des erreurs
Le professeur dans la vidéo expliquait aussi comment gérer les erreurs avec des ```try ... except ...``` afin de comprendre pourquoi le script ne fonctionne plus si un jour c'est le cas.

### Les exercices
Le cours s'articulait autour d'un site web fait exprès pour s'entrainer à scrapper, [un site d'une librairie](https://books.toscrape.com/index.html). Avec les différents exemple, j'ai pu m'entrainer puis me corriger grâce à la vidéo.

### Playwright 

Enfin, nous avons appris à utiliser **playwright** pour naviguer sur un site web dans nos scripts. 
Néanmoins, j'ai essayé d'utiliser cet outil pour scrapper le site de la SNCF (ainsi que trainline) mais ces deux sites ont mis en place des tests pour verifier que l'utilisateur est humain, tests que mon script ne peut pas passer, n'étant pas humain.

Ce module me servira tout de même pour mon projet de scraping de statistiques de football pour naviguer sur certaines page. 

### Début du projet

Afin de mettre rapidement en pratique ce que j'avais appris, j'ai juste voulu récupérer l'age moyen des joueurs de l'équipe du PSG. \
Je suis donc allée sur la page dédiée à cette équipe : https://www.sofascore.com/fr/equipe/football/paris-saint-germain/1644 \
On peut voir grâce à cette url que chercher des informations pour une équipe en particulier ne sera pas très compliqué car chaque équipe a son url qui lui est propre.

## Sprint 2

- [ ] Définir les données que je souhaite utiliser
- [ ] Comprendre les principes de la datavisualisation
- [ ] Faire une première datavisualistation

### Horodatage

Toutes les séances et le nombre d'heure que l'on y a passé.

| Date | Heures passées | Indications |
| -------- | -------- |-------- |
| Samedi 02/11  | 30 min  | Début de la vidéo pour comprendre ce qu'est le scraping |
| Dimanche 03/11  | 30 min  | Instalation de requests et beautiful soup et premières requests pour récupérer le code html de pages web|
| Vendredi 08/11  | 30 min  | Premiers exemples de scraping |
| Mardi 12/11  | 30 min  | Premiers exercices de scraping pour récupérer toutes les catégories de livre |
| Vendredi 15/11  | 1 h 30 min  | Exercice pour récuperer les catégories avec moins de X livres  |
| Vendredi 15/11  | 30 min  | Correction de l'exercice pour récuperer les catégories avec moins de X livres  |
| Samedi 16/11  | 1 h  | Exercice sur récupérer les livres avec une note de 1 étoile  |
| Samedi 16/11  | 30 min  | Correction de l'exercice sur récupérer les livres avec une note de 1 étoile  |
| Samedi 16/11  | 2h  | Exercice pour récupérer la valeur de la bibliothèque + correction  |
| Dimanche 17/11  | 1h  | Découverte de playwright  |
| Lundi 18/11  | 1h  | Essai de scraper sncf connect  |
| Lundi 18/11  | 30 min  | Scrapping de sofascore pour avoir l'âge moyen des joueurs du PSG  |
