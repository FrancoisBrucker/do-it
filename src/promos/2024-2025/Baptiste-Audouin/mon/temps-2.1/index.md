---
layout: layout/mon.njk

title: "Automatisation de montage vidéo avec Python"
authors:
  - Baptiste Audouin

date: 2024-11-06
tags: 
  - "temps 2"
  - "Python"

résumé: Dans ce MON je souhaite découvrir comment manipuler des fichier vidéos/audio avec python notamment avec la bibliothèque python moviepy.
---

{% prerequis %}

- Bases en Python

{% endprerequis %}

{% lien %}

 - [Documentation moviepy](https://pypi.org/project/moviepy/)
 - [Mon Github](https://github.com/baptiste7905/MON.2.1)

{% endlien %}

Dans ce MON je souhaite découvrir comment manipuler des fichier vidéos/audio avec python notamment avec la bibliothèque python **moviepy**.

## Contenu

### Sommaire

Voici le sommaire de ce MON réalisé à l'aide dela bibliothèque **Moviepy** :

<source src="src/promos/2024-2025/Baptiste-Audouin/mon/temps-2.1/videos/intro.mp4" type="video/mp4">


### Animation et stylisation des textes

Dans un second temps, cette bibliothèque permet d'intégrer de texte et d'en personnaliser les styles et les animations :

<source src="src/promos/2024-2025/Baptiste-Audouin/mon/temps-2.1/videos/text_animation_base.mp4" type="video/mp4">

Ensuite, il est possible de décomposer les mots pour animer les lettres. Voici un exemple avec le mot **Lettres** :

<source src="src/promos/2024-2025/Baptiste-Audouin/mon/temps-2.1/videos/text_animation_avance.mp4" type="video/mp4">

### Animation des vidéos

Maintenant, nous pouvons animer des vidéos entre elles.

Dans la vidéo qui suit, j'ai intégrer à la vidéo du sommaire l'enregistrement d'écran du code correspondant au code qui a permis de générer la vidéo :

<source src="src/promos/2024-2025/Baptiste-Audouin/mon/temps-2.1/videos/double_ecran.mp4" type="video/mp4">

Il existe énormément d'animations possibles avec cette bibliothèque, en voici quelques unes regroupées en une vidéo :

<source src="src/promos/2024-2025/Baptiste-Audouin/mon/temps-2.1/videos/multiple.mp4" type="video/mp4">

### Conclusion

Pour conclure, cette démonstration représente une introduction aux capacités de MoviePy. Elle illustre une petite partie de ce que cette bibliothèque peut accomplir, notamment en matière de gestion des sons, d'animation de texte, et de manipulation avancée des vidéos.
Toutefois, l'utilisation de MoviePy pour des montages complexes n'est pas toujours optimale comparée à des logiciels spécialisés. En revanche, MoviePy peut être très utile dans l'automatisation de montages simples et dans la normalisation des processus de création. Cela en fait un outil idéal pour produire rapidement des vidéos standardisées ou répétitives tout en gagnant un temps considérable.