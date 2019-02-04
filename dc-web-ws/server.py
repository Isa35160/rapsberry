from flask import Flask
from flask_socketio import SocketIO, send, emit
from flask import render_template
import time
import threading
from mouvement import Mouvement
from temperatureSensor import TemperatureSensor



app = Flask(__name__)
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template('index.html')


# def message_loop():
#     while True:
#         socketio.emit('alert', Broadcast=True)
#

move = Mouvement()
tempSens = TemperatureSensor()
# Vue que notre méthode pour lire nos message est une boucle infinie
# Elle bloquerait notre serveur. Qui ne pourrait répondre à aucune requête.
# Ici nous créons un Thread qui va permettre à notre fonction de se lancer
# en parallèle du serveur.
# read_messages = threading.Thread(target=message_loop)
detect = threading.Thread(target=move.detectMove, args=(socketio,))
temp = threading.Thread(target=tempSens.readTempLive, args=(socketio,))
# read_messages.start()
detect.start()
temp.start()


