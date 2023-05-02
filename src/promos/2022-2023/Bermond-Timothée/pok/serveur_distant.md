---
layout: layout/post.njk

title: "Serveur Distant"
authors:
  - Timothée Bermond

---
<!-- Début Résumé -->
Je vais créer un site qui permet de compter les points au Yams.
Il est disponible [ici](https://github.com/Timothee-Bermond/yams)
<!-- Fin Résumé -->
## Liste des thâches

- Création du front
- Suivi du cours de Mr. Brucker en MON2.1
- Création d'un compte sur evh
- Création du back avec node
- Génération de cookies
- Création BD
- Lien back et front
- Lien back et BD : routes + API

## Sprint 1
Durant le sprint 1 (25/11 - 7/12), je prévois :
- Tout d'abord de créer la partie front de mon site
- D'avoir entièrement suivi le cours dispensé en 2e année afin d'avoir les compétences pour déployer mon site sur un serveur distant.
- D'aller voir Mr. Brucker pour me créer un compte sur l'evh

Durant ce print j'ai eu le temps de créer toute ma partie front.
<img src="../Images/yams.jpg"/>
J'ai rencontré plusieurs difficultés : je voulais notamment ajouter un input avec une liste déroulante et une zone de texte. J'ai eu du mal à trouver comment faire, la solution était toute simple : utilisé une datalist qui en plus peut-être réutilisable pour plusieurs input.
<img src="../Images/datalist.jpg">
Une autre difficulté a été la création d'indication au survol d'une image. Je me suis pris la tête avec des *:hoover* alors qu'il suffisait d'utiliser la propriété title.
<img src="../Images/indication.jpg">
J'ai également tenté d'implémenter une boucle for dans le fichier javascrpit afin de traiter les scores de tous les joueurs d'un seul coup ce qui m'aurait permis de créer facilement d'autres joueurs. Mais cette méthode n'a pas fonctionné et je n'ai pas eu le temps de chercher une méthode alternative.
Pour toute la partie CSS je me suis référé à mon [MON1.2](../../../../mon/TB/Mes_MON/CSS). Il y a juste la fonctionnalité *:before* que j'ai utilisé afin d'ajouter un fond d'écran partiellement opaque.

J'ai ensuite suivi la [formation](https://francoisbrucker.github.io/cours_informatique/enseignements/ecm/2A/option-web/) de Mr. Brucker, notamment le Projet Numérologie, afin de me former sur les serveurs web. Je n'ai pas eu le temps de tout parcourir mais je finirais ça d'ici la fin de la semaine.

Pour ce qui est du dernier point de ce sprint : la création du compte sur l'evh, je m'y suis pris un peu tard et n'ai pas eu le temps de le faire.

J'ai également pour idée d'ajouter une fonctionnalité qui permet de créer des groupes, par exemple des gens avec qui vous jouez souvent, et lorsque vous vous connecterez les noms des joueurs seront entrés automatiquement et vous aurez accès aux nombres de parties gagnées de chacun et potentiellement d'autres statistiques.

## Sprint 2

Pour le sprint 2 je prévois de :
- Créer le back avec node
- Générer les cookies
- Créer la BD
- Mettre en place le lien back et front
- Ainsi que le lien back et BD : routes + API
- Faire en sorte que 2 joueurs puissent remplir les scores en même temps

Durant ce 2ème sprint, je me suis, tout d'abord, occupé de mettre en place node et express.

Pour cela, j'ai réorganisé mes fichiers en créant un dossier *static*.

De plus, j'ai séparé la partie création de la partie et déroulée de la partie, car un de mes objectifs est de faire en sorte que 2 joueurs puissent remplir les scores en même temps. 

Puis j'ai initialiser le projet et installé le package express.

J'ai ensuite créé le fichier *server.js* qui contiendra les routes et un dossier *back* pour les calculs.

J'arrive donc à cette architecture : 

    __ back
    |__ calcul.js
    __ node_module
    __ static
    |__ Images
    |__ index.html
    |__ index.js
    |__ yams.css
    |__ yams.css
    |__ yams.html
    |__ yams.js
    __ package-lock.json
    __ package.json
    __ server.js

Puis j'ai mis en place ma base de données. Pour cela, j'ai utilisé SQlite et sequelize.

Tout d'abord, je fais le lien avec la base de données SQlite:

```javascript
  const sequelize = new Sequelize({
    dialect: 'sqlite',
    storage: path.join(__dirname, 'db.sqlite')
  });
```

Puis je créé mon modèle : 

```javascript
  const Partie = sequelize.define('Partie',{
    nombreJoueurs: {
        type: DataTypes.INTEGER,
        allowNull: false,
        defaultValue:1
    },
    nameJ1 : {
        type: DataTypes.STRING,
        allowNull: false,
        defaultValue:'Joueur 1'
    },
    nombre1J1: {
        type: DataTypes.INTEGER,
        allowNull: false,
        defaultValue:0
    },
    ...
    chanceJ4: {
        type: DataTypes.INTEGER,
        allowNull: false,
        defaultValue:0
    },
    totalJ4: {
        type: DataTypes.INTEGER,
        allowNull: false,
        defaultValue:0
    }
  })
```

Je n'ai affiché qu'une partie car le modèle est très loin puisque je stock les points de tous les joueurs.
Je me suis demandé si il était possible de créer un modèle *player* puis de l'invoquer 4 fois dans mon modèle *partie* mais je n'ai pas trouvé la réponse.

Ensuite j'ai mis en place ma première route qui permet de créer la partie. Lorsque l'utilisateur clique sur le bouton suivant, une nouvelle partie est créée dans la base de données et les noms des joueurs sont récupérés dans les *headers* de la requête et enregistré dans la partie, puis un cookie est créé contenant l'id de la partie. J'ai cependant un problème avec cela car des fois le cookie ne s'envoie pas et je reste donc bloqué dans la partie précédente.

index.js : 
```javascript
  document.getElementById("bouton_suivant").addEventListener("click", () => {
    players = {
      nbrPlayers: nbr_players,
      player1: document.getElementById('text_choix1').value,
      player2: document.getElementById('text_choix2').value,
      player3: document.getElementById('text_choix3').value,
      player4: document.getElementById('text_choix4').value
    };
    fetch('/create',{
      method:'POST',
      headers:{
        'Content-Type': 'application/json',
        'Players':JSON.stringify(players)
      },
    })
    .then(
      window.location.replace('./yams.html')
      )
  })
```

server.js : 
```javascript
  app.use("/create", (req, res) => {
  db.Partie.create({
    }).then((partie) => {
      parametres = req.rawHeaders.toString().split("{")[1].split("}")[0]
      partie.nombreJoueurs = parametres.split(",")[0].split(":")[1]
      partie.nameJ1 = parametres.split(",")[1].split(":")[1]
      partie.nameJ2 = parametres.split(",")[2].split(":")[1]
      partie.nameJ3 = parametres.split(",")[3].split(":")[1]
      partie.nameJ4 = parametres.split(",")[4].split(":")[1]
      res.cookie("id", partie.id)
      partie.save()
      res.end()
    })
  })
```
J'utilise une méthode un peu barbare pour récupérer les noms des joueurs mais je n'ai pas trouvé comment faire mieux.

{% faire %}
Update : je suis allé voir Mr. Brucker et il suffisait d'utiliser le middleware bodyParser afin de récupérer les données dans le body de la requête. Ce qui me donne donc : 

index.js :
```javascript
  fetch('/create',{
      method:'POST',
      credentials: 'include',
      headers:{
        'Content-Type': 'application/json',
      },
      body:JSON.stringify(players)
    })
```

server.js :
```javascript
  partie.nombreJoueurs = req.body.nbrPlayers
  partie.nameJ1 = req.body.player1
  partie.nameJ2 = req.body.player2
  partie.nameJ3 = req.body.player3
  partie.nameJ4 = req.body.player4
  partie.save()
```
{% endfaire %}

Une fois la partie créée il faut que j'affiche le nom des joueurs ainsi que leur fiche de points. 

J'ai tout d'abord voulu accéder à la base de données depuis le fichier *yams.js* mais je n'ai pas réussi donc j'ai implémenté une route */initialisation* qui récupère le nombre de joueurs ainsi que leur nom dans la base de données et qui les affiche.

yams.js :
```javascript
    fetch('/initialisation')
    .then(response => response.json())
    .then(data => {
        console.log(data)
        if(data.nombreJoueurs == 1){
            document.getElementById('nom_j1').textContent = data.nameJ1.split('"')[1]
            document.getElementById('joueur1').classList.remove('hide')
            document.getElementById('btn_new_game').classList.remove('hide')
        }
        else if(data.nombreJoueurs == 2){
            document.getElementById('nom_j1').textContent = data.nameJ1.split('"')[1]
            document.getElementById('joueur1').classList.remove('hide')
            document.getElementById('nom_j2').textContent = data.nameJ2.split('"')[1]
            document.getElementById('joueur2').classList.remove('hide')
            document.getElementById('btn_new_game').classList.remove('hide')
        }
        else if(data.nombreJoueurs == 3){
            document.getElementById('nom_j1').textContent = data.nameJ1.split('"')[1]
            document.getElementById('joueur1').classList.remove('hide')
            document.getElementById('nom_j2').textContent = data.nameJ2.split('"')[1]
            document.getElementById('joueur2').classList.remove('hide')
            document.getElementById('nom_j3').textContent = data.nameJ3.split('"')[1]
            document.getElementById('joueur3').classList.remove('hide')
            document.getElementById('btn_new_game').classList.remove('hide')
        }
        else if(data.nombreJoueurs == 4){
            document.getElementById('nom_j1').textContent = data.nameJ1.split('"')[1]
            document.getElementById('joueur1').classList.remove('hide')
            document.getElementById('nom_j2').textContent = data.nameJ2.split('"')[1]
            document.getElementById('joueur2').classList.remove('hide')
            document.getElementById('nom_j3').textContent = data.nameJ3.split('"')[1]
            document.getElementById('joueur3').classList.remove('hide')
            document.getElementById('nom_j4').textContent = data.nameJ4.split('"')[1]
            document.getElementById('joueur4').classList.remove('hide')
            document.getElementById('btn_new_game').classList.remove('hide')
        }   
    })
```

server.js:
```javascript
  app.use('/initialisation', (req, res) => {
    id = req.cookies.id
    console.log(id)
    db.Partie.findByPk(id)
    .then((data) => {
      res.json(data)
    })
  })
```
J'utilise le package cookie-parser afin de récupérer les cookies, ce qui me permet d'obtenir l'id de la partie en cours.

J'ai ensuite créé la route qui permet d'enregistrer les valeurs des nouveaux scores du joueur 1. 

Pour cela, j'utilise la fonction *onchange* et je récupère les valeurs de toutes les combinaisons et je les stock dans un dictionnaire que j'envoie dans les *headers* de mon fetch. 

Je récupère ces données dans *server.js*, stock les données dans la bd puis à l'aide de *calcul.js* je calcule la somme et le total des points que j'ajoute également à la bd. 

J'ai tout d'abord eu des erreurs puisque les combinaisons vides me renvoyait "" et lorsque je calculais la somme j'obtenais donc une chaine de caractère. J'ai pour cela, modifié mon dictionnaire avec une boucle for afin afin de remplacer les valeurs vides par 0.

yams.js : 
```javascript
for(const combi of list_total){
    document.getElementById(combi+'j1').onchange = function(){

        ...

        pts_J1 = {
            nombre1J1 : document.getElementById('nombre1j1').value,
            nombre2J1 : document.getElementById('nombre2j1').value,
            nombre3J1 : document.getElementById('nombre3j1').value,
            nombre4J1 : document.getElementById('nombre4j1').value,
            nombre5J1 : document.getElementById('nombre5j1').value,
            nombre6J1 : document.getElementById('nombre6j1').value,
            brelanJ1 : document.getElementById('brelanj1').value,
            carreJ1 : document.getElementById('carrej1').value,
            fullJ1 : pts_fullj1,
            psJ1 : pts_psj1,
            gsJ1 : pts_gsj1,
            yamsJ1 : pts_yamsj1,
            yams2J1 : pts_yams2j1,
            yams3J1 : pts_yams3j1,
            chanceJ1 : document.getElementById('chancej1').value,
        }

        for (const pts in pts_J1){
            if(pts_J1[pts] == ''){
                pts_J1[pts] = 0
            } else if(typeof(pts_J1[pts]) == 'string') {
                pts_J1[pts] = parseInt(pts_J1[pts])
            }
        }
        fetch('/changeJ1',{
                method:'POST',
                headers:{
                  'Content-Type': 'application/json',
                  'Players':JSON.stringify(pts_J1)
                },
            }).then(response => response.json())
            .then(data => {
                document.getElementById('pts_sommej1').textContent = data.sommeJ1
                document.getElementById('pts_totalj1').textContent = data.totalJ1
            })
    }
}
```

server.js:
```javascript
app.use('/changeJ1', (req, res) => {
  pts_J1 = req.rawHeaders.toString().split("{")[1].split("}")[0]
  id = req.cookies.id
  db.Partie.findByPk(id)
  .then((data) => {
    data.nombre1J1 = parseInt(pts_J1.split(",")[0].split(":")[1])
    data.nombre2J1 = parseInt(pts_J1.split(",")[1].split(":")[1])
    data.nombre3J1 = parseInt(pts_J1.split(",")[2].split(":")[1])
    data.nombre4J1 = parseInt(pts_J1.split(",")[3].split(":")[1])
    data.nombre5J1 = parseInt(pts_J1.split(",")[4].split(":")[1])
    data.nombre6J1 = parseInt(pts_J1.split(",")[5].split(":")[1])
    data.brelanJ1 = parseInt(pts_J1.split(",")[6].split(":")[1])
    data.carreJ1 = parseInt(pts_J1.split(",")[7].split(":")[1])
    data.fullJ1 = parseInt(pts_J1.split(",")[8].split(":")[1])
    data.psJ1 = parseInt(pts_J1.split(",")[9].split(":")[1])
    data.gsJ1 = parseInt(pts_J1.split(",")[10].split(":")[1])
    data.yamsJ1 = parseInt(pts_J1.split(",")[11].split(":")[1])
    data.yams2J1 = parseInt(pts_J1.split(",")[12].split(":")[1])
    data.yams3J1 = parseInt(pts_J1.split(",")[13].split(":")[1])
    data.chanceJ1 = parseInt(pts_J1.split(",")[14].split(":")[1])
    data.sommeJ1 = calcul.somme(data.nombre1J1, data.nombre2J1, data.nombre3J1, data.nombre4J1, data.nombre5J1, data.nombre6J1)
    data.totalJ1 = calcul.total(data.sommeJ1, data.brelanJ1, data. carreJ1, data.fullJ1, data.psJ1, data.gsJ1, data.yamsJ1, data.yams2J1, data.yams3J1, data.chanceJ1)
    data.save()
    res.json(data)
  })

})
```
{% faire %}
Update : comme pour le nom des joueurs j'envoie les points des joueurs dans le *body* et non les *headers* de la requête.
{% endfaire %}

J'ai ensuite réitéré cela pour les joueurs 2, 3 et 4.

J'ai toujours un problème, c'est que mes cookies ne s'envoient pas toujours et je n'arrive pas à comprendre ce qui en est la cause.
Je suis allé voir avec Mr. Brucker et ce serait un problème avec les fonctions asynchrone (le cookie met trop de temps à s'envoyer et le code passe donc à la suite sans l'envoyer). J'ai essayé d'ajouter un then mais ça n'a pas réglé mon problème. 

### Déploiement sur l'ovh

Pour déployer son site sur l'ovh il faut tout d'abord suivre ces [instructions](https://francoisbrucker.github.io/cours_informatique/cours/ops/ssh/) pour générer sa paire de clé et accéder à son compte sur l'ovh. 

(Il y a peut-être quelques petites coquilles qui vont se glisser dans l'explication donc si quelque chose ne marche demandez à Mr. Brucker il saura vous répondre)

Puis, il faut ouvrir le fichier readme.txt pour trouver quel est le port associé à son compte.
```bash
cat readme.txt
```
Il faut modifier le port dans le fichier *server.js* afin qu'il corresponde à celui du fichier readme.txt.

Ensuit on ajoute son code (que l'on a mis sur github) dans le dossier node avec la commande : 
```bash
git clone https://github.com/Timothee-Bermond/yams.git 
```
Ensuite on se place dans le dossier contenant notre code (yams pour moi), et on entre la commande : 
```bash
node server.js
```
On peut maintenant accéder à notre site à l'url : node.mon_herbe@ovh1.ec-m.fr (en replacant mon_herbe par votre herbe).

Seul bémol lorsque l'on ferme le shell, le server s'arrête et on n'y a plus accès. Pour qu'il tourne même lorsque le shell est fermé il faut se placer dans le dossier contenant notre code et taper la commande :
```bash
/usr/bin/screen -d -m -S node node server.js
```
Et voilà, le site est déployé !




