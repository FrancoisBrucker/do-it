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


<div style="display: flex; justify-content: center; align-items: center; height: 480;">
  <video style="max-width: 100%; height: auto;" controls>
    <source src="./videos/intro.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
</div>


### Animation et stylisation des textes

Dans un second temps, cette bibliothèque permet d'intégrer de texte et d'en personnaliser les styles et les animations :

<div style="display: flex; justify-content: center; align-items: center; height: 480;">
  <video style="max-width: 100%; height: auto;" controls>
    <source src="./videos/text_animation_base.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
</div>

Ensuite, il est possible de décomposer les mots pour animer les lettres. Voici un exemple avec le mot **Lettres** :

<div style="display: flex; justify-content: center; align-items: center; height: 480;">
  <video style="max-width: 100%; height: auto;" controls>
    <source src="./videos/animation_text_avance_compatible.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
</div>

### Animation des vidéos

Maintenant, nous pouvons animer des vidéos entre elles.

Dans la vidéo qui suit, j'ai intégrer à la vidéo du sommaire l'enregistrement d'écran du code correspondant au code qui a permis de générer la vidéo :

<div style="display: flex; justify-content: center; align-items: center; height: 480;">
  <video style="max-width: 100%; height: auto;" controls>
    <source src="./videos/double_ecran.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
</div>

Il existe énormément d'animations possibles avec cette bibliothèque, en voici quelques unes regroupées en une vidéo :

<div style="display: flex; justify-content: center; align-items: center; height: 480;">
  <video style="max-width: 100%; height: auto;" controls>
    <source src="./videos/multiple.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
</div>

### Conclusion

Pour conclure, cette démonstration représente une introduction aux capacités de MoviePy. Elle illustre une petite partie de ce que cette bibliothèque peut accomplir, notamment en matière de gestion des sons, d'animation de texte, et de manipulation avancée des vidéos.
Toutefois, l'utilisation de MoviePy pour des montages complexes n'est pas toujours optimale comparée à des logiciels spécialisés. En revanche, MoviePy peut être très utile dans l'automatisation de montages simples et dans la normalisation des processus de création. Cela en fait un outil idéal pour produire rapidement des vidéos standardisées ou répétitives tout en gagnant un temps considérable.