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

J'ai développé cette application avec Node, Express, Sequelize, MySQL. Je prévois d'utiliser React pour la partie front.

J'ai utilisé le [tuto MERN stack][1], en particulier le tuto [REST API][1] et celui [JWT authentification](https://www.youtube.com/watch?v=enopDSs3DRw&list=PLillGF-RfqbbQeVSccR9PGKHzPJSWqcsm&index=2&ab_channel=TraversyMedia). J'ai remplacé la base de données MongoDB par une base de données [MySQL](https://www.mysql.com/). J'ai donc modifié la partie avec Mongoose en adaptant avec [Sequelize](https://sequelize.org/). J'ai remplacé les JWT par des cookies de session avec [cookie-parser](https://www.npmjs.com/package/cookie-parser). Pour le hachage, j'ai utilisé [bcryptjs](https://www.npmjs.com/package/bcryptjs).

#### Tuto :

- Tout le tuto MERN stack (MongoDB, Express, React, Node) : <https://www.youtube.com/watch?v=-0exw-9YJBo&list=PLillGF-RfqbbQeVSccR9PGKHzPJSWqcsm&ab_channel=TraversyMedia>.
- Tuto Sequelize : <https://sequelize.org/docs/v6/getting-started/>
- Tuto cookie de session avec cookie-parser (pas trop mal): <https://www.section.io/engineering-education/client-side-auth-with-express-cookie-parser/>

[1]: <https://www.youtube.com/watch?v=-0exw-9YJBo&list=PLillGF-RfqbbQeVSccR9PGKHzPJSWqcsm&ab_channel=TraversyMedia>

[2]: <https://sequelize.org/docs/v6/getting-started/>
