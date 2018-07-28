import mcpi.minecraft as minecraft
from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/') # Wir nehmen nun doch mal root, dann muss man weniger tippen im Browser...
def ausspionieren():
    mc = minecraft.Minecraft.create()
    playerIds = mc.getPlayerEntityIds()
    playerId = playerIds[0]
    position = mc.entity.getTilePos(playerId)
    positionstext = "Spielerposition: x=" + str(position.x) + " y=" + str(position.y) + " z=" + str(position.z)
    return render_template('index.html', positionstext=positionstext)