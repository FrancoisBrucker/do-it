---
layout: layout/mon.njk

title: "Les enjeux du cloud computing"
authors:
  - Lola Perdrix

date: 1971-01-01
tags: 
  - "temps 2"
  - "bleu"
  - "cloud"

résumé: "Comprendre les enjeux du cloud computing actuels."
---

{% prerequis %}

Aucun prérequis

{% endprerequis %}
{% lien %}

Les lien utiles pour la compréhension de celui-ci.

{% endlien %}

L'objectif de ce MON est d'explorer les solutions de cloud computing qui existent aujourd'hui et décrire les différents enjeux qui existent aujourd'hui face à l'essor de cette technologie désormais omniprésente.

## Introduction

Avant de parler des enjeux je voudrais d'abord redéfinir le sujet. Le cloud est une solution qui permet d'**accéder à distance à des ressources informatiques**, en allouant ou désallouant des machines sur demande et en **payant à l'usage un prestataire** (AWS, Google Cloud, etc). Il permet donc de disposer de services informatiques via Internet, comme l'utilisation de logiciels, de la puissance de calcul, ou de l'espace de stockage, etc. sans avoir besoin de posséder le matériel physique nécessaire. L'objectif est d'optimiser les processus de production des entreprises, en fournissant un service rapide et performant à moindre coût.

Plusieurs niveaux de délégations de services dans le Cloud :

- **SaaS :** on achète une solution tout prête sur le marché et on se pose pas énormément de questions sur la gestion, on fait confiance au propriétaire de la solution
- **PaaS :** le prestataire fournit toutes les pré-installations nécessaires sauf la donnée et l’application
- **IaaS :** le prestataire ne fournit que les infrastructures, ce qui permet plus de customisation

Et plusieurs types de cloud : **public** (les entreprises se partagent les ressources), **privés** (le prestataire réserve des ressources qui seront dédiés à l'entreprise seule) ou **hybrides** (les deux). On verra ar la suite d'autres typologies de cloud.

## L'émergence du cloud

Comme expliqué dans l'article ["La petite histoire de la grande transformation des systèmes d’information de gestion"](https://theconversation.com/la-petite-histoire-de-la-grande-transformation-des-systemes-dinformation-de-gestion-70823), le cloud est venu répondre à des sollicitations de plus en plus complexes et à des données de plus en plus massives qu'il devenait compliqué de gérer on-premise. Le passage au cloud s'est effectué via une longue transformations des SI qui se sont peu à peu externalisés. Nous somme passés de SI très spécifiques au commencement, vers des SI de plus en plus standardisés (tout le monde adopte peu à peu les mêmes solutions logicielles etc.).

#### Comment cette attirance pour le cloud s'explique ?

- Système perçu comme le plus simple à gérer et à financer à court terme, avec une implémentation rapide
- Une technologie simple d'utilisation, fluide, performante, et promettante (scalable)
- Une sécurité pour ses données
- Une diversité des offres
- Un manque de compétences internes
- Un effet de mimétisme ou de "mode"
- La force de persuasion des offreurs
- La possibilité pour des PME d’avoir une gestion de leur données de haut niveau !

#### Quelques inconvénients

Bien sûr, des contreparties existent, comme la **perte de la maîtrise du SI (ou "vassalisation")**, la **dépendance** à Internet, la **déportation de la gestion des risques**, et d'autres enjeux qu'on abordera justement.

## Des enjeux économiques

Évidemment, il est avant tout question d'argent...

D'après le rapport annuel de Flexera ([2024 State of the Cloud Report | Flexera](https://info.flexera.com/CM-REPORT-State-of-the-Cloud?utm_source=bing&utm_medium=PPC&utm_content=finops_cloud_computing&lead_source=PPC&cq_cmp=688232258&cq_term=cloud%20computing%20services&cq_plac=&cq_net=o&cq_plt=gp&msclkid=e37781f5fc381eae7748e6a1976636e1)) l'enjeu des coûts liés au cloud préoccupe plus les entreprises que celui lié à la sécurité.

Les modèle du cloud reste tout de même très attirant du point de vue économique pour les entreprises :

- Le paiement à l'uasge permet de mieux s'adapter à la consommation.
- L'efficience des traitements permet de réduire le time-to-market pour permettre à l'entreprise de rester compétitive.
- Le cloud permet d'éviter les investissements dans les matériels de type hardware.
- Le coût d’apprentissage pour les clients est réduit,

Même si il implique des nouveaux coûts de maintenance que l'on ne peut plus assurer seul et la surveillance (contrôle, audit...).

Enfin, cela peut créer des conflits : comme en 2023 avec Twitter qui ne veut plus payer Google Cloud pour ses services dans le but d'économiser les coûts. De nombreux services furent menacés pour les utilisateurs de Twitter et cela avait fait parler, mais finalement tout est rentré dansl'ordre ([Twitter is refusing to pay Google for cloud services. Here’s why it matters, and what the fallout could be for users](https://theconversation.com/twitter-is-refusing-to-pay-google-for-cloud-services-heres-why-it-matters-and-what-the-fallout-could-be-for-users-207718)).

L'aspect économique attrayant du cloud est donc à contrebalancer avec tous les autres enjeux que je vais décrire.

## Des enjeux de sécurité

#### Quelle sécurité le cloud offre-t-il ?

- Garanties de sécurité souvent **supérieures à ce que les entreprises peuvent assurer tous seuls** par manque d'expertise
- Les data centers sont des **lieux hautement sécurisés** : matériaux robustes, absence de fenêtres, absence de poignées de porte extérieurs, mur épais, paratonerre, dispositifs anti-incendie, etc. mais aussi une surveillance et un contrôle des accès strict.
- **Accès à distance contrôlé** : politique de mots de passe stricte, antivirus, parefeu, mises à jour matérielles, parfois même des solutions contre les attaques par déni de service (DDos : hypersollicitation des serveurs pour créer des disfonctionnements)
- **Obligation de moyens et non de résultats** pour les fournisseurs.

(Plus de détails dans [cet article](https://theconversation.com/le-stockage-des-donnees-a-distance-gage-de-securite-ou-pari-risque-161478))

Donc oui, le cloud est censé être un endroit sécurisé pour nos données, à l'image d'une banque qui garderait nos bijoux. Cependant, il faut faire attention car toutes les offres ne proposent pas le même niveau de sécurité, car cela a un coût évidemment...

#### L'accident d'OVH

Il faut garder en tête que ce n'est pas parce que c'est un lieu sécurisé que l'on est à l'abri de tout accident. Un bon exemple est celui d'OVH : en mars 2021 a eu lieu un incendie dans le data center de Strasbourg qui a coupé l’accès à près de 3,6 millions de sites web et sous-domaines, de tout type de structure (entreprises, collectivités,...) et pendant des durées variées (quelques heures, ou définitivement). OVH était à ce moment le 6e hébergeur de sites web mondial, cet incident a beaucoup fait réagir notamment des clients qui ont accusé OVH de négliger la sécurité. On retrouve les informations par exemple dans cet article [Panique chez les clients d'OVH en défaut de sauvegarde - Le Monde Informatique](https://www.lemondeinformatique.fr/actualites/lire-panique-chez-les-clients-d-ovh-en-defaut-de-sauvegarde-82299.html)

Cet accident pourrait s'expliquer par l'adoption d'un modèle low cost par OVH qui s'accompagne de lacunes en terme de sécurité incendie et de certification, ajouté à la vieillese du bâtiment utilisé. Peut-être est-ce de la malchance où le prix à payer pour voir voulu trop capitaliser sur des petits clients ?

Dans tous les cas, cela a engendré de nombreuses réactions liés aux indisponibilités crées, des données ont été perdues à jamais, certaines pertes n'ont pas pu être compensées.

- **Qui est rseponsable ?**

Un contrat existe : les clients se sont contenté de cette prestation à moindre prix qui ne proposait pas de solution de back up : il était de la responsabilité du client de prévoir des solutions de secours en parallèle.

#### Moyens d'assurer plus de sécurité

- La présence d'un **back-up** pour avoir une sauvegarde des données à d'autres endroits et la construction d'un **PRA (plan de reprise d'activité)** aurait pu grandement miniser l'impact de cet accident du côté des clients. Chaque entreprise devrait s'assurer de leur existence si ce n'est pas compris dans l'offre cloud.

- De plus, beaucoup de fournisseurs cloud effectuent de la **redondance** : les données sont dupliquées dans plusieurs data center, ce qui permet de basculer d'un data center à l'autre en cas d'accident ou de surutilisation des serveurs.

## Des enjeux d'intégrité et de confiance

Une question se pose tout naturellement : ***peut-on faire confiance à un prestataire pour qu'il ne fasse pas n'importe quoi avec nos données ?***

Pour cela l’ANSII (Agence nationale de la sécurité des systèmes d'information) a créé le  **Sec­NumCloud**, afin de certifier les fournisseurs cloud de confiance.

Mais aussi, il faut faire attention à l’équilibre des relations entre les entreprises et leur fournisseur cloud, et une fois les contrats signés, se pose la question de la **réversibilité** : sera-t-il aisé de faire machine arrière ? Cela dépend des contrats.

Ce sont des questions évidemment importantes pour les entreprises qui expliquent l'importance du choix du fournisseur cloud, qui font par ailleurs de plus en plus d'efforts de **transparence** sur leurs fonctionnement afin de gagner la confiance.

## Des enjeux de souveraineté numérique

Face à la domination des GAFAM sur le secteur du cloud, la France se sent en quelque sorte impuissante et se trouve limitée dans ses choix et ses négociations. Il ne faut pas attendre que la concentration autour des GAFAM soit devenue irréversible et la France souhaitent développer ses propres clouds au sein de son territoire.

#### Cloud souverain

La nécessité d'un **Cloud souverain**, détaillé dans l'article ["Pourquoi réhabiliter le cloud régional ? De la complexité de localiser les données dans les nuages"](https://theconversation.com/pourquoi-rehabiliter-le-cloud-regional-de-la-complexite-de-localiser-les-donnees-dans-les-nuages-73293), est apparu pour clarifier qui est propriétaire de la donnée, où elles sont stockées, qui est responsable, comment ça marche, et quel impact cela produit. Un cloud souverain serait un *"Modèle de déploiement dans lequel l’hébergement et l’ensemble des traitements effectués sur des données par un service de cloud sont physiquement réalisés dans les limites du territoire national par une entité de droit français et en applications des lois et normes françaises."* Cela permettrait à la France d'avoir plus de contrôle.

#### Cloud régional

De plus, comme illustré dans l'autre moitié de l'article : ["Pourquoi réhabiliter le cloud régional ? De la pertinence des data center locaux et globaux"](https://theconversation.com/pourquoi-rehabiliter-le-cloud-regional-de-la-pertinence-des-data-center-locaux-et-globaux-83556), il y a aussi une volonté de développer les **clouds régionaux** : « Modèle de déploiement dans lequel l’hébergement et l’ensemble des traitements effectués sur des données par un service de cloud sont physiquement réalisés dans les limites du territoire d’une des 13 régions administratives françaises. »

Exemples : Le data center régional **Hermine** en Bretagne qui se veut éco-responsable, **BT Blue** qui a des data centers certifiés ISO 27001, **DeepData** qui a construit un data center performant (Pays de la Loire), etc.

On se retrouve donc avec un **mix de micros data center régionaux et de mégas data center internationaux**, pour optimiser à la fois la collecte des données au plus près des utilisateurs et le traitement de celles-ci le plus efficace possible.

Les data centers régionaux du sud de la france permettrait d’apporter aussi des solutions aux pays d’Afrique du Nord qui sont en retard.

#### Projets

Des projets sont réalisés dans le but de construire des clouds souverains, stratégiques, régionaux, ou soutenables, comme par exemple le projet [Andromède](https://fr.wikipedia.org/wiki/Androm%C3%A8de_(cloud)) (qui n'a pas abouti) ou [Gaia-X](https://fr.wikipedia.org/wiki/Gaia-X) à l'échelle européenne.

Les revenus du marché du cloud computing en France en 2021 est de 7 Mrd d'euros avec pour principal acteur OVH.

## Des enjeux juridiques

Comme expliqué notamment dans l'article ["Le stockage des données à distance, gage de sécurité ou pari risqué ?"](https://theconversation.com/le-stockage-des-donnees-a-distance-gage-de-securite-ou-pari-risque-161478), un autre problème qui se pose est celui de la **législation des territoires :** différentes réglementations existent selon la nationalité du fournisseur et l'endroit où sont stockées les données, notamment les règles de confidentialité. De plus, les données d'une entreprise sont souvent réparties sur plusieurs datacenters et chez plusieurs fournisseurs, ce qui complexifie encore plus la surveillance.

Par exemple les réglementations américaines comme le Freedom Act (anciennement Patriot Act) ou le [Cloud Act](https://fr.wikipedia.org/wiki/CLOUD_Act) questionnent sur l'atteinte à notre vie privée de la part du gouvernement américain et rendent difficile le respect des lois françaises.

Les fournisseurs ne sont pas toujours transparents non plus sur les localisations des datacenters qu'ils utilisent, ce qui rend la tâche plus complexe encore, le RGPD peut par exemple potentiellement être esquivé et l'utilisateur peut perdre le contrôle de l'usage fait des ses données ce qui n'est pas normal.

L'enjeu de protection des données ne touche pas que l'IT mais doit être un **sujet transverse** à l'entreprise, l'objectif est de faire en sorte que les procédures soient toujours réglementées et révisées, pour se conformer au RGPD.

J'ai également pu prendre connaissance d'autres décrets ou législations existantes comme :

- le [Privacy shield](https://www.cnil.fr/fr/definition/privacy-shield) : qui certifie et autorise les échanges de données entre l'UE et des etreprises américaines "de confiance".
- le [Digital Services Act ou DSA](https://www.economie.gouv.fr/actualites/numerique-dsa-entre-en-vigueur) : qui régule les données en Europe, pour lutter notemment contre le contenu illicite.

Cependant ces réglementations sont nombreuses et complexes, ce qui rend difficile le choix de son fournisseur.

## Des enjeux organisationnels

N'oublions pas que l'avènement du cloud a aussi bouleversé les organisations, avec le cloud les entreprises changent leur manière de travailler, notamment avec les nouvelles offres “as a service”.

#### Des enjeux de recrutement : guerre des talents

Le secteur du Cloud est l’un des plus dynamiques en France en termes de recrutement. Selon LinkedIn, il y aurait eu 48 % de croissance en 5 mois en 2022. On exige maintenant de **nouvelles compétences** : Docker, Azure et Kubernetes parmi les compétences les plus recherchées (forte croissance, Source Indeed). C'est ce qui engendre une **guerre des talents** parmi les experts du cloud dont on a beosin.

#### Des nouveaux métiers

D'autres métiers ont également vu le jour, les métiers du conseil en cloud computing, les cloud brokers, les administrateurs, les ingénieurs cybersécurité, les architectes cloud, les DPO (délégué à la protection des données), etc.

#### Des nouvelles pratiques

- Le **SecOps** : pour assurer des bones pratiques en termes de sécurité dans l'entreprise
- Le [**FinOps**](https://blog.hubspot.fr/website/finops) : pour repenser la consommation des services cloud à l'échelle de l'entreprise pour éviter le gaspillage au maximum.
- Les [**Centres d'excellence Cloud (CCoE)**](https://docs.oracle.com/fr-fr/iaas/Content/cloud-adoption-framework/cloud-center-of-excellence.htm) : organe qui assure la mise en place des bonnes pratiques cloud et gère sa stratégie au sein de l'enteprise.
  
#### Bouleversement des organisations déjà en place

Dans l'article ["Quand les données des PME migrent vers les nuages : libération ou vassalisation ?"](https://theconversation.com/quand-les-donnees-des-pme-migrent-vers-les-nuages-liberation-ou-vassalisation-70822), on parle des **DSI** qui ont vu leur rôle évoluer avec les années : au départ techniciens et dépanneurs, s'occupant du matériel, ils assurent aujourd'hui un rôle de management, pour assurer la continuité du flux de données qui échappent désormais souvent à leur maîtrise. Et cela **impacte le business autant que l'IT**, car le cloud a engendré de nouvelles pratiques pour tous les métiers : de nouveaux logiciels, un télétravail grandement facilité, de l'agilité, de nombreuses données, des tâches plus rapides... Ces nouveaux modes de travail sont arrivés rapidement et sont encore amenés à évoluer, c'est pour cela qu'il y a aussi un véritable enjeu autour de **l'acceptation sociale** et de **l'accompagnement au changement** au sein des entreprises pour accueillir au mieux cette technologie nouvelle (plus si nouvelle maintenant).

## Des enjeux environnementaux

Enfin, un enjeu de taille majeure et d'actualité est l'enjeu environnemental. De nombreux articles évoquent les conséquences environnementales du cloud, qui est réellement énergivore.

Tout d'abord, d'après ["Les data centers sont de plus en plus problématiques pour la planète"](https://www.journaldugeek.com/2021/12/07/les-data-centers-sont-de-plus-en-plus-problematiques-pour-la-planete/), les data centers seraient aussi polluant que l'industre aéronautique. Les entreprises se cachent derrière la REC (renewable energy certification) pour se dire neutre en carbone sans réellement l'être. Peu de pays peuvent se vanter d'être écologiquement responsable par rapport à l'utilisation de leurs serveurs ! Les impacts sont décrits dans l'article et dans d'autres cités en bibliographie, mais aussi dans le [MON de Matthieu](https://francoisbrucker.github.io/do-it/promos/2024-2025/Matthieu-Dufort/mon/temps-2.2/).

#### Importance de la consommation d'eau

D'après l'article ["We are ignoring the true cost of water-guzzling data centres"](https://theconversation.com/we-are-ignoring-the-true-cost-of-water-guzzling-data-centres-167750), qui date de 2021, le cloud représentait 2% de la demande d’électricité mondiale en 2020, et environ 40% servent au refroidissement des serveurs. Cet article met bien en avant les dimensions du coût en énergie et en eau des data centers lié au cloud. Surtout, il insiste sur le fait que la consommation d'électricité n'est pas la seule source d'inquiétude, mais la **consommation d'eau** en est également une importante. Il y a une véritable pression sur les ressources en eau dans les régions où sont établis les data center. C'est donc une information de plus en plus transparente.

#### Quelques solutions technologiques

- Le [projet Natik de Microsoft](https://www.microsoft.com/en-us/research/project/natick/?msockid=04789ef652c86284261d8a1b538f6365) en 2023 mentionné dans [cet article](https://theconversation.com/most-data-lives-in-the-cloud-what-if-it-lived-under-the-sea-216067) : immersion de data center dans la mer (qui a vraiment eu beaucoup d'impacts positifs et encourageants).
- Mettre ses data centers dans des montagnes ou pays nordiques... 
- Recycler l'énergie "perdue" : récupérer la chaleur émise pour la recycler en chauffant des bâtiments : c'est le cas de la solution Hyperion décrite [ici](https://hyperion.green/2024/02/08/datacenter-recuperation-chaleur/#:~:text=Dans%20ce%20contexte%2C%20la%20r%C3%A9utilisation%20de%20la%20chaleur,et%20de%20promouvoir%20une%20%C3%A9conomie%20circulaire%20et%20durable.), qui se définit comme responsable et économiserait 50% de la consommation d'électricité.
- Utiliser des énergies renouvelables.

#### Nouveautés organisationnelles mises en place

- Les [Centres d'excellence cloud](https://docs.oracle.com/fr-fr/iaas/Content/cloud-adoption-framework/cloud-center-of-excellence.htm), déjà mentionnés.
- L'approche **GreenOps**, dont le but est de réduire la consommation et limiter l’impact environnemental du service numérique des entreprises et notamment du cloud, pour tendre vers le Green IT.
- Des indicateurs sont utilisés pour pouvoir faire des estimations : le **Power Usage Effectiveness** (PUE), le Green Energy Coefficient (GEC), Energy Reuse Factor (ERF), Carbon Usage Effectiveness (CUE), etc. Entre 2007 et 2021, les data centers français ont amélioré leur efficience énergétique par 47 %.
- Il existe aujourd'hui une définition de ***cloud soutenable*** : « Modèle de déploiement dans lequel l’hébergement et l’ensemble des traitements effectués sur des données par un service de cloud sont respectueux des dimensions environnementale, économique et sociétale-éthique » (tiré de [cet article](https://theconversation.com/pourquoi-rehabiliter-le-cloud-regional-de-la-complexite-de-localiser-les-donnees-dans-les-nuages-73293))

#### Le gaspillage

La notion de **gaspillage** évoquée dans cet article : ["La chasse au gaspillage dans le cloud et les data centers"](https://theconversation.com/la-chasse-au-gaspillage-dans-le-cloud-et-les-data-centers-196669) était pour moi aussi importante : c'est un sujet sur lequel j'étais initialement moins sensibilisée que les autres.

Malgré les efforts fournis pour améliorer l'efficacité énergétique des data centers, qui ont par ailleurs réellement marché, cela n'a fait que donner l'illusion d'une abondance de ressources.

La **virtualisation** a permis de mutualiser beaucoup de ressources matérielles (en répliquant des machines virtuelles sur une seule machine physique), mais il en résulte que les VM sont sous-utilisées, comme cela ne coûte pas cher, le client achète tout un serveur sans forcément l'utiliser dans la durée ce qui crée un gros gaspillage de ressources par rapport aux VM qui pourraient être utilisées mais qui se retrouvent bloquées. Les efforts fournis n'ont donc pas servi à grand chose...De plus, les clients surestiment souvent la quantité de mémoire dont ils ont besoin "par sécurité".

Pour régir face à cette tendance, il y a maintenant des recyclages de VM (on détecte les inutilisations pour employer la VM à un autre usage temporairement ou définitivement), mais on fait aussi de la **surallocation** / **overbooking** (comme dans les avions) mais ces techniques manquent de contrôle.

L'enjeu est donc de mieux utiliser la mémoire en accompagnant mieux les clients dans leur choix ou proposer des offres plus adaptées à leurs besoins.

#### Un problème de comportement

Comme souligné dans cet article : [The environmental cost of data centres is substantial, and making them energy-efficient will only solve half the problem](https://theconversation.com/the-environmental-cost-of-data-centres-is-substantial-and-making-them-energy-efficient-will-only-solve-half-the-problem-202643), le problème avec la consommation du cloud réside avant tout dans le comportement de la société. Le fait que tout soit si rapide pousse à la consommation et renforce **l'effet rebond** ou **paradoxe de Jevons**, selon lequel plus on réussira à augmenter l'efficacité de la solution dans l'objectif de moins consommer, plus le service sera utilisé et la consommation globale sera finalement encore augmentée.

**Conclusion :** c’est avant tout un changement de comportement qui est primordial plutôt que d’essayer d’optimiser à l'infini.

## Conclusion

Ce MON m'a permis d'avoir une **vue d'ensemble** sur les questions qui se posent au sujet du cloud et de son utilisation de nos jours. Ce sont ces nombreuses questions qui incitent les gouvernements à prendre de plus en plus de mesures et les entreprises à faire des choix de plus en plus réfléchis, en accord avec leurs priorités. Ce que je retiens avant tout, bien que je le savais déjà avant, est qu'il y a un gros problème de consommation qui n'est pas soutenable.

J'avais pour but de regarder un peu tous les enjeux avant de me concentrer sur un en particulier, mais la lecture des articles et la quantité d'informations que j'ai jugées importantes de noter ont rapidement écoulé le temps à ma disposition pour faire ces recherches approfondies. Encore une fois, j'aurais bien aimé avoir plus de temps... Néanmoins je reste satisfaite d'avoir réuni et formalisé toutes ces informations ici, bien qu'il fut difficile de sélectionner les informations pertinentes et d'en faire un résumé.

Pour finir, je note qu'il a été très difficile de trouver des informations et chiffres récents, la plupart des articles commencent à dater de quelques années et je trouve ça très dommage de ne pas avoir vu plus de choses d'actualités.

## Sources

{% lien %}

- [Cloud computing, big data  : de nouvelles opportunités pour les sociétés - Insee Première - 1643](https://www.insee.fr/fr/statistiques/2672067), Insee
- ["La petite histoire de la grande transformation des systèmes d’information de gestion"](https://theconversation.com/la-petite-histoire-de-la-grande-transformation-des-systemes-dinformation-de-gestion-70823), The Conversation, 2017
- [2024 State of the Cloud Report | Flexera](https://info.flexera.com/CM-REPORT-State-of-the-Cloud?utm_source=bing&utm_medium=PPC&utm_content=finops_cloud_computing&lead_source=PPC&cq_cmp=688232258&cq_term=cloud%20computing%20services&cq_plac=&cq_net=o&cq_plt=gp&msclkid=e37781f5fc381eae7748e6a1976636e1), Flexera, 2024
- [Twitter is refusing to pay Google for cloud services. Here’s why it matters, and what the fallout could be for users](https://theconversation.com/twitter-is-refusing-to-pay-google-for-cloud-services-heres-why-it-matters-and-what-the-fallout-could-be-for-users-207718), The Conversation, 2023
- [Panique chez les clients d'OVH en défaut de sauvegarde - Le Monde Informatique](https://www.lemondeinformatique.fr/actualites/lire-panique-chez-les-clients-d-ovh-en-defaut-de-sauvegarde-82299.html), Le Monde Informatique, 2021
- ["Pourquoi réhabiliter le cloud régional ? De la complexité de localiser les données dans les nuages"](https://theconversation.com/pourquoi-rehabiliter-le-cloud-regional-de-la-complexite-de-localiser-les-donnees-dans-les-nuages-73293), The Conversation, 2021
- ["Pourquoi réhabiliter le cloud régional ? De la pertinence des data center locaux et globaux"](https://theconversation.com/pourquoi-rehabiliter-le-cloud-regional-de-la-pertinence-des-data-center-locaux-et-globaux-83556), The Conversation, 2021
- ["Le stockage des données à distance, gage de sécurité ou pari risqué ?"](https://theconversation.com/le-stockage-des-donnees-a-distance-gage-de-securite-ou-pari-risque-161478), The Conversation, 2021
- [Cloud Act](https://fr.wikipedia.org/wiki/CLOUD_Act), Wikipédia
- [Privacy shield](https://www.cnil.fr/fr/definition/privacy-shield), CNIL
- [Digital Services Act ou DSA](https://www.economie.gouv.fr/actualites/numerique-dsa-entre-en-vigueur), site du gouvernement
- ["Quand les données des PME migrent vers les nuages : libération ou vassalisation ?"](https://theconversation.com/quand-les-donnees-des-pme-migrent-vers-les-nuages-liberation-ou-vassalisation-70822), The Conversation, 2017
- ["Les data centers sont de plus en plus problématiques pour la planète"](https://www.journaldugeek.com/2021/12/07/les-data-centers-sont-de-plus-en-plus-problematiques-pour-la-planete/), journaldugeek, 2021
- ["We are ignoring the true cost of water-guzzling data centres"](https://theconversation.com/we-are-ignoring-the-true-cost-of-water-guzzling-data-centres-167750), The Conversation, 2021
- [Most data lives in the cloud. What if it lived under the sea?](https://theconversation.com/most-data-lives-in-the-cloud-what-if-it-lived-under-the-sea-216067), The Conversation, 2023
- [Projet Natik](https://www.microsoft.com/en-us/research/project/natick/?msockid=04789ef652c86284261d8a1b538f6365), Microsoft
- [Datacenter et transition énergétique : quelle carte à jouer ? - Hyperion](https://hyperion.green/2024/02/08/datacenter-recuperation-chaleur/#:~:text=Dans%20ce%20contexte%2C%20la%20r%C3%A9utilisation%20de%20la%20chaleur,et%20de%20promouvoir%20une%20%C3%A9conomie%20circulaire%20et%20durable.)
- ["La chasse au gaspillage dans le cloud et les data centers"](https://theconversation.com/la-chasse-au-gaspillage-dans-le-cloud-et-les-data-centers-196669), The Conversation, 2023
- [The environmental cost of data centres is substantial, and making them energy-efficient will only solve half the problem](https://theconversation.com/the-environmental-cost-of-data-centres-is-substantial-and-making-them-energy-efficient-will-only-solve-half-the-problem-202643), The Conversation, 2023

{% endlien %}
