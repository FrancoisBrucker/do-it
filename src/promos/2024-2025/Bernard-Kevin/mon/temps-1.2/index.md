---
layout: layout/mon.njk

title: "MON 1.2 : Apprendre à envoyer des mails en Backend"
authors:
  - Kévin BERNARD

date: 2024-09-05
tags: 
  - "temps 1"
  - "email"
  - "smtp"
  - "vert"

résumé: "Ce MON a pour objectif d'expliquer comment envoyer des emails dans différents langages de programmation et de garantir la sécurité dans les échanges."
---

{% prerequis %}

Connaissances de base en programmation (HTML, JavaScript, PHP, Python).

{% endprerequis %}
{% lien %}

- [SMTP](https://www.youtube.com/watch?v=PJo5yOtu7o8)
- [Mailto](https://www.youtube.com/watch?v=NG3WhmbsFvc)
- [Nodemailer](https://www.youtube.com/watch?v=30VeUWxZjS8&t=1697s)
- [PHPMailer](https://github.com/PHPMailer/PHPMailer)
- [smtplib](https://www.youtube.com/watch?v=ueqZ7RL8zxM)
- [Variables d'environnement Node.js](https://www.youtube.com/watch?v=C4cfTFglgJc)
- [Tuto Email JS](https://www.youtube.com/watch?v=BgVjild0C9A)

{% endlien %}

## Table des matières

1. [Introduction](#section1)
2. [Exemples de code](#section2)
3. [Sécurité](#section3)
4. [API](#section4)
5. [Conclusion](#section5)

## 1. Introduction <a id="section1"></a>

L'objectif de ce MON est de découvrir les différentes façons d'envoyer un email dans différents langages de manière sécurisée. 

### Qu'est-ce que SMTP ?

SMTP est le protocole qu'utilise notre ordinateur pour acheminer les emails d'un client à un destinataire (le serveur de messagerie).

{% lien %}

[SMTP](https://www.youtube.com/watch?v=PJo5yOtu7o8)

{% endlien %}

---

## 2. Exemples de code <a id="section2"></a>

### 2.1 Envoi d'email avec HTML

Avec HTML, il n'est pas possible d'envoyer des emails directement, mais on peut créer un formulaire ou un lien qui ouvre la boîte mail (prêt à send) via `mailto`.

{% lien %}

[Mailto](https://www.youtube.com/watch?v=NG3WhmbsFvc)

{% endlien %}

Exemple de lien `mailto` :

```
html

<a href="mailto:someone@example.com?subject=Bonjour&body=Comment ça va ?">
  Envoyer un email
</a>
```


🚨 **Limitation :** Cette méthode dépend de la messagerie de celui qui clique sur le lien et n'envoie pas automatiquement d'email.

### 2.2 Envoi d'email avec Node.js (Nodemailer)

**Nodemailer** est une bibliothèque très populaire quand on utilise JavaScript pour envoyer des emails.

{% lien %}

[Nodemailer](https://www.youtube.com/watch?v=30VeUWxZjS8&t=1697s)

{% endlien %}

#### Installation :

```
bash

npm install nodemailer
```

#### Exemple de code :

```
javascript

const nodemailer = require('nodemailer');

let transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: 'votreEmail@gmail.com',
    pass: 'votreMotDePasse'
  }
});

let mailOptions = {
  from: 'votreEmail@gmail.com',
  to: 'destinataire@example.com',
  subject: 'Test Email',
  text: 'Hello world!'
};

transporter.sendMail(mailOptions, (error, info) => {
  if (error) {
    console.log(error);
  } else {
    console.log('Email envoyé : ' + info.response);
  }
});
```

### 2.3 Envoi d'email avec PHP (PHPMailer)

En PHP, la fonction native `mail()` est assez basique et limitée. C’est pourquoi **PHPMailer** est souvent utilisé pour envoyer des emails plus complexes et sécurisés.

{% lien %}

[PHPMailer](https://github.com/PHPMailer/PHPMailer)

{% endlien %}

#### Installation (via Composer) :

```
bash

composer require phpmailer/phpmailer
```

#### Exemple de code :

```
php

<?php
use PHPMailer\PHPMailer\PHPMailer;
require 'vendor/autoload.php';

$mail = new PHPMailer(true);

try {
    $mail->isSMTP();
    $mail->Host       = 'smtp.gmail.com';
    $mail->SMTPAuth   = true;
    $mail->Username   = 'votreEmail@gmail.com';
    $mail->Password   = 'votreMotDePasse';
    $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
    $mail->Port       = 587;

    $mail->setFrom('votreEmail@gmail.com', 'Votre Nom');
    $mail->addAddress('destinataire@example.com');

    $mail->isHTML(true);
    $mail->Subject = 'Sujet de l\'email';
    $mail->Body    = 'Contenu <b>en HTML</b>';

    $mail->send();
    echo 'Email envoyé avec succès';
} catch (Exception $e) {
    echo "L'email n'a pas pu être envoyé. Erreur : {$mail->ErrorInfo}";
}
```

### 2.4 Envoi d'email avec Python (smtplib)

En Python, on utilise la bibliothèque **smtplib** pour envoyer des emails via le protocole SMTP.

{% lien %}

[smtplib](https://www.youtube.com/watch?v=ueqZ7RL8zxM)

{% endlien %}

#### Exemple de code :

```
python

import smtplib
from email.mime.text import MIMEText

sender = 'votreEmail@gmail.com'
receiver = 'destinataire@example.com'
msg = MIMEText('Hello, ceci est un email envoyé via Python!')
msg['Subject'] = 'Test Email'
msg['From'] = sender
msg['To'] = receiver

try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender, 'votreMotDePasse')
        server.sendmail(sender, receiver, msg.as_string())
        print("Email envoyé avec succès")
except Exception as e:
    print(f"Erreur : {e}")
```

---

🚨 **Attention :** Ne jamais laisser vos mots de passe dans le code. Utilisez des **variables d’environnement** pour plus de sécurité.

---

## 3. Sécurité <a id="section3"></a>

L'envoi d'emails en programmation nécessite de manipuler des informations sensibles comme les identifiants d'accès au serveur SMTP.  
Comment sécuriser ses informations ?

### 3.1 Utilisation des variables d’environnement

Au lieu de stocker vos identifiants dans le code, stockez-les dans des fichiers d'environnement `.env` à bien mettre dans le `.gitignore`.

#### Exemple :

Dans Node.js :

```
javascript

require('dotenv').config();

const email = process.env.EMAIL;
const password = process.env.PASSWORD;
```

Dans votre fichier `.env` :

```
bash

EMAIL=votreEmail@gmail.com
PASSWORD=votreMotDePasse
```

{% lien %}

[Variables d'environnement Node.js](https://www.youtube.com/watch?v=C4cfTFglgJc)

{% endlien %}

### 3.2 Utilisation de TLS/SSL

Pour protéger les données pendant leur transmission, il est crucial d'activer **TLS** ou **SSL** lorsque vous configurez votre serveur SMTP. Par exemple, Nodemailer et PHPMailer supportent ces protocoles nativement.

---

## 4. API d'envoi d'emails <a id="section4"></a>

En plus de l'envoi via SMTP, on peut utiliser des **API spécialisées** pour simplifier l'envoi de mails à grande échelle. Des services comme **SendGrid**, **Mailgun**, **Postmark**, ou **EmailJS** permettent d'avoir des API fiables pour envoyer des emails.

#### Exemple avec EmailJS (en JavaScript) :

**EmailJS** permet d'envoyer des emails directement depuis une application front-end, sans avoir besoin de serveur backend. 

1. Créez un compte sur [EmailJS](https://www.emailjs.com/).
2. Configurez votre service email (par exemple Gmail) et créez un **template** dans l'interface EmailJS.
3. Obtenez votre **User ID** et votre **Service ID**.

{% lien %}

[Tuto Email JS](https://www.youtube.com/watch?v=BgVjild0C9A)

{% endlien %}

#### Exemple de code :

```
html

<head>
  <script type="text/javascript"
      src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js">
  </script>
  <script type="text/javascript">
    (function(){
        emailjs.init({
          publicKey: "oMqq7O7XOuIBpqy1P",
        });
    })();
  </script>
  <script src="js/contact.js"></script>
</head>

<body>
  <form>
    <div>
      <label for="message">Message</label>
      <textarea name="message" id="message" placeholder="Mon message" required></textarea>
    </div>
    <div>
      <label for="nom_prenom">Nom, Prénom</label>
      <input type="text" name="nom_prenom" id="nom_prenom" placeholder="Mon nom et prénom" required>
    </div>
    <div>
      <label for="mail">Mail</label>
      <input type="text" name="mail" id="mail" placeholder="Mon mail" required>
    </div>
    <button type="button" onclick="send_mail()">ENVOYER</button>
  </form>
</body>
```

```
javascript

// Script pour envoyer l'email avec EmailJS
document.getElementById('emailForm').addEventListener('submit', function(event) {
  event.preventDefault();

  emailjs.init('YOUR_USER_ID'); // Remplacez par votre User ID

  emailjs.sendForm('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', this)
    .then(function() {
      console.log('Email envoyé avec succès !');
    }, function(error) {
      console.log('Erreur dans l\'envoi de l\'email:', error);
    });
});
function send_mail(){
    let parametres = {
        nom_prenom: document.getElementById("nom_prenom").value,
        mail: document.getElementById("mail").value,
        message: document.getElementById("message").value
    };

    emailjs.send('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', parametres).then(function() {
        alert("Votre message a bien été envoyé !");
    }).catch(function(error) {
        console.error("Échec de l'envoi : ", error);
        alert("Échec de l'envoi, veuillez réessayer.");
    });    
}
```

🚨 **Remarque :** L'avantage d'EmailJS est qu'il permet d'envoyer des emails directement depuis le navigateur, évitant la configuration d'un serveur backend.

---

## 5. Conclusion <a id="section5"></a>

Quand on veut envoyer des emails en programmation, l'important est de savoir sécuriser les informations du user.
Ici, je ne parle pas des interactions avec le backend en cas d'une base de données avec plusieurs utilisateurs.