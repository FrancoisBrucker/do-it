---
layout: layout/mon.njk

title: " Web Front"
authors:
  - Lola Bourdon

date: 2023-09-25

tags: 
  - "temps 1"

résumé: "MON 1 sur le développement d'un site web basique"
---

Mes objectifs pour ce premier MON sont de découvirir les bases des langages HTML et CSS afin d'être capable de coder un site internet simple pour appliquer ce que j'ai appris. Pour rendre cela plus ludique, je vais coder au fur et à mesure de mon apprentissage un site internet très basique décrivant une fiche méthode du langage html pour Soline qui n'a pas suivi la formation html. Par la suite j'améliorerait l'esthétique du site grâce à la découverte de CSS.
 

##  Méthodologie 

Pour me former aux langages html et css, je suis partie de zéro. J'ai suivi, comme beaucoup, les cours de https://internetingishard.netlify.app. 
Il est temps de partager mes nouvelles compétences avec Soline pour qu'elle soit capabble de faire son site web basique, sans trop approfondir ses connaissances.

## 1. Prérequis

Pour commencer, Soline aura besoin d'utiliser sur son ordinateur un éditeur de texte tel que Visual Studio Code qu'elle possède déjà, même si elle pourrait en utiliser d'autres. 

Sur VScode, elle devra suivre les étapes suivantes : 
1. Dans l’explorateur de fichier, créer un dossier : "Mon-premier-site-vsc »
3. Ouvrir l'application VsCode et choisir Fichier > ouvrir > fichier puis naviguer jusqu'au dossier "Mon-premier-site-vsc".
4. Installer l’extension live folder : extension > live folder > installer, qui lui permettra de visualiser son super site web basique
5. Créer un nouveau fichier html "premier-essai.html", un icone <> devrait apparaitre devant le nom du dossier 

## 2. Les bases 
Maintenant que Soline est sur la fenêtre de son fichier html, voici quelques bases :

Un fichier html se commence avec <strong> &lt;html&gt;&lt;/html&gt;. </strong>
Maintenant l’intégralité de la page Web doit être enveloppée dans  &lt;html&gt; tout le code &lt;/html&gt;. 


Entres les <strong> &lt;html&gt;&lt;/html&gt;. </strong>:
- Il ne faut jamais mélanger les imbrications 
- Placer &lt;head&gt;&lt;/head&gt; qui fait référence aux titres, langages CSS, et contenu qui ne seront pas visible directement sur le site 
-  Ecrire le titre de la page entre &lt;title&gt;&lt;/title&gt; même si il n'apparaitra pas directement sur le site.

Maintenant que le &lt;head&gt; est fermée mais pas le &lt;/html&gt;, placer &lt;body&gt;&lt;/body&gt; qui encadre le contenu visible, rien ne s'affiche  sur la page web lorsqu'il est vide 

Dans <strong>&lt;body&gt;&lt;/body&gt;</strong> :
- &lt;p&gt;&lt;p&gt; encadre les paragraphes,  
- &lt;h1&gt;&lt;/h1&gt;à &lt;h6&gt;&lt;/h6&gt; sont pour les titres du plus au moins gros 
- &lt;ul&gt;&lt;/ul&gt;et &lt;li&gt;&lt;/li&gt; servent pour les listes simple et sont indissociables
- On peut mettre le &lt;p&gt;&lt;p&gt; dans le &lt;li&gt;&lt;li&gt; mais pas dans le &lt;ul&gt;&lt;ul&gt;
- Pour faire apparaitre les crochets sur la page il suffira de les encadrer par &lt ; &gt ; sans espace entre le t et le point virgule

Voyons ce que ces premières informations rendent sur un site web basique  pour cela, il suffit de faire clique droit sur le nom du fichier html et de cliquer sur <em> Open with Live Server </em>:

<img src="code1.png">
<img src="screen1.png">

Il existe également des liste ordonnée qui permettent de numéroter la liste. Cela fonctionne de la même manière mais on remplacera le &lt;ul&gt;&lt;/ul&gt;par &lt;ol&gt;&lt;ol&gt;

### Ecrire en Italique, gras ou souligné

Pour écrire en <em>italique</em> :
- Utiliser  la commande &lt;em&gt; <em>  texte </em> &lt;/em&gt; 

Pour écrire en <strong>gras</strong> :
- Utiliser la commande &lt;strong&gt; <strong> texte </strong> &lt;/strong&gt;

Pour écrire en <u>Souligné : </u>
- Utiliser la commande &lt;u&gt; <u> texte </u>&lt;/u&gt; 

On peux également imbriquer un élément gras dans un italique ou vice versa avec :</strong></em> &lt;em&gt;&lt;strong&gt;<em><strong> texte  </strong></em> &lt;/strong&gt;&lt;/em&gt;

Avec ces nouvelles informations, voyons ce que cela peut donner sur donner sur notre super site web :


<img src="screen2.png">
<img src="code2.png">
<img src="code3.png">
 
 
 ### Les Eléments Vides 
Les sauts de ligne et les lignes horizontales sont les éléments vides les plus courants. 
Pour indiquer un <u>saut de ligne définitif,</u> utiliser un seul élément <strong> &lt;/br&gt; </strong>
Pour les lignes horizontales, utiliser <strong>&lt;hr/&gt;</strong>.

###  Images

Pour finir la formation simple et rapide de Soline, parlons de comment insérer une une image sur notre super site web basique.

Pour cela, il faudra ajouter au dossier <em>"Mon-premier-site-vsc"</em>, les images que l'on utiliser, de la manière suivante :

<img src="screen3.png"> 

Partons du principe que soline n'a que des images.png. Il faut utiliser la commande <strong>&lt;img src='/code1.png'/&gt; </strong>

On pourra ajuster la taille avec : <strong> &lt;img src='/screen3.png'  width='200'/&gt; </strong>

Le fin du site final est le suivant :

<img src="dernierscreen.png">
<img src="derniercode.png">

## 3. Amélioration du site 

La partie html du site est terminée mais l'esthétique n'est pas forcément la meilleure. Pour l'améliorer j'ai fait mes premiers pas avec CSS en me basant toujours sur les cours de https://internetingishard.netlify.app. 