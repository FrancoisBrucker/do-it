---
layout: layout/mon.njk

title: "Prise de note du Cours Openclassrooms"
authors:
  - Arthur Louradou

date: 2023-09-27

tags: 
  - "cyber"
  - "pentest"
  - "security"
  - "web"
  - "sql"
  - "injection"
  - "notes"
---

## Introduction

Test d’intrusion = Pentest est une partie de la sécurité offensive en informatique.

Illustration des niveaux de connaissance dans une app : boite noire, grise, blanche.

<img src="https://user.oc-static.com/upload/2022/07/20/16583250551232_FR_7727176_Intrusion-Web_Static-Assets_p1c2-3a.png"/>

Différentes façons de tester le système : "bug bounty", "red team", "test d'intrusion"

## Posture du pentester, hacker éthique

Hacker → Penser “outside the box” ≠ mauvaises intentions. Le cadre du cours est entièrement légal tant qu’il n’est pas testé sur des systèmes sans autorisation.

Qualité principale : Autodidacte ! Soit précisément ce qui est ciblé par les MON de Do_It !

## Cadrage du besoin de test d’intrusion

Gestion de projet pour la préparation d’une attaque.

### 1. Présenter sa démarche

Parler des approches de boites grise, noire, blanche vues plus haut, des habitudes de fonctionnement du client pour ne pas impacter son activité à un moment critique.

### 2. Périmètre du test

Plusieurs types de clients : mature ou débutant. Avec ce dernier, il faut être plus pédagogue.

On pose les questions structurelles puis techniques. Demander une démonstration à l’usage.

Lien avec le cours de Design Thinking : se mettre à la place du client pour penser comme dans son activité.

Exemple : Application e-santé

**→ Quelles questions à poser au client ?**

Que fait l’application ? Qui interagit avec ? (patients, médecins, administratifs, etc.) Quelles données sont stockées et comment ? A-t-on confiance en les utilisateurs ? (Pour mener un test plutôt axé boite grise ou boite blanche) + Demander une démonstration du parcours d’un utilisateur classique.

Correction :

https://course.oc-static.com/courses/7727176/Réalisez+un+test+d'intrusion+web+-+Cadrez+votre+intervention+à+partir+des+objectifs+du+test+-+Corrigé.pdf

<aside>
🧑🏻‍💻 À ce stade, il me parait assez prématuré de parler de client, organisation et budget sans même avoir développé de compétences techniques. Je vais donc avancer dans le cours pour passer aux parties les plus intéressantes pour les objectifs de ce MON.

</aside>

## Environnement de travail

{% info "ℹ️" %}
Conseil : Prendre des notes de tout ce que l’on fait pour la traçabilité et se couvrir légalement.

{% endinfo %}

Par le passé, j’avais commencé à prendre des notes sur les outils pris en main avec HackTheBox.

Installation de Kali Linux. Mise à jour de VirtualBox et lancement de la machine déjà installée.

## Techniques

### Google Dorks

Faire de la recherche en source ouverte avec quelques techniques. Pour vérifier si un mot de passe ou bien un token ne serait pas exposé dans une documentation publique sur internet par exemple.

****************Connaitre les mots clés :**************** `site:root-me.org`, `ext:pdf`, `“password”` permettent d’affiner les recherches sur un site en particulier.

Recensement des failles trouvées dans Google : https://www.exploit-db.com/google-hacking-database

### OSINT

Renseignement en source ouverte.

Rechercher :

- Adresses mail, Domaines
- Dépôts Github
- Fuites de bases de données

À la main ou avec des outils spécialisés :

- https://github.com/laramies/theHarvester
- https://github.com/lanmaster53/recon-ng

Et recherches plus larges sur le Darknet.

Autre outil connu avant de lire ce cours : https://epieos.com/ qui permet de retrouver tous les comptes sur des services où une adresse mail ou un numéro de téléphone serait utilisé.

## Reconnaissance active

Outils techniques pour explorer plus largement le SI d’une entreprise.

- Registre whois
- Énumération des domaines et scrapping des urls trouvés dans chacun
- Certificats TLS - Transport Layer Security
- Historique DNS

Outil le plu complet d’exploration : https://github.com/OWASP/Amass de OWASP, dispo sur Kali.

Exemple : Pour lister les domaines de centrale-marseille.fr (attention, à ne pas faire sans l'accord du site !)

```bash
amass enum -d [centrale-marseille.fr](http://centrale-marseille.fr/) -src -active
```

Avec comme paramètres :

- `-src` pour afficher les sources de données
- `-active` pour aller chercher dans les certificats les noms de domaine à tester

## Nmap

- **Sans paramètre (= Scan SYN) :**
1. Résout le nom DNS de l'hôte.
2. Ping l'hôte.
3. Si l'hôte répond, réalise un “SYN scan”.
4. Ne scanne que les 1 000 premiers ports les plus connus sur les 65 535 possibles.
5. Ne fait pas de détection du service en écoute.

> N’envoie qu’un paquet SYN et attend la réponse SYN+ACK.
N’envoie jamais le ACK ou le RST.
La connexion reste donc ouverte chez le serveur, jusqu’au timeout !
>
- **Option `-p` :** Scan des ports dans une range de 0-65535
- **Option `-sV` :** Vérifie le service en écoute et sa version
- **Option `-oA` :** Pour enregistrer les résultats dans un format spécifique, dans l’exemple `-oA metasploit2`.

Il conviendrait de mettre en pratique les différentes options de Nmap car cet outil semble être à la base de toute investigation en pentest.

## Recherche des exploits à l’issue du scan

Avec Google, dans un premier temps

Avec des outils spécialisés ensuite, comme https://cve.mitre.org/index.html ou https://www.cvedetails.com/ qui donne le détail sur les CVE  (Common Vulnerability Exposure) recensées.

> **UTM (Unified Threat Management) :**
Logiciel qui peut fausser le résultat des scans lorsqu’ils détectent qu’ils sont scannés, entre autre !
>

## Chiffrement, Cryptographie

- **Communication TLS**

  Discussion entre client et serveur

- **Failles dans chiffrement ?**

  Vérifier la qualité du certificat TLS

  Vérifier les protocoles proposés par le serveur

  Suites de chiffrement

  Les libraires utilisées, parfois comportant des failles

<img src="https://user.oc-static.com/upload/2022/07/21/16584160662712_FR_7727176_Intrusion-Web_Static-Assets_p2c4-1a.png" alt="Schéma HTTPS"/>

> Dans le test d’intrusion, on vérifiera surtout la **qualité du certificat**.
>
> - qui peut ne pas être dans sa période de validité ;
> - dont le champ `subject name` ne correspond pas au nom DNS du site ;
> - dont l’autorité de certification n’est pas connue de votre ordinateur ;
> - qui peut simplement être révoqué ;
>
> i.e. “Votre connexion n’est pas privée” parfois indiqué dans les navigateurs :
>

Encore, différents outils :

https://www.ssllabs.com/ssltest/, https://github.com/rbsec/sslscan, https://github.com/drwetter/testssl.sh

## Protocoles et suites de chiffrement

Protocoles :

- SSL v2 ;
- SSL v3 ;
- TLS v1.0 ;

- TLS v1.1 ;
- TLS v1.2 ;
- TLS v1.3.

Seuls les protocoles en vert sont aujourd’hui recommandés pour HTTPS.

Pour chaque, il existe une liste de **suites de chiffrements** compatibles, de cette forme :

`<algo échange de clé>-<algo authentification>-<algo chiffrement symétrique et taille de clé>-<algo signature>`

Ex : `ECDHE-RSA-AES128-GCM-SHA256`

- `ECDHE` pour l’**échange de clés** ;
- `RSA` pour l’**authentification** ;
- `AES-128` pour le **chiffrement** ;
- `GCM` pour le mode d’opération du chiffrement par bloc (ce qui ne nous intéresse que peu dans notre cas de pentester, sauf dans certains cas très particuliers) ;
- `SHA-256` pour la **signature**.

Installation de SSLscan et utilisation :

Pull du projet Github. Lecture de la documentation https://www.oreilly.com/library/view/web-penetration-testing/9781788623377/285990a3-9992-40b0-ac36-69adc6fb47ce.xhtml

Dans le test effectué pour l’exemple sur root-me `sslscan [ctf12.root-me.org](http://ctf12.root-me.org/):443`, les protocoles utilisés sont tous anciens et vulnérables. Nous verrons ensuite comment exploiter ces vulnérabilités. → Mettre à jour openssl pour le serveur vulnérable

## Attaque d’un application web

### Utilisation d’un proxy d’interception

Comme un proxy (~VPN) mais qui est chargé de monitorer le trafic réseau vers l’application que l’on analyse.

Outil : **Burp Suite Community**

<aside>
ℹ️ **Installation** :
Revoir le tutoriel qui ne détaille pas comment configurer le proxy. Ensuite, les vidéos de tutoriel sur cet outil sont bien faites, elles expliquent comment configurer l’outil puis les fonctionnalités offertes par ce dernier.

</aside>

Onglets utiles : Intruder pour automatiser les requêtes et mener plusieurs fois une même attaque dans le scope, Repeater pour rejouer une requête avec des paramètres différents.

J’ai pu utiliser l’outil Intruder avec un dictionnaire de chemins courants (index, index.php, …) pour tester un à un tous ces chemins et avoir la satisfaction de réussir le challenge disponible à l’adresse : https://www.root-me.org/fr/Challenges/Web-Serveur/Fichier-de-sauvegarde

## Attaques par dictionnaire

Outil : seclists

Après l’installation avec `sudo apt install seclists`, nous avons des listes de dictionnaires dans le répertoire `/usr/share/seclists/`.

De nombreuses listes sont disponibles sur internet, comme celles utilisées dans le précédent challenge : https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/PHP.fuzz.txt
