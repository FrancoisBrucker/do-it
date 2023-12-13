---
layout: layout/pok.njk

title: "La Data Science au service de l'Anatomie Pathologique"
authors:
  - Alexandre Beyaert

date: 1971-01-01

tags: 
  - "temps 2"

résumé: Un POK traitant de l'usage de la Data Science au service de l'anatomie Pathologique. En particulier, la création d'un algorithme de classification afin d'aider au diagnostique les médecins dans le risque de récidive du carcinome basocellulaire.
---

{% prerequis %}
**Niveau :** Avancé
**Prérequis :** Bases en Python et en Datasciences (traitement d'image, segmentation, machine learning)
{% endprerequis %}

## Sommaire

1. Introduction
2. Description du projet
3. Analyse préliminaire des données
4. Sprint 2 : algorithmes de Machine Learning
5. Conclusion
6. Bibliographie

## 1. Introduction

Le but de ce projet est d'apporter des solutions informatiques d'analyse de données au service de l'anatomie pathologique. L'objectif est de créer un algorithme de classification afin d'aider au diagnostique les médecins dans le risque de récidive du carcinome basocellulaire.

Cette solution permettrait l'économie d'un temps précieux dans la lecture de lames au microscope afin de détecter les souches plus ou moins atteintes. La science des données doit pouvoir aider à trier ces différentes lames pour ne demander aux médecins qu'une analyse approfondie de certains échantillons.

## 2. Description du projet

### 2.1 Informations générales

**Titre :** Évaluation du risque d’agressivité des carcinomes basocellulaires à partir de multiples jeux de données
**Champ médical	:** Cancérologie Diagnostic Anatomie Pathologique
**Entité de rattachement :**	Service d’Anatomie Pathologiques, Timone, APHM, UMR911, MMG, AMU

### 2.2 Description du projet


L'Anatomie Pathologique (anapath) est une spécialité médicale centrée sur **le diagnostic des maladies à un niveau microscopique, en interprétant des images de tissus et de cellules, notamment dans le contexte de la pathologie tumorale et du cancer.** Les avancées dans la numérisation ouvrent de nouvelles perspectives, permettant potentiellement de se passer des microscopes optiques au profit d'écrans haute résolution. Cette transition vers la numérisation totale offre des opportunités de **développement d'outils basés sur l'analyse d'images et des pipelines de machine learning pour faciliter le diagnostic.**

En plus d'accélérer le processus diagnostique, ces outils peuvent contribuer à générer des données de santé normalisées et reproductibles, représentant un enjeu majeur pour la recherche en cancérologie. Les images microscopiques, souvent multimodales, peuvent être analysées en utilisant des techniques telles que l'immunohistochimie, permettant au pathologiste de visualiser différentes modalités d'information biologique superposées sur une même coupe tissulaire.

La thématique de l'aide au diagnostic et de l'automatisation en pathologie est actuellement compétitive, principalement axée sur l'analyse d'image. Plusieurs projets industriels et commerciaux se concentrent sur cette problématique, bien que peu d'entre eux se consacrent spécifiquement à la dermatopathologie. Ces nouvelles approches rencontrent des défis réglementaires et financiers, notamment liés à l'obtention du marquage CE et au remboursement par les organismes de santé.

En particulier, le carcinome basocellulaire, le cancer de la peau le plus fréquent, offre des images prototypiques et reproductibles au microscope, ce qui pourrait **permettre une automatisation accrue du diagnostic.** Cependant, les projets existants ne se concentrent pas suffisamment sur l'intégration des données existantes (compte-rendus) ni sur la combinaison de multiples jeux de données (clinique, histologique) avec l'analyse d'image pour répondre à des questions cliniques spécifiques, telles que **la prédiction de la récidive tumorale.**

Données : fichiers images, lames de microscopes numérisées, format .ndpi – anonymisées.

### 2.3 Missions et attendus souhaités

Le but de ce POK est de proposer un algorithme fonctionnel permettant de classer les lames cancéreuses et celles non cancéreuses.
Pour se faire :
**- le sprint 1** consistera en la **compréhension** du projet, sa **description** ainsi qu'en **l'analyse préliminaire** des données.
**- le sprint 2** consistera à adopter des méthodes de Machine Learning pour effectuer une **classification**.


## 3. Analyse préliminaire des données

### 3.1 Conversion automatisée des images du format ..ndpi au format .jpg

Les images sur lesquelles je travaille proviennent de microscopes numériques. Elles sont extraites au format .ndpi "NanoZoomer Digital Pathology Image" et sont de très hautes résolutions.

L'échantillon dont je dispose **propose des images allant de 100Mo à 1Go.**

Il est possible de les lire en utilisant le NDPI Viewer "NDP.wiew2" développé par le fabricant japonais d'instruments scientifiques Hamamatsu Photonics K.K..

Ce logiciel est téléchargeable gratuitement sur [le site d'Hamamatsu](https://www.hamamatsu.com/eu/en/product/life-science-and-medical-systems/digital-slide-scanner/U12388-01.html)

Voici son interface :

![NDP Viewer2](NDP_view2.jpg)

Afin de pouvoir utiliser ces images dans un algorithme de machine learning, **il faudrait les convertir dans un format plus propice à la programmation et permettant de réduire leur taille.**

Toutefois, depuis NDP Viewer2, cette conversion ne peut se faire qu'image par image et serait trop chronophage pour convertir des 100aines d'images.

La première problématique de ce POK consiste alors à **automatiser une conversion des images au format .ndpi vers .jpg.**

#### Tentative d'automatisation avec NDPview2

Ayant téléchargé NDPview2, ma première idée consiste alors à créer un algorithme Python convertissant les différents fichiers en faisant appel à ce NDP viewer.

```python
import os
import subprocess

# Chemins des dossiers
input_folder = 'C:\\Test-TER\\DATA-NDPI'
viewer_path = 'C:\\Program Files\\Hamamatsu\\NDP.view 2\\NDPView2.exe'
output_folder = 'C:\\Test-TER\\DATA-JPG'

# Chemin du fichier test
test_file = 'test.ndpi'
test_file_path = os.path.join(input_folder, test_file)

# Génération du chemin de sortie avec le même nom de fichier mais en extension .jpg
output_file_path = os.path.join(output_folder, os.path.splitext(test_file)[0] + '.jpg')

# Commande pour appeler le viewer NDPI et effectuer la conversion
command = [viewer_path, '-i', test_file_path, '-o', output_file_path]

# Exécuter la commande en utilisant subprocess.Popen
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = process.communicate()

# Afficher la sortie et les erreurs
print("Sortie:", output.decode())
print("Erreurs:", error.decode())

print("Conversion pour le fichier de test terminée.")
```
Hélas le programme se contente de lancer le viewer sans effectuer la conversion. Il semblerait donc que le viewer ne puisse servir de façon automatisée mais nécessite des actions manuelles pour effectuer la conversion.

#### Tentative d'automatisation avec OpenSlide

Le programme ci-dessous n'est pas abouti...
Il semble théoriquement possible de convertir les fichiers .ndpi vers .jpg grâce à la bibliothèque Python or en sortie ce programme renvoie une erreur indiquant que la bibliothèque ne peut lire les fichiers .ndpi.

cf [Documentation OpenSlyde Python](https://openslide.org/api/python/)


```python
!pip install openslide-python

!apt-get install openslide-tools
!pip install openslide-python

from openslide import OpenSlide
from PIL import Image

def convert_ndpi_to_jpg(input_path, output_path):
    # Ouvrir le fichier NDPI avec OpenSlide
    ndpi_slide = OpenSlide(input_path)

    # Extraire les dimensions de l'image
    width, height = ndpi_slide.dimensions

    # Lire l'image entière
    image = ndpi_slide.read_region((0, 0), 0, (width, height))

    # Convertir l'image PIL en mode RVB (si elle n'est pas déjà en mode RVB)
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # Enregistrer l'image au format JPG
    image.save(output_path, 'JPEG')

    # Fermer la lecture du fichier NDPI
    ndpi_slide.close()

# Chemin du fichier NDPI d'entrée
input_ndpi_path = 'C:\\Test-TER\\DATA-NDPI\\test.ndpi'

# Dossier de sortie pour les fichiers JPG
output_jpg_folder = 'C:\\Test-TER\\DATA-JPG'

# Construire le chemin de sortie pour le fichier JPG
output_jpg_path = output_jpg_folder + '\\test.jpg'

# Appeler la fonction pour convertir le fichier NDPI en JPG
convert_ndpi_to_jpg(input_ndpi_path, output_jpg_path)

print(f"Conversion terminée. Fichier JPG enregistré à : {output_jpg_path}")
```

### 3.2 Visualisation d'images

Pour commencer, regardons quelques images dont nous disposons.

```python
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Liste des chemins d'accès aux images
image_paths = ['C:\\TER\\visu1.png', 'C:\\TER\\visu3.png', 'C:\\TER\\visu2.png', 'C:\\TER\\visu4.png']

# Créer une figure avec 2x2 sous-graphiques
plt.figure(figsize=(8, 8))

# Boucle pour afficher chaque image dans un sous-graphique
for i, image_path in enumerate(image_paths, 1):
    
    img = mpimg.imread(image_path)
    plt.subplot(2, 2, i)
    plt.imshow(img)
    plt.axis('off')

# Ajuster l'espacement entre les sous-graphiques
plt.tight_layout()

plt.show()
```
![Exemples d'images](Visualisation.jpg)

Ces différentes images sont à l'heure actuelle peu exploitables.
On y remarque beaucoup de bruit, des tâches qui pourraient tromper l'algorithme quant à la détection du carcinome... 

![Annotations](Visualisation_annotee.jpg)
En noir, la zone où se trouve le carcinome.
En rouge, du bruit pour l'algorithme

Il va donc être nécessaire d'effectuer un pré-traitement de ces données pour réaliser la segmentation "zone cancéreuse vs zone non cancéreuse".

### 3.3 Pré-traitement - Segmentation

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Chemin de l'image
image_path = "D:/Master_SID/projet_TER/data/tumeur/9.jpg"

# Lecture de l'image et conversion BGR2RGB
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Aplatissement des pixels, préparation à la segmentation
pixels = image.reshape((-1, 3))
pixels = np.float32(pixels)

# Définition des critères pour l'algorithme k-means
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

# Choix du nombre de clusters
k = 3

# Modèle
_, labels, centers = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

centers = np.uint8(centers)

# Reconstruction de l'image segmentée
segmented_image = centers[labels.flatten()]
segmented_image = segmented_image.reshape(image.shape)


# Chemin de sortie
cv2.imwrite("D:/Master_SID/projet_TER/data/pretraitement_tumeur/9.jpg", cv2.cvtColor(segmented_image, cv2.COLOR_RGB2BGR))

# Affichage

plt.subplot(121), plt.imshow(image), plt.title('Original Image')
plt.subplot(122), plt.imshow(segmented_image), plt.title('Segmented Image')
plt.show()
```
![Image d'origine vs Image segmentée](pretraitement.jpg)

## 4. Sprint 2 : algorithmes de Machine Learning
(Ensuite, une fois la segmentation au point, nous allons pouvoir commencer à faire tourner des algorithmes de ML pour effectuer une classification : "cancer" ou "pas de cancer")

## 5. Conclusion
## 6. Bibliographie