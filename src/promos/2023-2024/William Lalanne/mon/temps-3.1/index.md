---
layout: layout/mon.njk

title: "Bases du développement mobile"
authors:
  - William Lalanne

date: 2023-09-27

tags: 
  - "temps 3"

résumé: "Dans ce MON je souhaite apprendre les bases de développement mobile"
---

{%prerequis%}

Pré-requis :
**Niveau :** Facile
**Prérequis :** Pour ce MON, il est nécessaire d'avoir certaines bases de JavaScript et de React pour comprendre les concepts avec plus de facilité mais il est possible de s'en passer. 

{%endprerequis%}


## Sommaire 

1. Présentation de React Native
2. Expo
3. Les bases de React Native
4. Créer une base de données pour l'app
5. Conclusion
6. Horodatage

## 1. Présentation

React Native est un framework créé par Facebook en 2015 qui permet de créer des applications mobile pour iOS ou Android en utilisant JavaScript. Dans le monde du développement mobilen il existe deux types distincts d'application : 
- Application native : 
- Application hybride : 

Techniquement, les applications développées aevc React Native  sont hybrides mais elles utilisent des composants graphiques natifs. 

## 2. Expo 
Expo est une plateforme qui permet de faire tourner une application mobile lors du développement de cette dernière. C'est très pratique pour voir à quoi ressemble l'application. 
Voyons comment expo fonctionne. 
D'abord, pour installer Expo il faut ouvrir un terminal et entrer la commande : 
```shell
npm install expo-cli
```

Une fois Expo installée, il faut créer un projet. On se place dans le dossier dans lequel on souhaite créer l'app et on utilise la commande : 
```shell
npx create-expo-app nomDeLApp
```

Une fois l'application créée, pour la visualiser, il suffit d'ouvrir un terminal, se placer dans le dossier dans lequel on a créé l'app et utiliser la commande : 
```shell
npm start
```
Quand on fait ça, un qr code apparaît dans le terminal comme ci-dessous : 

<div style="display:flex">
<div><img src="start_expo.webp"></div>
</div>

En téléchargeant l'application Expo sur son téléphone et en étant connecté sur le même réseau wifi que son ordinateur, on peut scanner le qrcode et visualiser l'application directement sur son téléphone. 


## 3. Les bases de React Native

Lorsque l'on travaille avec React Native et en développement mobile en général, le concept de View, "Vue" est souvent utilisé. Une view est le plus petit élément graphique que l'on peut créer, c'est une partie de l'écran qui peut contenir tout et n'importe quoi, une image, du texte, un input...
Comme pour React, React Native utilise des composants (components en anglais) qui sont des petits éléments de l'interface graphique, modulables et réutilisables. Les composants principaux en React Native sont donc : 
- View : 
- Text : affiche, stylise et imbrique des chaînes de texte et gère même les événements comme les clicks, les passages de souris...
- Image : pour afficher différents types d'image
- ScrollView : un conteneur dans lequel il est possible de défiler et qui peut contenir plusieurs composants et vues
- TextInput : input qui permet à l'utilisateur d'entrer du texte. 

En combinant tous ces composants, on peut réussir à créer des pages pour une application. C'est ce que je vais essayer de faire pour montrer comment React Native fonctionne. 

```js
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, TextInput, View, Image, ScrollView } from 'react-native';

export default function App() {
  return (
    <ScrollView style={styles.scrollViewContainer}>
      <View style={styles.container}>
        <Text>Bienvenue sur l'application de William</Text>
        <StatusBar style="auto" />
        <Image 
          source={require('./logo.webp')}
          style={styles.logo}
        />
        <TextInput style={styles.textInput} placeholder="Entrez votre texte ici"></TextInput>
        <Button>
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  textInput: {
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
  },
  scrollViewContainer: {
    flexGrow: 1,
  }
});
```

<div style="display:flex">
<div><img src="demo_app.webp" width="300" height="600"></div>
</div>

On va améliorer un peu cette page pour qu'elle ressemble à une page de connexion sur un site web. Il faut donc des input pour que l'utilisateur puisse entrer son prenom, so nom et un bouton pour se connecter. 

```js
export default function App() {
  return (
      <View style={styles.container}>
        <Text>Bienvenue sur l'application de William</Text>
        <Image 
          source={require('./logo.webp')}
          style={styles.logo}
        />
        <View style={styles.userInput}>
          <Text>Prénom</Text>
          <TextInput style={styles.textInput} placeholder="Entrez votre prénom ici"></TextInput>
        </View>
        <View style={styles.userInput}>
          <Text>Nom</Text>
          <TextInput style={styles.textInput} placeholder='Entrez votre nom ici'></TextInput>
        </View>
        <CustomButton title="S'inscrire" onPress={addProfil}></CustomButton>
      </View>
  );
}
```

<div style="display:flex">
<div><img src="amelioration_app.webp" width="300" height="600"></div>
</div>

Pour faire cela j'ai du créer un component **CustomButton** car le component **<Button>** de base n'est pas modifiable. Voici le fichier CustomButton.js : 

```js
const CustomButton = ({title, onPress}) => {
    return (
        <TouchableOpacity style={[styles.button]}>
            <Text style={styles.textButton}>{title}</Text>
        </TouchableOpacity>
    )
};

const styles = StyleSheet.create({
    button: {
        backgroundColor: '#0B109F',
        paddingVertical: 10,
        paddingHorizontal: 20,
        borderRadius: 5,
        marginTop: 40,
    },
    textButton: {
        color: '#fff',
        fontSize: 16,
        textAlign: 'center',
    }
})

export default CustomButton;
```
Le component prend deux paramètres en argument, **title** qui correspond à ce qu'on veut écrire dans le boutton et **onPress** qui correspond à la fonction qui sera déclenchée à chaque appuie sur le bouton. 


## 4.Créer une base de données pour l'app

Pour créer une base de données pour mon application j'ai décidé tout comme Vladimir d'utiliser SQLite qui permet de stocker localement des données. 

Tout d'abord, il faut créer la base de données, pour cela il existe une commande très simple qui est la suivante : 

```js
const db = SQLite.openDatabase("database.db");
```

La méthode ***openDatabase*** prend en argument le nom que l'on veut donner à notre base de données et crée la base de données. Si celle-ci existe déjà elle ne sera pas recréée mais simplement récupérée pour que l'on puisse travailler dessus. 

db est le nom de la constante à appeler lorsqu'on veut utiliser la base de données. 

Après avoir créer notre bdd, créons une table avec une requête SQL : 
```js
useEffect( () => {
    db.transaction(tx => {
        tx.executeSql('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMRAY KEY AUTOINCREMENT, prenom TEXT, nom TEXT');
    });

}, []);
```

Plusieurs choses à dire sur cette partie du code. Une "transaction" est une série d'opérations sur une base de données qui doivent être éxecutées ensemble. Donc **db.transaction(tx)** permet de dire que l'on va réaliser une suite d'opérations sur la base de données db, cette suite d'opérations est appelée ***tx***. Ensuite on précise quelles instructions tx doit réaliser. Ici, ***tx.executeSql('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMRAY KEY AUTOINCREMENT, prenom TEXT, nom TEXT'));*** permet de créer une table **users** avec trois colonnes : id, prenom, nom.

J'aimerais maintenant que quand l'utilisateur clique sur le bouton s'inscrire après avoir rentré son prénom et son nom, ses informations soient enregistrées dans la base de données. 
Pour cela voilà les commandes : 

```js
const [prenom, setPrenom] = React.useState('');
const [nom, setNom] = React.useState('');

const addProfil = () => {
if (prenom !== '' && nom !== '') {
    console.log("prenom et nom ne sont pas vides")
    database.transaction(tx => {
        tx.executeSql(
            "INSERT INTO users (prenom, nom) VALUES (?, ?)",
            [prenom, nom],
            (_, result) => {
                console.log('Profil ajouté');
                setPrenom('');
                setNom('');
            },
            error => {
                console.error('Erreur lors de l\'ajout du profil:', error);
            }
        );
    });
} else {
    console.error('Les valeurs prenom et nom ne doivent pas être vides');
}
};
```

Pour faire simple, lorsqu'on appuie sur le bouton s'inscrire, la fonction addProfil est lancée. 
Si l'utilisateur a rentré un nom et un prénom, tout est ajouté à la base de données. 


## 4.Horodatage

Mercredi 21/02 : 3h visionnage du cours de React Native sur Youtube
Vendredi 23/02 : 3h visionnage du cours de React Native sur Youtube 
Lundi 26/02 : 2h SQLite
Mardi 27/02 : 2h application

