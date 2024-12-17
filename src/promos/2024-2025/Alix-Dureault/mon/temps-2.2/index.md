---
layout: layout/mon.njk

title: "TypeScript vs. JavaScript"
authors:
  - Alix Duréault

date: 2024-10-16
tags: 
  - "temps 2"
  - "info"

résumé: "Le but de ce MON est de comprendre comment s'inscrit le langage TypeScript dans la lignée de JavaScript."
---

{% prerequis %}
Pour ce MON, il est intéressant d'avoir des bases en JavaScript. Elles permettent de mieux comprendre les concepts abordés. Pour cela, je peux conseiller la lecture de mon [MON précédent](https://francoisbrucker.github.io/do-it/promos/2024-2025/Alix-Dureault/mon/temps-2.1/).
{% endprerequis %}

En faisant mes recherches pour mon premier MON sur JavaScript et React, j’ai pu entendre parler de TypeScript sans comprendre réellement de quoi il s’agit.

Ainsi, ce MON sera dédié à comprendre ce qu’est le langage TypeScript, à comprendre les différences entre ce langage et JavaScript et enfin apprendre les bases du langage.

Pour commencer mes recherches, j’ai regardé le documentaire ["TypeScript Origins : The Documentary" de OfferZen Origins](https://www.youtube.com/watch?v=U6s2pdxebSo). Il retrace à travers un ensemble d’interview l’histoire de TypeScript. 

A travers la compréhension des enjeux stratégiques, du contexte historique et des interactions avec VsCode ou Angular, il permet d’avoir une bonne vision du but du langage, de sa manière de se développer, des choix stratégiques qui entourent la création et le développement du langage. On comprend notamment l’importance de la création de ce langage pour des grands projets qui utilisait JavaScript et avait du mal avec sa complexité, notamment avec l’exemple de la symbiose avec l’environnement de développement VSCode.

## Qu’est ce que c’est que TypeScript ?

{% lien "Sources" %}

- ["Big projects are ditching TypeScript... Why ?" de Fireship](https://www.youtube.com/watch?v=5ChkQKUzDCs)
- ["What is TypeScript?", article de Meredith Shubel pour TheNewStack](https://thenewstack.io/what-is-typescript/)
- ["TypeScript pour le nouveau programmeur" de typescriptlang.org](https://www.typescriptlang.org/docs/handbook/typescript-from-scratch.html#next-steps)
- ["Where TypeScript Excels" de The New Stack](https://www.youtube.com/watch?v=BUo7B6UuoJ4)
- ["TypeScript vs JavaScript in 2024 - Difference EXPLAINED" de Daniel | Tech & Data](https://www.youtube.com/watch?v=HCXPJmtV47I)

{% endlien %}

TypeScript est un langage lancé en 2012 par Anders Hejlsberg, concepteur de C# chez Microsoft. Il ne rencontre pas un grand succès à ses débuts. Mais suite, à sont adoption par le framework Angular 2, il commence à connaître un succès qui arrive à son climax dans les années 2020.

TypeScript est un langage de programmation compilé, orienté objet et fortement typé qui s'appuie sur JavaScript. Il a été construit sur la base de JavaScript, les deux langages sont ainsi étroitement liés. Son but est d’offrir de meilleurs outils à n’importe quelle échelle que JS, rendre le développement JavaScript plus efficace, introduire les types optionnels dans JavaScript, aider à détecter les erreurs plus tôt et implémenter les fonctionnalités prévues du futur JavaScript.

TypeScript est un langage open source, soutenu par Microsoft. Il est considéré à la fois comme un langage et un ensemble d’outils.

TypeScript comprend trois composants principaux : 

- le **langage** (syntaxe, mots-clés, annotations de type),
- le **compilateur TypeScript TSC** (convertit les instructions écrites en TypeScript en son équivalent JavaScript),
- le **service de langage TypeScript** (couche supplémentaire d'applications de type éditeur).

TypeScript vérifie les erreurs d'un programme avant son exécution, et le fait en fonction des types de valeurs.

## Qu’est ce que c’est que JavaScript ?

{% lien "Sources" %}

- ["What is TypeScript?", article de Meredith Shubel pour TheNewStack](https://thenewstack.io/what-is-typescript/)
- ["TypeScript pour le nouveau programmeur" de typescriptlang.org](https://www.typescriptlang.org/docs/handbook/typescript-from-scratch.html#next-steps)
- ["TypeScript vs JavaScript in 2024 - Difference EXPLAINED" de Daniel | Tech & Data](https://www.youtube.com/watch?v=HCXPJmtV47I)

{% endlien %}

Pour bien comprendre la différence et l’utilité de TypeScript, il faut avoir en tête quelques éléments sur JavaScript.

JavaScript est un langage de programmation faiblement typé. Il est considéré comme un langage universel du Web. 

JavaScript a été initialement introduit comme langage côté client. Il était censé être utilisé seulement pour de courts extraits de code intégrés dans une page Web. Ainsi, les premiers navigateurs Web exécutaient ce code assez lentement. Depuis, JS est monté en popularité, notamment pour créer des expériences interactives. Récemment, avec le développement de Node.js, JavaScript est désormais également identifié comme une technologie émergente côté serveur. Ce changement est notamment du au côté “exécutable n’importe où” que peut avoir JavaScript.

Le problème c’est que à mesure que JavaScript se développe, il devient de plus en plus compliqué, ce qui rend difficile pour les utilisateurs de garder les choses en ordre lorsqu'ils maintiennent et réutilisent le code. Un autre problème de JS est qu’il néglige de nouvelles fonctionnalités comme la vérification de type forte, les vérifications d’erreurs au moment de la compilation et l’orientation objet.

D’autres problèmes résultent du fait des débuts assez humbles du langage, par exemple : 

- L'opérateur d'égalité de JavaScript `==` contraint ses opérandes, cela entraîne des résultats innatendus comme `“ “ == 0`.
- JavaScript permet également d'accéder à des propriétés qui ne sont pas présentes et ces erreurs ne sont détectables que lors de l’exécution.

Enfin JavaScript reste un langage peu typé. Ainsi, les paramètres de fonction et les variables n'offrant que peu ou pas d'informations.

## Quelle est la différence entre JavaScript et TypeScript ?

{% lien "Sources" %}

- ["What is TypeScript?", article de Meredith Shubel pour TheNewStack](https://thenewstack.io/what-is-typescript/)
- ["TypeScript pour le nouveau programmeur" de typescriptlang.org](https://www.typescriptlang.org/docs/handbook/typescript-from-scratch.html#next-steps)
- ["TypeScript vs JavaScript in 2024 - Difference EXPLAINED" de Daniel | Tech & Data](https://www.youtube.com/watch?v=HCXPJmtV47I)

{% endlien %}

Pour comprendre la différence entre TypeScript et JavaScript et l’intérêt de TypeScript, l’article ["La nécessité de TypeScript et ses limites" de christopher.engineering](https://christopher.engineering/blog/typescript-est-necessaire/) est assez intéressant par son exemple simple qui vulgarise ce que permet de faire TypeScript.

JS est un langage dynamique. Cela permet de faire beaucoup de choses différentes mais si le code ne fonctionne pas, on ne peut le détecter qu’au moment où un navigateur l’interprète et retourne une erreur.

TypeScript empêche ce type d’erreur en ajoutant à JS un système de type. C’est donc un JS plus strict. Le vérificateur de types de TypeScript est conçu pour laisser passer les programmes corrects tout en détectant autant d'erreurs courantes que possible. Automatiquement, une variable se verra assigner un type lors de sa première assignation. On peut aussi lui donner son type lors de sa déclaration. Enfin, si une valeur doit avoir plusieurs type, il est aussi possible de lui donner le type `any` qui permet de lui assigner n’importe qu’elle valeur.

Lorsque JS n’est pas un langage compilé, TypeScript fait le choix de l’être. Cette absence de compilation fait que lorsque l’on code en JS, il est difficile de trouver et de corriger les erreurs. Ainsi, TypeScript facilite la vérification des erreurs.

De plus, TypeScript fait une meilleure prise en charge de l’IDE que JS, le compilateur TypeScript informe l'IDE des informations de type riches en temps réel. Cela permet, lorsque l’on utilise TypeScript, de pouvoir voir les erreurs lorsque l’on code.

Un autre avantage est que TypeScript permet, avec la fonction `tsc index.ts` de passer à un fichier JS. Il est d’ailleurs possible de choisir la version de JS à laquelle on veut se rendre. Ainsi, lorsque l’on code en TypeScript, on n’a pas besoin de se soucier de si une fonction utilisée sera supportée ou non par tel ou tel navigateur.

Enfin, contrairement à JavaScript, TypeScript permet d’utiliser les concepts de programmation orientée objet dans le domaine des classes, des interfaces et de l’héritage.

Du point de vue des ressemblances, TypeScript préserve le comportement d'exécution de JavaScript. Si on déplace du code de JavaScript vers TypeScript, il est garanti qu'il s'exécutera de la même manière, même si TypeScript pense que le code comporte des erreurs de type.

## Quelle est l’interopérabilité des deux langages ?

{% lien "Sources" %}

- ["TypeScript pour le nouveau programmeur" de typescriptlang.org](https://www.typescriptlang.org/docs/handbook/typescript-from-scratch.html#next-steps)
- ["TS/JS Interoperability" de la roadmap TypeScript](https://roadmap.sh/typescript)

{% endlien %}

TypeScript et JavaScript sont entièrement interopérables. 

Le fait que TypeScript soit construit sur la base de JavaScript signifie aussi que la syntaxe de JS est légale en TS. TypeScript ne considère aucun code JavaScript comme une erreur en raison de sa syntaxe. Cela signifie que vous pouvez prendre n'importe quel code JavaScript fonctionnel et le placer dans un fichier TypeScript sans vous soucier de la manière exacte dont il est écrit.

Cela est valable dans ce sens mais aussi dans l’autre : on peut utiliser du code TypeScript dans des projets JavaScript.

Cette interopérabilité est valable à la fois pour la syntaxe mais aussi pour les bibliothèques. Pour utiliser des bibliothèques JavaScript dans des projets TypeScript, il suffit d’inclure directement les fichiers JavaScript ou d’utiliser des définitions de type pour la bibliothèque. Les définitions de type fournissent des informations de type pour les bibliothèques JavaScript, ce qui facilite leur utilisation dans TypeScript.

Pour aller plus loin sur comment utiliser JavaScript dans un projet TypeScript et incorporer petit à petit du TypeScript dans la syntaxe, cette vidéo ["Using JavaScript in TypeScript - Discover the Interoperability" by TypeScript TV with  Benny](https://www.youtube.com/watch?v=AZhZlEbBaB4) est assez intéressante.

## En résumé, pourquoi utiliser TypeScript ?

{% lien "Sources" %}

- ["What is TypeScript?", article de Meredith Shubel pour TheNewStack](https://thenewstack.io/what-is-typescript/)

{% endlien %}

TypeScript est à la fois plus simple et plus efficace. Sa prise en main est rapide lorsque l’on sait déjà codé en JavaScript et les intéractions entre fichiers .js et .ts est relativement simple.

Un autre avantage est sa portabilité. TypeScript peut s'exécuter dans n'importe quel environnement où JavaScript s'exécute : navigateurs, appareils et systèmes d'exploitation.

## Quelles sont les limites de TypeScript ?

{% lien "Sources" %}

- ["Big projects are ditching TypeScript... Why ?" de Fireship](https://www.youtube.com/watch?v=5ChkQKUzDCs)
- ["Bases" de typescriptlang.org](https://www.typescriptlang.org/fr/docs/handbook/2/basic-types.html)
- ["La nécessité de TypeScript et ses limites" de christopher.engineering](https://christopher.engineering/blog/typescript-est-necessaire/)

{% endlien %}

En 2023, quelques gros projets ont décidé de ne plus utilisé TypeScript mais à la place de revenir sur du JS pur. Cela peut être compliqué à comprendre lorsque l’on connaît tous les points positifs que peut avoir TypeScript comparé à JS.

La raison qui a pu être trouvé d’abandonner l’utilisation de TypeScript est la raison qui en fait un bon langage comparé à JS : les types. En effet, même si la présence de type pour les variables empêche certaines erreurs d’arriver, cela implique aussi une grande complexité du code. En effet, pour garantir la cohérence et la sécurité du programme, tout doit être typé.

De plus, la vérification de types limite les sortes de programmes que l’on peut lancer. Il y a des situations où cette rigueur est contre-productive.

Enfin, le système de type de TypeScript n’est pas parfait et connaît une certaine limite lorsqu’il traite de la donnée externe. Une fois que l’application tourne et va chercher ces données extérieurs, on est de nouveau exposé au genre d’erreurs que l’on voulait éviter de base. Une solution pour ce type de solution est d’implémenter un système de runtime type checking, créer une fonction qui contrôle tout ce qui rentre dans l’application au runtime.

Une autre raison qui peut être soulevé, c’est que lorsque l’on passe de TypeScript à JavaScript, on élimine l’étape de compilation. Cela peut donner un gros boost en productivité, notamment pour un projet de grande envergure. De plus, on peut retrouver les bénéfices de TypeScript dans JS en utilisant JSDoc.

D’autres soucis de TypeScript qui peuvent être soulevés sont : 

- **Les outils :** il faut comprendre la configuration complexe de TypeScript pour pouvoir l’utiliser et les librairies externes peuvent être compliquées à utiliser quand les types sont de mauvaises qualités.
- **La verbosité :** au lieu d’un langage concis comme JS, on passe à un code annoté qui demande parfois l’écriture manuelle de type. Cela demande plus de travail et de temps.

## Qu’est ce que c’est que JSDoc ?

{% lien "Sources" %}

- ["Big projects are ditching TypeScript... Why ?" de Fireship](https://www.youtube.com/watch?v=5ChkQKUzDCs)
- ["Getting Started with JSDoc 3" de jsdoc.app](https://jsdoc.app/about-getting-started)

{% endlien %}

JSDoc est un format de commentaire standard où l’on déclare des types et de la documentation dous le format habituelle des commentaires JS. Ces commentaires peuvent être utilisés pour générer des type et permet de garder le fil des fonctions et variables crées an aillant accès à la définition des paramètres au fur et à mesure qu’ils sont utilisés. 

JSDoc 3 est une API qui génère de la documentation pour JavaScript. En ajoutant des commentaires sous le format JSDoc directement dans le code source, l’API les scanne et génère la documentation HTML automatiquement.

Le git officiel de l’API de documentation est disponible sur ce lien : [Github de JSDoc](https://github.com/jsdoc/jsdoc). Il est possible d’apporter une contribution au projet depuis ce repository GitHub. La page offre aussi tout un guide sur l’installation et l’utilisation de l’API. Cette API permet de générer automatiquement la documentation du fichier yourJavaScriptFile.js avec la ligne de commande : 

```bash
./node_modules/.bin/jsdoc yourJavaScriptFile.js
```

Les commentaires JSDoc se place immédiatement avant le code à documenter. Chaque commentaire commence par `/**`, cela permet d’être détecter par l’API. Pour ajouter à la description du code, on peut ajouter des tags comme `@constructor` pour des fonctions qui sont des constructeurs pour des classes.

La page ["JSDoc Reference" de typescriptlang.org](https://www.typescriptlang.org/docs/handbook/jsdoc-supported-types.html) donne une vision  des tags qui sont utilisables avec JSDoc que ce soit dans TypeScript ou JavaScript. En effet, certains ne sont utilisables que dans l’un des deux seulement. La page liste des tags existants et pour chacun détaille l’utilisation qui peut en être faite, la syntaxe associée.

## Comment créer un projet TypeScript, le configurer et l’exécuter?

{% lien "Sources" %}

- ["Install and Configure" et "Running TypeScript" la roadmap TypeScript](https://roadmap.sh/typescript)
- ["Download TypeScript" de typescriptlang.org](https://www.typescriptlang.org/download/)

{% endlien %}

Il y a trois moyens différents d’installer TypeScript selon l’utilisation prévu :

- module npm
- package NuGet
- extension Visual Studio

L’installation peut aussi se faire dans deux scopes différents, celui du projet ou une installation plus globale. L’installation globale n’est pas forcément intéressante, elle ne permet pas la même flexibilité qu’une installation par projet. En effet, lorsque l’on installe TypeScript par projet, cela permet d’utiliser de nombreuses versions différentes de TypeScript et donc pour chaque projet de fonctionner de manière cohérente.

### Installation par un module npm pour un projet spécifique

TypeScript est disponible sous forme de package sur le registre npm disponible sous le nom `typescript`. 

Il faut tout d’abord initialiser npm dans le répertoire du projet en question avec la commande : 

```bash
npm init
```

Pour l’ajouter à un projet, il suffit de taper dans le terminal la commande : 

```bash
npm install --save-dev typescript 
```

Pour configurer le projet, on créer un fichier `tsconfig.json` dans le répertoire du projet. Ce fichier spécifie les options du compilateur pour la construction de ce projet. Cela peut ressembler à :

```json
{
  "compilerOptions": {
    "target": "es5",
    "module": "commonjs",
    "strict": true,
    "outDir": "./dist",
    "rootDir": "./src"
  },
  "exclude": ["node_modules"]
}
```

Pour exécuter le compilateur TypeScript, on utilise la commande suivante dans le terminal :

```bash
npx tsc
```

Il est possible de jouer sur certaines options lors de la compilation. La page ["tsc CLI Options" de typescriptlang.org](https://www.typescriptlang.org/docs/handbook/compiler-options.html) détaille ce qui est de faire. On peut par exemple spécifier les fichiers d’entrée, ajouter des options de construction, des options de surveillance, des commandes CLI ou des drapeaux de compilateur.

Une fois le fichier compiler, il faut ensuite exécuter le code JavaScript généré avec la commande : 

```bash
node app.js
```

## A quoi sert le fichier `tsconfig.json` ?

{% lien "Sources" %}

- ["tsconfig.json" de la roadmap TypeScript](https://roadmap.sh/typescript)
- ["What is a tsconfig.json" de typescriptlang.org](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html#handbook-content)

{% endlien %}

`tsconfig.json` est un fichier de configuration dans TypeScript qui spécifie les options du compilateur pour la création de votre projet. Il aide le compilateur TypeScript à comprendre la structure de votre projet et la manière dont il doit être compilé en JavaScript.

```json
{
  "compilerOptions": {
    "target": "es5",
    "module": "commonjs",
    "strict": true,
    "outDir": "./dist",
    "rootDir": "./src"
  },
  "exclude": ["node_modules"]
  "include": ["src"]
}
```

### Explication des options

Les sources que j’ai pu trouver détaillent seulement les options les plus communes.

- **target :** permet d’indiquer la version de JavaScript à compiler
- **module :** indiquer le système de modules à utiliser
- **strict :** activer ou désactiver la vérification stricte du type
- **outDir :** donner le répertoire pour générer les fichiers JavaScript compilés
- **rootDir :** donner le répertoire racine des fichiers TypeScript
- **include :** donner un tableau de modèles de fichiers/répertoires à inclure dans la compilation
- **exclude :** donner un tableau de modèles de fichiers/répertoires à exclure de la compilation

## Quels sont les types qu’ajoute TypeScript à JavaScript ?

{% lien "Sources" %}

- ["Typescript Types" et les différents articles pour les types existants de la roadmap TypeScript](https://roadmap.sh/typescript)
- ["Everyday Types" de typescriptlang.org](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html)

{% endlien %}

Avec TypeScript, il est possible d’utiliser des types générique ou de créer ces propres types. Je vais commencer par présenter les types inclus dans le langage TypeScript.

On peut distinguer les types relatifs aux primitives et ceux relatifs aux objects.

### Les types primitives

Dans JavaScript, trois primitives sont couramment utilisés et possèdent un type correspondant dans TypeScript :

- **number** (la valeur peut être n’importe quelle valeur numérique, entier ou décimal)
- **string** (n’importe quelle chaîne de caractère)
- **boolean** (peut prendre seulement 2 valeurs, true ou false)

Comme les deux valeurs primitives **null** et **undefined** de JavaScript qui sont utilisées pour signaler une valeur absente ou non initialisée, TypeScript possède des types correspondants portant le même nom. Le comportement de ces types dépend de l'activation ou non de l’option `strictNullChecks`. 

Si elle est désactivée (`off`), des valeurs qui peuvent être null ou undefined peuvent être utilisé dans toutes les propriétés peut importe le type. Si elle est activée (`on`), pour pouvoir utilisée des propriétés pour ces valeurs, il va falloir les tester.

D’autres types de primitives existent :

- **BigInt**, utilisée pour les très grands entiers
- **Symbol**, utilisée pour créer une référence unique dans l’ensemble du code. Ainsi en utilisant la fonction `Symbol()`, la valeur contenu dans la fonction ne peut être utilisée qu’une seule fois dans l’ensemble du code.

```tsx
const firstName = Symbol("name");
const secondName = Symbol("name");
```

Le type **void** représente le type lorsque les fonction s ne retournent aucune valeurs. C’est le type induit par TypeScript à chaque fois qu’une fonction ne retourne rien.

### Les types objects

TypeScript permet de saisir spécifiquement un objet à l'aide d'une **interface** qui peut être réutilisée par plusieurs objets.

```tsx
interface Point {
  x: number;
  y: number;
}
 
function printCoord(pt: Point) {
  console.log("The coordinate's x value is " + pt.x);
  console.log("The coordinate's y value is " + pt.y);
}
```

On peut aussi créer des **classes** : elles sont des plans directeurs pour la création d'objets dotés de propriétés et de méthodes spécifiques. Les classes sont un concept fondamental de la programmation orientée objet.

```tsx
class Car {
  make: string;
  model: string;
  year: number;

  constructor(make: string, model: string, year: number) {
    this.make = make;
    this.model = model;
    this.year = year;
  }
```

Les **énumérations (`enum`)** permettent de définir un ensemble de constantes nommées. Cela peut faciliter la documentation ou la création d'un ensemble de cas distincts.

```tsx
enum Direction {
  Up = 1,
  Down,
  Left,
  Right,
}
```

Pour les **tableaux**, il existe plusieurs manières de déclarées leurs types :

- number[ ]
- Array<number>

Cette syntaxe permet de changer la partie `number` en fonction du type contenu dans l’array.

Le type **tuple** représente un autre type de tableau. Il est utile lorsque l’on sait exactement combien d'éléments il contient et exactement quels types il contient à des positions spécifiques.

```tsx
type StringNumberPair = [string, number];
```

### Les autres types

TypeScript possède aussi un type spécial : **any**. Ce type est utilisable à chaque fois que l’on souhaite se soustraire aux erreurs de vérification de type.

Le type **unknown** est l'équivalent de type sûr de any. On peut lui assigner n’importe qu’elle valeur. Aucune opération n'est autorisée sur un unknown sans d'abord affirmer ou restreindre à un type plus spécifique.

Le type **never** représente le type des valeurs qui n'apparaissent jamais.

## Comment créer son propre type ?

{% lien "Sources" %}

- ["Everyday Types" de typescriptlang.org](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html)
- ["Union Types”, “Intersection Types”, “Types Aliases”, “keyof operators” et “Combining Types” de la roadmap TypeScript](https://roadmap.sh/typescript)

{% endlien %}

Le système de types de TypeScript permet de créer de nouveaux types à partir de types existants.

1. **Union types**

Un type d'union est un type formé de deux ou plusieurs autres types, représentant des valeurs qui peuvent être n'importe lequel de ces types.

```tsx
function printId(id: number | string) {
  console.log("Your ID is: " + id);
}
```

TypeScript n'autorisera une opération que si elle est valide pour chaque membre de l'union.

2. **Type aliases**

Au lieu d’écrire des types d’objets ou des types unions à chaque fois pour les nouveaux objets, on peut définir un type pour le réutiliser plusieurs fois et y référer avec un seul nom. La syntaxe pour le définir est la suivante :

```tsx
type Point = {
  x: number;
  y: number;
};

type ID = number | string;
```

Ce type est utilisable comme n’importe quel autre type.

Les interfaces et les alias se ressemblent beaucoup. La seule différence qui peut être faite est qu’un type alias est défini une seule fois et ne peut être modifié alors qu’une interface peut être agrandie.

3. **Intersection types**

Ce type permet de créer un nouveau type en combinant plusieurs types existants. Le type crée possède toutes les caractéristiques des types existants.

```tsx
interface A {
  a: string;
}

interface B {
  b: number;
}

type AB = A & B;
let value: AB = { a: 'hello', b: 42 };
```

4. **L’opérateur keyof**

Cet opérateur est utilisé pour obtenir l’union des keys d’un type d’un objet.

```tsx
interface User {
  name: string;
  age: number;
  location: string;
}

type UserKeys = keyof User; // "name" | "age" | "location"
const key: UserKeys = 'name';
```

## Comment ajouter le type dans le code ?

{% lien "Sources" %}

- ["Everyday Types" de typescriptlang.org](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html)

{% endlien %}

Dans la plupart des cas et dans la mesure du possible, TypeScript tente de déduire automatiquement les types du code. C’est à dire, si on écrit : 

```tsx
let myName = "Alice";
```

Le type de la variable myName sera déduit automatiquement comme un string.

Pour déclarer le type d’une variable nous même, on va utiliser la syntaxe :

```tsx
let myName: string = "Alice";
```

Pour les fonctions, TypeScript permet de spécifier les types des valeurs d’entrée et de sortie des fonctions. Lorsque l’on déclare une fonction, on peut ajouter des annotations de type après chaque paramètre pour déclarer les types de paramètres acceptés par la fonction. Cela prend la forme suivante :

```tsx
/* Annotation sur la valeur d'entrée */
function greet(name: string) {
  console.log("Hello, " + name.toUpperCase() + "!!");
}

/* Annotation sur la valeur de sortie */
function getFavoriteNumber(): number {
  return 26;
}
```

Comme pour les annotations de type de variable, généralement il n’y a pas besoin d'une annotation sur les valeurs de sortie. TypeScript déduira le type de retour de la fonction.

Pour les objets, on liste leurs propriétés et leurs types sous la forme : 

```tsx
pt: { x: number; y: number }
```

## Que sont les assertions ?

{% lien "Sources" %}

- [" As Type", “As Const”, “Non Null Assertion” de la roadmap TypeScript](https://roadmap.sh/typescript)
- ["The satisfies Operator" de typescriptlang.org](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-9.html#the-satisfies-operator)

{% endlien %}

Les assertions de type sont un moyen de remplacer la vérification de type statique par défaut et d'indiquer au compilateur que vous en savez plus sur le type d'une expression particulière que lui. On utilise le mot clé `as` pour les réaliser. Il permet d'informer explicitement le compilateur du type d'une valeur lorsqu'il ne peut pas être déduit automatiquement.

```tsx
let someValue: any = "Hello, TypeScript!";
let strLength: number = (someValue as string).length;
```

Dans l’exemple, le mot clé `as` permet d’être sur que someValue soit un string avant d’aller chercher la propriété `.lenght`.

Il est important de noter que les assertions de type ne modifient pas le type d'exécution d'une valeur et ne provoquent aucun type de conversion. Il s'agit d'une construction de compilation utilisée pour la vérification de type statique dans TypeScript.

Un autre type d’assertion est celle qui utilise les mots clés `as const`. Ils permettent d’affirmer qu'une expression a un type spécifique et que sa valeur doit être traitée comme une valeur en lecture seule.

```tsx
const colors = ['red', 'green', 'blue'] as const;
```

L’assertion non nul utilisant l’opérateur `!` permet d'indiquer au compilateur qu'une valeur ne sera jamais nulle ou indéfinie.

```tsx
let name: string | null = null;

let nameLength = name!.length;
```

L’opérateur `satisfies` de valider que le type d'une expression correspond à un type, sans modifier le type résultant de cette expression. Cet opérateur peut être utilisé pour détecter de nombreuses erreurs possibles.

```tsx
type Colors = "red" | "green" | "blue";
type RGB = [red: number, green: number, blue: number];
const palette = {
    red: [255, 0, 0],
    green: "#00ff00",
    bleu: [0, 0, 255]
//  ~~~~ The typo is now caught!
} satisfies Record<Colors, string | RGB>;
```

## Quels sont les intérêts d’avoir un langage typé ?

{% lien "Sources" %}

- ["Narrowing" de typescriptlang.org](https://typescriptlang.org/docs/handbook/2/narrowing.html#typeof-type-guards)

{% endlien %}

Comme on a pu le voir, ajouter des types à un langage permet d’éviter des erreurs simples, comme multiplié un string et un number. Mais cela présente d’autres avantages comme pouvoir faire certaines actions en fonction

Certains opérateurs permettent d’effectuer certaines actions en fonction du type de la variable. C’est le cas de l’opérateur typeof.

```tsx
function printAll(strs: string | string[] | null) {
  if (typeof strs === "object") {
    for (const s of strs) {
      console.log(s);
    }
  } else if (typeof strs === "string") {
    console.log(strs);
  } else {
    // do nothing
  }
}
```

Ce type de vérification peut aussi être utilisé avec l’opérateur `===` pour vérifier si deux variables sont du même type :

```tsx
function example(x: string | number, y: string | boolean) {
  if (x === y) {
    // We can now call any 'string' method on 'x' or 'y'.
    x.toUpperCase();
    y.toLowerCase();
  } else {
    console.log(x);
    console.log(y);
  }
}
```

Des opérateurs semblables peuvent être utilisés : 

- `!==`
- `==`

L’opérateur `instanceof` permet de vérifier si un objet est une instance d’une certaine classe.