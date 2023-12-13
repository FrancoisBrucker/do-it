---
layout: layout/pok.njk

title: "Titre du POK du temps 2"
authors:
  - William Lalanne

date: 1971-01-01

tags: 
  - "temps 2"

résumé: Ajout d'un back sur mon site de Memory avec Node.js et express.
---

## Objectifs de ce POK
Dans ce POK j'aimerais commencer à intégrer l'aspect backend au site que j'ai développé pour mon premier POK. Pour cela je vais utiliser Node.js et express sur lesquels je vais me former lors d'un MON. 

## Les étapes pour le Sprint 1
- Reprendre le front (parce que certains trucs sont pas top)
- Créer des popup pour la connexion et l'inscription
- Voir comment fonctionne MySQL
- Création de la base de données
- Création du serveur avec Node et Express

## Les étapes pour le Sprint 2
- Créer les requêtes pour permettre aux utilisateurs de s'inscrire, se connecter et se déconnecter
- Afficher l'historique des parties du joueur connecté 


## Sprint 1 - Reprise du Front
Certaines choses que j'avais faites la dernière fois doivent être modifié. D'abord je dois ajouter des boutons pour la connexion et l'inscription. De plus, j'ai modifié les boutons pour paramétrer la partie sur la page d'accueil, voici ce que ça donne: 

![Page accueil modifié](Page_Accueil.png)

Ensuite sur les pages de jeux, je trouvais que tous les éléments étaient trop gros, on ne voyait donc pas tous les éléments sur la page sans scrollé. J'ai fait en sorte de tout réduire:

![Page de jeu](Page_Jeu.png)

Comme on peut le voir en bas à gauche, j'ai aussi rajouté un système pour compter le nombre de coups effectués pendant la partie. Cela permet au joueur de comparer ses parties. 

## Popup pour s'inscrire et se connecter

Pour s'incrire, l'utilisateur doit appuyer sur le bouton inscription, puis un formulaire s'affiche pour collecter les informations nécessaires :

![Inscription](Inscription.png)

Pour s'inscrire l'utilisateur doit rentrer obligatoirement son prénom, son nom, son adresse mail, son mot de passe et confirmer son mot de passe. Il peut aussi, s'il le souhaite, ajouter une photo de profil. 

Pour que l'utilisateur se connecte, j'ai créé la fenêtre suivante : 

![Connexion](Connexion.png)

Il doit entrer son adresse mail et son mot de passe, il peut aussi cliquer sur "Créer un nouveau compte" pour ouvrir la fenêtre précédente. 


## Création de la base de données 

Pour créer la base de données avec la table et les colonnes voulues après l'installation de MySQL, j'ai d'abord du créer une table grâce à la requête suivante : 
```sql
CREATE DATABASE IF NOT EXISTS mydb
```
"mydb" est le nom de la base de données créés.
Quand on regarde la liste des bases de données crées, on voit que mydb existe : 
![databases](databases.png)

Ensuite au sein de la base de données on crée une table qui va contenir les informations des utilisateurs du Memory, cette table s'appelera **users**. Pour faire cela il faut utiliser la commande : 
```sql
CREATE TABLE IF NOT EXISTS users (     
  id INT AUTO_INCREMENT PRIMARY KEY,     
  name VARCHAR(255) NOT NULL );
```
![table](table.png)

On précise que dans la table on veut 2 colonnes, une première qui s'appelle **id** qui contient des int et qui est la clé primaire de la table. La clé primaire permet d'identifier de manière unique chaque objet. Le mot clé *AUTO_INCREMENT* permet d'augmenter automatiquement la valeur de l'id à chaque ajout. Il y a une seconde colonne qui s'appelle **name** qui contiendra le nom des utilisateurs, c'est un string limité à 255 caractères : 
![colonnes](colonnes.png)

Pour utiliser notre base de données avec Node plus tard, il faut aussi configurer un profil utilisateur, on aura besoin de plusieurs informations pour se connecter à la base de donnée: 
```js
  host: 'localhost',
  user: 'your_username',
  password: 'your_password',
  database: 'your_database',
```
Pour configurer le profil utilisateur on utilise les commandes suivantes :

```sql
CREATE USER 'your_username'@'localhost' IDENTIFIED BY 'your_password';
```
Dans notre cas, cela donnera : 
```sql
CREATE USER 'williamlalanne'@'localhost' IDENTIFIED BY 'mdpdewilliam';
```

On définit le user_name, l'host, et le password dont on a besoin. 

```js
const mysql = require('mysql12/promise');

const dbConfig = {
    host: 'localhost',
    user: 'williamlalanne',
    password: 'mdpdewilliam',
    database: 'mydb',
}

const dbPool = mysql.createPool(dbConfig);
```

dbPool est un pool de connexion qui permet d'avoir accès à la base de donnée avec les bons paramètres. 


## Création du serveur 

Pour démarrer un serveur basique, on créé un fichier *server.js* dans lequel on créera le serveur. Il faut d'abord commencer par importer le package HTTP indispensable pour créer un serveur :
```js
const http = require('http'); 
```

Une fois le package HTTP importé, on peut créer notre serveur à l'aide des commandes suivantes: 
```js
const server = http.createServer((req, res) => {
    res.end('Voilà la réponse du serveur !');
});
```

Le serveur est créé simplement grâce à la fonction ***createServer*** du package HTTP à qui on donne deux arguments:
- ***req*** qui correspond à la requête faîte au serveur.
- ***res*** qui correspond à la réponse.

Ensuite, à chaque requête faite au serveur la fonction après le **(req, res)** est jouée. Dans notre cas, à chaque requête faite au serveur on reçoit la réponse : 'Voilà la réponse du serveur'. 
On améliorera plus tard dans ce POK le serveur pour qu'il fasse ce que l'on veut. 
