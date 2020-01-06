import mcpi.minecraft as minecraft
from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/')
def pyminemap():
    try:
        positionstexte = []
        mc = minecraft.Minecraft.create()
        playerIds = mc.getPlayerEntityIds()
        for playerId in playerIds:
            position = mc.entity.getTilePos(playerId)
            positionstexte.append("Spielerposition: x=" + str(position.x) + " y=" + str(position.y) + " z=" + str(position.z))
        return render_template('index.html', positionstexte=positionstexte)
    except (ConnectionResetError, ConnectionRefusedError):
        return render_template('index.html', positionstext=None)
