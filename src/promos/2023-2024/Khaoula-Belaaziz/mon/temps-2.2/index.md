---
layout: layout/mon.njk

title: "Animations avec React Native & Utilisation d'Android Emulator"
authors:
  - Khaoula BELAAZIZ

date: 2023-11-22
tags: 
  - "temps 2"

résumé: .
---


Ce MON vient pour compléter mon MON 2-1 à propos des bases de REACT NATIVE : [Apprendre et Maîtriser React Native : Guide pour Débutants](http://localhost:8080/promos/2023-2024/Khaoula-Belaaziz/mon/temps-2.1/). 
Mon objectif pour ce MON est d'apprendre à faire des animations et des tranformation avec react native pour notre projet 3A [KILLER](https://francoisbrucker.github.io/do-it/projets/2023-2024/Killer/)

# Fondamentaux des Animations dans React Native

### Types d'animations :

**Transitions** : Changements doux d'un état à un autre.
**Transformations** : Changement de propriétés comme la taille, la position, la rotation.
**Animations basées sur les gestes** : Répondre aux interactions de l'utilisateur.

### Outils et bibliothèques d'animation
#### Animated API de React Native :
Une bibliothèque intégrée pour réaliser des animations de base, fournissant une grande variété de composants et de méthodes animables.

{% raw %}
```js
import { Animated } from 'react-native';
```
{% endraw %}

#### Lottie : [LottieFiles](https://lottiefiles.com/search?q=eliminated&category=animations) 
Pour intégrer des animations vectorielles de haute qualité conçues avec Adobe After Effects.
{% raw %}
```js
import LottieView from 'lottie-react-native';
```
{% endraw %}

#### React Native Reanimated :
Une bibliothèque plus avancée pour des animations complexes qui nécessitent des interactions plus fluides et performantes.
{% raw %}
```js
import Animated from 'react-native-reanimated';
```
{% endraw %}

## Création d'Animations Simples

### Interpolation :
L'interpolation permet de transformer une valeur d'entrée en une nouvelle valeur
de sortie, généralement dans un but d'animation.
{% raw %}
```js
const value = useRef(new Animated.Value(0)).current; // Initialisation d'une valeur animée

// Interpolation de cette valeur
const opacity = value.interpolate({
  inputRange: [0, 1],
  outputRange: [0, 1],
});

// Début de l'animation
Animated.timing(value, {
  toValue: 1,
  duration: 1000,
  useNativeDriver: true, // Utilisation du driver natif pour de meilleures performances
}).start();

```
{% endraw %}
Dans cet exemple, *value* passe de 0 à 1 en 1000 millisecondes, ce qui entraîne un changement d'opacité de complètement transparent à complètement opaque.

### Animated.View :
**Animated.View** est un composant qui peut être animé, généralement utilisé pour envelopper tout élément qu'on souhaite animer.
{% raw %}
```js
<Animated.View style={{ opacity }}>
  {/* Le contenu de la vue s'effacera progressivement */}
</Animated.View>

```
{% endraw %}

### Animated.Text:
De même, **Animated.Text** permet d'animer les propriétés d'un élément texte.
{% raw %}
```js
<Animated.Text style={{ opacity }}>
  Je m'estompe !
</Animated.Text>

```
{% endraw %}

### Exemples

#### Animation de **fade-in/fade-out** :
On utilise l'opacité pour faire apparaître ou disparaître un élément progressivement.
{% raw %}
```js
// Animation de fade-in
Animated.timing(value, {
  toValue: 1,
  duration: 2000,
  useNativeDriver: true,
}).start();

// Animation de fade-out
Animated.timing(value, {
  toValue: 0,
  duration: 2000,
  useNativeDriver: true,
}).start();
```
{% endraw %}

#### Translation, rotation, et échelle :
Animer la position, la rotation et la taille des éléments.
{% raw %}
```js
// Exemple de translation
const translateY = value.interpolate({
  inputRange: [0, 1],
  outputRange: [0, 100], // Déplacer de 100 pixels vers le bas
});

// Exemple de rotation
const rotate = value.interpolate({
  inputRange: [0, 1],
  outputRange: ['0deg', '360deg'], // Rotation d'un tour complet
});

// Exemple d'échelle
const scale = value.interpolate({
  inputRange: [0, 1],
  outputRange: [1, 2], // Doubler la taille
});

// Application dans le style d'un Animated.View
<Animated.View
  style={{
    transform: [
      { translateY },
      { rotate },
      { scale },
    ],
  }}
>
  {/* Contenu à animer */}
</Animated.View>
```
{% endraw %}


# Android Emulator
J'avais besoin d'installer Android Emulator car je n'ai pas pu lancer la simulation du projet 3A avec n'importe quel réseau wifi, et vue que je ne peux pas coder sans voir la simulation vertuelle de mon travail, j'ai dû chercher un moyen pour visualiser mon travail sans passer par l'application Expo Go sur mon smartphone.
## Définition
 L'émulateur Android est une composante du SDK Android qui permet de simuler un appareil Android sur un ordinateur, ce qui  permet de tester les applications dans un environnement virtuel Android sans avoir besoin d'un appareil physique. 

## Installation et configuration de l'émulateur Android
### Installez Android Studio :

Téléchargez et installez Android Studio depuis le site officiel d'[ANDROID STUDIO](https://developer.android.com/studio) .
Durant l'installation, assurez-vous d'inclure le Android Virtual Device (AVD) qui est l'outil pour gérer les émulateurs.

### Configurez un appareil virtuel :

1. Lancez Android Studio.
2. Ouvrez l'AVD Manager via Tools > AVD Manager.
3. Cliquez sur Create Virtual Device et choisissez un appareil dans la liste qui correspond aux spécifications que vous souhaitez émuler.
4. Sélectionnez une image système pour votre émulateur, comme une version récente de l'API Android. Téléchargez l'image si nécessaire.
5. Terminez la configuration de l'appareil virtuel et lance

<div style="display: flex; justify-content: space-around;">
  <img src="android studio.webp" alt="android emulaor" style="width: 100%; margin-right: 2%;">
</div>

## Bibliographie 
{% prerequis "**Références**" %}
- React native :Animated **Tout au long de la phase d'apprentissage** : (https://reactnative.dev/docs/animated)
- React native modal animation popup example with overlay | Blurry background color and style **Temps estimé de la vidéo avec application du contenu = 1h30**, **Niveau débutant**  : (https://youtu.be/ccAilrI0IxA?si=ndYD4z5r8SEe5I9g)
- Learn React Native Gestures and Animations - Tutorial **Temps estimé en essayant d'adapter le principe au projet 3A = 3h**, , **Niveau intermédiaire**: (https://youtu.be/wEVjaXK4sYQ?si=tmumKh0qL8MvG8ad)
- React Native Animated Splash Screen | Transform Your App's First Impression Tutorial 2023 **Temps estimé en essayant d'adapter le principe au projet 3A = 2h**, , **Niveau intermédiaire**: (https://youtu.be/OnsF0vP6iyE?si=o6HHphBnK45Vs9re)
{% endprerequis %}
{%info "**Pour l'installation de Android Emulator**"%}
**Temps estimé de cette partie, avec les bugs = 3h**, réalisé le 14/01/2024 de 14h à 17h.
-	Install Android Emulator for React Native Expo - Windows PC **Temps estimé de la vidéo = 15min**: (https://youtu.be/ZGIU5aIRi9M?si=lZBQPYtbrDL7HwRy) 
-	Setting up a React Native Expo App and Android Studio | 1  **Temps estimé de la vidéo = 5min**: (https://youtu.be/WkXrDvImVXc?si=K1uNJCQb-bjeFm_Q) 
-	React Native CLI and Android Emulator in Windows  **Temps estimé de la vidéo = 17min**: (https://youtu.be/RF7zwYIrlds?si=WiUZ2-3KNyw7ruOd) 
- How To Run React Native Android Emulator On Android Studio  **Temps estimé de la vidéo = 3min**: (https://youtu.be/43E9FDjTJBM?si=12QzwKXsEA5gylXm) 
- How To Setup & Run React Native App on Android Emulator from Terminal and edit In Visual Studio Code  **Temps estimé de la vidéo = 15min**: (https://youtu.be/8ejuHsaXiwU?si=aFJ6zRkJ2mSj_5Ma) 
{% endinfo %}

