---
layout: layout/mon.njk

title: "MON 3.2 : Initiation à la cyber sécurité"
authors:
  - Thomas Duroy 

date: 2023-04-05

tags:
  - 'temps 3'
  - 'cyber-sécurité'
  - 'injection SQL'
---

## Motivations

Pour compléter cette année de formation en informatique et avoir un scope de connaissance assez étendu, j'ai cherché à découvrir le domaine de la cyber sécurité et j'ai découvert le site [PortSwigger Academy](https://portswigger.net/web-security/learning-path). Au cours de mon auto-formation, j'ai été impressionné par la qualité du contenu éducatif proposé sur ce site bien que quelques points négatifs restent à souligner.

## Ce que j'ai fait

Le site est organisé de manière linéaire (d'où le nom "learning path" utilisé pour décrire la formation ) et j'ai eu le temps de compléter (partiellement car présence d'exercices de niveau expert) les deux premières sections.

Tout d'abord, je me suis concentré sur les pages dédiées aux injections SQL. A travers cela j'ai pu découvrir des concepts clés dans le domaine de la sécurité web. De nombreuses variantes (injection aveugle, injection UNION) et méthodes (récupération de données sensibles, changer la logique de fonctionnement du site) étaient expliquées conceptuellement puis mises en pratique à travers des "labs" de différents niveaux (débutant/confirmé/expert).

Ensuite, je me suis attaqué à la section "Authentication" où j'ai appris à exploiter et détourner l'utilisation de token. De plus, j'ai dû apprendre à utiliser "Burp Suite" pour intercepter et examiner les requêtes HTTP afin d'établir une stratégie d'attaque (sniper, fork, brute...) en utilisant le "Repeater" et "Intruder".

## Les plus du site

Les formations proposées sur le site PortSwigger Academy sont très bien structurées, avec une progression pédagogique clairement définie. Les différents exercices sont classés par niveau de difficulté, de débutant à avancé, ce qui permet de choisir son propre rythme d'apprentissage. Les cours proposés aident à comprendre les causes, conséquences et enjeux des différentes failles de sécurité.

Ces pages contiennent des explications claires et détaillées, avec des exemples concrets pour illustrer les différents concepts. Les exercices pratiques liés à ces pages m'ont pris beaucoup de temps, mais j'ai appris une vraie démarche de hacking.

En effet, au travers des solutions proposées, on apprend une véritable méthodologie de "hacking" : sonder le site et ses réactions à diverses requêtes, deviner la structure de la base de données par tatonnement, procéder à son attaque et la corriger.

De plus, j'ai apprécié la possibilité de suivre des labs, qui permettent de s'entraîner sur des environnements sécurisés pour appliquer les techniques apprises dans les cours. Les labs proposés sont très intéressants et couvrent un large éventail de vulnérabilités et de techniques de hacking. Les solutions proposées sont détaillées et très utiles pour comprendre les erreurs commises.

## Les points négatifs

J'ai noté quelques points faibles dans l'approche pédagogique du site. Comme mentionné précédemment, j'ai utilisé Burp Suite pour compléter des labs. Cependant, je ne me suis aperçu de la nécessité de l'utiliser qu'après avoir séché devant un lab. La connaissance de Burp Suite est donc supposée, ce qui peut être un obstacle pour les débutants.

En outre, les exercices peuvent parfois sembler décourageants, surtout pour les débutants, ce qui peut ralentir la progression de l'apprenant. Il y'a parfois de véritable écart de niveau entre deux exercices de la même catégorie.

## Conclusion

Dans l'ensemble, je recommande vivement le site PortSwigger Academy pour tous ceux qui cherchent à se former dans le domaine de la sécurité web et du hacking. Les cours proposés aident à comprendre les causes, conséquences et enjeux des différentes failles de sécurité, les labs sont très intéressants pour s'entraîner et appliquer les concepts appris, et les solutions proposées sont suffisament détaillées pour s'y retrouver. Malgré quelques défauts mineurs, le site offre une excellente plateforme pour se former et progresser dans ce domaine.
