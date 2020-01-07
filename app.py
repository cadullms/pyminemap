import mcpi.minecraft as minecraft
from flask import render_template
from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def pyminemapIndex():
    return render_template('index.html')

@app.route('/list')
def pyminemapList():
    try:
        positionstexte = []
        mc = minecraft.Minecraft.create()
        playerIds = mc.getPlayerEntityIds()
        for playerId in playerIds:
            position = mc.entity.getTilePos(playerId)
            positionstexte.append("Spielerposition: x=" + str(position.x) + " y=" + str(position.y) + " z=" + str(position.z))
        return render_template('list.html', positionstexte=positionstexte)
    except (ConnectionResetError, ConnectionRefusedError):
        return render_template('list.html', positionstext=None)

@app.route('/map')
def pyminemapMap():
    return render_template('map.html')
    
@app.route('/api/players/positions', methods = ['GET'])
def getPlayerPositions():
    try:
        positions = []
        mc = minecraft.Minecraft.create()
        for playerId in mc.getPlayerEntityIds():
            playerPosition = mc.entity.getPos(playerId)
            position = {
                'playerId': playerId,
                'x': playerPosition.x,
                'y': playerPosition.y,
                'z': playerPosition.z
            }
            positions.append(position)
        return jsonify(positions)
    except (ConnectionResetError, ConnectionRefusedError):
        return jsonify([])

@app.route('/api/worldDimensions', methods = ['GET'])
def getWorldDimensions():
    # see: https://www.stuffaboutcode.com/p/minecraft-api-reference.html
    try:
        mc = minecraft.Minecraft.create()
        x = 0
        while mc.getBlock(x,0,0) != 95:
            x += 1
        z = 0
        while mc.getBlock(0,0,z) != 95:
            z += 1
        maxX = x - 1
        minX = maxX - 256
        maxZ = z - 1
        minZ = maxZ - 256
        return jsonify({'minX':minX,'maxX':maxX,'minZ':minZ,'maxZ':maxZ})
    except (ConnectionResetError, ConnectionRefusedError):
        return jsonify(None)
