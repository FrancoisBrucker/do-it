---
layout: layout/post.njk

title: "InstantBuddy"
authors:
  - Thibault Adelain

tags: ['pok']
---

<!-- début résumé -->

Github: <https://github.com/ThibaultAdelain/InstantBuddyNode>

<!-- fin résumé -->

Cette application a pour but de rencontrer des gens autour de nous, à proximité.

J'ai développé cette application avec :

- *Back-end* : Node, Express, Sequelize, MySQL.
- *Front-end* : React, Redux, tailwind CSS.

J'ai utilisé le [tuto MERN stack][1]. 

**Pour le *back-end* :** j'ai remplacé la base de données MongoDB par une base de données [MySQL](https://www.mysql.com/). J'ai donc modifié la partie avec Mongoose en adaptant avec [Sequelize](https://sequelize.org/). J'ai remplacé les JWT par des cookies de session avec [cookie-parser](https://www.npmjs.com/package/cookie-parser). Pour le hachage, j'ai utilisé [bcryptjs](https://www.npmjs.com/package/bcryptjs).

**Pour le *front-end* :** j'ai utilisé [React](https://fr.reactjs.org/), [Redux](https://redux.js.org/) pour la gestion des states, [tailwind CSS](https://tailwindcss.com/) pour la mise en forme. J'ai aussi utilisé [react-toastify](https://www.npmjs.com/package/react-toastify) et des components [flowbites](https://flowbite.com/).

#### Tuto :

- Tout le tuto MERN stack (MongoDB, Express, React, Node) : <https://www.youtube.com/watch?v=-0exw-9YJBo&list=PLillGF-RfqbbQeVSccR9PGKHzPJSWqcsm&ab_channel=TraversyMedia>.
- Tuto Sequelize : <https://sequelize.org/docs/v6/getting-started/>
- Tuto cookie de session avec cookie-parser (pas trop mal): <https://www.section.io/engineering-education/client-side-auth-with-express-cookie-parser/>

[1]: <https://www.youtube.com/watch?v=-0exw-9YJBo&list=PLillGF-RfqbbQeVSccR9PGKHzPJSWqcsm&ab_channel=TraversyMedia>

[2]: <https://sequelize.org/docs/v6/getting-started/>
