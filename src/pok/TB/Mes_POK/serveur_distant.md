---
layout: layout/post.njk

title: "Serveur Distant"
authors:
  - Timothée Bermond

---
<!-- Début Résumé -->
Je vais créer un site qui permet de compter les points au Yams.
<!-- Fin Résumé -->
# Liste des thâches

- Création du front
- Suivi du cours de Mr. Brucker en MON2.1
- Création d'un compte sur evh
- Création du back avec node
- Génération de cookies
- Création BD
- Lien back et front
- Lien back et BD : routes + API

# Sprint 1
Durant le sprint 1 (25/11 - 7/12), je prévois :
- Tout d'abord de créer la partie front de mon site
- D'avoir entièrement suivi le cours dispensé en 2e année afin d'avoir les compétences pour déployer mon site sur un serveur distant.
- D'aller voir Mr. Brucker pour me créer un compte sur l'evh

Durant ce print j'ai eu le temps de créer toute ma partie front.
<img src="../../Images/yams.jpg"/>
J'ai rencontré plusieurs difficultés : je voulais notamment ajouter un input avec une liste déroulante et une zone de texte. J'ai eu du mal à trouver comment faire, la solution était toute simple : utilisé une datalist qui en plus peut-être réutilisable pour plusieurs input.
<img src="../../Images/datalist.jpg">
Une autre difficulté a été la création d'indication au survol d'une image. Je me suis pris la tête avec des *:hoover* alors qu'il suffisait d'utiliser la propriété title.
<img src="../../Images/indication.jpg">
J'ai également tenté d'implémenter une boucle for dans le fichier javascrpit afin de traiter les scores de tous les joueurs d'un seul coup ce qui m'aurait permis de créer facilement d'autres joueurs. Mais cette méthode n'a pas fonctionné et je n'ai pas eu le temps de chercher une méthode alternative.
Pour toute la partie CSS je me suis référé à mon [MON1.2](../../../../mon/TB/Mes_MON/CSS.md). Il y a juste la fonctionnalité *:before* que j'ai utilisé afin d'ajouter un fond d'écran partiellement opaque.

J'ai ensuite suivi la [formation](https://francoisbrucker.github.io/cours_informatique/enseignements/ecm/2A/option-web/) de Mr. Brucker, notamment le Projet Numérologie, afin de me former sur les serveurs web. Je n'ai pas eu le temps de tout parcourir mais je finirais ça d'ici la fin de la semaine.

Pour ce qui est du dernier point de ce sprint : la création du compte sur l'evh, je m'y suis pris un peu tard et n'ai pas eu le temps de le faire.

J'ai également pour idée d'ajouter une fonctionnalité qui permet de créer des groupes, par exemple des gens avec qui vous jouez souvent, et lorsque vous vous connecterez les noms des joueurs seront entrés automatiquement et vous aurez accès aux nombres de parties gagnées de chacun et potentiellement d'autres statistiques.

# Sprint 2

Pour le sprint 2 je prévois de :
- Créer le back avec node
- Générer les cookies
- Créer la BD
- Mettre en place le lien back et front
- Ainsi que le lien back et BD : routes + API

