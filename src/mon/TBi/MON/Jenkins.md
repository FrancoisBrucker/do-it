---
layout: layout/post.njk

title: "Jenkins"
authors:
  - Tuncay Bilgi

tags: ['Jenkins','CI/CD']
---

# Jenkins :

### Objectif :

Comprendre les besoins qui mènent à l'utilisation d'un outil comme Jenkins pour un developpeur fullstack, puis mettre en place un exemple pratique d'utilisation.

### Sujets abordés pendant le MON :

- Qu'est ce que Jenkins ?
- Pourquoi utiliser un tel outil ?
- Les bases
- Exemple d'utilisation concret sur un de mes projets.


### pré-requis :
- Connaitre le contexte de devleppoment Fullstack.

## Continuous Delivery and Continuous Integration (CI/CD) : 

Ce sont des concepts de développement qui ont plusieurs but : 

 - Améliorer la qualité du code
 - Faciliter la vie des développeurs
 - Développer du code plus rapidement
 - Ajouter les dernières fonctionnalités le plus rapidement possible

Plus particulièrement, **la continuous integration** est l'ensemble de bonnes pratiques et d'outils qui permet de développer,tester et d'integrer le code dans une version prête à être déployée le plus souvent possible.
Traditionnelement, dans une équipe de développeur, la partie front et la partie Back pouvaient être développés par des personnens différentes et mises en communs queques fois avant de lancer des tests. Cette technique est innéficace car elle laisse le temps à des bugs ou des oncompatibilités de grandir sans que l'on s'en rend compte. En effet, si l'on test le système seulement une fois par mois, il est possible de se retroiver avec une version qui ne marche plus dutout et de perdre énormément de temps.
Des outils comme git, github action ou Jenkins permettent aux développeurs de mettre leurs codes en communs puis de lancer une batterie de test sur ce code plusieurs fois par jour. Grâce à cela, on évite la propagations de bugs et finalement, on gagne du temps.

Quand le code est testé est prêt à être déployé il ne reste qu'à ... le déployé!

**La continuous delivery** est l'ensemble d'outils et de pratiques qui permettent de déployer automatiquement la dernièere version fonctionelle du code sur le serveur de production. Cela permet do'ffrir au client une version qui soit toujours fonctionelle et qui possède les derniers ajouts, mises à jours correcctives ou même mises à jour de sécurité.
Onpeut par exemple imaginer une automatisation qui, toute les nuits, récupère toutes les fonctionnalités codées par les développeurs, les teste puis si tout fonctionne, les mets en commun dans une version à jour du code. Cette automatisation pourrait même déployer directement le code.
On appelle cela un *nightly build*.

{% info %}

Par exemple ce site de M.Brucker utilise de la CI/CD :
  - les élèves développent en collaboration grâce à github
  - A chaque commit sur la branche principale, le code est testé par Github action
  - Si les tests passent, le code est déployé sur le site github.io et la dernière version est disponnoble directement sans que M.Bricker est besoin de déployer quoi que ce soit lui-même

  Le problème avec cette manière de procéder est que l'on peut oush un commit monstreux qui détruit le site. Peut importe l'état des tests, le commit sera accepté et ik faudra réparer le code avant de pouvoir déployer le site à nouveau. 

{% endinfo %}

## Qu'est-ce que Jenkins?

{% info %} Une vidéo explicative [ici](https://www.youtube.com/watch?v=LFDrDnKPOTg&ab_channel=Simplilearn) {% endinfo %}

 L'idée est d'un tel outil est de mettre en place un environnement d'intégration continue. C'est à dire que le but est de créer un outil qui permet de developper, tester et pousser le code automatiquement, dès sa création. Par exemple, au lieu d'ajouter de nouvelles fonctionnalités sur notre site web, de faire un commit sur le repository, puis se rendre compte qu'il ne marche pas et corriger les bugs puis recommencer, on peut automatiser tout ça. Dans le meilleur des cas, à chaque nouvelle fonctionnalité, elle est automatiquement testée puis integrée dans une version viable du code, prête à être déployée. Si les tests détectent des erreurs ou des incompatibilités dans le code, la nouvelle fonctionnalité n'est pas integrée dans la branche principale et le développeur peut la retravailler sans jamais corrompre la version du code qui marche.



