---
layout: layout/mon.njk

title: "k9s speedrun any% unrestricted wg+ WR"
authors:
  - Loïck Goupil-Hallay

date: 2024-11-10

tags:
  - 'temps 2'
  - 'dev'
  - 'kubernetes'
  - 'k9s'
---

{%prerequis 'MON facile'%}
- [Kubernetes](https://kubernetes.io/)
- [Helm](https://helm.sh/)
{%endprerequis%}

{% lien %}
- [k9s](https://k9scli.io/)
{% endlien %}

## Introduction
Tout DevOps qui se respecte est amené à travailler avec un orchestrateur de conteneurs: **Kubernetes**. Il doit être capable de naviguer dans les ressources de son cluster afin de débugger, déployer, ou simplement observer ce qui s'y passe.
La CLI **kubectl** est très puissante, mais elle n'est pas forcément la plus ergonomique pour toutes les opérations du quotidien. On y passe beaucoup de temps dès qu'il faut faire quoi que ce soit. Afin de gagner en productivité, il existe un outil formidable d'interface graphique en CLi pour Kubernetes : **k9s**.

Dans ce MON, nous allons voir comment devenir un maître de **k9s**, afin de ne plus jamais perdre de temps pour nos opérations de tous les jours.
