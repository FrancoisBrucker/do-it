---
layout: layout/pok.njk

title: "POK 1 - VBA, fais-le pour moi"
authors:
  - Victor Pawlaczyk

date: 2024-09-01

tags:
  - "temps 1"
  - "Vert"
  - "VBA"

résumé: Au travail, certains collègues doivent effectuer des tâches qui me semblent plutôt basiques et surtout très répétitives sur Excel. Le but de ce POK est donc d’essayer d’utiliser les VBA pour automatiser certaines de ces tâches.
---

{% prerequis %}

Connaissances de base en VBA

{% endprerequis %}
{% lien %}

Les lien utiles pour la compréhension de celui-ci.

{% endlien %}

## Tâches

### Sprint 1

Liste des taches que l'on pense faire. On coche si la tache est réalisée. A la fin du sprint on fait une petite étude post-mortem pour voir ce qui s'est passé et les ajustement à faire pour le prochain sprint, pok.

- [x] Répertorier des tâches répétitives que mes collègues aimeraient voir automatisées
- [x] Sonder des connaissances et/ou internet pour avoir des retours d'expériences sur ce genre de projets
- [x] De l'idéation à la conception : comment techniquement j'imagine que les demandes identifiées puissent être automatisées ?
- [x] Choisir un premier exemple concret d'automatisation, faire une maquette
- [x] Test de la maquette, réaction de mes collègues/retour d'expérience
- [ ] Codage du programme VBA à partir de la maquette, et des retours reçus
- [ ] Test de ce programme

### Sprint 2

- [x] Continuer le codage du programme du Sprint 1
- [x] Test de ce programme + correction des bugs
- [x] identification de ses faiblesses ou des améliorations possibles
- [x] Correction des faiblesses, amélioration du programme
- [x] Codage d'un autre programme qui réponde à une autre des demandes identifiées
- [x] Test de ce programme + correction des bugs
- [x] identification de ses faiblesses ou des améliorations possibles
- [x] Correction des faiblesses, amélioration du programme

### Horodatage

Premier Sprint :

| Date | Heures passées | Indications |
| -------- | -------- |-------- |
| Jeudi 05/09  | 1H  | Echanges avec Corinne, identification de ses besoins |
| Vendredi 06/09  | 1H  | Retours d'expérience |
| lundi 09/09  | 3H  | Recherche de moyens techniques de répondre à la demande + élaboration de la maquette |
| Mercredi 11/09  | 1H  | Présentation de la maquette |
| Lundi 16/09  | 2H  | Analyse des retours sur la maquette + codage VBA |
| Lundi 16/09  | 30 min  | Analyse du Sprint + réflexion sur le prochain Sprint |
| Lundi 16/09 | 1H30 | Rédaction livrable |

Deuxième Sprint :

| Date | Heures passées | Indications |
| -------- | -------- |-------- |
| vendredi 04/10  | 3H  | Codage |
| dimanche 06/10  | 2H  | Codage |
| jeudi 10/10  | 1H  | Présentation avec Corinne + correction des bugs |
| lundi 14/10  | 2H 30  | Essai recherche + codage remplissage des formulaires pdf |
| mardi 15/10  | 1H  | Rédaction livrable |

## Premier Sprint

### Identification des tâches à automatiser

La première étape consiste à échanger avec mes collègues sur leur utilisation quotidienne d'Excel et leurs tâches récurrentes pour identifier les tâches qui pourraient être automatisées ou simplifiées avec des macros. C'est avec Corinne que j'ai identifié différentes manipulations à automatiser.

En résultat de ces échanges et réflexions, voici les objectifs possibles d'automatisation que nous avons identifiés :

- La saisie de devis sur Excel à partir des extractions faites d'un progiciel interne
- La vérification des documents administratifs du personnel présent sur le chantier
- Le suivi des demandes de badge d'accès au site
- les demandes de badges hebdomadaires pour les véhicules.

### Retours d'expériences de projets similaires

Ensuite j'ai recherché dans mon entourage mais aussi sur internet quelques retours d'expérience sur ce type de projets avec du VBA. Les principaux points d'attention qui résultent de ces retours d'expérience sont les suivants :

- Il faut fait attention à l'utilisateur final de l'outil que l'on met au point au cours du projet. Souvent, l'utilisateur final de l'outil n'est pas forcément à l'aise avec l'informatique et ce genre de programmes et de macros peuvent les perdre plus que les aider réellement.
- Parfois, le codage de la macro cause plus de prise de tête qu'il n'apporte de gain réel une fois au point.
- Il ne faut pas négliger la partie "design thinking". Si la macro n'est pas faite pour n'être utilisée qu'à titre personnel, il faut être vigilant à ne pas partir trop loin tête baissée dans le codage sans vérifier régulièrement que le résultat corresponde réellement aux attentes de(s) l'utilisateur(s) visé(s).

### Ma Phase d'idéation

Pour le sujet de saisie des devis, j'ai pensé à coder une macro de mise en forme des données. C’est la solution qui me paraît intéressante à creuser. En effet, il est possible d’extraire les données depuis le logiciel où arrivent les devis, les bons de commande et les factures. On peut facilement faire un copier-coller depuis cette extraction vers un excel. Le souci c’est que toutes les informations récupérées ne sont pas forcément pertinentes, il y a des colonnes en trop, d’autres pas dans le bon ordre, etc. C’est une perte de temps considérable de remettre à chaque fois ces données copiées dans une mise en forme exploitable pour l’utilisation qu’on veut avoir de ce tableur. Une première piste à creuser est donc une macro qui automatise cette mise en forme des tableaux à partir des extractions du logiciel.

Pour la vérification des documents administratifs, on a déjà mis en place un tableau dans lequel on renseigne la date d’expiration du document valide que l’on a plutôt que simplement indiquer s’il est « ok » ou non à la saisie du dossier. Aujourd’hui, ma collègue doit régulièrement vérifier ligne à ligne si les documents que l’on a sont toujours valides. En fonction du nombre d’ouvriers présents, cela peut être rapide comme très long. Il serait intéressant de mettre en place un bouton qui lance une macro de « vérification des documents à jours » qui renverrai à la fin une message box indiquant que toutes les pièces d’identité sont valides ou alors celles qui sont périmées le cas échéant (idem pour les visites médicales, etc). Cela rendrait la vérification beaucoup plus efficace. Il serait aussi intéressant de lister les données manquantes dans le tableau.

Pour les demandes de badge, on renseigne déjà la date à laquelle la demande a été faite, puis quand elle est acceptée on le renseigne aussi. Encore une fois, il serait sympa qu’un bouton associé à une macro recherche seul parmi tout le tableau les demandes qui ont été envoyées mais pas encore acceptées, pour savoir quels cas posent « problème » et faciliter les relances au bureau des badges.

### Le Maquettage

Pour commencer, avant de me lancer tête baissée dans le codage en VBA de programmes hyper compliqués et complets, il m’a semblé important de tester l’adhésion du public visé à la solution envisagée. J’ai donc en étape intermédiaire utilisé des fonctions excel que je connaissais un peu mieux pour faire des premiers tests de mes idées à ma collègue Corinne. Pour ce début j’ai commencé à travailler sur le suivi des documents administratifs. J’ai amélioré un peu le tableau existant pour commencer à y automatiser certaines vérifications, notamment la validité des pièces d’identité. J’ai commencé par ajouter une colonne de test qui compare la date de validité du document à la date du jour. Cette colonne renvoie vrai ou faux. En ajoutant une mise en forme conditionnelle verte ou rouge, j’ai pu voir que Corinne pouvait vérifier beaucoup plus rapidement si tout était encore valide. Mais elle doit encore parcourir elle-même tout le tableau.

Voici le retour d'expérience obtenu de cette maquette :

- Corinne m’a suggéré d’ajouter un intermédiaire « se périme bientôt » en plus des catégories "valide" et "périmé", comme ça elle peut mettre en garde les ouvriers concernés et leur boîte d’intérim.
- « Oh, tu pourrais me faire ça aussi avec les visites médicales ? »
- « Tu crois que ça pourrait mettre à jour les dates de contrat des intérims tout seul aussi » (-> Nouveau défi !)

### Analyse Post Mortem du Sprint

Je n'ai pas réalisé l'intégralité de ce que j'avais initialement prévu pour le premier sprint étant donné qu'à ce stade, je n'ai pas encore réussi à coder une solution viable en VBA pour répondre à un des problèmes efficacement. Le codage est en cours. Cela constituera le coeur du second sprint qui était déjà prévu de la sorte.

## Second Sprint

### La vérification des documents administratifs

Le début de ce second sprint consistait à coder, dans la continuité du premier sprint, la macro de vérification des documents administratifs. Sur un plan technique, cette phase m'a permis de me rendre compte que les array étaient assez contraignants à utiliser en vba. Par exemple, quand on définit un array dynamique, il faut en réalité redéfinir sa dimension en permanence, je n'ai pas trouver de moyen d'ajouter des items à la suite de l'array sans devoir l'agrandir au préalable (une sorte d'équivalent de ".append" en python). De plus, il n'est pas possible de renvoyer un array via une "message box". In fine, il s'est avéré beaucoup plus pratique dans ce cas précis d'utiliser une chaîne de caractère à la place pour concaténer à la suite les noms des profils incomplets ou à litige. Par souci de clarté, j'ai souhaité intégrer des retours à la ligne dans ma chaîne de caractère, ce qui se traduit par la commande suivante "vbCrLf".

Une fois le programme de vérification de validité des cartes d'identité et des visites médicales codé, j'ai pu le montrer à ma collègue Corinne. On a pu vérifier à nouveau que le programme fonctionnait et lui convenait. Ensuite, j'ai ajouté la macro en question sur le vrai tableur qu'elle utilise et non pas ma copie qui me servait de test. J'ai eu quelques bugs lors de la liaison du bouton avec la macro, mais ça a finalement fonctionné. Avant de faire cette présentation à Corinne, j'avais eu le temps aussi de programmer une autre macro qui vérifiait la validité des contrats des intérimaires en fonction des dates renseignées dans le fichier excel. Cette dernière a aussi plu à ma collègue et répond bien à son besoin.

### La saisie des devis

Cette partie était relativement simple à coder. Il s'agissait simplement jouer sur la mise en page du tableau extrait. Pour autant c'était intéressant de se pencher sur la question car celà m'a permis de manipuler un peu les différentes commandes de mise en page via vba. Ainsi j'ai pu mettre en application toute une partie de ce que j'avais appris lors de mon premier MON sur vba.

### Les badges

En ce qui concerne les deux sujets identifiés sur les badges, il s'est finalement avéré peu pertinent d'utiliser vba dans ces deux cas. Pour le suivi des demandes de badge, le code aurait été très similaire à celui des CNI et des visites médicales car il s'agit encore de comparer des dates. En revanche, le programme n'est plus pertinent à mettre en place étant donné que les demandes de badges d'accès se rarifient avec l'avancée du chantier. En effet, il y en avait énormément au départ mais maintenant les accès sont faits et les équipes sont globalement stables.

Concernant les badges véhicules, l'idée aurait été de réussir à modifier à l'aide de vba un formulaire pdf. D'après mes recherches, cela semble faisable. Cependant, la license d'Adobe Acrobat fournie par mon entreprise ne contenait malheureusement pas la bibliothèque nécessaire "Adobe Acrobat Type Library". J'ai vu que d'autres bibliothèques pouvaient permettre d'effectuer ce genre d'interaction comme itext mais, même si cette bibliothèque me permettait d'arriver à mes fins, il aurait fallu l'installer sur mon PC pro et celui de ma collègue. Je voyais venir la source de problèmes plus que la solution miracle. Ce fut le moment pour moi de me souvenir du retour d'expérience récurrent relevé pendant le premier sprint, à savoir : "Parfois, le codage de la macro cause plus de prise de tête qu'il n'apporte de gain réel une fois au point." Pour autant, explorer le sujet m'a déjà permis d'apprendre que l'on pouvait modifier des pdf à formulaires via un programme vba. De plus, je suis à présent d'autant plus curieux d'explorer les différentes manières qui peuvent exister pour "automatiser" le remplissage de ce type de formulaires facilement.

### Le projet Bonus

Après avoir commencé à manipuler les macros excel, et étant en plein dans le codage de celles présentées ci-dessus, j'étais beaucoup plus attentif aux tâches qui se prêtaient bien à une automatisation via vba. C'est alors que je me suis rendu compte qu'un des fichiers de synthèse que l'on remplit régulièrement pouvait être un très bon sujet pour compléter ce POK et manipuler encore un peu vba. En effet, c'est un fichier excel qui vise à synthétiser sur une feuille de calcul les données présentes sur une dizaine d'autres feuilles identiques que l'on crée au fur et à mesure du projet. J'ai donc codé une macro qui permet de créer la nouvelle ligne du tableau synthèse quand on crée une nouvelle feuille dans le fichier.

### Analyse Post Mortem du 2nd Sprint

Finalement, j'ai pu dans ce second sprint terminer de coder la macro inachevée du premier sprint mais aussi en coder quelques autres. En revanche tous les programmes que j'avais envisagés n'ont pas forcément abouti, que ce soit parce qu'ils ne répondaient plus à un réel besoin ou parce que leur mise en oeuvre était trop contraignante, risquant une balance investissement/bénéfice très mauvaise.

Par ailleurs, j'ai été très surpris par le gain en rapidité que j'ai pu observer entre ma première macro et les suivantes. Je ne pensais pas m'approprier si vite les manipulations élémentaires du langage. Bien sûr, pour chaque programme je devais rechercher au fur et à mesure du code certaines propriétés ou formulations qui me manquaient malgré tout. D'ailleurs, la recherche de solutions pour le remplissage des formulaires pdf via vba est une des parties qui m'a pris plus de temps que prévu.

## Conclusion

Je souhaite conclure ce POK avec deux points qui m'ont marqués. Pour le premier, c'est le constat de la puissance pédagogique que ce projet a eu pour moi. Il m'a permis d'appliquer directement ce que j'avais étudié sur vba dans le cadre de mon MON, et ainsi de m'approprier le langage en m'entraînant sur des projets concrets dont je cernais clairement l'objectif, et dont le résultat m'est utile. Le deuxième point concerne l'inclusion de ma collègue Corinne dans le projet, ce qui était très intéressant. En effet, une partie des macros que j'ai codées lui étaient destinées, cela a inclu toute une dimension d'expérience utilisateur à laquelle j'ai du porter attention. La possibilité de tester avec elle au fur et à mesure mes propositions pour réadapter les macros à son utilisation était également enrichissante car ça me permettait de challenger mes programmes et me poussait à les améliorer.
