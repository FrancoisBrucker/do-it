---
layout: layout/post.njk

title: "Sûrement le seul MON d'info d'Eugénie"
authors:
    - "Eugénie Giraud-Telme"

tags: ['mon']

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

### Compresser des dossiers

### Projet d'application ?