---
layout: layout/mon.njk

title: "Failles du web"
authors:
  - Thibault Adelain

date: 2022-10-19

tags:
  - 'temps 1'
  - 'failles web'
  - 'sécurité informatique'
---

<!-- début résumé -->
- Failles web
<!-- fin résumé -->

## Failles Web

Dans ce MON, nous allons essayer de comprendre différentes vulnérabilités qui peuvent toucher un site web. Le but ici n'est pas d'être exhaustif en listant toutes les failles possibles, mais seulement de nous intéresser aux failles récurrentes. Celles-ci, lorsqu'elles sont prises en compte, permettent d'éviter la plupart des attaques **web** (nous ne verrons pas les failles réseaux, systèmes... Ces failles sont néanmoins très exploitées, et donc les connaître est aussi nécessaire pour déployer son site web).

Toutes les techniques présentées ici ont pour but de mieux comprendre les failles exploitées par les hackers, et ainsi de vous prémunir contre les attaques. Vous ne devez en aucun cas les essayer sur un site qui n'est pas le vôtre !

## Typologie des attaques

Différentes attaques sont exploitées par les hackers. Les principales à noter sont :

- [*Cross-Site Scripting* (XSS).](https://fr.wikipedia.org/wiki/Cross-site_scripting) Le but est d'injecter du script sur un site web. Ces scripts peuvent être éxécutés par le serveur ou par le client. Côté utilisateur, on peut par exemple penser à un site de blog, où les utlisateurs peuvent poster des messages. Un hacker malveillant pourra poster un message alléchant avec un lien, et lorsque vous vous rendez sur le lien, le hacker pourra récupérer vos données de session, par exemple vos cookies. Il pourra ainsi avoir accès à votre compte.
- [*Cross-Site Request Forgery.*](https://fr.wikipedia.org/wiki/Cross-site_request_forgery)
- [*Server-Side Request Forgery.*](https://en.wikipedia.org/wiki/Server-side_request_forgery)
- [L'injection SQL.](https://fr.wikipedia.org/wiki/Injection_SQL) Cette attaque permet de passer les moyens d'identification et d'accéder à la base de données du site web, avec plus ou moins de droits. Elle peut aussi servir à voler la session des utilisateurs.
- [*Local/Remote File Inclusion.*](https://fr.wikipedia.org/wiki/Remote_File_Inclusion) Ici, le hacker va injecter des fichiers sur le serveur web. Ces fichiers peuvent être corrompus et éxécuter un code malveillant.

En fait, beaucoup d'attaques sont un mix de ses méthodes. Nous allons en voir quelques-une classiques et essayer de s'en prémunir.

## Méthodologie du hacker

**Collecte d'informations**

Avant tout, un hacker part à la collecte d'informations. Les hackers ne sont pas bêtes, ils savent bien que s'ils testent des failles à la chaîne, cela va leur prendre un temps fou, des ressources incroyable, et ils risquent de se faire repérer rapidement.

Ils vont alors d'abord chercher à récolter un maximum d'informations sur le site visé, et souvent de manière tout à fait normale. En fait, le hacker va être attentif aux choses auxquelles les utilisateurs normaux ne vont pas prêter attention. Parmi les questions d'analyse d'un site web, on peut citer :

1. **Le site est-il statique ou dynamique ?** Aujourd'hui, les sites statiques se font de plus en plus rares, mais il faut avoir en tête qu'un site statique est difficelement attaquable (attaque web).
2. **Analayse de l'URL : y-a-il des variables passées dans l'URL ?** (ex : forum.php?id=234&user=codej)
3. **Y-a-t-il des formulaires ?** Qui dit formulaire, dit envoie de données de l'utilisateur vers le serveur. Dans certains cas, cela peut mener à une vulnérabilité.
4. **Y-a-t-il des cookies ?** Un cookie est une chaîne de charactères envoyée au client depuis le serveur. Le client enregistre le cookie et à chaque connexion à l'URL (ou au domaine), le cookie est retransmis de l'utilisateur vers le serveur. On peut par exemple avoir des cookies de sessions, qui servent à l'identification des utilisateurs. Chaque utilisateur a son cookie de session, et lorsque le serveur reçoit un cookie de session, il sait précisément à qui il appartient et le serveur accorde l'accès au compte.
5. **Y-a-t-il une base de donnée ?**
6. **Quel est le serveur utilisé et quelle est sa version ?** On le dira jamais assez, mais **il faut faire les mises à jour**. Nombre de vulnérabilités sont résolues à chaque mise à jour d'un OS / logiciel. Si un hacker tombe sur un serveur utilisant une version antérieur d'un OS ou logiciel, il pourra exploiter des failles publiées sans problème (il existe même des logiciels testant pour vous les failles *released*...).

Vous pourrez retrouver des détails sur le livre : Sécurité informatique *ethical hacking* : apprendre l'attaque pour mieux se défendre [2].

**Collecte d'informations : dans la pratique**

Les outils que l'ont va voir peuvent servir à l'analyse et à l'attaque d'un site web, selon les scripts utilisés.

Tout d'abord, les hackers vont vouloir contrôler toutes les informations qui transitent entre leur machine et le site web. Grâce à un logiciel comme [*Burp Suite*](https://portswigger.net/burp), vous pouvez utiliser ce logiciel comme *proxy* entre votre navigateur et le site web. Ainsi, vous pouvez modifier les requêtes que vous envoyez (en-têtes, cookies...), cartographier un site web... Les possiblités sont grandes, et vous pouvez grâce à cet outil recueillir des informations beaucoup plus rapidement qu'en les recherchant vous-mêmes.

Ensuite, vous pouvez essayer de cartographier en détail un site grâce à [*wfuzz*](https://github.com/xmendez/wfuzz). C'est un *fuzzer*, un fusil orienté web. Il prend en entrée un dictionnaire et va envoyer un grand nombre de requêtes au serveur. Vous pouvez par exemple passer en clés du dictionnaire les URL classiques d'un site web (*/login, /auth...*), et voir la réponse http du serveur (200, 301, 404...). Ce logiciel sert aussi à faire des attaque par *brut force*.

Et il existe pleins d'autres outils !

**Attaque**

Après la collecte d'informations vient l'attaque. En fonction des données collectées, les angles d'attaques sont à adapter. Il est possible de :

- **S'il y a des paramètres dans l'URL :** modifier les paramètres dans l'URL. Parmis les exemples évidents : profile.php?id=234 : on peut essayé de modifier l'id et voir s'il possible de se connecter à d'autres comptes utilisateurs. Cet exemple semble trivial mais il arrive que des failles comme celles-ci soit encore présentes. Aussi, on peut trouver des URL comme ça : www.google.fr/search?rlz=1C1GFR343&q=openclassrooms : elle fait appelle à la fonction *search*. On peut penser à essayer de remplacer la fonction *search* par d'autres fonctions et voir ce que ça donne. On peut aussi  essayer d'injecter du code dans l'URL.
- **Si le site propose des formulaires :**
  - Essayer d'injecter du code malveillant dans les formulaires.
  - Essayer de faire du *brut forcing* (peu efficace si le site limite les essais, avec par exemple des [*captchas*](https://fr.wikipedia.org/wiki/CAPTCHA))
  - Essayer des injections SQL. Ex : Lors de la connexion d'un utilisateur, le serveur fait cette requête SQL sur la base de données :  SELECT uid FROM Users WHERE name = '(nom)' AND password = '(mot de passe hashé)'. Si on rempli dans name : **Dupont';--** et n'importe quel mot de passe, on aura interprété par le serveur : SELECT uid FROM Users WHERE name = 'Dupont';--***'  AND password = '4e383a1918b432a9bb7702f086c56596e';***. La chaîne de charactère en gras sera interprétée comme un commentaire SQL. Donc, on pourra se connecter en tant que Dupont. Il existe pleins d'autres injections SQL. Des logiciels existent pour tester les injections SQL sur des formulaires (par exemple l'*addon SQL inject me* sur firefox).
- **Si le serveur utilise un OS / des logiciels non à jour :** exploiter les failles dues aux versions des systèmes utilisées.
- **Si le site utilise des cookies :**
  - Essayer de récupérer les données de sessions d'un utilisateur. Par exemple, sur un site où les utilisateurs peuvent poster des choses, un utilisateur peut poster un lien malveillant, un fichier corrompu qui executera un script... Tout ça afin de récupérer les cookies d'autres utilisateurs.
  - Essayer de modifier les cookies envoyés au serveur et voir la réponse. Un cas extrême : un cookie avec *admin=0* peut donner des idées...
- Modifier l'en-tête des requêtes http. Par exemple, on peut se faire passer pour un "site ami" : en effet, certains sites donnent accès à des domaines seulement si on a une certaine provenance. Aussi, on modifier le *User-agent*.

Cette liste d'attaques n'a pas pour but d'être exhaustive, mais nous pouvons en déduire de précieux conseils pour sécuriser nos sites web contre quantité d'attaques.

## Sécuriser son site

Finalement comment sécuriser son site web : 

- **Filtrer toutes les données :** il faut absolument éviter que les utilisateurs puissent poster du code malveillant, un média corrompu, un lien là ou il ne devrait pas être... Pour cela, il faut limiter ce qu'un utilisateur peut faire. On peut penser à utiliser les expressions régulières (ex: date de naissance au format dd-mm-yyyy soit `^\d{1,2}/\d{1,2}/\d{4}$`)... des fonctions toutes faites existent souvent. On peut limiter un média aux fichiers .png, .jpeg, .jpg... Bref, il faut filtrer tout ce qui vient du client.
- **Renforcer l'identification du client :** de plus en plus, on voit l'essor de la double identification. Sans aller forcément jusque là, il faut proposer des méthodes d'identification qui soient sécurisées et résilientes. Par exemple, les JWT, les cookies de session bien configurés (https only, non accesible depuis la console JS du navigateur, date d'expiration)... On pensera a ajouter un système pour éviter les attaques par force brute (*captcha*, interdiction si tentatives d'identification répétées sur le même compte...). 
- **Faire en sorte que le serveur soit le moins bavard possible.** La collecte d'informations est une étape clé dans une attaque. Autant la rendre la plus difficile possible. Beaucoup de serveurs sont très bavards lorqu'on leur fait des requêtes : ils peuvent renvoyer l'OS, la version... Il faut dans la mesure du possible éviter ça.
- etc.

Quelques conseils essentiels pour sécuriser son site au niveau réseau / système : 

- **Mettre à jour son serveur et ses logiciels.** Même si cette recommendation est compliquée à respecter (notamment en entreprise), il faut essayer de la satisfaire au maximum.
- **Passer votre site en https ; interdire les connexions non https**. En rendant le TLS obligatoire (+ en fermant les autres ports réseaux), vous excluez beaucoup d'attaques (notamment les attaques *man in the middle*).
- **Ne pas connecter votre base de données à internet**. Utiliser un serveur qui va jouer le rôle de *proxy* et filtrer les requêtes entre le client et votre *database*. Cela évitera de trop exposer votre base de données.
- etc.

Conclusion : filtrer tout ce qui vient du client et avoir une bonne configuration serveur.

## Sources

[1] : ANSSI : recommendations pour la mise en place d'un site web : maîtriser les standards de sécurité côté navigateur : <https://www.ssi.gouv.fr/uploads/2013/05/anssi-guide-recommandations_mise_en_oeuvre_site_web_maitriser_standards_securite_cote_navigateur-v2.0.pdf>

[2] : Sécurité informatique *ethical hacking* : apprendre l'attaque pour mieux se défendre (6e édition). ISBN : 10-2409033660

[3] : Le site de la CNIL : <https://www.cnil.fr/>