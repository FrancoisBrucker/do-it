---
layout: layout/mon.njk

title: "MON 1.1 - Introduction au Golang"
authors:
  - Emma Gonin

date: 2024-09-05

tags: 
  - "temps 1"
  - "golang"

résumé: "Ce MON est une introduction au langage Golang."
---

{% prerequis %}

Pas de prérequis spécifique, juste de la curiosité pour le langage. 

{% endprerequis %}

## Introduction
Le Go, ou Golang, est un langage de programmation open source créé par Google en 2009. Il se revendique simple d'utilisation avec une rapidité et efficacité d'exécution. Il est multi-platformes et a permis le développement d'outils pour le Cloud (Docker, Kubernetes), d'outils CLI (Terraform) ou pour le développement de jeux vidéos (Ebitengine).

## Table des matières

## Installation de Go sur son ordinateur
Pour installer Go sur son ordinateur, on télécharge un fichier d'installement sur le lien https://go.dev/dl/ selon son système d'exploitation.
Pour faire notre première utilisation de Go, on va faire un classique affichage de "Hello world !" dans notre terminal !
On crée un fichier main.go dans lequel on écrit :
```
package main

import (
  "fmt"
)

func main() {
  fmt.Println("Hello world ! ")
}
```
On exécute le fichier dans le Powershell (à l'emplacement du fichier) en tapant la commande
```
go run main.go
```

   
## Faire sa propre application CLI (Command Line Interface)
J'ai voulu me familiariser avec le langage en suivant un tutoriel pour faire ma propre application à interface à ligne de commandes. 


## Ressources

- Pour toutes les questions générales ou précises relevant du langage Go, je conseille d'aller lire la documentation officielle qui est assez fournie : https://go.dev/docs
- Le site officiel de Golang propose un tutoriel pour se familiariser au langage, je me suis servie de ce tutoriel pour faire ce MON et vous résumer les principaux axes de ce langage : https://go.dev/tour/welcome/1
- J'ai suivi un tutoriel vidéo qui retrace en 1h les bases du Go, je conseille cette vidéo : https://www.youtube.com/watch?v=8uiZC0l4Ajw&ab_channel=AlexMux
- 


