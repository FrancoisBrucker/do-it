---
layout: layout/pok.njk

title: "POK 3 : Suite site Web en React pour gérer mes tâches"
authors:
  - Kévin BERNARD

date: 2025-01-07

tags:
  - "temps 3"
  - "React"
  - "3D"
  - "Gestion de tâches"
  - "Spring Boot"
  - "Spring Data JPA"
  - "API REST"
  - "React Three Fiber"

résumé: Un POK où je crée un site web attirant en React pour gérer mes tâches avec des animations 3D.
---

{% prerequis %}
Pas de prérequis pour le moment
{% endprerequis %}

{% lien %}
<b>SOURCES</b>
- [Vidéo Youtube de The Ethical Technologist,  ](https://www.youtube.com/watch?v=i63WQrzrKag)
- [Vidéo Youtube de Roberts Dev Talk, Javascript Promises vs Async Await EXPLAINED (in 5 minutes)](https://www.youtube.com/watch?v=li7FzDHYZpc)
- [Vidéo Youtube de Web Dev Simplified, Why I Don’t Use Arrow Functions With const/let](https://www.youtube.com/watch?v=5iGGvJn8K1U)
- [Vidéo Youtube de Web Dev Simplified, Asynchronous Vs Synchronous Programming](https://www.youtube.com/watch?v=Kpn2ajSa92c)
- [GitHub du site, creature_site de KevinBERNARD1901](https://github.com/KevinBERNARD1901/creature_site)

{% endlien %}

{% chemin %}
<b> POK & MON </b>
- [POK 2 : Site Web en React pour gérer mes tâches, Kévin BERNARD](../temps-2/index.md/)
{% endchemin %}

Le but de ce POK est de réaliser un site en React pour gérer mes tâches avec un horodateur, un agenda avec une importation de créatures 3D à partir de Blender.

## Tâches

### Sprints

#### Sprint 1

- [x] Changer l'image de fond
- [] Faire la page de To do (liste des tâches, ajout de tâches, suppression de tâches, chronomètre, marquer comme fait, catégoriser par domaine et par réalisation)
- [x] Rajouter les requêtes API pour les tâches

#### Sprint 2

<!-- - [] Changer les get pour les tâches par réalisation et par domaine ou un seul get et filtrer dans le front
- [] Faire le front la partie front de To do -->

### Horodatage

| Date | Heures passées | Indications |
| -------- | -------- |-------- |
| **Début Sprint 1** |
| Mardi 07/01 | 2H | Ce que je fais en Front + mise en place d'une image en background |
| Vendredi 10/01 | 4H30 | Faire les hooks/appel à l'API + étude fonction fetch + await/async VS then + fonction arrow vs function + sync vs async |
| Samedi 18/01 | 2H | Connection back-front et création méthode post |
| Lundi 20/01 | 2H | Création de Domain.java + Implementation des méthodes HTTP de TO DO (suppression de tâches, chronomètre, marquer comme fait, catégoriser par domaine et par réalisation) |
| Total | 10H30 |

## Contenu

### Premier Sprint

#### Changement de l'image de fond

Dans un premier temps, je voulais avoir un aperçu de ce que donnerais la page finale avec un décor en background donc j'ai importé une image en background issue de Pinsterest, [Image ajouté par Agatha de Lima](https://fr.pinterest.com/pin/10977592835947395/).

J'avais un souci quand je mettais l'image en fond d'écran parce que le RouterProvider faisait en sorte de s'adapter à la taille de mes composants ce qui empêchait l'image d'être en fond d'écran.

Pour corriger cela j'ai défini mes bodys, html, #root comme étant en 100% de la hauteur et de la largeur.

#### Faire la page de To do

##### Connection back-front et création méthode get

Pour connecter mon front à mon back, j'ai utilisé la fonction fetch qui permet de faire des requêtes HTTP. J'aurais pu utiliser Axios mais je ne souhaitais pas apprendre une librairie pour le moment.

Pour intégrer la fonction fetch, j'ai dû apprendre à utiliser les fonctions async et await que j'ai comparé avec then. J'ai regardé une vidéo de [Roberts Dev Talk](https://www.youtube.com/watch?v=li7FzDHYZpc) qui explique la différence entre les promesses et les fonctions async et await.

Ensuite j'ai dû apprendre les différences entre les fonctions fléchées et les fonctions normales parce que j'avais des problèmes avec les fonctions fléchées notamment avec les variables const et let.
J'ai regardé une vidéo de [Web Dev Simplified](https://www.youtube.com/watch?v=5iGGvJn8K1U) qui explique pourquoi il ne faut pas utiliser les fonctions fléchées avec const et let.

J'ai enfin pu créer une méthode post pour créer une tâche dans ma base de données et j'ai pu appelé la méthode get dans mon front, c'est là que j'ai créé le composant Task.js.

##### Création de Domain.java + Implementation des méthodes HTTP de TO DO

J'avais déjà créé la méthode post pour créer une tâche et get pour avoir la liste des tâches.
J'ai donc créé les méthodes delete et patch pour marquer une tâche comme faite, supprimer une tâche, ajouter le temps passé sur cette tâche et catégoriser par domaine et par réalisation.

Pour cela, j'ai d'abord ajouté les attributs (à partir du diagramme de classe de mon [POK 2]()) :

```java
    private LocalTime timePassedOnIt;
    private LocalTime totalTime;
    private Date creationDate;
    private Date doneDate;
    @ManyToOne
    @JoinColumn(name = "domainId")
    private Domain projectDomain;
```

Pour les domaines, j'ai créé une classe Domain.java qui contient un domainId, name, domainDone, creationDate, doneDate et color. Ensuite j'ai ajouté un attribut projectDomain dans Task.java qui est une clé étrangère vers Domain avec un ManyToOne et un JoinColumn pour spécifier le nom de la colonne.

J'ai rajouté mes méthodes patch et delete dans mon TaskController.java et j'ai pu les appeler dans mon front. Sachant que PatchTaskTime_passed_on_it ajoute la durée envoyée en paramètre à la durée déjà passée sur la tâche et PatchTaskTotal_time remplace la durée totale par la durée envoyée en paramètre.

{% details "Code" %}

```java
// DeleteMapping
    @DeleteMapping("/tasks/{taskId}")
    public void deleteTaskByID(@PathVariable int taskId) {
        taskService.deleteById(taskId);
    }

    // PatchMapping
    @PatchMapping("/tasks/taskDone/{taskId}")
    public void PatchTaskTaskDone(@PathVariable int taskId) {
        taskService.patchTaskTaskDone(taskId);
    }

    @PatchMapping("tasks/timePassedOnIt/{taskId}")
    public void PatchTaskTime_passed_on_it(@PathVariable int taskId, @RequestParam LocalTime timePassedOnIt) {
        taskService.PatchTaskTime_passed_on_it(taskId, timePassedOnIt);
    }

    @PatchMapping("tasks/totalTime/{taskId}")
    public void PatchTaskTotal_time(@PathVariable int taskId, @RequestParam LocalTime totalTime) {
        taskService.patchTaskTotal_time(taskId, totalTime);
    }
```

{% enddetails %}

J'ai également mis plusieurs routes get pour récupérer les tâches par réalisation et par domaine. Je n'ai pas encore réfléchi s'il vaut mieux par exemple: faire une route pour chaque domaine ou une route pour tous les domaines et filtrer dans le front.

### Second Sprint

### Retour sur expérience