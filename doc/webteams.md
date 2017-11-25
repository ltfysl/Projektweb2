
# Dokumentation Praktikum 
Praktikumsgruppe B Abdüllatif Yesil & Berkay ÖZ 24.10.17


## Aufbau der Webanwendung 
Die Hauptseite auch Indexseite genannt beinhaltet eine Tabelle mit 9 Spalten und 15 Zeilen.
Die Tabelle soll uns Name, Vorname, Matrikelnummer und Semesteranzahl der Gruppenmitglieder auflisten.
Die letzte Spalte "Aktion" mit zwei Buttons,"bearbeiten" und "löschen", bieten die Möglichkeit bereits erfasste Einträge zu bearbeiten oder zu löschen
Im Fußbereich der Tabelle ist ein Button mit der Bezeichnung erfassen, dieser
bietet die Möglichkeit - durch das ausfüllen des Formulars auf der /edit Seite - neue Teammitglieder hinzuzufügen 
Auf der /edit Seite wiederum gibt es wieder zwei Buttons, einmal "Speichern", der das ausgefüllte Formular abspeichert
und "Abbruch", mit dem wir zurück zur Indexseite gelangen und das Formular nicht abgespeichert wird. 



## Durchgeführte Ergänzungen
In der "form0.tpl" wurden weitere Spalten für das zweite Teammitglied erstellt und zusätzlich beiden Teammitglieder die Spalte "Semesteranzahl" hinzugefügt. 
Die Datei "form1.tpl" wurde mit einem Hyperlink mit der Bezeichnung "Abbruch" ausgestattet die uns zurück zur Indexseite bringt 
In der "websteams.css" Datei haben wir die Attribute der Seite wie z.b Hintergrundfarbe der Seite oder der Tabelle, die Borderlines und die Ausrichtung der Tabelle definiert. 
Hintergrund der Seite und der Tabelle wurden mit einem Hintergrundbild ausgestattet und die Überschrift der Tabelle schwarz gefärbt. 
Die Lösch Funktion wurde in der "Database.py" so ergänzt das bei Aufruf die Einträge mit dem Default Wert initialisiert werden 
und ihren Anfangswert bekommen bzw. zurückgesetzt werden. Zum Schluss wurde in der "webteams.js" Datei die Funktion "confirmDelete" vervollständigt. Sodass wenn man auf Löschen klickt noch eine Abfrage kommt, ob man wirklich die Daten Löschen möchte. Bei der wahl "Abbrechen" wird das Löschen mit preventDefault verhindert.

## Beschreibung des HTTP-Datenverkehrs 
### Beim Start der Anwendung 
* Beim Start wird der Server über den Localhost(127.0.0.1) mit dem Port 8080 aufgerufen und gestartet.

### Beim Speichern von Formulardaten 
* Durch das klicken auf den Button "erfassen", wird die Edit seite mit der GET Methode aufgerufen 
Nachdem man das Formular komplett ausgefüllt hat und auf "Speichern" klickt, werden die Einträge mit der POST Methode abgespeichert. 
Beim Löschen wird die delete Funktion mit der GET Methode ausgeführt und die Spalten bekommen ihre Defaultwerte. 

