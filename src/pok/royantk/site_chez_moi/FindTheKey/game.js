
//document.getElementById("transitionBox1C").style.display = "inline";
//document.getElementById("transitionBox1C").style.visibility = "hidden";


// Elements

const playButton = document.getElementById("playButton");
const playButtonText = document.getElementById("Play");
const startTitle = document.getElementById("startTitle");
const startElements = document.getElementById("startElements");

const keyIcon = document.getElementById("keyIconC");
const heart1 = document.getElementById("heart1C");
const heart2 = document.getElementById("heart2C");
const heart3 = document.getElementById("heart3C");
const mainMessage = document.getElementById("mainMessageText");

const leftBox = document.getElementById("leftBoxC");
const rightBox = document.getElementById("rightBoxC");
const topBox = document.getElementById("topBoxC");
const bottomBox = document.getElementById("bottomBoxC");
const centerBox = document.getElementById("centerBoxC");

const topLeftBox = document.getElementById("topLeftBoxC");
const bottomLeftBox = document.getElementById("bottomLeftBoxC");
const topRightBox = document.getElementById("topRightBoxC");
const bottomRightBox = document.getElementById("bottomRightBoxC");

const topArrow = document.getElementById("topArrowC");
const bottomArrow = document.getElementById("bottomArrowC");
const leftArrow = document.getElementById("leftArrowC");
const rightArrow = document.getElementById("rightArrowC");

// Objets :

// Case

class Case {

  constructor(x, y, boxType, etat, n) {
    this.n = n;
    this.x = x;
    this.y = y;
    this.boxType = boxType;
    this.etat = etat;

    this.mapId = "map" + String(x) + String(y);

    document.getElementById("miniMap").insertAdjacentHTML('beforeend', '<svg id = map' + String(this.x) + String(this.y) + ' width="280" height="280">' + svgCases[this.boxType][this.etat] + '</svg>');
    document.getElementById('map' + String(x) + String(y)).style.transform = "scale(" + String(1.48 / (n + 0.15 * (n - 1))) + ")";
    document.getElementById('map' + String(x) + String(y)).style.position = "absolute";
    document.getElementById('map' + String(x) + String(y)).style.top = (y * 1.15 * 415 / (n + 0.15 * (n - 1)) + (1.48 / (n + 0.15 * (n - 1)) - 1) * 280 / 2 + 30);
    document.getElementById('map' + String(x) + String(y)).style.left = (x * 1.15 * 415 / (n + 0.15 * (n - 1)) + (1.48 / (n + 0.15 * (n - 1)) - 1) * 280 / 2 + 30);
  }

  getSVG() {
    return svgCases[this.boxType][this.etat];
  };

  action(player) {
    switch (this.boxType) {
      case "key":
        player.hasKey = true;
        break;

      default:
        break;
    };
  };
}


// Jeu

class Game {
  constructor(size) {
    this.size = size;
    this.cases = [...Array(size)].map(() => Array(size));
    this.xDepart = Math.floor(Math.random() * size);
    this.yDepart = Math.floor(Math.random() * size);
    this.xKey = Math.floor(Math.random() * size);
    this.yKey = Math.floor(Math.random() * size);
    /* this.xyEnemies = [];
    for (let i = 0; i < size - 1; i++) {
      x = Math.floor(Math.random() * size);
      y = Math.floor(Math.random() * size);
      xyEnemies[i] = [];
      
    }
 */

    while (this.xKey == this.xDepart && this.yKey == this.yDepart) {
      this.xKey = Math.floor(Math.random() * size);
      this.yKey = Math.floor(Math.random() * size);
    }
  }

  generate() {

    for (let x = 0; x < this.size; x++) {
      for (let y = 0; y < this.size; y++) {

        if (x == this.xDepart && y == this.yDepart) {
          this.cases[this.xDepart][this.yDepart] = new Case(this.xDepart, this.yDepart, "depart", 0, this.size);
        }
        else {
          if (x == this.xKey && y == this.yKey) {
            this.cases[this.xKey][this.yKey] = new Case(this.xKey, this.yKey, "key", 0, this.size);
          }
          else {
            this.cases[x][y] = new Case(x, y, "simple", 0, this.size);
          };
        };

      };
    };

    for (let i = 0; i < Math.min(this.size - 1, 3); i++) {
      let x = Math.floor(Math.random() * this.size);
      let y = Math.floor(Math.random() * this.size);
      while (this.cases[x][y].boxType != "simple") {
        x = Math.floor(Math.random() * this.size);
        y = Math.floor(Math.random() * this.size);
      } 
      this.cases[x][y].boxType = "enemy";
    };
  };
};


// Joueur

class Player {

  constructor(x, y) {
    this.life = 3;
    this.x = x;
    this.y = y;
    this.hasKey = false;
  }

  move(direction, game) {

    game.cases[this.x][this.y].etat = 2; // Case explorée

    switch (direction) {
      case "up":
        this.y -= 1;
        break;
      case "right":
        this.x += 1;
        break;
      case "down":
        this.y += 1;
        break;
      case "left":
        this.x -= 1;
        break;
      default:
        break;
    }

    game.cases[this.x][this.y].etat = 1; // Case active
    game.cases[this.x][this.y].action(this);

    if (game.cases[this.x][this.y].boxType == 'enemy') {
      this.life += -1;
    }

    if (game.cases[this.x][this.y].boxType == 'life') {
      this.life += 1;
    }

    majAffichage(player, game);
    majMap(player, game);
  }
}


// // Ennemi

// class Enemy {
//   constructor(x,y) {
//     this.x = x;
//     this.y = y;
//     this.alive = true;
//   }

//   move() {
//     VorH = (Math.random() > 0.5);
//     PorM = Math.floor(Math.random() * 2) * 2 - 1 ;
//     if (VorH) {
//       this.x += PorM
//     } else {
//       this.y += PorM
//     }
//   }
// }

// Codes SVG des variantes :

const svgCaseActiveSimple = '<rect width="280" height="280" rx="30" fill="#f7f7f7"/>'
const svgCaseInexploreeSimple = '<g fill="none" stroke="#707070" stroke-width="1" stroke-dasharray="15"><rect width="280" height="280" rx="30" stroke="none"/><rect x="0.5" y="0.5" width="279" height="279" rx="29.5" fill="none"/></g>'
const svgCaseExploreeSimple = '<rect width="280" height="280" rx="30" fill="#e4e4e4"/>'
const svgCaseActiveKey = '<defs><filter id="Icon_feather-key" x="57.5" y="51.776" width="175" height="170.603" filterUnits="userSpaceOnUse"><feOffset dx="10" dy="10" input="SourceAlpha"/><feGaussianBlur result="blur"/><feFlood flood-color="#7e7e7e"/><feComposite operator="in" in2="blur"/><feComposite in="SourceGraphic"/></filter></defs><path id="Tracé_3" data-name="Tracé 3" d="M28,0H252a28,28,0,0,1,28,28V252a28,28,0,0,1-28,28H28A28,28,0,0,1,0,252V28A28,28,0,0,1,28,0Z" fill="#f7f7f7"/><g transform="matrix(1, 0, 0, 1, 0, 0)" filter="url(#Icon_feather-key)"><path id="Icon_feather-key-2" data-name="Icon feather-key" d="M145.5,3l-15,15M73.424,75.077a41.251,41.251,0,1,1-58.341,0,41.25,41.25,0,0,1,58.341,0Zm0,0L104.25,44.251m0,0,22.5,22.5L153,40.5,130.5,18M104.25,44.251,130.5,18" transform="translate(62 59.38)" fill="none" stroke="#a7a7a7" stroke-linecap="round" stroke-linejoin="round" stroke-width="15"/></g>'
const svgCaseInexploreeKey = ''
const svgCaseExploreeKey = '<path id="Tracé_3" data-name="Tracé 3" d="M28,0H252a28,28,0,0,1,28,28V252a28,28,0,0,1-28,28H28A28,28,0,0,1,0,252V28A28,28,0,0,1,28,0Z" fill="#e4e4e4"/><path id="Icon_feather-key" data-name="Icon feather-key" d="M145.5,3l-15,15M73.424,75.077a41.251,41.251,0,1,1-58.341,0,41.25,41.25,0,0,1,58.341,0Zm0,0L104.25,44.251m0,0,22.5,22.5L153,40.5,130.5,18M104.25,44.251,130.5,18" transform="translate(67.999 65.752)" fill="none" stroke="#6e6e6e" stroke-linecap="round" stroke-linejoin="round" stroke-width="15" stroke-dasharray="20"/>'
const svgCaseActiveSortie = ''
const svgCaseInexploreeSortie = ''
const svgCaseExploreeSortie = ''
const svgCaseActiveEnemy = '<rect width="280" height="280" rx="30" fill="#ff9696"/><path d="M30.9,34.21l5.3,1.768h.955l1.067-5.339a20.307,20.307,0,0,1,.656-2.41l-4.148-8.3L39.6,5.34A3.271,3.271,0,0,0,37.528,1.2L34.427.169A3.269,3.269,0,0,0,30.29,2.237L25,18.116a6.549,6.549,0,0,0,.354,4.994l5.55,11.1Zm86.291,37.209L106.409,55.246a6.542,6.542,0,0,0-5.441-2.913H85.036l14.1-4.979a6.547,6.547,0,0,0,3.375-2.578L113.47,28.339a3.272,3.272,0,0,0-.908-4.536l-2.721-1.815a3.272,3.272,0,0,0-4.536.908L94.97,38.4,82.6,42.519H75.224L73.1,31.92c-.448-2.242-3.551-12.3-14.233-12.3S45.085,29.678,44.638,31.92l-2.12,10.6H35.138L22.774,38.4,12.436,22.9A3.272,3.272,0,0,0,7.9,21.988L5.18,23.8a3.272,3.272,0,0,0-.908,4.536L15.229,44.776A6.547,6.547,0,0,0,18.6,47.353l14.1,4.977H16.774a6.545,6.545,0,0,0-5.443,2.912L.55,71.419a3.27,3.27,0,0,0,.908,4.536L4.178,77.77a3.272,3.272,0,0,0,4.536-.908l9.812-14.718h9.62L15.711,82.04a6.539,6.539,0,0,0-.993,3.467V101.39a3.27,3.27,0,0,0,3.271,3.271h3.271a3.27,3.27,0,0,0,3.271-3.271V86.445L39.672,62.216c-.206,2.872-.425,5.746-.425,8.628,0,10.848,8.332,20.734,19.624,20.734s19.624-9.885,19.624-20.734c0-2.882-.221-5.756-.425-8.628L93.212,86.445V101.39a3.27,3.27,0,0,0,3.271,3.271h3.271a3.27,3.27,0,0,0,3.271-3.271V85.5a6.552,6.552,0,0,0-.993-3.467L89.6,62.143h9.62l9.812,14.718a3.272,3.272,0,0,0,4.536.908l2.721-1.815A3.268,3.268,0,0,0,117.192,71.419ZM83.01,19.933l-4.148,8.3a20.308,20.308,0,0,1,.656,2.41l1.067,5.339h.955l5.3-1.768,5.55-11.1a6.54,6.54,0,0,0,.354-4.994L87.452,2.237A3.27,3.27,0,0,0,83.315.169L80.214,1.2A3.273,3.273,0,0,0,78.145,5.34L83.01,19.933Z" transform="translate(81.129 87.67)" fill="#a34b4b"/>'
const svgCaseExploreeEnemy = '<rect width="280" height="280" rx="30" fill="#e8d9d9"/><path d="M30.9,34.21l5.3,1.768h.955l1.067-5.339a20.307,20.307,0,0,1,.656-2.41l-4.148-8.3L39.6,5.34A3.271,3.271,0,0,0,37.528,1.2L34.427.169A3.269,3.269,0,0,0,30.29,2.237L25,18.116a6.549,6.549,0,0,0,.354,4.994l5.55,11.1Zm86.291,37.209L106.409,55.246a6.542,6.542,0,0,0-5.441-2.913H85.036l14.1-4.979a6.547,6.547,0,0,0,3.375-2.578L113.47,28.339a3.272,3.272,0,0,0-.908-4.536l-2.721-1.815a3.272,3.272,0,0,0-4.536.908L94.97,38.4,82.6,42.519H75.224L73.1,31.92c-.448-2.242-3.551-12.3-14.233-12.3S45.085,29.678,44.638,31.92l-2.12,10.6H35.138L22.774,38.4,12.436,22.9A3.272,3.272,0,0,0,7.9,21.988L5.18,23.8a3.272,3.272,0,0,0-.908,4.536L15.229,44.776A6.547,6.547,0,0,0,18.6,47.353l14.1,4.977H16.774a6.545,6.545,0,0,0-5.443,2.912L.55,71.419a3.27,3.27,0,0,0,.908,4.536L4.178,77.77a3.272,3.272,0,0,0,4.536-.908l9.812-14.718h9.62L15.711,82.04a6.539,6.539,0,0,0-.993,3.467V101.39a3.27,3.27,0,0,0,3.271,3.271h3.271a3.27,3.27,0,0,0,3.271-3.271V86.445L39.672,62.216c-.206,2.872-.425,5.746-.425,8.628,0,10.848,8.332,20.734,19.624,20.734s19.624-9.885,19.624-20.734c0-2.882-.221-5.756-.425-8.628L93.212,86.445V101.39a3.27,3.27,0,0,0,3.271,3.271h3.271a3.27,3.27,0,0,0,3.271-3.271V85.5a6.552,6.552,0,0,0-.993-3.467L89.6,62.143h9.62l9.812,14.718a3.272,3.272,0,0,0,4.536.908l2.721-1.815A3.268,3.268,0,0,0,117.192,71.419ZM83.01,19.933l-4.148,8.3a20.308,20.308,0,0,1,.656,2.41l1.067,5.339h.955l5.3-1.768,5.55-11.1a6.54,6.54,0,0,0,.354-4.994L87.452,2.237A3.27,3.27,0,0,0,83.315.169L80.214,1.2A3.273,3.273,0,0,0,78.145,5.34L83.01,19.933Z" transform="translate(81.129 87.67)" fill="none" stroke="#b25858" stroke-width="5"/>'
const svgCaseActiveDepart = '<path d="M28,0H252a28,28,0,0,1,28,28V252a28,28,0,0,1-28,28H28A28,28,0,0,1,0,252V28A28,28,0,0,1,28,0Z" fill="#f7f7f7"/><path id="Icon_awesome-home" data-name="Icon awesome-home" d="M87.613,38.566,30,86.016v51.212a5,5,0,0,0,5,5l35.016-.091a5,5,0,0,0,4.975-5V107.23a5,5,0,0,1,5-5h20a5,5,0,0,1,5,5v29.885a5,5,0,0,0,5,5.015l35,.1a5,5,0,0,0,5-5V85.981l-57.6-47.415A3.809,3.809,0,0,0,87.613,38.566Zm91,32.251L152.492,49.284V6a3.75,3.75,0,0,0-3.75-3.75h-17.5A3.75,3.75,0,0,0,127.494,6V28.692L99.518,5.675a15,15,0,0,0-19.061,0L1.36,70.817A3.75,3.75,0,0,0,.86,76.1l7.968,9.687a3.75,3.75,0,0,0,5.284.509l73.5-60.539a3.809,3.809,0,0,1,4.781,0l73.5,60.539a3.75,3.75,0,0,0,5.281-.5l7.968-9.687a3.75,3.75,0,0,0-.531-5.29Z" transform="translate(50.001 67.76)" fill="#e3e6ea"/>'
const svgCaseExploreeDepart = '<path d="M28,0H252a28,28,0,0,1,28,28V252a28,28,0,0,1-28,28H28A28,28,0,0,1,0,252V28A28,28,0,0,1,28,0Z" fill="#e4e4e4"/><path id="Icon_awesome-home" data-name="Icon awesome-home" d="M87.613,38.566,30,86.016v51.212a5,5,0,0,0,5,5l35.016-.091a5,5,0,0,0,4.975-5V107.23a5,5,0,0,1,5-5h20a5,5,0,0,1,5,5v29.885a5,5,0,0,0,5,5.015l35,.1a5,5,0,0,0,5-5V85.981l-57.6-47.415A3.809,3.809,0,0,0,87.613,38.566Zm91,32.251L152.492,49.284V6a3.75,3.75,0,0,0-3.75-3.75h-17.5A3.75,3.75,0,0,0,127.494,6V28.692L99.518,5.675a15,15,0,0,0-19.061,0L1.36,70.817A3.75,3.75,0,0,0,.86,76.1l7.968,9.687a3.75,3.75,0,0,0,5.284.509l73.5-60.539a3.809,3.809,0,0,1,4.781,0l73.5,60.539a3.75,3.75,0,0,0,5.281-.5l7.968-9.687a3.75,3.75,0,0,0-.531-5.29Z" transform="translate(50.001 67.76)" fill="#fafcfc"/>'
const svgCaseVide = ''

const svgCases = {
  "simple": [svgCaseInexploreeSimple, svgCaseActiveSimple, svgCaseExploreeSimple],
  "depart": [svgCaseActiveDepart, svgCaseActiveDepart, svgCaseExploreeDepart],
  "key": [svgCaseInexploreeSimple, svgCaseActiveKey, svgCaseExploreeKey],
  "sortie": [svgCaseInexploreeSortie, svgCaseActiveSortie, svgCaseExploreeSortie],
  "enemy": [svgCaseInexploreeSimple, svgCaseActiveEnemy, svgCaseExploreeEnemy]
}

//const svgKey = '<defs><filter id="Icon_feather-key" x="0" y="0" width="75.33" height="73.612" filterUnits="userSpaceOnUse"><feOffset dx="5" dy="5" input="SourceAlpha"/><feGaussianBlur result="blur"/><feFlood flood-color="#7e7e7e"/><feComposite operator="in" in2="blur"/><feComposite in="SourceGraphic"/></filter></defs><g transform="matrix(1, 0, 0, 1, 0, 0)" filter="url(#Icon_feather-key)"><path id="Icon_feather-key-2" data-name="Icon feather-key" d="M63.164,3,56.831,9.333m-24.1,24.1a17.416,17.416,0,1,1-24.632,0,17.416,17.416,0,0,1,24.632,0Zm0,0L45.748,20.416m0,0,9.5,9.5L66.331,18.833l-9.5-9.5M45.748,20.416,56.831,9.333" transform="translate(0.5 1.95)" fill="none" stroke="#a7a7a7" stroke-linecap="round" stroke-linejoin="round" stroke-width="7"/></g>'
const svgMissingKey = '<g id="keyIcon" transform="translate(3.5 4.95)"><path data-name="Icon feather-key" d="M63.164,3,56.831,9.333m-24.1,24.1a17.416,17.416,0,1,1-24.632,0,17.416,17.416,0,0,1,24.632,0Zm0,0L45.748,20.416m0,0,9.5,9.5L66.331,18.833l-9.5-9.5M45.748,20.416,56.831,9.333" transform="translate(-3.001 -3)" fill="none" stroke="#a7a7a7" stroke-linecap="round" stroke-linejoin="round" stroke-width="7"/></g>'
const svgKey = '<g id="key" transform="translate(-1373.5 -429.901)"><path d="M63.164,3,56.831,9.333m-24.1,24.1a17.416,17.416,0,1,1-24.632,0,17.416,17.416,0,0,1,24.632,0Zm0,0L45.748,20.416m0,0,9.5,9.5L66.331,18.833l-9.5-9.5M45.748,20.416,56.831,9.333" transform="translate(1376.999 435.85)" fill="none" stroke="#6e6e6e" stroke-linecap="round" stroke-linejoin="round" stroke-width="7"/><path d="M63.164,3,56.831,9.333m-24.1,24.1a17.416,17.416,0,1,1-24.632,0,17.416,17.416,0,0,1,24.632,0Zm0,0L45.748,20.416m0,0,9.5,9.5L66.331,18.833l-9.5-9.5M45.748,20.416,56.831,9.333" transform="translate(1373.999 431.85)" fill="none" stroke="#a7a7a7" stroke-linecap="round" stroke-linejoin="round" stroke-width="7"/></g>'
const svgFullHeart = '<g transform="translate(3 3)"><path d="M33.375,59.885,29.024,55.96C13.575,41.775,3.375,32.569,3.375,21.1a16.315,16.315,0,0,1,16.5-16.6,17.747,17.747,0,0,1,13.5,6.339A17.747,17.747,0,0,1,46.875,4.5a16.315,16.315,0,0,1,16.5,16.6c0,11.469-10.2,20.675-25.649,34.86Z" transform="translate(-3.375 -4.5)" fill="#dc3545" stroke="#000" stroke-width="6"/></g>'
const svgEmptyHeart = '<g transform="translate(3 3)"><path d="M33.375,59.885,29.024,55.96C13.575,41.775,3.375,32.569,3.375,21.1a16.315,16.315,0,0,1,16.5-16.6,17.747,17.747,0,0,1,13.5,6.339A17.747,17.747,0,0,1,46.875,4.5a16.315,16.315,0,0,1,16.5,16.6c0,11.469-10.2,20.675-25.649,34.86Z" transform="translate(-3.375 -4.5)" fill="none" stroke="#000" stroke-width="6"/></g>'

// Listeners :

// Départ partie
var gameStarted = false;

playButton.addEventListener('click', function (event) {
  startGame(player, game);
  gameStarted = true;
});

rightArrow.addEventListener('click', function (event) {
  if (player.x < game.size - 1) { player.move("right", game) };
});

leftArrow.addEventListener('click', function (event) {
  if (player.x > 0) { player.move("left", game) };
});

topArrow.addEventListener('click', function (event) {
  if (player.y > 0) { player.move("up", game) };
});

bottomArrow.addEventListener('click', function (event) {
  if (player.y < game.size - 1) { player.move("down", game) };
});

document.addEventListener("keydown", (e) => {
  switch (e.key) {
    case "ArrowLeft":
      if (player.x > 0 && gameStarted) { player.move("left", game) };
      break;
    case "ArrowRight":
      if (player.x < game.size - 1 && gameStarted) { player.move("right", game) };
      break;
    case "ArrowUp":
      if (player.y > 0 && gameStarted) { player.move("up", game) };
      break;
    case "ArrowDown":
      if (player.y < game.size - 1 && gameStarted) { player.move("down", game) };
      break;
  }
});

// Fonctions :

function startGame(player, game) {
  if (gameStarted) {
    document.location.reload(true)
  }
  startElements.style.animation = "start 1s ease 0s 1 normal forwards";
  game.generate(player, game);
  majAffichage(player, game);
}

function majMap(player, game) {
  let xp = player.x;
  let yp = player.y;
  let n = game.size;
  let sc = 1 / (n + 0.15 * (n - 1));

  for (let x = 0; x < n; x++) {
    for (let y = 0; y < n; y++) {
      document.getElementById("map" + String(x) + String(y)).innerHTML = game.cases[x][y].getSVG();
      document.getElementById("map" + String(x) + String(y)).setAttribute("transform", "scale(" + String(1.48 / (n + 0.15 * (n - 1))) + ")")
    };
  };
}

function majAffichage(player, game) {
  let x = player.x;
  let y = player.y;
  let n = game.size;

  switch (player.life) {
    case 3:
      heart1.innerHTML = svgFullHeart
      heart2.innerHTML = svgFullHeart
      heart3.innerHTML = svgFullHeart
      break;
    
    case 2:
      heart1.innerHTML = svgEmptyHeart
      heart2.innerHTML = svgFullHeart
      heart3.innerHTML = svgFullHeart
      break;

    case 1:
      heart1.innerHTML = svgEmptyHeart
      heart2.innerHTML = svgEmptyHeart
      heart3.innerHTML = svgFullHeart
      break;

    default:
      heart1.innerHTML = svgEmptyHeart
      heart2.innerHTML = svgEmptyHeart
      heart3.innerHTML = svgEmptyHeart
      break;
  }

  if (player.hasKey) {
    keyIcon.innerHTML = svgKey;
    mainMessage.innerHTML = "Return home!"
    if (player.x == game.xDepart && player.y == game.yDepart) {
      startElements.style.animation = "start 1s ease 0s 1 normal backwards";
      startTitle.innerHTML = "Well done!"
      playButton.innerHTML = "Replay!"
    }
  }

  centerBox.innerHTML = game.cases[x][y].getSVG();

  leftBox.innerHTML = "";
  rightBox.innerHTML = "";
  topBox.innerHTML = "";
  bottomBox.innerHTML = "";

  topLeftBox.innerHTML = "";
  bottomLeftBox.innerHTML = "";
  topRightBox.innerHTML = "";
  bottomRightBox.innerHTML = "";


  if (x != 0 && y != 0) topLeftBox.innerHTML = game.cases[x - 1][y - 1].getSVG();
  if (x != 0 && y != n - 1) bottomLeftBox.innerHTML = game.cases[x - 1][y + 1].getSVG();
  if (x != n - 1 && y != 0) topRightBox.innerHTML = game.cases[x + 1][y - 1].getSVG();
  if (x != n - 1 && y != n - 1) bottomRightBox.innerHTML = game.cases[x + 1][y + 1].getSVG();

  if (x != 0) leftBox.innerHTML = game.cases[x - 1][y].getSVG();
  if (x != n - 1) rightBox.innerHTML = game.cases[x + 1][y].getSVG();
  if (y != 0) topBox.innerHTML = game.cases[x][y - 1].getSVG();
  if (y != n - 1) bottomBox.innerHTML = game.cases[x][y + 1].getSVG();


  if (player.life <= 0) {
    startElements.style.animation = "start 1s ease 0s 1 normal backwards";
    startTitle.innerHTML = "You died."
    playButton.innerHTML = "Replay!"
  }
}

// Main

let gameSize = 4;
let game = new Game(gameSize);
let player = new Player(game.xDepart, game.yDepart);
