---
layout: layout/mon.njk

title: "Cryptographie"
authors:
  - ORY Victor

date: 2023-09-16

tags:
  - 'temps 1'
  - 'Cryptographie'
---
# Résumé :



## Ressources :

- [SubReddit dédié à la cryptologie ](https://www.reddit.com/r/crypto/wiki/index/)


## Pré-requis : 

{%prerequis 'Niveau débutant '%}

Pré-requis :

- Aucun

 {%endprerequis%}

## Ce qu'on fait :

- Trouver les bonnes sources 


# Letsgo :

## 1 - Trouver les bonnes sources :

Après avoir récolté les informations du subreddit **r/cryptography**, on peut voir que les utilisateurs suivants et leur compte GitHub semblent sortir du lot d'après la communauté :
- [GitHub repo 1 : pFarb](https://github.com/pFarb)
- [GitHub repo 2 : sobolevn](https://github.com/sobolevn)

## 2 - À quoi ça sert ? 

La cryptographie est un outil puissant avec des limites qui a des applications dans beaucoup de technologies de communications et plus encore. Par exemple : 
  - La signature électronique
  - Les communications sécurisées ( HTTPS )
  - Sécuriser du contenu sur un disque 
  - ... 

## Petit rappel historique : 

L'encryptage existe depuis très longtemps et peut être simple.
Une table de substitution peut être utilisée pour encrypter un message.

Tableau de substitution : 

| A | B | C | ... | Z |
|---------------|---------------|---------------|
|  K   | Y   | F  | ... | T |


Toutefois cela est sensible à des attaques par fréquence, càd, repérer la lettre qui revient le plus souvent pour en déduire les équivalences de lettres. 
Ensuite, il y a eu des améliorations de ce processus à travers le temps toutefois même "énigma" a pu être crackée. 

## La partie triste : 

Il faut faire des math pour comprendre les trucs là .... 
Par exemple il va falloir faire appel aux probabilités discrètes, aux opérateurs logiques, notamment XOR. 

## La fonction de base : 

La fonction de base est le **XOR**, elle se comporte de la manière suivante : 

| A | B | XOR(A,B) |
|---------------|---------------|---------------|
|  0  | 0  | 0 | 
|  0  | 1  | 1 | 
|  1  | 0  | 1 | 
|  1  | 1  | 0 | 

Cette fonction, appliquée à un message, $$m$$, avec une clée, $$k$$, de longueur égale à celle du message permet de l'encrypter en un message, $$c$$. 

| m | 0 | 1 | 0 | 0 | 1 |
| k | 1 | 0 | 0 | 1 | 1 |
|---------------|---------------|---------------|---------------|---------------|
| c | 1 | 1 | 0 | 1 | 0 |



Ainsi, beaucoup de systèmes sont des déclinaisons de ce procédé comme par exemple WEP(wifi), HTTPS.
Toutefois, cette technique requiert que la clé soit de longueur au moins égale à celle du message ==> C'est chiant  ! 
Par conséquent un élément essentiels de ces algorithmes est le PRG ou Pseudo Random Generator, G, qui étends la clé k' de 6 bits en 64 bits comme ceci : $$G(k') = k $$ 

## Le block Sipher :

Cette technique s'appui sur une clé, $$k$$, qui va être divisé en n, étapes pour appliquer au message, m, n encryptages successifs. 