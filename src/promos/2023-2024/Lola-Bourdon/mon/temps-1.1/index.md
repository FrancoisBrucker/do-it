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

Pour me former aux langages html et css, je suis partie de zéro. J'ai suivi, comme beaucoup, les cours de https://internetingishard.netlify.app . 
Il est temps de partager mes nouvelles compétences avec Soline pour qu'elle soit capabble de faire son site web basique, sans trop approfondir ses connaissances.

## 1. Prérequis

Pour commencer, Soline aura besoin d'utiliser sur son ordinateur un éditeur de texte tel que Visual Studio Code qu'elle possède déjà, même si elle pourrait en utiliser d'autres. 

Sur VScode, elle devra suivre les étapes suivantes : 
1. Dans l’explorateur de fichier, créer un dossier : "Mon-premier-site-vsc »
3. Ouvrir l'application VsCode et choisir Fichier > ouvrir > fichier puis naviguer jusqu'au dossier "Mon-premier-site-vsc".
4. Accepter de faire confiances aux auteurs, puisque c'est elle
5. Installer l’extension live folder : extension > live folder > installer, qui lui permettra de visualiser son super site web basique
6. Créer un nouveau fichier html "premier-essai.html" un icone <> devrait apparaitre devant le nom du dossier 

## 2. Les bases 
Maintenant que Soline est sur la fenêtre de son fichier html, voici quelques bases :

On commence le fichier html avec &lt;html&gt;&lt;/html&gt;.
Maintenant l’intégralité de la page Web doit être enveloppée dans des balises &lt;html&gt;&lt;/html&gt;. 
&lt;html&gt;ouvre le code et &lt;/html&gt; le ferme.



Entres les &lt;html&gt;&lt;/html&gt; :
- Il ne faut jamais mélanger les imbrications 
- Placer &lt;head&gt;&lt;/head&gt; qui fait référence aux titres, langages CSS, et contenu qui ne seront pas visible directement sur le site 
- On pourra ecrire le titre de la page entre &lt;title&gt;&lt;/title&gt; mais il n'apparaitra pas directement sur le site.
- Maintenant que le head est fermée mais pas le &lt;/html&gt;, on utilisera &lt;body&gt;&lt;/body&gt; qui encadre le contenu visible, rien ne s'affiche  sur la page web lorsqu'il est vide 

Dans &lt;body&gt;&lt;/body&gt; :
- &lt;p&gt;&lt;p&gt; encadre les paragraphes,  
- &lt;h1&gt;&lt;/h1&gt;à &lt;h6&gt;&lt;/h6&gt; sont pour les titres du plus au moins gros 
- &lt;ul&gt;&lt;ul&gt;et &lt;li&gt;&lt;/li&gt; servent pour les listes simple et sont indissociables
- On peut mettre le &lt;p&gt;&lt;p&gt; dans le &lt;li&gt;&lt;li&gt; mais pas dans le &lt;ul&gt;&lt;ul&gt;
- Pour faire apparaitre les crochets sur la page il suffira de les encadrer par &lt ; &gt ; sans espace entre le t et le point virgule

Voyons ce que ces premières informations drendent sur un site web basique:

<img src="code1.png">
<img src="screen1.png">

Il existe également des liste ordonnes qui permettent de numéroter la liste. Cela fonctionne de la même manière mais on remplacera le &lt;ul&gt; par &lt;ol&gt;&lt;ol&gt;.
On utilisra &lt;ol&gt;&lt;ol&gt; pour les recettes, les instructions et même les tables.
On utilisera &lt;ul&gt; pour les inventaires d'articles, les caractéristiques des produits, les comparaisons pour/contre et les menus de navigation.

### Ecrire en Italique ou en gras

Pour écrire en <em>italique</em>, il faut utiliser  la commande &lt;em&gt; <em>  texte </em> &lt;/em&gt; qui n'affecte qu'une partie du texte de la ligne, à la différence de &lt;p&gt;&lt;p&gt;  qui est un élément de niveau bloc.

De la même manière, Pour écrire en <strong>gras</strong>, on utilisera &lt;strong&gt; <strong> texte </strong> &lt;/strong&gt;

On peux également imbriquer un élément gras dans un italique ou vice versa avec :</strong></em> &lt;em&gt;&lt;strong&gt;<em><strong> texte  </strong></em> &lt;/strong&gt;&lt;/em&gt;
      
 
 
 
      <h3> Les élements vides </h3>
Les sauts de ligne et les règles horizontales sont les éléments vides les plus courants. Pour indiquer au navigateur un saut de ligne définitif, il faut utiliser un seul élément &lt;/br&gt; 
C'est utilisé pour les signatures, non pas pour sauter beaucoup de ligne 

Pour les lignes horizontales, on utiliserz simplement &lt;/hr&gt; souvent utile pour une rupture thématique.

</hr>

