---
layout: layout/mon.njk

title: "Introduction à la blockchain"
authors:
  - OLIANA Guillaume

date: 1971-01-01
tags: 
  - "temps 2"

résumé: "Un MON autour de la blockchain."
---

{% prerequis %}

LAucun prérequis, ce MON est un travail de recherche qui a pour but de m'éduquer sur ces technologies, aussi bien que ceux qui prendront le temps de le lire.

{% endprerequis %}
{% lien %}

[Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf)

[Une brève explication de ce qu'est la blockchain](https://kriptomat.io/fr/blockchain/lhistoire-du-blockchain/)

[Comprendre la blockchain en 7min](https://www.youtube.com/watch?v=6uYRN6b5EMU&t=13s)



{% endlien %}


## Contenu

### **1. Introduction à la blockchain**
Définition
La blockchain est une technologie de stockage et de transmission de données fonctionnant comme un registre distribué et immuable. Chaque transaction ou information est enregistrée dans un réseau décentralisé de manière sécurisée et transparente, accessible à tous les participants du réseau. Une fois les données validées, elles deviennent impossibles à modifier ou à supprimer, garantissant ainsi l’intégrité des informations.

Historique : Origine et évolution
Les prémices de la blockchain
Les bases théoriques de la blockchain remontent aux années 1990, avec des travaux sur l’horodatage sécurisé des données numériques. Ces concepts techniques se sont concrétisés en 2008 avec l’invention de Bitcoin, la première application fonctionnelle de cette technologie.

### Création de Bitcoin (2008)

Satoshi Nakamoto, un pseudonyme collectif ou individuel, publie le livre blanc intitulé "Bitcoin: A Peer-to-Peer Electronic Cash System".
La blockchain est utilisée pour résoudre le problème du "double spending" dans les monnaies numériques, garantissant qu’une unité de monnaie ne puisse pas être dépensée deux fois.
Le premier bloc, connu sous le nom de Genesis Block, est miné le 3 janvier 2009, marquant le début de l’ère blockchain.
Au-delà de Bitcoin : Évolution vers d'autres plateformes

### Ethereum (2015) : Introduit les smart contracts, des programmes exécutés automatiquement sur la blockchain, ouvrant la voie à des applications complexes au-delà des paiements.
Hyperledger Fabric (2016) : Développé pour des blockchains permissionnées adaptées aux entreprises, comme dans la gestion de la chaîne d'approvisionnement.
Polkadot, Solana et d’autres : Axées sur des solutions innovantes comme l’interopérabilité et la haute performance.

Cas d’utilisation de la blockchain

Bien que la blockchain soit née pour soutenir les cryptomonnaies, son champ d'application s'est étendu à de nombreux secteurs.

- Bitcoin reste la cryptomonnaie emblématique, mais des milliers d'autres, comme Ethereum et Binance Coin, (BNB) exploitent la blockchain pour des paiements décentralisés ou des services spécifiques.

- Les entreprises utilisent par exemple la blockchain pour garantir la traçabilité des produits tout au long de leur chaîne logistique, réduisant ainsi les fraudes et augmentant la transparence.

- Les contrats intelligents automatisent des processus complexes, comme la gestion des droits d'auteur ou l’exécution de contrats financiers.


- Les dossiers médicaux sont stockés de manière sécurisée sur une blockchain, permettant un accès contrôlé par les patients et les professionnels de santé.
Identité numérique

La blockchain est une technologie qui va bien au-delà de la simple spéculation financière associée aux cryptomonnaies. Avec son caractère décentralisé, sécurisé et transparent, elle transforme les industries et les interactions numériques.


### **2. Principes de fonctionnement de la blockchain**

La blockchain est souvent comparée à un registre public numérique, mais elle est bien plus complexe. Pour bien comprendre, je vais essayer d'expliquer son fonctionnement en illustrant un exemple concret : une transaction où l’utilisateur **A** envoie 1 Bitcoin à l’utilisateur **B**.

---

#### **2.1 Structure d’une blockchain**

Une blockchain est une chaîne de blocs (logique), chaque bloc contenant un ensemble de transactions et des métadonnées qui garantissent la continuité et l’intégrité de la chaîne.

- **Bloc dans la blockchain** :  
  Chaque bloc contient les éléments suivants :
  - **Transactions** : Liste des transferts effectués, signés par les utilisateurs.
  - **Hash du bloc précédent** : Empreinte unique du bloc précédent, permettant de lier les blocs entre eux.
  - **Timestamp** : Date et heure à laquelle le bloc a été validé.
  - **Nonce** (Proof of Work uniquement) : Une valeur trouvée par les mineurs pour résoudre le puzzle cryptographique.

- **Fonctionnement global** :  
  Les blocs sont enchaînés grâce aux hashes, formant une structure où toute modification dans un bloc invalide la chaîne entière à partir de ce point.

---

#### **2.2 Exemple concret : Transaction Bitcoin**

Voici les étapes détaillées lorsque **A** envoie 1 Bitcoin à **B** :

1. **Création de la transaction** :
   - **A** utilise son portefeuille Bitcoin pour créer une transaction.
   - La transaction spécifie :
     - L'adresse Bitcoin de **B** (clé publique de B, dérivée de sa clé privée).
     - Le montant transféré (1 BTC, soit 0.40€ en 2010 et 90 000€ en 2024).
     - Une signature numérique générée avec la clé privée de **A**, prouvant que **A** autorise la transaction.

2. **Diffusion de la transaction** :
   - La transaction est propagée sur le réseau peer-to-peer (P2P).
   - Les nœuds reçoivent la transaction et vérifient :
     - La validité de la signature numérique.
     - Que **A** dispose bien d’au moins 1 BTC non dépensé.

3. **Regroupement des transactions dans un bloc** :
   - Les mineurs collectent des transactions valides et les regroupent dans un bloc candidat.
   - Le bloc contient :
     - Un hash du bloc précédent.
     - Une liste de transactions, y compris celle de **A** vers **B**.
     - Un nonce, initialement non défini.

4. **Validation du bloc par Proof of Work (PoW)** :
   - Les mineurs exécutent un processus de *brute force* pour trouver un nonce $n$ tel que :  
     \[
     $H(\text{header} + n) < \text{cible}$
     \]
     où $\text{header}$ inclut les données du bloc.  
   - Une fois la condition satisfaite, le mineur diffuse le bloc validé au réseau.

5. **Ajout du bloc à la blockchain** :
   - Les autres nœuds vérifient le bloc proposé (validité des transactions, résolution correcte du PoW, etc.).
   - Si le bloc est validé, il est ajouté à la chaîne, devenant le nouveau bloc "le plus récent".
   - La transaction de **A** à **B** est maintenant confirmée et devient immuable.

6. **Confirmation de la transaction** :
   - Une transaction est considérée comme sécurisée après plusieurs confirmations (généralement 6 blocs).
   - **B** peut maintenant dépenser son Bitcoin.

---

### **2.3 Mécanismes de consensus**

Dans un réseau décentralisé, le consensus est essentiel pour garantir la cohérence des données partagées entre tous les nœuds. Ce processus repose sur des algorithmes mathématiques permettant de valider les blocs tout en sécurisant le réseau contre les attaques malveillantes.

- **Proof of Work (PoW)**  
  - **Principe** : Comme expliqué plus haut, chaque mineur doit résoudre un puzzle cryptographique complexe, consistant à trouver un nonce $n$ tel que :  
    \[
    $H(\text{header} + n) < \text{cible}$
    \]
    où $H$ est une fonction de hashage, $\text{header}$ contient les données du bloc, et $\text{cible}$ est une valeur ajustée par le réseau pour maintenir un temps de bloc constant (par exemple, 10 minutes pour Bitcoin).  

  - **Sécurité** :  
    - La complexité du puzzle rend la falsification des blocs coûteuse en termes de ressources.  
    - Une attaque nécessiterait une puissance de calcul supérieure à 50 % de celle du réseau total (fameuse attaque des 51 %).  

  - **Avantages** :  
    - Garantit une sécurité robuste grâce au coût élevé du minage.  
  - **Inconvénients** :  
    - Inefficience énergétique : La résolution de $H(\text{header} + n)$ est un processus de recherche exhaustive (brute-force).  
    - Centralisation potentielle dans des pools de minage.  

- **Proof of Stake (PoS)**  
  - **Principe** : Les validateurs sont choisis pour proposer ou valider des blocs en fonction de la quantité de tokens qu’ils possèdent et ont "stakée".  
  - **Sélection du validateur** :  
    - Le choix est souvent basé sur une fonction pseudo-aléatoire pondérée par :  
      - Le montant staké $S$.  
      - L’ancienneté du staking $T$.  
    - Exemple :  
      \[
      $P_i = \frac{S_i \cdot T_i}{\sum_{j} S_j \cdot T_j}$
      \]
      où $P_i$ est la probabilité qu’un validateur $i$ soit choisi.

  - **Sécurité** :  
    - Une attaque nécessiterait de posséder une part significative des tokens, ce qui rend l’attaque économiquement risquée.  
  - **Avantages** :  
    - Faible consommation d’énergie.  
    - Validation rapide des blocs.  
  - **Inconvénients** :  
    - Concentration des pouvoirs entre les riches détenteurs de tokens.  

- **Autres variantes**  
  - **Delegated Proof of Stake (DPoS)** :  
    - Principe : Les participants élisent un nombre fixe de délégués qui se chargent de valider les blocs.  
    - Avantages : Hautes performances grâce à un consensus rapide.  
    - Inconvénient : Centralisation partielle autour des délégués.  

  - **Proof of Authority (PoA)** :  
    - Utilisé dans des blockchains permissionnées, où seuls des nœuds validateurs approuvés peuvent ajouter des blocs.  
    - Sécurité reposant sur la réputation des validateurs.

---

#### **2.4 Immutabilité et sécurité**

La sécurité de la blockchain repose sur des propriétés mathématiques et cryptographiques.

- **L’immutabilité**  
  - Chaque bloc dépend du hash du bloc précédent. Si un attaquant modifie les données d’un bloc $B_k$, le hash de $B_k$ change, rendant $B_{k+1}$ invalide.  
  - Recréer la chaîne entière à partir de $B_k$ nécessiterait de recalculer le PoW (ou satisfaire d’autres conditions de consensus) pour chaque bloc, ce qui est pratiquement impossible dans des blockchains bien réparties.  

- **Cryptographie**  
  - **Fonctions de hashage** :  
    - Propriétés utilisées :  
      - **Résistance aux collisions** : Il est presque impossible de trouver deux entrées $x$ et $y$ telles que $H(x) = H(y)$.  
      - **Résistance à la préimage** : Pour un $h$, il est difficile de trouver un $x$ tel que $H(x) = h$.  
    - Exemple : Bitcoin utilise **SHA-256**, qui produit un hash de 256 bits.  

  - **Signatures numériques** :  
    - Utilisation de la cryptographie asymétrique. Chaque utilisateur possède :  
      - Une **clé privée** $d$ pour signer.  
      - Une **clé publique** $Q$ dérivée de $d$ :  
        \[
        $Q = d \cdot G$
        \]
        où $G$ est un point générateur sur une courbe elliptique.  
      - Une transaction est signée avec $d$, et tout participant peut vérifier la signature avec $Q$.  

  - **Prévention de la double dépense** :  
    - Chaque transaction inclut une référence à une transaction précédente, empêchant qu’un même token soit utilisé deux fois.  

- **Décentralisation**  
  - Chaque nœud du réseau stocke une copie complète du registre, garantissant que la perte ou la compromission de certains nœuds ne compromette pas l’intégrité de la blockchain.  
  - Les décisions sont prises par consensus, éliminant le besoin d’un tiers centralisé.

---

### 3. Composants techniques classiques

Les composants techniques qui font fonctionner une blockchain sont variés, allant des protocoles réseau à la cryptographie utilisée pour sécuriser les transactions. Comprendre ces éléments est essentiel pour saisir comment la blockchain garantit la sécurité, la décentralisation et l'intégrité des données.

#### Langages de programmation

Les applications blockchain reposent sur des langages de programmation spécifiques, chacun ayant un rôle distinct en fonction de la plateforme. Par exemple, **Ethereum** utilise principalement **Solidity**, un langage conçu pour écrire des contrats intelligents (smart contracts) qui s'exécutent sur sa blockchain. Solidity permet aux développeurs de créer des programmes automatisés qui interagissent avec des données et des événements sur la blockchain, comme l’envoi de fonds ou la gestion d’un actif numérique.

Sur des blockchains comme **Solana**, le langage privilégié est **Rust**. Rust est choisi pour sa performance, notamment dans la gestion de l'exécution rapide des transactions, ce qui est crucial dans un environnement à fort volume d’opérations comme celui de Solana.


#### Protocoles Réseau

Le réseau blockchain est généralement basé sur un modèle **peer-to-peer (P2P)**. Cela signifie que chaque participant, ou **nœud**, du réseau possède une copie complète (ou partielle) de la blockchain et interagit avec d'autres nœuds sans qu'il y ait de serveur central. Cette décentralisation est la clé de la résistance aux censures et aux attaques.  

Lorsqu'une transaction est effectuée, elle est envoyée à tous les nœuds du réseau, et chaque nœud valide cette transaction selon les règles du consensus (comme le Proof of Work ou Proof of Stake). L'absence de serveur central élimine un point de défaillance unique, ce qui rend la blockchain extrêmement robuste contre les attaques.

Le modèle P2P permet aussi un traitement parallèle et une synchronisation rapide des données à travers le réseau, augmentant ainsi la résilience du système et la rapidité des transactions, surtout sur les blockchains publiques comme Bitcoin ou Ethereum.

#### Infrastructure des Nœuds

Les nœuds sont les composants fondamentaux de la blockchain. On distingue principalement deux types de nœuds : les **full nodes** et les **light nodes**. 

Les **full nodes** conservent une copie complète de la blockchain, validant chaque transaction et chaque bloc selon les règles du consensus. Ils sont essentiels à la sécurité et à la décentralisation du réseau. Cependant, ils nécessitent des ressources importantes en termes de stockage et de puissance de calcul.

Les **light nodes**, quant à eux, ne conservent qu’une partie de la blockchain, généralement l’en-tête des blocs, et se fient aux full nodes pour obtenir les informations nécessaires à la validation des transactions. Ils sont plus légers et nécessitent moins de ressources, mais sont moins impliqués dans le processus de validation de la blockchain.


La décentralisation du réseau, associée à ces mécanismes de consensus, empêche toute manipulation ou falsification des données, ce qui est une caractéristique clé des blockchains publiques, comme Bitcoin.

### 4. Cas pratiques et implémentations

La blockchain, en plus de ses fondements théoriques, se déploie déjà dans des applications concrètes à travers divers secteurs. De la gestion des chaînes d'approvisionnement à la création de contrats intelligents, les cas d'usage sont variés et en pleine évolution. Cette section présente des exemples pratiques et montre comment les technologies blockchain sont implémentées dans des environnements réels.

#### Démonstration d'une blockchain simple en Python

L'une des façons les plus simples d'appréhender le fonctionnement d'une blockchain est de la créer en Python. Voici les étapes essentielles pour concevoir une blockchain de base.

1. **Structure d’un bloc**
   Un bloc de la blockchain contient généralement trois éléments essentiels :
   - **Index** : Un identifiant unique pour chaque bloc.
   - **Timestamp** : La date et l’heure de la création du bloc.
   - **Données** : Les informations stockées dans le bloc, comme des transactions ou des événements.
   - **Hash du bloc précédent** : Le lien avec le bloc précédent, assurant la chaîne.
   - **Hash du bloc actuel** : Un identifiant unique généré à partir des données du bloc et du hash du bloc précédent.

   En Python, un bloc peut être représenté par une classe `Block` avec ces propriétés. Le code peut ressembler à ceci :

   ```python
   import hashlib
   import time

   class Block:
       def __init__(self, index, previous_hash, timestamp, data, hash):
           self.index = index
           self.previous_hash = previous_hash
           self.timestamp = timestamp
           self.data = data
           self.hash = hash

       def calculate_hash(self):
           block_string = f'{self.index}{self.previous_hash}{self.timestamp}{self.data}'
           return hashlib.sha256(block_string.encode('utf-8')).hexdigest()

   def create_genesis_block():
       return Block(0, "0", int(time.time()), "Genesis Block", "0")

   def create_new_block(previous_block, data):
       index = previous_block.index + 1
       timestamp = int(time.time())
       hash = hashlib.sha256(f'{index}{previous_block.hash}{timestamp}{data}'.encode('utf-8')).hexdigest()
       return Block(index, previous_block.hash, timestamp, data, hash)

   # Création de la chaîne de blocs
   blockchain = [create_genesis_block()]
   previous_block = blockchain[0]
   for i in range(1, 10):
       new_block = create_new_block(previous_block, f"Block #{i} Data")
       blockchain.append(new_block)
       previous_block = new_block

   # Affichage de la blockchain
   for block in blockchain:
       print(f"Block #{block.index} : {block.hash}")

  ```


  Ce code illustre une chaîne de blocs qui s’étend avec chaque nouvelle "transaction" (ici, des données textuelles). Chaque bloc se réfère au précédent grâce à son hash, assurant la continuité de la blockchain.

2. **Validité et ajout de blocs **

Lorsqu’un nouveau bloc est ajouté, sa validité est vérifiée par rapport à la chaîne existante. Si le hash du bloc précédent ne correspond pas, cela signifie qu'une tentative de fraude a été effectuée. Dans une implémentation réelle, ce processus est répété et vérifié par plusieurs nœuds du réseau, assurant la sécurité de la blockchain.

**Utilisation de frameworks de blockchain**


Bien que créer une blockchain à partir de zéro soit un excellent moyen d'apprendre, dans un cadre réel, des frameworks et des plateformes spécialisées sont utilisés pour déployer des blockchains plus complexes.





