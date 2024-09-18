---
layout: layout/pok.njk

title: "GoAuth2.0"
authors:
  - Valentin Billa

date: 2024-09-05

tags: 
  - 'temps 1'
  - 'vert'
  - 'avancé'
  - 'Go'
  - 'Authentification'
  - 'OAuth2'

résumé: Création d'un serveur d'authentification OAuth2.0 en Go.
---

{% prerequis %}
- Bases relativement solides en programmation
- Une idée des différences entre utilisateur, client, serveur
- Quelques concepts d'authentification peuvent aider (token, hash...)  
{% endprerequis %}

## Objectifs

Je n'ai jamais codé en Go, mais le langage m'intrigue depuis un moment, c'est pourquoi j'ai envie de tenter de coder un
projet concret pour m'initier aux bases. En l'occurence, ce sera un serveur d'authentification OAuth2, mes connaissances
sur le sujet sont relativement superficielles, c'est pourquoi je souhaite les approfondir au long de ce POK.

{% info %}
Les objectifs sont volontairement très (trop) optimistes, pour être certain de ne pas manquer de contenu !
{% endinfo %}

## À propos de OAuth et Go
OAuth est un protocole d'autorisation utilisé pour permettre à des applications tierces d'accéder aux ressources d'un
utilisateur sans divulguer les identifiants de celui-ci. Il est couramment utilisé pour permettre des connexions via des
services comme Google, Facebook, etc.

Go (ou Golang) est un langage de programmation développé par Google, connu pour sa simplicité, ses performances élevées,
et son support solide pour la concurrence grâce aux goroutines.

## Sprint 1
### Planning Prévisionnel
#### 1.1 Introduction à Go
  - [X] Configurer l'environnement de développement Go.
  - [X] Parcourir les tutoriels de base sur Go.
  - [X] Écrire quelques programmes simples pour se familiariser avec la syntaxe et les concepts de Go.

#### 1.2 Concepts de base d'OAuth2
  - [X] Étudier le protocole OAuth2 (RFC 6749).
  - [X] Comprendre les différents rôles (Client, Ressource Owner, Authorization Server, Resource Server).
  - [X] Examiner les types de flux (Authorization Code, Implicit, Resource Owner Password Credentials, Client Credentials).

#### 1.3 Développement initial
  - [X] Créer un projet Go pour le serveur OAuth2.
  - [X] Implémenter une première version du serveur OAuth2 avec les routes de base pour l'autorisation et les tokens.
  - [X] Tester les premières implémentations avec des clients simples.

*Propositions pour le Sprint 2*
#### 2.1 Tests et Client
  - [ ] Écrire des tests unitaires pour quelques fonctions internes.
  - [ ] Écrire des tests d'intégration pour les routes principales.
  - [ ] Créer une page de connection avec Java Spring Boot Oauth.

#### 2.2 Persistence des données
  - [ ] Choisir et configurer une base de données (ex. MySQL).
  - [ ] Mettre en place les schémas de base pour stocker les utilisateurs, les clients OAuth2, et les tokens.

### Horodatage

| Date           | Heures passées | Indications             |
|----------------|----------------|-------------------------|
| Samedi 07/09   | 2H             | Introduction à Go       |
| Lundi 10/09    | 4H             | Concepts d'OAuth2       |
| Mardi 11/09    | 4H             | Serveur Basique         |
| Mercredi 12/09 | 5H             | Intégration à Redis     |
| Samedi 13/09   | 4H             | Token Rotation          |
| Dimanche 13/09 | 2H             | Fausse Routes Protégées |
| Lundi 13/09    | 4H             | OAuth2.1 & GitHub       |
| Mardi 14/09    | 3H             | Rédaction Compte Rendu  |
| **Total**      | **28H**        | **Petit Overtime...**   |

### Rétro

J'ai un peu abusé... le sujet m'intéresse beaucoup et j'avais envie de bien travailler sur un projet pour 
avoir des choses à mettre sur mon GitHub. Étant donné que j'ai tendance à hyper-focus, il va falloir que
je me fixe des limites dures pour le prochain sprint pour éviter d'en faire trop.

Néanmoins, j'ai pu faire le gros du travail de prototypage les 10 premières heures. Travail que j'ai 
ensuite raffiné les heures suivantes dont je parlerais dans des parties supplémentaires.

Mon plan pour le sprint 2 ne change que très peu (encore très fourni) car je n'ai volontairement pas
beaucoup touché à ce qui était prévu pour le second sprint.

Pour mieux respecter les objectifs de temps, je vais utiliser un minuteur plutôt qu'un chronomètre
pour l'horodatage et apposer des estimations de temps aux étapes prévues pour le sprint.
Aussi, la rédaction du compte rendu de POK m'a pris bien plus de temps que prévu,
je le prendrais en compte au sprint 2, en particulier en rédigeant au fur et à mesure que j'avance.

### Introduction à Go

Quel meilleur endroit pour faire connaissance avec un langage que la doc ?!
J'ai commencé par me balader sur un [tutoriel interfactif](https://go.dev/tour/) disponible sur le site du langage.

On y constate en effet la grande simplicité du langage
- 2 structures de données disponibles par défault (dictionnaires `map[T]T` et arrays `[]T`)
- seules les boucles `for` existent
- pas d'héritage (le type embedding permet une fonctionnalité similaire.)
- seulement deux types de visibilités (public et package private) choisies en fonction de la casse du premier caractère
- les erreurs sont des valeurs

Les channels sont au cœur du langage, mais je n'ai pas trop eu l'occasion d'y toucher.
Elles permettent une grande flexibilité et aisance dans la gestion de l'asynchrone.

Une fois le tutoriel complété, j'ai directement décidé de me mettre les mains à la patte
pour me mettre en conditions réelles.

Pour plus d'informations n'hésitez pas à aller voir les POK&MON existants sur Go
{% chemin %}
[MON d'Emma](../../../Gonin-Emma/mon/temps-1.1)
{% endchemin %}

### Concepts de base d'OAuth2

OAuth (Open Authorization) est un protocole d'autorisation standardisé permettant à des applications tierces d'accéder
aux ressources d'un utilisateur sans divulguer les identifiants de celui-ci.
OAuth est souvent utilisé pour permettre des connexions via des services comme Google, Facebook, etc.,
tout en renforçant la sécurité.

Voici une image pour illustrer rapidement le rôle du serveur d'authentification (Dropbox dans le cas ci-dessous)
![Illustration de l'authentification](./basic-auth-flow.png)

L'objectif premier du protocole OAuth est simple : transmettre un token (~équivalent à une clé numérique)
à une application tierce pour que celle-ci puisse faire des actions en tant que l'utilisateur qui
a consenti à lui donner certains droits. Par exemple, sur l'image d'au-dessus, l'application à le
droit d'accéder aux fichiers dropbox de l'utilisateur.

Comme pour beaucoup de processus de sécurité ou d'authentification, la communication s'établie
en plusieurs étapes, car elle a pour objectif de vérifier tout un tas de choses sur les parties prenantes
que l'on détaillera lors de l'explication du flow authorization code avec PKCE.

Pour mieux comprendre les concepts clés, j'ai passé un long moment à lire la [spécification OAuth2](https://datatracker.ietf.org/doc/html/rfc6749),
suite à quoi j'ai utilisé le [playground OAuth](https://www.oauth.com/playground/) pour tester les différents flows d'authentification.

Plusieurs protocoles sont proposés dans la spécification pour récupérer le token cependant nous
allons nous concentrer sur un seul, principalement, car c'est le plus recommandé et sécurisé,
mais aussi puisque c'est d'après moi le plus intéressant.

#### Clients Publics / Privés
> **RFC 6749 Section 2.1: OAuth 2.0 Client Types**
> [tools.ietf.org/html/rfc6749#section-2.1](https://tools.ietf.org/html/rfc6749#section-2.1)
>
> OAuth définit deux types de clients : les clients confidentiels et les clients publics.
>
> Les clients confidentiels sont des applications qui sont capables de s'authentifier de manière sécurisée avec le serveur d'autorisation,
> par exemple en étant capables de garder leur secret client \[équivalent d'un mot de passe\] enregistré en sécurité. \
> Les clients publics ne peuvent pas utiliser de secrets clients enregistrés, 
> comme les applications s'exécutant dans un navigateur ou sur un appareil mobile.
> *texte traduit à partir de https://oauth.net/2/client-types/*

#### Protocole avec code autorisation et PKCE 

Ce [playground](https://www.oauth.com/playground/authorization-code.html) est une petite merveille pour mieux comprendre
le protocole utilisé, je conseille de faire une tour dessus avant la lecture des paragraphes suivants.

![Authorization Code Flow](authorization-code-flow.png)
Ici, okta est le serveur d'authentification et le 'resource server' peut être utilisé pour récupérer des données à partir des tokens fournis par okta.
*Tout à l'heure Dropbox était responsable à la fois de l'authentification et de ressources, ce n'est pas toujours le cas.*

Le flow du code d'autorisation comprend plusieurs étapes clés :

1. **Initialisation de la demande d'autorisation** :
   L'utilisateur commence le processus d'autorisation en accédant à une page de connexion via l'application cliente.
   L'application redirige l'utilisateur vers le serveur d'autorisation avec les informations pertinentes (client_id,
   redirection_uri, etc.).
2. **Demande de l'autorisation** :
   L'utilisateur est invité à se connecter et à autoriser l'accès pour l'application cliente.
   Le serveur d'autorisation affiche une page de connexion où l'utilisateur doit entrer ses identifiants.
3. **Consentement** :
   Après s'être connecté, l'utilisateur est invité à donner son consentement quant aux informations auxquelles l'
   application cliente peut accéder.
4. **Obtention du code d'autorisation** :
   Une fois l'utilisateur authentifié et le consentement donné, le serveur d'autorisation émet un code d'autorisation et
   redirige l'utilisateur vers l'application cliente grâce à l'URL de redirection fournie. Cette URL contient le code
   d'autorisation.
5. **Échange du code d'autorisation contre un token** :
   L'application cliente envoie ce code d'autorisation au serveur d'autorisation pour obtenir un token d'accès.
6. **Réception du token d'accès** :
   Le serveur de token vérifie l'authenticité de la demande, puis émet un token d'accès.
7. **Accès aux ressources protégées** :
   L'application cliente utilise ensuite ce token d'accès pour accéder aux ressources protégées de l'utilisateur sur le
   serveur de ressources.

### PKCE (Proof Key for Code Exchange) ?

Le PKCE est une extension du protocole OAuth 2.0 conçue pour atténuer certaines
vulnérabilités de sécurité associées aux clients publics qui ne peuvent pas stocker de secrets client en toute sécurité.
En ajoutant PKCE, on renforce la sécurité du Flow Authorization Code en empêchant les éventuels attaquants d'obtenir des
tokens d'accès en interceptant le code d'autorisation durant l'échange.

Voici un résumé des échanges avec PKCE :
1. **Client** : Génère un `code_verifier` et calcule `code_challenge = hash(code_verifier)`.
2. **Client** : Fait une demande d'autorisation en incluant `code_challenge`.
3. **Serveur d'autorisation** : Stocke `code_challenge` et émet un `code d'autorisation`.
4. **Client** : Fait une demande de token d'accès en incluant le `code_verifier`.
5. **Serveur d'autorisation** : Vérifie `code_challenge` contre le hash du `code_verifier` fourni.
6. **Serveur d'autorisation** : Émet un token d'accès si la vérification est réussie.

Cette procédure garantie l'identité du client auprès du serveur d'autorisation. En effet, puisque l'opération de
hash ne peut être faite que dans un sens, même si le `code_challenge` seul le client qui a généré le `code_verifier`
peut le retrouver et l'envoyer au serveur d'autorisation.

### Développement Initial

{% info %}
Le code que j'ai écrit lors de ce POK est disponible sur un [répository GitHub](https://github.com/ValentinBilla/GoAuth2.0). \
*J'y ai même mis un logo tout mignon, ça vaut le détour.*
{% endinfo %}

Au vu des étapes clés du flow code d'autorisation, je dois implémenter obligatoirement 3 endpoints 
1. `GET /authorize` (**Demande de l'autorisation**)
   Qui renvoie une page HTML de connection pour que l'utilisateur se connecte
   *un simple login suffira, je ne souhaite pas me concentrer sur la partie UI/UX*
2. `POST /authorize` (**Obtention du code d'autorisation**)
   Qui permet de générer le code d'accès et rediriger l'utilisateur vers l'application cliente
3. `POST /token` (**Échange du code d'autorisation contre un token**)

En plus de ceux-là, j'ai créé un enpoint permettant de simuler une requête sur le serveur de resource,
authentifiée par un token : `GET /photos/:id`

#### Modules et Frameworks
J'ai décidé d'utiliser gin pour plus simplement créer des endpoints avec les paramètres que je souhaite décris par des structs.

Voici un exemple d'endpoint déclaré pour gin :
```go
type authorizationGrantRequest struct {
	ResponseType string `form:"response_type" binding:"required,oneof=code token"`
	ClientId     string `form:"client_id" binding:"required"`
	ClientSecret string `form:"client_secret"`
	RedirectUri  string `form:"redirect_uri" binding:"required,url"`
	Scope        string `form:"scope"`
	State        string `form:"state" binding:"required"`

	CodeChallenge       string `form:"code_challenge" binding:"required,if=CodeChallengeMethod=plain"`
	CodeChallengeMethod string `form:"code_challenge_method" binding:"required,oneof=plain S256"`

	Username string `form:"username"`
	Password string `form:"password"`
}

func GetAuthorize(c *gin.Context) {
	var request authorizationGrantRequest
	if err := c.ShouldBind(&request); err != nil {
		c.JSON(400, gin.H{"error": err.Error()})
		return
	}

	c.Header("Content-Type", "text/html; charset=utf-8")
	c.HTML(http.StatusOK, "authorize.gohtml", gin.H{
		"clientId": request.ClientId,
		"scopes":   strings.Split(request.Scope, "+"),
	})
}
```

Ensuite, pour la génération de tokens j'ai préféré déléguer à un module existant (`github.com/golang-jwt/jwt/v5`), 
car c'est une partie sensible qui n'est pas triviale à correctement implémenter, surtout la validation de tokens existants.

Initialement, j'ai écrit le hashing et la validation des mots de passes mot même en utilisant Argon2ID un algorithme de
hash recommandé par [OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#argon2id).
J'ai finalement, pour la postérité, décidé d'utiliser un wrapper existant (`github.com/alexedwards/argon2id`).

Pour ce qui est du stockage des codes d'accès et des tokens de refresh, j'ai décidé d'utiliser Redis pour sa simplicité
et la possibilité d'assigner une durée de vie aux données stockées après laquelle elles expirent.

## Sprint 2
### Planning Prévisionnel
#### 2.1 Tests et Client
- [ ] Écrire des tests unitaires pour quelques fonctions internes.
- [ ] Écrire des tests d'intégration pour les routes principales.

#### 2.2 Persistence des données
- [ ] Choisir et configurer une base de données (ex. MySQL).
- [ ] Mettre en place les schémas de base pour stocker les utilisateurs, les clients OAuth2, et les tokens.

{% lien %}
- [Site officiel de Go](https://go.dev)
- [Spécification OAuth2.0](https://datatracker.ietf.org/doc/html/rfc6749)
- [Playground OAuth2.0](https://www.oauth.com/playground/)
{% endlien %}
