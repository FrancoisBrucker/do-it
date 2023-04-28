---
layout: layout/mon.njk

title: "Introduction au C++"

authors:
  - Jeffrey Edisah

date: 2023-03-23

tags:
  - 'temps 3'
  - 'info'
  - 'c++'

---

<!-- début résumé -->

Ce MON permet une introduction au C++. Il est fait en prévision de mon dernier MON de l'année.

<!-- fin résumé -->

Pour ce MON, je suis 2 cours OpenClassrooms afin de voir les bases du langage. Une expérience dans un langage de programmation, et plus particulièrement orienté objet type Java, ou bien Python. En effet dans ce MON, je vais essayer de comparer ce que j'ai trouvé d'unique avec le C++ par rapport à ces langages mais également par rapport au langage C.

Les tutoriels consultés :
- [Programmez en C++](https://openclassrooms.com/fr/courses/1894236-apprenez-a-programmer-en-c)
- [Orienté Objet en C++](https://openclassrooms.com/fr/courses/7137751-programmez-en-oriente-objet-avec-c)

### Mes raisons

Si je me lance actuellement dans ce MON, c'est car une partie non négligeable du code source de [Blender](https://www.blender.org/), sujet de mon dernier MON est en C++. Il est également en C et en Python mais j'ai déjà quelques connaissances dans ces langages alors que je suis assez démuni en C++. Or, ce langage est omniprésent dans les logiciels de modélisation 3D ainsi que dans le domaine du jeu vidéo, des domaines qui peuvent m'intéresser fortement à l'avenir.

## Documentation officielle

La première difficulté rencontré avec le C++ est la difficulté à trouver la documentation officielle. En effet sur Internet les liens ne sont pas autant mis en avant que les documentations de langages telles que [Python](https://docs.python.org/fr/3/) ou bien [Java](https://docs.oracle.com/en/java/). Pour C++ j'ai passé beaucoup de temps à chercher la documentation officielle avant de partir sur les tutoriels OpenClassrooms. Il s'avère que comme le langage C, la documentation C++ est disponible en livre, écrit par Bjorne Stroustrup, le créateur du langage. Le site qui se rapproche le plus d'une documentation officielle sur Internet est le site [isoC++](https://isocpp.org/) mais qui ne montre pas de point d'entrée rapide.

## Langage compilé

Tout comme le C, le C++ est un langage compilé, plus rapide, traduisant le programme en langage machine compréhensible pour elles. Ce qui veut dire que les programmes C++ doivent être recompilés sur chacune des machines où ils se trouvent avant de pouvoir être exécuté.

Les compilateurs sont abordés plus en détail dans ce [MON de Jean-Baptiste](../../../JBD/Mes_MON/compiler)

## Contrôle avancée de la mémoire

Le C++ comme le C permet un contrôle plus permissif sur la mémoire de la machine pour écrire les programmes. Ce contrôle plus avancée permet une meilleure efficacité en codant mais est aussi plus dangereux à manipuler. Je détaille ici les différents moyens mis à disposition par le langage pour ça.

### Typage des variables

Comme le C, le C++ est un langage typé avec différents types classiques (bool, int, char, double, etc...) qui permettent une allocation précise de la mémoire en fonction du type de la fonction, tout comme en C++ et en Java, et à l'inverse de Python ou de Javascript.

### Références

Le C++ introduit le concept de référence, qui comme son nom l'indique permet de référencer une variable déjà existante sans devoir lui attribuer une autre case mémoire. Les références sont utiles pour modifier directement les paramètres de fonction sans avoir à créer des variables locales pour effectuer nos calculs. Une référence se déclare comme ceci :

        int variable(0); 
        int& référence(variable);

### Pointeurs

Comme le C, le C++ continue à utiliser les pointeurs, c'est-à-dire des variables qui garde en mémoire les adresses mémoires vers d'autres variables. Ces pointeurs sont les outils de prédilection pour la gestion de la mémoire en C comme en C++. En effet à partir des pointeurs on peut accéder aux valeurs pointés et allouer la mémoire manuellement. Par contre, il est nécessaire de libérer la mémoire aussi, avant de supprimer le pointeur, sinon on perd de vue les variables considérés, et on risque de remplir la mémoire de la machine jusqu'au plantage. Voici le cycle de vie d'un pointeur.

        int *pointeur(0); //initialisation du pointeur
        pointeur = new int; //allocation mémoire d'un int
        *pointeur = 2; //affectation dans la précédente case mémoire
        delete pointeur; //libération de la case mémoire
        pointeur = 0; //pointeur ne pointe plus vers rien


## Conclusion

Le C++ est un langage plutôt difficile à mon avis, et nécessite une connaissance d'autres langages à priori avant de l’utiliser. Mais ce MON m'a permis une bonne mise à jour nécessaire pour le prochain MON.