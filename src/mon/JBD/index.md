---
layout: layout/post.njk

title: "MON Jean-Baptiste"
authors:
  - Jean-Baptiste Durand

tags: ['mon']
---

<!-- début résumé -->
Ensemble des MON réalisés par Jean-Baptiste Durand
<!-- fin résumé -->

<div class="temps-container">
	<div class="temps-border temps-border-left"/>
	<h2 class="temps">Temps 1</h2>
	<div class="card-container">
		<div class="card">
			<img src="./Image/Google_Apps_Script.svg.png" alt="Avatar" style="width:100%">
			<p>Google apps script ou comment automatiser les choses embêtantes dans un tableur</p>
		</div>
		<div class="card">
			<img src="./Image/11ty.png" alt="Avatar" style="width:100%">
			<p> Créer son site web statique avec eleventy </p>
		</div>
	</div>
</div>

<div class="temps-container">
	<div class="temps-border temps-border-right"/>
	<h2 class="temps">Temps 2</h2>
	<div class="card-container">
		<div class="card">
			<img src="./Image/logo-mongoDB.jpg" alt="Avatar" style="width:100%">
			<p>Bases de données non relationnelles (MongoDB, ...)</p>
		</div>
		<div class="card">
			<img src="./Image/1200px-Sass_Logo_Color.svg.png" alt="Avatar" style="width:100%">
			<p> Web Front 2 (SASS, postCSS) </p>
		</div>
	</div>
</div>

<div class="temps-container">
	<div class="temps-border temps-border-left"/>
	<h2 class="temps">Temps 3</h2>
	<div class="card-container">
		<div class="card">
			<img src="./Image/1631026680-logo-react-native.png" alt="Avatar" style="width:100%">
			<p>Développement Mobile (React Native)</p>
		</div>
		<div class="card">
			<img src="./Image/13429_ILL_DevOpsLoop.png" alt="Avatar" style="width:100%">
			<p> Dev-ops (objets et/ou méthodes)</p>
		</div>
	</div>
</div>

<style>
	.temps{
		text-align:center;
		font-size:2em;
		border-bottom-width:0px;
		margin-top:1em;
	}
	.temps-container{
		position:relative;
		padding-left: 30px;
		padding-right: 30px;
	}
	.temps-border{
		position:absolute;
		border:solid;
		border-width: 10px 0px 10px 0px;
		top:calc(-1em - 5px);
		bottom:calc(-1em - 5px);
		z-index:-1;
	}
	.temps-border-left{
		border-left-width:10px;
		border-radius: 40px 0px 0px 40px;
		right:10%;
		left:0;
	}
	.temps-border-right{
		border-right-width:10px;
		border-radius: 0px 40px 40px 0px;
		left:50%;
		right:0;
	}
	.card-container{
		display:flex;
		flex-direction:row;
	}
	.card{
		flex:1;
	}
</style>