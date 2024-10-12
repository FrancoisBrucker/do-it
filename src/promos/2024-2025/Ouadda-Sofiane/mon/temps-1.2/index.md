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

{% endlien %}

## Objectifs

L'objectif de ce cours est de fournir les bases pour créer une application Vue.js complète. Vous apprendrez à structurer l'application, utiliser Vue Router, gérer les événements entre composants.

### 1. Initialisation du projet Vue.js

Nous allons commencer par la création du projet Vue.js avec l'aide de Vue CLI.

- **Installer Vue CLI** : Assurez-vous d'avoir Node.js installé, puis exécutez `npm install -g @vue/cli`.
- **Créer un projet Vue** : Utilisez `vue create mon-projet`. Choisissez les options de base comme Babel et Vue Router (sans Vuex).
  
Voici la structure générée du projet :
- **`src/components`** : Contiendra les composants réutilisables.
- **`src/views`** : Contiendra les pages principales (ou vues) de l'application.
- **`src/router`** : Contiendra la configuration des routes (navigation).

### 2. Composants Vue.js

Les composants sont au cœur de Vue.js. Ils permettent de créer des éléments modulaires et réutilisables. Voici comment définir et utiliser un composant.

- **Création d'un composant** : Créez un fichier `MonComposant.vue` dans le dossier `src/components/` avec la structure suivante :

  ```
  vue
  <template>
    <div>
      <h2> "title" </h2>
      <p> "description" </p>
    </div>
  </template>

  <script>
  export default {
    props: {
      title: String,
      description: String
    }
  }
  </script>
  ```

Ce composant prend deux props, title et description, et les affiche dans le template.

  - **Utilisation dans une vue** : Importez ce composant dans une vue (comme Home.vue) et utilisez-le :
  ```
  <template>
  <div>
    <MonComposant title="Bienvenue" description="Ceci est un exemple"/>
  </div>
  </template>

  <script>
  import MonComposant from '@/components/MonComposant.vue';

  export default {
    components: {
      MonComposant
    }
  }
  </script>
  ```

### 3. Vue Router

Pour naviguer entre plusieurs pages de votre application, nous allons utiliser Vue Router.

  - **Installation de Vue Router** : Si vous ne l'avez pas ajouté lors de la configuration du projet, installez-le avec `npm install vue-router`.

  - **Configuration des routes** : Dans src/router/index.js, configurez les routes pour votre application :
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
````

Cela définit deux routes : une pour la page d'accueil et une pour la page "À propos".

  - **Navigation entre pages** : Dans votre template, utilisez le composant <router-link> pour créer des liens de navigation :  
  ```
  <router-link to="/">Accueil</router-link>
  <router-link to="/about">À propos</router-link>
  ```

  - **Afficher la vue actuelle** : Ajoutez <router-view> dans votre App.vue pour rendre la vue actuelle selon l'URL active :
  ```
  <template>
  <div>
    <router-view></router-view>
  </div>
  </template>
  ```

### Horodateur

| Date            | Heures passées | Indications |
| --------------- | -------------- |-------------|
