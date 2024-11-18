---
layout: layout/mon.njk

title: "Developpeur Blockchain"
authors:
  - Antoine Varnerot
tags:
  - 'temps 3'

date: 2023-03-23
---

## Description du MON

Pendant les 10h consacrées à ce MON, je veux :

- découvrir les metiers du Web 3
- apprendre les bases d'un outil/framework du web 3 (Solidity)

Prérequis:

- Bonnes bases de Javascript/Typescript
- Fonctionnement basique de la blockchain et des cryptomonnaies

## Informations

Etant donné que je ne connais pas les métiers qui mêlent developpement web et Web 3 / blockchain, j'ai cherché naïvement "developpeur blockchain" sur Google et j'ai remarqué qu'il existait beaucoup de métiers derrière.
Les deux principaux sont :

1. Developpeur blockchain core (~backend)
2. Les développeurs d’applications décentralisées (developpeur de Dapps) (~frontend)

L'article qui m'a beaucoup aidé pour comprendre ces métiers est :
<https://www.commentcoder.com/developpeur-blockchain/>

Après avoir vu cela, j'ai compris que l'activité sur laquelle je voulais avoir plus d'informations était developpeur blockchain core

Les languages utilisés dans ces métiers sont :

- Solidity
- JavaScript
- Rust
- Pyhton (Django)
- C++

## Solidity

Solidity est le langage d’Ethereum pour coder des Smart Contracts. Il est très proche du JavaScript.
Un Smart contract écrit en Solidity est du code qui tourne sur la blockchain Ethereum.
Solidity permet, par exemple, de créer des NFTs, des jeux vidéo, des plateformes de DeFi et toutes autres formes de projets web3.

J'ai lu les 20/30 premières pages de la documentation en francais de solidity (sur +200 pages). Cela m'a permis d'apprendre les concepts propres à Ethereum (EVM plus particulièrement) comme le gas, les messages calls, la gestion des données (Storage, Memory et Stack) ... Ainsi que quelques exemples simples de code Solidity. Lien vers la doc :
<https://solidity-fr.readthedocs.io/_/downloads/fr/v0.5.0/pdf/>
Ce pdf est assez compliqué à comprendre au bout d'un moment et me semblait pas en adéquation avec ce que je voulais faire c'est pour cela que je n'ai pas continué la lecture.

J'ai aussi beaucoup utilisé le site ethereum directement :

- <https://ethereum.org/fr/developers/docs/smart-contracts/>
- <https://ethereum.org/fr/developers/docs/programming-languages/javascript/>

Ce dernier site est très clair et contient beaucoup beaucoup de documentation accessible à tous.

## Framework Truffle

Extension vsc : <https://trufflesuite.com/guides/configuring-visual-studio-code/>
Truffle :
<https://trufflesuite.com/>
<https://github.com/trufflesuite/truffle>

J'ai ensuite suivi le tuto quickstart qui permet d'explorer des petits projets déja existants avec des explications :

<https://trufflesuite.com/docs/truffle/quickstart/>

Pour déployer nos smarts contracts, on doit se connecter à une blockchain. On pourrait se connecter à celle d'Ethereum mais on a pas envie dépenser de l'argent pour le dev. Heuresement, Truffle à sa propre blockchain local. On s'y connecte avec la commande 

```bash
truffle develop
```

qui renvoit ici :
<figure>
  <img src="../assets/truffleDevelop.png">
</figure>

On voit que ca a créé 10 comptes avec leurs clés respectives.

Pour migrer les contrats sur la blockchain on utilise ```migrate``` qui renvoie :

```bash
Starting migrations...
======================
> Network name:    'develop'
> Network id:      5777
> Block gas limit: 6721975 (0x6691b7)


1_deploy_contracts.js
=====================


   Deploying 'ConvertLib'
   ----------------------

   > transaction hash:    0xb6b11e717f56b967a0b7657dbebc95d746f871415b0f6e2e27ebae3f09b65b25

   > Blocks: 0            Seconds: 0
   > contract address:    0xcba5Fba74cf4A83f99fd359829Bba560c3339F86
   > block number:        1
   > block timestamp:     1678288800
   > account:             0x6bcb62979E599B1cE4Ef3f3DF3575B644Cb9A613
   > balance:             99.999468208
   > gas used:            157568 (0x26780)
   > gas price:           3.375 gwei
   > value sent:          0 ETH
   > total cost:          0.000531792 ETH



   Linking
   -------
   * Contract: MetaCoin <--> Library: ConvertLib (at address: 0xcba5Fba74cf4A83f99fd359829Bba560c3339F86)


   Deploying 'MetaCoin'
   --------------------

   > transaction hash:    0x675fa58ed29a7dc17fea9e9dcca19597a6a3ed24ebcc409648a44deae71e4a8d

   > Blocks: 0            Seconds: 0
   > contract address:    0xb4dEbAE5393b921A3f556388538D2c9d142cf6D1
   > block number:        2
   > block timestamp:     1678288801
   > account:             0x6bcb62979E599B1cE4Ef3f3DF3575B644Cb9A613
   > balance:             99.998105632065943366
   > gas used:            416594 (0x65b52)
   > gas price:           3.270752661 gwei
   > value sent:          0 ETH
   > total cost:          0.001362575934056634 ETH


   > Saving artifacts
   -------------------------------------
   > Total cost:     0.001894367934056634 ETH

Summary
=======
> Total deployments:   2
> Final cost:          0.001894367934056634 ETH
```

On voit qu'il a bien déployer les deux contrats et on voit, comme sur une facture, le detail de chaque transaction. On reconnait les concepts appris sur le site ethereum.org comme le gas, les différentes unités de monnaie (Wei, ETH).
Le coût total du contrat correspond environ à 3€ en mars 2023. Ce n'est pas énorme mais le code est très basique. Si on était ammené à utiliser beaucoup de la mémoire sur la blockchain, ce coût grimperait vite.

Pour la suite du tuto, il est conseillé d'utiliser Ganache :
<https://trufflesuite.com/ganache/>

J'ai utilisé cette techno comme sur le tuto mais je sais pas si tout a marché comme prévu. En effet , j'ai réussi à effectuer des transactions entre comptes (visible dans l'onglet "Transactions") mais le solde des comptes n'a pas changé.
