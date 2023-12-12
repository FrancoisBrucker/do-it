---
layout: layout/mon.njk

title: "Le langage C#"
authors:
  - Assane Diouf

date: 2023-12-01
tags: 
  - "temps 2"

résumé: "Apprendre C# et en particulier le développement web avec C#"
---

## Pourquoi ?
C# est un langage connu avec une large communanuté de développeur. Avec C#, on a un large éventail de choix allant de l'application web au jeu vidéo en passant par l'application mobile.
Je vais particulièrement m'intéresser au développement web ici.

## Faire un pendu
En me basant sur les MON précédent sur le langage, et la documentation, je vais essayer de réaliser un petit jeu textuel pour assimiler les bases du langages.

Voici les taches que j'identifie pour réaliser ce jeu :
- [ ] Savoir lire dans un fichier le prochain mot
- [X] Savoir lire les entrées de l'utilisateur
- [X] Apprendre à organiser le code correctement

### Méthode
J'ai commencé par relire les MON des élèves ayant travaillé sur le langage avant moi (Vladimir et Savinien, voir dans la partie Source). Je me suis ensuite directement rendu sur le site officiel du langage (lien dans les Sources). J'ai ensuite suivi les étapes de découvertes du C# et fait un premier Hello World.

### Ce que j'ai fait
Pour mieux assimiler les principes du langages et pratiquer, j'ai décidé de réaliser un pendu en C#. Mon objectif final et d'avoir un petit site web avec un back en C# depuis lequel on peut jouer au pendu.

Pour commencer, j'ai développé un pendu auquel on peut jouer depuis la console. Pour le faire proprement, j'ai voulu bien séparer mon code. Pour se faire, j'ai fait les choix suivant :
- Avoir une classe Pendu, qui s'occupe simplement de gérer le jeu. Cette classe sera responsable du bon déroulement du jeu (lancement du jeu, vérification des propositions de l'utilisateur, cloture du jeu si victoire ou défaite)
- Avoir quelque chose pour sélectionner le mot à trouver. Je dis "quelque chose" car je voudrais me laisser la possibilité de changer la méthode de sélection de ce mot : le lire dans un fichier, le récupérer sur internet, etc... Afin d'avoir cette liberté d'implémentation, j'ai décidé de créer une interface nommée IWordProvider.
- Avoir un programme qui va utiliser la classe Pendu et communiquer avec le user (nombre d'essais restant, est-ce que le joueur a gagné, etc...).

J'ai donc séparé toutes les classes relatives au jeu (la class Pendu et l'interface dans leur namespace) pour obtenir l'architecture suivante :

```
projet
└── JeuPendu
    ├── WordProviders
    |   └── IWordProvider.cs
    |   └── OneWordProvider.cs
    └── Pendu.cs
 └── Program.cs
```

Le fichier Program.cs ressemble à ça à la fin du MON :

``` c#
using JeuPendu;
using JeuPendu.WordProviders;

Console.WriteLine("Jouons au pendu !");

Pendu Jeu = new Pendu(new OneWordProvider("Pendu"));

Jeu.Start();

Console.WriteLine(Jeu.KnownLetters);
Console.WriteLine("Entre une lettre ou un mot pour commencer.");
while(Jeu.IsGoingOn())
{
    string guess = Console.ReadLine() ?? "";
    if(Jeu.IsGoodGuess(guess))
    {
        Console.WriteLine("Bravo !");
        if(Jeu.Won) continue;
    }
    else
    {
        Console.WriteLine("Et non, essaie autre chose...");
        
        if(Jeu.Lost) continue;
        
        Console.WriteLine("Il te reste {0} essais", Jeu.NbAllowedMistakes - Jeu.Mistakes);
    }
    Console.WriteLine(Jeu.KnownLetters);
    Console.WriteLine("As-tu d'autres propositions ?");
}

if(Jeu.Won)
{
    Console.WriteLine("Bravo ! Le mot est bien {0}, tu as gagné !", Jeu.SecretWord);
}
else 
{
    Console.WriteLine("Le mot était {0}...", Jeu.SecretWord);
}
```

Dans ce code, on voit que la constructeur de Pendu prend en parametres un objet de type OneWordProvider. En réalité, la classe Pendu travaille avec un objet de type IWordProvider (mon interface), et OneWordProvider est une classe qui implémente l'interface IWordProvider donc je peux l'utiliser ici. La classe OneWordProvider, comme son nom l'indique, ne va fournir qu'un seul et même mot à chaque fois, en l'occurrence ici le mot "PENDU".

## Sources
- MON Vladimir : vue d'ensemble syntax + POO en C#
- MON Savinien : vue d'ensemble .NET et différentes possibilités + exemple API Web bien détaillé -> manque utilisation du back dans un site à mon goût mais très très clair
- https://learn.microsoft.com/fr-fr/dotnet/csharp/tour-of-csharp/ : vue plus détaillée du langages et accès à la documentation
- https://youtu.be/mw254_XAnGU?si=w7nkqOI2DmRyp9Ak : clarification utilisation des namespaces
- https://youtube.com/playlist?list=PLdo4fOcmZ0oW8nviYduHq7bmKode-p8Wy&si=fJe1Oh3-JxUdWSva : playlist ASP.NET débutant, pour découvrir le web avec C# (date de 4 ans)
