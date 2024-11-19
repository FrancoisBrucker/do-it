---
layout: layout/mon.njk

title: "Initiation au BackEnd: go to learn Go!"
authors:
  - Thomas Merle
date: 2024-10-16

tags: 
  - "temps 2"
  - "Developpement BackEnd"
  - "Go"
  - "DevWeb"
  - "Dark Kitchen"

résumé: "Je réalise ce MON pour m'initier au BackEnd et au language Go afin de pouvoir comprendre le backend de notre projet 3A et de pouvoir y contribuer. Je vais probablement utiliser un tutoriel en ligne et utiliser la documentation Go."
---

{% prerequis %}

- [`Bases en Dev Web`](/cs/contribuer-au-site/#prerequis)

{% endprerequis %}
{% lien %}

[`GoLang Tuto`](https://devopssec.fr/article/configurer-environnement-golang#begin-article-section)

{% endlien %}

- le niveau et les prérequis nécessaires en utilisant la balise [`prerequis`](/cs/contribuer-au-site/#prerequis)
- les autres POK & MON en rapport en utilisant la balise [`lien`](/cs/contribuer-au-site/#lien)

{% note %}
Objectifs :
- Découvrir le language Go, ses utilisations et son utilité pour réaliser le BackEnd d'un site web
- Apprendre à utiliser Go
- Faire un TP d'application : codage d'un jeu de morpions, tic-tac-toe game.

{% endnote %}

## Table des matières<a name="table-des-matières"></a>
- [Table des matières](#table-des-matières)
- [Chapitre 1 : Introduction à Go](#introduction)
- [Chapitre 2 : Les Bases de la Programmation](#bases)
- [Chapitre 3 : Variables et Opérateurs](#variables-operateurs)
- [Chapitre 4 : Les Conditions](#conditions)
- [Chapitre 5 : Les Boucles](#boucles)
- [Chapitre 6 : Les Fonctions](#fonctions)
- [Chapitre 7 : Les Tableaux](#tableaux)
- [Mini Projet: écriture d'un code de jeu de morpions en Go](#projet)
    

## Contenu

# Apprentissage de GoLang

L'objectif de cet apprentissage est de maîtriser les bases du langage Go afin d'écrire un petit jeu de **morpions** ou **tic-tac-toe**. 

---

## Chapitre 1 : Introduction à Go<a name="introduction"></a>

Go est un langage de programmation moderne développé par Google. Il se distingue par sa **simplicité**, sa **performance** et sa **concurrence**.

### Pourquoi choisir Go ?
- **Concis et expressif :** Code lisible et compact.
- **Compilé et performant :** Génère des exécutables rapides.
- **Concurrence facilitée :** Avec des goroutines et des canaux.
- **Communauté active :** De nombreux projets open-source.

### Applications typiques :
- Développement web (back-end)
- Infrastructure (Docker, Kubernetes)
- Data science
- Développement de jeux

---

## Chapitre 2 : Les Bases de la Programmation<a name="bases"></a>

1. **Télécharger et installer Go** : instructions officielles sur [go.dev](https://go.dev/dl/).

### Exemple : Hello, World !
Le programme le plus simple pour afficher du texte.

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

### Points clés :
- **Package** : Groupe de fichiers Go.
- **Fonction `main`** : Point d'entrée du programme.
- **`fmt.Println`** : Fonction pour afficher des messages à la console.

---

## Chapitre 3 : Variables et Opérateurs<a name="variables-operateurs"></a>

### Déclaration des variables
- **Syntaxe classique** : `var nom_variable type`
- **Avec initialisation** : `var nom_variable type = valeur`
- **Inférence de type** : `nom_variable := valeur`

### Types de base
- **Entiers :** `int`, `uint`, etc.
- **Flottants :** `float32`, `float64`
- **Chaînes :** `string`
- **Booléens :** `bool`

### Exemple
```go
var age int = 30
var name string = "Alice"
var isStudent bool = true
```

### Opérateurs
- **Arithmétiques** : `+`, `-`, `*`, `/`, `%`
- **De comparaison** : `==`, `!=`, `<`, `>`
- **Logiques** : `&&`, `||`, `!`

### Exemple
```go
// Opérations arithmétiques
var x, y int = 10, 5
var z float64 = 2.5
result := x + y * int(z) // Conversion de z en int

// Conditions
if age >= 18 {
    fmt.Println("Vous êtes majeur")
} else {
    fmt.Println("Vous êtes mineur")
}

// Boucle for
for i := 0; i < 10; i++ {
    fmt.Println(i)
}

```

### Points clés:
* ***Typage fort**: Go est un langage à typage statique, ce qui signifie que le type d'une variable doit être déclaré explicitement ou déduit par le compilateur.
* **Inférence de type**: Le compilateur peut souvent déduire le type d'une variable lors de son initialisation.
* **Conversion de type**: Il est possible de convertir un type en un autre à l'aide d'une conversion explicite (cast).
* **Constante**: Une valeur qui ne peut pas être modifiée après sa déclaration. On utilise le mot-clé const.
* **Zero value**: Si une variable n'est pas initialisée, elle prend une valeur par défaut (0 pour les nombres, "" pour les chaînes, false pour les booléens).

---

## Chapitre 4 : Les Conditions<a name="conditions"></a>
Dans ce chapitre, nous abordons les conditions en Go, essentielles pour gérer la logique de contrôle dans vos programmes.

## 1. Les instructions `if` et `else`
### Exemple : Contrôle d'entrée en boîte de nuit
Pour automatiser l'entrée des clients selon leur âge, nous utilisons les conditions `if` et `else`.

```go
package main

import (
    "fmt"
    "os"
    "strconv"
)

func main() {
    fmt.Print("Entrez votre âge : ")
    var age int
    fmt.Scan(&age)

    if age < 18 {
        fmt.Println("Sortez !")
    } else {
        fmt.Println("Entrez :)")
    }
}
```

🏁 **Résultats :**
Entrez votre âge : 16 Sortez ! 
Entrez votre âge : 25 Entrez :

## 2. Les instructions `elseif`
L'instruction `else if` permet de gérer des cas supplémentaires lorsque la première condition `if` n'est pas remplie. Elle permet de tester plusieurs alternatives de manière structurée.

## 3. Les instructions `switch` et `case`
L'instruction `switch` simplifie les tests d'égalité multiples, idéale pour des menus ou des choix.

### Exemple : Menu interactif
Ce programme teste différentes valeurs entrées par l'utilisateur et affiche un message approprié :

```go
func main() {
    scanner := bufio.NewScanner(os.Stdin)
    fmt.Print("Votre choix : ")
    scanner.Scan()
    choix, err := strconv.Atoi(scanner.Text())
    if err != nil {
        fmt.Println("Entrez un entier !")
        os.Exit(2)
    }

    switch choix {
    case 0, 1:
        fmt.Println("George Boole !")
    case 7:
        fmt.Println("William Van de Walle !")
    case 23:
        fmt.Println("Pour certains, le nombre 23 est source de nombreux mystères.")
    case 42:
        fmt.Println("La réponse à la question ultime du sens de la vie !")
    case 666:
        fmt.Println("Quand le diable veut une âme, le mal devient séduisant.")
    default:
        fmt.Println("Mauvais choix !")
    }
} 
```

🏁 **Résultats :**
Votre choix : 666
Quand le diable veut une âme, le mal devient séduisant
Votre choix : 7
William Van de Walle !
Votre choix : 1
George Boole !
Votre choix : 0
George Boole !

### Points clés :
- Utiliser `if`, `else if`, et `else` pour structurer la logique.
- `switch` simplifie les tests d'égalité.

---

## Chapitre 5 : Les Boucles<a name="boucles"></a>
Les boucles permettent d'exécuter un bloc de code de manière répétée. En Go, la seule structure de boucle est le mot-clé `for`.
Utilisons une boucle avec une initialisation, une condition et une itération pour les cas où vous savez combien de fois le bloc sera exécuté.

### 1. Boucle avec un nombre d'itérations connu
```go
for i := 0; i < 10; i++ {
    fmt.Println(i)
}
```

### Exemple : Écrire une phrase 100 fois 
```go
func main() {
    for compteur := 0; compteur < 100; compteur++ {
        fmt.Println(compteur+1, ") Je ne dois frapper mes camarades de classe")
    }
}
```

🏁 **Résultats:** 
1. Je ne dois frapper mes camarades de classe
2. Je ne dois frapper mes camarades de classe
...
100. Je ne dois frapper mes camarades de classe

### 2. Boucle avec un nombre d'itérations inconnu
Utilisez une boucle avec une condition pour des itérations dont le nombre n’est pas déterminé à l'avance. La boucle s'arrête quand la condition devient fausse.

### Exemple : Accepter l'entrée en boîte uniquement pour les majeurs :

```go
package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
)

func main() {
    scanner := bufio.NewScanner(os.Stdin)
    var age int

    for age < 18 {
        fmt.Print("Entrez votre âge : ")
        scanner.Scan()
        age, _ = strconv.Atoi(scanner.Text())
    }

    fmt.Println("Bienvenue en boîte de nuit !")
}
```

🏁 **Résultats:** 
Entrez votre âge : 17
Entrez votre âge : 19
Bienvenue en boîte de nuit !

### Points clés :
* Nombre d'itérations connu : Utilisez la syntaxe '`for initialisation` ; `condition` ; `itération`.
* Nombre d'itérations inconnu : Utilisez une condition avec `for`.
* Gérez toujours les entrées utilisateur pour éviter des boucles infinies.

---

## Chapitre 6 : Les Fonctions<a name="fonctions"></a>
Les fonctions structurent le code en regroupant des instructions pour accomplir des tâches spécifiques. Elles améliorent la lisibilité et permettent de réutiliser le code.

### Déclaration d'une Fonction

```go
func nomDeLaFonction(liste_de_paramètres) type_de_retour {
    // Bloc de code
}
```

1. **Fonction sans type de retour ni paramètres**
Une fonction simple qui n'accepte ni paramètres ni type de retour.

### Exemple : 
```go
func affichage() {
    fmt.Println("#################################")
    fmt.Println("\tBonjour")
    fmt.Println("#################################")
}

func main() {
    affichage()
}
```

2. **Fonction avec paramètres et type de retour**
Une fonction peut accepter plusieurs paramètres, quels que soient leurs types.

### Exemple : 
```go
func affichage(nom string, age int) {
    fmt.Println("Bonjour", nom, "vous avez", age, "ans")
}

func main() {
    affichage("Hatim", 9)
    affichage("Alex", 12)
}
```

🏁 **Résultat:**
Bonjour Hatim vous avez 9 ans
Bonjour Alex vous avez 12 ans

3. **Fonction avec type de retour**
Utilisez le mot-clé `return` pour renvoyer une valeur, qui peut être stockée ou utilisée directement.

### Exemple : 
```go
func maxNbr(a int, b int) int {
    if a > b {
        return a
    }
    return b
}

func main() {
    max := maxNbr(10, 30)
    fmt.Println(max)
    fmt.Printf("Valeur : %d , Type : %T\n", maxNbr(50, 30), maxNbr(50, 30))
}
```

🏁 **Résultat:**
30
Valeur : 50 , Type : int

4. **Retourner plusieurs valeurs**
Une fonction peut renvoyer plusieurs valeurs de types différents.

### Exemple : 
```go
func additionTrois(a int, b int) (int, int) {
    return a + 3, b + 3
}

func main() {
    a, b := 5, 8
    fmt.Println("Avant fonction a =", a, " b =", b)
    a, b = additionTrois(a, b)
    fmt.Println("Après fonction a =", a, " b =", b)
}
```

🏁 **Résultat:**
Avant fonction a = 5  b = 8
Après fonction a = 8  b = 11

---

## Chapitre 7 : Les Tableaux<a name="tableaux"></a>
Les tableaux permettent de stocker un ensemble de valeurs de même type. Ils peuvent être statiques (taille fixe) ou multidimensionnels.

## 1. Initialisation des Tableaux

### Déclaration
```go
var nomTableau [taille]type
```

### Exemple:
```go
func main() {
    var tableauInt [10]int
    var tableauFloat [10]float32
    var tableauString [10]string
    var tableauBool [10]bool

    fmt.Println("Valeur par défaut des tableaux :")
    fmt.Println("Int :", tableauInt)
    fmt.Println("Float :", tableauFloat)
    fmt.Println("String :", tableauString)
    fmt.Println("Bool :", tableauBool)
}
```

🏁 **Résultat :**
Int : [0 0 0 0 0 0 0 0 0 0]
Float : [0 0 0 0 0 0 0 0 0 0]
String : [         ]
Bool : [false false false false false false false false false false]


## 2. Accès aux éléments
* Accès par Index

```go
func main() {
    var jours = [7]string{"lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"}

    fmt.Println("Premier jour :", jours[0])
    fmt.Println("Dernier jour :", jours[len(jours)-1])
}
``` 

* Parcourir avec une Boucle range
* 
```go
func main() {
    var jours = [7]string{"lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"}

    for index, jour := range jours {
        fmt.Println(jour, "est le jour numéro", index+1)
    }
}
```

🏁 **Résultat:**
lundi est le jour numéro 1
mardi est le jour numéro 2
...
dimanche est le jour numéro 7

## 3. Modifier des valeurs

```go
func main() {
    var jours = [5]string{"Hatim", "Robert", "Inconnu", "Ahmed", "Inconnu"}

    jours[0] = "Alex" // Remplacer "Hatim" par "Alex"
    fmt.Println(jours)
}
```

* Modifier via une fonction

```go
func replaceByHatim(jours [5]string) [5]string {
    for i, jour := range jours {
        if jour == "Inconnu" {
            jours[i] = "Hatim"
        }
    }
    return jours
}
```

## 4. Tableaux à Deux Dimensions

```go
func main() {
    const (
        maxLigne   = 3
        maxColonne = 4
    )
    var tableau [maxLigne][maxColonne]int
    fmt.Println(tableau)
}
```

**Modifier une valeur :**
```go
tableau[0][1] = 42 // Modifier l'élément de la première ligne, deuxième colonne
```

### Points Clés:
* **Initialisation** : Un tableau a une taille fixe et un type unique pour ses éléments.
* **Accès** : Utilisez les index pour accéder ou modifier des éléments.
* **Boucle** : Utilisez range pour parcourir les éléments avec index et valeurs.
* **Multidimensionnel** : Permet de modéliser des structures comme des grilles.
---

🎯 **Prochaine étape :** Utiliser ces concepts pour coder un jeu de morpions ou tic tac toe game en Go !

---

## Mini Projet: écriture d'un code de jeu de morpions en Go<a name="projet"></a>

### Introduction

L'objectif de ce projet est de développer un jeu de morpions en ligne de commande avec Go. Les joueurs alternent leurs tours pour placer leur symbole (X ou O) sur un damier 3x3, et le jeu se termine lorsqu'un joueur aligne trois symboles ou qu'il n'y a plus de place.

### Etape 1 : Initialisation

```go
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

// Taille du damier et symboles des joueurs
const (
	tailleDamier   = 3
	symboleJoueur1 = "X"
	symboleJoueur2 = "O"
)

// Damier initial
var damier = [3][3]string{
	{"1", "2", "3"},
	{"4", "5", "6"},
	{"7", "8", "9"},
}

var joueur1 = true // Le joueur 1 commence
```

**Explications:**
* Constantes globales : Taille du damier et symboles des joueurs pour éviter les erreurs dans le code.
* Damier : Utilisation d'un tableau 2D pour modéliser un damier clair.
* Tour du joueur : La variable joueur1 permet de savoir à qui c’est le tour.

**Difficultés rencontrées:**
Créer un damier en 2D a été un défi au départ, car cela nécessite d’ajuster les indices lors des placements. J’ai choisi un tableau 2D pour une meilleure lisibilité lors de l’affichage.


### Étape 2 : Fonction Principale

```go
func main() {
	jouer()
}

func jouer() {
	for {
		afficherDamier()
		numeroCase := recupererSaisieUtilisateur()
		placerSymbole(numeroCase)

		if verifierVictoire() {
			afficherDamier()
			fmt.Println(obtenirNomJoueur(), "a gagné !")
			break
		}

		if verifierMatchNul() {
			afficherDamier()
			fmt.Println("Match nul !")
			break
		}

		joueur1 = !joueur1 // Changement de joueur
	}
}
```

**Explications:**
* Boucle principale : Le jeu continue jusqu'à ce qu’un joueur gagne ou qu’il n’y ait plus de cases disponibles.
* Fonctions clés : `recupererSaisieUtilisateur`, `placerSymbole`, `verifierVictoire` et `verifierMatchNul`.

**Difficultés rencontrées:**
La gestion des conditions de victoire dans une structure 2D a nécessité une réflexion sur les indices (lignes, colonnes, diagonales).

### Étape 3 : Gestion des Entrées Utilisateur

```go
func recupererSaisieUtilisateur() (ligne, colonne int) {
	scanner := bufio.NewScanner(os.Stdin)
	for {
		fmt.Printf("%s, entrez la ligne et la colonne (ex: 1 2) : ", obtenirNomJoueur())
		scanner.Scan()
		input := scanner.Text()
		fmt.Sscanf(input, "%d %d", &ligne, &colonne)

		// Vérification des limites et des cases libres
		if ligne >= 1 && ligne <= tailleDamier && colonne >= 1 && colonne <= tailleDamier && damier[ligne-1][colonne-1] != symboleJoueur1 && damier[ligne-1][colonne-1] != symboleJoueur2 {
			return ligne - 1, colonne - 1
		}

		fmt.Println("Entrée invalide ou case occupée. Essayez encore.")
	}
}
```

**Explications:**
Cette fonction `recupererSaisieUtilisateur` : 
* Vérifie que l’entrée est valide (nombres dans les limites, case libre).
* Utilise `fmt.Sscanf` pour interpréter facilement les coordonnées.

**Difficultés rencontrées:**
Le parsing des coordonnées a été délicat, mais l'utilisation de fmt.Sscanf a grandement simplifié la lecture des saisies.

### Étape 4 : Mise à Jour du Damier

```go
func placerSymbole(ligne, colonne int) {
	if joueur1 {
		damier[ligne][colonne] = symboleJoueur1
	} else {
		damier[ligne][colonne] = symboleJoueur2
	}
}

func afficherDamier() {
	fmt.Println()
	for _, ligne := range damier {
		fmt.Println(ligne)
	}
	fmt.Println()
}
```

**Explications:**
* La fonction `placerSymbole` met à jour le damier avec le symbole du joueur.
* La fonction `afficherDamier` montre l'état actuel du jeu.

### Étape 5 : Vérification des Conditions

```go
func verifierVictoire() bool {
	// Vérifie les lignes, colonnes et diagonales
	for i := 0; i < tailleDamier; i++ {
		if damier[i][0] == damier[i][1] && damier[i][1] == damier[i][2] {
			return true
		}
		if damier[0][i] == damier[1][i] && damier[1][i] == damier[2][i] {
			return true
		}
	}
	// Vérifie les diagonales
	return (damier[0][0] == damier[1][1] && damier[1][1] == damier[2][2]) ||
		(damier[0][2] == damier[1][1] && damier[1][1] == damier[2][0])
}

func verifierMatchNul() bool {
	for _, ligne := range damier {
		for _, caseDamier := range ligne {
			if caseDamier != symboleJoueur1 && caseDamier != symboleJoueur2 {
				return false
			}
		}
	}
	return true
}
```

**Explications:**
* La focntion `verifierVictoire` vérifie les conditions de victoire pour les lignes, colonnes et diagonales.
* La focntion `verifierMatchNul` vérifie si toutes les cases sont occupées.

### Synthèse sur le TP 

**Structure choisie :**
* Un tableau 2D pour modéliser le damier.
* Des fonctions modulaires pour chaque aspect du jeu : affichage, saisie utilisateur, vérifications et gestion des tours.
* Utilisation de la bibliothèque `bufio` : Je n’étais pas familier avec son fonctionnement pour les entrées utilisateur, mais des recherches sur les forums Go et l’expérimentation m’ont permis de surmonter ce problème rapidement.

**Difficultés et Résolutions:**
#### Blocage : Gestion des indices dans un tableau 2D
**Problème** : L'utilisation d'un tableau 2D au lieu d'un tableau 1D rendait la vérification des conditions de victoire plus complexe, notamment pour les diagonales.
💡 *Solution* : 
J'ai utilisé des boucles pour parcourir dynamiquement chaque ligne, colonne et diagonale.
J'ai également vérifié manuellement les indices critiques pour les diagonales, car elles ne peuvent pas être parcourues directement comme une ligne ou une colonne.

#### Blocage : Contrôle des entrées utilisateur
**Problème** : Les utilisateurs peuvent entrer des valeurs non valides (par exemple, des lettres, des nombres hors limites ou des cases déjà occupées).
💡 *Solution* :
Une boucle `for` a été mise en place pour redemander une entrée valide tant que la saisie n’était pas correcte.
J'ai utilisé `fmt.Sscanf` pour analyser les coordonnées et ajouté des messages explicatifs pour guider les joueurs.

#### Blocage : Gestion des conditions de victoire
**Problème** : Vérifier les alignements (lignes, colonnes et diagonales) dans un tableau 2D nécessitait une logique différente pour chaque type d'alignement.
💡 *Solution* :
J'ai écrit une fonction générique qui vérifie les alignements de manière conditionnelle.
En cas de répétitions (par exemple, plusieurs lignes), j'ai optimisé le code en regroupant les vérifications dans une boucle.

#### Blocage : Affichage esthétique du damier
**Problème** : Le damier n’était pas lisible au début à cause d’un espacement mal géré.
💡 *Solution* :
J’ai ajusté le formatage en ajoutant des espaces et en séparant les lignes par des bordures visuelles pour rendre le jeu plus clair.

**Démo du jeu  via le terminal:**

<video width="600" controls>
  <source src="demo_morpions.mov" type="video/quicktime">
</video>

{% lien %}
**Lien vers le Github du projet:**
[Projet Morpions Go](https://github.com/ThomasMerle25/morpions-go "Morpions Go")

**Lien Tutoriel suivi:**
[`GoLang Tuto`](https://devopssec.fr/article/configurer-environnement-golang#begin-article-section)
{% endlien %}

## Horodateur

Toutes les séances et le nombre d'heures que l'on y a passé.

| Date | Heures passées | Indications |
| -------- | -------- |-------- |
| 05-12/11/2024  | 6H | Tutoriel sur le site web: initilaisation de mon environnement Go et apprentissage des bases|
| 14/11/2024  | 1H | Initialisation du jeu et fonction principale |
| 16/11/2024  | 1H | Gestion des entrées utilisateurs |
| 17/11/2024  | 1H | Mise a jour du damier et vérifications des conditions |
| 18/11/2024  | 2H | Corrections du code et écritures des tests unitaires |


