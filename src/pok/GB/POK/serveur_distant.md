---
layout: layout/post.njk

title: "Serveur Distant"
authors:
  - Gabriel BARBE

---
<!-- Début Résumé -->
POK visant à reproduire le site effectué dans le temps mais sur un serveur distant et en y rajoutant du back-end. 
<!-- Fin Résumé -->
# Organisation
Dans un premier temps, ajouter du back-end grâce au MON suivi sur le site de M. Brucker puis dans un second temps l'implémenter sur un serveur distant. 
TO do-list : 
Sprint 1 : 
- Ramener le site sur l'ovh 
- Gérer des cookies pour implémenter une page de connexion
<br> 
Sprint 2 :
- Insérer une base de donnée
- Gérer le backend en node
- Si le temps le permet voir un peu pour la sécurité  

### Nouveau projet Express 
Pour le développement du projet, j'ai choisi de le faire via Express car c'est ce que recommandait M. Brucker et donc dans un premier temps je crée un nouveau projet à l'adresse http://localhost:3000/. <br>
Concernant la base de données et le langage associée à utiliser, j'ai longtemps hésité mais j'ai finalement décidé de suivre l'exemple associé à Express sur <a href="http://developer.mozilla.org"/> et donc d'utiliser l'ORM Mongoose associée à une base de données MangoDB.