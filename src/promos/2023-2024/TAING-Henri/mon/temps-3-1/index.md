---
layout: layout/mon.njk

title: "Faire du clean code et du back avec Python Flask"
authors:
  - TAING Henri

date: 2024-02-07

tags:
  - "temps 3"
  - Bonnes pratiques
  - HTML
  - CSS
  - JS
  - Python
  - Flask

résumé: Quoi ? Il y a des conventions pour la manière d'écrire le code ? Une convention par langage en plus ?! Mon dieu, il est temps de nettoyer tout ce code sale et de rénover le site du projet 3A ! (Et aussi le moment d'apprendre de faire du back) 


---

{%prerequis 'MON débutant'%}
Savoir lire du code
{%endprerequis%}

---

## Table des matières

1. [Introduction](#section-1)
2. [PEP 8 pour Python et Google HTML/CSS Style Guide et Google JavaScript Style Guide](#section-2)
3. [Découverte et apprentissage de Flask](#section-3)
4. [Conclusion](#section-4)
5. [Sources et horodateur](#section-5) 

## 1. Introduction <a id="section-1"></a>

Cherchant un poste à l'étranger en IT pour mon premier, mes choix sont assez restreints au vu de mes compétences techniques limitées. 
Pour autant, ce n'est pas une raison de ne pas les valoriser en mettant en avant les projets effectués à l'école et sur mon temps libre, avec un lien github par exemple qui donne sur du clean code.
Dans ce MON, vous verrez les principales conventions utilisées pour rédiger du code et moi, je prendrai cette occasion pour intégrer tout le code que j'ai écrit et le code écrit pour le back par Cassandra.

## 2. PEP 8 pour Python et Google HTML/CSS Style Guide et Google JavaScript Style Guide <a id="section-2"></a>

Le but de ses conventions est définir des règles de format et de style pour le code afin de promouvoir la collaboration et la compréhension. L'idée est d'écrire du code qui soit lisible et consistent pour faire en sorte que sa lecture ne soit pas une souffrance visuelle en plus d'intellectuelle. 
Ces guides sont mis à jour régulièrement pour suivre l'évolution de la programmation. Et je vais de ce pas les appliquer à tous les projets que je compte mettre sur GitHub, commençant par le projet 3A. 

Les principaux points relèvent de :
- l'indentation, par exemple, en Python, il faut faire en sorte soit de s'aligner sur le délimiteur ouvert (parenthèse, strophe, crochet) ou d'ajouter 4 espaces pour séparer les arguments du reste ou en alignant les autres lignes par rapport à la première. Et on va préférer les espaces (avec la touche espace) que les "tabs",

{% details "Exemple calqué sur celui du guide" %}

```
#  Aligné avec le délimiteur ouvert.
f = drole(v1, v2,
          v3, v4)

#  Ajout de 4 espaces (crée un autre niveau d'indentation) pour dinstinguer les arguments du reste.
def fonction(
        a1, a2, a3,
        a4):
    print(a1)

#  "S'aligner sur la première ligne" ou encore s'aligner sur "hanging indent"".
fonction = f(
         b1, b2,
         b3, b4)

```

{% enddetails %}

- le nombre de caractères par ligne, en Python, on conseillera 79 caractères, pour JavaScript 80, 
- les espaces dans le code, on évitera les espaces inutiles du genre, 

{% details "Un autre exemple calqué sur celui du guide" %}

```
#  Ok.
petitdej(jambon[1], {fromage: 2})

#  Ah nan.
petitdej( jambon[ 1 ], { fromage: 2 } )
```

{% enddetails %}

- les commentaires dans le code, il faut que ce soient des phrases complètes, explicites et compréhensibles avec une majuscule au début et utilisés si et seulement si ils aident à la compréhension du code
- les noms des variables, fonctions, etc, par exemple, ne jamais utiliser "l", "O", qui peuvent être confondus avec "1" et "0", écrire le nom des variables en miniscules, etc. 
- des recommandations générales du type : 
{% details "Autres exemples calqués sur celui du guide" %}

```
#  Ok:
def f(x): return 2*x

#  Ah nan, on évite lambda !:
f = lambda x: 2*x

#  Ok:
if booleen:

# Ah nan, le booleen donne déjà l'information du True ou False:
if booleen == True:

```

{% enddetails %}


## 3. Découverte et apprentissage de Flask <a id="section-3"></a>

J'apprends mieux en faisant et sous pression. 
Donc, j'ai décidé de m'inscrire à un hackathon en ligne, "Social Impact Hackathon & Southend Tech". 

En me basant sur la formation [Formation DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3-fr#etape-1-installation-de-flask) conseillée par @Samy Diafat, mon ami ChatGPT, mes deux neurones et mon coéquipier, un professeur à la retraite, j'étais prêt à me lancer dans cette semaine de hackathon.

En bref, ce que j'ai appris dans le stress et le doute : 

**Créer une application Flask**

```
from flask import Flask
app = Flask(__name__)
if __name__ == '__main__':
    app.run(debug=True)

```

**Créer l'architecture qui va avec**

Flask a son architecture propre, c'est-à-dire que dans le dossier du projet, il y a app.py qui va être le pivot du back-end (là où on va mettre les routes, etc.), plusieurs dossiers, **static** pour les éléments statiques comme les fichiers CSS ou des images, **templates** pour les vues (ce qui va être affiché) ici en HTML, **instance** et **migrations** qui se créeront avec la base de données.

**Créer des routes pour que l'application renvoie les vues pour l'utilisateur**

```
from flask import Flask, render_template

@app.route('/register')  
def register():
    return render_template('register.html')

```

**Lancer l'application**

```
Dans le terminal :
python app.py

```

**Relier à une base de données avec SQLAlchemy**

```
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

Dans le terminal :
python -m flask db init
                
```

**Créer des users grâce à une classe**

```

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    feel = db.Column(db.Integer, default=None)
    day = db.Column(db.Integer, default=None)
    health = db.Column(db.Enum(HealthStatus), default=None)
    district = db.Column(db.Enum(District), default=None)  

    __table_args__ = (
        db.CheckConstraint('feel >= 1 AND feel <= 5', name='check_feel_range'),
        db.CheckConstraint('day >= 1 AND day <= 5', name='check_day_range'),
    )
  
```

**Mettre à jour la base de données avec Flask (on peut aussi passer par DB Browser pour visualiser et modifier la base de données)**

```
from flask_migrate import Migrate 

migrate = Migrate(app, db)

Dans le terminal :
python -m flask db migrate
python -m flask db upgrade

```

**La méthode POST pour les inputs**

```
from sqlalchemy.exc import IntegrityError

@app.route('/process_login', methods=['POST'])
def process_login():
    try:
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['username'] = username  
            return redirect(url_for('inputs'))
    except IntegrityError:
        pass
    return render_template('login.html', error='Invalid credentials. Please try again.')

```


## 4. Conclusion <a id="section-4"></a>

J'aurais bien voulu plonger plus dans Bootstrap que j'ai effleuré rapidement pour faire mes pages de login/register, mais, au moins, je peux maintenant dire que je suis le développeur full-stack le plus débutant qu'il soit. 
To-do-list avant de quitter Centrale : Faire un hackathon [X], Être full-stack [X].

## 5. Sources et horodateur <a id="section-5"></a>

[PEP 8 - Style pour Python](https://peps.python.org/pep-0008/#fn-hi)
[Google JavaScript Style Guide](https://google.github.io/styleguide/jsguide.html)
[Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html)
[Formation DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3-fr#etape-1-installation-de-flask)
[L'application que j'ai créé durant le hackathon](https://github.com/henritaing/social_tracker)

> **Horodateur** : 
> Mercredi 07/02 : 2h (Lecture des conventions et nettoyage de mon MON d'analyse de données)
> Samedi 18/02 : 3h (Bases avec la formation DigitalOcean et création de l'architecture, des routes et initialisation de la base de données avec la création d'users)
> Dimanche 19/02 : 4h (Création de la logique pour gérer les users, l'inscription, la connexion puis l'extraction de ses données pour les analyser et les visualiser)
> Lundi 20/02 : 1h (Retour d'expérience)