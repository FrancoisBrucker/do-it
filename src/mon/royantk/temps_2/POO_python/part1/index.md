---
layout: layout/post.njk

title: "Partie 1 - Écrivez des méthodes et des classes avec Python"
authors:
  - Killian ROYANT

tags: ['mon']
---

<!-- début résumé -->

## Partie 1 - Écrivez des méthodes et des classes avec Python

1. Tirez le maximum de ce cours
2. Comprenez la programmation orientée objet
3. Écrivez une classe Python
4. Créez et utilisez des objets Python
 Quiz : Écrire des méthodes et des classes avec Python

<!-- fin résumé -->

### 1 - Tirez le maximum de ce cours

Fait

### 2 - Comprenez la programmation orientée objet

#### Exercice 1 - Identifiez les classes

{% faire %}

- Pour chaque situation, identifiez une classe et créez un diagramme simple, en vous aidant du diagramme Client ci-dessus.
- Ensuite, identifiez toutes les variables nécessaires en fonction de la description, suivies de toutes les méthodes. N’ajoutez que les attributs qui sont mentionnés dans la description.

{% endfaire %}

{% exercice %}
J’ai une boîte à outils. Cette boîte à outils peut contenir des outils, et je peux ajouter ou enlever des outils à la boîte à outils.
{% endexercice %}
{% details "corrigé" %}

##### Boîte à outils

- État (Variables)
  - liste_outils
- Comportement (Méthode)
  - ajouter(outil)
  - retirer(outil)

{% enddetails %}

{% exercice %}
Je possède aussi des marteaux. Les marteaux peuvent être de couleurs différentes, et peuvent être utilisés pour planter et pour retirer des clous. Je peux également changer la couleur d’un marteau en le peignant.
{% endexercice %}
{% details "corrigé" %}

##### Marteau

- État (Variables)
  - couleur
- Comportement (Méthode)
  - peindre(couleur)
  - planter(clou)
  - retirer(clou)

{% enddetails %}

{% exercice %}
Enfin, je possède aussi des tournevis. Ils ont une taille (mesurée en millimètres) et peuvent être utilisés pour serrer ou desserrer une vis.
{% endexercice %}
{% details "corrigé" %}

##### Tournevis

- État (Variables)
  - taille
- Comportement (Méthode)
  - serrer(vis)
  - desserer(vis)

{% enddetails %}

### 3 - Écrivez une classe Python

Voir script.py

### 4 - Créez et utilisez des objets Python

### Quiz : Écrire des méthodes et des classes avec Python
