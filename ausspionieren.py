import mcpi.minecraft as minecraft
from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/')
def ausspionieren():
    try:
        mc = minecraft.Minecraft.create()
        playerIds = mc.getPlayerEntityIds()
        playerId = playerIds[0]
        position = mc.entity.getTilePos(playerId)
        positionstext = "Spielerposition: x=" + str(position.x) + " y=" + str(position.y) + " z=" + str(position.z)
        return render_template('index.html', positionstext=positionstext)
    except (ConnectionResetError, ConnectionRefusedError):
        return render_template('index.html', positionstext="No minecraft instance available.")
