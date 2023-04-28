---
layout: layout/mon.njk

title: " Jest et Next.js : Tests frontend/Backend "

authors:
  - Tuncay Bilgi

date: 2023-04-05

tags:
  - 'temps 3'
  - 'tests'
  - 'react'
---


Dans ce MON, nous allons apprendre à tester nos components React.js

{%prerequis 'Niveau intermédiaire '%}
Pré-requis :

- Bases React et/ou Next.js
- Typescript

 {%endprerequis%}

 {% info %}
 Documentation : 
 - [NextJS](https://nextjs.org/docs)
 - [Jest](https://jestjs.io/fr/)
 {% endinfo %}

 ## Initialisation : 

### Installations

 On commence par installer les dépendances nécessaires et par initialiser notre projet.
 On commence un projet next.js, auquel on installe jest et les types typescript :

 ```sh
 npx create-next-app@latest
 npm i -D jest ts-jest @types/jest
 ``` 

### Fichiers importants

 Ensuite, on ajoute à la racine du projet un fichier de configuration qui va permettre à jest de travailler avec Next.js .

/jest.config.js : 

  ```js
    const nextJest = require("next/jest");
    const createJestConfig = nextJest({
     dir: "./",
    });
    const customJestConfig = {
    moduleDirectories: ["node_modules", "<rootDir>/"],
    testEnvironment: "jest-environment-jsdom",
    };

    module.exports = createJestConfig(customJestConfig);
 ``` 

 On peut voir qu'on y précise un environnement de test, cette ligne est cruciale pour plus tard, puisque c'est cet environnement qui va simuler notre application.

 On créer aussi un dossier _test_ qui va accueillir tous les fichiers tests qui seront exécutés en tapant la commande `npx jest` .

 ### De la matière à tester : 

 Nous allons créer deux types de tests différents : 

- Test backend d'appel à la base de donnée.
- Test frontend avec snapshot.

Pour ça il nous faut une fonction qui appelle une base de donnée et un component à tester.

#### Le component : 

Le component à tester sera un header :

{% raw %}

```js
    import React, {useState, useEffect} from 'react';
    import { getCategories } from '../services';
    import Link from 'next/link';



    const Header = () => {
        const [categories, setCategories] = useState([]);
        useEffect(() => {getCategories().then((result)=> setCategories(result))},[])
    return (
     <>
        <div className='container mx-auto px-10 mb-4' id='header'>
            <div className=' border-black w-full inline-block py-6 border-b-2'>
                <div className='md:float-left block'>
                    <Link href="/">
                        <span className='cursor-pointer font-bold text-4xl text-white inline-block'>
                            ArtBlog
                        </span>
                    </Link>
                </div>
                <div className='hidden md:float-left md:contents'>
                    {categories.map((category) => (
                        <Link key={category.slug} href={{pathname:`/category/${category.slug}`,query:{ name: category.name}}}>
                            <span className='md:float-right mt-2 align-middle text-white ml-4 font-semibold cursor-pointer'>
                                {category.name}
                            </span> 
                        </Link>
                    ))}
                </div>
            </div>
        </div>
        </>

    )
    }

    export default Header

```
{% endraw %}
On peut voir que c'est simplement un header qui affiche un titre et des liens qu'il récupère dans une base de données avec la fonction getCategories().

Ce component apparaît dans toutes les pages du site et est donc utiliser au seins de contextes différents, les tests devront se passer de ces contextes, et ils devront aussi se passer de l'appel à la base de données car il ne faut pas que la résolution du tests dépendent de la disponibilité de la base de données ou même des informations qui y sont contenues.

#### La requête à la base de donnée : 

Nous créons une fonction getCategories() qui va demander à une base de donnée quels catégories existent. Ca n'est pas un simple fetch puisque c'est une requête graphQL, mais cela ne changerait rien si c'était le cas.

```js
export const getCategories = async() => {
        const query = gql`
        query GetCategories {
          categories  {
            name
            slug
          }
        }

        `

        const result = await request(graphqlAPI, query)
        return result.categories
      }
```

### Les tests: 

#### Backend :
On commence par le plus important :  les tests backend.

Dans l'idéal, il faut une base de donnée spéciale pour les tests, et ne pas tester les fonctions sur la base de production car on y modifierait des données potentiellement essentielles.

On créer le fichier "categoriepage.js" dans le dossier test. IL contiendra tous les tests liés à la fonctionnalité du site concernant les catégories.

Jest utilise des méthodes built-in pour tester pleins de choses différentes, allez voir la documentation sur internet pour savoir lesquelles utiliser.

{%attention%}
Par défaut Jest utilise la syntaxe `const a = require('./module')` qui n'est pas compatible avec le reste du projet qui lui est en ES6 et donc utilise la syntaxe suivante `import {a} from module`. Le fichier de configuration d'avant permet la compatibilité avec ce changement d'import.
{%endattention%}

Voici le test : 

```js
import { getCategories,getPostsByCat } from "../services"

test(
    'CategoriesProps are fetched', async() =>{
        const categories = await getCategories();
        expect(categories).toContainEqual({name :'Sculpture',slug:'sculpture'})
    }
)
```

On lance `npx jest`, le résultat nous montre que le test est effectué : 

```sh
 PASS  __tests__/test_header.tsx   
 PASS  __tests__/test_categories.ts

Test Suites: 2 passed, 2 total
Tests:       3 passed, 3 total
Snapshots:   1 passed, 1 total
Time:        2.84 s
Ran all test suites.
```

#### Frontend : 

Les tests frontend sont délicats, déjà car ils ne sont pas forcément recommandés. Le frontend dépend de pleins de choses : 

- le code
- le navigateur
- les données envoyés par la base de données

Non seulement il est dur de tester le frontend en se détachant de ses dépendances, mais en plus cela n'a pas forcément de sens.

Nous allons tout de même essayer d'implémenter un système dit de **snapshot** .
Les snapshot sont une "photographie" de votre frontend à un instant donné. En lançant un test, le code va simuler le frontend puis regarder si il y a des différences avec la snapshot.
Cette snapshot n'est pas stocké en tant qu'image, c'est enfaîte plus ou moins le fichier html qui est récupéré puis comparé.

Voici une implémentation naïve : 

```js
import React from 'react';
import renderer from 'react-test-renderer';
import Header from '../components/Header';
import { getCategories } from '../services';

describe('Header', () => {

  it('renders correctly', async () => {
      const element = renderer.create(<Header/>).toJSON();
      expect(element).toMatchSnapshot();
  });
});
```

Ici, on récupère notre component, puis on le "render" et on le compare à la dernière snapshot avec 'toMatchSnapshot'. Si il n'y a pas de snapshot, jest valide le test et créer une snapshot qui sera utilisée les prochaines fois.

Cette implémentation à deux problème, elle n'est pas asynchrone, et elle lance le component header tel quel. Si la fonction n'est pas asynchrone, on n'attend pas que le component se met à jour avec les données qu'il récupère avant d'enregistrer la snapshot.De plus, lancer le component est un problème car ce component appel la base de données. Si il y a un problème coté BDD, il pourrait se répercuté coté frontend et ça pourrai invalider notre snapshot alors qu'il n'y a pas de soucis coté frontend.

Pour contourner ces problèmes, on utilise des fonctions asynchrones qui attendent la complétion du component et aussi, on utilise des mocks.
Les mocks sont un moyen de jest de dire au component : 'Au lieu d'utiliser ta fonction pour faire ta requête, tu vas utiliser la mienne pour les tests'. 
En pratique : on code une copie de fonction qui renvoie ce que renvoie la fonction qui appel la base de donné quand tout ce passe bien, et on appel cette fonction au lieu d’appeler l'originale.

```js
jest.mock('../services', () => ({
  getCategories: jest.fn(),
}));

beforeEach(() => {
    (getCategories as jest.Mock).mockResolvedValue([{ name: 'category', slug: 'slug' }, { name: 'category2', slug: 'slug2' }]);
  });

```

Ici, on mock le module '../service' qui contient getCategories, et on lui dit de justement remplacer le getCategories par notre fausse fonction initialisée par jest.fn() .

Ensuite, avant chaque test, on dit a getCategories de renvoyer une réponse à une requête avec du contenu, exactement le même format de contenu que ce que doit renvoyer la fonction d'origine mais avec des valeurs de tests.

On lance 'npx jest' et jest nous génère notre snapshot : 

```html
// Jest Snapshot v1, https://goo.gl/fbAQLP

exports[`Header renders correctly 1`] = `
<div
  className="container mx-auto px-10 mb-4"
  id="header"
>
  <div
    className=" border-black w-full inline-block py-6 border-b-2"
  >
    <div
      className="md:float-left block"
    >
      <a
        href="/"
        onClick={[Function]}
        onMouseEnter={[Function]}
        onTouchStart={[Function]}
      >
        <span
          className="cursor-pointer font-bold text-4xl text-white inline-block"
        >
          ArtBlog
        </span>
      </a>
    </div>
        <div className="hidden md:float-left md:contents" id='links'>
            
        </div>
  </div>
</div>
`;

```

On peut retrouver toute l'arborescence de mon Header ... ou presque.

{%attention 'Les problèmes'%}
En théorie, dans la balise d'id 'links' il devrait y avoir les valeurs 'category' de la fonction getCategories. Cependant, il n'y a rien. C'est à cause du fait que la snapshot n'attend pas la mise à jour du useEffect avant d'être sauvegardée. C'est problématique et en sit, on est sensé combiner des await et une fonction act() pour résoudre le problème mais je n'y suis pas arrivé alors je laisse ce problème à l'appréciation du lecteur.
{%endattention%}

### Conclusion : 

Nous avons deux types de tests qui marchent avec jest.
Je trouve personnellement que les tests frontend sont très laborieux pour le peu de bénéfices qu'ils apportent.
 

 

