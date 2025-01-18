---
layout: layout/mon.njk

title: "MON 3.2. La recette des Cookies"
authors:
  - Sarah Sebastien

date: 2024-14-01
tags: 
  - "temps 3"
  - "CNIL"
  - "traceurs"
  - "ciblage publicitaire"


résumé: "Ce MON traitera du concept de Cookies, comment il a vu le jour, son utilisation par les entreprises, et les réglementations qui vont avec."

---
---

{%prerequis 'Niveau débutant'%} 
Prérequis : Aucun
{%endprerequis%}

## Sommaire

- [Introduction](#introduction)
- [Qu'est ce qu'un cookie ?](#definition)
- [D'où ça vient?](#histoire)
- [Est-ce qu'un cookie c'est sécurisé?](#sécurité)
- [L'utilisation des cookies dans le ciblage publicitaire](#publicité)
- [Que dit la loi?](#loi)

<h2 id=introduction> Introduction</h2>

Après avoir lu le MON de Kawtar sur le **Data Collection** et le POK de Victor sur **l'AIPD**, que j'ai trouvés très intéressants, j'ai voulu explorer un peu plus ce sujet. Et je me suis dit : *"C'est bien beau tout ça, mais finalement, c'est quoi un cookie ? Et à quoi ça sert ?"*. 
Voilà donc comment ce MON a vu le jour. 

<h2 id=definition> Qu'est ce qu'un cookie?</h2>

### Tentative de définition, la plus simple possible

Un cookie Internet, que l'on appelle aussi **témoin** (ou même **témoin de connexion**) est un fichier texte qui est échangé entre **le client** et **le serveur** entre chaque appel : ils sont générés par le serveur d'un site internet ou d'une application, puis sont déposés sur le disque dur de l'ordinateur.

> Dans son usage le plus basique, un cookie permet **d'identifier** un internaute qui visite un site web et de le **reconnaître** lorsqu'il le visitera à nouveau.

Le **serveur** va **stocker les informations de la session** de l'utilisateur dans une BDD et ne donner qu'à l'utilisateur un **identifiant de session** *(ou cookie)* (qui est unique et aléatoire) qui est stocké dans le disque dur de l'utilisateur. Dès lors que la session se termine, le cookie devient *obsolète*.

{%info%}
On compare ça au fait de poser son vêtement au vestiaire et de recevoir un ticket avec un numéro pour le retrouver lorsque l'on revient.
{%endinfo%}

Techniquement parlant, les cookies sont envoyés à l'aide d'en-têtes http *(protocole qui assure que le navigateur et le serveur peuvent se comprendre)*  dans les messages échangés entre le navigateur, souvent appelé **client**, et le **serveur.**

{%faire%}
Le protocole http est **sans état**, ie : il ne conserve ni ne stocke les sessions des clients. Donc, le client est responsable du stockage des informations de session pour les demandes ultérieures. Ainsi, lorsque le client fait une requête, il doit inclure ses informations de session au serveur pour l'authentification ou la validation.
{%endfaire%}

<img width=350 src=def_cookies.webp>

[Source](https://blog.larapulse.com/web/protect-cookies)

### Les attributs d'un cookie 

<img width=400 src=info_cookie.webp>

- **ID de session** : un **long** string **aléatoire** utilisé for la gestion d'une session, qui sert à identifier de manière **unique** un client qui essaie d'accéder à un serveur
- **date d'expiratiion** : plus ou moins longue 
  - *réseaux sociaux* comme Facebook : sessions avec des durées de vie très longues *(pas beaucoup besoin de se connecter)* 
  - *site d'une banque* : sessions avec des durées de vie très courtes, pour sécuriser les données *(5 minutes ou moins, sans interaction de l'utilisateur avec le serveur)*
- **domaine** : qui spécifie le domaine dans lequel le cookie peut être utilisé
- **chemin** : utilisé pour spécifier la ressource ou le chemin où ce cookie est valide (URL)
- **HttpOnly** : protection définie dans les entêtes http : si *true*, permet d'éviter d'accéder au cookie via JavaScript du côté client
 
### Pourquoi on se sert d'un cookie ?

Les cookies ont de multiples usages : ils peuvent servir à...

- la gestion de sessions utilisateur (*ex: mémoriser un identifiant client auprès d'un site marchand)*
-  le suivi de l'activité de l'utilisateur sur le site *(ex: le contenu courant d'un panier d'achat)*
- les préférences d'un utilisateur *(ex: sa langue d’affichage)*
- un identifiant permettant de tracer notre navigation à des fins statistiques ou publicitaires, etc. 
- réseaux sociaux, notamment générés par leurs boutons de partage.

Certains de ces usages sont strictement nécessaires aux fonctionnalités expressément demandées par l’utilisateur ou bien à l’établissement de la communication et donc **impossibles à refuser**. D’autres, qui ne correspondent pas à ces critères, nécessitent un consentement de l’utilisateur avant lecture ou écriture.
C'est pour ça qu'on distingue **deux types de cookies**.

### Les cookies internes et tiers

- Les **cookies "internes"** *(ou cookies first party)* proviennent du site visité, principalement sur son propre domaine. Ils peuvent être utilisés pour le fonctionnement du site ou pour collecter des données personnelles.
- Les **cookies "tiers"** *(ou cookies third party)* sont déposés sur des domaines différents, généralement par des entreprises tierces. Ils sont émis par des sites tiers présents sur la page affiché : ils servent à suivre les pages visitées sur le site pour collecter des informations sur l'utilisateur.

{%faire%}
Les cookies **internes** suivent l'utilisateur uniquement sur le site web d'origine, tandis que les cookies **tiers** peuvent le suivre sur tous les sites qui les utilisent.
{%endfaire%}

### Vers la fin des cookies tiers ?

Les cookies tiers sont de plus en plus remis en question pour limiter le suivi publicitaire, et notamment par certains navigateurs. *(ex : Safari d'Apple en 2017 avec programme ITP ("Intelligent Tracking Prevention" ou "prévention intelligente de pistage"))*

La CNIL observe l'émergence plusieurs alternatives aux cookies tiers, voici celles que j'ai retenues *(et comprises)* :

- **Fingerprinting** : Identifie de manière unique un utilisateur en utilisant les caractéristiques techniques de son navigateur pour créer une *empreinte numérique*, plutôt que de stocker des cookies.
- **Authentification unique (SSO)** : Permet la connexion à plusieurs sites avec un seul compte utilisateur, ce qui peut être utilisé pour suivre l'utilisateur sur différents sites.
- **Ciblage publicitaire par cohorte** : consiste à regrouper les utilisateurs en "cohortes"basées sur des caractéristiques similaires *(intérêts ou les comportements en ligne)*, plutôt que des individus spécifiques : permet de réduire le suivi individuel
  
{%prerequis "<u>Sources</u>"%}
Ressources de la CNIL :
https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/alternatives-aux-cookies-tiers
https://www.cnil.fr/fr/cookies-et-autres-traceurs/definitions/glossaire
Wikipédia : 
https://fr.wikipedia.org/wiki/Cookie_(informatique) *(permet d'avoir une vision globale des thèmes et notions du sujet)*
Youtube :
https://www.youtube.com/watch?v=GhrvZ5nUWNg
https://www.youtube.com/watch?v=zHBpJA5XfDk *(très bonne explication des attributs d'un cookie)*
https://www.youtube.com/watch?v=ZHvwVsoQx3o *(quelques précisions sur les cookies, même si ce n'est pas le but principal de la vidéo)*
{%endprerequis %}

<h2 id=histoire> D'où ça vient?</h2>

### Le premier cookie

Les cookies furent inventés au milieu des **années 1990** par les **Américains**. Leur but était améliorer **l’expérience de l’utilisateur**, pour permettre aux sites web de se souvenir du passage d'une personne. Les cookies ont ainsi joué un rôle important dans le développement d’internet tel qu’on le connaît aujourd’hui. 

À ses débuts, le **World Wide Web**, tel qu'imaginé par Tim Berners-Lee, était conçu comme **"sans état"**: chaque requête effectuée via le protocole HTTP était considérée comme **indépendante**. Pas de possibilité pour le serveur de lier deux requêtes successives provenant du même système et, donc de **stocker des informations sur un utilisateur**.  Cette fonctionnalité visait à renforcer les liens entre les personnes publiant sur le Web, en encourageant les sites à inclure des liens vers d'autres sites qui leur envoyaient des visiteurs. 

En 1994, deux ingénieurs *(John Giannandrea et Lou Montulli)* de chez Netscape créent le **cookie**. Ils travaillaient à ce moment là sur un projet de création de serveurs qui permettraient à leur clients d'avoir une solution de **commerce en ligne**. L'enjeu était de savoir : *comment garder la trace des différents éléments qu’un client qui navigue sur un site web ajoute à son panier ?*
Le problème à l'époque, c'était que **sans état**, chaque navigation vers une nouvelle page provoque l’oubli de toutes les actions précédentes. 

Les deux ingénieurs proposent alors une solution permettant de stocker un **état** dans un nouvel objet qu'ils appellent ***Persistent Client State HTTP Cookies*** ou **cookie**.

{%faire%}
Des expérimentations testent le stockage de ces informations dans l’URL des pages, cependant elles ne sont pas très fructueuses. 
{%endfaire%}

### La naissance de nouveaux problèmes qui deviennent vite préoccupants

Netscape voulait à cette époque, **être rapide** : dès qu'il a été trouvé, le code a été introduit sur le web, *sans en informer les utilisateurs, sans introduire de notification à la dépose d’un cookie par un site web, et sans documentation.*

{%faire%}
Ce n'est qu'en 1996, que l’existence des cookies est pour la première fois révélée au grand public, dans un article du Financial Times.
{%endfaire%}

Très vite, Netscape commence à être **critiquée**, pour un problème : 
Si le serveur du site peut *lire et écrire* des cookies sur l'ordinateur de l'utilisateur, alors lorsqu'il intègre des ressources tierces telles que des images, des scripts, etc., le serveur fournissant ces ressources tierces peut également lire et écrire des cookies sur le terminal de l'utilisateur, en identifiant le contexte dans lequel ces ressources ont été appelées (par exemple, l'URL). 
Alors, si un éditeur de contenu en ligne intègre une bannière publicitaire sur son site, le **publicitaire** peut **accéder aux URL visitées par l'utilisateur**. Si ce même publicitaire est également présent sur le site d'un autre éditeur, il peut identifier le même utilisateur sur ce site également. 

**En 1997**, l’IAB (Interactive Advertising Bureau) annonce un chiffre d’affaire global du marché de la publicité en ligne de **906,5 millions de dollars**. Forte opisition qui amène à un constat sans appel : *il faut désactiver par défaut les cookies tiers*. En octobre **2000** la norme est publiée, RFC2965. Cette année-là, le chiffre d’affaire calculé par l’IAB est de **8,2 milliards de dollars** *(soit presque 1000% de croissance en trois ans)*. 

{%info "Remarque"%}
En 1996, la société **DoubleClick** a été créée pour exploiter ces cookies tiers à des fins publicitaires. Cette entreprise est un succès : elle est rachetée pour **1,1 milliards de dollars** en **2005** par des investisseurs et fera ensuite l’objet d’un  rachat en **2007** pour **3,1 milliards de dollars** par Google.
{%endinfo%}

---

{%prerequis "<u>Sources</u>"%} 
https://linc.cnil.fr/une-petite-histoire-du-cookie
https://www.numerama.com/tech/701436-au-fait-pourquoi-les-cookies-sappellent-ils-des-cookies.html
{%endprerequis %}

<h2 id=sécurité> Est-ce qu'un cookie c'est sécurisé?</h2>

Les cookies contiennent des **données personnelles** de *notre compte*, de *notre ordinateur*. Les cookies sont donc des **données sensibles** d'un point de vue de la sécurité. *Particulièrement les **cookies de session** qui permettent de s'authentifier sur un site internet.*
En théorie, un cookie associé à un site web **ne peut pas être envoyé à un autre site web**. Mais, un certain nombre de failles permettent de voler des cookies. 

En faisant mes recherches, je suis tombée sur [cette vidéo](https://www.youtube.com/watch?v=nHUswhLl-Bw) de ce fort sympathique québécois. Il y explique, avec un exemple concret **comment récupérer un ID de session**. J'ai donc essayé de réappliquer sa vidéo, pour mieux comprendre les enjeux.

### Récupérer un ID de session : tentative 1

Il faut se rendre sur cette adresse : **[altoromutual.com](https://altoromutual.com)**, via **Chrome** (je n'ai pas réussi sur Mozilla).

Une fois arrivé sur la page, on fait *clique droit > inspecter*.
<img width=350 src=inspecter.webp>

On ouvre l'onglet *Application* pour accéder aux cookies, et on clique sur l'URL du site.
On voit alors qu'il n'y a qu'une ligne.

<img src=pasidentifier.webp>

Il faut ensuite se connecter *(identifiant : admin, et mot de passe : admin)*. Si on regarde le chemin de la page, on voit qu'on arrive sur la page :

```
https://altoromutual.com/bank/main.jsp
```
On voit bien que cette page est une page **réservée aux utilisateurs**, où est écrit *"Hello Admin User"*.

Si on se penche maintenant sur les cookies du site, on voit alors apparaître le cookie de connexion qui vient d'être envoyé par le serveur, comme on s'est connecté.

<img src=identifier.webp>

Maintenant, si on ouvre un onglet de *Navigation privée*, et qu'on revient sur [cette page](https://altoromutual.com) et qu'on essaie de se connecter à cette page :
```
https://altoromutual.com/bank/main.jsp
```
On voit que c'est impossible, car je n'ai pas les droits pour accéder à cette page, comme je ne suis pas identifiée. **MAIS**, si je recopie les cookies de session que j'avais obtenus au début en me connectant, dans les cookies de la page privée, et que j'essaie à nouveau d'accéder à la page administrateur, la magie opère ...

<img src=page_administrateur.webp>

### Récupérer un ID de session : tentative 2

En continuant mes recherches, je suis tombée sur la méthode du **Cross site scripting**(ou XXS).En fait, cette technique part d'une question simple : *et si on a accès au Java Script d'un site, qu'est ce qu'on pourrait faire ?* XSS consiste donc à injecter un code JavaScript malveillant, dans une autre page web. Ce code est exécuté par les victimes et permet aux attaquants de contourner les contrôles d'accès et d'usurper l'identité des utilisateurs. Il permet notamment facilement, d'extraire des informations et **des cookies**.

Il existe normalement une politique qui empêche un site Web de lire ou d'écrire des données sur un autre site, c'est la **SOP** (same origin policy). Elle vérifie **3 conditions** dans l'origine du site web :
- **le protocole**
- **l'hôte**
- **le port** 
- 
Alors seulement si ces 3 paramètres sont **identiques** pour 2 origines **différentes**, le navigateur autorise la lecture ou l'écriture d'origines croisées.

{%faire%}
Exemple : 
http//pwnfunction.com
http//hackfunction.com
Le protocole est le même, mais l'hôte est différent : la navigateur refuse la lecture.
{%endfaire%}
---
{%prerequis "<u>Sources</u>"%}
Par manque de temps, et parce que ça devenait un peu compliqué pour moi vu mon faible niveau en JavaScript et en web, j'ai seulement visionné les vidéos suivantes. Mais elles restent très intéressantes, et très accessibles pour un sujet pas si facile ! 
https://www.youtube.com/watch?v=ZHvwVsoQx3o
https://www.youtube.com/watch?v=UXtxfka2TuY
https://www.youtube.com/watch?v=EoaDgUgS6QA
{%endprerequis %}


<h2 id=publicité> L'utilisation des cookies dans le ciblage publicitaire</h2>

### A quelle fin ?

On considère qu’un consommateur doit obtenir l’information qu’il désire en **3 clics** (ie *maximum 3 pages après la page d'accueil*) : c'est ce qu'on appelle la **règle des trois clics**. Même si ce n'est qu'une simple règle, elle reflète bien **la frustration** d'un internaute lorsqu’il a des difficultés à trouver l’information souhaitée. 

Les cookies, qu'on appelle **cookies de pistage**, permettent sont alors un outil de :

- **suivi et d’analyse** du comportement des utilisateurs, en collectant leur données de navigation afin d’améliorer leur expérience et de créer un profil de consommation.
- **remarketing** qui permet de suggérer plus tard à un internaute qui serait passé sur un site e-commerce des biens qui l’intéressaient

{%prerequis "<u>Sources</u>"%}
https://www.definitions-marketing.com/definition/regle-des-3-clics/
{%endprerequis%}

### Prendre conscience de ces cookies de pistage grâce au logiciel CookieViz

#### Qu'est ce que c'est ?

**CookieViz** est le premier logiciel à destination du grand public développé en interne par la **CNIL**. Il est disponible sur Windows, Linux et Mac OS. C'est un **logiciel open source** qui analyse les interactions entre notre ordinateur, notre navigateur et des sites et serveurs distants. Il permet de savoir à quels autres acteurs le site qu'on visite envoie des informations. 

Vous pouvez retrouver [ici](https://linc.cnil.fr/cookieviz-une-dataviz-en-temps-reel-du-tracking-de-votre-navigation) le support de présentation de l'application avec les liens utiles pour télécharger le logiciel.

#### Utilisation du logiciel

J'ai voulu faire le test : j'ai navigué sur un grand nombre de sites en **2 étapes** pour voir l'influence des cookies et de mon consentement. Dans la première étape, *j'acceptais tous les cookies*, dans la 2e *je les refusais tous*.
Pour mon chemin de navigation, j'ai varié les plaisirs : 

- je suis allée faire du shopping sur **Asos**
- j'ai cherché un cadeau d'anniversaire pour ma soeur sur **Amazon**
- j'ai regardé les dernières sorties de  livres sur la **Fnac**
- j'ai regardé plusieurs vidéos **Youtube** parmi le top tendances
- j'ai cherché une nouvelle table de chevet sur **leboncoin**
- je me suis mis à jour sur les actualités sur **bbc** et j'ai traduit une phrase que je n'avais pas comprise sur **reverso**

Au final j'ai navigué sur près de **9 sites**, en revenant sur *Google* entre chaque recherche, mais aucune des recherches que j'ai faites n'avait de lien avec la précédente.

### Expérience 1 : on accepte tous les cookies

#### Résultats au global 

<img width=350 src=diagramme_cookie_1.webp>

Si on regarde les statistiques annoncées par le logiciel sur **ma navigation** :

- Sur les **9 sites visités**, **76%** d'entre eux ont déposé au moins un cookie.
- Ces cookies échangent potentiellement des informations avec **28 domaines tiers**

Si on se penche maintenant sur **l'usage des cookies**: 
<img width=350 src=diagramme_usage_cookies_1.webp>

{%info%}
- La **zone orange** indique la couverture de tiers déclarés comme *explicitement publicitaires* dans des fichiers ads.tx ayant déposé des cookies parmi les sites visités.
- La **zone violette** indique la couverture des tiers ayant déposé des cookies dont la finalité *n’est pas explicitement indiqué comme publicitaire* dans des fichiers ads.txt.
{%endinfo%}

On peut voir qu'il y a quand même beaucoup plus de violet que de orange dans ce diagramme...

#### Résultats au détails

- la pieuvre avec le plus de tentacules c'est **reverso**. Et les tentacules mènent à des domaines tiers très ciblés : *casalemedia*, *adnxs*, *smartadserver*, tous des domaines publicitaires. On retrouve également une tentacule liée à Amazon par le biais du domaine *amazon-adsystem*
- la seconde pieuvre avec le plus de tentacule c'est **asos**, étonnement ses tentacules mènent à de nombreux autres réseaux sociaux : on retrouve *facebook, instagram, snapchat, tiktok, pinterest* et d'autres. 

### Expérience 2: on refuse tous les cookies

#### Résultats au global 

<img width=350 src=diagramme_cookie_2.webp>

Si on regarde les statistiques annoncées par le logiciel sur **ma navigation** :

- Sur les **9 sites visités**, **89%** d'entre eux ont déposé au moins un cookie.
- Ces cookies échangent potentiellement des informations avec **13 domaines tiers**

Si on se penche maintenant sur **l'usage des cookies**: 
<img width=350 src=diagramme_usage_cookies_2.webp>

{%attention "Remarques"%}
- on passe de 76% à 86% de sites qui ont déposés des cookies en les refusant. *Un résultat qui me semble tout de même drôlement illogique. Même si cette information ne nous renseigne pas sur la réelle nature du cookie...*
- si on regarde le diagramme d'usage de cookies, on remarque que la zone violette **est beaucoup plus étendu quand on refuse les cookies**. On en déduit donc, que les cookies tiers ont tendance à être moins explicites quand on refuse les cookies. 
{%endattention%}

#### Résultats au détails

- on remarque que le pieuvre reverso a perdu beaucoup de ses tentacules, mais que certaines sont tenaces : notamment celle d'amazon adsystem, étonnamment.
- on remarque une deuxième pieuvre de google,*ce qui est cohérent avec le fait que j'accédé à chaque site depuis google.*

{%faire%}
Constat intriguant : sur le site de la **fnac** aucune bannière de consentement des cookies ne s'est affichée de toute ma navigation sur le site.
{%endfaire%}

---

{%info 'DoubleClick'%}
J'ai remarqué plusieurs fois l'apparition du cookie **DoubleClick** utilisé par Google pour sa régie publicitaire du même nom : il contrôle l’ensemble des campagnes publicitaires qui passent par cette régie. Il permet alors d’améliorer les performances de ces campagnes, et d’éviter que les publicités soient affichées plusieurs fois de suite.
{%endinfo%}

<h2 id=loi> Que dit la loi?</h2>
 
Les lois régissant l'utilisation des cookies varient selon les pays et les régions, mais en général, elles visent à protéger la vie privée des utilisateurs en ligne et à garantir qu'ils sont informés de manière transparente sur l'utilisation des cookies par les sites web qu'ils visitent. 

### Principes énoncés par le CNIL

- **Consentement** 
  - Les sites web doivent obtenir le consentement des utilisateurs **avant** le dépôt ou la lecture des cookies, et il doit être **re-demandé** à chaque fois qu'il est nécessaire. 
  - Le consentement doit donc être **libre, spécifique, éclairé, univoque** et donné **explicitement**
  - Chaque acteur recueillant le consentement doit être en mesure de prouver qu'il l'a fait *( captures d'écran horodatées, audits réguliers, conservation des informations sur les outils utilisés)
  - *L'acceptation des conditions générales d'utilisation ne suffit pas pour recueillir le consentement*
  - la simple poursuite de la navigation sur un site ne peut plus être considérée comme une expression valide du consentement de l’internaute
- **Transparence** 
  - Les utilisateurs doivent être **informés** la finalité des cookies utilisés, les données collectées et la manière dont elles sont utilisées, de manière **claire, complète et rédigée en termes simples et compréhensibles.**
- **Options de contrôle**
  - L'utilisateur doit avoir un **réel choix** entre accepter ou refuser les cookies, sans subir de préjudice en cas de refus.
  - l’utilisateur doit être en mesure de **retirer** son consentement, à tout moment, avec la **même simplicité** qu’il l’a accordé
- **Données personnelles**
  - Si les cookies collectent des données personnelles, les **lois sur la protection des données personnelles** peuvent également s'appliquer, ce qui signifie que les sites web doivent se conformer à des normes plus strictes en matière de collecte, de traitement et de protection de ces données.

En plus de ça, le CNIL a publié certaines *recommandations* à destinations des 
- Limiter la durée de vie des traceurs à treize mois sans prolongation automatique.
- Conserver les données collectées pendant vingt-cinq mois maximum.
- Réexaminer régulièrement ces périodes pour les limiter au strict nécessaire.

{%info '*Trop de consentement, tue le consentement*'%}
La multiplication de ces bannières, si elle a permis de rendre plus visible l’existence des traceurs, aboutirait, selon certains, à une **fatigue du consentement** qui signifierait, selon eux, que les internautes ne souhaitent pas que leur accord leur soit demandé.
Cependant, on remarque tout de même que **70 % des personnes** interrogées trouvent indispensable que les acteurs obtiennent leur accord avant qu’il soit possible de se servir de leurs données de navigation via des traceurs, même si cela prend un peu plus de temps dans la navigation. Signe supplémentaire de cette volonté de contrôle étroit de l’usage des traceurs, les personnes interrogées se prononcent massivement pour que les sites qu’elles fréquentent souvent leur redemandent un consentement à intervalles réguliers (77 % souhaitent ainsi qu’une nouvelle demande de consentement pour utiliser des traceurs ait lieu au moins tous les 3 mois).
{%endinfo%}

### Exceptions des cookies

Traceurs sont cependant exemptés du recueil de consentement, exemple :

- traceurs destinés à **l’authentification auprès d’un service**
- traceurs destinés à **garder en mémoire le contenu d’un panier d’achat** sur un site marchand
- traceurs visant à **générer des statistiques de fréquentation**
- traceurs permettant aux sites payants de **limiter l’accès gratuit** à un échantillon de contenu demandé par les utilisateurs.

{%prerequis "<u>Sources</u>"%}
https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies/que-dit-la-loi
https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies/lignes-directrices-modificatives-et-recommandation
https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookie-walls/publicite-ciblee-en-ligne-quels-enjeux-pour-la-protection-des-donnees-personnelles
https://www.cnil.fr/fr/la-loi-informatique-et-libertes#article82
{%endprerequis%}

### Cookie Walls

De nombreux services en ligne sont gratuits aujourd'hui, mais pas sans conséquence : les données personnelles des utilisateurs (âge, emplacement géographique, intérêts et comportements d'achat) sont souvent collectées, *via cookies et d'autres outils de suivi*, et utilisées par les entreprises du web pour financer ses services, principalement via la publicité ciblée.

{%info "Cookie Walls"%}
L’expression « murs de traceurs » *(ou « cookie walls » en anglais)* désigne le fait de conditionner l’accès à un service à l’acceptation par l’internaute du dépôt de cookies sur son terminal (ordinateur, smartphone, ...). 
{%endinfo%}

En cas de refus de ces *cookies*, certains sites ont recourt à la proposition d’un choix alternatif **l'internaute doit fournir une contrepartie** (*pour permettre aux éditeurs de ces site de compenser la perte de revenus publicitaires liée à cette absence de traceurs par un autre mode de rémunération*)

<u>**Solution**</u> :
Dans la majorité des cas, la contrepartie est **financière**, on parle alors de **paywall** : *l’internaute qui refuse d’accepter les cookies est obligé de payer pour accéder au site*. Exemple : on retrouve souvent cela sur des sites de magazines en lignes, qui proposent de *s'abonner* en cas de non consentement 

Les **Cookie Walls** ne sont pas interdits par principe, mais leur légalité dépend de plusieurs critères. En l'absence d'une législation spécifique ou d'une position de la Cour de justice de l'Union européenne, c'est la CNIL qui a établi et publié ces critères :

- **Alternative juste** : Les utilisateurs doivent avoir une vraie option pour accéder au site sans accepter les cookies.
- **Tarif raisonnable** : Si le site propose une option payante pour éviter les cookies, le prix doit être juste et justifié.
- **Transparence sur les données** : Si le site demande aux utilisateurs de créer un compte, il doit expliquer clairement pourquoi et limiter les données collectées.
- **Raisons des cookies** : Le site doit dire clairement pourquoi les cookies sont nécessaires pour accéder au service. Seules les raisons importantes sont acceptables.
- **Refus des cookies** : Normalement, si un utilisateur refuse les cookies, aucun ne devrait être utilisé. Mais dans quelques cas spéciaux, le site peut demander le consentement pour certaines fonctions spécifiques et nécessaires.

Si certains sont intéressés par le droit, le site du CNIL est bien étoffé à ce sujet, vous pouvez aller sur [cette page](https://www.cnil.fr/fr/les-procedures-de-sanction)

{%prerequis "<u>Sources</u>"%}
https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookie-walls
https://www.cnil.fr/fr/cookie-walls-la-cnil-publie-des-premiers-criteres-devaluation
{%endprerequis%}

### Scandale liés aux cookies

#### Facebook-Cambridge Analytica, en 2014

Ce scandale, souvent appelé la **fuite de données Facebook-Cambridge Analytica**, concerne les informations personnelles de **87 millions de personnes** sur Facebook, qu'une société britannique nommée Cambridge Analytica, a récupérées à partir de **2014**. Elle a ensuite utilisé ces informations pour influencer les campagnes politiques à grande échelle:

- lors des élections présidentielles aux États-Unis en 2016 
- lors du référendum sur le Brexit au Royaume-Uni.

Tout part d'un quiz de personnalité développé sur une application appelée "thisisyourdigitallife", conçue en 2014 par Aleksandr Kogan, un chercheur en psychologie affilié à l'Université de Cambridge. Environ 270 000 personnes ont téléchargé cette application sur Facebook, ce qui a permis de partager, sans leur consentement explicite, leurs données personnelles, ainsi que celles de leurs amis, avec l'application. Tout cela, en raison de la manière dont Facebook autorisait le partage de données à l'époque.

**Utilisation des données par Cambridge Analytica :** Cambridge Analytica a acheté ces données à Kogan, affirmant qu'elles seraient utilisées à des fins de recherche académique. Cependant, il a été révélé que les données ont été utilisées pour développer des profils psychographiques détaillés des électeurs, qui ont ensuite été utilisés pour cibler des messages politiques personnalisés
Le scandale Facebook-Cambridge Analytica est une affaire qui a éclaté en 2018 et qui a suscité de vives préoccupations quant à la protection de la vie privée des utilisateurs et à la manipulation des données personnelles à des fins politiques:

#### Yahoo, en 2023

29 décembre 2023, la CNIL a sanctionné la société YAHOO EMEA LIMITED d’une amende de 10 millions d’euros pour ne pas avoir respecté le choix des internautes qui refusaient les cookies sur son site « Yahoo.com » et ne pas avoir permis aux utilisateurs de sa messagerie « Yahoo! Mail » de librement retirer leur consentement aux cookies.

{%prerequis "<u>Sources</u>"%}
https://www.lesechos.fr/tech-medias/hightech/scandale-de-cambridge-analytica-facebook-accepte-de-payer-725-millions-de-dollars-1891714
https://fr.wikipedia.org/wiki/Scandale_Facebook-Cambridge_Analytica
{%endprerequis %}

### Conclusion

Comme on l'a vu, les cookies sont des fichiers **installés** sur nos ordinateurs, on peut donc facilement contrôler les **cookies tiers**, qui ne sont pas forcément nécessaires pour profiter des ressources disponibles sur Internet. Pour ce faire, on peut soit :
- **limiter l'utilisation des cookies** : dans les paramètres de notre navigateur / en utilisant la navigation privée.
- **effacer les cookies** déposés par les sites web sur notre appareil
*Pour le paramétrage des naviguateurs, la CNIL explique [sur cette page](https://www.cnil.fr/fr/cookies-et-autres-traceurs/comment-se-proteger/maitriser-votre-navigateur), toute la marche à suivre en fonction du naviguateur.*

### Horodateur
| Date | Heures passées | Indications |
| -------- | -------- |-------- |
| Mercredi 07/02 | 45min | *Définition du plan et recherches de ressources adaptées* |
| Samedi 02/03 | 1h30  | *Visionnage de plusieurs vidéos youtube et lectures d'articles internet pour définir précisément et simplement les cookies* |
| Dimanche 03/03 | 30min | *Recherches sur l'histoire des cookies* |
| Samedi 09/03 | 2h30 | *Découverte de CookieViz, installation, prise en main, réalisation d'une étude et analyse des résultats* |
| Dimanche 10/03 | 1h30 | *Recherche d'informations sur la loi concernant ce sujet, lecture des évolutions pénales, lectures de plusieurs articles sur des scandales passés, synthèses du résultat des recherches* |
| Lundi 11/03 | 1h | *Réalisation de l’entraînement "Récupérer un ID de session"* |
| Samedi 16/03 | 1h15 | *Recherches sur le sujet du ciblage publicitaire, visionnage de vidéos, et synthèse* |
| Dimanche 17/03 | 1h | *Recherche des conseils à appliquer lors d'une navigation sur internet, et synthèse des conseils les plus pertinents trouvés* |