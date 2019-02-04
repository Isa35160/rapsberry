from flask import Flask
from flask_socketio import SocketIO, send, emit
from flask import render_template
import time
import threading
from mouvement import Mouvement




app = Flask(__name__)
socketio = SocketIO(app)
movementText = SocketIO(app)

@app.route("/")
def index():
    return render_template('index.html')


def message_loop():
    while True:
        socketio.emit('alert', Broadcast=True)
        movementText.emit('moveAlert', Broadcast=True)





move = Mouvement()
# Vue que notre méthode pour lire nos message est une boucle infinie
# Elle bloquerait notre serveur. Qui ne pourrait répondre à aucune requête.
# Ici nous créons un Thread qui va permettre à notre fonction de se lancer
# en parallèle du serveur.
read_messages = threading.Thread(target=message_loop)
read_messages.start()
move.detectMove()

