---
layout: layout/post.njk

title: "Coté Web"
authors:
  - Gabriel BARBE

---
<!-- Début Résumé -->
MON sur le developpement côté serveur suivi sur le site de M. Brucker puis sur mdn developper. 
<!-- Fin Résumé -->
Il n'est pas question de paraphraser ici l'entièreté du cours, néanmoins j'incluerai un résumé sous chaque partie. <br/>
Etant complètement débutant j'ai trouvé que le cours dispensé en anglais sur [mdn.developper](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/development_environment) détaillait plus toute la démarche de création de serveur, c'est pourquoi après les deux premiers modules, j'ai continué mon apprentissage sur ce site.
## Coté serveur 
### Lire des données 
Afin de lire des données sur un site web et les réutiliser ensuite, on utilise la fonction javascript "fetch". Cette dernière est fondamentale dans l'utilisation des bases de données. La fonction fetch peut être utilisé sur des fichiers textes, des images ou du json ([voir Devweb 1](Devweb1)) à condition que ces dernières soient sur un serveur web !
### Serveur web minimal
On peut créer un "serveur minimal" grâce à node simplement avec la commande shhell : 
```bash
node index.js
```
Cette commande crée un serveur minimal en local. 
Ce serveur suit le protocole http c'est à dire une suite de requête de l'utilsateur et de réponse de la machine. 

### Création du premier projet grâce à Node/Express 
Express est un framework de node, lui-même environnement de développement, permettant de coder des sites côtés serveur. Tout l'intéret de l'apprentissage de ce MON est de basculer le site créer avec le premier POK : "Mon site chez moi" coté serveur.<br>
Le framework Express crée tout le "squelette" de notre site web et l'importe sur un serveur local. Ce serveur est localisé à http://localhost:3000/.
Nous obtenons donc notre premier site web sur serveur : <img src="../../Images/Express.png">