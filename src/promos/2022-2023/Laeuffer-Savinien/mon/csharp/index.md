---
layout: layout/mon.njk

title: "C# et .NET (Bases, création d'une API)"
authors:
  - Savinien Laeuffer
date: 2023-01-25

tags:
  - 'temps 2'
---

<!-- début résumé -->
C# et .NET (Bases, création d'une API)
<!-- fin résumé -->

## Description

Ayant trouvé mon stage de fin d'études chez Lucca, j'aurai besoin de connaître le langage C# et la plateforme .NET. J'ai donc cherché sur internet des cours afin d'apprendre ce langage et j'ai trouvé ce que je cherchais sur le site de Microsoft, qui propose de nombreux cours pour faire de différentes choses en C#.

Microsoft fournit beaucoup de cours, de videos et de documentations afin d'apprendre le C# et .NET, c'est donc de ça dont je me suis servi afin d'apprendre.

## Présentation de C# et .NET

##### C#

C# est un langage de programmation orienté objet créé par Microsoft en 2000. Il est principalement utilisé pour développer des applications Windows mais peut également être utilisé pour développer des applications web, des jeux vidéo, des applications mobiles et des applications de réalité virtuelle. C# est basé sur le langage C++ et est similaire à Java en termes de syntaxe. Il est utilisé dans le développement d'applications avec la plateforme .NET de Microsoft. Il est également utilisé pour développer des applications avec les frameworks ASP.NET et Xamarin pour développer des applications mobiles multiplateformes.

<div style="width:100%;">
  <figure style="text-align:center">
    <img style="height:200px; margin-left: auto; margin-right: auto" src="../csharp.png">
    <figcaption>C#</figcaption>
  </figure>
</div>


##### .NET

.NET est un framework de développement d'applications créé par Microsoft. Il permet aux développeurs de créer des applications pour Windows, web, mobile, jeux, IoT et d'autres types d'applications en utilisant des langages de programmation tels que C#, F#, et Visual Basic. Il fournit un ensemble de bibliothèques de classes, un runtime pour l'exécution des applications, ainsi qu'un environnement de développement intégré (IDE) pour faciliter le développement d'applications.

.NET est conçu pour être une plateforme de développement moderne et polyvalente, il offre des fonctionnalités telles que la gestion de la mémoire automatique, la sécurité, les services Web, et un support pour les applications multi-plateformes. .NET Core est une version open-source de .NET qui peut être utilisée sur différentes plateformes comme Windows, Linux et macOS.

<div style="width:100%;">
  <figure style="text-align:center">
    <img style="height:200px; margin-left: auto; margin-right: auto" src="../dotnet.png">
    <figcaption>C#</figcaption>
  </figure>
</div>

Voici un tableau résumant les différents frameworks .NET:

Modèle d’application | Infrastructure | Notes
--- | --- | ---
Web | ASP.NET Core | Infrastructure pour générer une logique côté serveur.
Web | ASP.NET Core MVC | Infrastructure pour générer une logique côté serveur pour les pages ou les API web.
Web | ASP.NET Core Razor Pages | Infrastructure pour créer une application HTML générée par le serveur.
Client web | Blazor | Blazor fait partie de ASP.NET Core. Ses deux modes autorisent soit la manipulation de Document Object Model (DOM) par le biais de sockets en tant que véhicule de communication pour l’exécution de code côté serveur, soit une implémentation de WebAssembly pour l’exécution du langage C# compilé sur un navigateur.
Bureau | WinForms | Infrastructure pour créer des applications de style Windows « battleship gray ».
Bureau | Windows Presentation Foundation (WPF) | Framework pour la génération d’applications de bureau dynamiques conformes à différents facteurs de forme. WPF permet aux éléments de formulaire d’effectuer des mouvements, des fondus, des glissements et d’autres effets à l’aide d’une bibliothèque enrichie d’animations.
Mobile | Xamarin | Permet aux développeurs .NET de créer des applications pour les appareils iOS et Android.


## Bases en C#

##### Prérequis

Pour coder en C# il faut quelques prérequis:

- On installe [Visual Studio Code](https://code.visualstudio.com/) ou un autre editeur de code.
- On installe aussi [l'extension C#](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csharp) pour VSCode.
- On installe localement le [SDK .NET](https://dotnet.microsoft.com/en-us/download) pour VSCode.

##### Hello World

Le tutoriel Hello World n'est pas très utile en soi, mais il faut bien commencer quelque part, j'ai donc passé moins de 2 minutes sur l'exécution de la commande:
```
Console.WriteLine("Hello World!");
```

Ce premier cours est disponible [ici](https://learn.microsoft.com/fr-fr/training/modules/csharp-write-first/2-exercise-hello-world?WT.mc_id=dotnet-35129-website&ns-enrollment-type=learningpath&ns-enrollment-id=learn.build-dotnet-applications-csharp)

## Créer une API web avec ASP.NET Core

Supposons que nous souhaitons créer une gestion de profils d'utilisateurs pour une application web quelconque. Un utilisateur doit comporter un pseudo, un numéro unique en guise d'id, un âge, et un booléen indiquant si le compte a été activé ou non.
Le service créer permettra d'ajouter, d'afficher, de modifier et de supprimer des utilisateurs. On cherche donc à créer des requêtes CRUD (Create, Read, Update, Delete) en C# pour des objets User.

On apprendra ici à créer une application d'API web grâce à ASP.NET Core. On executera cette API et on pourra la tester à partir du CLI en ajoutant, supprimant, updatant, lisant des utilisateurs.

Les méthodes HTTP que nous allons créer seront les méthodes
- ```GET```
- ```POST```
- ```PUT```
- ```DELETE```

### Création du projet

Tout d'abord, afin d'utiliser le module nécessaire à la création de l'API, on vérifie que .NET 6.0 est correctement installé en entrant la commande suivante:
```
dotnet --list-sdks
```

Si la sortie ressemble à ceci, alors c'est bon.
```
3.1.100 [C:\program files\dotnet\sdk]
5.0.100 [C:\program files\dotnet\sdk]
6.0.100 [C:\program files\dotnet\sdk]
```

Dans Visual Studio Code, on commence par ouvrir un dossier au nom de notre projet, ici je l'appelerai "APIUser"
Une fois le dossier ouvert, on créer notre projet d'API web de base en entrant dans le terminal
```
dotnet new webapi -f net6.0
```

On aura maintenant accès à ces dossiers et fichiers dans notre répertoire:
```bash
-| Controllers
-| obj
-| Properties
-| appsettings.Development.json
-| appsettings.json
-| APIWeb.csproj
-| Program.cs
-| WeatherForecast.cs
```

Ces fichiers correspondent à une API météo. On peut se baser sur le contenu de ces fichiers pour créer notre API, mais dans notre cas nous crérons un autre contrôleur.

### La classe User

Dans un dossier Models que l'on crée avec la commande ```mkdir Models``` on créera notre fichier ```User.cs``` qui comportera notre classe utilisateur.

Dans ce fichier on écrit le code suivant afin de définir la classe User:
```csharp
namespace APIUser.Models;

public class User
{
    public int Id { get; set; }
    public int? Age { get; set; }
    public string? Name { get; set; }
    public bool IsActivated { get; set; }
}
```

### Le service de données

Pareil que précédemment, on se sert de la commande ```mkdir Services``` pour créer un dossier Services dans lequel nous créerons le fichier ```UserService.cs```.
Ce fichier va nous permettre de créer des méthodes de stockage d'utilisateur en local.

On entre le code suivant:
```csharp
using APIUser.Models;

namespace APIUser.Services;

public static class UserService
{
    static List<User> Users { get; }
    static int nextId = 2;
    static UserService()
    {
        Users = new List<User>
        {
            new User { Id = 1, Name = "admin", Age = "99", IsActivated = true },
        };
    }

    public static List<User> GetAll() => Users;

    public static User? Get(int id) => Users.FirstOrDefault(u => u.Id == id);

    public static void Add(User user)
    {
        user.Id = nextId++;
        Users.Add(user);
    }

    public static void Delete(int id)
    {
        var user = Get(id);
        if(user is null)
            return;

        Users.Remove(user);
    }

    public static void Update(User user)
    {
        var index = Users.FindIndex(u => u.Id == user.Id);
        if(index == -1)
            return;

        Users[index] = user;
    }
}
```

Les méthodes Get, GetAll, Add, Delete et Update sont maintenant créées afin de gérer la liste d'utilisateur stockée localement dans la variable de liste Users. Le code est assez facile à comprendre, il faut simplement réapprendre la syntaxe de ce langage.

### Ajout d'un contrôleur

Dans le dossier ```Controllers``` déjà existant, on crée notre fichier ```UserController```, et dans ce fichier on ajoute le code suivant:

```csharp
using APIUser.Models;
using APIUser.Services;
using Microsoft.AspNetCore.Mvc;

namespace APIUser.Controllers;

[ApiController]
[Route("[controller]")]
public class UserController : ControllerBase
{
    public UserController()
    {
    }

    // C'est ici que nous rédigerons nos fonction GET, GETALL, POST, PUT, et DELETE
}
```

Notre classe UserController fraichement créée se base sur la classe ControllerBase fournit par ASP.NET Core pour l'utilisation des requêtes HTTP.

Dans la suite, il faut savoir que les attributs entre crochets vont définir quel type de méthode on aura affaire. Le type ActionResult est la classe de base pour les résultats d'action d'ASP.NET Core

##### Méthode GETALL

Pour afficher tous les utilisateurs on se sert donc de l'attribut ```[HttpGet]```:

```csharp
[HttpGet]
public ActionResult<List<User>> GetAll() =>
    UserService.GetAll();
```

##### Méthode GET(id)

Pour afficher un seul utilisateur on se sert de l'attribut ```[HttpGet]``` en ajoutant le fait que l'on veuille le chercher par ID. Si l'utilisateur n'existe pas, on renvoie le résultat NotFound() qui renvoie un code 404:

```csharp
[HttpGet("{id}")]
public ActionResult<User> Get(int id)
{
    var user = UserService.Get(id);

    if(user == null)
        return NotFound();

    return user;
}
```


##### Méthode POST(user)

Pour ajouter un nouvel utilisateur, on se sert de l'attribut ```[HttpPost]```. Ici on remplace ActionResult par IActionResult qui est un type permettant de savoir si la demande a bien réussi et fournit l'ID de l'utilisateur fraichement créé.

```csharp
[HttpPost]
public IActionResult Create(User user)
{            
    UserService.Add(user);
    return CreatedAtAction(nameof(Get), new { id = user.Id }, user);
}
```

##### Méthode PUT(user)

Pour update un utilisateur, , on se sert de l'attribut ```[HttpPut]```. On vérifie bien sûr que l'élément existe avant de l'updater. Elle prend deux paramètres qui sont l'id et l'objet User que l'on veut mettre à jour.

```csharp
[HttpPut("{id}")]
public IActionResult Update(int id, User user)
{
    if (id != user.Id)
        return BadRequest();
           
    var existingUser = UserService.Get(id);
    if(existingUser is null)
        return NotFound();
   
    UserService.Update(user);           
   
    return NoContent();
}
```

##### Méthode DELETE(id)

Pour supprimer un utilisateur on utilise ```[HttpDelete("{id}")]```. On cherche si l'utilisateur existe bien avant de le supprimer à l'aide de la méthode GET par id, sinon on renvoie une erreur 404 NotFound().

```csharp
[HttpDelete("{id}")]
public IActionResult Delete(int id)
{
    var user = UserService.Get(id);
   
    if (user is null)
        return NotFound();
       
    UserService.Delete(id);
   
    return NoContent();
}
```

### Execution de l'API

Pour générer l'API web, on peut exécuter la commande suivante:
```
dotnet run
```

Dans un autre terminal (on peut ouvrir un 2ème terminal dans Visual Studio Code), on accède à l'API Web grâce à la commande:
```
httprepl https://localhost:{PORT}
```

Il faut bien sûr renseigner le port adéquat qui est fournit dans le CLI après avoir lancé la première commande.

On accède au point de terminaison ```User``` grâce à la commande:
```
cd User
```

Puis pour afficher les actions que l'on peut faire sur l'API User, on exécute la commande suivante:
```
ls
```

Si tout est correct, on devrait voir afficher ceci:
```
    https://localhost:{PORT}/User> ls
    .      [GET|POST]
    ..     []
    {id}   [GET|PUT|DELETE]
```

Ce qui indique que les méthodes ont bien été compilées.

### Exemple de requêtes

On peut exécuter une requête POST pour ajouter un nouvel User dans HttpRepl en utilisant la commande suivante :


```
post -c "{"age":90, "name":"Savinien",, "isActivated":false}"
```

On peut le mettre à jour grâce à la commande (il faut préciser l'id):

```
put 2 -c "{"age":90, "name":"Savinien",, "isActivated":true}"
```

Si la sortie est la suivante alors ça a fonctionné:
```
HTTP/1.1 204 No Content
Date: Fri, 20 Jan 2022 22:14:43 GMT
Server: Kestrel
```

Pour vérifier que l'utilisateur a été mis à jour on essaye de l'afficher:
```
get 2
```

Notre utilisateur devrait donc s'afficher:
```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Date: Fri, 20 Jan 2022 22:15:55 GMT
Server: Kestrel
Transfer-Encoding: chunked

{
    "id": 2,
    "age": 90, 
    "name": "Savinien", 
    "isActivated": true
}
```

Pour le supprimer, il suffit d'exécuter:
```
delete 2
```

Cette commande renvoie un résultat 204 No Content pour une réussite, et affiche:

```
HTTP/1.1 204 No Content
Date: Fri, 20 Jan 2022 22:18:20 GMT
Server: Kestrel
```

En exécutant la commande suivante, on affiche tous les utilisateurs et on se rend compte que l'utilisateur précédemment créé est bien supprimé et ne figure plus dans la liste.
```
get
```

## Ressources

La plupart des ressources utilises pour apprendre le C# se trouvent sur le site web de Microsoft et sont très bien faites.

- [Microsoft Learn](https://learn.microsoft.com/fr-fr/)

- [Video .NET](https://dotnet.microsoft.com/en-us/learn/videos)

- [Écrire vos premières lignes de code en C#](https://learn.microsoft.com/fr-fr/training/modules/csharp-write-first/)

- [Créer une API web avec des contrôleurs ASP.NET Core](https://learn.microsoft.com/fr-fr/training/modules/build-web-api-aspnet-core/)
