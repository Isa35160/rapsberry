import RPi.GPIO as GPIO
import time
from leds import Leds


leds = Leds()

class Mouvement():
    broche = 17
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(broche, GPIO.IN)
    # Pinout leds
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)


    def detectMove(self, socketIo):
        previousstate = 0
        while True:
            # Lecture du capteur
            currentstate = GPIO.input(self.broche,)
            # Si le capteur est déclenché
            if currentstate == 1 and previousstate == 0:
                socketIo.emit('MoveOn', 'mouvement détecté', Broadcast=True)
                leds.led_on('1')
                # En enregistrer l'état
                previousstate = 1
            # Si le capteur est stabilisé
            elif currentstate == 0 and previousstate == 1:
                socketIo.emit('MoveOff', 'aucun mouvement', Broadcast=True)
                leds.led_on('2')
                previousstate = 0
            # On attends 10ms

