---
layout: layout/mon.njk

title: "Programmes binaires et Compilateurs"
authors:
  - Jean-Baptiste Durand

date: 2023-01-04

tags:
  - 'temps 2'
  - 'Programmes Binaires'
  - 'Compilateur'
  - 'Yacc et Lex'
  - 'C'
---

<!-- début résumé -->
Comment fonctionne le language machine - binaire - et comment créer un compilateur de language informatique.
<!-- fin résumé -->

<h2 id="toc"> Table des matières </h2>

- [Table des matières](#toc)
- [Language Machine](#h1)
  - [Qu'est ce que le language machine ?](#h1-1)
  - [Lire un fichier désassemblé](#h1-2)
- [Compilateur de language](#h2)
  - [Lex](#h2-1)
  - [Yacc](#h2-2)
  - [Mes difficultés pour faire de l'algorithmie avancée](#h2-3)
  - [Solution à ces problèmes](#h2-4)
- [Liens Utiles](#liens)

<h2 id="h1"> Language Machine </h2>

<h3 id="h1-1"> Qu'est ce que le language machine ? </h3>

Le language machine est un **language informatique reconnu par l'ordinateur** et qu'il peut executer directement sans l'aide d'un intermédiaire (pas besoin d'un interpréteur de language).
Par exemple, le C est un language informatique compilé, et Python est un language interprété.

<img src="../Image/differencePyC.jpg" alt="Arbre de calcul" style="height: 400px; margin: 0 auto; border: 0" />

|       | Avantage | Inconvénient |
| ----------- | ----------- | -------- |
| Language Interprété      | Est **cross-platform**, fonctionne pour n'importe quel appareil | Toute personne voulant executer le code doit avoir l'**interpréteur** sur sa machine |
| Language Compilé   | Nécessite d'utiliser le compilateur une **unique fois** | Un fichier compilé est **spécifique à une distribution**, un fichier Linux est différent d'un Windows |

{% info %}
Un language compilé peut être lu, pour comprendre ce que fait un programme avant de l'executer, ce qui peut être une bonne idée si le programme compilé est un virus.
{% endinfo %}

Sur Linux, il est possible de récupérer le code machine d'un fichier compilé grâce à la commande **objdump** (pas disponible par défaut)

``` bash
objdump -d fichierCompilé > languageMachine.txt
```

Il existe aussi un logiciel permettant de décompiler des fichiers : [Ghidra](https://ghidra-sre.org/).
Ce logiciel est disponible sur Linux, Windows et MacOS et a beaucoup plus d'outil permettant de comprendre comment fonctionne le fichier compilé.

Voilà à quoi peut ressembler une partie de code désassemblée. (Ici seulement la partie principal du code)

```
0000000000001149 <main>:
    1149:       f3 0f 1e fa             endbr64 
    114d:       55                      push   %rbp
    114e:       48 89 e5                mov    %rsp,%rbp
    1151:       48 83 ec 10             sub    $0x10,%rsp
    1155:       c7 45 f4 02 00 00 00    movl   $0x2,-0xc(%rbp)
    115c:       c7 45 f8 05 00 00 00    movl   $0x5,-0x8(%rbp)
    1163:       8b 55 f4                mov    -0xc(%rbp),%edx
    1166:       8b 45 f8                mov    -0x8(%rbp),%eax
    1169:       01 d0                   add    %edx,%eax
    116b:       89 45 fc                mov    %eax,-0x4(%rbp)
    116e:       8b 45 fc                mov    -0x4(%rbp),%eax
    1171:       89 c6                   mov    %eax,%esi
    1173:       48 8d 05 8a 0e 00 00    lea    0xe8a(%rip),%rax        # 2004 <_IO_stdin_used+0x4>
    117a:       48 89 c7                mov    %rax,%rdi
    117d:       b8 00 00 00 00          mov    $0x0,%eax
    1182:       e8 c9 fe ff ff          call   1050 <printf@plt>
    1187:       b8 00 00 00 00          mov    $0x0,%eax
    118c:       c9                      leave  
    118d:       c3                      ret
```

<h3 id="h1-2"> Lire un fichier désassemblé </h3>

- La première colonne permet de connaître la **position** (en hexadécimal) **de l'instruction** dans le fichier compilé, est utile pour pouvoir comprendre quelle partie du code est exécutée lorsqu'il y a les fonctions **call** ou **jmp**.
- La 2e colonne est l'**écriture hexadécimale des instructions** à effectuer, est la traduction exacte du code binaire de l’exécutable. Cette partie du code n'est pas vraiment exploitable.
- La 3e colonne est la **traduction fonctionnelle** de ces instructions avec les paramètres associés.

L'exemple précédent est le language machine associé à cette fonction écrite en C.

```c
int main()
{
    int a=2;
    int b=5;
    int c;

    c= a + b;
    printf("%d\n",c);
    return 0;
}
```

Voici quelques fonction qui permettent de comprendre le fonctionnement global du code.

- **mov** et **movl**

Permettent de stocker en mémoire une valeur.

**mov** quand cette valeur était déjà stockée ailleurs

**movl** quand c'est une nouvelle valeur.

- **add**

Permet d'ajouter 2 valeurs

- **call**

Permet d'appeler la fonction située à l'emplacement mémoire associé

<h3 id="h1-3">Registre de mémoire </h3>

Il y a 4 **registres de travail** : *eax*, *ebx*, *ecx* et *edx*, ayant 32 bits chacun.

À ces 4 registres, s'ajoute 4 autres registres :

- *eip*, pointeur d'instruction, il contient le numéro de la ligne en cours d'execution dans le programme.
- *esp*, pointeur de tête de pile
- *ebp*, pointeur de pile
- *flags*, permettant de contenir le résultat d'une opération qui vient d'être exécutée

Dans l'exemple précédent, on peut voir notamment **rax** et **rbp**, ils fonctionnent de la même façon que respectivement **eax** et **ebp**, je ne sais pas quel est la différence entre les 2.

<h2 id="h2"> Compilateur de language </h2>

L'objectif est de créer sont propre language informatique et de créer le compilateur associé.

J'ai utilisé les 2 technologies **yacc** et **lex**, qui permettent de créer de manière basique, un compilateur, en C.

<h3 id="h2-1"> Lex </h3>

{% note %}
Lex est un générateur d’analyseur lexical, c'est à dire qu'il reconnaît les expressions régulières et peut leurs associer des actions.
{% endnote %}

exemple : 

```
[0-9]+          {yylval.num = atoi(yytext); return NUMBER;}
```

**[0-9]** est une expression régulière permettant de reconnaître les caractères '0', '1', '2', '3', '4', '5', '6', '7', '8' et '9'
**+** permet de trouver toutes expression respectant au moins une fois ou plus l'expression juste avant.
**[0-9]+** reconnaît tous les nombres, ayant 1 ou plusieurs chiffres.

Donc l'exemple va reconnaître les nombres et stocker leurs valeurs

<h3 id="h2-2"> Yacc </h3>

{% note %}
Yacc est un générateur d’analyseur syntaxique, c'est à dire qu'il va reconstruire une syntaxe à partir de plusieurs éléments de cette syntaxe.
{% endnote %}

exemple : 

```
Expression:Expression'*'Expression      {$$=$1*$3;}
    |Expression'/'Expression            {$$=$1/$3;}
    |Expression'+'Expression            {$$=$1+$3;}
    |Expression'-'Expression            {$$=$1-$3;}
    |Expression'%'Expression            {$$=$1%$3;}
    |'('Expression')'                   {$$=$2;}
    |'-' Expression %prec UMINUS        {$$=-$2;}
    | NUMBER                            {$$=$1;}
;
```

On définit qu'un calcul peut être l'addition de 2 calculs, la différence entre 2 calculs ou un nombre. Ce qui permet de reconstruire tous les calculs possibles entre des nombres et en faisant des additions et des soustractions.

L'objectif va être de construire un arbre pour faire les opérations.
Par exemple pour le calcul suivant **12+4*(7+2)**, l'arbre suivant sera généré :

<img src="../Image/treeYacc.jpg" alt="Arbre de calcul" style="height: 200px; margin: 0 auto; border: 0" />

Cet arbre est ensuite parcouru en Postfixe, ce qui donne :

**12 4 7 2 + * +**

Cette écriture est très pratique pour calculer, si on utilise une **pile LIFO** (ce qui est le cas dans le language machine). 

{% info %}
Pour lire ce genre de calcul, on lit le calcul de la gauche vers la droite, si on a un nombre, on empile ce nombre, si on a un opérateur, on dépile les 2 dernière valeurs, on effectue le calcul, puis on empile le résultat.
{% endinfo %}

Ici tous les opérateurs se sont retrouvés à la fin, mais on peut tout à fait avoir ce genre d'expression **12 5 - 4 7 2 + * +**

<h3 id="h2-3"> Mes difficultés pour faire de l'algorithmie avancée </h3>

J'avais d'abord envie de faire les fonctions basiques de programmation (*if*, *for*, *while*)

Le principal problème avec YACC, c'est que les feuilles de l'arbre générées sont exécutées avant les racines (c'est lié à la lecture Postfixe de l'arbre).

Voulant créer une fonction *if*, j'ai naïvement écrit dans mon fichier yacc: 

``` 
ifFunction : IF Condition action ELSE action    {if($2){printf("Condition passée \n");}else{printf("Possibilité par défaut \n");};}
| IF Condition action                           {if($2){printf("Condition passée \n");};}
```

et en executant une fonction *if* :

```
if 1>0 {print(True);} else print(False);
```

J'obtiens comme résultat :
```
Booleen : 1
Booleen : 0
Condition passée
```

Les deux actions - dans le cas où la condition est vraie ou fausse - sont exécutées.

Il n'est pas possible de bloquer l'execution d'une action, ce qui est embêtant pour une fonction if.

Ensuite, il n'est pas possible d'aller à un endroit précis du code, rendant les boucles *for* et *while* impossible.

Dans le language machine, une boucle while s'execute de la manière suivante : 

```
0   condition
1   jmp 4
2   code de la boucle
3   jmp 0
4   code après la boucle
```

Il est donc primordial de pouvoir sauter d'une ligne d'exécution à une autre pour faire des boucles.

<h3 id="h2-4">Solution à ces problèmes </h3>

Il n'est pas impossible de contourner ces problèmes, pour cela il faut manuellement reconstruire les lignes d'executions grace au parseur de yacc et ensuite executer le code.
Voici un exemple d'une personne ayant réalisé cela : [compiler if and while](https://github.com/chetnasureka/if-else-and-while-compiler-for-C-in-Yacc/blob/master/parser.y)


<h2 id="liens">Liens Utiles </h2>

**Language machine**

[Cours architecture des ordinateurs](https://igm.univ-mlv.fr/~giraudo/Old/Enseignements/2016-2017/AO/Cours_impr_4.pdf)

[Cours d'assembleur](https://docplayer.fr/12446949-Assembleur-x86-p-ezequel.html)

**Désassembleur**

[Ghidra](https://ghidra-sre.org/)

[Documentation objdump](https://man7.org/linux/man-pages/man1/objdump.1.html)

**Yacc et Lex**

[Cours 1](https://pageperso.lis-lab.fr/alexis.nasr/Ens/Compilation/cmX_lex_yacc.pdf)

[Cours 2](https://lafibre.info/images/doc/201705_lex_yacc_tutorial.pdf)

[Header Yacc](https://www.ibm.com/docs/en/aix/7.2?topic=information-yacc-grammar-file-declarations)

[Complément Header Yacc](https://www.ibm.com/docs/en/zos/2.4.0?topic=section-precedence-associativity)

[Exemple avec boucle if et while](https://github.com/chetnasureka/if-else-and-while-compiler-for-C-in-Yacc/blob/master/parser.y)

**Mon projet**

[GitHub](https://github.com/Jean-Baptiste-DP/Compiler-Yacc-Lex)
