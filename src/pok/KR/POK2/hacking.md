---
layout: layout/post.njk

title: "Hacking-Guide"
authors:
  - Kasimir Romer
---
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
Ce document a été réalisé dans le cadre d'un POK dans le parcours ["Do-It"](../../../../about/index) à l'EC Marseille. Le choix des thèmes est plus ou moins arbitraire, il ne prétend expressément pas à l'exhaustivité. Il doit s'agir d'un recueil de thèmes intéressants pour les participants et qu'ils peuvent mettre en pratique. Il n'y aura pas d'explication approfondie des sujets, mais seulement une brève introduction et quelques liens vers des informations complémentaires. Les participants devront se former de manière autonome et approfondir les sujets. Il s'agit d'une introduction aux technologies de base du hacking, de sorte que l'on puisse avoir un aperçu de tout ce qui est possible dans ce domaine.
Ce document est ouvert à l'extension, afin que les lecteurs puissent y trouver davantage d'informations à l'avenir. 

{% exercice %}
À certains endroits du document, il y a des blocs comme celui-ci. Dans ceux-ci, je place de petites tâches qui doivent inciter le lecteur à travailler lui-même sur les sujets. Les tâches ne sont pas nécessaires à la compréhension du document, mais elles permettent d'approfondir les connaissances acquises. Les tâches ne sont pas évaluées, il n'y a pas non plus de solutions.
{% endexercice %}

## Outils importants
Les différentes tâches à accomplir lors d'un CTF nécessitent des outils, des sites web et des programmes très différents. Je les expliquerai à chaque fois que le contexte s'y prêtera. Certains outils sont toutefois si importants que je souhaite les présenter ici :

### Kali Linux
Kali Linux est une distribution Linux spécialement conçue pour les tests d'intrusion et le piratage. Elle contient de nombreux outils utiles pour le travail d'un hacker. La distribution est gratuite et peut être téléchargée [ici](https://www.kali.org/downloads/). Je recommande d'utiliser Kali dans une machine virtuelle, par exemple dans VirtualBox. Pour cela, il existe [ici](https://www.kali.org/get-kali/) des images déjà prêtes. Celle-ci peut être facilement importée dans VirtualBox, les identifiants sont `kali:kali`.

Il n'est toutefois pas obligatoire d'utiliser Kali Linux. Il existe d'autres distributions qui remplissent le même objectif, par exemple ParrotOS. Mais il est également possible d'utiliser des installations Linux standard, dans ce cas, les outils nécessaires peuvent être facilement téléchargés et installés. Il est seulement important d'utiliser Linux, car la plupart des outils ne sont pas développés pour Windows.
Kali Linux s'est entre-temps quasiment imposé comme standard.

### Ligne de commande
De très nombreuses tâches sont traitées en ligne de commande, c'est pourquoi il est nécessaire de connaître les commandes de base comme `cd`, `ls` ou `cat`. Il y a beaucoup de bons tutoriels sur Internet qui t'introduisent à la ligne de commande, par exemple [ici](https://www.youtube.com/watch?v=5XgBd6rjuDQ). Si tu vois quelque part une commande en ligne de commande avec des paramètres et que tu ne sais pas ce qu'une commande fait exactement, tu peux le vérifier ici : https://explainshell.com/ - ce site t'explique la signification de chaque paramètre. 

### "Couteau de poche suisse": CyberChef
L'outil CyberChef (https://gchq.github.io/CyberChef/) est un véritable touche-à-tout. Les fonctions dont on a souvent besoin pour les CTF sont par exemple la conversion de/en base64, hex ou binaire, le décryptage, la détection des données intégrées, etc. L'avantage de CyberChef est qu'il maîtrise non seulement toutes ces fonctions, mais qu'il est également possible de les enchaîner, par exemple en décodant d'abord une chaîne de caractères en base64, en la dézippant et en affichant ensuite le fichier résultant. Il existe bien sûr d'autres outils pour ces tâches, mais à mon avis, CyberChef offre le meilleur choix, une interface épurée et est facile à utiliser.

{% exercice "**Exercice**" %}
Sur la plateforme de hacking "TryHackMe", il y a une très bonne explication et une tâche pour CyberChef. Je vous conseille de la lire et d'effectuer la tâche : https://tryhackme.com/room/adventofcyber4# -> Task 12 (Day 7)
{% endexercice %}

## Reconnaisance
La reconnaissance est la première étape d'un CTF. Il s'agit de collecter des informations sur la cible, de trouver des vulnérabilités et de trouver des points d'entrée. Il existe de nombreuses techniques de reconnaissance, mais les plus importantes sont les suivantes :

### Nmap
Nmap est un outil de reconnaissance de réseau. Il permet de scanner des adresses IP et de trouver des ports ouverts. Il est possible de scanner des adresses IP individuelles, des plages d'adresses IP ou des réseaux entiers. Nmap peut également être utilisé pour détecter des vulnérabilités. Il existe de nombreuses options pour Nmap, mais les plus importantes sont les suivantes :
- `-sS` : scan TCP SYN
- `-sV` : détecte les services qui tournent sur les ports
- `-p` : spécifie les ports à scanner (par exemple `-p 1-1000` pour scanner les ports 1 à 1000)
- `-oN` : enregistre le résultat dans un fichier texte (par exemple `-oN resultat.txt`)
- et beaucoup d'autres que vous pouvez trouver [dans le manuel](https://nmap.org/book/man-briefoptions.html)

{% exercice "**Exercice**" %}
1. Nmap met à disposition un serveur de test sur lequel on peut tester différentes fonctions de nmap. Le serveur se trouve sous scanme.nmap.org - Découvre quels ports sont ouverts et quels services y sont exécutés.
2. analyse ton réseau domestique (pas le réseau de l'école ou d'autres réseaux - c'est illégal). Tu trouveras peut-être des ports que tu ne connais pas.
{% endexercice %}

### Dirb
Dirb (directory buster) est un scanner de contenu Web. Il recherche les objets Web existants (et/ou cachés). Il fonctionne essentiellement en lançant une attaque basée sur un dictionnaire contre un serveur Web et en analysant les réponses.
Dirb est livré avec un ensemble de listes de mots d'attaque préconfigurées pour une utilisation facile mais vous pouvez utiliser vos propres listes de mots. Il existe de nombreuses options pour Dirb, mais les plus importantes sont les suivantes :
- `-w` : spécifie le dictionnaire à utiliser
- `-o` : enregistre le résultat dans un fichier texte

Une ligne de commande typique pour Dirb ressemble à ceci :
```bash
dirb http://adresse_web -w /usr/share/dirb/wordlists/common.txt -o resultat.txt
```

### Shodan
Shodan est un moteur de recherche pour les appareils connectés à l'internet (appareils IoT). Il permet aux utilisateurs de trouver et d'accéder à des appareils tels que des webcams, des routeurs, des serveurs et des systèmes de contrôle industriel, entre autres, qui sont connectés à l'internet. Contrairement aux moteurs de recherche traditionnels qui indexent les sites web, Shodan indexe des informations sur les appareils qui composent l'internet, notamment le type d'appareil, son emplacement et les ports ouverts. Ces informations peuvent être utiles aux chercheurs en sécurité et aux testeurs de pénétration pour identifier les vulnérabilités et les vecteurs d'attaque potentiels. En outre, elles peuvent être utilisées par les organisations pour identifier et surveiller les appareils connectés à leurs réseaux, ainsi que par les particuliers pour surveiller leurs propres appareils et vérifier s'ils sont exposés à l'internet. 
Shodan se trouve à l'adresse suivante : https://www.shodan.io/

## Passwort-Cracking
Le cracking de mot de passe est une méthode utilisée pour découvrir les mots de passe d'un compte ou d'un système protégé. Il existe plusieurs techniques de cracking de mot de passe, notamment la force brute, la dictionnaire et l'attaque par phishing. La force brute consiste à tester toutes les combinaisons possibles jusqu'à ce que le mot de passe soit trouvé. La méthode de dictionnaire consiste à utiliser une liste prédéfinie de mots de passe couramment utilisés. L'attaque par phishing consiste à tromper l'utilisateur pour qu'il révèle son mot de passe. Il est important de noter que le cracking de mot de passe illégal et peut entraîner des poursuites judiciaires. Il est donc important de s'assurer d'avoir l'autorisation avant de procéder à un cracking de mot de passe. Il est préférable de se concentrer sur la sensibilisation à la sécurité et sur la mise en place de bonnes pratiques de gestion des mots de passe pour éviter les risques de cracking.

### Listes de mots de passe
Il existe de nombreuses listes de mots de passe disponibles sur Internet. Ceux-ci contiennent souvent les mots de passe les plus fréquemment utilisés dans le passé. La célèbre liste de mots de passe _rockyou.txt_ contient plus de 14 millions de mots de passe. Elle a été publiée en 2009 par un pirate informatique qui l'avait volée sur un serveur (de la site web "RockYou" - d'où le nom). La liste est disponible publiquement et peut être téléchargée sur GitHub. En outre, elle est déjà déposée dans Kali Linux. Cette liste est souvent le point de départ d'attaques par bruteforce de mots de passe.
Ici sont les 15 mots de passe les plus courants de la liste _rockyou.txt_ :
```markup
123456
12345
123456789
password
iloveyou
princess
1234567
rockyou
12345678
abc123
nicole
daniel
babygirl
monkey
lovely
```
Il est également possible de créer soi-même des listes de mots de passe, par exemple pour générer des mots de passe composés d'un mot et d'un chiffre spécifiques. L'outil _cewl_ peut être utilisé pour extraire des possibles mots de passe du texte source d'une page web. L'outil _crunch_ peut être utilisé pour créer des listes de mots de passe à partir de chaînes de caractères prédéfinies.

### John the Ripper et Hashcat
John the Ripper est un outil populaire pour cracker les mots de passe. Il est capable de cracker des mots de passe sur différents systèmes d'exploitation et peut utiliser différentes méthodes pour deviner les mots de passe, comme la force brute ou la méthode de dictionnaire. Il peut également utiliser des modules pour cracker des mots de passe cryptés spécifiques, tels que des mots de passe salés ou des mots de passe cryptés avec des algorithmes de hachage tels que MD5 et SHA. John the Ripper peut être utilisé de manière interactive ou en mode script pour automatiser les tâches de cracking de mot de passe. Il est important de noter que l'utilisation de John the Ripper peut violer les termes d'utilisation et les lois sur la sécurité informatique. Il est donc important de s'assurer d'avoir l'autorisation avant d'utiliser cet outil.

Hashcat fait des choses similaires à John the Ripper, mais il est plus rapide et plus efficace sur une GPU (John the Ripper est optimisé pour les CPU). En outre, les deux outils se distinguent naturellement dans d'autres domaines tels que les types de hachage pris en charge ou les intégrations/scripts de tiers. Mais en principe, ils sont tous deux à classer dans la catégorie des "outils de craquage de mots de passe".

## Criminalistique numérique
Dans les événements CTF, les défis de la criminalistique numerique impliquent généralement l'analyse d'une image ou d'un fichier fourni pour découvrir des drapeaux ou des indices cachés. Ces défis peuvent aller du simple découpage de fichiers à l'analyse plus complexe de la mémoire. Pour réussir les défis d'analyse scientifique, il est important de bien comprendre les différents outils et techniques d'analyse scientifique disponibles, ainsi que d'être capable de penser de manière critique et méthodique. Dans ce chapitre, nous allons couvrir les bases de l'analyse forensique et présenter certains des outils et techniques forensiques les plus couramment utilisés.

### Outils intégrés
Il existe plusieurs outils d'analyse légale de base qui sont couramment utilisés sur les systèmes Linux pour analyser et étudier les données. Certains de ces outils incluent :

**file** : Cet outil est utilisé pour identifier le type de fichier en fonction de son contenu. Il peut être utilisé pour déterminer si un fichier est une image, un document texte ou un exécutable, par exemple.
```bash
$ file ~/Downloads/flag.png
~/Downloads/flag.png: PNG image data, 800 x 600, 8-bit/color RGB, non-interlaced
```

**strings** : Cet outil est utilisé pour extraire des chaînes de caractères imprimables d'un fichier. Il peut être utile pour identifier des mots-clés ou du texte dans un fichier qui peuvent être pertinents pour une enquête.
```bash
$ strings ~/Downloads/flag.png
libc.so.6
puts
/=*"H
Enter key
flag{strings_are_useful}
__cxa_finalize
```

**dd** : Cet outil est utilisé pour effectuer des copies au niveau des bits de supports de stockage, tels que des disques durs ou des clés USB. Il peut être utilisé pour créer une copie exacte d'un périphérique de stockage à des fins d'analyse médico-légale.
Cette commande va créer une copie exacte de l'ensemble du disque dur /dev/sda et l'enregistrer dans le fichier /path/to/image.dd :
```bash
$ dd if=/dev/sda of=/path/to/image.dd bs=1M
```

**grep** : Cet outil est utilisé pour rechercher des motifs ou du texte spécifiques dans un fichier ou un groupe de fichiers. Il peut être utilisé pour rechercher des mots-clés ou des chaînes de texte spécifiques dans un fichier.
```bash
$ grep "example" /path/to/file
example text found on line 10
```

**hexdump** : Cet outil est utilisé pour afficher le contenu d'un fichier au format hexadécimal. Il peut être utile pour identifier des modèles hexadécimaux dans un fichier qui peuvent être pertinents pour une enquête.

**md5sum** : Cet outil est utilisé pour vitement calculer le hachage MD5 d'un fichier. Un hachage est une représentation unique du contenu d'un fichier, et peut être utilisé pour vérifier l'intégrité d'un fichier ou pour identifier si deux fichiers sont identiques.
```bash
$ md5sum ~/Downloads/flag.png
a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4  /home/user/Downloads/flag.png
```

### Wireshark
Wireshark est un logiciel de capture de paquets et d'analyse réseau. Il permet aux utilisateurs de capturer les paquets réseau en utilisant les protocoles de la couche 2 et 3 du modèle OSI, et de les analyser pour identifier les erreurs, les anomalies et les attaques. Wireshark est capable de capturer des paquets en utilisant différents protocoles de réseau tels que TCP, UDP, HTTP, FTP, SSH, etc. Il est également capable d'analyser des fichiers de capture de paquets (.pcap) pour identifier les anomalies et les attaques. Les fichiers pcap sont souvent utilisés dans les CTF (Capture the Flag) pour tester les compétences en sécurité des participants et pour analyser les captures de paquets réseau. 

{% exercice "**Exercice**" %}
1. Capturez des paquets sur votre propre réseau : Utilisez Wireshark pour capturer des paquets sur votre propre réseau domestique ou professionnel. Analysez les paquets pour mieux comprendre les différents protocoles et services utilisés.
2. Analysez les fichiers PCAP : Téléchargez des fichiers PCAP à partir de ressources en ligne telles que le [Wireshark sample wiki] (https://wiki.wireshark.org/SampleCaptures), et utilisez Wireshark pour analyser les paquets.
{% endexercice %}

### Sleuth Kit
Le Sleuth Kit est un ensemble d'outils open-source pour l'analyse forensique de systèmes de fichiers. Il permet aux utilisateurs de lire les systèmes de fichiers couramment utilisés, tels que NTFS, FAT, ext2/3/4, et UFS, et de les analyser pour récupérer des informations telles que les fichiers supprimés, les journaux d'événements et les informations de métadonnées. Il peut également être utilisé pour analyser les images de disques durs et les fichiers de sauvegarde. Le Sleuth Kit est souvent utilisé en conjonction avec l'outil Autopsy pour fournir une interface graphique à l'analyse des données. Il est un outil important pour les professionnels de la sécurité informatique et les enquêteurs pour récupérer des données et des informations cachées.

## Exploiter les vulnérabilités
Pour obtenir un accès root sur un système (souvent la cible d'un CTF), il faut exploiter des vulnérabilités qui ont été trouvées auparavant (par exemple par nmap). Il est possible de développer soi-même le code d'expoloitation, mais pour de nombreuses vulnérabilités, il existe déjà de nombreuses "charges utiles" prêtes à l'emploi qu'il suffit d'exécuter.

### Metasploit
Une fois les vulnérabilités identifiées, Metasploit peut être utilisé pour explorer les vulnérabilités en utilisant des modules d'exploitation prédéfinis. Il est également possible de développer des scripts personnalisés pour automatiser des actions spécifiques. Metasploit permet également de créer des payloads pour installer des backdoors sur le système cible, afin de maintenir une connexion à distance pour une utilisation ultérieure. Pour une utilisation efficace de Metasploit, il est important de comprendre les différentes options et fonctionnalités de l'outil et de rester à jour avec les dernières vulnérabilités connues.

Une fois que vous avez une session active avec Metasploit, vous pouvez utiliser différentes commandes pour naviguer dans les différentes options. La commande "show" permet d'afficher les différents modules disponibles, tandis que la commande "use" permet de sélectionner un module spécifique pour l'utiliser. Il est également possible de chercher des modules spécifiques en utilisant la commande "search", en utilisant des mots-clés pertinents tels que le nom de la vulnérabilité ou le système d'exploitation cible. Une fois que vous avez sélectionné un module, vous pouvez utiliser la commande "show options" pour afficher les options disponibles et configurer les options nécessaires pour l'exploitation. Enfin, pour lancer l'exploitation, vous pouvez utiliser la commande "exploit". Il est important de noter que l'utilisation de Metasploit peut violer les termes d'utilisation et les lois sur la sécurité informatique. Il est donc important de s'assurer d'avoir l'autorisation avant de lancer des attaques.

L'ensemble des fonctionnalités est décrit dans la documentation : https://docs.metasploit.com/

{% exercice "**Exercice**" %}
Bien entendu, il ne faut pas attaquer n'importe quel système avec Metasploit, même si cela est théoriquement possible. C'est pourquoi TryHackMe a créé une bonne introduction que l'on trouve ici : https://tryhackme.com/room/metasploitintro
Travaille sur cette pièce et essaie de résoudre les tâches qui s'y trouvent.
{% endexercice %}

## Perspectives
Ce guide de CTF est conçu pour vous donner un aperçu des différentes catégories de défis que vous pourriez rencontrer lors d'un événement CTF. Cependant, il est important de noter que les informations présentées dans ce guide ne représentent qu'une petite partie de toutes les possibilités. Chaque défi CTF est différent, et il est probable que vous rencontriez des exercices qui ne rentrent pas dans les catégories présentées. La chose la plus importante est de savoir utiliser les moteurs de recherche correctement et de trouver les informations nécessaires. La plupart des informations dont vous avez besoin sont déjà disponibles en ligne. Il est donc essentiel de développer vos compétences de recherche et de savoir où trouver les informations dont vous avez besoin pour résoudre les défis CTF.

### Autres sujets
Nous n'avons malheureusement pas eu le temps d'aborder les thèmes suivants dans ce guide. Ils n'en sont pas moins très importants et devraient être traités à l'avenir :
- **Cryptographie** : La cryptographie est l'étude des techniques pour protéger l'information en utilisant des algorithmes mathématiques. Dans les CTF, les défis de cryptographie peuvent inclure la cassage de chiffrements, la recherche de faiblesses dans les protocoles de cryptographie et la mise en place de systèmes de cryptographie.
- **Exploitation Web** : L'exploitation web consiste à identifier et à utiliser les vulnérabilités présentes dans les applications web pour obtenir un accès non autorisé ou pour exécuter des actions malveillantes. Dans les CTF, les défis d'exploitation web peuvent inclure la recherche de faiblesses dans les applications web, la détection de injections SQL et la mise en place de phishing.
- **Reverse Engineering** : Le reverse engineering consiste à décompiler et à analyser le code d'un logiciel pour comprendre son fonctionnement et identifier les vulnérabilités. Dans les CTF, les défis de reverse engineering peuvent inclure la décompilation de programmes binaires, la recherche de faiblesses dans les programmes et la mise en place de contre-mesures pour protéger les programmes contre les attaques.