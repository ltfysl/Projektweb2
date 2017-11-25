<html>
<meta charset= "UTF-8"/>
			<style>
				@import "/webteams.css";
			</style>
<body>
	<table>
	<tr>
		<th colspan="5">Studiengang</th>
	</tr>
	<tr>
		<th>Bezeichnung</th><th>Kurzbezeichnung</th><th>Beschreibung</th><th>Anzahl Semester</th>
	</tr>
	% for studiengang in studiengange:
	<tr>
		<td> ${studiengang["Bezeichnung"]} </td><td>${studiengang["Kurzbezeichnung"]}</td><td>${studiengang["Beschreibung"]}</td><td>${studiengang["AnzahlSemester"]}</td>
	</tr>
	% endfor
	</table>
	<a href="/" class="button">Abmelden</a>
</body>
</html>