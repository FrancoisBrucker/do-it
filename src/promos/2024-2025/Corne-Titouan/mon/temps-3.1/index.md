---
layout: layout/mon.njk

title: "Test-Driven Developpment : les tests au coeur du développement"
authors:
  - Titouan Corne

date: 2025-01-06
tags: 
  - "temps 3"
  - "test"
  - "vert"
  - "méthodologie"
  - "Test-Driven Developpment"

résumé: "Avec ce MON, je compte étudier la méthodologie Test-Driven Developpment qui repose sur l'écriture de test en amont (généralement les tests sont implémentés après le code). Ainsi, je vais me former à l'écriture de tests. Enfin, j'aimerais me familiariser avec un outil de gestion de tests (Jenkins par exemple) et comprendre comment l'intelligence artificielle (Copilot, GPT) peut être un outil privilégié dans l'écriture de tests. Exceptionnellement, ce MON sera constitué de 15 heures de travail. "
---

{% prerequis %}

Liste des prérequis du POK ET/OU MON

{% endprerequis %}
{% lien %}

- [Site officiel](https://react.dev/)
- [GitHub : application pour tester et prendre en main les différents concepts](mettre lien ici)

{% endlien %}

## Table des matières

1. [Test-Driven Developpment : Comprendre la méthodologie](#section1)

## 1. Test-Driven Developpment : Comprendre la méthodologie <a id="section1"></a>

La méthodologie Test-Driven Developpment (tdd) consiste à concevoir un logiciel par des itérations successives courtes, telles que chacune de ses itérations correspond à un problème à résoudre formulé sous forme de test.

Un **test unitaire** est une petite portion de code écrite pour vérifier qu'une partie spécifique de votre application fonctionne comme prévu. Cela aide à identifier rapidement des erreurs ou régressions (bugs ou comportements incorrects introduits dans une fonctionnalité qui fonctionnait correctement auparavant) dans votre code.

Le tdd suit généralement un cycle en trois étapes :

1. **Red :** Ecrire un test qui échoue (car le code pour le satisfaire n'existe pas encore, puisqu'on écrit **le test en amont** du code).
2. **Green :** Ecrire le **minimum** de code nécessaire pour que le test réussisse. On ne s'occupe pas ici de l'algorithme utilisé ou de sa performance.
3. **Refactor :** Améliorer le code tout en gardant les tests au "vert", de sorte à ce que sa performance soit optimale.

{% details "Exemple illustratif simple en python" %}

- **Etape 1 : Ecrire le test (Red)**

On écrit un test qui vérifie que la fonction `add(a,b)` renvoie bien la somme de `a` et de `b`. Par exemple, add(4,3) devrait retourner 7

``` python
import unittest

class TestAddition(unittest.TestCase):
    def test_add_two_numbers(self):
        self.assertEqual(add(4, 3), 7)  # étant donné qu'on écrit le test en amont, la fonction add n'a pas encore été codée
```

Si on exécute le test à cette étape, on va obtenir une erreur qui est normale et voulue puisque la fonction `add` n'a pas été codée.

{% info %}

`unittest` est le module intégré de Python pour créer et exécuter des tests unitaires. Il fournit une infrastructure pour écrire, organiser, et exécuter des tests de manière systématique et automatisée.

{% endinfo %}

- **Etape 2 : Implémenter le code minimal (Green)**

A présent on code la fonction `add` :

``` python
def add(a,b):
  return a + b
```

A ce stade, si on exécute le test, il devrait réussir.

- **Etape 3 : Optimiser le code (Refactor)**

Dans ce cas simple, il n'y a pas vraiment de besoin de refactoriser, car la fonction est déjà concise et claire. Cependant, dans des cas plus complexes, cette étape consiste à nettoyer ou optimiser le code tout en gardant les tests au "vert".

Ensuite on peut continuer la méthodologie en entammant un nouveau cycle => nouvelle étape *red*, avec l'écriture d'un nouveau test.

{% enddetails %}

Les **erreurs récurrentes** à ne pas faire en tdd :

- Oublier d'exécuter régulièrement les tests
- Ecrire trop de tests à la fois, ou des tests trop complexes. Il est important d'avancer par petits pas.
- Ecrire des tests qui manquent d'assertions, c'est-à-dire des tests qui ne vérifient pas correctement que le code fonctionne comme souhaité. Exemple d'assertion en Python avec unittest : `self.assertEqual(add(2, 3), 5)`

Les (nombreux) **avantages** du tdd :

- Amélioration de la qualité du code : code robuste, bien structuré et moins sujet aux bugs.
- Réduction des bugs et régressions : suite de tests automatisée qui garantit que chaque modification du code est validée. Cela aide à prévenir les régressions lorsque de nouvelles fonctionnalités ou des corrections de bugs sont introduites.
- Conception guidée par les tests : cela évite le surdéveloppement ou l'écriture de code inutile, ce qui améliore la clarté et la maintenabilité.
- Conception axée sur les résultats : on se concentre sur les objectifs fonctionnels (ce que le code doit faire) au lieu de se perdre dans les détails de l'implémentation.
- Documentation vivante : les tests eux-mêmes servent de documentation technique vivante qui décrit comment chaque fonctionnalité est censée fonctionner.
- Méthodologie adapté à l'intégration continue : le tdd garantit un flux de développement fluide, avec des livraisons fréquentes et fiables. On avance continuement petit pas par petit pas

## Sources utiles

{% lien %}

- [A Practical Example using Test Driven Development. Source : Vandan Gogna, an IBM Garage expert, sur Medium (2021)](https://vandangogna.medium.com/a-practical-example-using-test-driven-development-88b4536ac574)
- [Documentation sur le JSX. Source : Meta Platforms, Inc. (2024)](https://legacy.reactjs.org/docs/introducing-jsx.html)

{% endlien %}
