---
layout: layout/mon.njk

title: "MON 2.1 : rappels en Python"
authors:
  - Clarisse Francese

date: 1970-11-01
tags: 
  - "temps 2"
  - "python"
  - "vert"

résumé: "J'ai besoin d'utiliser Python pour notre projet de groupe Avat'Art, or je n'ai pas touché à ce logiciel depuis la fin de la prépa. Je compte donc dépoussiérer mes connaissances et essayer de retrouver une partie de mon niveau d'avant."
---

{% prerequis %}

MON débutant, aucun prérequis

{% endprerequis %}
{% lien %}

[Mon Github perso](https://github.com/Clarisse-Francese/GithubClarisse.git) : vous pouvez y retrouver tous les codes des exos Python et ma fiche récap Python  
[📚 60 Exercices corrigés en Python & POO👍👍](https://www.coodemaroc.com/2021/09/python.html) Consulté le 18 octobre 2024.  
[Une sélection d'exercices pour apprendre la programmation Python](https://python.developpez.com/exercices/) Consulté le 18 octobre 2024.

{% endlien %}

## Sommaire

- [Rappels et exos de bases](#rappels)
- [Exercice inventé : groupes aléatoires en Do_It](#exi)
- [Conclusion](#ccl)

<h2 id=rappels> 📘Rappels et exos de bases</h2>

J'ai d'abord **créé mon propre espace Github** sur Visual studio code puis consacré 1h à relire mes fiches sur mes **cours informatiques en prépa**. J'ai ainsi pris le temps d'écrire les fonctions les plus utiles en python sur un fichier nommé **Rappels Python** que je garde sur mon Github perso. J'ai surtout révisé la déclaration de variables, les listes, les boucles for, while et les fonctions.

Une fois ces premiers rappels faits, j'ai décidé de **faire des exercices** pour m'entrainer à coder. J'ai pioché les exercices que je trouvais pertinents sur ces 2 sites [📚 60 Exercices corrigés en Python & POO👍👍](https://www.coodemaroc.com/2021/09/python.html) et [Une sélection d'exercices pour apprendre la programmation Python](https://python.developpez.com/exercices/).
L'ensemble des exercices réalisés sont disponibles dans le fichier **Ex de bases** de [mon Github](https://github.com/Clarisse-Francese/GithubClarisse.git).

{% details "Exemple d'un des exercices codés " %}

Ex 13 : Dans la série "Kaamelott" d'Alexandre Astier, le "**cul de chouette**" est le jeu favori du tavernier et du chevalier Karadoc. Le but présumé de ce jeu est de jeter des dés en tentant d'atteindre un certain total par jet. Le but de cet exercice est d'écrire une fonction qui, pour une valeur donnée, renvoie toutes les **solutions de 3 dés** (dés classiques allant de 1 à 6) pouvant donner cette valeur. Attention, les solutions doivent être uniques.

```python
def cul_de_chouette (valeur) :
    res = list()
    for i in range (1,7):
        for j in range (i,7):
            for k in range (j,7):
                if k+i+j == valeur :
                    res.append((i,j,k))
                    
    return res

n = int(input("Quelle est la valeur à atteindre ? "))
print("Les combinaisons de dés possibles pour faire", n,"sont",cul_de_chouette(n))
```
En rentrant par exemple la valeur 7, on obtient bien les valeurs de dés possibles pour atteindre cette somme : 
```python
Quelle est la valeur à atteindre ? 7
Les combinaisons de dés possibles pour faire 7 sont [(1, 1, 5), (1, 2, 4), (1, 3, 3), (2, 2, 3)]
```
{% enddetails %}


<h2 id=exi> 🎲Exercice inventé : groupes alétoires en Do_It</h2>

Après avoir fait 13 exercices trouvés sur internet, j'ai eu envie de résoudre un exercice qui répond à une poblématique que j'ai eu l'autre jour. En effet, je pense que la **restitition des POK&MON serait très intéressante à faire en 3 groupe de 8 élèves** chacun. Mais pour que l'échange soit optimale, il faudrait que ces groupes soit créé aléatoirement (pour éviter de choisir d'être avec ses copains) et avec une répartition équitable des différents profils vert, bleu et saumon dans chaque groupe.  
Ainsi, je vais **créér un programme** qui prend en **entrée un dictionnaire contenant la liste des élèves de Do_It et la couleur par laquelle ils se définissent** et qui renvoie en **sortie 3 groupes de 8 élèves répartis aléatoirement en respectant la proportion des couleurs**.  
Ayant souvent entendu que **ChatGPT** était très utile pour coder, j'ai décidé de m'appuyer sur lui pour réaliser la majorité du code.

J'ai d'abord demandé à ChatGPT de créer le dictionnaire, voici ma requête :  
*créé moi un dictionnaire sur python avec 2 valeurs :  
Prénoms triés par odre alphabétique : Mathis, Mbaye, Baptiste, Clarisse, Damien, Emma, Valentin, Sophia, Charles, Matthieu, Jeanne, Juliette, Kévin, Alix, Lola, Manuela, Loïck, Esther, Inès, Isée, Thomas, Guillaume, Titouan, Sofiane, Victor  
Couleur : aléatoirement attribué entre "bleu", "vert" et "saumon"*

J'ai ensuite modifié le dictionnaire pour mettre des couleurs plus cohérentes avec les élèves en regardant leur choix de cours dans le tableau [Étudiants Do_It](https://docs.google.com/spreadsheets/d/1ZMgJ7oZyIxTkz6Cj7Ko-sEQpEDAAw8SkJBjZ4Dtjaig/edit?gid=0#gid=0) du drive Do_It.  
On obtient alors le dictionnaire suivant : 
```python
promo = {'Alix': 'bleu', 'Baptiste': 'saumon', 'Charles': 'saumon', 'Clarisse': 'saumon', 'Damien': 'saumon', 'Emma': 'vert', 'Esther': 'bleu', 'Guillaume': 'bleu', 'Inès': 'saumon', 'Isée': 'saumon', 'Jeanne': 'saumon', 'Juliette': 'bleu', 'Kévin': 'vert', 'Lola': 'bleu', 'Loïck': 'vert', 'Manuela': 'vert', 'Mathis': 'vert', 'Matthieu': 'saumon', 'Mbaye': 'bleu', 'Sofiane': 'vert', 'Sophia': 'bleu', 'Thomas': 'vert', 'Titouan': 'bleu', 'Valentin': 'vert', 'Victor': 'saumon'}
```

Puis, j'ai formulé des **requêtes à ChatGPT** pour créer la fonction et l'**améliorer après chaque test**. Voici mes requêtes : 

- *Je veux une fonction qui prenne en entrée la promo et qui retourne en sortie 3 listes contenant chacune 8 élèves. Chaque liste doit être la mieux répartie possible entre les couleurs. Ainsi les profils bleu, saumon et vert sont équitablement répartis entre les 3 listes.*
- *Est-ce que tu peux préciser entre parenthèse à coté de chaque prénom d'élève sa couleur associée* 
- *Est ce que à la fin tu peux ajouter un récap du nombre d'élève de chaque couleur dans chacun des groupes* 
- *Peux tu afficher le récapitulatif à la fin après la composition des groupes et supprimer les ' dans l'affichage des listes des groupes* 
- *Idem je veux que tu supprimes les ' dans l'affichage du récap des couleurs à la fin*

Puis j'ai modifié manuellement quelques paramètres d'affichage. Par exemple pour écrire uniquement (b) au lieu de (bleu) dans les listes renvoyées. Ainsi, après cette super conversation avec ChatGPT, on obtient le code ci-dessous

```python
import random

def repartir_groupes(promo):
    bleu = [prenom for prenom, couleur in promo.items() if couleur == 'bleu']
    vert = [prenom for prenom, couleur in promo.items() if couleur == 'vert']
    saumon = [prenom for prenom, couleur in promo.items() if couleur == 'saumon']
    
    random.shuffle(bleu)
    random.shuffle(vert)
    random.shuffle(saumon)

    groupes = [[] for _ in range(3)]  # 3 groupes
    couleur_counts = [{ 'bleu': 0, 'vert': 0, 'saumon': 0 } for _ in range(3)]  # Compteur pour chaque groupe

    for i in range(8):  # 8 élèves par groupe
        for j in range(3):  # Répartir entre les 3 couleurs
            if len(bleu) > 0:
                groupes[j].append(f"{bleu.pop()} (b)")
                couleur_counts[j]['bleu'] += 1
            if len(vert) > 0:
                groupes[j].append(f"{vert.pop()} (v)")
                couleur_counts[j]['vert'] += 1
            if len(saumon) > 0:
                groupes[j].append(f"{saumon.pop()} (s)")
                couleur_counts[j]['saumon'] += 1

    return groupes, couleur_counts

# Exemple d'utilisation
promo = {'Alix': 'saumon', 'Baptiste': 'vert', 'Charles': 'saumon', 'Clarisse': 'bleu', 'Damien': 'vert', 'Emma': 'bleu', 'Esther': 'vert', 'Guillaume': 'bleu', 'Inès': 'vert', 'Isée': 'bleu', 'Jeanne': 'saumon', 'Juliette': 'vert', 'Kévin': 'bleu', 'Lola': 'vert', 'Loïck': 'saumon', 'Manuela': 'saumon', 'Mathis': 'saumon', 'Matthieu': 'bleu', 'Mbaye': 'saumon', 'Sofiane': 'saumon', 'Sophia': 'bleu', 'Thomas': 'saumon', 'Titouan': 'bleu', 'Valentin': 'vert', 'Victor': 'vert'}

groupes, couleur_counts = repartir_groupes(promo)
for i, groupe in enumerate(groupes):
    print(f"Groupe {i + 1}: {', '.join(groupe)}")

# Affichage du récapitulatif des couleurs sans apostrophes
print("\nRécapitulatif des couleurs :")
for i in range(3):
    print(f"Groupe {i + 1}: bleu: {couleur_counts[i]['bleu']} - vert: {couleur_counts[i]['vert']} - saumon: {couleur_counts[i]['saumon']}")
```

En testant la fonction, voici l'une des réponses possibles : 
```python
Groupe 1: Guillaume (b), Emma (v), Victor (s), Titouan (b), Valentin (v), Matthieu (s), Mbaye (b), Kévin (v), Inès (s) 
Groupe 2: Alix (b), Loïck (v), Damien (s), Juliette (b), Thomas (v), Isée (s), Lola (b), Manuela (v), Baptiste (s) 
Groupe 3: Sophia (b), Mathis (v), Jeanne (s), Esther (b), Sofiane (v), Charles (s), Clarisse (s)

Récapitulatif des couleurs : 
Groupe 1: bleu: 3 - vert: 3 - saumon: 3 
Groupe 2: bleu: 3 - vert: 3 - saumon: 3 
Groupe 3: bleu: 2 - vert: 2 - saumon: 3
```

On a donc bien répondu à l'objectif ! J'étais assez i**mpressionnée de la facilité avec laquelle on peut coder des petites fonctions grâce à ChatGPT** maintenant.
En retravaillant sur ce MON plus tard, j'ai réalisé que la fonction créé ne répondait en réalité pas pleinement à l'objectif car les 3 groupes ne sont pas équilibrés en nombre (9, 9 et 7 élèves au lieu de 9, 8 et 8 élèves). J'ai donc tenté de corriger avec l'aide de ChatGPT ce problème mais impossible d'y arriver. Soit il répartit bien en nombre, soit il répartit bien en couleur mais je n'arrive pas à créer une fonction qui prenne en compte les 2 critères. Ainsi, **j'ai vu les limites de ChatGPT**.

<h2 id=ccl> 👍Conclusion</h2>

Ce MON m'a bien permis de **dépoussiérer mes connaissances sur Python** pour être plus à l'aise dans mon projet de groupe donc **l'objetif est atteint**. Je pense avoir plutôt bien organisé mon temps et ma manière d'apprendre car si c'était à refaire je ne changerai rien à mon organisationce pendant ce MON.

## ⌛Horodatage

| Date | Heures passées | Indications |
| -------- | -------- |-------- |
| Jeudi 17/10 | 2h | création Github perso, relecture de mes cours de prépa et rédaction de fiche Rappels Python|
| Jeudi 17/10 | 2h | ex 1 à 9 réalisés (voir Github perso) |
| Vendredi 18/10 | 1h30 | ex 10 et 11 réalisés avec les bibliothèques numpy et random (voir Github perso) |
| Mercredi 23/10 | 1h15 | ex 12 et 13 (voir Github perso) |
| Mercredi 23/10 | 2h | ex inventé groupes aléatoires en Do_It et rédaction du MON sur Github |
| Mardi 12/10 | 0h30 | ex inventé groupes aléatoires en Do_It : tentative de correction du code |
| Mardi 12/10 | 0h45 | ex 14 (voir Github perso|