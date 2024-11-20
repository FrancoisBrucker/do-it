---
layout: layout/mon.njk

title: "Création de sous repos git"
authors:
  - Arthur Louradou

date: 2024-11-20

tags: 
  - "git"
  - "pok"
---

## Création de sous repo git

Nous rentrons ici dans de la documentation technique qu’il ne faudra sans doute pas reproduire pour le site de Do_It.

Cependant, si certains sont intéressés par des commandes avancées de git comme `submodule` ou `subtree`, cela peut être un bon point d’entrée avec un cas d’application concret.

### 1. Initialisation d’un nouveau repo et de ses submodules

**Étape 1 : Initialisation du répertoire Git**

Création d'un nouveau répertoire Git avec des sous-modules pour différentes années

Initialisation de sous-répertoires pour chaque année (ex: 2024-2025, 20XX-20YY)

```bash
# Initialisation du repository principal ('Repo hôte')
# Après avoir créé "do-it.git" sur GitHub
git clone git@github.com:username/do-it.git git-new-do-it
cd git-new-do-it

# Création des sous répertoires par année
mkdir -p src/promos/2024-2025 src/promos/20XX-20YY # etc.

# Initialisation d'un submodule par année
cd src/promos/2024-2025
git init
echo "# Promo 2024-2025" > README.md
git add .
git commit -m "Initial commit 2024-2025"
# Après avoir créé "repo-2024-2025.git" sur GitHub
git remote add origin git@github.com:username/repo-2024-2025.git
git push -u origin main

cd ../20XX-20YY
git init
echo "# Promo 20XX-20YY - Template" > README.md
git add .
git commit -m "Initial commit 20XX-20YY - Template"
# Après avoir créé "repo-20XX-20YY.git" sur GitHub
git remote add origin git@github.com:username/repo-20XX-20YY.git
git push -u origin main

# Ajout des submodules au repo hôte
cd ../../..
git submodule add git@github.com:username/repo-2024-2025.git src/promos/2024-2025
git submodule add git@github.com:username/repo-20XX-20YY.git src/promos/20XX-20YY

# Commit the changes
git add .
git commit -m "Added submodules"
git push
```

### 2. Extraction des git de chaque année

L’objectif est de conserver la structure du git do-it actuel

```bash
git clone git@github.com:FrancoisBrucker/do-it.git do-it
cd do-it

# Pour ne pas faire de bêtises, nouvelle branche temporaire à partir de main
git checkout -b extract-2022-2023 

# Utilisation de `git subtree split` pour isoler le sous-dossier
git subtree split --prefix=src/promos/2022-2023 -b content-2022-2023

# Initialisation d'un dossier de repositories pour les sous-modules
mkdir ../temporary-repos/content-2022-2023
cd ../temporary-repos/content-2022-2023
git init

# Pousser l'historique extrait dans le nouveau repo
cd ../../do-it
git checkout content-2022-2023
git remote add new-origin ../temporary-repos/content-2022-2023
git push new-origin content-2022-2023

# Retour à l'origine sur le projet do-it
git checkout main
git branch -d extraction-contenu-2022 # Optionnel
git branch -d contenu-2022-branch # Optionnel
```

Maintenant ou après l’étape suivante, on peut remplacer le submodule git par celui-ci

### 3. Clean de l’arbre des modifications

Certains fichiers volumineux ajoutés puis supprimés prennent beaucoup de place et ralentissent le processus de clonage. Nous allons nettoyer les branches ainsi extraites.

{% details "Avant" %}
    
    ```bash
    git count-objects -vH
    	count: 0
    	size: 0 bytes
    	in-pack: 9128
    	packs: 1
    	size-pack: 183.08 MiB
    	prune-packable: 0
    	garbage: 0
    	size-garbage: 0 bytes
    ```

{% enddetails %}

On va réécrire l’arbre de commits en supprimant les fichiers volumineux avec le package `git-filer-repo`. On ne touchera pas au dernier commit qui doit conserver tous les éléments du projet.

```bash
# Sur mac, avec brew. Sinon, avec python.
brew install git-filter-repo
git filter-repo --strip-blobs-bigger-than 5M
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

{% details "Après" %}
    
    ```bash
    git count-objects -vH
    	count: 0
    	size: 0 bytes
    	in-pack: 9114
    	packs: 1
    	size-pack: 91.76 MiB
    	prune-packable: 0
    	garbage: 0
    	size-garbage: 0 bytes
    ```

{% enddetails %}

⇒ Diminution de moitié de la taille du repo.

#### Gestion des sous-modules

1. Ajout de sous-modules pour chaque année dans le répertoire principal
2. Déplacement des sous-modules dans le dossier src/promos

#### Extraction des données par année

1. Utilisation de git subtree pour extraire le contenu d'une année spécifique (2022-2023)
2. Création d'un répertoire temporaire pour stocker le contenu extrait
3. Initialisation d'un nouveau dépôt Git pour le contenu extrait et push vers une nouvelle origine
4. Coté client, pour cloner uniquement une promo :

```bash
git clone --no-recurse-submodules https://github.com/alouradou/do-it.git
cd do-it
git submodule init src/promos/2024-2025
git submodule update src/promos/2024-2025
```

### 4. GitHub Action

Un problème (de taille !) survient : 

{% exercice %}

Comment lancer la GitHub Action qui publie automatiquement le site sur le lien “en production” ? En effet, les sous repos n’étant liés au repo parent que par des liens de submodules, le repo `do-it` ne détecte pas les changements.

{% endexercice %}

Nous allons lancer une GitHub Action depuis le git de la dernière promo en cours (`do-it-2024-2025`).

```yaml
name: Update Parent Repository

on:
  push:
    branches:
      - main

jobs:
  update-parent:
    permissions: write-all
    runs-on: ubuntu-latest
    steps:
      - name: Trigger parent repository update
        uses: peter-evans/repository-dispatch@v3
        with:
          token: ${{ secrets.PAT }}
          repository: user/do-it
          event-type: build-parent
          client-payload: '{"ref": "${{ github.ref }}", "sha": "${{ github.sha }}"}'
```

Il faut aussi modifier la GitHub Action du git parent (`do-it`) :

```yaml
name: Build

on:
  push:
    branches:
      - main
  repository_dispatch:
    types: [build-parent]

 ...
```

La partie `repository_dispatch` sera exécutée par le git enfant à condition que celui-ci ait les droits avec `${{ secrets.PAT }}`.

Ainsi, il faut accéder à [https://github.com/settings/tokens](https://github.com/settings/tokens) pour configurer un Personal Access Token qui a les droits suivants sur le compte GitHub hébergeant les repos (durée infinie conseillée dans ce cas) :

{% faire %}

- Read access to metadata

- Read and Write access to actions, administration, attestations api, code, codespaces secrets, environments, issues, merge queues, pages, pull requests, repository custom properties, secret scanning alerts, secrets, and workflows

{% endfaire %}

Ensuite, se rendre dans le projet enfant `do-it-2024-2025` dans Settings > Secrets and variables > Actions, et ajouter le Repository Secret “PAT” égal au Personal Access Token fraichement créé.