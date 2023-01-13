---
layout: layout/post.njk

title: "Hacking-Guide"
authors:
  - Kasimir Romer
---
TODO: Überall Referenzen hinzufügen ("weiterlesen: ...")

## Introduction
### Hacking, n'est-ce pas une mauvaise chose ?
Le terme "hacking" a une connotation très négative pour de nombreuses personnes. Les hackers, ce sont pourtant ceux qui attaquent les ordinateurs et distribuent des virus. C'est vrai, ces personnes sont aussi des hackers, mais le terme est beaucoup plus large. Il est défini de manière très différente par de nombreuses personnes, pour moi un hacker est quelqu'un qui utilise un produit ou un outil d'une manière différente de celle prévue à l'origine.
Dans le domaine de la sécurité informatique, nous ne parlons pas de hackers, mais d'attaquants, car dans ce mot, il est directement clair qu'il s'agit de l'adversaire. Nous ne voulons certes pas devenir un attaquant, mais nous pouvons nettement mieux nous défendre si nous connaissons les techniques d'attaque et si nous pouvons nous y préparer. Si nous pensons comme un attaquant, nous avons plus de chances de le devancer. C'est pourquoi il est important de connaître les techniques d'attaque ("savoir hacker").

### CTFs
CTF est l'abréviation de "Capture the Flag", à l'origine un jeu dans le monde réel dans lequel il s'agit de voler le drapeau de l'autre équipe. Dans le contexte de la sécurité informatique, il s'agit d'un jeu dans lequel il faut trouver des messages cachés (flags) sur les systèmes informatiques. Les CTF sont donc une manière ludique d'apprendre et d'appliquer différentes techniques de sécurité informatique, puisque ces techniques sont nécessaires pour trouver les drapeaux.
Dans le monde réel, il n'y a pas beaucoup de possibilités d'essayer des techniques de piratage, car c'est illégal si l'autre partie n'est pas d'accord. C'est pourquoi les CTF sont un excellent moyen de tester et d'étendre légalement ses connaissances en matière de piratage.
En principe, il existe deux types de CTF : Jeopardy et Attack-Defense. Dans les CTF Jeopardy, on joue seul ou en équipe et on essaie de trouver des drapeaux sur les systèmes informatiques. Dans le cas d'Attack-Defense, deux équipes jouent l'une contre l'autre. Elles reçoivent chacune un réseau avec des points faibles, disposent d'un certain temps pour sécuriser le réseau et tentent ensuite d'attaquer le réseau de l'adversaire. L'équipe gagnante est celle qui parvient à pénétrer plus avant dans le réseau adverse.
Les techniques apprises ici sont utiles pour les deux types de CTF, mais au début, on se concentrera plutôt sur les CTF de type Jeopardy.

### Prérequis
{% prerequis %}
Pour tirer le maximum de ce cours, les connaissances préalables suivantes sont nécessaires :
- Utilisation de base de la ligne de commande
- Savoir googler - tu dois savoir comment reconnaître les bons résultats de recherche et comment cibler les choses dont tu as besoin.
Tout le reste s'apprend ici ou dans la pratique, c'est-à-dire dans les CTF. Comme on peut le constater, les obstacles à l'entrée sont très faibles.
{% endprerequis %}

### Sur ce document
Ce document a été réalisé dans le cadre d'un POK dans le parcours ["Do-It"](../../../about/index) à l'EC Marseille. Le choix des thèmes est plus ou moins arbitraire, il ne prétend expressément pas à l'exhaustivité. Il doit s'agir d'un recueil de thèmes intéressants pour les participants et qu'ils peuvent mettre en pratique. Il n'y aura pas d'explication approfondie des sujets, mais seulement une brève introduction et quelques liens vers des informations complémentaires. Les participants devront se former de manière autonome et approfondir les sujets. Il s'agit d'une introduction aux technologies de base du hacking, de sorte que l'on puisse avoir un aperçu de tout ce qui est possible dans ce domaine.
Ce document est ouvert à l'extension, afin que les lecteurs puissent y trouver davantage d'informations à l'avenir. 

{% exercice %}
À certains endroits du document, il y a des blocs comme celui-ci. Dans ceux-ci, je place de petites tâches qui doivent inciter le lecteur à travailler lui-même sur les sujets. Les tâches ne sont pas nécessaires à la compréhension du document, mais elles permettent d'approfondir les connaissances acquises. Les tâches ne sont pas évaluées, il n'y a pas non plus de solutions.
{% endexercice %}

## Outils importants
Les différentes tâches à accomplir lors d'un CTF nécessitent des outils, des sites web et des programmes très différents. Je les expliquerai à chaque fois que le contexte s'y prêtera. Certains outils sont toutefois si importants que je souhaite les présenter ici :

### Kali Linux
Kali Linux est une distribution Linux spécialement conçue pour les tests d'intrusion et le piratage. Elle contient de nombreux outils utiles pour le travail d'un hacker. La distribution est gratuite et peut être téléchargée [ici](https://www.kali.org/downloads/). Je recommande d'utiliser Kali dans une machine virtuelle, par exemple dans VirtualBox. Pour cela, il existe [ici](https://www.kali.org/get-kali/) des images déjà prêtes. Celle-ci peut être facilement importée dans VirtualBox, les identifiants sont `kali:kali`.
{% faire %}
TODO Kasimir: es gibt auch andere OSes, das kurz erklären (Linux quasi zwingend notwendig, aber man kann die Tools auch woanders installieren oder z.B. ParrotOS nutzen)
{% endfaire %}

### Ligne de commande
De très nombreuses tâches sont traitées en ligne de commande, c'est pourquoi il est nécessaire de connaître les commandes de base comme `cd`, `ls` ou `cat`. Il y a beaucoup de bons tutoriels sur Internet qui t'introduisent à la ligne de commande, par exemple [ici](https://www.youtube.com/watch?v=5XgBd6rjuDQ). Si tu vois quelque part une commande en ligne de commande avec des paramètres et que tu ne sais pas ce qu'une commande fait exactement, tu peux le vérifier ici : https://explainshell.com/ - ce site t'explique la signification de chaque paramètre. 

### "Couteau de poche suisse": CyberChef
L'outil CyberChef (https://gchq.github.io/CyberChef/) est un véritable touche-à-tout. Les fonctions dont on a souvent besoin pour les CTF sont par exemple la conversion de/en base64, hex ou binaire, le décryptage, la détection des données intégrées, etc. L'avantage de CyberChef est qu'il maîtrise non seulement toutes ces fonctions, mais qu'il est également possible de les enchaîner, par exemple en décodant d'abord une chaîne de caractères en base64, en la dézippant et en affichant ensuite le fichier résultant. Il existe bien sûr d'autres outils pour ces tâches, mais à mon avis, CyberChef offre le meilleur choix, une interface épurée et est facile à utiliser.
{% faire %}
TODO Kasimir: TryHackMe AoC2022 Day 7 - sehr ausführliche Erklärung für CyberChef
{% endfaire %}

{% exercice %}
TODO ici, on va trouver une exercise après
{% endexercice %}
