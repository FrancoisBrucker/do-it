---
layout: layout/mon.njk

title: "MON 2.1 : Animation 3D en React"
authors:
  - Kévin BERNARD

date: 2024-11-18
tags: 
  - "temps 2"
  - "vert"
  - "react"
  - "react three fiber"
  - "three.js"
  - "glb"
  - "gltf"
  - "3D"

résumé: ""
---

{% prerequis %}
- React : 1/3 📶
- 3D en Web : 0/3 📶
{% endprerequis %}

{% lien %}
<b>SOURCES</b>
- [Documentation Three.js](https://threejs.org/docs)
- [Documentation R3F](https://r3f.docs.pmnd.rs)
- [Vidéo Youtube de Codeur de Nuit, Tuto THREE.JS](https://www.youtube.com/watch?v=vhK6o26OV4Q)
- [Vidéo Youtube de Codeur de Nuit, Tuto THREE.JS [Javascript]](https://www.youtube.com/watch?v=vhK6o26OV4Q)
- [Vidéo Youtube de Graven, ThreeJS expliqué en 3 minutes (Javascript 3D✨)](https://www.youtube.com/watch?v=4IvhajhllFo) 
- [Vidéo Youtube de rithmic, React Three Fiber (R3F) - The Basics](https://www.youtube.com/watch?v=vTfMjI4rVSI)
-  [Site FreeCodeCamp, How to Implement a Blender Model in a React.js Application using Three.js](https://www.freecodecamp.org/news/blender-three-js-react-js/)
-  [Vidéo Youtube de The Khronos Group, What is glTF?](https://www.youtube.com/watch?v=tonSNnEj-ow)
{% endlien %}

## Table des matières

1. [Introduction](#section1)
2. [Qu'est-ce que du 3D dans un site web ?](#section2)
3. [Three.js](#section3)
4. [R3F (React Three Fiber)](#section4)
5. [GLB/GLTF](#section5)
6. [Conclusion](#section6)

## 1. Introduction <a id="section1"></a>

J'ai réalisé ce MON pour incorporer des créatures blenders sur un site que j'ai commencé à réaliser pour mon POK 2.
Sachant que je voulais coder en react, je me suis intéressé à l'intégration de modèle 3D pour du react. Je me suis donc posé comme question :

<center><b>Comment ajouter de l'animation 3D (blender) à React ?</b></center>

Ce MON a pour but d'expliquer comment cela marche, le principe, la théorie plutôt que de donner des explications de code. Il existe plein de tutoriel bien mieux que ce que je pourrais faire si je voulais expliquer du code dont les documentations de Three.js et R3F que je vous conseille vivement d'aller consulter.

{% lien %}
- [Documentation Three.js](https://threejs.org/docs)
- [Documentation R3F](https://r3f.docs.pmnd.rs)
{% endlien %}

## 2. Qu'est-ce que du 3D dans un site web ? <a id="section2"></a>

Dans un premier temps j'ai cherché à comprendre ce qu'était du 3D dans un site web.

<!-- On a l'habitude sur les sites webs d'avoir du 2D et avant de me poser la question d'intégrer des créatures blenders je n'avais jamais vu ou entendu parler de 3D sur des sites webs. -->

Cela peut paraître évident mais pour passer de la 2D à la 3D on va rajouter un axe qui va nous permettre d'introduire la notion de profondeur. On passe donc de coordonnées (x, y) à (x, y, z).

Ainsi, ce que l'on a dans un modèle 3D ce sont :
- la **position** (x, y, z) des points pour former la géométrie
- l'**orientation** des points pour calculer le comportement de la lumière
- la **coordonnée des textures** pour projeter une image sur la surface du modèle 3D

Une fois que l'on a ces points, on les projette sur la page web. Ce sont des API comme WebGL développé par Khronos qui font l'intermédiaire entre JS et la carte graphique pour que cette dernière calcule nos points et les projettent à l'écran.

Si vous voulez plus de détail, [Vidéo Youtube de Codeur de Nuit, Tuto THREE.JS](https://www.youtube.com/watch?v=vhK6o26OV4Q)

L'information sur ce sujet est éparse, il se peut que je n'ai pas toutes les informations.

## 3. Three.js <a id="section3"></a>

J'ai ensuite cherché comment intégrer du 3D sur un site. Par recommandation de François BRUCKER et de tout le monde sur Internet, Three.js est la librairie qui ressort pour du web. Il y a des alternatives dont les plus populaires sont Babylon.js ou encore Playcanvas. J'ai choisi de me concentrer sur Three.js car la documentation est de qualité, importante et je souhaite travailler avec R3F qui utilise Three.js.

Three.js est une bibliothèque Javascript parue en 2010 dans sa première version qui permet de placer une zone où l'on va manipuler des objets en 3D.
Pour cela, on va devoir définir une **scène** avec la caméra, des **meshes**, une **lumière**, des **frames** et des **contrôles**.

### Scène

La scène est ce sur quoi la caméra est orientée. On peut la comparer à une scène de théâtre où se passe l'action. Dans Three.js, la scène est représentée par la balise scene et correspond à monde virtuel contenant tous les objets que l'on met dans notre page.

Ainsi avec la balise camera, on peut choisir quelle partie de la scène on veut montrer à travers sur notre canva grâce au renderer.

### Mesh

Les meshes sont les objets que l'on choisit de mettre dans notre scène. Cela peut aller de formes très simples comme un cube, une sphère jusqu'à quelque chose de très compliqué comme un personnage ou un décor.

Quand on choisit un mesh, on peut régler son matériaux, sa taille et sa position.

### Lumière

La lumière c'est la lumière, merci Einstein !
Pour pouvoir voir les couleurs d'un matériaux il faut de la lumière. On a 2 types de lumières: la lumière directionnel qui est à placer et se comporte comme une source de lumière (lampe) et la lumière ambiante qui est uniforme dans notre scène.

### Frames

L'animation d'un objet est une succession d'images de cet objet pour donner l'impression de mouvement.

Une frame correspond à une image et le navigateur relance une nouvelle frame dès que la dernière a fini d'être calculée.
On a donc un delta qui correspond au temps entre la dernière frame et la frame actuelle.

Grâce à cela on peut faire une modification de notre objet chaque seconde (par exemple une rotation) et créer facilement une rotation.

### Contrôles

Les contrôles sont les interactions entre l'utilisateur et la page web. En effet ce qui fait la force du 3D dans une page web est qu'elle réagit aux actions de l'utilisateur.

On peut mettre déclencher des actions quand l'utilisateur clique, hover, scroll, tape au clavier...

{% lien %}
- [Vidéo Youtube de Codeur de Nuit, Tuto THREE.JS [Javascript]](https://www.youtube.com/watch?v=vhK6o26OV4Q)
- [Vidéo Youtube de Graven, ThreeJS expliqué en 3 minutes (Javascript 3D✨)](https://www.youtube.com/watch?v=4IvhajhllFo) 
{% endlien %}

---

Plutôt que de parler du code, je m'attarde sur les principes du 3D dans un site web car je considère ce MON comme une introduction au 3D en web et que je ne vois l'intérêt de répéter ce que dirait la documentation de Three.js qui est déjà complète et claire.

{% lien %}
[Documentation Three.js](https://threejs.org/docs)
{% endlien %}

---

## 4. R3F (React Three Fiber) <a id="section4"></a>

Par la suite, je me suis intéressé à R3F. Dans l'environnement React, c'est la seule bibliothèque qui est suffisamment développée pour être utilisée à ce jour. 

React Three Fiber est Three.js dans l'écosystème de React. Tout ce que l'on utilise de Three.js peut être utilisé dans React. On peut considérer R3F comme une surcouche de Three.js pour s'adapter à l'environnement React.

L'avantage principale de React Three Fiber est que l'on peut utiliser les fonctions hooks de React, notamment UseRef, UseState et UseFrame qui appartient à la bibliothèque de R3F et permet d'exécuter le code à chaque frame.

{% lien %}
- [Vidéo Youtube de rithmic, React Three Fiber (R3F) - The Basics](https://www.youtube.com/watch?v=vTfMjI4rVSI)
- [Documentation R3F](https://r3f.docs.pmnd.rs)
{% endlien %}

### Extensions

En plus de R3F, il existe d'autres bibliothèques qui facilitent l'interaction 3D.
La plus utilisée est React Three Drei qui facilite le code en ajoutant des fonctions préfètes comme le zoom, le fait de tourner autour de notre objet...
Il en existe d'autres à usage plus spécifique comme React Three Cannon pour ajouter les règles physiques du monde réel.

## 5. GLB/GLTF <a id="section5"></a>

Maintenant que je sais comment faire du 3D avec React, il ne me reste plus qu'à apprendre comment utiliser mes modèles blenders avec R3F.

Ce qui fait l'intérêt du 3D en web c'est de pouvoir importer des modèles faits sur d'autres logiciels comme Blender. On serait vite limiter si l'on ne pouvait créer des modèles 3D qu'avec des lignes de code.

Ce qui permet le passage des logiciels de 3D au web est le format glb/gltf, c'est l'équivalent du jpeg pour la 3D. Ainsi, tous nos modèles 3D et animations de notre fichier glb/gltf peuvent être ajoutés à notre canva.

{% lien %}
[Site FreeCodeCamp, How to Implement a Blender Model in a React.js Application using Three.js](https://www.freecodecamp.org/news/blender-three-js-react-js/)
{% endlien %}

Glb/gltf est un format de transmission créé par Khronos pour optimiser le rendu, la taille et le processus des formats 3D pour les applications et le web.

La différence entre gltf (graphic library transmission format) et glb (binary) est la possibilité de pouvoir lire le gltf car il est basé sur du langage JSON mais en contrepartie il est un peu plus lourd.

{% lien %}
[Vidéo Youtube de The Khronos Group, What is glTF?](https://www.youtube.com/watch?v=tonSNnEj-ow)
{% endlien %}

## Conclusion <a id="section6"></a>

Pour répondre à ma question :

**Comment ajouter de l'animation 3D (blender) à React ?**

Grâce à ce MON, j'ai réussi à comprendre comment s'intégrait le 3D dans du web et quels outils utilisés étaient à ma portée pour répondre à mon besoin.
Je peux utiliser React Three Fiber pour ajouter mon document blender, sous format glb, à mon canva.