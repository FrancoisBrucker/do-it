---
layout: layout/mon.njk

title: "Les test dans Angular"
authors:
  - Antoine Varnerot
tags:
  - angular
  - test
  - javascript
  - 'temps 3'

date: 2023-04-05
---
<head>
  <link rel="stylesheet" href="../assets/style.css">
</head>

## Description du MON

Dans ce MON j'aimerais bien relier deux connaissances :

- la programmation par les tests qu'on a vu en cours du temps 3
- Angular que j'ai pu utiliser dans des projets

Sur le site d'Angular, il y a une partie "Testing", je vais essayer de suivre le tuto qu'il fournisse :
<https://angular.io/guide/testing>

Prérequis (selon le tuto):

- Angular fundamentals
- JavaScript
- HTML
- CSS
- Angular CLI

Les tests sont effectués avec Jasmin/Karma. <https://jasmine.github.io/>

Pour lancer les tests unitaires et d'intégration d'une application il y a juste à utiliser la commande :

```bash
ng test
```

Si on a implémenté de l'intégration continue, on peut mettre dans le fichier package.json :

```json
"scripts": {
    "test": "ng test",
    "test:ci": "ng test --watch=false --browsers=ChromeHeadlessCI"
}
```

## Essais

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
  <img src="../assets/tests-init.png">
  <figcaption>Résultat des tests du projet 3a</figcaption>
</figure>

Les fichiers de tests dans Angular sont tous les fichiers qui ont l'extension ```.spec.ts```.

Il y a 18 erreurs mais il y a quand même 11 succès ^^.
On va essayer de comprendre comment on peut résoudre ces erreurs et comment implémenter d'autres tests.

## Réalisation

En regardant de plus près les erreurs, il y en avait beaucoup qui était très simple à résoudre. En effet, il n'y avait pas d'erreur dans le code en lui-même mais le fichier qui était exécuté pour faire le test ne disposait pas de toutes les informations. Par exemple, il n'y avait pas le module pour faire des requêtes HTTP. Je l'ai donc rajouté avant de réaliser tous les tests :

```typescript
import { HttpClientTestingModule } from '@angular/common/http/testing'; // Ligne ajoutée

beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [HttpClientTestingModule], // Ligne ajoutée
      declarations: [ PlanningDialogComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PlanningDialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });
```

Après avoir réalisé tout ces imports manquants, il me restait que 5 erreurs.

J'ai aussi rajouté l'option ```--code-coverage``` pour savoir si tout mon code était bien testé.
Résultat :
=============================== Coverage summary ===============================
Statements   : 57.04% ( 174/305 )
Branches     : 9.52% ( 2/21 )
Functions    : 48.67% ( 55/113 )
Lines        : 57.23% ( 174/304 )
================================================================================

## Ajouter des tests personnalisés

Il suffit d'utiliser les 3 fonctions suivantes pour implémenter un test :

- describe : pour définir une suite (ou groupe) de "specs".
- it : pour définir une "spec" (ou un test).
- expect : pour implémenter les assertions.

## Tests de routage

On peut maintenant réaliser des tests de routage par exemple pour vérifier que le router nous redirige au bon endroit :

```typescript
it('should navigate to home page', async () => {
  await router.navigate(['']);
  expect(location.path()).toBe('/');
});

it('should navigate to about page', async () => {
  await router.navigate(['/about']);
  expect(location.path()).toBe('/about');
});

it('should navigate to about page with navigateByUrl()', async () => {
  await router.navigateByUrl('/about');
  expect(location.path()).toBe('/about');
});
```
Et que le bon component est bien chargé (app-home ici pour la route '') :

```typescript
it('should display home component for default route', async () => {
  await router.navigate(['']);
  fixture.detectChanges();
  const home = fixture.debugElement.nativeElement.querySelector('app-home');
  expect(home).toBeTruthy();
});
```
