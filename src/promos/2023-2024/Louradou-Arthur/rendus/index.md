---
layout: layout/post.njk

title: "DM 1 Ops"
authors:
   - "Arthur Louradou"

tags: ['DM', 'Ops']
---

<script>

function turnExportOn() {
   document.getElementById("export-button").style.display = "none";

   document.querySelector("header").hidden = true;
   document.querySelector("article").style.marginTop = "40px";
   document.querySelector("footer p").innerHTML = document.querySelector("footer p").innerHTML + " - CSS de <a href=\"https://francoisbrucker.github.io/do-it/\">https://francoisbrucker.github.io/do-it/</a>";
}

</script>

<button id="export-button" onclick="turnExportOn()">Cliquer ici pour créer une page exportable</button>

<br />
{% info %}
[Le sujet du DM](https://francoisbrucker.github.io/cours_informatique/cours/système/linux/scripting/DM/)
{% endinfo %}

## Introduction Comte de Monte Cristo

```bash
curl https://www.gutenberg.org/files/17989/17989-0.txt
```

```bash
curl https://www.gutenberg.org/files/17989/17989-0.txt > monte-cristo-tome1.txt
```

```bash
wc -l monte-cristo-tome1.txt
# puis -w puis -c
```

→ 17067 lignes

→ 121931 mots

→ 784212 caractères !

## En-tête

1. Le roman commence à la 82ème ligne, d’après mon éditeur de texte graphique préféré.
2. Pour avoir cette information à la manière Ops :

    ```bash
    grep "Le 24 février 1815" monte-cristo-tome1.txt -n
    ```

   L’option -n affiche le numéro de ligne :

   `82:Le 24 février 1815, la vigie de Notre-Dame de la Garde signala le`

3. Pour trouver la fin de l’en-tête, on peut chercher ligne contenant la chaîne de caractère `"START OF THE PROJECT GUTENBERG"` avec grep :
4. Voilà donc la commande à exécuter.

    ```bash
    grep "START OF THE PROJECT GUTENBERG" monte-cristo-tome1.txt -n
    ```

   Il s’agit donc de la ligne 24.

5. En ajoutant ceci à la commande précédente, on obtient 24 en sortie :

    ```bash
    | cut -f 1 -d :
    ```

   Il faut lire le manuel de cut pour avoir les options `-d` indiquant le délimiteur et `-f` qui indique le nombre de sections à garder.

6. Avec le numéro 24 ainsi retourné, on peut donner en paramètre à tail avec un + devant la valeur 24. On ajoute ensuite 1 au résultat avec la syntaxe bash $(( . + 1)), qui donne finalement la commande :

    ```bash
    tail -n +$(($(grep "START OF THE PROJECT GUTENBERG" monte-cristo-tome1.txt -n | cut -f 1 -d :) + 1)) monte-cristo-tome1.txt
    ```

   On met ce résultat dans un fichier avec `> roman_brut.txt`. On donne alors cette sortie à `wc` comme au début :

    ```bash
    wc -l roman_brut.txt
    ```

   Et donc :

    - 17043 lignes
    - 124488 mots
    - 783326 caractères

Le man de grep nous indique que l’option `-E` permet d’insérer des expressions régulières à la place d’une simple chaine de caractère.

Ainsi, la commande suivante nous donne le nombre de mentions à “Marseille” ou “Marseillais” qui est de **85** :

```bash
grep -E "Marseille|Marseillais" roman_brut.txt | wc -l
```

Et voici un joli script qui télécharge les 4 tomes, retire l’en-tête (et le pied de page !), puis concatène chacun des tomes dans un seul fichier.

```bash
array=(https://www.gutenberg.org/files/17989/17989-0.txt https://www.gutenberg.org/files/17990/17990-0.txt https://www.gutenberg.org/files/17991/17991-0.txt https://www.gutenberg.org/files/17992/17992-0.txt)

echo "" > monte-cristo-full.txt

for i in {0..3}
do

	curl ${array[$i]} > monte-cristo-reading.txt

	tail -n +$(($(grep "START OF THE PROJECT GUTENBERG" monte-cristo-reading.txt -n | cut -f 1 -d :) + 1)) monte-cristo-reading.txt > monte-cristo-reading2.txt

	head -n +$(($(grep "END OF THE PROJECT GUTENBERG" monte-cristo-reading2.txt -n | cut -f 1 -d :) - 1)) monte-cristo-reading2.txt > monte-cristo-reading.txt

	cat monte-cristo-reading.txt >> monte-cristo-full.txt

done

rm -rf monte-cristo-reading.txt monte-cristo-reading2.txt
```

On a donc 68 994 lignes dans les 4 tomes et 2 966 509 caractères. Soit 42,9 en moyenne au total. Notons que je n’exclue pas ici les lignes blanches qui font baisser cette moyenne.

Sans que je n’explique pourquoi, la commande suivante ne fonctionne pas (sur zsh, du moins) :

```bash
echo $(($(wc -l monte-cristo-full.txt) / $(wc -l monte-cristo-full.txt)))
```

Avec `script.sh` le script défini plus haut, voilà le code à exécuter :

```bash
if [ -e "comte-monte-cristo.txt" ]; then
    echo "Le fichier existe déjà." >&2
    exit 1
else
    ./script.sh
    wc -l comte-monte-cristo.txt | cut -f 4 -d ' ' >&2
fi

exit 0
```

## Poubelle

D’abord, changeons le PATH pour y ajouter ~/.local/bin

```bash
export PATH=$HOME/.local/bin:$PATH
mkdir ~/.local/bin
```

Le script ayant été crée dans un dossier à part, cela explique la dernière commande.

```bash
cd ~/dm
touch poubelle.sh
chmod +x ./poubelle.sh
cp ./poubelle.sh ~/.local/bin/poubelle
```

De cette façon, nous pouvons exécuter le script `poubelle` que voici :

```bash
#!/bin/bash

SHORT=f,r:,l,h
LONG=force,recover:,list,help
OPTS=$(getopt --alternative --name poubelle --options $SHORT --longoptions $LONG -- "$@")

# Traitement des options
eval set -- "$OPTS"

while :
do
  case "$1" in
    -f | --force )
      f=1
      shift
      ;;
    -r | --recover )
      r="$2"
      shift 2
      ;;
    -l | --list )
      l=1
      shift
      ;;
    -h | --help )
      echo "Ceci est un DM d'Ops. Plus d'infos sur https://francoisbrucker.github.io/cours_informatique/cours/syst%C3%A8me/linux/scripting/DM/"
      exit 2
      ;;
    -- )
      shift;
      break
      ;;
    * )
      echo "Option non reconnue: $1"
      exit 1
      ;;
  esac
done

fichier=$1

if [ $r ]; then fichier=$r; fi

# Traitement du chemin par défaut de la poubelle
if [ ! $POUBELLE ]; then
    POUBELLE=~/.config/poubelle
    [ ! -d ~/.config ] && mkdir ~/.config
    [ ! -d ~/.config/poubelle ] &&  mkdir ~/.config/poubelle
fi

if [ "$r" ]; then
    if [ -e $POUBELLE/$fichier ]; then
        echo 'Retablissement du fichier dans le dossier ./'
        mv $POUBELLE/$fichier ./$fichier
    else
        echo 'Fichier introuvable' >&2
    fi
elif [ "$l" ]; then
    echo "Contenu de la poubelle :"
    ls $POUBELLE
elif [ -e $POUBELLE/$fichier ]; then
    echo 'Fichier deja dans la poubelle !' >&2
    if [ "$f" ]; then
        echo 'Deplacement du fichier a la poubelle (en ecrasant son predecesseur)...'
        mv $fichier $POUBELLE
        exit 0
    else
        exit 1
    fi
else
    echo 'Deplacement du fichier a la poubelle...'
    mv $fichier $POUBELLE
fi
```

Ainsi, plusieurs possibilités sont envisagées :

`poubelle fichier` envoie le fichier dans la poubelle si fichier existe et qu’il n’y a pas de fichier appelé de la sorte dans la poubelle.

Sinon, on peut forcer cette démarche en tapant `poubelle fichier -f`.

Il est possible de rétablir un élément de la poubelle avec `poubelle -r fichier`.

Enfin, nous pouvons lister les éléments de la poubelle avec `poubelle -l`.
