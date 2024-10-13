---
layout: layout/mon.njk

title: "Développement d'une Application Vue.js"
authors:
  - Sofiane Ouadda
date: 2024-10-10

tags: 
  - temps 1.2
  - "Développement Web"
  - "FrontEnd"
  - "Vue.js"

résumé: "Ce cours détaille comment créer une application complète avec Vue.js, de la configuration initiale à la gestion des composants dynamiques."

---

{% prerequis %}

Bases en HTML, CSS, et JavaScript sont nécessaires. Une connaissance préalable des concepts de programmation réactive est recommandée.

{% endprerequis %}
{% lien %}

[`Vue.js Documentation Officielle`](https://vuejs.org/guide/)

[`Vue Router Documentation`](https://router.vuejs.org/)

[`Vue Mastery – Free Vue.js Tutorials`](https://www.vuemastery.com/)

[`Vue.js Crash Course Youtube`](https://www.youtube.com/watch?v=Wy9q22isx3U)

[`Learn Vue 3 Components`](https://www.youtube.com/watch?v=6IuFRgGQD24)

[`Vue Router Tutorial`](https://www.youtube.com/watch?v=YmxHXjJPfv0)

{% endlien %}

## Objectifs

À la fin de ce cours, vous serez capable de :
1. Comprendre les bases de Vue.js.
2. Configurer un projet Vue.js avec Vue CLI.
3. Créer et utiliser des composants Vue.
4. Configurer et utiliser Vue Router pour naviguer entre plusieurs vues.
5. Gérer les événements entre composants.
6. Utiliser les propriétés calculées et les observateurs pour améliorer la réactivité.
7. Mettre en place une gestion d'état simple sans Vuex.

---

## 1. Introduction à Vue.js

Vue.js est un framework JavaScript progressif utilisé pour construire des interfaces utilisateur dynamiques. Contrairement à des frameworks monolithiques, Vue est conçu pour être adopté de manière progressive. Vous pouvez l'utiliser pour créer des fonctionnalités interactives dans des projets existants ou créer des applications monopages complexes (Single Page Applications - SPA).

### Architecture MVVM (Model-View-ViewModel)

Vue suit un modèle MVVM où :
- **Model** : Représente les données de votre application.
- **View** : Ce qui est visible par l'utilisateur (le HTML).
- **ViewModel** : Fait le lien entre les deux, en répercutant les changements du modèle sur la vue, et inversement.

### Directives

Vue.js est basé sur des **directives** qui lient votre HTML à votre logique JavaScript :
- `v-if` : Affiche ou cache des éléments en fonction d'une condition.
- `v-for` : Boucle sur une liste pour générer plusieurs éléments.
- `v-bind` : Lie dynamiquement des attributs ou des classes CSS à des données.

#### Exemple :
```
<template>
  <div>
    <p v-if="isLoggedIn">Bienvenue, utilisateur !</p>
    <p v-else>Veuillez vous connecter.</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isLoggedIn: false
    };
  }
};
</script>
```

### Réactivité
Vue.js est réactif par nature. Cela signifie que lorsque les données de l'état changent, la vue est automatiquement mise à jour sans que vous ayez à manipuler manuellement le DOM.

## 2. Installation de Vue CLI et création d’un projet

### Installation de Vue CLI

Vue CLI est un outil en ligne de commande qui permet de créer des projets Vue.js de manière rapide et efficace. Il offre une configuration standard avec des outils modernes comme Babel, ESLint, et Vue Router.

#### Installez Vue CLI :

Assurez-vous d’avoir Node.js installé, puis exécutez la commande suivante pour installer Vue CLI globalement sur votre machine :

```
npm install -g @vue/cli
```

### Création d’un projet

Pour créer un nouveau projet, utilisez la commande suivante :

```
vue create mon-projet
```
Vue CLI vous demandera de choisir certaines options comme Babel, Vue Router et ESLint.

### Structure du projet généré

Une fois le projet créé, la structure suivante sera générée :

- `src/components` : Contient tous les composants réutilisables.
- `src/views` : Contient les pages principales de l'application.
- `src/router` : Gère les routes pour naviguer entre différentes vues/pages.
- `App.vue` : Le composant principal qui contient la structure générale de l'application.
- `main.js` : Le point d’entrée où Vue.js est initialisé.

## 3. Création et utilisation des composants

Les composants sont l'élément central de Vue.js. Ils permettent de diviser l'interface en parties réutilisables. Chaque composant a sa propre logique, son template et son style.

### Création d'un composant

Un composant Vue est défini dans un fichier `.vue` et comporte trois sections principales :

- **Template** : Définit la structure HTML.
- **Script** : Contient la logique JavaScript du composant.
- **Style** : Permet d’ajouter des styles spécifiques au composant.

### Exemple de composant simple :

```
<template>
  <div>
    <h1>{{ title }}</h1>
    <p>{{ description }}</p>
  </div>
</template>

<script>
export default {
  props: ['title', 'description']
};
</script>

<style scoped>
h1 {
  color: blue;
}
</style>
```
### Utilisation d’un composant
Une fois créé, vous pouvez réutiliser un composant dans une autre vue ou un autre composant :

```
<template>
  <div>
    <MonComposant title="Bienvenue" description="Ceci est un exemple de composant"/>
  </div>
</template>

<script>
import MonComposant from '@/components/MonComposant.vue';

export default {
  components: {
    MonComposant
  }
};
</script>
```

## 4. Vue Router : Navigation entre Pages

Vue Router est la bibliothèque officielle pour gérer les routes dans une application Vue.js. Il permet de naviguer entre plusieurs pages sans recharger la page, ce qui est essentiel dans une SPA (Single Page Application).

### Installation de Vue Router

Si Vue Router n’a pas été installé lors de la création du projet, vous pouvez l’ajouter avec la commande suivante :

```
npm install vue-router
```

### Configuration des routes

Dans `src/router/index.js`, vous configurez vos routes en associant chaque chemin à un composant de vue :

```
import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/views/Home.vue';
import About from '@/views/About.vue';

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/about', name: 'About', component: About }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
```
### Navigation entre les pages

Pour naviguer entre les pages, vous utilisez le composant `<router-link>` :
```
<template>
  <div>
    <router-link to="/">Accueil</router-link>
    <router-link to="/about">À propos</router-link>
  </div>
</template>
```

Enfin, dans `App.vue`, vous devez inclure le composant `<router-view>` qui rend la vue correspondant à la route actuelle :

```
<template>
  <div>
    <router-view></router-view>
  </div>
</template>
```
## 5. Gestion des événements et méthodes
Vue.js permet de gérer facilement les événements utilisateurs, tels que les clics de boutons ou les saisies de formulaires, via des méthodes associées.

### Attachement d'événements

Vous pouvez utiliser la directive `v-on` ou son raccourci `@` pour attacher des événements comme `click`, `submit`, etc. :

```
<template>
  <button @click="incrementCounter">Incrémenter</button>
  <p>{{ counter }}</p>
</template>

<script>
export default {
  data() {
    return {
      counter: 0
    };
  },
  methods: {
    incrementCounter() {
      this.counter++;
    }
  }
};
</script>
```

Dans cet exemple, chaque fois que le bouton est cliqué, la méthode `incrementCounter` est appelée, augmentant la valeur de `counter`.

## 6. Computed Properties et Watchers
Les computed properties et watchers sont deux fonctionnalités puissantes pour gérer les calculs basés sur les données et réagir aux changements.

### Computed Properties
Les computed properties sont des propriétés dérivées qui sont recalculées uniquement lorsque leurs dépendances changent, ce qui améliore les performances par rapport aux méthodes :

```
<template>
  <div>
    <p>Prix total : {{ totalPrice }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      price: 100,
      quantity: 2
    };
  },
  computed: {
    totalPrice() {
      return this.price * this.quantity;
    }
  }
};
</script>
```

### Watchers

Les **watchers** permettent de surveiller des données réactives et d'exécuter du code lorsque ces données changent. Cela peut être particulièrement utile pour effectuer des actions en réponse à des modifications.

#### Exemple de Watcher
Voici un exemple simple de watcher qui réagit aux changements d'une propriété :

```
<template>
  <div>
    <input v-model="inputText" placeholder="Entrez du texte"/>
    <p>Texte actuel : {{ inputText }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      inputText: ''
    };
  },
  watch: {
    inputText(newValue) {
      console.log(`Texte modifié : ${newValue}`);
      // Vous pouvez également ajouter ici des actions supplémentaires
    }
  }
};
</script>
```
Dans cet exemple, chaque fois que `inputText` est modifié par l'utilisateur, un message est enregistré dans la console.

## 7. Gestion d'état avec Vue.js
Bien que Vuex soit le système de gestion d'état officiel pour Vue.js, il est parfois possible de gérer l'état global simplement avec des méthodes dans votre composant. Cela peut être suffisant pour des projets simples.

### Exemple de gestion d'état basique
Nous pouvons gérer un état global (comme un panier d'achats) en utilisant des événements personnalisés ou des props. Voici un exemple basique sans Vuex :

```
<template>
  <div>
    <button @click="addToCart(item)">Ajouter au panier</button>
    <p>Nombre d'articles dans le panier : {{ cartCount }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      cartCount: 0,
    };
  },
  methods: {
    addToCart(item) {
      this.cartCount++;
      console.log(`Article ajouté : ${item}`);
    }
  }
};
</script>
````

Dans cet exemple, lorsque l'utilisateur clique sur le bouton, le nombre d'articles dans le panier augmente, et vous pouvez facilement voir la mise à jour.

## Ressources pour aller plus loin

- [Vue.js Official Guide](https://vuejs.org/guide/)
- [Vue Router Official Documentation](https://router.vuejs.org/)
- [YouTube Channel - Academind](https://www.youtube.com/c/Academind) pour des tutoriels avancés sur Vue.js
- [YouTube - Traversy Media](https://www.youtube.com/c/TraversyMedia) pour des projets pratiques avec Vue.js

## Horodateur

| Date       | Heures passées | Indications                                                                  | 
|------------|----------------|------------------------------------------------------------------------------|
| 25/09      | 1H30           | Visionnage de la vidéo "Vue.js Crash Course" sur YouTube, introduction à Vue.js : Concepts fondamentaux (MVVM, réactivité, directives) | 
| 25/09      | 2H             | Lecture de la documentation officielle de Vue.js sur les concepts de base  |
| 26/09      | 2H             | Visionnage de "Learn Vue 3 - The Complete Guide" sur YouTube  
| 26/09      | 1H30           | Communication entre composants : Événements et passage de données            |
| 27/09      | 1H30           | Pratique des composants et du Vue Router avec des exemples simples   |
| 27/09      | 1H30           | Gestion des événements utilisateurs et méthodes dynamiques                   |
| 28/09      | 1H             | Utilisation des computed properties   | 
| 29/09      | 1H             | Gestion de l'état global avec le système de réactivité de Vue                | 
