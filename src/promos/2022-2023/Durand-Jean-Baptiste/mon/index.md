---
layout: layout/mon-index.njk

title: "MON Jean-Baptiste"
authors:
    - Jean-Baptiste Durand
---

<!-- début résumé -->

Ensemble des MON réalisés par Jean-Baptiste Durand

<!-- fin résumé -->

<div class="temps-container">
	<div class="temps-border temps-border-left"></div>
	<h2 class="temps">Temps 1</h2>
	<div class="card-container">
		<a class="card" style="background-color:rgba(64, 134, 244,var(--opacity));" href="./gglAppsScript">
			<div class="img-container"><img src="./Image/Google_Apps_Script.svg.png" alt="Avatar" style="width:100%"/></div>
			<p class="MON-descriptif">Google apps script ou comment automatiser les choses embêtantes dans un tableur</p>
		</a>
		<a class="card" style="background-color:rgba(218, 170, 248,var(--opacity));" href="./SQLinjection">
			<div class="img-container"><img src="./Image/SQLinjection.jpg" alt="Avatar" style="width:100%;"/></div>
			<p class="MON-descriptif"> SQL injection </p>
		</a>
	</div>
</div>
<div class="temps-container">
	<div class="temps-border temps-border-right"></div>
	<h2 class="temps">Temps 2</h2>
	<div class="card-container">
		<a class="card" style="background-color:rgba(126, 160, 219,var(--opacity));" href="./yaccLex">
			<div class="img-container"><img src="./Image/compileur-logo.png" alt="Avatar" style="width:100%;border-radius: 8em;"></div>
			<p class="MON-descriptif">Programmes binaires et Compilateurs</p>
		</a>
		<a class="card" style="background-color:rgba(255, 56, 33,var(--opacity));" href="./firewall">
			<div class="img-container"><img src="./Image/firewallLogo.png" alt="Avatar" style="width:100%"/></div>
			<p class="MON-descriptif"> Firewall </p>
		</a>
	</div>
</div>
<div class="temps-container">
	<div class="temps-border temps-border-left"></div>
	<h2 class="temps">Temps 3</h2>
	<div class="card-container">
		<a class="card" style="background-color:rgba(0, 127, 53 ,var(--opacity));" href="./compiler">
			<div class="img-container"><img src="./Image/compiler.jpg" alt="Avatar" style="width:100%"/></div>
			<p class="MON-descriptif">Compilateur (partie 2)</p>
		</a>
		<a class="card" style="background-color:rgba(152, 115, 93,var(--opacity));" href="./phaser">
			<div class="img-container"><img src="https://phaser.io/images/img.png" alt="Avatar" style="width:100%"/></div>
			<p class="MON-descriptif"> Phaser - Game Engine + Github CI</p>
		</a>
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
		margin:1em;
		border-radius: 4em;
		--opacity:0.2;
		transition: all 1s;
	}
	.card:hover{
		--opacity:0.6;
	}
	
	.img-container{
		height:408.6px;
		display: flex;
		justify-content: center;
		align-items: center;
		background-color:white;
		margin-right:1em;
		margin-left:1em;
		margin-top:1em;
		border-radius: 3em;
	}
	img{
		border-width:0;
	}
	.MON-descriptif{
		margin:2em;
		font-size:1.2em;
	}
</style>
