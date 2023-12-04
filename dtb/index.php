<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="master.css">
	<title>název hry</title>
</head>
<body>
	<header>
		<h1>Placeholder název hry</h1>
		<nav>
			<ul>
				<li><a href="#" class="animate-btn">Domů</a></li>
				<li><a href="#" class="animate-btn">O hře</a></li>
				<li><a href="#" class="animate-btn">Hrát</a></li>
				<li><a href="#" class="animate-btn">Kontakt</a></li>
			</ul>
		</nav>
	</header>
	
	<main>
		<h2>popis hry</h2>
		<p>Teprv bude</p>
		
		<section id="scoreboard">
			<h3>Skóre</h3>
			<ol>
	<?php  
	$servername = "dbs.spskladno.cz";
	$username = "student09";
	$password = "xxx";
	$dbname = "vyuka09";

	$conn = new mysqli($servername, $username, $password, $dbname);

	if ($conn->connect_error) {
		exit("Spojení se nezdařilo. Chyba: " . $conn->connect_error);
	}
	$mysqli->set_charset("utf8mb4");
	
	$conn->close();
	?>
				<li><span>1.</span>nevim1</li>
				<li><span>2.</span>nevim2</li>
				<li><span>3.</span>nevim3</li>
			</ol>
		</section>
		
		<section id="game">
			<h3>Hra</h3>
			<p>nevim4</p>
		</section>
	</main>
</body>
</html>
