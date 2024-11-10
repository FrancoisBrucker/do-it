---
layout: layout/pok.njk

title: "VSCode Extension: Achievements"
authors:
  - Loïck Goupil-Hallay

date: 2024-11-10

tags:
  - "temps 2"
  - "dev"
  - "vscode"

résumé: Développement d'une extension permettant de débloquer des succès en fonction de l'utilisation de VSCode.
---

{% prerequis 'POK moyen'%}
- [VSCode](https://code.visualstudio.com/)
{% endprerequis %}

{% lien %}
- [Achievements sur GitHub](https://github.com/boxboxjason/achievements)
- [API VSCode](https://code.visualstudio.com/api)
- [Développer son extension VSCode](https://code.visualstudio.com/api/get-started/your-first-extension)
{% endlien %}

## Introduction
Après avoir passé des années à coder, on se rend compte qu'on en a passé des heures sur nos lignes de code. Tout collectionneur de succès qui se respecte aimerait pouvoir montrer à ses amis qu'il a passé des heures à coder. Et puis qui n'a jamais rêver de terminer VSCode ? C'est pourquoi j'ai décidé de développer une extension pour VSCode permettant de débloquer des achievements en fonction de l'utilisation de l'éditeur.

Il existe déjà deux extensions de ce type sur le marché, mais elles ne sont pas complètes du tout et ne sont plus maintenues. J'ai donc décidé de développer la mienne, qui sera plus complète et plus à jour.
