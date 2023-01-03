---
layout: layout/post.njk

title: "MON 2.1 : Web Front 1"
authors:
  - Thomas Duroy

---

# MON 2.1: WEB DEV 1

J'ai passé la plus grande partie de ces 10h à revoir les bases HTML/CSS/JS sur différents sites comme : 
- https://www.internetingishard.com/html-and-css/?fbclid=IwAR29PimL3BvePP-RgpBlIZK8sbU7aDNeGYtGRIL7RikziVqMCcfwKJfNvg4

- https://developer.mozilla.org/fr/docs/Learn/JavaScript?fbclid=IwAR3AzVCZ8GFXkytVnL8jv7YSSC3Apla98ndJV8ypipAUwtTn7PrLRTXOv4g

<br>
Beaucoup de personnes ayant déjà fait des tutoriels sur les bases du dev web au temps 1, j'ai pensé qu'il serait plus judicieux de me consacrer à l'explication d'éléments intéressants à ajouter à une page web comme un carrousel. 

<br>

Voici donc le tutoriel pour le réaliser. 

<br>


## Tutoriel Carrousel
---

Ce tutoriel consiste en l'explication, étape par étape, du code obtenu à l'adresse suivante : https://codepen.io/dcode-software/pen/BaRMvJo.

<br>

### **Étape 1 : Squelette du carrousel** 
<br>

Dans le body de notre fichier html, nous créons ici 2 éléments de type div qui constituent le squelette de notre carrousel.

```html
<div class=carousel> 
    <div class="carousel_slot"> Mettre ici ce que vous voulez</div>
</div>
```

Le premier div de classe "carousel" sera la box contenant tous les slots. En effet, nous allons empiler les div "carousel_slot" puis n'afficher que celui sélectionné par l'utilisateur à l'aide d'attribution de classe.

Vous pouvez ajouter autant de "carousel_slot" que vous avez envie.

<br>

Un élément important de ce carousel est le div contenant les boutons de navigation. Il sera généré par une fonction js mais ressemble à ceci :

```html
<div class="carousel_navigation">
        <span class="carousel_button"></span>
        <span class="carousel_button"></span>
        <span class="carousel_button"></span>
      </div>
```
(attention, il ne faut **pas** ajouter ce code au fichier html)

<br>


### **Étape 2 : Style CSS**

<br>

L'affichage du slot selectionné se fera par un changement de classes. Il est donc important de créer 4 classes de style distinct, à savoir :
 - Le style d'un slot par défaut  

```css
.carousel_slot{
  display: none;
  }
```
Il est possible de le styliser davantage mais l'attribut "display" doit absolument être fixé à "none" pour faire disparaître les slots non-désirés.

- Le style du slot sélectionné

```css
.carousel_selected_slot{
  display:block;
}
```

Similairement, ici l'attribut "display" doit être "block" pour rendre le slot visible.

- Le style de bouton par défaut

```css
.carousel_button{
  width: 10px;
  height: 10px;
  display: inline-block;
  background: rgba(255,255,255,0.3);
  border-radius: 50%;
}
```
Quelques précisions sur ces paramètres :

-$inline-block$ = contrairement au inline, cet attribut respecte les attributs "margin" et "padding" mais permet aussi de définir une hauteur et largeur de l'élément.

-$rgba$ : a désigne un paramètre alpha, allant de 0 à 1 qui définit la transparence.

-$border-radius$ : indiquer une seule valeur permet de désigner la courbe des 4 coins (avec 50% on obtient un cercle).



- Le style du bouton sélectionné

```css
.carousel_selected_button{
  background:rgba(255,255,255,1);
}
```

On obtient alors des cercles transparents et celui selectionné est plus visible que les autres. 

<img src="carousel_buttons.png">

<br>

### **Étape 3 : Changement de classes avec js**
<br>

Comme mentionné au départ, la création des boutons va passer par une fonction js. Pour chaque "carousel_slot", on crée dans une array un bouton par défaut comme suit:

```js
document.querySelectorAll(".carousel").forEach(carousel =>

  const items = carousel.querySelectorAll(".carousel_slot");
  const buttonsHtml = Array.from(items, () => {
      return `<span class="carousel_button"></span>`;
  });
```
Puis on place ces spans dans un div de navigation qu'on insère à son tour à l'intérieur du carrousel (spécifié par le paramètre "beforeend"). <br>L'appel $buttonsHtml.join("")$ concatène les éléments de la liste. De plus l'argument de cette méthode, appelé le séparateur, définit se qui sépare les éléments dans la concaténation (ici rien d'où les deux guillements). <br>

On obtient au final, le div de navigation comme montré à l'étape 1.

```js
  carousel.insertAdjacentHTML(
      "beforeend", `<div class="carousel_navigation">
			${buttonsHtml.join("")} </div>`
  );
```

Il est maintenant temps de changer faire fonctionner le carrousel en changeant les classes des slots et des boutons. <br>

On commence par déselectionner tous les slots et boutons en réponse au click de l'utilisateur sur un bouton (on garde cependant son indice i).

```js
  buttons.forEach((button, i) => {
      button.addEventListener("click", () => {
        items.forEach((item) =>
          item.classList.remove("carousel_selected_slot")
       buttons.forEach((button) =>
          button.classList.remove("carousel_selected_button")
      );
```
Au slot correspond au bouton d'indice i, on ajoute la classe du slot sélectionné ce qui le fait apparaîte. Et au bouton sur lequel on a cliqué, on lui attribue la classe du bouton selectionné, ce qui le rend moins transparent.

```js
        items[i].classList.add("carousel_selected_slot");
        button.classList.add("carousel_selected_button");
    });
```

Enfin, il ne reste plus qu'à initialiser l'état du carrousel.

```js
items[0].classList.add("carousel_selected_slot");
buttons[0].classList.add("carousel_selected_button");

});
```

Et voilà à quoi cela peut ressembler:

<img src="carousel_1.png">
<img src="carousel_2.png">
<img src="carousel_3.png">