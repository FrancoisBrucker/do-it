# Ce que tu dois connaître avant de publier sur le site

Tu dois d'abord lire le [README.md](README.md) et t'assurer d'avoir le projet qui fonctionne.

Voilà la structure du site qu'il faudra respecter pour ne pas que ça devienne le bazar !

Pour éviter d'avoir à écrire son nom prénom entier on va utiliser le trigramme ! Si je m'appelle François BRUCKER, mon trigramme correspondant sera **FBR**, ça sera le nom de chacun de mes dossiers au sein des différentes catégories.

```bash
src
├── pok
│   └── 2022-2023
│       └── FBR
|           ├── pok-1.md
|           ├── pok-2.md
|           └── pok-3.md
├── mon
│   └── 2022-2023
│       └── FBR
|           ├── mon-1-1.md
|           ├── mon-1-1.md
|           ├── mon-2-1.md
|           ├── mon-2-2.md
|           ├── mon-3-1.md
|           └── mon-3-2.md
├── projets
│   └── 2022-2023
│       └── FBR-LPI-FMA
|           └── index.md
└── promos
    └── 2022-2023
        └── FBR
            └── index.md
```

Tu peux maintenant te référer aux différentes sections pour écrire du contenu !

## Créer sa page de profil (à faire au début d'année)

Afin de centraliser tous vos travaux et pouvoir y accéder facilement plus tard, vous allez devoir vous créer une page de profil.
Je vais alors créer un dossier portant le nom de mon trigramme. Je m'appelle François BRUCKER, mon trigramme c'est FBR et je suis en promo 2022-2023 donc je crée le dossier à cet endroit là `./src/promos/2022-2023/FBR/` et à l'intérieur je créé un fichier `index.md`. Voilà le template de base que vous pouvez embellir si vous maîtrisez un peu le CSS ! Cette page sera bien entendu à compléter au fur et à mesure de l'année afin d'ajouter les liens vers vos POK&MON et projet.

**Attention : pour apparaître sur la page qui liste les copains de ma promo, ma page doit avoir le tag 'promo20XX_20XX'. (avec les bonnes années)**

```markdown
---
layout: layout/post.njk

title: "François BRUCKER"
tags: ['promo2022_2023']

---

La liste de mes POK pour cette année :

1. Blabla
2. Blabla
3. Blabla



La liste de mes MON pour cette année :

## Temps 1

1. Blabla
2. Blabla

## Temps 2

1. Blabla
2. Blabla

## Temps 3

1. Blabla
2. Blabla
```

## Écrire un MON

Je suis François BRUCKER, élève de Do-It promo 2022-2023 et je veux écrire mon MON 2.1. Je vais donc créer le fichier `mon-2-1.md` dans le dossier `./src/mon/2022-2023/FBR/`. Je vais ensuite utiliser le template suivant :

**Attention : pour apparaître sur la page qui liste tous les MONs, votre MON doit avoir le tag 'mon'.**

```
---
layout: layout/post.njk

title: "Mon super MON qui déchire"
authors:
  - François BRUCKER
résumé: "Découverte de HTML & CSS"

tags: 
  - 'html'
  - 'css'
---

C'est trop cool !
```

On choisit ici d'écrire le prénom avec une majuscule et le nom de famille tout en majuscule. L'idée étant de rester consistent sur l'ensemble du site afin de n'avoir qu'un seul vous.

Je n'oublie pas d'aller modifier ma page de profil dans `.src/promos/2022-2023/FBR/index.md`

## Écrire un POK

Je suis François BRUCKER, élève de Do-It promo 2022-2023 et je veux écrire mon POK 3. Je vais donc créer le fichier `pok-3.md` dans le dossier `./src/pok/2022-2023/FBR/`. Je vais ensuite utiliser le template suivant :

**Attention : pour apparaître sur la page qui liste tous les POKs, votre MON doit avoir le tag 'pok'.**

```
---
layout: layout/post.njk

title: "Mon super POK qui claque"
authors:
  - François BRUCKER
résumé: "Découverte de HTML & CSS"

tags: 
  - 'html'
  - 'css'
tags: 
  - 'html'
  - 'css'


---

C'est trop cool !
```

De la même façon on choisit ici d'écrire le prénom avec une majuscule et le nom de famille tout en majuscule. L'idée étant de rester consistent sur l'ensemble du site afin de n'avoir qu'un seul vous.

Je n'oublie pas d'aller modifier ma page de profil dans `.src/promos/2022-2023/FBR/index.md`

## Écrire un projet

Je suis François BRUCKER, élève de Do-It promo 2022-2023 et je veux écrire mon projet avec Laetitia PIET (LPI) et Florian MAGNANI (FMA). Je vais donc créer le fichier `index.md` dans le dosser `./src/projets/2022-2023/nom-du-projet/`. Je vais ensuite utiliser le template suivant :

**Attention : pour apparaître sur la page qui liste tous les projets, votre MON doit avoir le tag 'projet'.**

```
---
layout: layout/post.njk

title: "My Project"
authors:
  - François BRUCKER
  - Laetitia PIET
  - Florian MAGNANI
résumé: "Le meilleur des projets"
tags: 
   - 'projet'
---


On a bien travaillé !
```

Toujours pareil, on choisit ici d'écrire le prénom avec une majuscule et le nom de famille tout en majuscule. L'idée étant de rester consistent sur l'ensemble du site afin de n'avoir qu'un seul vous.

Je n'oublie pas d'aller modifier ma page de profil dans `.src/promos/2022-2023/FBR/index.md`.
