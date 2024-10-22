---
layout: layout/mon.njk

title: "Découverte de Three.js"
authors:
  - Assane Diouf

date: 2024-02-14
tags: 
  - "temps 3"

résumé: "Découverte de Three.js et du creative programming."
---

## Introduction
Dans ce MON je vais essayer Three.js, il s'agit d'un framework js qui permet de faire de la 3D directement dans le navigateur. Beaucoup de développeurs créatifs ont pu faire des sites tout à fait bluffant avec ce framework.

## Présentation
Three.js est une librairie javascript constituant une abstraction par dessus WebGL, permettant ainsi de faire des rendus 3D plus facilement directement dans le navigateur.

Il peut être utilisé pour faire des jeux ou des sites offrants des expériences uniques. Cette librairie peut aussi être utilisée pour faire du **creative coding**. Il s'agit de l'utilisation de l'informatique comme un moyen d'expression artistique à part entière.

## Comment l'utiliser ?

### Installation
L'Installation peut se faire de 2 **façons** différentes. Celle que j'ai utilisée consiste à installer three js dans le projet avec node ainsi que vite. *Vite ne sera utilisé que pour le développement.*

```bash
npm install --save three
npm install --save-dev vite
```

Pour lancer le code et visualiser votre site, il faut lancer vite : 

```bash
npx vite
```

### Premiers pas
*Le code de cette section est tiré de la documentation de Three.js*
Commençons par le index.html !

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<title>My first three.js app</title>
		<style>
			body { margin: 0; }
		</style>
	</head>
	<body>
		<script type="module" src="/main.js"></script>
	</body>
</html>
```

On créer une page HTML simple. Tout se passe dans le javascript.

```js
import * as THREE from 'three';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );

const renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );
    
const geometry = new THREE.BoxGeometry( 1, 1, 1 );
const material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } );
const cube = new THREE.Mesh( geometry, material );
scene.add( cube );
    
camera.position.z = 5;
    
function animate() {
    requestAnimationFrame( animate );
    
    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;
    
    renderer.render( scene, camera );
}
    
animate();
```

On commence par importer le package. Ensuite, pour pouvoir afficher des éléments, il nous faut une scène et une caméra.

Ensuite, on récupère le renderer WebGL, c'est lui qui va se charger de faire les appels à WebGL et d'afficher nos modèles.

Puis on crée une forme simple : un cube. Three.js dispose de méthodes de base pour facilement créer les formes usuelles. La géométrie est la forme ici et le mesh va définir la couleur de l'objet. on pourrait ici mettre une texture par exemple. Ici, on veut simplement que notre cube soit vert.
Il ne reste plus qu'à ajouter le cube à la scène.

## Possibilités
Durant ma découverte de Three.JS, j'ai découvert le nombre impressionnant d'applications possibles. La page de démo de la librairie est remplie d'exemples tous plus impressionnants les uns que les autres.

On peut aussi voir de nombreux développeurs utiliser cette librairie pour réaliser des sites aux expériences plus immersives (des portfolios epoustouflants aux jeux vidéo et aux expériences en réalités augmentées).

Pour me former à Three.JS, j'ai démarré un site d'application mais je n'ai pas eu le temps de le mener à son terme. Je pense que pour un développeur avec un esprit d'artiste, three.js est parfait : couplé avec des outils comme Blender il est vraiment possible de laisser sa créativité s'exprimer.

## Comment appprendre ?

Pour apprendre Three.js, il y a des ressources sur le site de la librairie ainsi que sur youtube par exemple. Mais il y a aussi de nombreux cours et en particulier un qui semble n'avoir que de bons retours et être d'excellente qualité (et proposé par un français) : [Three.js Journey](https://threejs-journey.com)

## Sources
- [Three.js](https://threejs.org/docs/index.html#manual/en/introduction/Installation)
- [Video Youtube](https://youtu.be/vhK6o26OV4Q?si=H9FHf-daqZJ9Lmra)
