---
layout: layout/pok.njk

title: "Création d'un calendrier avec Vue.js"
authors:
  - Sophia Capdevielle

date: 2024-09-18

tags:
  - "temps 1" 
  - "Vue.js"
---

{% prerequis %}

Bases front-end et Vue.js (cf MON 1.1)

{% endprerequis %}

L'objectif de ce POK est de prendre en main l'outil Vue.js découvert avec mon MON 1.1 en réalisant une application web: un calendrier. Cet outil basique devrait permettre à l'utilisateur d'afficher un calendrier mensuel, de naviguer entre les mois et de gérer des événements.



#### Sprint 1

L'objectif de ce premier sprint est de réaliser une base de calendrier avec Vue.js. 


#### Sprint 2

Pour le prochain sprint, l'objectif est d'intégrer la gestion des événements et d'améliorer le base de calendrier réalisée lors du sprint 1.

### Horodatage


| Date | Heures passées | Indications |
| -------- | -------- |-------- |
| Samedi 14/09  | 2h  | Voir (et comprendre) les différentes façons de faire un calendrier avec Vue.js |
| Dimanche 15/09  | 3h  | Faire un premier calendrier avec V-calendar (et comprendre)|
| Lundi 16/09  | 2h  | Corrections des bugs et amélioration du style |
| Mercredi 18/09  | 2h  | Débuts sur la gestion d'événements |


## Contenu

Il existe plusieurs façons de créer un calendrier avec Vue:
* Avec une bibliothèque dédiée: V-Calendar
* Avec une bibliothèque d'UI: Vuetify
* À partir de zéro

Chaque méthode a ses avantages et inconvénients. Pour commencer, j'ai choisi la première option car plus simple et donc (selon moi) plus adaptée pour débuter.

Tout d'abord on installe v-calendar: `npm install v-calendar`

On importe et configure v-calendar dans le main.js:

```
import { createApp } from 'vue';\
import App from './App.vue';\
import VCalendar from 'v-calendar';\

const app = createApp(App);

app.mount('#app')\
app.use(VCalendar, {})

```

On créer un composant CalendarComponent.vue dans src/components/ puis dans App.vue, on importe ce composant.

App.vue:
```
<template>
  <div id="app">
    <CalendarComponent />
  </div>
</template>

<script>
import CalendarComponent from './components/CalendarComponent.vue';

export default {
  name: 'App',
  components: {
    CalendarComponent,
  },
};
</script>
````

CalendarComponent.vue:
```
<template>
  <div>
    <v-calendar
      is-range
      :attributes="attrs"
      :color="selectedColor"
    />
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import { VCalendar } from 'v-calendar';  
export default defineComponent({
  name: 'CalendarComponent',
  components: {
    VCalendar,  
  },
  data() {
    return {
      attrs: [
        {
          key: 'today',
          highlight: {
            backgroundColor: '#FFDDDD',
            color: '#FF0000',
          },
          dates: new Date(),
        },
      ],
    };
  },
});
</script>

<style>

.vc-calendar {
  border-radius: 8px; 
  background: #fff;
}

.vc-calendar-header {
  background: #ffc5cb; 
  color: #333; 
  font-weight: bold; 
}

.vc-calendar-day {
  color: #333; 
}

.vc-calendar-day.selected {
  background: #ffc5cb; 
  color: #333;
}

</style>
````

Et voilà ca que ça donne:

![Calendrier vue 1](./calendriervue1.png)
![Calendrier vue 2](./calendriervue2.png)


On peut aussi intégrer des bibliothèques de style comme Bootstrap ou Tailwind CSS.

L'un des inconvénients de V-Calendar est qu'il restreint beaucoup; je vais donc voir pour utiliser une autre méthode de création de calendrier lors du sprint 2.

Je souhaite également m'occuper de la gestion des événements sur le calendrier. 

### Sources

[Documentation v-calendar](https://vcalendar.io/getting-started/installation.html)