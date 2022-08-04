---
layout: layout/post.njk 
title: Comment installer do-it chez vous
date: 2019-05-30
tags: 
   - 'tutoriel'
   - 'installation'
---

<!-- résumé : début -->
Installation du site do-it chez vous.
<!-- résumé : fin -->

## première installation

1. installation de node :
   * sous mac : 
      1. avec <https://brew.sh/>
      2. `brew install node`. La version doit être supérieure à 12. Chez moi, la commande `node --version`donne "v18.6.0"
2. récupérer le site avec git : `git clone https://github.com/FrancoisBrucker/do-it.git`
3. allez dans le dossier *"do-it"*
3. `npm install` : pour installer les dépendances de <https://www.11ty.dev/> qui est notre générateur de site
4. `npm run build` : pour installer les dépendances front
5. test en local avec `npm run serve` :
   * il ne doit pas y avoir d'erreur
   * vous devriez voir le site en local sur <http://localhost:8080>

## pousser ses modification sur le serveur

Une fois vos modifications effectuées, **vérifiez que tout fonctionne encore !**.

Puis on pousse le tout sur le serveur :

1. `git status` : pour voir ce qui a été modifié
2. si on a ajouté des fichiers : `git add _mon_fichier_ajouté` (ou `git add --all` si on a **bien vérifié** que ça ne rajoutait pas de fichiers indésirables)
3. `git commit -am"le message de commit"` mettez un message de commit simple et informatif.
4. `git push` : pour pousser sur le serveur
