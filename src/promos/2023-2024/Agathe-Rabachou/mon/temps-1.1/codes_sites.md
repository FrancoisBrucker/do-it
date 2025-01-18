---
layout: layout/mon.njk

title: "Web Front - codes"
authors:
  - Agathe Rabachou

date: 2023-09-27


résumé: Codes de mon MON.
---
*Accueil du site :*
```html
<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="utf-8" >
    <title>Accueil - Robbie Lens Photographie</title>
    <link href="style.css" rel="stylesheet" >
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Manrope&family=Montserrat&display=swap" rel="stylesheet">
</head>

<body>
    <header>
        <nav>
            <img src="images/logo.webp" alt="Logo Robbie Lens" >
            <div>
                <a href="index.html">Accueil</a>
                <a href="a-propos.html">À propos</a>
                <a href="portfolio.html">Portfolio</a>
            </div>
        </nav>
    </header>
    <main>
        <section class="contenu_accueil">
            <div>
                <h1>Robbie Lens Photographie</h1>
                <p>
                    Où <em>professionalisme</em> s’allie avec <em>passion</em>. Depuis
                    plus de 5 ans maintenant, j’exerce mon métier avec la passion
                    qui m’anime : capturer l’essence de chaque instant.
                </p>
                <a href="portfolio.html" class="cta">UN PROJET ? ÉCRIVEZ-MOI</a>
            </div>
            <img src="images/robbie-lens.webp" alt="Portrait avec effet de la photographe Robbie Lens" >
        </section>
        <section class="photos_accueil">
            <h2>Mon dernier projet</h2>
                <div>    
                    <img src="images/accueil/element-1.webp" alt="Twelve apostles - Australie" >
                    <img src="images/accueil/element-2.webp" alt="Wai-O-Tapu - Nouvelle-Zélande" >
                    <img src="images/accueil/element-3.webp" alt="Parc National d’Abel Tasman - Nouvelle-Zélande" >
                </div>    
                <div>    
                    <img src="images/accueil/element-4.webp" alt="Lac Rotorua - Nouvelle-Zélande" >
                    <img src="images/accueil/element-5.webp" alt="Milford Sound - Nouvelle-Zélande" >
                    <img src="images/accueil/element-6.webp" alt="Lac Wanaka - Nouvelle-Zélande" >
                </div>
        </section>
    </main>
    <footer>
        <img src="images/logo.webp" alt="Logo Robbie Lens" >
        <div>
            <a target="_blank" href="https://twitter.com/" class="lien-icone">
                <img src="images/twitter.webp" alt="Logo Twitter" >
            </a>
            <a target="_blank" href="https://www.instagram.com/" class="lien-icone">
                <img src="images/instagram.webp" alt="Logo Instagram" >
            </a>
        </div>    
    </footer>
</body>

</html>
```

*Page "A propos" :*
```html
<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="utf-8" >
    <title>À propos - Robbie Lens Photographie</title>
    <link href="style.css" rel="stylesheet" >
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Manrope&family=Montserrat&display=swap" rel="stylesheet">
</head>

<body>
    <header>
        <nav>
            <a href="index.html" class="lien-icone">
                <img src="images/logo.webp" alt="Logo Robbie Lens" >
            </a>
            <div>
                <a href="index.html">Accueil</a>
                <a href="a-propos.html">À propos</a>
                <a href="portfolio.html">Portfolio</a>
            </div>
        </nav>
    </header>
    <main class="a-propos-main">
        <section>
            <h1>À propos</h1>
            <div class="carre-contenu">
                <p>
                    Photographe depuis plus de 5 ans, je réalise des reportages aux photos dynamiques et pertinentes
                    pour vos
                    projets de communication. Créativité, qualité, et sérénité pour vous! Je gère tout, depuis la
                    direction
                    artistique, la réalisation du reportage jusqu’à la livraison de vos photos retouchées, prêtes à
                    l’emploi.
                </p>
                <h2>Services</h2>
                <ul>
                    <li>Portrait seul ou à plusieurs</li>
                    <li>Shooting mode</li>
                    <li>Retouches sur mesure</li>
                    <li>Développement</li>
                </ul>
            </div>
            <div>
                <a href="portfolio.html" class="cta">VOIR MON PORTFOLIO</a>
            </div>
        </section>
    </main>
    <footer>
        <a href="index.html" class="lien-icone">
            <img src="images/logo.webp" alt="Logo Robbie Lens" >
        </a>
        <div>
            <a target="_blank" href="https://twitter.com/" class="lien-icone">
                <img src="images/twitter.webp" alt="Logo Twitter" >
            </a>
            <a target="_blank" href="https://www.instagram.com/" class="lien-icone">
                <img src="images/instagram.webp" alt="Logo Instagram" >
            </a>
        </div>
    </footer>
</body>

</html>
```

*Portfolio :*
```html
<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="utf-8" >
    <title>Portfolio - Robbie Lens Photographie</title>
    <link href="style.css" rel="stylesheet" >
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Manrope&family=Montserrat&display=swap" rel="stylesheet">
</head>

<body>
    <header>
        <nav>
            <a href="index.html" class="lien-icone">
                <img src="images/logo.webp" alt="Logo Robbie Lens" >
            </a>
            <div>
                <a href="index.html">Accueil</a>
                <a href="a-propos.html">À propos</a>
                <a href="portfolio.html">Portfolio</a>
            </div>
        </nav>
    </header>
    <main>
        <section>
            <h1>Portfolio</h1>
        </section>
        <section class="portfolio-section-photos">
            <h2>Voyages</h2>
            <div class="photos_voyages">
                <a href="images/portfolio/paysage1.webp" class="lien-conteneur-photo">
                    <img src="images/portfolio/paysage1.webp" alt="Mont Aoraki - Nouvelle-Zélande" >
                    <div class="photo-hover">Voir la photo</div>
                </a>
                <a href="images/portfolio/paysage2.webp" class="lien-conteneur-photo">
                    <img src="images/portfolio/paysage2.webp" alt="Parc National d’Abel Tasman - Nouvelle-Zélande" >
                    <div class="photo-hover">Voir la photo</div>
                </a>
                <a href="images/portfolio/paysage3.webp" class="lien-conteneur-photo">
                    <img src="images/portfolio/paysage3.webp" alt="Lac Rotorua - Nouvelle-Zélande" >
                    <div class="photo-hover">Voir la photo</div>
                </a>
                <a href="images/portfolio/paysage4.webp" class="lien-conteneur-photo">
                    <img src="images/portfolio/paysage4.webp" alt="Lac Wanaka - Nouvelle-Zélande" >
                    <div class="photo-hover">Voir la photo</div>
                </a>
                <a href="images/portfolio/paysage5.webp" class="lien-conteneur-photo">
                    <img src="images/portfolio/paysage5.webp" alt="Mont Taranaki - Nouvelle-Zélande" >
                    <div class="photo-hover">Voir la photo</div>
                </a>
                <a href="images/portfolio/paysage6.webp" class="lien-conteneur-photo">
                    <img src="images/portfolio/paysage6.webp" alt="Milford Sound - Nouvelle-Zélande" >
                    <div class="photo-hover">Voir la photo</div>
                </a>
                <a href="images/portfolio/paysage7.webp" class="lien-conteneur-photo">
                    <img src="images/portfolio/paysage7.webp" alt="Twelve Apostle - Australie" >
                    <div class="photo-hover">Voir la photo</div>
                </a>
                <a href="images/portfolio/paysage8.webp" class="lien-conteneur-photo">
                    <img src="images/portfolio/paysage8.webp" alt="Wai-O-Tapu - Nouvelle-Zélande" >
                    <div class="photo-hover">Voir la photo</div>
                </a>
                <a href="images/portfolio/paysage9.webp" class="lien-conteneur-photo">
                    <img src="images/portfolio/paysage9.webp" alt="Mont Cook - Nouvelle Zélande" >
                    <div class="photo-hover">Voir la photo</div>
                </a>
            </div>
            <h2>Portraits</h2>
            <div class="photos_portraits">
                <a href="images/portfolio/portrait1.webp" class="lien-conteneur-photo">
                    <img src="images/portfolio/portrait1.webp" alt="Portrait jeune femme 1" >
                    <div class="photo-hover">Voir la photo</div>
                </a>
                <a href="images/portfolio/portrait2.webp" class="lien-conteneur-photo">
                    <img src="images/portfolio/portrait2.webp" alt="Portrait jeune femme 2" >
                    <div class="photo-hover">Voir la photo</div>
                </a>
                <a href="images/portfolio/portrait3.webp" class="lien-conteneur-photo">
                    <img src="images/portfolio/portrait3.webp" alt="Portrait jeune homme 3" >
                    <div class="photo-hover">Voir la photo</div>
                </a>
                <a href="images/portfolio/portrait4.webp" class="lien-conteneur-photo">
                    <img src="images/portfolio/portrait4.webp" alt="Portrait jeune femme 4" >
                    <div class="photo-hover">Voir la photo</div>
                </a>
                <a href="images/portfolio/portrait5.webp" class="lien-conteneur-photo">
                    <img src="images/portfolio/portrait5.webp" alt="Portrait jeune femme 5" >
                    <div class="photo-hover">Voir la photo</div>
                </a>
                <a href="images/portfolio/portrait6.webp" class="lien-conteneur-photo">
                    <img src="images/portfolio/portrait6.webp" alt="Portrait jeune femme 6" >
                    <div class="photo-hover">Voir la photo</div>
                </a>
            </div>
        </section>
    </main>
    <footer>
        <a href="index.html" class="lien-icone">
            <img src="images/logo.webp" alt="Logo Robbie Lens" >
        </a>
        <div>
            <a target="_blank" href="https://twitter.com/" class="lien-icone">
                <img src="images/twitter.webp" alt="Logo Twitter" >
            </a>
            <a target="_blank" href="https://www.instagram.com/" class="lien-icone">
                <img src="images/instagram.webp" alt="Logo Instagram" >
            </a>
        </div>
    </footer>
</body>

</html>
```

*Feuille de style :*
```css
* {
  margin: 0;
}

body {
  font-family: 'Manrope', sans-serif;
  font-size: 1em;
  background-color: #1f2039;
}

a {
  color: #242424;
  text-decoration: none;
}

em {
  color: #a5b4fc;
  font-style: normal;
}

h1 {
  font-size: 3.5em;
  color: #a5b4fc;
  font-family: 'Montserrat', sans-serif;
}

h2 {
  color: #f9f8ff;
}

p,
li {
  font-size: 1.1em;
  color: #f9f8ff;
}

header,
footer {
  background-color: white;
  padding: 20px 50px;
}

.cta {
  background: linear-gradient(#8e86b5, #acaeed);
  color: white;
  border-radius: 50px;
  padding: 20px 30px;
  display: inline-block;
}

a:hover {
  text-decoration: underline;
}

.cta:hover {
  background: linear-gradient(#696484, #8788ba);
  text-decoration: none;
}

.lien-icone {
  margin-left: 30px;
}

.lien-icone:hover {
  opacity: 0.5;
}

.carre-contenu {
  border-right: 1px solid #8e86b5;
  border-bottom: 1px solid #8e86b5;
  padding: 50px;
  margin-bottom: 80px;
}

.carre-contenu h2 {
  margin-top: 30px;
}

.carre-contenu ul {
  margin-top: 30px;
}

section {
  padding: 80px;
}

.a-propos-main {
  width: 50%;
  margin: auto;
}

footer, nav{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}

nav a{
  margin-left:30px;
}

.contenu_accueil{
  display: flex;
  flex-direction: row;
  width: 50%;
  align-items: center;
  margin: auto;
  gap: 50px;
}

.photos_accueil {
  background-color: white;
  padding: 80px;
}

.photos_accueil h2{
  color: #242424;
  text-align: center;
  margin-bottom: 80px;
}

.photos_accueil div{
  display: flex;
  flex-direction: row;
  gap: 15px;
  justify-content: center;
  margin-bottom: 15px;
}

p{
  margin-bottom: 50px;
}

.portfolio-section-photos {
  background-color: white;
}

.portfolio-section-photos h2 {
  color: #242424;
  margin-bottom: 80px;
}

.photos_voyages{
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: 300px 300px 300px;
  gap: 15px;
  margin-bottom: 80px;
}

.photos_portraits{
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: 300px 300px;
  gap: 15px
}

.photos_voyages img,
.photos_portraits img {
  width: 100%;
  height: 100%;
  /* permet aux images de respecter les dimensions de la grid CSS */
  object-fit: cover;
}

.portfolio-section-photos {
  background-color: white;
}

.portfolio-section-photos h2 {
  color: #242424;
  margin-bottom: 80px;
}

.lien-conteneur-photo {
  position: relative;
}

.photo-hover {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5em;
  color: white;
  background-color: rgba(0, 0, 0, 0.7);
  display: none;
}

.lien-conteneur-photo:hover .photo-hover {
  display: flex;
}
```