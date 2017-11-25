<!DOCTYPE html>
<html>
	<head>
		<title>Praktikum 2</title>
		<meta charset= "UTF-8"/>
			<style>
				@import "/webteams.css";
			</style>
	</head>
	<body>
		<div>
			<form action="/loginSubmitPassword/?email=${email}" method="POST">

				<label>Password</label>
				<input type="password" name="password" />
				<br>
				<button type="submit" class="button">Einloggen</button>

			</form>
		</div>
	</body>
</html>