Die momentane Nutzung des Programmes:
WICHTIG: Das Programm sollte am besten einfach auf dem Laptop den Stefan nutzt gelassen werden, da dort schon alles installiert ist

Starten des Programmes auf Stefans Laptop:
-VM mit Oracle Linux starten: Dort ist Keycloak als Docker Container installiert
-In die Systemkonsole: "docker start keycloak"
-Man sollte sich nun auch vom Host aus verbinden können
-Zum Test: (Ip der VM):8080 um zum Admin Menü zu kommen(Login: Am besten Stefan fragen da ich hier die Login Daten nicht auf Github veröffentlichen möchte)
-Es ist unbekannt ob man sich im Admin Terminal anmelden muss, aber am besten einmal mindestens machen
-Im Flask Ordner(Programm - Ordner) app.py ausführen(mit VSCode öffnen --> Oben rechts ausführen)
-Auf 127.0.0.1:5000 ist das Programm am laufen. Ob die Verbindung von anderen Geräten aus möglich ist ist bisher ungeklärt(Stefan fragen)
-Momentan gibt es nur 2 User: (noah, abcd) und (stefan, 1234) <-- (username, password). Diese werden vermutlich bald gelöscht
-Zum erstellen neuer Nutzer:
--in die Adminkonsole einloggen
--Unter "Users" neuen Benutzer erstellen: Dabei ist nur der Username wichtig
--Im neuen Nutzer unter "Credentials" eine Passwort festlegen: Schieberegler anmachen wenn das Passwort beim ersten einloggen vom Nutzer verändert werden soll
--Im neuen Nutzer "Email verified" auf Ja setzen wenn dem Nutzer erlaubt sein soll, die Liste zu sehen. Ist "Email verified" aus, kann der user die Seite nicht nutzen





Das starten des Programmes auf anderen Geräten:

-Bei auftretenden Problemen die zuständige Person fragen(Stefan)

1.: Python herunterladen:
- Auf https://www.python.org/downloads/ Python herunterladen. Es wurde in der Entwicklung die Version 3.12.2 genutzt, sollte es in der Zukunft bei neueren Versionen Probleme geben könnte der Versionsunterschied Schuld sein

2.: Installer ausführen:
- Im Downloadsordner sollte sich nun die Datei "python-(Version, z.B. 3.12.2)-amd64.exe" befinden. Dies ist der Installer. Diesen ausführen und den im Installation Fenster angegebenen Schritten folgen

3.: Bibliotheken installieren:
- Das Python Programm benötigt Bibliotheken(externe importierbare Codestücke) um zu funktionieren
- Windows: Win + R drücken(Win ist die Taste mit dem Windows Symbol)
- Im "Ausführen" Fenster "cmd" eingeben(Dies öffnet die Systemkonsole)(Ohne " vor und nach dem Befehl)
- Im Konsolenfenster "py -m pip install flask flask_oidc psycopg2" eingeben(Ohne " vor und nach dem Befehl)
- Warten bis alles heruntergeladen ist
- Bei Problemen: https://packaging.python.org/en/latest/tutorials/installing-packages/

4.: Keycloak als Docker Container installieren:
- Docker installieren: https://youtu.be/XgRGI0Pw2mM?si=8iMyRdqHyBrSTsrP
- Keycloak als Container installieren: https://youtu.be/yr8UmVTuxYw?si=PfgqK19tfvKJhbAf
- - Teil der Installation ist das festlegen der Admin Login Daten: "docker run --name keycloak -d -p 8080:8080 -e KEYCLOAK_ADMIN=(admin name) -e KEYCLOAK_ADMIN_PASSWORD=(admin password) quay.io/keycloak/keycloak:latest start-dev"
  - Admin name und password sind wichtig, diese irgendwie notieren
 
5.: Keycloak Realm erstellen:
-Am besten ein Youtube Video über Keycloak Basics anschauen
-Wichtige Daten die im Realm stehen müssen:
- - Realm name: elrealm
  - Neuer Client: ClientID: elre
  - Neuer Client: Client Authentication muss an sein
  - Neuer Client: Unter Authentication: Nur Standard Flow anmachen
  - Neuer Client: Home URL: http://127.0.0.1:5000/*
  - Neuer Client: Valid redirect URIs: http://127.0.0.1:5000/*
  - Neuer Client: Web Origins: /*
  - Realm Settings: Sessions: SSO Session Idle: 1 Second
  - Realm Settings: Sessions Client Session Idle: 1 Minute
- Clients: Neuer Client: Credentials: Das "Client Secret" herauskopieren und in die client_secrets.json Datei im Flask Ordner(Programm Dateien) zu "client_secret" schreiben

6.: PostgreSQL Datenbank starten:
- https://www.guru99.com/download-install-postgresql.html
- Als Passwort wird "Natlanmap39" empfohlen: Das Risiko dies öffentlich hier hinzuschreiben wurde von zwei Seiten als klein eingeschätzt, besonders da dieses bereits im (auch öffentlichen) Code an 4 Stellen zu lesen ist
- Sonßt: Passwort kann selbst festgelegt werden
- Das neue Password muss im Programm in app.py in Zeile 85, 106, 146, 177 in 'password="(Hier das Passwort)"' eingetragen werden
- Sollten besondere Änderungen an den PostGreSQL Einstellungen vorgenommen worden sein(z.B.: Port ändern) so muss dieses ebenfalls im Programm in den bereits genannten Zeilen geändert werden

7.: Programm mit Python ausführen:
- In die Programmdateien navigieren. Wurde der Ordner heruntergeladen und nicht bewegt so befindet sich die Datei in Downloads --> Flask
- Im Ordner "Flask" befindet sich die Datei "app.py". Auf diese Rechtsklick --> Öffnen mit --> Python

8.: Zur Programmseite navigieren:
- Nach Schritt 3 sollte sich ein Konsolenfenster geöffnet haben
- Im Konsolenfenster sollte irgendwo:
   "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on http://127.0.0.1:5000"
  zu lesen sein
- Da das Programm eine lokale Internetseite öffnet, muss das Programm in einem Browser genutzt werden. In der Entwicklung wurde Firefox genutzt, andere wurden noch nicht getestet
- Öffnen sie die im Konsolenfenster angegebene Seite(wahrscheinlich http://127.0.0.1:5000) im Browser
