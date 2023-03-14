---
layout: layout/post.njk

title: "Developpeur Blockchain"
authors:
  - Antoine Varnerot

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

## Framework

Extension vsc : <https://trufflesuite.com/guides/configuring-visual-studio-code/>
Truffle :
<https://trufflesuite.com/>
<https://github.com/trufflesuite/truffle>

Ganache

J'ai ensuite suivi le tuto quickstart qui permet d'explorer des petits projets déja existants avec des explications :

<https://trufflesuite.com/docs/truffle/quickstart/>

To deploy our smart contracts, we're going to need to connect to a blockchain. Truffle has a built-in personal blockchain that can be used for testing. This blockchain is local to your system and does not interact with the main Ethereum network.
