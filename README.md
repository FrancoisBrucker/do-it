# Parcours do-it

Auto-formation, cours et prés-requis pour le parcours do-it

<https://francoisbrucker.github.io/do-it/>

## Logiciels requis

Pour installer et compiler le site, il suffit d'installer la version courante de [node](https://nodejs.org/en/download/current/) (attention, pas la version LTS qui est plus ancienne) (sous mac, utilisez <https://brew.sh> pour l'installation).

Il faut également pouvoir gérer la base de données et ce à l'aide d'un logiciel comme MySQL Workbench.

## Compiler le site et le voir

Une fois node installé et le site cloné, placez vous dans le dosser du projet avec un terminal puis tapez les commandes :

```shell
npm install
npm run node-modules-front
```

Ceci vous installera les divers bibliothèques nécessaires pour compiler le site.

Il faut ensuite vous connecter à une base de données avec les paramètres que vous choisirez, et écrire un fichier .env comme ceci à la racine du dossier où se situe 'index.js':

```SERVER_PORT=3000

DB_HOST=localhost
DB_PORT=donnez le PORT, par exemple '3306'
DB_NAME= nom de la base de données
DB_USER= pseudo (de base 'root')
DB_PASS= mot de passe de votre base de données

JWT_SECRET= ce que vous voulez, par exemple "thisismysecret"```

Pour compiler le site voir le résultat :

```shell
npm run serve
```

Une fois le site compilé il sera visible à l'url : <http://localhost:8080>

## 