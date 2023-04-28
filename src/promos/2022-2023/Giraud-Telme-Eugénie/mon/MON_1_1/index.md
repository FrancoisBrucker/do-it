---
layout: layout/mon.njk

title: "Sûrement le seul MON d'info d'Eugénie"
authors:
    - "Eugénie Giraud-Telme"

tags :
  - 'automatisation'
  - 'temps 1'

date: 2022-10-07
---
<!-- Début Résumé -->
J'ai choisi de faire le MON appscript parce que ça ne peut qu'être utile.

<!-- fin Résumé -->

Je vais commencer par explorer le site du livre : Automate the boring stuff with Python. Je pourrai ensuite creuser les thématiques qui m'intéressent grâce à Google Apps script et éventuellement trouver une application utile à mettre en place.

Lecture du chapitre 10 : L'organisation de dossiers

### Le module shutil

Pour ce chapitre, une bibliothèque python est utile : shutil.

#### Pour copier fichiers et dossiers

| **Fonction** | **Explication** |
|:---:|:---:|
| shutil.copy(source, destination) | Cela copie un fichier d'un endroit à un autre en spécifiant le chemin de l'endroit à chaque fois. La fonction renvoie le chemin du fichier copié. |
| shutil.copytree(source, destination) | Cela copie un dossier avec tous ses fichiers et sous-dossiers. Même fonctionnement que celle d'avant. |

Exemples :

    import shutil, os
    from pathlib import Path
    p = Path.home()
    shutil.copy(p / 'spam.txt', p / 'some_folder')
        'C:\\Users\\Al\\some_folder\\spam.txt'

    shutil.copy(p / 'eggs.txt', p / 'some_folder/eggs2.txt')
        WindowsPath('C:/Users/Al/some_folder/eggs2.txt')

    shutil.copytree(p / 'spam', p / 'spam_backup')
        WindowsPath('C:/Users/Al/spam_backup')

#### Pour déplacer et renommer des fichiers et des dossiers

| **Fonction** | **Explication** |
|:---:|:---:|
| shutil.move(source, destination) | On peut déplacer un fichier ou un dossier à l'adresse précisée. Soit on l'envoie dans un dossier et il gardera le même nom, soit on l'envoie dans un dossier en précisant le nouveau nom au bout de l'adresse. |

Attention, il faut que le dossier dans lequel on déplace l'objet existe bien, sinon, la fonction va transformer l'objet en un fichier sans extension du nom du présumé dossier. De même, il faut que tout les dossiers cités dans l'adresse de destination existent, sinon python trouvera une erreur. Lorsqu'on déplace un fichier dans un dossier, s'il existe déjà un fichier du même nom dedans, celui-ci sera écrasé.

Exemples :

    import shutil
    shutil.move('C:\\bacon.txt', 'C:\\eggs')
        'C:\\eggs\\bacon.txt'

    shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt')
        'C:\\eggs\\new_bacon.txt'

    shutil.move('C:\\bacon.txt', 'C:\\eggs')   (le dossier eggs n'existe pas)
        'C:\\eggs'

#### Pour effacer définitivement

| **Fonction** | **Explication** |
|:---:|:---:|
| os.unlink(path) | Cela efface le fichier. |
| os.rmdir(path) | Cela efface le dossier vide. |
| shutil.rmtree(path) | Cela efface le dossier et tout ce qu'il contient. |

Il faut faire attention à ces fonctions car une erreur est chère payée. Il vaut mieux faire afficher par la fonction les fichiers qui seraient supprimés avant de réellement l'exécuter. 
Comme ça : 

    import os
    from pathlib import Path
    for filename in Path.home().glob('*.rxt'):
        #os.unlink(filename)
        print(filename)

#### Envoyer à la corbeille

Pour éviter le problème cité à la partie d'avant, il y a une solution.

Il faut installer le module sen2trash en exécutant "pip install --user send2trash" dans un terminal.

| **Fonction** | **Explication** |
|:---:|:---:|
| send2trash.send2trash(path) | Cela envoie l'objet dans la corbeille. |

Avant l'utilisation de la fonction, il faut importer le module.

### Parcourir une arborescence

La fonction os.walk(path) permet de parcourir une arborescence. Elle renvoie 3 éléments : une chaîne de caractères correspondant au nom du dossier actuel, une liste des noms des dossiers contenus dans le dossier actuel et une liste des noms des fichiers contenus dans le dossier actuel.

On peut donc utiliser ce programme :

    import os

    for folderName, subfolders, filenames in os.walk('C:\\delicious'):
        print('The current folder is ' + folderName)

        for subfolder in subfolders:
            print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

        for filename in filenames:
            print('FILE INSIDE ' + folderName + ': '+ filename)

On obtiendra une liste des objets de l'arborescence, comme si on la parcourait par niveau.

### Compresser des dossiers

Ici, nous allons utiliser le module zipfile de Python.

#### Lire des fichiers zip

(Cette partie ne m'intéresse pas trop, j'ajouterai des informations si je me rends compte que je vais en avoir besoin. En résumé, il existe une fonction qui permet d'obtenir l'arborescence contenue dans un fichier zip.)

Fonctions utiles pour la suite : 

Pour créer l'objet zip et pour que Python le comprenne, il faut faire :
    import zipfile, os
    from pathlib import Path
    p = Path.home()
    exampleZip = zipfile.ZipFile(p / 'example.zip')

On utilise ensuite exampleZip en préfixe des fonctions qu'on veut lui appliquer.
Il faut ensuite fermer l'objet avec la fonction close() : exampleZip.close().

#### Extraire de fichiers zip

La fonction extractall() permet d'extraire l'intégralité des objets contenus dans le fichier zip vers le dossier de travail où l'on se trouve. On peut également ajouter le chemin d'accès à un dossier entre les parenthèses, on a deux cas de figure : soit le dossier existe et le contenu du fichier zip sera envoyer dans ce dossier, soit le dossier n'existe pas et il est créé pour mettre le contenu du fichier zip.

Exemple d'utilisation : 

    import zipfile, os
    from pathlib import Path
    p = Path.home()
    exampleZip = zipfile.ZipFile(p / 'example.zip')
    exampleZip.extractall()
    exampleZip.close()

Il existe aussi une fonction pour n'extraire qu'un fichier dans le fichier zip mais je ne pense pas en avoir besoin.

#### Créer et ajouter à un fichier zip

Pour comprendre comment faire, observons ces lignes de code :

    import zipfile
    newZip = zipfile.ZipFile('new.zip', 'w')
    newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
    newZip.close()

On crée l'objet zip en l'ouvrant en mode écriture avec le w en second argument de la fonction ZipFile(). Ensuite, on y ajoute le contenu compressé du fichier spam.zip (la méthode de compressage est précisée en second argument de write()). Ceci est le cas de figure lorsqu'on crée un fichier zip et qu'on le remplit. S'il y avait déjà du contenu dans ce fichier zip, il aurait été remplacé par le fichier spam compressé. Si on souhaite ajouter de l'information dans un fichier zip existant, il faut l'ouvrir en mode ajout (ou append) grâce à la lettre a au lieu du w.

### Projet d'application 

J'ai installé les versions recommandées de Python et de l'éditeur.

J'ai choisi de faire le projet sur la création de fichier zip de backup.

Le principe de la fonction à créer est le suivant :
- La fonction prend en variable un dossier.
- Elle commence par trouver le nom du nouveau fichier zip pour éviter d'écraser les versions précédentes du backup.
- Elle crée le fichier zip.
- Elle parcourt l'arborescence du dossier en ajoutant tous les fichiers du dossier de départ dans le fichier zip.

Après avoir créé la fonction, je l'ai lancée sur un dossier d'un électif (RIS) de l'année dernière pour voir si cela fonctionnait bien. J'ai eu une première erreur dû à des mauvaises indentations. Je l'ai relancé et ça a fonctionné : un fichier zip nommé RIS_1.zip s'est créé. Je l'ai relancé deux fois pour vérifier que le nom s'incrémentait bien, c'était le cas. Dernier test, j'ai effacé le fichier RIS_2.zip en conservant le RIS_3.zip. En relancant la fonction, le programme a bien recréé RIS_2.zip et est passé au RIS_4.zip au coup d'après.

J'ai tenté de modifier légèrement le programme pour voir si j'arrivais à copier dans le fichier zip tous les documents sauf ceux en .pdf.

J'ai ensuite réalisé qu'aucun des fichiers n'apparaissaient dans les dossiers de backup. Je n'ai toujours pas trouvé la solution.