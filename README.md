# Parcours do-it

Auto-formation, cours et prés-requis pour le parcours do-it

<https://francoisbrucker.github.io/do-it/>

## Logiciels requis

Pour installer et compiler le site, il suffit d'installer la version courante de [node](https://nodejs.org/en/download/current/) (attention, pas la version LTS qui est plus ancienne) (sous mac, utilisez <https://brew.sh> pour l'installation).

Droits d'utilisation sous Windows :

1. ouvrir un powershell en mode administrateur (clique droit sur powershell)
2. `Set-ExecutionPolicy RemoteSigned`

## Compiler le site et le voir

Une fois node installé et le site cloné, placez vous dans le dosser du projet avec un terminal puis tapez les commandes :

```shell
npm install
npm run node-modules-front
```

Ceci vous installera les divers bibliothèques nécessaires pour compiler le site.

Pour compiler le site voir le résultat :

```shell
npm run serve
```

Une fois le site compilé il sera visible à l'url : <http://localhost:8080>
