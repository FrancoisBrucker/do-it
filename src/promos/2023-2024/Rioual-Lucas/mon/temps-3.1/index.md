---
layout: layout/mon.njk

title: "Symfony 6"
authors:
  - Lucas Rioual

date: 1970-09-01

tags: 
  - "temps 3"
  - "symfony 6"
  - "php"


résumé: "Découverte du framework Symfony 6"
---





{% prerequis %}
**PHP, Docker(mieux mais pas indispensable), Programmation orienté objet**
{% endprerequis %}

L'objectif de ce MON est de me former sur un framworks PHP : Symfony. Pourquoi ce Frameworks ? Parce qu'il est beaucoup utilisé dans l'entreprise dans laquelle je vais faire mon stage.
Pour cela, je vais suivre le livre sur symfony 6 : https://symfony.com/book en parallèle de la doc officielle https://symfony.com/doc/current/index.html.


## Présentation du projet

Le projet proposé dans le livre [https://symfony.com/book](https://symfony.com/book) de Symfony 6 est une plateforme web qui  a pour but d'obtenir un retour d'expérience sur des conférences. Une sorte de livre d’or. Il y a une liste des conférences sur la page d'accueil ainsi qu'une page pour chacune d'entre elles.

Il y a également une page admin qui permet d’ajouter, supprimer ou modifier les conférences et les commentaires présents sur le site.

La base de donnée utilisé dans le livre est PostgreSQL mais nous n’avons pas besoin de connaissance sur cet outil pour comprendre le livre. Le livre se concentre vraiment sur l’API.

En plus de tout ça, le livre explique comment mettre notre application en production grâce à [Platform.sh](http://Platform.sh) . J’ai sauté le chapitre sur ça, car il fallait prendre un abonnement payant pour la mise en production.

Le livre est très dense avec beaucoup d’information. Pendant ce MON, j’ai eu le temps de parcourir que la moitié du livre.

## Set up du projet

J’ai mis beaucoup de temps à installer tous les outils nécessaires pour lancer symfony. Je vais présenter ici les étapes nécessaires à l’installation du projet pour Windows.

### PHP

Tout d’abord il faut installer PHP. Il faut aller sur le ce site [https://windows.php.net/download#php-8.3](https://windows.php.net/download#php-8.3), et télécharger le zip x64 Thread Safe. 

Ensuite, il faut ajouter le contenu zip dans sa variable d’environnement PATH. Voilà comment faire : [https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/)

Ensuite, dans le dossier PHP, il faut dupliquer le fichier php.ini-development et renommer le nouveau fichier php.ini. C’est ce fichier qui indiquera les extensions nécessaires au projet. Pour ajouter une dépendance, il faut décommenter la ligne associée.
Voici les extension à décommenter :

 

```bash
extension=curl
extension=gd
extension=intl
extension=mbstring
extension=openssl
extension=pdo_pgsql

; The MIBS data available in the PHP distribution must be installed.
; See https://www.php.net/manual/en/snmp.installation.php

extension=sodium
extension=xsl
extension=zip
```

On peut vérifier l’installation de php avec la commande 

```bash
php --version
```

### **Composer**

[Composer](https://getcomposer.org/) permet de gérer les dépendances du projet. Pour l’installer, il faut télecharger le Composer-setup.exe depuis ce site [https://getcomposer.org/download/](https://getcomposer.org/download/)

Normalement, cela ajoute directement Composer à la variable PATH.
On peut vérifier que l’installation s’est bien passée :

```bash
composer --version
```

### Node.js/Docker/Docker Compose

Je n’ai pas eu de souci car ils étaient déjà installé sur ma machine. Il faut suivre les sites officiels :

[NodeJS](https://nodejs.org/) et [Docker](https://docs.docker.com/install/)

### Symfony CLI

Symfony CLI permet d’accroitre la productivité en permettant d’écrire du code gâce à des lignes de commandes.

Installez la [commande symfony](https://symfony.com/download). Il faut installer le Binaries amd64 et ajouter le contenu du fichier télécharger dans la variable PATH.

Ensuite, comme écrit dans le livre, pour pouvoir utiliser HTTPS localement, nous avons également besoin d'`installer une autorité de certification` :

`$ symfony server:ca:install`

Maintenant dernière étape pour savoir si on a tout bien installé :
`symfony book:check-requirements`

Si on a tout fait correctement, on doit avoir cette réponse :

```bash
C:\Users\utilisateur>symfony book:check-requirements
[OK] Git installed
[OK] PHP installed version 8.3.3 (C:\PHP\php.exe)
[OK] PHP extension "tokenizer" installed - required
[OK] PHP extension "xml" installed - required
[OK] PHP extension "mbstring" installed - required
[OK] PHP extension "xsl" installed - required
[OK] PHP extension "openssl" installed - required
[OK] PHP extension "zip" installed - optional - needed only for chapter 17 (Panther)
[OK] PHP extension "intl" installed - required
[OK] PHP extension "pdo_pgsql" installed - required
[OK] PHP extension "curl" installed - optional - needed only for chapter 17 (Panther)
[OK] PHP extension "gd" installed - optional - needed only for chapter 23 (Imagine)
[OK] PHP extension "redis" not found, optional - needed only for chapter 31
[OK] PHP extension "amqp" not found, optional - needed only for chapter 32
[OK] PHP extension "json" installed - required
[OK] PHP extension "session" installed - required
[OK] PHP extension "ctype" installed - required
[OK] PHP extension "sodium" installed - required
[OK] Composer installed
[OK] Docker installed
[OK] Docker Compose installed
[OK] npm installed

                                                                                                                        
 [OK] Congrats! You are ready to start reading the book.                                                                
                                                                                                                        

```

## Mon retour sur le livre

Je ne vais pas détaillé les autres chapitres du livre car je ne vais pas mieux expliquer que l’auteur, qui est le créateur de Symfony.  J’ai eu le temps de faire les 14 premiers chapitres du livre. 

Durant ces chapitres, on voit comment créer des controleurs, des entity et des repository, comment faire une page admin CRUD qui communique avec la base de donnée ou comment utiliser twig pour des templates HTML.

Il y a beaucoup de concept différents à assimiler. Il faut être à l’aise sur la programmation orienté objet, bien connaître PHP ou encore le concept de routage et controleurs .
Personnellement, je ne connaissais pas bien PHP. Je devais m’arrêter sans cesse pour me documenter sur les concepts PHP.

Le cours de Java, Spring Boot m’a permis de mieux appréhender certains concepts comme les controleurs, les repository et les entity qu’on retrouve dans Symfony.

Je conseille Symfony et ce livre pour des personnes qui ont déjà un bon bagage en développement web. Parce qu’il repose sur pas mal de prérequis qui j’ai listé en haut.

Voici le repo github de ce que j'ai fait : https://github.com/LucasRioual/guestbook-symfony



