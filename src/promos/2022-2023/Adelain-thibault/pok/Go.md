---
layout: layout/pok.njk

title: "POK Thibault Adelain - Autres - Go"
authors:
  - Thibault Adelain

date: 2023-01-25

tags:
  - 'temps 3'
---

## Objectifs

- Prendre en main le langage Go dont :
  - ~~Prise en main~~
  - ~~Premiers programmes~~
  - ~~Tests~~
  - ~~REST API~~

## Go

Le langage [Go](https://go.dev/), également connu sous le nom de Golang, est un langage de programmation open source conçu par Google en 2007. Go est un langage de programmation compilé, qui se concentre sur la simplicité, la sécurité et la rapidité d'exécution des programmes. Par exemple, Go intègre des vérifications de sécurité lors de la compilation, telles que la gestion des pointeurs, pour éviter les erreurs de segmentation et les bugs de mémoire (comme les dépassements piles). Go offre également des fonctionnalités pour la programmation concurrente (vous pouvez écrire des programmes qui exécutent plusieurs tâches simultanément), qui peuvent aider à éviter les conflits d'accès aux données. Go a été conçu pour être facile à apprendre, avec une syntaxe simple et concise. Je n'ai eu aucun mal à à prendre en main Go venant de python.

[D'après les créateurs](https://go.dev/doc/faq), Go a été conçu pour combiner la facilité de programmation d'un langage interprété à typage dynamique avec l'efficacité et la sécurité d'un langage compilé à typage statique. Go devait être fiable, rapide à écrire et surtout à exécuter. Voici quelques objectifs que les développeurs ont voulu atteindre :

- un système de types expressif mais léger
- la concurrence et la collecte de déchets
- la spécification rigide des dépendances
- etc

Go est aussi connu pour sa grande efficacité, avec un temps de compilation et d'exécution rapide. Vous pouvez retrouver les cas d'utilisation classiques [ici](https://go.dev/solutions/use-cases).

## Tutos pour débuter

Tutos sur la [doc officielle](https://go.dev/doc/tutorial/) dont :

- [Getting started](https://go.dev/doc/tutorial/getting-started)
- [Getting started with fuzzing](https://go.dev/doc/tutorial/fuzz)
- [Developing a RESTful API with Go and Gin](https://go.dev/doc/tutorial/web-service-gin)
- [A tour of Go](https://go.dev/tour/welcome/1)

## Quelques examples

#### REST API

[Tuto](https://go.dev/doc/tutorial/web-service-gin)

Le développement web avec Gin ressemble beaucoup à Flask. C'est un framework minimal qui laisse beaucoup de liberté au développeur. Il est donc très facile et rapide de développer une API basique avec gin, mais lorsque le projet grandi, cela demande une certaine méthode/expérience pour organiser le projet pour qu'il reste maintenable.

*Note: pour un ORM avec Go : voir [GORM](https://github.com/go-gorm/gorm).*

Exemple :

```go
package main

import (
 "github.com/gin-gonic/gin"
 "net/http"
 "strconv"
)

var count_user = 0

type User struct {
 ID     int    `json:"id"`
 Name   string `json:"name"`
}

var users = []User{}

func NewUser(name string) User {
 count_user++
 return User{count_user, name}
}

func main() {

 router := gin.Default()
 router.GET("/users", getUsers)
 router.GET("/user/:id", getUserByID)
 router.POST("/createUser", postUser)

 router.Run("localhost:5080")
}

func getUsers(c *gin.Context) {
 c.IndentedJSON(http.StatusOK, users)
}

func postUser(c *gin.Context) {
 var NewUser User

 err := c.BindJSON(&NewUser)
 if err != nil {
  return
 }

 users = append(users, NewUser)
 count_user++
 c.IndentedJSON(http.StatusOK, NewUser)
}

func getUserByID (c *gin.Context) {
 id := c.Param("id")

 for _, user := range users {
  if strconv.Itoa(user.ID) == id {
   c.IndentedJSON(http.StatusOK, user)
   return
  }
 }
 c.IndentedJSON(http.StatusNotFound, gin.H{"message": "User not found"})
}
```

Comme vous pouvez le voir, créer une application web basique se fait en quelques lignes de code.

#### Test avec Fuzzing

[Tuto](https://go.dev/doc/tutorial/fuzz)

Tester son programme est essentiel. Le fuzzing est une méthode permettant de tester son programme avec un grand nombre d'entrée aléatoires. Attention, tester son programme avec un Fuzzer ne dispense pas des tests unitaires. En effet, vous ne pourrez pas contrôler l'entrée et la sortie avec le fuzzing, vous pouvez seulement vérifier des pattern, contrairement aux tests unitaires ou vous pourrez avoir une vision entrée/sortie.

Le fuzzing permet toutefois d'explorer des chemins qui n'ont pas été prévus par le développeur lors de la conception de l'app, et donc de débogguer des programmes / de corriger des vulnérabilités. C'est donc un outil supplémentaire pour tester nos codes.

Je vous laisse suivre le [tuto](https://go.dev/doc/tutorial/fuzz) pour plus de détails.

#### Programmation objet

Personnellement, venant du python/C++, j'ai dû m'adapter à une programmation objet complètement différente.

Go et C++ sont deux langages de programmation avec des approches différentes en matière de programmation orientée objet.

La programmation orientée objet en Go est basée sur la définition et l'utilisation de types structurés et d'interfaces. Contrairement à d'autres langages de programmation orientée objet, Go n'a pas de notion de classes.

Un exemple pour comprendre :

```go
package main

import "fmt"

type Animal interface {
 isScared() bool
}

type Cat struct {
 Name string
}

type Dog struct {
 Name string
}

func (c Cat) isScared() bool {
 return true
}

func (d Dog) isScared() bool {
 return false
}

func isScared(a Animal) {
 fmt.Println(a.isScared())
}

func main() {

 catty := Cat{"Catty"}
 doggy := Dog{"Doggy"}

 println(doggy.isScared()) // method of doggy instance of Dog
 println(catty.isScared()) // method of catty instance of Cat

 isScared(catty) // interface Animal
 isScared(doggy) // interface Animal
}
```

Jusque là, rien de bien différent de la programmation objet classique, à part que l'on définit des types au lieu de classes. Chaque type à une méthode isScared.

Maintenant, voyons le concept d'interface. Les interfaces sont définies comme une collection de méthodes, où chaque méthode spécifie le nom de la fonction et le type de retour attendu.

Dans l'exemple ci-dessus, on a définit une fonction isScared sur l'interface animal pour savoir si l'animal est peureux ou non.

*Note : Lorsqu'un type implémente toutes les méthodes définies dans une interface, il est considéré comme implémentant cette interface. Cela signifie que le type peut être utilisé de manière interchangeable dans le code qui utilise cette interface. Cette approche permet de créer du code générique qui peut être utilisé avec n'importe quel type qui implémente l'interface.*

Autre exemple :

Supposons que nous avons une interface Shape qui définit une méthode Area() et une méthode Perimeter() pour calculer l'aire et le périmètre d'une forme. Supossons également que nous avons deux types Rectangle et Circle qui implémentent l'interface Shape.

```go
package main

import (
 "fmt"
 "math"
)

type Shape interface {
    Area() float64
    Perimeter() float64
}

type Rectangle struct {
    width, height float64
}

func (r Rectangle) Area() float64 {
    return r.width * r.height
}

func (r Rectangle) Perimeter() float64 {
    return 2 * (r.width + r.height)
}

type Circle struct {
    radius float64
}

func (c Circle) Area() float64 {
    return math.Pi * c.radius * c.radius
}

func (c Circle) Perimeter() float64 {
    return 2 * math.Pi * c.radius
}

func main() {
    var s Shape
    s = Rectangle{width: 3, height: 4}
    fmt.Println("Rectangle Area:", s.Area())
    fmt.Println("Rectangle Perimeter:", s.Perimeter())

    s = Circle{radius: 5}
    fmt.Println("Circle Area:", s.Area())
    fmt.Println("Circle Perimeter:", s.Perimeter())
}
```

Dans cet exemple, nous utilisons une variable de type Shape qui peut stocker des instances des types Rectangle ou Circle. Nous pouvons  appeler les méthodes Area() et Perimeter() sur ces instances.

Aussi, Go ne supporte pas l'overloading. Je vous renvoie à la [faq](https://go.dev/doc/faq#overloading) pour savoir pourquoi.

C'est un peu perturbant, mais je suis sûr que l'on peut vite s'y faire.

Go se défend en avançant des avantages par rapport à C++. Par exemple, Go dispose d'un ramasse-miettes automatique (garbage collector) intégré, qui permet de gérer automatiquement la mémoire allouée aux objets, évitant ainsi les fuites de mémoire et les problèmes de corruption de la mémoire qui peuvent survenir en C++.

## Ressenti

J'ai trouvé que le langage Go était plutôt facile à prendre en main venant de python. De mon point de vue, il a une syntaxe simple et intuitive, et j'ai eu plus de faciliter avec Go qu'avec Rust par exemple. Je pense que pour mes projets futurs qui nécessiteront des performances élevées, je n'hésiterai pas à utiliser Go.
