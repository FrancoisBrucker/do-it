---
layout: layout/pok.njk

title: "POK1 - Étude d'un système d'information complexe"
authors:
  - Schultz Mathis

date: 2023-10-18

tags: 
  - "temps 1"
  - "système d'information"

résumé: Le but de ce POK est de faire l'étude du système d'information d'une multinationale.
---

<h2 id="h1"> Introduction </h2>

Pour mettre à profit mes connaissances préliminaires sur les systèmes d'informations, je vais vous proposer une analyse d'un système très complexe, opérationnel et en constante évolution, dans ce POK, le nom du système d'information a été anonymisé.

{% info "Approche préliminaire" %}
Mon analyse n'est que préliminaire et ne permet pas de tirer de quelconque conclusion.
{% endinfo %}

<h2 id="toc"> Table des matières </h2>

- [Introduction](#h1)
- [Table des matières](#toc)
- [Organisation des sprints](#sprint)
- [Quel est le rôle de cette super-application](#h1-1)
- [Approche utilisé](#h1-2)
- [Un outil habilitant](#h2)
- [Un outil coercitif](#h3)
- [Etat actuel](#h4)
- [Conclusion](#h5)
- [Liens utiles](#liens)

<h2 id="sprint"> Organisation des sprints </h2>

**Sprint 1**

- Accéder aux données : demander les droits auprès de l'entreprise.
- Création des comptes utilisateurs.
- demande pour obtenir une tablette avec connexion sécurisé au site.
- Découverte du site et des ressources à disposition.
- relecture de la part d'un manager.

**Sprint 2**

- Continuer à découvrir les informations à disposition.
- interroger des collègues sur leur rapport à l'outil.
- Anonymisation des données publiées.
- Réalisation de diagramme à partir de bride de document texte.
- Blocage lié à des droits administrateurs que je n'avais pas.
- Relecture de la part d'un manager.
- Certains paragraphes sont encore en suspend ou on été refusé.

<h2 id="h1-1"> Quel est le rôle de cette super-application </h2>

Le rôle du système est de rassembler l'ensemble des outils informatiques qu'utilise les différents organes. Les intérêts sont variés et propre à chaque acteurs :

- faciliter les rapports de chantier.
- Aider la transmission d'information au service de comptabilité.
- Aider au management des équipes.
- ...

Le but de l'application est de faire le lien entre tous les outils de chaque acteurs.

<img src="structure.webp">  

*Différents acteurs au sein d'un groupe de travaux public*

**Voici un exemple d'application de la plate-forme :**

Le but est d'analyser le trajet d'une donnée lorsqu'un chef de chantier effectue une demande de ressource pour son chantier. Voici un diagramme montrant le trajet et l'exploitation de la demande :

<img src="exemple_interaction.webp">

*Diagramme du traitement d'une commande*

<img src="achat.webp">

*Diagramme plus détaillé du traitement du commande, source : google image*

<h2 id="h1-1"> Approche utilisé </h2>

Afin de débuter mon analyse, je me suis donc rapproché de mon tuteur et du service informatique du groupe. Les démarches sont longues et ne me donnent que peu d'accès mais permettent de visualiser l'intérêt de l'uniformisation de la donnée.
Pour des raisons de confidentialités lié à la publication du fonctionnement de l'application, mais aussi lié à mon statu d'apprenti qui ne me donne malheureusement pas un plein accès au code de l'application, les démarches pour accéder aux informations me prennent du temps, je n'aurai dans cette étude qu'un accès à une partie de l'interface utilisateur :

- accès aux fonctionnalités de chefs de chantier et de rapport
- accès aux fonctionnalités de conducteur de travaux
- accès à la documentation de la structure de l'application
- accès à l'interface Ressource Humaine

Cela ne représente que 3 des 17 acteurs en jeux dans le fonctionnement de l'application.

<h2 id="h2"> Un outil habilitant </h2>

Dans ce paragraphe nous allons nous intéresser aux différents bénéfices qu'apporte cette plateforme.  
Tout d'abord d'un point de vue globale cette application permet aux différents managers à différentes échelles de suivre les projets, leur avancement ainsi que leurs résultats.  
Cet outil favorise la reproductibilité, en effet, aujourd'hui lorsque le groupe souhaite ouvrir une nouvelle agence il suffit de faire venir des collaborateurs qui sont déjà formé sur les outils, il y a une facilité pour changer de secteur puisque ces outils sont commun dans tout le groupe.  
Il y a une simplification de certain processus avec l'automation de certaines tâches : les bons de commandes qui sont directement transmis aux comptables des différents organisme avec une nomenclature uniformisé qui permet de faire le lien d'un organe à un autre.

<h2 id="h3"> Un outil coercitif </h2>

Le but de ce paragraphe est de mettre en lumière les aspects négatifs de cet outil.

**Un enjeu social**

Une transition difficile, en effet, cet outil a demandé un effort complémentaire pour prendre la main sur le système et être capable de réaliser les missions nécessaire. Ce service présenté comme étant une révolution pour faciliter le travail permet effectivement une gestion d'une grosse structure facilement avec beaucoup d'indicateur de performance afin de prendre des décision stratégique efficace, cependant ce genre d'application n'a pas tendance à faciliter la gestion à petite échelle. Traditionnellement, le manager récoltait les informations afin de faire des rapports qui étaient donc très échelonner. Actuellement, il est possible d'outre-passer chaque rapport puisque le haut de la pyramide à donc accès à l'ensemble de l'information sans avoir tout l'aspect social. Si une équipe sous-performe pour une raison qui est indépendante de leur volonté, cela n'est pas forcément visible au travers des données des rapports. A l'inverse un rapport traditionnel permet de transmettre les raisons des échecs : une météo instable, une grève d'un fournisseur... Tout ces facteurs ne sont pas visible pour celui qui traite la data sans avoir de lien humain avec les échelons qu'il dirige.  

Une perte de lien entre les collaborateurs; l'efficacité qu'apporte ce système en transmettant automatiquement les documents vient réduire le nombre d’interactions. Par exemple les comptables ne devrons plus aller collecter les bons auprès des collaborateurs. Les échanges se limiteront aux cas où un problème surviendrait.  

La segmentation et l'automation de processus à tendance à réduire l'étendu de compétence de l'employé qui remplit le formulaire. En effet face à un choix limité, l'appel aux connaissances est plus restreinte.

Une place fixe, n'ayant que des accès limités à la plate-forme, il n'y a que trop peu de recul sur l'outil, chacun a accès à des données qui lui sont ciblés : des formations ou document n’explicitant que sa part du travail. Ce qui permet d'éviter que n'importe qui puisse compromettre l'entreprise, qu'il y ait des doubles contrôles et faciliter l'accès vers les données pertinentes des utilisateurs. Cependant, ce cadre très restreint empêche que les utilisateurs comprennent pourquoi il réalise tel ou tel action. En effet, un chef qui ne comprend pas l'intérêt de remplir un rapport va avoir tendance à le bâcler, ce qui va compromettre le travail des comptables et créer des tensions.

**Un enjeu environnemental** 

La digitalisation et la dématérialisation des processus. L'utilisation de Cloud, de tablette ou autre support informatique en vue de dématérialiser à tendance à augmenter l'impact environnemental : en effet, ce type d'outil à pour objectif de maximiser les traces de chaque opérations, et ces traces sont conservés sur des durées infiniment trop longue. Il est possible de retrouver le bon de commande de l'utilisation d'un camion il y a plusieurs années sur un chantier achevé depuis longtemps.

**Un enjeu de design** 

Un design en constante évolution, en effet, tout d'abord il faut prendre en considération les évolutions du travail. Les équipes et matériels évoluent régulièrement. Cela impose au manager de mettre à jour les bases de données afin que chaque partie ait accès à des informations fiable. Cependant un enjeu plus complexe est celui de la mise à jour des techniques. En effet, dans le cas d'une évolution de procédé il faut faire évoluer la structure de l'application. Cela est donc fait par un sous-traitant qui va reprendre les procédés. Cette dépendance a un coût élevé mais permet de continuer d'utiliser l'outil. Tout l'enjeu est donc d'avoir une application qui permette de réduire les coûts en optimisant les procédés tout en restant moins cher que le coût d'exploitation de l'application. Ce service a donc pour vocation d'avoir la plus grosse structure possible. En effet lorsque l'on recherche des optimisations sur les procédés via l'utilisation de ce genre de ressource de management cela a pour but de permettre de la gestion uniforme de grande masse.  

Cette application a pour but d'uniformiser la data, c'est à dire que si quelqu'un est affecté à un chantier, alors il va apparaîtra sur ce chantier pour les autres services : le service RH pourra identifier les activités de chacun, les mangers peuvent suivre les performance des chefs au cours du temps ou des chantiers. L'enjeu est donc la création de trace qui permet de retracer exactement les évènements et remettre la faute précisément sur un employé en cas de besoin managériale : il est facile de retrouver où une information à bloqué, ou alors qu'elle décision à compromis le projet.

**Un enjeu économique**

D'un point de vue économique le système a tendance à optimiser les performances d'entreprise, cependant ce système s'installe comme une dépense mensuelle indispensable et éternelle pour l'entreprise, en plus du coût des outils numériques.  
Il est nécessaire d'acheter :

- Une tablette par chefs de chantier pour rédiger le rapport
- Un téléphone d'entreprise pour chaque chefs et cadres
- Des serveurs & un service de cloud pour accéder aux datas sur chantier
- Des forfaits téléphoniques élevés pour l'accès internet afin d'effectuer les rapports journalier.
- Une structure d'appuie technologique pour entretenir le parc informatique, s'assurer de l'intégrité des datas, de la sécurité informatique.

<h2 id="h4"> Etat actuel </h2>

Aujourd'hui, l'application est indispensable, et s'en défaire n'est pas possible tant les outils ont été perfectionné et tant le travail des utilisateurs a été adapté à ce système. L'application semble dans l'ensemble bien accepté, chacun en perçoit une partie de l'intérêt. Je trouve un lien assez fort entre le statut hiérarchique et l'intérêt perçu. En effet, plus on a accès, plus on trouve l'intérêt du système mais plus il y a une demande de rigueur. Celui qui a une vue d'ensemble va rechercher à ce que chacun fasse le plus proprement possible son travail car il perçoit l'impacte d'un travail bâclé. A l'inverse celui qui rempli des formulaires sans comprendre l'intérêt de l'information ne va pas réaliser ses missions avec attention et risque de faire des fautes de frappes qui amèneront un stress supplémentaire. Globalement l'explication de l'étendu du système permet d'engager ses utilisateurs dans de la rigueur et apaise le travail.

<h2 id="h5"> Conclusion </h2>

Le plus difficile pour moi a été de m'y retrouver avec toutes les informations à disposition. En effet, de nombreux documents expliquent comment un employé doit utiliser son logiciel mais peu de ressource explique le fonctionnement profond du logiciel. Ou alors ces documents ne sont pas accessible. De plus les temps de relecture ralentissent considérablement mon travail puisque je dois me rendre au bureau pour valider avec mon tuteur les idées développées.

<h2 id="liens"> Liens utiles </h2>

Comme les informations sont tirées de documents internes, aucune source n'est spécifiée.
