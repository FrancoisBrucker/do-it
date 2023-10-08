---
layout: layout/mon.njk

title: "MON 1.1 : Comprendre le Web"
authors:
  - Paul Le Bihan

date: 2023-09-27

tags: 
  - "mon"
  - "temps 1"
  - 

résumé: "Un MON traitant d'un sujet."
---



## Téléchargements de fichiers

### Récupération du fichier

#### Url

Pour télécharger le 1er tome du Comte de Monte-Cristo au format utf-8 et affichez le résultat dans stdout, avec la commande `curl`, il faut entrer dans le terminal : `curl https://www.gutenberg.org/files/17989/17989-0.txt`


#### Sauvegarde

Pour sauvegarder le contenu de l'url dans un fichier en utilisant la redirection de stdout vers un fichier, on peut taper : `curl https://www.gutenberg.org/files/17989/17989-0.txt -o LeComteDeMonte-Cristo`



### Métrologie

#### Nombres

Pour avoir le nombre de lignes, de mots et de caractères de ce fichier, en utilisant `wc`, on peut écrire : `wc -lwm LeComteDeMonte-Cristo`
