---
layout: layout/pok.njk

title: "CupCare - Votre Café, Votre Instant"
authors:
  - Assane Diouf

date: 2023-12-01

tags: 
  - "temps 2"

résumé: Une application mobile pour savoir quelle machine à café marche à Centrale pour passer la meilleure pause possible
---

## Introduction
Personnellement, je ne bois pas de café. L'idée m'est venu en voyant sans arrêt mes camarades courir dans l'école à la recherche d'une machine à café qui fonctionne.

L'objectif de CupCare - l'application mobile que je vais développer - est donc de faciliter cette étape de recherche de la bonne machine à café. Les fonctionnalités auxquelles j'ai pensées sont donc les suivantes :
- Voir les machines à café et leur état (en panne, en marche ou inconnue)
- Voir quels produits sont disponibles
- Rechercher où trouver un produit en particulier. *Par exemple, savoir ou il est possible de récupérer un chocolat chaud (si c'est possible)*
- Un système d'authentification simple
- Laisser la possibilité aux utilisateurs de dire si un produit est accessible (ou pas) depuis une certaine machine
- Mme Piet a aussi proposer l'idée d'ajouter des informations sur l'affluence

### Quel point de départ ?
ChatGPT a fait des suggestions pour le nom du projet, et a généré un petit texte de présentation de l'application.

```
Bienvenue sur CupCare - Votre Café, Votre Instant!
Découvrez une nouvelle façon de vivre votre rituel matinal avec CupCare, votre compagnon de confiance pour un café parfait à tout moment de la journée!

✨ Pourquoi choisir CupCare?

CupCare est bien plus qu'une simple application – c'est votre alliée matinale, toujours prête à vous guider vers le café parfait, accompagné du biscuit qui mettra un sourire sur votre visage.

🌍 Un Café, Une Aventure

Que vous soyez étudiant en quête d'inspiration ou jeune ingénieur prêt à conquérir le monde, CupCare vous assure que votre pause café soit aussi exceptionnelle que vous l'êtes. Notre application vous permet de localiser instantanément les machines à café fonctionnelles les plus proches, vous assurant ainsi de ne jamais être loin de votre pause café bien méritée.

☕ Toujours à portée de main

Avec CupCare, la recherche du café parfait devient une aventure quotidienne. Où que vous soyez, quoi que vous fassiez, votre café idéal et votre biscuit préféré ne sont qu'à quelques clics. Soyez prêt à redécouvrir le plaisir d'une pause café à chaque instant.

🎓 Pour les Étudiants, Par les Étudiants

CupCare comprend les besoins des étudiants et des jeunes ingénieurs. Nous sommes là pour simplifier votre journée bien remplie en vous offrant un accès rapide à votre carburant essentiel – le café !

Rejoignez la communauté CupCare dès aujourd'hui et transformez chaque tasse en une expérience inoubliable. Parce que chaque journée mérite un café exceptionnel.

Commencez votre journée avec CupCare! ☕✨
```

J'ai aussi fait générer un logo par Bing Image Creator. Cela m'a permis d'avoir une piste pour la charte graphique de l'application. Voici le logo en question :
![Logo généré par Bing Image Creator](./CupCare.jpg)

### Comment je vais m'y prendre ?
J'ai prévu d'utiliser Flutter et Firebase pour développer cette application. 

Flutter est un framework Dart de développement multiplateforme développé par Google. Pas de panique : j'explique la phrase. Dart est un langage développé par Google pour concurrencer javascript à l'origine - ça n'a pas fonctionné. En revanche, Google a tout de même décidé de développer Flutter en se basant dessus. Flutter est multiplateforme, car il permet de cibler plusieurs plateformes "en même temps" : mobile (Android et iOS), web et desktop (Windows, Mac et Linux).

Firebase est une plateforme de développement d'application et dispose d'outils pour accélérer le développement (base de données en NoSQL, authentification, etc...), le déploiement et le monitoring d'applications.

Il s'agit de deux technologies que j'avais déjà utilisées ensemble, ce POK me permet de réactiver mes connaissances et d'ajouter une meilleure application mobile à mon portefolio.


## Ce que je vais faire dans le premier sprint
*J'ai mis la difficulté estimée entre parenthèses pour chaque tache*
- [ ] Lister les pages essentielles (1)
- [ ] Faire le design des pages principales (2)
- [ ] Initialiser le projet (1)
- [ ] Ajouter les pages principales dans l'application (3)
- [ ] Ajouter des données factices dans Firebase (1)

## Ce que j'ai fait à la fin du sprint 1

## Ce que je vais faire dans le deuxième sprint
- [ ] Lier Firebase à Flutter
- [ ] Mettre à jour les pages avec les données
- [ ] Ajouter de vraies données
- [ ] Déployer

## Ce que j'ai fait à la fin du sprint 2

## Conclusion