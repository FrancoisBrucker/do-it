---
layout: layout/post.njk

title: "Le MON de Léonard"
authors:
  - Léonard Barbotteau

tags: ['mon']
---

<!-- début résumé -->
HTML, CSS et JAVASCRIPT
<!-- fin résumé -->

## Description

Dans ce MON, je vais revoir les grands points du CSS et de l'HTML, ainsi que m'introduire à l'écriture du javascript


## Rappels d'HTML et découverte du Javascript.

Cette partie consiste particulièrement à revoir HTML et CSS. Comme mes connaissances ne sont pas très poussées, j'ai décidé de suivre un cours sur openclassrooms. De plus l'objectif du MON est d'apprendre également le Javascript, que je n'ai jamais vu avant cette année. 


#####  1. Apprentissage du HTML/CSS

A l'aide d'[openclassroom](https://openclassrooms.com/fr/courses/1603881-apprenez-a-creer-votre-site-web-avec-html5-et-css3), je revois et découvre de nombreuses possibilités offertes par les deux langages.

#####  2. Création de la page web

Je commence le projet en HTML et CSS en parallèle du point précédent en créant un fichier site.html. J'ai fait quelque chose de très simple mais qui m'a permis d'utiliser les connaissances acquises, de découvrir aussi plein de template en css ce qui je pense sera ma solution retenue à l'avenir. Je pense que se baser sur un css bien fourni et changer certains objets si besoin est plus efficace que faire tout son css soi-meme.

Voici le code utilisé:
~~~
<!DOCTYPE html>
<html>
    <head>
        <!-- En-tête de la page -->
        <meta charset="utf-8" />
        <title>Raclette</title>
        <link rel="stylesheet" href="style.css" />
    </head>

    <body>
        <div class="header">
            <h2>Bonjour et bienvenue sur mon site !<br />
                On va parler des plats d'hiver aujourd'hui</h2>
          </div>

    <div class="row">
        <div class="column" style="background-color:#dd5329">
            <h1>La fameuse et inévitable raclette</h1>
            <p>Source : <a href="https://fr.wikipedia.org/wiki/Raclette">Wikipedia</a></p>
            <p>La raclette (Bratchäs en suisse allemand, Bratkäse en allemand, litt. « fromage rôti ») est une recette de cuisine traditionnelle et emblématique de la cuisine suisse. Variante des fondues au fromage, elle consiste à faire fondre du raclette et à le racler au fur et à mesure qu’il fond. Elle est traditionnellement servie avec des pommes de terre en robe des champs et accompagnée de légumes au vinaigre (cornichons, oignons)</p>
            <img src="raclette.jpg" alt="Photo de Raclette" />
        </div>

        <div class="column" style="background-color:#db7455">
            <h1>La merveilleuse tartiflette</h1>
            <p>Source : <a href="https://fr.wikipedia.org/wiki/Tartiflette">Wikipedia</a></p>
            <p>La tartiflette (dérivé de tartifle ou tartiflâ, pomme de terre en savoyard) est une recette de cuisine à base de gratin de pommes de terre, d'oignons et de lardons, le tout gratiné au reblochon (fromage AOP des pays de Savoie).

                D'origine récente (le plat a été inventé dans les années 1980), la recette est devenue l'un des emblèmes de la cuisine française, y compris à l'étranger. La « tartiflette au reblochon ou reblochon de Savoie » obtient un Label rouge le 9 octobre 2014 : pour être certifié Label rouge, l'AOP Reblochon de Savoie doit être le seul fromage du plat et constituer au minimum 20 % de la recette1. De plus, le produit doit être gratiné au four traditionnel. </p>
            <img src="tartiflette.jpg" alt="Photo de Tartiflette" />
        </div>


        <div class="column" style="background-color:#c49384">
            <h1>La somptueuse fondue</h1>
            <p>Source : <a href="https://fr.wikipedia.org/wiki/Fondue">Wikipedia</a></p>
            <p>La fondue au fromage consiste en un mélange de fromages, de vin et d'assaisonnement, bien qu'il existe de nombreuses variantes, comme l'utilisation de bière plutôt que de vin20. Traditionnellement, le caquelon est frotté avec une gousse d'ail coupée, le vin blanc est ajouté et chauffé avec de la fécule de maïs, puis le fromage râpé est ajouté et remué doucement jusqu'à ce qu'il soit fondu, bien qu'en pratique tous les ingrédients puissent être combinés et chauffés ensemble en même temps.</p>
            <img src="fondue.jpeg" alt="Photo de Fondue"  width="225" height="225"/>>
        </div>
    
    </div>

    <div class="footer">
        <p>Je vous propose maintenant de jouer à un petit jeu : un <a href= "snake/snake.html"> snake</a> maison!</p>
      </div>
        

    </body>
</html>
~~~
Voici le résultat :
![Fromage](imagesite.jpg "Image du site")

##### 3. Apprentissage du Javascript

J'ai ensuite vu des [tutos sur youtube](https://www.youtube.com/watch?v=XkvrHQNmigs&t=266s) pour m'introduire au JavaScript. C'était intéressant mais juste suivre un cours était compliqué surtout après le long cours sur HTML/CSS.

##### 4. Ecriture d'un petit jeu : Snake
Assez vite j'ai donc voulu mettre la main à la pate et, pour me simplifier la vie et avoir des ressources sur internet je me suis lancé dans l'écriture d'un [Snake](snake.html) en JavaScript.

Voici le code:
~~~
<!DOCTYPE html>
<html>
<head>
  <title>Mon Snake</title>
  <style>
    html, body {
    height: 100%;
    margin: 0;
  }

  body {
    background: black;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  canvas {
    border: 1px solid white;
  }
  </style>
</head>
<body>
<canvas width="400" height="400" id="game"></canvas>
<script>
var canvas = document.getElementById('game');
var context = canvas.getContext('2d');

var grid = 16;
var count = 0;

var snake = {
  x: 160,
  y: 160,
    
  dx: grid,
  dy: 0,

  cells: [],

  maxCells: 4
};
var apple = {
  x: 320,
  y: 320
};

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}

function loop() {
  requestAnimationFrame(loop);

  if (++count < 4) {
    return;
  }

  count = 0;
  context.clearRect(0,0,canvas.width,canvas.height);

  snake.x += snake.dx;
  snake.y += snake.dy;

  if (snake.x < 0) {
    snake.x = canvas.width - grid;
  }
  else if (snake.x >= canvas.width) {
    snake.x = 0;
  }

  if (snake.y < 0) {
    snake.y = canvas.height - grid;
  }
  else if (snake.y >= canvas.height) {
    snake.y = 0;
  }

  snake.cells.unshift({x: snake.x, y: snake.y});

  if (snake.cells.length > snake.maxCells) {
    snake.cells.pop();
  }

  context.fillStyle = 'red';
  context.fillRect(apple.x, apple.y, grid-1, grid-1);

  context.fillStyle = 'green';
  snake.cells.forEach(function(cell, index) {
 
    context.fillRect(cell.x, cell.y, grid-1, grid-1);

    if (cell.x === apple.x && cell.y === apple.y) {
      snake.maxCells++;

      apple.x = getRandomInt(0, 25) * grid;
      apple.y = getRandomInt(0, 25) * grid;
    }

    for (var i = index + 1; i < snake.cells.length; i++) {
   
      if (cell.x === snake.cells[i].x && cell.y === snake.cells[i].y) {
        snake.x = 160;
        snake.y = 160;
        snake.cells = [];
        snake.maxCells = 4;
        snake.dx = grid;
        snake.dy = 0;

        apple.x = getRandomInt(0, 25) * grid;
        apple.y = getRandomInt(0, 25) * grid;
      }
    }
  });
}

document.addEventListener('keydown', function(e) {
  // left arrow key
  if (e.which === 37 && snake.dx === 0) {
    snake.dx = -grid;
    snake.dy = 0;
  }
  // up arrow key
  else if (e.which === 38 && snake.dy === 0) {
    snake.dy = -grid;
    snake.dx = 0;
  }
  // right arrow key
  else if (e.which === 39 && snake.dx === 0) {
    snake.dx = grid;
    snake.dy = 0;
  }
  // down arrow key
  else if (e.which === 40 && snake.dy === 0) {
    snake.dy = grid;
    snake.dx = 0;
  }
});

// start the game
requestAnimationFrame(loop);
</script>
</body>
</html>	
~~~


