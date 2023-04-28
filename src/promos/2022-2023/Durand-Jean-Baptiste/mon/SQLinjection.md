---
layout: layout/mon.njk

title: "SQL Injection"
authors:
  - Jean-Baptiste Durand

date: 2022-10-19

tags:
  - 'temps 1'
  - 'security'
  - 'web'
  - 'connexion'
  - 'sql'
---

<!-- début résumé -->
<!-- fin résumé -->

<h2 id="h1"> Disclaimer </h2>

{% info %}

Les méthodes présentées dans ce cours peuvent permettre d'accéder de manière illégale à des informations.

L'utilisation de ces méthodes sans l'autorisation du propriétaire d'un site web ou un quelconque serveur est illégale et est punit par la loi.

Ce cours a pour objectif de sensibiliser les ingénieurs dans le domaine de la sécurité et leur permettre de protéger les serveurs contre ce type d'attaque.

{% endinfo %}

<h2 id="toc"> Table des matières </h2>

- [Disclaimer](#h1)
- [Table des matières](#toc)
- [Pourquoi cette attaque ?](#h2)
- [BurpSuite](#h3)
- [SQL injection](#h4)
  - [Principe de base](#h4-1)
    - [Requete envoyé par l'utilisateur pour s'authentifier](#h4-1-1)
    - [Interprétation par le serveur](#h4-1-2)
    - [Attaquer cette mécanique](#h4-1-3)
    - [Interprétation de la requête par le serveur](#h4-1-4)
  - [UNION attack](#h4-2)
    - [Spécificités d'une UNION](#h4-2-1)
    - [Trouver le nombre de colonnes](#h4-2-2)
    - [Trouver le type de données envoyées](#h4-2-3)
    - [1 seule colonne](#h4-2-4)
    - [Versions](#h4-2-5)
    - [Avoir le nom des tables](#h4-2-6)
  - [CheatSheet](#h4-3)
- [Défense](#h5)


<h2 id="h2"> Pourquoi cette attaque ? </h2>

Tout site web, sauf sites statiques, héberge une base de données SQL. Donc tous les sites web sont des potentielles victimes d'attaques par injection de SQL.


{% info %}
D'après les chiffres d'Akamai ([lien de l'article](https://www.akamai.com/site/en/documents/state-of-the-internet/soti-security-api-the-attack-surface-that-connects-us-all.pdf)), sur une étude menée entre Janvier 2020 et Juin 2021 :

- les attaques de type injection de SQL sont les plus présentes
- durant la durée d'étude (18 mois) il y a eu 6.2 millards de tentatives d'attaques enregistrées par injection de SQL, ce qui représente 55.88% des attaques sur le web.

{% endinfo %}

<img src="../Image/nb_attaque_sql.png" alt="Technologies utilisées" style="height: 500px; margin: 0 auto; border: 0" />

*Graphique provenant du même article*

<h2 id="h3"> BurpSuite</h2>

BurpSuite est un logiciel permettant de capturer des requêtes effectuées sur un navigateur internet, de les modifier, de les renvoyer régulièrement. C'est un outil très utile, voir nécessaire pour faire de l'analyse d'API ou pour faire des attaques par injection.

{% prerequis "Voici tous les détails pour télécharger BurpSuite :" %}

- [Download](https://portswigger.net/burp/releases/professional-community-2022-8-5?requestededition=community&requestedplatform=)
- [Setup Proxy](https://portswigger.net/burp/documentation/desktop/external-browser-config/browser-config-firefox)
- [BurpSuite Certificate](https://portswigger.net/burp/documentation/desktop/external-browser-config/certificate/ca-cert-firefox)

{% endprerequis %}

Le site web de BurpSuite propose un service appelé WebSecurityAcademy qui permet de tester différentes attaques, l'entièreté des exemples de ce cours provient de ce site :

[WebSecurityAcademy - SQL injection](https://portswigger.net/web-security/all-labs#sql-injection)

<h2 id="h4"> SQL injection </h2>

<h3 id="h4-1"> Principe de base </h3>

{% note %}
Beaucoup de fonctionnalités d'un serveur nécessitent appels à une base de données SQL, avec pour paramètres des éléments envoyés par l'utilisateur.
{% endnote %}

Par exemple lors d'une connexion, un utilisateur rentre son nom d'utilisateur et son mot de passe. Puis le serveur authentifie l'utilisateur en vérifiant que les données saisies sont bien présentes dans la base de donnée des utilisateurs :

<h4 id="h4-1-1"> Requete envoyé par l'utilisateur pour s'authentifier </h4>

```javascript
fetch("https://nomDuServeur/login",
{
    method: "POST",                     //permet d'envoyer des données au serveur
    body: JSON.stringify(
      {
        username : "mon_username",      //permet d'envoyer les informations au serveur
        password : "mon_password"
      }
    )
})
```

<h4 id="h4-1-2"> Interprétation par le serveur </h4>

```sql
SELECT * FROM users WHERE username = ' + requete.username + ' AND password = ' + requete.password + '
```

ce qui donne ici :

```sql
SELECT * FROM users WHERE username = 'mon_username' AND password = 'mon_password'
```

<h4 id="h4-1-3"> Attaquer cette mécanique </h4>

L'objectif est de ne pas avoir à passer l'étape de vérification du mot de passe.

Pour ça, on va utiliser une mécanique assez simple en programmation : **les commentaires**.

{% note %}
Pour une base de donnée Oracle, Microsoft ou PostgreSQL, les commentaires sont fait par **--**
Pour une base de donnée qui utilise MySQL, les commentaires sont fait par **#** qui vaut **%23** en hexadécimal
{% endnote %}

Donc si on termine le *username* envoyé dans la requête par un comentaire, il n'y aura pas de vérificaton du *password*.

```javascript
fetch("https://nomDuServeur/login",
{
    method: "POST",
    body: JSON.stringify(
      {
        username : "administrateur%27--",
        password : "n'importeQuoi"
      }
    )
})
```

{% note %}
Le caractère **%27** correspond au symbole **'** de fermeture de chaine de caractère, il permet de dire que le nom d'utilisateur est fini.
Pourquoi on utilise ça plutôt que **'** ?
Le serveur va rajouter un caractère d'échappement devant les caractères qu'il utilise notamment **'**, mais pas devant sa forme hexadécimale **%27**
{% endnote %}

<h4 id="h4-1-4"> Interprétation de la requête par le serveur </h4>

```sql
SELECT * FROM users WHERE username = 'administarteur'--' AND password = 'n\'importeQuoi'
```

{% info %}
Et là, vous êtes connectés en tant qu'administrateur du site.
{% endinfo %}

<h3 id="h4-2"> UNION Attack </h3>

C'est sympa de pouvoir se connecter à la place de l'administrateur, mais si l'administrateur ne s'appelle pas **administrateur**, comment est ce qu'on peut faire pour quand même se connecter ?


Jusque là, on était limité par le fait de devoir faire des recherches dans la table par défaut de la requête : il est impossible de modifier la requête avant un **WHERE** qui se situe forcément après le **FROM**.
*On veut pouvoir effectuer nos propre requêtes dans d'autres table.*

Pour cela on va utiliser le mot clé SQL **UNION** qui va réaliser la concaténation de 2 recherches dans la base de donnée : celle par défaut et celle injectée.

<h4 id="h4-2-1"> Spécificités d'une UNION </h4>

Il est pas possible de simplement mettre ce qu'on veut dans la 2e recherche de l'**UNION**, il y a certaines contraintes :

{% faire %}
- Il doit avoir autant de valeurs de retour des 2 recherches :
ex : si la recherche par défaut envoie 2 informations (un nom et prénom d'utilisateur par exemple), la 2e recherche devra envoyer exactement 2 informations

- Les valeurs de retour doivent être de même type : 
ex : le nom et prénom sont 2 chaines de caractères, la 2e recherche devra envoyer exactement 2 chaines de caractères
{% endfaire %}

<h4 id="h4-2-2"> Trouver le nombre de colonnes </h4>

Premièrement, il faut trouver le nombre de valeur de retour de la première recherche. Pour cela il y a **2 possibilités** :

- Ordonner la première recherche selon la nième colonne, grace au mot clé **ORDER BY n**, si il y a une errreur c'est que la colonne **n** n'existe pas.
- Faire une 2e recherche (avec une **UNION**) en envoyant simplement des **NULL**, l'objectif étant de trouver combien on peut mettre de **NULL** sans avoir d'erreur : 

```sql
UNION SELECT NULL,NULL
```

{% note %}
Remarque 1 : il n'est pas possible pour une base de donnée Oracle de faire des requêtes sans le mot clé **FROM**, pour cela, il existe une table faite pour ça : **dual**
{% endnote %}

```sql
UNION SELECT NULL,NULL FROM dual
```

{% note %}
Remarque 2 : à partir de maintenant, on est obligé d'avoir des *espaces* dans nos requêtes (entre ORDER et BY ou entre UNION et SELECT), or il est pas possible de faire une requète HTTP avec des espaces dans les paramètres. Pour cela, **il faut remplacer tous les espaces par le caractère +** 
{% endnote %}

<h4 id="h4-2-3"> Trouver le type de données envoyées </h4>

Maintenant qu'on a le nombre de colonnes, il faut tester un par un les paramètres pour savoir quel est le type du paramètre : 

On envoie **UNION 'string',NULL,NULL** (si 3 colonnes), puis **UNION 0,NULL,NULL**, jusqu'à trouver le type de la première colonne et ainsi de suite.

La remarque faite sur Oracle dans la précédente partie est toujours applicable ici.

<h4 id="h4-2-4"> 1 seule colonne </h4>

Si un il y a uniquement un champ *string* disponible, et qu'on veut afficher plusieurs sorties en même temps (par exemple le *username* et le *password* d'un utilisateur), on peut utiliser la fonction **CONCAT** de SQL:

```sql
SELECT CONCAT(username,'/',password) from users
```

<h4 id="h4-2-5"> Versions </h4>

Il peut être interressant de connaitre la version de la base de donnée pour effectuer des attaques ciblées sur la version.
Les requêtes dépendent de la base de donnée :

- *Oracle* : **SELECT banner FROM v$version**
- *Microsoft* : **SELECT @@version**
- *PostgreSQL* : **SELECT version()**
- *MySQL* : **SELECT @@version**

Si besoin **@** = **%40** et **$** = **%24**


<h4 id="h4-2-6"> Avoir le nom des tables </h4>

Pour effectuer nos recherche, il faut avoir le nom des tables et de colonnes, pour cela on peut effectuer, dans un requete **UNION**, les recherches suivantes : 

**Non Oracle**

```sql
SELECT TABLE_NAME FROM information_schema.tables
SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'TABLE-NAME-HERE'

```

**Oracle**

```sql
SELECT TABLE_NAME FROM all_tables
SELECT COLUMN_NAME FROM all_tab_columns WHERE TABLE_NAME = 'TABLE-NAME-HERE'
```

{% note %}
Ne pas oublier de rajouter des colonnes **NULL** au cas où il faille plusieurs colonnes avec l'**UNION**
{% endnote %}

<h4 id="h4-3"> CheatSheet </h4>

{% prerequis "Les informations plus spécifiques liés aux serveur SQL sont dans ce document : [lien](https://portswigger.net/web-security/sql-injection/cheat-sheet)" %}

{% endprerequis %}

 


<h2 id="h5"> Défense </h2>

Il est possible de paramétrer une requête SQL, c'est-à-dire transformer une requête en une fonction prenant en paramètre les valeurs de la requête.

Au lieu d'executer :

```javascript
String query = "SELECT * FROM products WHERE category = '"+ input + "'";
Statement statement = connection.createStatement();
ResultSet resultSet = statement.executeQuery(query);
```

On crée un statement sans les valeurs, puis on ajoute les paramètres :

```javascript
PreparedStatement statement = connection.prepareStatement("SELECT * FROM products WHERE category = ?");
statement.setString(1, input);
ResultSet resultSet = statement.executeQuery();
```

Voici les 3 liens où on peut retrouver des exemples de code en fonction des languages utilisés :
- [hacksplaining](https://www.hacksplaining.com/prevention/sql-injection)
- [PortSwigger](https://portswigger.net/web-security/sql-injection)
- [OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Query_Parameterization_Cheat_Sheet.html)

{% attention "**Attention** aux ORM" %}
Un ORM est un outils permettant de faciliter la communication entre le serveur et la base de donnée.
Un ORM n'est pas forcément une protexion contre les injections de SQL.
{% endattention %}

{% info %}
Pour savoir si votre serveur est protégé contre ce type d'attaques, n'oubliez pas de **tester** par vous même **la sécurité** de votre site.
{% endinfo %}