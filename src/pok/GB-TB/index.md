---
layout: layout/post.njk

title: "Le POK de Timothé et Gabriel"
authors:
  - Timothé BERMOND
  - Gabriel BARBE

tags: ['pok']
---
<!-- Début Résumé -->

Notre site chez nous : 
Gabriel : Jeu de Pierre, Feuille, Ciseaux en 1vs1 pour commencer puis contre l'ordinateur. 
Timothé : Réalisation d'une roulette permettant de faire des choix au hasard. 

<!-- Fin Résumé -->

### Partie Gabriel 

Dans un premier temps, construction du site web en lui même, page accueil reliée à 2 autres pages, dévelopemment du CSS en collaboration avec timothé. <br>
Réalisation du CSS de la page du POK, réussir à situer mon bouton où je le voulais etc. <hr>

Dans un second temps, focus sur le petits jeu Pierre, Feuille, Ciseaux. 
Sans avoir besoin de rentrer dans les détails de ce jeu, le but était plutot de développer une interface graphique et un peu stylysé de quelque chose, ce jeu étant globalementassez facile à programmer. <br>

La partie plus technique est d'afficher les boutons et les liens effectuant ce que l'on veut au bon moment ainsi que les faire disparaitre. Une fois que cela sera fait j'aimerais généraliser ce jeu afin de pouvoir jouer contre l'ordinateur qui donne un coup aléatoire ; l'enjeu étant là encore d'avoir un graphisme cohérent avec différents boutons etc. <br>

J'ai donc commencé par une fonction se déclanchant après l'appui d'un bouton simple. Cette fonction demande quel coup veut effectuer chaque joueur : 

```bash
             function choixCoups (){
                var bool=false;
                while (bool===false) {
                    J1=prompt('J1 choisit son coup : Pierre, Feuille ou Ciseaux');
                    if (J1 === 'Pierre' || J1 === 'Feuille' || J1 === 'Ciseaux') {
                        bool=true;
                    } else {
                        bool=false;
                        alert('Entrez un coup valide ');}
                }
                bool=false;
                while (bool===false) {
                    J2=prompt('J2 choisit son coup');
                        if (J2 === 'Pierre' || J2 === 'Feuille' || J2 === 'Ciseaux') {
                            bool=true;
                        } else {
                            bool=false;
                            alert('Entrez un coup valide ');
                        }
                }
                PFC(J1,J2);
            }
```
PFC est ensuite une fonction déduisant le vainqueur avec des if...else. Problème : une fois le bouton appuyé, on ne peut plus refuser de jouer, le bouton "annuler" du prompt n'annule pas notre demande et affiche "entrez un coup valide". De plus, ma condition n'accepte qu'une orthographe très spécifique pour le coup voulu. Néanmoins cette fonction est satisfaisante pour notre première partie. <hr>
J'ai ensuite développé une autre méthode permettant cette fois-ci de jouer contre l'IA mais aussi de me passer du prompt pour selectionner mon coup. Dorénavant, lorsque j'appuie sur "jouer" une liste de coup disponible apparait et je n'ai qu'à cliquer sur le coup désiré. Parralèlement se lance une fonction determinant le coup de l'IA (déterminé aléatoirement). 

```bash
            function choixCoups2 () {
                var html = document.querySelector('html');

                var panneau = document.createElement('div');
                panneau.setAttribute('class', 'liste');
                html.appendChild(panneau);

                var choix = document.createElement('ul');
                panneau.appendChild(choix);

                var l1 = document.createElement('li');
                choix.appendChild(l1);

                var l2 = document.createElement('li');
                choix.appendChild(l2);

                var l3 = document.createElement('li');
                choix.appendChild(l3);

                var pierre = document.createElement('button');
                pierre.textContent='Pierre';
                l1.appendChild(pierre);
                pierre.addEventListener('click', Pierre);

                var ciseaux = document.createElement('button');
                ciseaux.textContent='Ciseaux';
                l2.appendChild(ciseaux);
                ciseaux.addEventListener('click', Ciseaux);

                var feuille = document.createElement('button');
                feuille.textContent='Feuille';
                l3.appendChild(feuille);
                feuille.addEventListener('click', Feuille);

                document.querySelector('.ensemble').style.display = 'none';
                coupOrdi();
            }
            function coupOrdi(){
                a = 1 + Math.floor(Math.random()*((4-1)));
                if (a===1){
                    J2='Pierre';
                }
                else if (a===2) {
                    J2='Feuille';
                }
                else { 
                    J2='Ciseaux';
                }
            }
```
J'ai ensuite adapté ma page afin que les deux options de jeu soit possible. 