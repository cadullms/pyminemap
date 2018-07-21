from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/') # Wir nehmen nun doch mal root, dann muss man weniger tippen im Browser...
def ausspionieren():
    positionstext = "Hier soll dann irgendwann mal die Position des Spielers stehen. Da musst Du nun noch passenden Code für schreiben!"
    return render_template('index.html', positionstext=positionstext)