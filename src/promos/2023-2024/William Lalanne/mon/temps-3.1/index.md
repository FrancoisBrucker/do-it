---
layout: layout/mon.njk

title: "Bases du développement mobile"
authors:
  - William Lalanne

date: 2023-09-27

tags: 
  - "temps 3"

résumé: "Dans ce MON je souhaite apprendre les bases de développement mobile"
---

{%prerequis%}

Pré-requis :
**Niveau :** Facile
**Prérequis :** Pour ce MON, il est nécessaire d'avoir certaines bases de JavaScript et de React pour comprendre les concepts avec plus de facilité mais il est possible de s'en passer. 

{%endprerequis%}


## Sommaire 

1. Présentation de React Native
2. Expo
3. Les bases de React Native
4. Créer une base de données pour l'app
5. Conclusion
6. Horodatage

## 1. Présentation

React Native est un framework créé par Facebook en 2015 qui permet de créer des applications mobile pour iOS ou Android en utilisant JavaScript. Dans le monde du développement mobilen il existe deux types distincts d'application : 
- Application native : 
- Application hybride : 

Techniquement, les applications développées aevc React Native  sont hybrides mais elles utilisent des composants graphiques natifs. 

## 2. Expo 
Expo est une plateforme qui permet de faire tourner une application mobile lors du développement de cette dernière. C'est très pratique pour voir à quoi ressemble l'application. 
Voyons comment expo fonctionne. 
D'abord, pour installer Expo il faut ouvrir un terminal et entrer la commande : 
```shell
npm install expo-cli
```

Une fois Expo installée, il faut créer un projet. On se place dans le dossier dans lequel on souhaite créer l'app et on utilise la commande : 
```shell
npx create-expo-app nomDeLApp
```

Une fois l'application créée, pour la visualiser, il suffit d'ouvrir un terminal, se placer dans le dossier dans lequel on a créé l'app et utiliser la commande : 
```shell
npm start
```
Quand on fait ça, un qr code apparaît dans le terminal comme ci-dessous : 
![expo_start](start_expo.png)

En téléchargeant l'application Expo sur son téléphone et en étant connecté sur le même réseau wifi que son ordinateur, on peut scanner le qrcode et visualiser l'application directement sur son téléphone. 


## 3. Les bases de React Native



## 4.Horodatage

Mercredi 21/02 : 2h visionnage du cours de React Native sur Youtube
Vendredi 23/02 : 2h visionnage du cours de React Native sur Youtube 
Samedi 24/02 : 4h création d'une petite application 
