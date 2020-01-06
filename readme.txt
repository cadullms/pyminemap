Hier noch ein paar Hinweise:

FLASK ==================================================

Ganz wichtig: Vor dem ersten Start muss flask installiert werden mit:

    pip install Flask

Dann immer starten mit:

    FLASK_APP=pyminemap.py flask run --host=0.0.0.0

Zu flask gibt es die Dokumentation hier: http://flask.pocoo.org
Und hier das Wichtigste in Kürze: http://flask.pocoo.org/docs/1.0/quickstart/

TEMPLATES ==============================================

Das index.html ist weitgehend ganz normales statisches
HTML. Die einzige Stelle, wo etwas Dynamisches ins
Spiel kommt , ist wo {% %} und {{}} anzeigen, dass da
Template-Code statt HTML kommt. In diesem Fall nur eine
Fallunterscheidung (wenn der Positionstext gefüllt ist
mach dies, sonst mach was anderes) und eben die Darstellung
des Positionstextes selbst im <h1> Tag.

JAVASCRIPT =============================================

index.html enthält ein kleines Stückchen JavaScript:

    <script type="text/javascript">
        setTimeout(function () { 
          location.reload();
        }, 1000);
    </script>

Damit lädt sich die Seite nun auch schon automatisch
jede Sekunde selbst neu. Das ist ein schönes Einstiegs-
beispiel für JavaScript-Code, der in eine HTML-Seite ein-
gebettet ist. Die setTimeout-Funktion kriegt immer genau
zwei Parameter: Eine function, die sie ausführen soll und
ein Intervall in Millisekunden. setInterval wartet dann
immer genau die angegebene Anzahl an Millisekunden, führt
die Funktion aus, wartet wieder, führt wieder die Funktion
aus, und so weiter. In diesem Fall macht die Funktion nur
eins: location.reload(), was quasi dasselbe macht wie der
Reload-Button im Browser.
    
Diese Lösung bringt aber einige Probleme mit sich, wie Du
sicher herausfinden wirst. Am Ende sollten wir da was
Schlaueres machen. Vorerst wird es da JQuery tun. Dazu später
mehr... :-)

