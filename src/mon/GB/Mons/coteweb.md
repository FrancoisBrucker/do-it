---
layout: layout/post.njk

title: "Coté Web"
authors:
  - Gabriel BARBE

---
<!-- Début Résumé -->
MON suivi en majorité grâce au site de M. Brucker sur le développement coté serveur. Il n'est pas question de paraphraser ici l'entièreté du cours, néanmoins j'incluerai un résumé sous chaque partie. 
<!-- Fin Résumé -->

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