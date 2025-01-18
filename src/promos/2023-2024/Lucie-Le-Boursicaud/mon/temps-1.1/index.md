---
layout: layout/mon.njk

title: "MON 1 : Initiation à C++"
authors:
  - Lucie Le Boursicaud

date: 1970-09-01

tags: 
  - "temps 1"
  - "Informatique"
  - "Langage C++"
  - "Apprentissage d'un langage"

résumé: "Dans ce MON l'objectif est de découvrir un nouveau langage informatique dans lequel je n'ai aucune base. A la fin des 10h de cours j'espère savoir coder de petits algorithmes simples en C++."
---

{%prerequis 'Niveau débutant'%} 
Prérequis : Savoir ce qu'est un langage orienté objet. 
{%endprerequis%}

## Sommaire

1. Présentation du langage
2. Syntaxe du C++
3. Premiers algorithmes
4. Orientation objet

## 1.Présentation du langage
Le langage C++ est apparu dans les années 90 et il est aujourd'hui devenu un langage très utilisés et indispensable pour certains programmeur. Son grand atout est sa fonctionalité de classe permettant d'utiliser la programmation object comme en JAVA. Sa rapidité, sa puissance ainsi que sa très bonne gestion de la mémoire font de lui un langage incontournable. Nous allons découvrir ensemble les bases de ce langage.

##### Documents et outils utilisés
[La programmation en C++](http://math.univ-lyon1.fr/~omarguin/programmation/C++Polycop1.pdf)
[La programmation objet en C++](http://math.univ-lyon1.fr/~omarguin/programmation/C++Polycop2.pdf)
[Exercices de programmation sur CodeSignal](https://app.codesignal.com/)


## 2. Syntaxe du C++
#### Type de variable 
Comme d'autres langages le C++ possède plusieurs type de variables :  
+ vide : *void*  - aucune voriable ne peut être de ce type on verra son utilité plus tard
+ entier : *char* - petit entier de -128 à 127 
          *short* - grand entier de -32768  à 32767
          *long* - très grand entier 
          *int* - coïncide avec short ou long en fonction de l'initialisation 
+ réels : *float* - précision de 7 chiffres
          *double* - précision de 15 chiffres 
          *long double* - précision de 18 chiffres

Parfois on pourra rencontré le type ***unsigned*** , il s'agit d'un entier dit "non signé".

#### Déclarer une variable 
Il est nécessaire de déclarer une variable avant de devoir l'utiliser en C++.
Pour déclarer une variable on utilise la syntaxe suivante : *type liste_de_variables*.
Exemples :
```html
 int a, b, c;    // déclare trois entiers a,b et c
 const float Taille = 1.67;  // déclare une constante de type float
 const Nom = 'Lucie'; // déclare une constante littérale
```
#### Les différents opérateurs
+ "+" : addition
+ "-" : soustraction
+ "*" : multiplication
+ "/" : donne le quotient (entier si il s'agit de deux entiers)
+ "%" : donne le reste modulo entre deux entiers
Exemples :
```html
 20.0 / 3.2    donnera  6.25
 15 / 8       donnera 1
 15 % 8       donnera 7
```
Comme d'autres langage l'utilisation de ++ ou de -- permet d'incrémenter ou de décrémenter une variable.

#### Instructions
Pour donner des instruction en C++ on peut soit faire une instruction par ligne comme ceci : 
```html
int a = 4;
a++; 
```
Ou utiliser des instruction-bloc comme ceci :
```html
{
  int a = 4;
  a++ ;
}
```
Si je déclare une variable dans un bloc alors elle ne pourra pas être utilisée en dehors de ce bloc., il s'agit d'une variable *locale*.
Il est interdit de donner le même nom à deux variables distinctes au sein d'un même bloc. 
Si je déclare une variable en dehors d'un bloc alors c'est une variable dite *globale*.

#### Fonctions 
##### Elements de bases
Une fonction est définie par 4 éléments distincts : 
+ son nom 
+ le type de valeur qu'elle renvoie
+ les paramètres dont elle a besoin
+ le corps de la fonction

Toute fonction doit être définie avant de pouvoir être utilisée.
Pour déclarer une fonction on utilise cette syntaxe : type nom(liste_des_paramètres).
Exemples :
```html
double Distance(double x1, double y1, double x2, double y2);
char Concatenation(char mot1, char mot2);
void AfficherUnNombreXFois(int nombre, int x);
```
On voit ici l'utilité de <strong>*void*</strong> rencontré plus tôt. La dernière fonction n'a pour vocation que d'afficher et ne return pas de valeur.

##### Définir une fonction
Pour déclarer une fonction voici la syntaxe : 
type nom_de_la_fonction(tous_les_paramètres) 
{
  corps de la fonction
}

Exemples :
```html
double Moyenne(double x, double y){
  return (x + y) / 2.0
}
```
Lorsque l'on utilise *return* cela interrompt l'exécution de la fonction.

##### Utiliser une fonction
Une fois ma fonction déclarée je peux appeler ma fonction pour l'utiliser sur différentes valeurs. 
```html
double n=3;
double m=4;
double resultat = Moyenne(n,m);
```
Alors la variable *resultat* récupérera la valeur de la moyenne de 3 et 4 soit 3.5.

##### Les différentes instructions
Comme d'autres langages on retrouve les instructions de bases *if*, *while*, *do*, *for*, et aussi *switch* qui permet de dissocier différents cas pour lequels on ne veut pas lancer la même instruction.

##### Compléments
Il existe des expressions particulière en C++. 
  + L'expression virgule 
Elle s'utilise de la forme suivante : *expression 1* , *expression 2*.
D'abord, l'*expression 1* est évaluée mais sa valeur n'est pas gardée en mémoire.
Ensuite l'*expression 2* est évaluée et donne sa valeur est l'*expression 1*.
Cette utilisation est utile dans le cas où l'*expression 1* a un effet de bord.

  + L'expression conditionnelle
Elle s'utilise de la forme suivante : *expression 1* ? *expression 2* : *expression 3*.
D'abord l'*expression 1* est évaluée. Ensuite, si elle est non nulle, l'*expression 2* est évaluée et donne sa valeur à l'expression conditionnelle. Sinon, l'*expression 3* est évaluée et donne sa valeur à l'expression conditionnelle. 

Plusieurs fonctions utiles sont aussi à connaitre telles que : *floor*, *fabs*, *sqrt*, *pow* ainsi que les fonctions trigo.


+ Les énumérations
Les énumérations sont des listes de noms représentant les valeurs entières successives 0,1,2,...
On peut l'a défini de la façon suivante : <strong>enum</strong> *nom* { *liste_de_noms* }
Exemple :
```html
enum Chiffres { un, deux, trois, quatre, cinq, six, sept, huit, neuf}
enum Peinture { huile, gouache, acrylique, aquarelle}
```
Alors on obtiendra la déclaration implicite des constantes entières : 
```html
const int huile=0;
const int gouache=1;
const int acrylique=2;
...
```
Et attribue à ces constantes un type appelé Peinture.

+ Tableaux
Un tableau est une collection indicée de variables de même type.
On peut le définir de la façon suivante : *type* *nom* [*taille*] où 
*type* est le type des éléments du tableau 
*nom* est le nom du tableau
*taille* est une constante entière égale au nmbre d'éléments du tableau.

Exemples:
```html
int taille[2];       //tableau de deux entiers pour indiquer sa taille
double tempsdouche[7];     //tableau de 7 réels pour indiquer le nombre de minutes passées sous la douche
Peinture collection[10];    //tableau de 10 peintures
```
> Soit i une expression entière, on note Peinture[i] l'élement d'indice i du tableau *Peinture*.

+ Chaînes de caractères
En C++, une chaine de caractères est en fait un tableau de caractères avec un caractère nul '\0' en fin de chaîne.
Exemple :
```html
char couleur[8]; // on a 7 caractères utiles
strcpy(couleur, "rouge")
```
Les chaines de caractères peuvent être affichées grâce aux habituels *cin* et *cout*. De nombreuses fonctions de bases utiles pour les chaines de caractères sont déjà pré-définies en C++.

## 3.Premiers algorithmes
Dans cette partie je vais m'exercer à coder de petits algorithmes simples avec ce que j'ai appris du langage. 

#### Algorithme de calcul de distance entre deux points 
```html
double Distance(x1,y1,x2,y2){
  double dx,dy;
  dx = x1-x2;
  dy = y1-y2;
  return sqrt(dx*dx+dy*dy);
}
```

#### Algorithme de calcul du maximum entre deux entiers
```html
int Max(int a, int b)
{
if ((a <= b))
return b;
return a;
}
```

#### Algorithme de calcul du maximum entre une liste d'entiers
```html
int main()
{
    int arr[] = { 2, 7, 9, -1, 0, 3, 6, 21, 8, -12};
 
    int max = INT_MIN;
    for (int i: arr)
    {
        if (i > max) {
            max = i;
        }
    }
    return max;
}
```

#### Entrainement sur CodeSignal
Suite à cela j'ai repris le mode arcade de CodeSignal depuis le début mais en codant en C++ cette fois-ci. CodeSignal est une plateforme qui permet d'évaluer ses compétences en développement. Elle propose une variété de défis de programmations qui peuvent résolu en utilisant le langage de son choix.


## 4. Orientation Objet
#### Définitions
En informatique un objet est défini comme ce qui suit : 
*"Un objet est une structure informatique regroupant :* 
*- des variables, caractérisant l'état de l'objet,*
*- des fonctions, caractérisant le comportement de l'objet."*

Tout objet appartient à une classe, on dira que l'objet est une *instance* de cette classe.
Ainsi avant de décrire un objet il est important de décrire la classe à laquelle il appartienne. 

#### Stratégie D.D.U 
Lorsque l'on souhaite programmer une classe, on passe par trois phases :
+ Déclaration
+ Définition
+ Utilisation

##### Déclaration 
Cette partie se traite dans un fichier .h qui se présente sous cette forme :
```html
class Classe
{
  public : 
    *déclaration*
  private :
    *déclaration*
}
```

##### Définition
Cette partie se traite dans un fichier .cpp qui contient les définitions des fonctions de la classe.

##### Utilisation
Cette partie se traite aussi dans un fichier .cpp dans lequel on pourra utilisé notre classe.

Ainsi pour chaque classe on aura un fichier .h avec sa déclaration et un fichier .cpp contenant sa définition.

<div><img src="schema objet.webp"></div>

#### Comment créé un programme ? 
On procéde en trois étape : 
+ Créer les fichiers sources en .h et .cpp.
+ Compiler les fichieres .cpp ce qui crée deux fichiers objets.
+ Editer les liens entre les fichiers objets pour obtenir un fichier exécutable en .exe.
  
Pour ce faire, sur Microsoft, il suffit de créer les fichiers sources, de les ajouter dans un projet et de lancer la commande <strong>build</strong>. Les phase 2 et 3 se feront alors automatiquement.

#### Conclusion
Pendant ce MON j'ai pu découvrir ce nouveau langage qui m'est désormais bien moins inconnu. J'ai pu le pratiquer à l'aide de CodeSignal sur des algorithmes plutôt simple. J'ai appris comment l'utiliser en orientation objet avec un exemple du cours que j'ai consulté (voir dans les ressources). En 10h il est compliqué de maîtriser un nouveau langage mais le but ici était de le découvvrir et d'en comprendre les bases.


