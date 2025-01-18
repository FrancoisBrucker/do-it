---
layout: layout/pok.njk

title: "Plateforme de certification en ligne"
authors:
  - Serigne Mbaye Sy AMAR

date: 2024-16-09

tags: 
  - "développement web"
  - "Laravel "

résumé: Un POK traitant de la création d'une plateforme de certification en ligne où les utilisateurs peuvent suivre des cours en vidéo et obtenir un certificat après évaluation.

---
{% prerequis %}

- Avoir des connaissances en développement web (HTML, CSS, JavaScript).
- Connaître le framework back-end Laravel.
- Des bases en bases de données (MySQL).
- Connaître l'utilisation de systèmes de gestion des utilisateurs et d'authentification.

{% endprerequis %}

{% lien %}

[Les lien utiles pour la compréhension de celui-ci.](https://laravel.com/docs/10.x)

{% endlien %}

<style>
   .hint {
  background-color: #e2f0d9;
  color: #155724;
  padding: 15px;
  border-left: 5px solid #c3e6cb;
  border-radius: 4px;
  margin-bottom: 15px;
}
.tip {
  background-color: #fff3cd;
  color: #856404;
  padding: 15px;
  border-left: 5px solid #ffeeba;
  border-radius: 4px;
  margin-bottom: 15px;
}
  </style>
## Table des matières
1. [Pourquoi créer une plateforme d'apprentissage en ligne ?](#section-1)
2. [Pourquoi utiliser Laravel pour une telle plateforme ?](#section-2)
3. [Tâches](#section-3)
4. [Résultats ](#section-4)

   
## Pourquoi créer une plateforme d'apprentissage en ligne 🌍📚?

Dans un monde où l'éducation et le développement personnel sont de plus en plus numérisés, la création d'une plateforme d'apprentissage en ligne présente de nombreux avantages. Elle permet de démocratiser l'accès à la connaissance, de briser les barrières géographiques et de permettre à quiconque, où qu'il soit, d'accéder à des formations de qualité. Voici quelques raisons clés pour lesquelles ce projet est non seulement pertinent, mais également porteur d'avenir.

   D'abord une plateforme de cours en ligne permet aux étudiants du monde entier d'accéder à des connaissances spécialisées. Que ce soit pour des étudiants dans des régions reculées ou pour des professionnels qui cherchent à acquérir de nouvelles compétences, ce type de plateforme est un levier pour la formation continue.
  
   Ensuite, contrairement aux méthodes traditionnelles d'enseignement, une plateforme en ligne permet aux apprenants de progresser à leur rythme. Ils peuvent visionner des vidéos, revoir des leçons et passer des évaluations selon leur propre emploi du temps, rendant l'apprentissage flexible et adapté aux besoins de chacun.
 
   Enfin, grâce à la flexibilité de la plateforme, le contenu peut être mis à jour régulièrement. De nouveaux cours peuvent être ajoutés, permettant aux étudiants d'accéder aux dernières innovations dans leur domaine. L'apprentissage devient ainsi un processus continu, en phase avec les évolutions du marché.

[Voici un article sur les plaformes de certifications en ligne](https://bienvenum.org/plateforme-de-formation-en-ligne/#:~:text=Elles%20permettent%20aux%20apprenants%20d,et%20adapt%C3%A9%20%C3%A0%20chaque%20individu).

---

## Pourquoi utiliser Laravel pour une telle plateforme 🖥️⚙️?

Laravel, un des frameworks PHP les plus populaires, est un bon choix pour le développement d'une telle plateforme. C'est grace a ces raison qu'il est un bon choix:

1. **Sécurité renforcée**  

2. **Système d'authentification intégré**  
  
3. **Flexibilité et évolutivité**  
   
4. **Écosystème riche**  
   
5. **Architecture MVC claire**  
  
6. **Gestion des bases de données simplifiée**  
   
   [Voici un tutoriel rapide sur Laravel](https://grafikart.fr/tutoriels/introduction-laravel-2112#autoplay)

---

## Tâches 📝✅
L'objectif de ce projet est de créer une plateforme en ligne où les étudiants peuvent suivre des cours en vidéo et passer une évaluation pour obtenir un certificat. Les instructeurs peuvent s'inscrire, et une fois approuvés par le super administrateur, ils peuvent ajouter des cours. Le projet est divisé en deux sprints pour structurer les étapes de développement.


#### Sprint 1 :

Ce sprint est dédié à la création de l'interface utilisateur de la plateforme et la mise en place des systèmes d'authentification et des droits d'accès pour les différents rôles (étudiant, instructeur, super admin). Les tâches incluent la conception des pages et l'intégration du frontend.

| Tâche                                           | Durée estimée |
|------------------------------------------------|---------------|
| Développer les pages d'accueil                    | 4h            |
| Créer les formulaires d'inscription            | 1h            |
| Mettre en place la structure des pages vidéos  | 3h            |
| Implémenter le système d'authentification      | 2h            |


***Étude post-mortem :***  
À la fin de ce sprint, Je vais évaler la fonctionnalité des pages développées et corriger les bugs éventuels.


***À la fin de du sprint***

- [x] Développer les pages d'accueil   

- [x] Créer les formulaires d'inscription   

- [x] Mettre en place la structure des pages vidéos   

- [x] Implémenter le système d'authentification  
   
#### Sprint 2 : 

Ce sprint est dédié à l'ajout de fonctionnalités permettant aux instructeurs de créer des cours, aux étudiants de les suivre et de passer des évaluations.
| Tâche                                      | Durée estimée |
|-------------------------------------------|---------------|
| Développer un tableau de bord(Toutes les pages visibles) pour les admins  | 4h            |
| Assurer la sécurité             | 1h30            |
| Permettre la création de cours(gérer les permissions)  | 2h            |
| Intégrer un lecteur vidéo                  | 1h30            |
| Recherche sur le systeme de payement       | 1h            |

***À la fin de du sprint***
- [x] Développer un tableau de bord(Toutes les pages visibles) pour les admins
  
- [x] Assurer la sécurité
  
- [x] Permettre la création de cours(gérer les permissions)
  
- [x] Intégrer un lecteur vidéo 
  
- [x] Recherche sur le systeme de payement
  
- [ ] Implémentation d'un filtre de recherche par catégorie pour les cours (non terminé). 

- [ ] Liaison correcte pour le paiement en ligne  

- [ ] Gestion de la progression de l'étudiant dans la base de données (non terminé). 
  
***Étude post-mortem :***  
Je vais évaler la fluidité de la gestion des cours et ajuster les problèmes liés à la gestion des données.

---

## Résultats 
Pour avoir une meilleure présentation des résultats, j'ai téléchargé l'extension [Simulateur téléphone mobile - test site responsive](https://www.webmobilefirst.com/).

<div class="tip">
  <strong>🎯</strong> J'ai nommé la plateforme Skills Proof pour faire référence au POK.
</div>


<div class="hint">
  <strong>💡</strong> Vous allez tomber sur cette page d'accueil à l'ouverture de la plateforme. Cette page, représentant la page d'accueil, a pour but de présenter la plateforme dans sa globalité et est dédiée aux étudiants et aux instructeurs.
</div>

{% details "Page d'accueil"%}
<img src="images/1.webp" alt="image" />

<img src="images/1a.webp" alt="image" />

<img src="images/1b.webp" alt="image" />

<img src="images/1c.webp" alt="image" />


<img src="images/1d.webp" alt="image" />

<img src="images/1dd.webp" alt="image" />

<img src="images/1f.webp" alt="image" />
{%enddetails%}



<div class="hint">
  <strong>💡</strong> Après cette page d'accueil, l'élève peut aussi consulter les cours disponibles. Il est censé faire également une sorte de filtre par catégorie, mais je n'ai pas encore réussi à l'implémenter.
</div>

{% details "Les cours disponibles"%}
<img src="images/1g.webp" alt="image" />
{%enddetails%}

<div class="hint">
  <strong>💡</strong> Ainsi, s'il trouve un cours qui l'intéresse, il doit se connecter et s'inscrire au cours.
</div>

{% details "Connexion"%}
<img src="images/2.webp" alt="image" />
{%enddetails%}



<div class="hint">
  <strong>💡</strong> Ici, l'étudiant va ajouter le cours dans son panier, qui s'incrémente automatiquement.
</div>

{% details "Ajouter le cours dans son panier"%}
<img src="images/entre1.webp" alt="image" />
{%enddetails%}

<div class="hint">
  <strong>💡</strong> Il sera redirigé ici lorsqu'il clique sur son panier pour finaliser sa commande.

Là, je n'ai pas réussi à lier correctement le paiement en ligne, même si j'ai essayé de l'implémenter avec Sandbox Payment System, qui n'est pas un système français. Mais cela n'a pas abouti, donc j'aimerais essayer d'implémenter les méthodes françaises comme Paylib ou PayPal.
</div>
{% details "Finalisatioon commande"%}
<img src="images/entre2.webp" alt="image" />
{%enddetails%}

<div class="hint">
  <strong>💡</strong> En supposant que l'étudiant a payé, il verra sur son tableau de bord qu'il s'est inscrit à un cours.
</div>
{% details "Tableau de bord de l'étudiant"%}
<img src="images/3.webp" alt="image" />

<img src="images/4.webp" alt="image" />
{%enddetails%}

<div class="hint">
  <strong>💡</strong> S'il clique sur le cours, il verra la vidéo avec les leçons qu'il devra cocher chaque fois qu'il en termine une. Je n'ai pas fini le développement, mais je dois faire en sorte qu'à chaque fois qu'il coche un cours, je mette à jour sa progression dans la base de données.
</div>
{% details "Contenu du cours"%}
<img src="images/6.webp" alt="image" />
{%enddetails%}

<div class="hint">
  <strong>💡</strong> Maintenant, du côté admin, je vais essayer de me connecter en premier lieu comme admin simple (instructeur). 
</div>
{% details "Comme instructeur"%}
<img src="images/7.webp" alt="image" />
{%enddetails%}


<div class="hint">
  <strong>💡</strong> Sur la page d'accueil, il verra toutes les données concernant les cours (nombre d'élèves, nombre de cours) et leur évolution. Mais pour le moment, les données qui y sont sont statiques ; je n'ai pas pu les implémenter. Il s'agit juste d'une récupération de données, mais il y a beaucoup d'autres choses plus intéressantes et utiles à mettre en place sur les 20h à venir. Mais ce que je veux montrer ici, c'est qu'en tant qu'instructeur, il n'est pas permis de visiter la liste des instructeurs, d'ajouter, supprimer, etc. Quand il essaie, il voit un message en haut lui montrant cela. Ce qu'il peut faire, c'est uniquement ce qui le concerne (les cours, quizz, etc.).
</div>
{% details "Page d'accueil admin"%}
<img src="images/8.webp" alt="image" />
{%enddetails%}


<div class="hint">
  <strong>💡</strong> Si on se connecte maintenant avec le compte du super admin, on peut tout faire. Ici, c'est un enchaînement d'écrans où j'ai visité les pages une par une. Mais il y a d'autres pages que j'ai déjà développées, comme l'attribution des permissions (les rôles), l'ajout des quizz et leurs réponses, etc., que je n'ai pas encore mises sur le tableau de bord. Elles sont accessibles juste en tapant la route (le lien) pour le moment.
</div>
{% details "Dashbord super admin"%}
<img src="images/9.webp" alt="image" />

<img src="images/10.webp" alt="image" />

<img src="images/11.webp" alt="image" />

<img src="images/12.webp" alt="image" />

<img src="images/13.webp" alt="image" />

<img src="images/14.webp" alt="image" />

<img src="images/dernier.webp" alt="image" />

<img src="images/nondernier.webp" alt="image" />
{%enddetails%}


## Conclusion
Je termine en rappelant que le but de ce projet est de mettre en valeur mes compétences en Laravel, surtout avec la méthode CRUD, car presque la totalité du développement consiste à Créer, Lire, Modifier et Supprimer je voulais aussi renforcer mes compétences en développement frontend. Donc je peux dire que j'ai appris énormément de choses qui me donnent plus de confiance avec ce framework.
Vous trouverez le code source sur mon GitHub dont [voici le lien](https://github.com/MbayeSyAmar/skillsproof.git)