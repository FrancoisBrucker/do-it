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
