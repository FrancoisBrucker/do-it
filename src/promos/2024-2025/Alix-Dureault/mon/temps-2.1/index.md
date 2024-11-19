---
layout: layout/mon.njk

title: "Javascript et React"
authors:
  - Alix Duréault

date: 2024-10-16
tags: 
  - "temps 2"
  - "info"
  - "React"
  - "JS"

résumé: "Ce MON a pour but de me former en Java Script et en React."
---

{% prerequis %}
Ce MON est fait pour débuter en JS et React mais quelques connaissances en HTML et CSS peuvent être utiles.
{% endprerequis %}


Le but de ce MON est de me former à l'utilisation de React afin que je puisse derrière l'utiliser pour la deuxième partie de mon POK et pour mon projet 3A.

React est un framework front-end qui permet d’avoir accès à des librairies de composants et de simplifier le code du front-end de nos apps. A l'intérieur de ce framework, les composants sont codés en Javascript. Ainsi, ce MON est divisé en 2 parties, une sur les bases de JavaScript et une sur les bases de React.

## Javascript

Pour apprendre les bases de JS, j'ai suivi le parcours de formation proposé sur le site suivant : [JavaScript Roadmap](https://roadmap.sh/javascript).

Le langage JavaScript est une des bases d’Internet avec HTML et CSS. Souvent abréviée en JS. C’est un langage de programmation compilé qui fonctionne avec des fonctions de premier ordre.

Il permet d’ajouter de l’intéractivité aux pages (sliders, allertes, boutons en interactions, popups,…). Il est aussi utilisé pour d’autres raisons come sur Node.js, React, Apache CouchDB, Adobe Acrobat ou Electron.

### Quel est l'intérêt de ce langage et son histoire ?

Pour résumer rapidement, le langage a été crée par Brendan Eich of NetScape en 1995. Il a été crée dans le but de rendre les sites web dynamiques. Au début, il avait été nommé Mocha, puis LiveScript. En 1996, il a été renommé JavaScript dans le but de capitaliser sur la communauté de Java. En 1997, le langage a été standardisé pour la première fois.

Les sources suivantes sont intéressantes pour en apprendre plus sur le sujet : 
- [Historique des différentes versions du langage](https://roadmap.sh/guides/history-of-javascript)
- [Histoire du langage et des stratégies mises en place pour son développement](https://dev.to/codediodeio/the-weird-history-of-javascript-2bnb)
- [Historique des versions et de leurs apports](https://www.educative.io/blog/javascript-versions-history)

### Comment intégrer le fichier JS dans la structure HTML et CSS ?

Pour en apprendre plus sur le sujet, j'ai lu les pages : 
- [Où placer le code JS](https://www.w3schools.com/js/js_whereto.asp)
- [Lier JS au code HTML](https://www.digitalocean.com/community/tutorials/how-to-add-javascript-to-html)

Pour intégrer le JS dans le reste du code pour le front, il y a 2 solutions

#### Placer le JS dans le code HTML

On peut placer le code JS dans le code HTML, entre les balises `<script></script>`. 

```html
<script>
document.getElementById("demo").innerHTML = "My First JavaScript";
</script>
```

On peut placer autant de fonctions JS que l’on veut dans le code. A l’intérieur des balises ```<head>``` ou ```<body>```.  On le place dans le body généralement quand on modifie un élément du body et head quand l’action est extérieure au corps du texte, par exemple pour un pop up.

#### Placer le JS dans un fichier séparé

Le script peut aussi être placé dans un fichier .js séparé.

Si on l’utilise, il faut ajouté la référence dans le code html, soit dans le ```<head>``` ou alors dans le ```<body>```.

```html
<script src="myScript.js"></script>
```

On peut ajouter plusieurs script sur une seule page en écrivant plusieurs fois cette même ligne avec les différents fichiers .js. La ```src``` peut être un URL, un chemin de fichier ou n’importe quel chemin d’accès.

#### Quelle méthode est la plus intéressante ?

Avantages d’un code externe :

- Le même code peut être utilisé sur plusieurs pages web différentes.
- Le HTML et le JS sont séparés.
- Plus lisible et plus facile à maintenir.
- Peut améliorer la rapidité de chargement des pages.

### Quelles formes prennent les variables en JS ?

Sur le sujet j'ai lu les sources suivantes :
- [Introduction sur les variables](https://javascript.info/variables)
- [Plus de détails et quelques exercices](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables)
- [Aller un peu plus loin](https://www.codeguage.com/courses/js/variables)
- [Notion de hoisting](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting)
- [Notion de scope](https://www.w3schools.com/js/js_scope.asp)

Un script js a besoin de travailler avec des informations. On utilise des variables dans le but de les stocker. Elles sont très utiles pour paramétrer différentes actions sur le site.

**Déclarer une variable :**

```JS
let message;
```

En utilisant l’opérateur “=”, on peut en modifier sa valeur.

```JS
sage = 'Hello'; // store the string 'Hello' in the variable named message
```

On peut condenser les deux action ensemble :

```JS
let message = 'Hello!';

let user = 'John', 
	age = 25, 
	message = 'Hello';
```

On peut changer la valeur en réutilisant l’opérateur “=”. On peut aussi copier la valeur d’une variable dans une autre. Mais par contre, on ne peut pas déclarer deux fois la même variable.

Il y a quelques règles pour nommer une variable :
- Le nom ne peut être composé que de lettres, chiffres et les symboles $ ou _
- Le premier caractère ne peut pas être un chiffre
- Si le nom est composé de plusieurs mots, l’écrire dans la structure camelCase
- Les majuscules sont importantes
- Les lettres d’autres alphabet que le latin sont autorisées
- La convention est d’utiliser l’anglais pour nommer les variables
- Les mots “let”, “class”, “return”, “function”, “this” sont interdits
- Le nom ne doit pas contenir d’espace

Une variable peut contenir du texte, des nombres (entier ou décimaux), des fonctions, des données complexes. Il n’y a pas besoin de déclarer le type de la variable.

On peut aussi déclarer des variables constantes. Ce sont des variables dont on ne peut pas changer la valeur. Il faut leur assigner leur valeurs au moment de la déclaration. Ces constantes sont souvent utilisées pour les valeurs difficiles à retenir  ou prônes à des fautes d’orthographes ET connues avant l’exécution comme les codes hexagonales des couleurs. La convention pour les nommer est de les écrire en utilisant des majuscules et des “_”.

```JS
const myBirthday = '18.04.1982';
```

L’hoisting fait référence au process utilisé par l’interpréteur qui consiste à bouger toutes les déclarations de fonctions, variables, classes et imports avant le reste du code. Ces effets ne sont pas valables pour tous les outils de déclaration. ```var```, ```let``` et ```class``` sont considérés comme non hoisting.

Le scope d'une variable correspond à la visibilité de la variable ou de comment elle peut être utilisé après avoir été déclarée. Ce scope dépend de comment la variable a été déclarée. Il en existe 3 types :

- Global Scope : variables déclarées en dehors de fonctions ou de ```{ }```. Elles sont accessibles dans l’ensemble du code. ```var```, ```let``` et ```const``` donnent ce type de scope
- Function Scope : variables déclarées dans une fonction et ne peuvent être utilisées que dans celle-ci. ```var```, ```let``` et ```const``` donnent ce type de scope
- Block Scope : Un block est une partie du code entourée de ```{ }```. variables déclarées dans un block et ne peuvent être utilisées hors de celui-ci. ```let``` et ```const``` donnent ce type de scope

### Quels sont les différents types de variables

Mes sources pour cette partie sont les suivantes :
- [Primitives et Objects](https://www.codeguage.com/courses/js/data-types)
- [Types et structures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)
- [Data types](https://www.w3schools.com/js/js_datatypes.asp)
- [Objects](https://javascript.info/object)
- [Définition des Objects](https://www.w3schools.com/js/js_object_definition.asp)
- [Travailler avec les objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects)

Cela fait référence au type de donnée que peut contenir une variable. Il décrit un ensemble de valeurs et les opérations possibles sur ces valeurs. 

JS est un langage dynamique. Une variable n’est pas assigné à un certain type et on peut donc lui assigner n’importe quel type de données.

JS sépare les données en deux grandes catégories : **primitives** et **objects**.

#### Primitive

Un primitive regroupe les formes simples de données. Il existe 7 types associés à cette catégorie : undefined, null, numbers, strings, Booleans, Symbols and BigInt. Ils n’ont aucune propriété ou méthode qui leurs sont attachées.

- **Number :** nombre, utilisé dans les calculs, les algorithmes,… Ils peuvent être entiers ou décimaux.
- **Strings :** chaînes de caractères. Elle peut être délimité par des apostrophes : “ “ ou ‘ ‘ ou ` `.
- **Booleans :** valeur true ou false. Utilisé avec des opérateurs conditionnels.
- **Null :** 1 seule valeur, la valeur **null**.
- **Undefined** : 1 seule valeur, la valeur **undefined**. Cela indique l’absence de valeur.
- **BigInt :** type numérique qui peut représenter les valeurs de valeurs arbitraires. Permet de faire des opérations avec les grands entiers.
- **Symbol :** valeur unique et immuable. Peut être usée comme une clé pour une propriété d’objet.

#### Object

Un object, ou reference, est l’opposé d’un primitive : une valeur composé de primitives. Donc tous ce qui n’est pas primitive est un object.

Ils sont écrits à l’intérieur de ```{ }``` et composés de valeurs. Leur valeurs sont accessibles à l’aide de la notation avec un point. Les valeurs peuvent être de n’importe quel type.

Une valeur peut être une fonction et dans ce cas là, elle est appelée méthode de l’objet.

On peut créer une fonction constructrice d’objet de même structure quand on a plein d’objets qui vont tous avoir la même structure.

### Quelle forme prend une fonction en JS ?

Sur le sujet, j'ai lu les ressources :
- [Bases sur les fonctions](https://www.codeguage.com/courses/js/functions-basics)
- [Fonctions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)

Les fonctions sont des blocs de codes qui sont utilisables plusieurs fois quand on les appellent. Elles sont codées pour exécuter une tâche particulière.

Il existe plusieurs moyens de déclarer une fonction en JS.

```JS
function square(number) {
  return number * number;
}

const square = function (number) {
  return number * number;
};

const factorial = function fac(n) {
  return n < 2 ? 1 : n * fac(n - 1);
};

var utils = [
   function(a, b) { return a + b; },
   function(a, b) { return a - b; }
];
```

Seule la première façon de déclarer une fonction permet d’appeler une fonction avant de l’avoir déclarer.

La deuxième façon à d'autres avantages : 
- avoir des fonctions anonymes ou non
- référer à la fonction à l’intérieur d’elle même
- utiliser la fonction comme paramètre d’une autre fonction
- définir plusieurs fonctions en une seule

Les fonctions ne peuvent être appeler que dans le scope (fonction, code entier,…) de là où elles ont été déclarées. Les arguments d’une fonction peuvent être des chaînes de caractères, des nombres, des objets et autres.

En JS, on peut utiliser la récursivité de 3 manières différentes :
1. par son nom
2. avec “arguments.callee”
3. une variable définie localement qui fait référence à cette fonction

On peut aussi déclarer une fonction à l’intérieur de la déclaration d’une autre. En faisant cela, la fonction ébergé n’est appelable seulement à l’intérieur de sa fonction parente.

D'autres propriété à regarder dans les sources fournies sont :
- Les rest parameters
- la mise en place de valeur par défaut aux paramètres
- les IIFE

## React

Mes sources principales pour cette partie du MON ont été :
- [Documentation React](https://react.dev/learn)
- [Roadmap sur React](https://roadmap.sh/react)

### Comment créer un nouveau projet React ?

Pour cela le MON de Thomas Duroy [Débuter avec React.js](https://francoisbrucker.github.io/do-it/promos/2022-2023/Duroy-Thomas/mon/MON_3.1/) explique bien comment créer un projet.

### Que contient le code d'une application React ?

Une app REACT est constituée de composants. Un composants fait partie de l’UI et chacun à sa propre logique et apparence. Un composant peut aller d’un bouton à une page entière. Les composants React sont des fonctions JavaScript qui rendent du markup, comme par exemple, cette fonction qui donne un bouton :

```
function MyButton() {
  return (
    <button>I'm a button</button>
  );
}
```

Une fois qu’on a déclaré un composant, on peut l’appeler dans un autre composant :

```
export default function MyApp() {
  return (
    <div>
      <h1>Welcome to my app</h1>
      <MyButton />
    </div>
  );
}
```

Les noms de composants React doivent toujours commencés par une majuscule. Les tags en HTML doivent toujours être en minuscules.

La partie ```export default``` indique quel est le composant principale dans le fichier.

Le mot clé ```export``` permet de rendre cette fonction accessible à l’extérieur du fichier.

React utilise la syntaxe markup JSX (optionnelle) qui est plus rigoureuse que HTML. Attention, un composant ne peut pas renvoyer plusieurs balises JSX ou HTML. On doit les envelopper dans une balise parent qui englobe toutes les autres de type ```<div>…</div>``` ou ```<>…</>```.

### Comment ajoute ton le style à la page ?

En React, on sépcifie une classe CSS avec la propriété ```className```. Elle fonctionne comme l’attribut ```class``` en HTML.

```
<img className="avatar" />
```

Ensuite, dans un fichier css séparé, on écrit le style en css qui correspond.

```CSS
/* Dans le code CSS */
.avatar {
  border-radius: 50\%;
}
```

Pour lier le fichier de style et le fichier on ajoute un tag de type ```<link>``` dans le code html.

### Quelle est l'utilité du JS dans le framework React ?

JSX permet d’intégrer du markup dans le code JavaScript. Grâce aux délimitateurs ```{ }```, on peut retourner dans le JS. Ainsi, cela peut nous permettre de coder des variables dans le code et les afficher dans l’app ou encore d’utiliser des paramètres comme valeurs pour une balise JSX ou l’utiliser dans le style ou encore concatener la donnée avec du texte. Comme par exemple :

{%raw%}
```
return (
  <>
    <h1>{user.name}</h1>
    <img
      className="avatar"
      src={user.imageUrl}
      alt={'Photo of ' + user.name}
      style={{
        width: user.imageSize,
        height: user.imageSize
      }}
    />
  </>
);
```
{%endraw%}

Pour intégrer des variables JS dans le css pour le style, il faut utiliser l’attribut “style” comme dans l’exemple ci-dessus, avec la syntaxe : ```style = {{object}}```.

### Peut-on afficher une information sous certaines conditions ?

Il n’y a pas de syntaxe particulière dans React pour cela. Ainsi, on utilise la syntaxes JS pour cela. Voici plusieurs exemples : 

```
let content;
if (isLoggedIn) {
  content = <AdminPanel />;
} else {
  content = <LoginForm />;
}
return (
  <div>
    {content}
  </div>
);

<div>
  {isLoggedIn ? (
    <AdminPanel />
  ) : (
    <LoginForm />
  )}
</div>

<div>
  {isLoggedIn && <AdminPanel />}
</div>
```
### Comment rendre l'application React interactive a des évènements ?

Pour répondre à des évènements sur l’app, on déclare des fonctions “event handler” à l’intérieur des composants comme la fonction ```handleClick``` dans l’exemple suivant.

```
function MyButton() {
  function handleClick() {
    alert('You clicked me!');
  }

  return (
    <button onClick={handleClick}>
      Click me
    </button>
  );
}
```

Attention, on n’appelle pas la fonction qui gère l’évènement. On la donne seulement au composant. React l’appellera lorsque l’évènement sera déclenché.

### Comment bien décomposer sont projet React ?

Pour cette partie, j'ai utilisé ces deux sources :
- [Premier projet sur React](https://www.youtube.com/watch?v=Rh3tobg7hEo)
- [Penser en React](https://fr.react.dev/learn/thinking-in-react)

La première chose à faire lorsque l’on commence un projet React est de penser à l’UI directement, à quoi va ressembler l’application finale, quels sont ses composants, … Dans un code JS habituel, le programme se compose en plusieurs étapes qui sont exécutés les unes après les autres. En React, la logique se décompose plutôt en “je veux tel rendu visuel”.

Voici un petit résumé des étapes de la construction d’une app React en partant de la maquette :

1. **Décomposer l’UI en une hiérarchie de composants :** Délimiter les composants, sous-composants, les nommer et déterminer leur hiérarchie.
2. **Construire une version statique en React :** Construire une version qui affiche l’UI à partir du modèle de données sans en gérer l’interactivité.
3. **Trouver une représentation minimale suffisante de l’état de l’UI :** Déterminer la plus petite représentation possible de l’état dont l’application a besoin.
4. **Identifier où l’état devrait vivre :** Déterminer quel composant est responsable de faire évoluer cet état en identifiant les composants évoluant en fonction de cet état, trouvant leur plus proche ancêtre commun et en décidant où placer l’état.
5. **Ajouter un flux de données inverse :** Permettre aux composants de modifier les états en fonction de l’interaction avec l’utilisateur.