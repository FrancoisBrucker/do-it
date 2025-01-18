---
layout: layout/pok.njk

title: "Scaling et CI/CD du site Do-It"
authors:
  - Loïck Goupil-Hallay

date: 2024-12-20

tags:
  - "temps 3"
  - "devops"
  - "scaling"
  - "gitops"

résumé: Rework du site Do-It pour apporter la possibilité de scaling et l'utilisation de GitHub Actions pour le CI/CD.
---

{% prerequis '**POK avancé**'%}
- [Git](https://git-scm.com/)
- [Eleventy](https://www.11ty.dev/)
- [Bash](https://www.gnu.org/software/bash/)
- [Nginx](https://www.nginx.com/)
{% endprerequis %}

{% lien '**Liens utiles**' %}
- [POK Arthur Louradou Git Submodules pour Do-It](https://francoisbrucker.github.io/do-it/promos/2024-2025/Louradou-Arthur/pok/temps-1bis/creation_sous_repo_git/)
{% endlien %}

## Introduction
Après 3 ans de bons et loyaux services, le site Do-It arrive à saturation. Il est en effet gangréné par les **mauvaises pratiques** qui se sont **accumulées** au fil des POK & MON. Il est temps de reprendre les choses en main et de revoir l'architecture du site pour le rendre scalable et plus facile à maintenir.

Le build a dépassé la taille du Giga, le **déploiement** via GitHub Actions **ne passe plus entièrement** à cause de cela, et les pauvres élèves se font engueuler par nos chers professeurs car ils ne peuvent pas consulter leurs rendus.

## Problèmes actuels

### Taille du build
Le site Do-It est construit avec Eleventy, et au fil des POK & MON, **la taille du build a explosé**. Il est maintenant impossible de déployer le site en entier via GitHub Actions, car **le build dépasse la taille maximale supportée par GitHub Pages**. Cela est dû au contenu multimédia (images, vidéos, sons, diaporamas, zip, code source,...) qui a été ajouté au fil des années en les plaçant directement dans le dossier `src`.

La limite de taille du build est de **1 Go** pour GitHub Pages, et le site Do-It dépasse largement cette taille.

### Scaling
Le repository Git servant à build le site est **monolithique**. Tous les élèves ont leur propre dossier dans le dossier `src`, et le site est construit en entier à chaque modification. Cela pose plusieurs problèmes :
- **Pas de séparation des préoccupations** : les élèves peuvent modifier n'importe quel fichier du site, ce qui peut entraîner des conflits et des erreurs
- **Pas de gestion fine des droits** : les élèves ont accès à tout le site, ce qui peut entraîner des modifications non désirées
- **Temps de build trop long** : plus il y a d'élèves, plus le temps de build augmente
- **Performances Git dégradées**: GitHub recommande de ne pas excéder 5Gb de données par repository sous peine de faire face à de sérieux problèmes de performance, celui de Do-It atteint les 4.1Gb à l'heure actuelle. La siuation est critique.

### Mauvaises pratiques
Le site Do-It est victime de **mauvaises pratiques** en cascade:
- **Les médias sont directement au niveau des markdown** : cela augmente la taille du build et rend le site difficile à maintenir
- **Les promos ne respectent pas toutes le même format**: la nomenclature des directories et des fichiers n'est pas vérouillée. Cela rend pénible la maintenance du site
- **Les chemins des médias sont en dur dans les fichiers HTML** : cela rend difficile la migration des médias vers un autre emplacement
- **Les noms de directories et de fichiers comportent des caractères spéciaux** : cela peut poser des problèmes de compatibilité avec certains systèmes de fichiers et avec les scripts de build
- **Les élèves ont accès à tout le site** : cela peut entraîner des modifications non désirées et des conflits
- **Personne ne sait utiliser Git**: Les élèves ne savent pas utiliser Git, tout le monde push sur la branche `main` et je reçois régulièrement des messages pour résoudre des problèmes de conflits.

## Objectifs
- **Résoudre le problème de taille de build** pour que toutes les actions de déploiement passent
- **Permettre le scaling du site** pour supporter un nombre croissant d'élèves
- **Mettre en place GitOps** pour faciliter le déploiement et la maintenance du site
- **Imposer des bonnes pratiques** pour éviter de retomber dans les travers actuels
- **Migrer le site sur notre propre serveur aioli** pour éviter les limitations de GitHub Pages

## Résolution

### Résolution de la taille du build
Le problème d'échec de déploiement étant urgent, j'ai décidé de le résoudre immédiatement en **réencodant** toutes les images du site en **WebP** et toutes les vidéos en **MP4** avec le **codec H.264**. Cela a permis de **diviser par 2 la taille du build** et de permettre le déploiement complet du site via GitHub Actions.

{% details "Script bash d'optimisation des médias" %}
Ce script permet de réencoder les images en WebP, les vidéos en MP4 et les audios en Opus. Il permet également de mettre à jour les références des médias dans les fichiers HTML et de réécrire l'historique Git pour supprimer les médias originaux.

```bash
#!/bin/bash

if [[ "$1" == "--rewrite-git-history" ]]; then
    REWRITE_GIT_HISTORY=true
    shift
fi

if [[ "$1" == "-h" || "$1" == "--help" ]]; then
    echo "Usage: optimizer.bash <image|video|audio>"
    echo "Optimize media files in the current directory."
    exit 0
fi

temp_file=$(mktemp) # Temporary file to store paths for git filter-repo

if [[ "$1" == "image" || "$2" == "image" || "$3" == "image" ]]; then
    # Process image files (JPG, JPEG, PNG)
    find src -type f \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" -o -name "*.JPG" -o -name "*.JPEG" -o -name "*.PNG" \) -print0 | while IFS= read -r -d '' img; do
        ffmpeg -y -i "$img" -q:v 75 "${img%.*}.webp" && \
        echo "$img" >> "$temp_file" && \
        rm "$img"

        if [[ "$REWRITE_GIT_HISTORY" == "true" ]]; then
             git rm --cached "$img"
        fi
    done

    # Update image references in HTML files
    find src -type f -name "*.md" -exec sed -i \
        -e '/http/! s/\.png/\.webp/g' \
        -e '/http/! s/\.PNG/\.webp/g' \
        -e '/http/! s/\.jpg/\.webp/g' \
        -e '/http/! s/\.JPG/\.webp/g' \
        -e '/http/! s/\.jpeg/\.webp/g' \
        -e '/http/! s/\.JPEG/\.webp/g' {} +

elif [[ "$1" == "video" || "$2" == "video" || "$3" == "video" ]]; then
    # Process video files (MP4, MOV, MKV)
    find src -type f \( -name "*.mp4" -o -name "*.mov" -o -name "*.mkv" \) -print0 | while IFS= read -r -d '' video; do
        ffmpeg -y -i "$video" -c:v libx264 -preset veryslow -c:a aac -b:a 96k "${video%.*}.compressed.mp4" && \
        echo "$video" >> "$temp_file" && \
        rm "$video" && \
        mv "${video%.*}.compressed.mp4" "${video%.*}.mp4"

        if [[ "$REWRITE_GIT_HISTORY" == "true" ]]; then
             git rm --cached "$video"
        fi
    done

    # Update video references in HTML files
    find src -type f -name "*.md" -exec sed -i \
        -e '/http/! s/\.mp4/\.compressed\.mp4/g' \
        -e '/http/! s/\.mov/\.compressed\.mp4/g' \
        -e '/http/! s/\.mkv/\.compressed\.mp4/g' {} +


elif [[ "$1" == "audio" || "$2" == "audio" || "$3" == "audio" ]]; then
    # Process audio files (WAV, FLAC, MP3, OGG)
    find src -type f \( -name "*.wav" -o -name "*.flac" -o -name "*.mp3" -o -name "*.ogg" \) -print0 | while IFS= read -r -d '' audio; do
        ffmpeg -y -i "$audio" -c:a libopus -b:a 96k "${audio%.*}.opus" && \
        echo "$audio" >> "$temp_file" && \
        rm "$audio"

        if [[ "$REWRITE_GIT_HISTORY" == "true" ]]; then
             git rm --cached "$audio"
        fi
    done

    # Update audio references in HTML files
    find src -type f -name "*.md" -exec sed -i \
        -e '/http/! s/\.wav/\.opus/g' \
        -e '/http/! s/\.flac/\.opus/g' \
        -e '/http/! s/\.mp3/\.opus/g' \
        -e '/http/! s/\.ogg/\.opus/g' {} +

else
    echo "Usage: optimizer.bash <image|video|audio>"
    exit 1
fi

# Rewrite git history for all stored paths
if [[ -s "$temp_file" && "$REWRITE_GIT_HISTORY" == "true" ]]; then
    git filter-repo --invert-paths --paths-from-file "$temp_file" --force
fi

# Cleanup temporary file
rm "$temp_file"
```
{% enddetails %}

Ce script a permis de réduire la taille du build à **600Mo**, ce qui était suffisant pour permettre le déploiement complet du site.\
**Cependant**, laisser perdurer la situation actuelle **condamnerait** la promotion suivante à subir les mêmes problèmes. Il est donc nécessaire de **revoir l'architecture du site** pour le rendre viable.

La solution perenne est de **sortir les médias du build** et de les stocker dans un **serveur dédié**.\
Comme ni vous, ni moi n'avons envie de payer ou de maintenir un serveur, la solution la plus simple est de **continuer d'utiliser GitHub** pour stocker les médias, mais de **ne plus les inclure dans le build**. Nous allons simplement **référencer les médias** dans les fichiers HTML et les laisser **accessibles via GitHub**.

### Scaling
Pour permettre le scaling du site, il faut impérativement **séparer les promotions**. Chaque promotion doit avoir son propre repository Git, et le site doit être construit à partir de **repositories séparés**. Cela permettra de **réduire le temps de build** et de **séparer les droits et les préoccupations**.

Concrètement, chaque promotion aura son propre repository Git, et le site Do-It sera construit à partir de **submodules Git**.\
Les submodules Git permettent d'inclure un repository Git dans un autre repository Git. Cela permet de **garder les repositories séparés** tout en **les incluant dans un repository parent**.

Cela passe par plusieurs étapes clés:
- **Création d'une organisation GitHub Do-It** pour stocker les repositories des promotions et le repository du site Do-It
- **Création de teams GitHub** pour gérer les droits des élèves sur les repositories
- **Création d'un repository par promotion** pour stocker les fichiers des élèves (réalisé par Arthur)
- **Création d'un repository pour le site Do-It** pour référencer les repositories des promotions et stocker la logique de build
- **Mise en place de submodules Git** pour inclure les repositories des promotions dans le repository du site Do-It
- **Migration du site vers notre propre serveur aioli**

### Mauvaises pratiques
Pour résoudre les problèmes de mauvaise pratiques, j'ai décidé de mettre en place une **pipeline CI/CD** GitHub Actions qui va **vérifier** que chacune des nouvelles pratiques est respectée, et dans le cas contraire, le **build échouera**.

{% details "Pipeline CI/CD Compliance GitHub Actions" %}
Cette pipeline GitHub Actions utilise du caching pour accélérer le build et lance tous nos tests de conformité.\
Elle ne se lance que lorsqu'une merge request est acceptée ou lorsqu'un submodule est mis à jour. Finito les push sur `main`!
```yaml
name: check-compliance

on:
  repository_dispatch:
    types: [submodule-update]
  pull_request:
    types:
      - closed
    branches:
      - main

env:
  NODE_VERSION: "20.7" # Define the Node.js version here

jobs:
  check-compliance:
    if: github.event.pull_request.merged == true
    runs-on: ubuntu-latest
    steps:
      # Checkout code without initializing submodules
      - uses: actions/checkout@v4
        with:
          submodules: false # Defer submodule initialization

      # Restore Git Submodules Cache
      - name: Restore Git Submodules Cache
        uses: actions/cache@v4
        with:
          path: .git/modules
          key: submodules-${{ github.ref_name }}
          restore-keys: |
            submodules-${{ github.ref_name }}
            submodules-

      # Git Submodule Update
      - name: Git Submodule Update
        run: |
          git submodule sync
          git submodule update --init --recursive

      # Cache Git Submodules
      - name: Cache Git Submodules
        uses: actions/cache@v4
        with:
          path: .git/modules
          key: submodules-${{ github.ref_name }}

      # Restore Node.js Modules Cache
      - name: Restore Node.js Modules Cache
        uses: actions/cache@v4
        with:
          path: ~/.npm
          key: npm-cache-${{ env.NODE_VERSION }}-${{ github.ref_name }}
          restore-keys: |
            npm-cache-${{ env.NODE_VERSION }}-${{ github.ref_name }}
            npm-cache-${{ env.NODE_VERSION }}-
            npm-cache-

      # Use Node.js
      - name: Use Node.js ${{ env.NODE_VERSION }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}

      # Install dependencies
      - name: Install dependencies
        run: npm ci

      # Save Node.js Modules Cache
      - name: Save Node.js Modules Cache
        uses: actions/cache@v4
        with:
          path: ~/.npm
          key: npm-cache-${{ env.NODE_VERSION }}-${{ github.ref_name }}

      - name: Check Compliance
        run:  npm run check-compliance
```
{% enddetails %}

{% details "Pipeline CI/CD Build GitHub Actions" %}
Cette pipeline GitHub Actions construit le site Do-It à partir des submodules Git et applique les changements sur la branche `gh-pages` pour déployer le site. Elle ne conserve que la dernière version du build pour éviter de faire grossir le repository Git inutilement.
```yaml
name: build

on:
  workflow_run:
    workflows: ["check-compliance"]
    types:
      - completed

env:
  NODE_VERSION: "20.7" # Define the Node.js version here

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      # Checkout code without initializing submodules
      - uses: actions/checkout@v4
        with:
          submodules: false # Defer submodule initialization

      # Restore Git Submodules Cache
      - name: Restore Git Submodules Cache
        uses: actions/cache@v4
        with:
          path: .git/modules
          key: submodules-${{ github.ref_name }}
          restore-keys: |
            submodules-${{ github.ref_name }}
            submodules-

      # Git Submodule Update
      - name: Git Submodule Update
        run: |
          git submodule sync
          git submodule update --init --recursive

      # Cache Git Submodules
      - name: Cache Git Submodules
        uses: actions/cache@v4
        with:
          path: .git/modules
          key: submodules-${{ github.ref_name }}

      # Restore Node.js Modules Cache
      - name: Restore Node.js Modules Cache
        uses: actions/cache@v4
        with:
          path: ~/.npm
          key: npm-cache-${{ env.NODE_VERSION }}-${{ github.ref_name }}
          restore-keys: |
            npm-cache-${{ env.NODE_VERSION }}-${{ github.ref_name }}
            npm-cache-${{ env.NODE_VERSION }}-
            npm-cache-

      # Use Node.js
      - name: Use Node.js ${{ env.NODE_VERSION }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}

      # Install dependencies
      - name: Install dependencies
        run: npm ci

      # Save Node.js Modules Cache
      - name: Save Node.js Modules Cache
        uses: actions/cache@v4
        with:
          path: ~/.npm
          key: npm-cache-${{ env.NODE_VERSION }}-${{ github.ref_name }}

      - name: Build
        run: |
          npm run build-github
          npm run node-modules-front
          npm run build-tailwind

    outputs:
      build-dir: ./dist

  deploy:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy
        uses: peaceiris/actions-gh-pages@v4
        with:
          publish_dir: ${{ needs.build.outputs.build-dir }}
          github_token: ${{ secrets.GITHUB_TOKEN }}
          force_orphan: true
          publish_branch: gh-pages
```
{% enddetails %}
