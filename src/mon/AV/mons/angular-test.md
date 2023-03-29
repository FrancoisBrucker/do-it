---
layout: layout/post.njk

title: "Les test dans Angular"
authors:
  - Antoine Varnerot

---
<head>
  <link rel="stylesheet" href="../../assets/style.css">
</head>

## Description du MON

Dans ce MON j'aimerais bien relier deux connaissances :

- la programation par les tests qu'on a vu en cours du temps 3
- Angular que j'ai pu utiliser dans des projets

Sur le site d'Angular, il y a une partie "Testing", je vais essayer de suivre le tuto qu'il fournisse :
<https://angular.io/guide/testing>

Prérequis (selon le tuto):

- Angular fundamentals
- JavaScript
- HTML
- CSS
- Angular CLI

Fonctionne avec Jasmin/Karma. <https://jasmine.github.io/>

Pour lancer les tests unitaires et d'intégration d'une application il y a juste à utiliser la commande :

```bash
ng test
```

Quand je l'utilise sur le projet 3a, on voit :

```bash
29 03 2023 15:55:08.683:WARN [karma]: No captured browser, open http://localhost:9876/
29 03 2023 15:55:08.765:INFO [karma-server]: Karma v6.4.1 server started at http://localhost:9876/
29 03 2023 15:55:08.765:INFO [launcher]: Launching browsers Chrome with concurrency unlimited
29 03 2023 15:55:08.778:INFO [launcher]: Starting browser Chrome
29 03 2023 15:55:17.648:INFO [Chrome 111.0.0.0 (Windows 10)]: Connected on socket lNB9loYvtK6OizDlAAAB with id 86176802

...
(beaucoup d erreurs)
...

Chrome 111.0.0.0 (Windows 10): Executed 29 of 29 (18 FAILED) (5.695 secs / 1.836 secs)
TOTAL: 18 FAILED, 11 SUCCESS
```

Et ca nous ouvre une fenêtre Chrome à l'adresse localhost:9876 où les erreurs sont affichées d'une facon plus lisible :

<figure>
  <img src="../../assets/tests-init.png">
  <figcaption>Résultat des tests du projet 3a</figcaption>
</figure>

Il y a 18 erreurs mais il y a quand même 11 succès ^^.
On va essayer de comprendre comment on peut résoudre ces erreurs et comment implémenter d'autres tests.

Les fichiers de tests dans Angular sont tous les fichiers qui ont l'extension ```.spec.ts```
