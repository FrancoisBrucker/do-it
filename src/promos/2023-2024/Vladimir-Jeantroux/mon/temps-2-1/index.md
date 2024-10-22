---
layout: layout/mon.njk

title: "React Native et back end"
authors:
  - Vladimir Jeantroux

tags:
  - 'temps 2'
  - 'React'
  - 'Développement Web'
---

## Description 

Ce MON vise à enseigner des bases de React Native aux débutants. React Native est un framework open-source de Facebook permettant de développer des applications iOS et Android, grâce aux langages Javascript et React. L'intérêt principal de React Native est qu'il permet de gérer à la fois le front et le back-end, en faisant un outil très polyvalent. 

J'ai choisi ce MON pour pouvoir approfondir et développer du front et back-end sur mon projet 3A, l'application [Killer](https://francoisbrucker.github.io/do-it/projets/2023-2024/Killer/).

{%prerequis%}

Pré-requis :

Des bases de Javascript et de React.js sont requises pour mieux comprendre le contenu de ce MON. Pas de problème pour ceux ayant suivi le cours dev web 0 to hero, mais sinon il y a quelques MON des temps et années précédentes traitant de React.js.

Outils requis : 
- Un IDE (Visual Studio Code, par exemple) pour écrire et éditer le code
- Node.js pour pouvoir exécuter le code et créer un serveur local
- Expo Go sur son téléphone pour éventuellement tester l'application (Ne fonctionne que sur les réseaux wifi privés, sinon il faut télécharger un émulateur Android sur son ordinateur.)

{%endprerequis%}

## La syntaxe de React Native

La syntaxe de React Native repose principalement sur l'utilisation de composants, écrits en JavaScript ou TypeScript, qui représentent des éléments d'interface utilisateur. Ces composants sont créés en utilisant la bibliothèque React et sont structurés de manière modulaire et réutilisable. 

Par exemple, disons que je veux coder une page comportant simplement le texte "Bonjour, ça va ?".

```js
import React from 'react';
import { View, Text,} from 'react-native';

const Page = () => {
  return (
    <View>
      <Text>Bonjour, ça va ?</Text>
    </View>
  );
};

export default Page
```
Ce qu'on a fait, dans l'ordre : on commence tout d'abord par importer les composants dont on a besoin, ici 'React' pour créer les composants, ainsi que les composants 'View', qui est un conteneur de base et 'Text', permettant d'afficher du texte. On crée ensuite le composant "Page" qui ne prend aucun argument, et à l'intérieur on crée un espace d'affichage contenant un élément textuel qui affiche "Bonjour, ça va ?" La dernière ligne permet d'exporter le composant "Page", et signifie qu'il pourra être réutilisé ailleurs.

## Une application simple

Ajoutons maintenant un composant plus complexe : une boîte où l'utilisateur peut taper, ainsi qu'un bouton. 

```js
import React, { useState } from 'react';
import { View, Text, Button, TextInput} from 'react-native';

const App = () => {
  const [userInput, setUserInput] = useState('');

  const handleInputChange = (text) => {
    setUserInput(text);
  };

  const clearInput = () => {
    setUserInput('');
  };

  return (
    <View>
      <Text>Bonjour, ça va ?</Text>
      <TextInput
        placeholder="Entrez votre texte ici"
        onChangeText={handleInputChange}
        value={userInput}
        multiline={true}
      />
      <Text>Vous avez écrit : {userInput}</Text>
      <Button title="Effacer" onPress={clearInput} />
    </View>
  );
};
```

On commence par importer 'useState' qui est un hook qui permet de gérer l'état dans les composants fonctionnels. On initialise ainsi une variable 'userInput' pour stocker le texte saisi par l'utilisateur. 'setUserInput' est une fonction qui permet de mettre à jour cette variable d'état. 

On définit une fonction 'handleInputChange' qui prend le texte entré par l'utilisateur en paramètre et met à jour l'état 'userInput' en utilisant 'setUserInput'.

Dans 'View', on ajoute l'objet 'TextInput', et les changements de texte seront gérés par la fonction 'handleInputChange', et le texte de l'utilisateur sera même réaffiché en bas de la boîte de texte. On a aussi créé un bouton qui lorsqu'il est pressé, efface le texte écrit grâce à la fonction 'clearInput', définie au préalable. 
Cet exemple permet de montrer que React Native permet de gérer des éléments visuels, ainsi que le stockage d'informations.

Notons qu'il est aussi possible d'ajouter une Stylesheet CSS dans un fichier React pour gérer l'apparence de la page.

## Projet : Base de données

Pour aller plus loin, créons une base de données grâce à SQLite. Pour commencer, créons un projet avec la commande suivante : 

```
npx create-expo-app my-app
```

Un nouveau dossier est alors créé, et on va travailler dans le fichier 'App.js', où on va coder. On lance ensuite pour installer les composants nécessaires : 

```
npm install 
```

On pourra par la suite lancer le projet avec 

```
npx expo start
```

On va commencer par créer une manière d'ajouter des entrées à la base de données. 

```js
const addName = () => {
  db.transaction(tx => {
    tx.executeSql('INSERT INTO names (name) values (?)', [currentName],
      (txObj, resultSet) => {
        let existingNames = [...names];
        existingNames.push({ id: resultSet.insertId, name: currentName});
        setNames(existingNames);
        setCurrentName(undefined);
      },
      (txObj, error) => console.log(error)
    );
  });
}
```

Cette fonction sera liée à un espace où l'utilisateur peut taper du texte. La fonction va exécuter une requête SQL pour insérer le nom que l'utilisateur a tapé dans la base de données. Le '?' est remplacé par le nom entré par l'utilisateur. En cas de succès de la requête, une fonction reçoit l'objet de la transaction avec la base de données (le nom de l'objet), et le résultat de la requête, et va ajouter un nouvel objet au tableau des noms. 

```js
const deleteName = (id) => {
  db.transaction(tx => {
    tx.executeSql('DELETE FROM names WHERE id = ?', [id],
      (txObj, resultSet) => {
        if (resultSet.rowsAffected > 0) {
          let existingNames = [...names].filter(name => name.id !== id);
          setNames(existingNames);
        }
      },
      (txObj, error) => console.log(error)
    );
  });
};

const showNames = () => {
return names.map((name, index) => {
  return (
    <View key={index} style={styles.row}>
      <Text>{name.name}</Text>
      <Button title='Delete' onPress={() => deleteName(name.id)} />
    </View>
  );
});
};
```

On ajoute aussi les fonctions pour supprimer une entrée, ainsi que pour afficher les entrées existantes.

```js
return (
    <View style={styles.container}>
      <TextInput value={currentName} placeholder='name' onChangeText={setCurrentName} />
      <Button title="Add Name" onPress={addName} />
      {showNames()}
      <StatusBar style="auto" />
    </View>
  );
```

Ce dernier bloc de code permet de tout afficher : un espace d'entrée du texte, un bouton pour ajouter le nom, ainsi que la liste des noms 'showNames'. Ces éléments permettent de retourner une base de données basique.

Le source code complet peut être trouvé [ici](https://github.com/chelseafarley/expo-sqlite-tutorial). Il comporte des fonctions plus avancées comme l'importation et l'exportation de bases de données, mais je ne me sens pas assez à l'aise en React pour pouvoir l'expliquer dans ce MON. 

## Bibliographie 

- Documentation de React Native https://reactnative.dev/docs/getting-started 
- React Native Course https://www.youtube.com/watch?v=obH0Po_RdWk 
- Local SQLite Database for Expo React Native App with Import and Export Database from Device Files https://www.youtube.com/watch?v=1kSLd9oQX7c
- Installer un émulateur Android (Nécessite un pc puissant) https://docs.expo.dev/workflow/android-studio-emulator/
- Faire tourner un projet Expo sur un émulateur Android https://www.brainstormcreative.co.uk/react-native-expo/how-to-run-an-expo-app-on-android-emulator/
- MON précédents sur React.js de [Thomas Duroy](https://francoisbrucker.github.io/do-it/promos/2022-2023/Duroy-Thomas/mon/MON_3.1/) et [Lucas Rioual](https://francoisbrucker.github.io/do-it/promos/2023-2024/Rioual-Lucas/mon/temps-2.1/).

## Horodatage 

>Mardi 5/12 - Mercredi 6/12 - Jeudi 7/12 : Visionnage de la vidéo React Native Course (2h-2h-1h)
>Jeudi 7/12 : Visionnage de la vidéo Créer une base de données (1h)
>Jeudi 7/12 : Application simple (1h)
>Jeudi 7/12 : Codage de la base de données (2h30)