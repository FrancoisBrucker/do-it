---
layout: layout/mon.njk

title: "Cryptographie"
authors:
  - ORY Victor

date: 2023-09-16

tags:
  - 'temps 1'
  - 'Cryptographie'
  - 'Math'
---
# Résumé :



## Ressources :

- [SubReddit dédié à la cryptologie ](https://www.reddit.com/r/crypto/wiki/index/)
- Si vous voulez des compléments, il y a aussi le [MON]() de Louradou 


## Pré-requis : 

{%prerequis 'Niveau prépa de Math'%}

Pré-requis :

- Probabilité math
- Volonté

 {%endprerequis%}

## Ce qu'on fait :

- Trouver les bonnes sources 


# Letsgo :

## 1 - Trouver les bonnes sources :

Après avoir récolté les informations du subreddit **r/cryptography**, on peut voir que les utilisateurs suivants et leur compte GitHub semblent sortir du lot d'après la communauté :
- [GitHub repo 1 : pFarb](https://github.com/pFarb)
- [GitHub repo 2 : sobolevn](https://github.com/sobolevn)

## 2 - À quoi ça sert ? 

La cryptographie est un outil puissant avec des limites qui a des applications dans beaucoup de technologies de communications et plus encore. Par exemple : 
  - La signature électronique
  - Les communications sécurisées ( HTTPS )
  - Sécuriser du contenu sur un disque 
  - ... 

## Petit rappel historique : 

L'encryptage existe depuis très longtemps et peut être simple.
Une table de substitution peut être utilisée pour encrypter un message.

Tableau de substitution : 

| A | B | C | ... | Z |
|---------------|---------------|---------------|
|  K   | Y   | F  | ... | T |


Toutefois cela est sensible à des attaques par fréquence, càd, repérer la lettre qui revient le plus souvent pour en déduire les équivalences de lettres. 
Ensuite, il y a eu des améliorations de ce processus à travers le temps toutefois même "énigma" a pu être crackée. 

## La partie triste : 

Il faut faire des math pour comprendre les trucs là .... 
Par exemple il va falloir faire appel aux probabilités discrètes, aux opérateurs logiques, notamment XOR. 

## La fonction de base : 

La fonction de base est le **XOR**, elle se comporte de la manière suivante : 

| A | B | XOR(A,B) |
|---------------|---------------|---------------|
|  0  | 0  | 0 | 
|  0  | 1  | 1 | 
|  1  | 0  | 1 | 
|  1  | 1  | 0 | 

Cette fonction, appliquée à un message, $$m$$, avec une clée, $$k$$, de longueur égale à celle du message permet de l'encrypter en un message, $$c$$. 

| m | 0 | 1 | 0 | 0 | 1 |
| k | 1 | 0 | 0 | 1 | 1 |
|---------------|---------------|---------------|---------------|---------------|
| c | 1 | 1 | 0 | 1 | 0 |



Ainsi, beaucoup de systèmes sont des déclinaisons de ce procédé comme par exemple WEP(wifi), HTTPS.
Toutefois, cette technique requiert que la clé soit de longueur au moins égale à celle du message ==> C'est chiant  ! 
Par conséquent un élément essentiels de ces algorithmes est le PRG ou Pseudo Random Generator, G, qui étends la clé k' de 6 bits en 64 bits comme ceci : $$G(k') = k $$ 

## Le block Sipher :

Cette technique s'appui sur une clé, $$k$$, qui va être divisé en n, étapes pour appliquer au message, m, n encryptages successifs. 

# Conclusion de ce cours théorique abandonné au bout de 4H 

C'est vachement mathématique et je pense que ce n'est pas exactement ce à quoi je voulais me confronter, c'était purement technique et peu informatif sur les pratiques liées à ces techniques. 


# Shift du sujet vers l'étude de la cryptographie vu comme un objet ou un outil : 

## Souveraineté 

Pour cela, je me suis basé sur les articles suivants dans un premier temps :

- [La cryptographie, socle de la souveraineté numérique](https://www-cairn-info.lama.univ-amu.fr/revue-defense-nationale-2022-10-page-59.htm)

Ainsi on comprend que la cryptographie permet de répondre à plusieurs contraintes :

- confidentialité des données, seul la personne concernées doit pouvoir les lire,
- intégrité, les données ne sont pas modifiables, important dans le secteur bancaire,
- authentification,
- preuve de non re-jeu,
- horodatage aveugle,
- l'éco-système des cryptomonnaies, 
- sécurisation d'un vote ,

J'ai particulièrement d'espoir en ces techniques pour protéger notre privée, ainsi des chercheurs travaillent sur des méthodes permettant de transmettre à un moteur de recherche une requête, cryptée, indiscernable par Google par exemple mais traitable. Ainsi Google ne perdrai aucune fonction mais ne serait plus capable de savoir ce vous avez recherché.

La maîtrise de la cryptologie est donc un enjeu majeur pour le secteur diplomatique et du renseignement. L'algorithme actuellement le plus utilisé et l'AES (Advanced Encryption Standard). Pour déterminer si un algorithme d'encryptage est bon il est nécessaire qu'il soit publique et peer-reviewed pour prouver l'absence de backdoor, ou bien créer soit même un algorithme secret. 

Pour l'évaluer, il est important que les données soit très confidentiel toutefois la vitesse d'encryptage est aussi essentiel pour un procédé de communication. 

La France a des compétences importantes dans le domaine de la recherche cryptographique avec notamment ses laboratoires utilisant déjà les techniques d'ordinateur quantique. Toutefois, nous restons à la merci des ricains qui ont déjà montré leur capacité à vendre des modèles avec des backdoors. 


### Géopolitique des données, la datasphère : 

Pour cette étude, j'ai parcourue la revue [Hérodote](https://www-cairn-info.lama.univ-amu.fr/revue-herodote-2020-2.htm) dédiée au sujet avec de multiples articles : 

- [Du cyberespace à la datasphère. Enjeux stratégiques de la révolution numérique](https://www-cairn-info.lama.univ-amu.fr/revue-herodote-2020-2-page-3.htm)

{note}
Bon article d'introduction
{endnote}

Postulat de base : + capteur, ++ données, Big Data ==> Big Analyse, ça a changé le monde : les acteurs, les outils et les processus.

{% info %}
Qu'est ce que la **datasphère** ? 

"désigne une nouvelle ère géologique caractérisée par l’incidence déterminante des activités humaines sur l’écosystème terrestre, à l’origine notamment du changement climatique." d'après « La sphère des données et le droit : nouvel espace, nouveaux rapports aux territoires », de Jean-Sylvestre Bergé.

Cela diffère du cyber-espace, décrit dans cet article comme : "un espace de menace à la sécurité nationale, un « territoire » à maîtriser et une priorité stratégique"

{% endinfo %}

Ainsi la difficulté est de définir ces espaces, leurs intersections et leurs acteurs parmi la multiplicité des dimensions ( physique avec les câbles sous-marins, production de software, stockage des données, ...).

Un enjeu est l'utilisation des ces technologies d'information pour influencer des masses : Nous sommes vulnérables à des manipulations politiques par les médias sociaux sur internet (cf Cambridge Analytica) avec des innovations importante. 

Ensuite, la souveraineté est aussi questionné à travers le **cloud computing¨**, mais aussi de la **5G** un enjeu au début économique et maintenant stratégique.
Et cela, devient un élément essentiel de la stratégie de puissance des pays comme le montre le comportement de l'Estonie, l'Israël, la Chine et la Russie en investissant.

### Focus sur le Cloud Computing et ses implications politique :

[Le cloud computing : de l’objet technique à l’enjeu géopolitique. Le cas de la France](https://www-cairn-info.lama.univ-amu.fr/revue-herodote-2020-2-page-149.htm)

{% faire %}
Un article qui va plus en profondeur du déroulé politique du cloud français et analyse vite fait les causes d'échec. 
{% endfaire %}

De base l'enjeu du cloud est économique, toutefois très vite la question de la sécurité des données s'est invitée. Ce shift dimenssionelle s'opère à partir de la crise de 2008 où la mondialisation est remise ne question.
Ainsi les critères de la confidentialité, de l’intégrité et de la disponibilité des données mettent en perspective imposent cette dimension politique et d'intelligence économique.
La France a tenté de lancer un projet de Cloud Souverain Andromède avec Thalès, Orange et Dassault dans le cadre de sa stratégie numérique. Toutefois ce projet fut un échec par incompétences des décideurs politiques et a nui au constructeurs français dans cette compétition internationale.
Après qqs années, en sorti de crise et après les révélations d'Edward Snowden, la volonté de relancer ce cloud souverain revient en 2015 avec d'autres acteurs plus spécialisé dans le cloud, notamment OVH. Toutefois, cela reste en second plan jusqu'en 2018, où il devient un élément essentiel à la modernisation des processus de l'État. 
{% faire "Définition de l'article"%}
Le cloud privé garantit la restriction de l’accès aux données grâce à l’isolation de l’infrastructure. Le cloud public permet davantage de flexibilité et de facilité d’usage mais son infrastructure, même si elle comporte de solides cloisonnements, est à disposition du grand public et est hébergée dans les locaux du fournisseur de services. Un déploiement hybride conjugue les avantages des deux modèles en permettant d’adapter la solution retenue au type de données hébergées et à leur niveau de sensibilité.
{% endfaire %}

Ensuite le CLOUD ACT, fait par l'administration de Trump, rend possible l'utilisation des données stockées par les fournisseurs de Cloud américains sous couvert de mandat. Cela remet fort en question l'utilisation de AWS, Azure par l'administration française et ses entreprises. Et cela efface les débats sur l'utilité d'un projet de cloud publique et se concrétise avec le cloud national stratégique.

## [La transformation numérique du ministère des Armées](https://www-cairn-info.lama.univ-amu.fr/revue-herodote-2020-2-page-165.htm)


{% faire %}
Un article dans la technique politique et pas la technique technique, se répète un peu avec les articles précédents, pas ouf
{% endfaire %}

Toujours dans cet environnement de révolution digitale, l'Armée a donc eu l'ambition dès 2008 de s'intéresser à :  l’Internet des objets, l’intelligence artificielle ou au big data. La gestion de données c'est important, on utilise des méthodes agiles et pas grand choses de plus. 