---
layout: layout/mon.njk

title: "Rust en back-end avec Actix-web"
authors:
  - Assane Diouf

date: 2024-02-14
tags: 
  - "temps 3"

résumé: "Pendant ce MON nous découvrirons Rust pour le back-end avec Actix-Web."
---

## Introduction
Rust est un langage de programmation montant et apprécié par les développeurs pour son aspect "safe by design". Ses cas d'utilisation s'élargissent donc et il est désormais autant possible de développer des CLI, des applications embarquées ou des sites avec Rust.
Dans ce MON je vais m'intéresser à ce dernier cas. Toutefois, s'il est possible de traiter à la fois le front et le back avec Rust, je ne vais m'intéresser qu'au back ici. Pour celà, je vais partir à la découverte d'Actix-web, mais il existe aussi Rocket ou Axum pour faire la même chose avec Rust.
Je compte me baser sur la documentation officielle ainsi que sur le livre que m'a prêté M. Brucker "Zero to production in Rust".

## Ce que j'ai fait
Pendant ce MON, j'ai suivi, un peu comme un tuto, le livre prêté par M. Brucker sur Rust. Dans ce livre, on crée une newsletter en Rust de A à Z. Je me suis arrêté juste après le chapitre de la première mise en production. Ce livre est très bien, il suit un projet de A à Z et retrace des bonnes pratiques en expliquant à chaque étape pourquoi elles sont importantes.

## Découverte d'Actix-Web
Actix Web est un framework Rust pour faire du back. On peut lancer un serveur HTTP et définir des controlleurs et les routes auxquelles il répondent.
Voici un exemple tiré du site du framework :
```rust
#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .service(hello)
            .service(echo)
            .route("/hey", web::get().to(manual_hello))
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}

#[get("/")]
async fn hello() -> impl Responder {
    HttpResponse::Ok().body("Hello world!")
}

#[post("/echo")]
async fn echo(req_body: String) -> impl Responder {
    HttpResponse::Ok().body(req_body)
}

async fn manual_hello() -> impl Responder {
    HttpResponse::Ok().body("Hey there!")
}
```

## Gérer une base de données
En Rust, différentes options sont possibles pour travailler avec une base de données. On peut décider décider de travailler avec un ORM, ou sans, d'avoir un crate qui gère les requêtes en async ou non et ainsi de suite. Dans "Zero to production in Rust", on utilise sqlx qui permet de créer une base de données et d'effectuer les migrations.

## L'importance des tests
Dans tous le livre, l'auteur prête une attention particulière aux tests. Il réalise les tests d'intégration et les tests unitaires.
Au fur et à mesure, ces tests nous permettent d'avoir davantages confiance en le code écrit en s'assurant qu'il fonctionne bien.

## Les logs
Les logs permettent d'améliorer l'observabilité de notre api. L'objectif est d'avoir suffisemment d'informations sur notre applications lorsqu'elle s'exécute pour nous aider en cas de bugs ou de soucis. Dans le livre, on aborde la trace par exemple. L'idée est de pouvoir savoir à quelle requête correspondent chaque logs.

## Déploiement dans le cloud
Je n'ai pas eu le temps de mettre en pratique le chapitre sur les logs et celui sur le déploiement dans Digital Ocean.
Pour le déploiement, l'auteur a décidé de dockeriser l'api. Ensuite, il a pu envoyer l'image dans son serveur digital ocean, configuré au préalable.