---
layout: layout/mon.njk

title: "Introduction au C#"
authors:
  - Vladimir Jeantroux

date: 2023-09-18

tags:
  - 'temps 1'
  - 'C'
---
## Résumé :

C# (prononcer C Sharp) est un langage orienté objet prédominant dans le domaine du développement de jeux vidéos, très utilisé dans les moteurs tels que Unity ou Godot. 

## Pré-requis : 

{%prerequis%}

Pré-requis :

- Avoir des bases en C et en programmation orientée objet 

 {%endprerequis%}

On va aussi avoir besoin d'un IDE comme Visual Studio Code, avec l'extension C# et le framework .NET. 

## C'est quoi .NET ? 

.NET (prononcer dot net) est un framework qui fournit un environnement de développement et d'exécution pour le développement d'applications web. Il contient des librairies et des outils de base qui permettent de faciliter la tâche du développeur. L'intérêt pour C# est d'avoir des outils pour coder son application sans avoir à tout réinventer, et simplement pouvoir construire par-dessus les templates qu'offre .NET. 

L'intérêt principal de .NET est qu'il est polyvalent, avec plusieurs composants avec des fonctions différentes, comme une bibliothèque de classes ou de frameworks pour différents types d'application. Un tableau complet recensant les composants et leurs fonctionnalités peuvent être trouvés dans le [MON de Savinien Laeuffer](https://francoisbrucker.github.io/do-it/promos/2022-2023/Laeuffer-Savinien/mon/csharp/), MON qui m'a permis de bien comprendre les différents aspects de ce langage. 

## Notions basiques 

### La programmation orientée objet (POO)

C# est un langage orienté objet, ce qui signifie qu'il repose sur la notion d'objets et de classes. Elle se fonde sur l'idée de modéliser des entités du monde réel ou des abstractions informatiques sous forme d'objets, qui possèdent des caractéristiques (appelées attributs) et des comportements (appelés méthodes). La POO permet de structurer et d'organiser le code de manière plus modulaire, ce qui facilite la compréhension, la maintenance et la réutilisation du code. C'est une notion centrale à C# qu'il faut bien comprendre avant de vouloir commencer à coder. 

#### 1. Classes

Une classe est un modèle pour créer des objets. Elle définit les attributs (variables) et les méthodes (fonctions) que les objets auront. Voici un exemple simple de définition de classe :

```csharp 
class Personne
{
    public string Nom;
    public int Age;

    public void Parler()
    {
        Console.WriteLine("Bonjour");
    }
}
```

On a déclaré une classe s'appelant "Personne". Un objet de la catégorie Personne aura deux attributs : son nom et son âge. Cet objet a aussi une fonction Parler qui renvoie simplement dans le terminal le texte "Bonjour". L'intérêt de cette méthode est que c'est ensuite facile de définir des Personnes, et on peut en avoir plusieurs représentants dans le programme. 

#### 2. Objets 

Les objets sont les instances de classe. Par exemple, si je veux créer une nouvelle personne : 

```csharp
Personne personne1 = new Personne();
personne1.Nom = "Alice";
personne1.Age = 25;
personne1.Parler();
```

Cela me permet de définir un représentant de la classe Personne avec tous les attributs et méthodes qui vont avec. Ceux qui ont bien suivi les cours d'informatique en 1A se rendront compte qu'on se rapproche beaucoup de la structure en Java, à quelques différences de syntaxe près. On a aussi les notions de constructeurs, qui permettent de faciliter la création d'objets.

```csharp 
class Personne
{
    public string Nom;
    public int Age;

    // Constructeur
    public Personne(string nom, int age)
    {
        Nom = nom;
        Age = age;
    }

    public void Parler()
    {
        Console.WriteLine("Bonjour");
    }
}
```

Cela peut paraître fastidieux à implémenter au début, mais la création d'objets par la suite devient beaucoup plus simple. 

```csharp
Personne personne1 = new Personne("Alice", 25);
```

En une seule ligne, on a créé un nouvel objet; les constructeurs permettent de créer plusieurs objets très rapidement et accélèrent le développement. 

## Exemples d'application 

Pour apprendre à me servir de C#, j'ai codé quelques exemples simples pour me familiariser avec les méthodes. On a d'abord le plus simple, l'incontournable : 

```csharp
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Hello, World!");
    }
}
```

J'ai aussi expérimenté avec des boucles et des conditions, en créant un programme qui liste les nombres premiers jusqu'à une certaine limite : 

```csharp
using System;

class Program
{
    static bool EstNombrePremier(int nombre)
    {
        if (nombre <= 1)
            return false;

        for (int i = 2; i * i <= nombre; i++)
        {
            if (nombre % i == 0)
                return false;
        }
        return true;
    }

    static void Main()
    {
        int limite = 50;

        for (int nombre = 2; nombre <= limite; nombre++)
        {
            if (EstNombrePremier(nombre))
            {
                Console.Write(nombre + " ");
            }
        }
    }
}
```
Pour exécuter ce fichier, on se place dans le dossier où se trouve le fichier avec le code (au format .cs) et on exécute dans le terminal : 

```powershell 
dotnet new console
```
Cela nous crée un environnement de projet. On peut maintenant compiler le code et le faire tourner et avoir la sortie : 

```powershell
dotnet build
dotnet run
```

Output : 
```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 
```

IMPORTANT ! Une bonne pratique est de nommer son fichier à partir du nom de la classe, cela peut éviter certaines erreurs. 

## Ouverture 

Je me suis ensuite intéressé à ce qui pouvait être étudié après avoir compris C#, et de sujets qui pourraient être intéressants après avoir compris C# : 
- Créer un  jeu vidéo de type Snake ou Morpion, pour tester ses connaissances et faire ses premiers pas dans le gamedev. Je voulais expérimenter avec ça à la fin du MON mais la tâche paraît compliquée et j'ai manqué de temps. 
- S'intéresser à l'utilisation des différents frameworks .NET : après avoir lu la 2e partie du MON de Savinien Laueffer, il serait intéressant de développer une application web. 
- Rust : un autre langage qui gagne de la popularité chez les développeurs. 

## Annexes

### Horodatage 

12/10 14h-16h Lecture des MON précédents, recherche des sources, installation des outils et début de l'apprentissage

14/10 15h-20h Apprentissage et entraînement sur W3Schools

15/10 13h-16h Mise en pratique et ouverture

### Bibliographie 

- MON de Savinien Laeuffer : https://francoisbrucker.github.io/do-it/promos/2022-2023/Laeuffer-Savinien/mon/csharp/ 

- Tutoriel C# de W3Schools : https://www.w3schools.com/cs/cs_getstarted.php 

- Documentation de Microsoft : https://learn.microsoft.com/fr-fr/dotnet/csharp/ 

- MON Rust de Assane Diouf : https://francoisbrucker.github.io/do-it/promos/2023-2024/Diouf-Asssane/mon/Rust/ 