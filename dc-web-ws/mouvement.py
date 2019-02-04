import RPi.GPIO as GPIO
import time


class Mouvement():
    broche = 17
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(broche, GPIO.IN)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)

    def detectMove(self):
        previousstate = 0

        while True:
            # Lecture du capteur
            currentstate = GPIO.input(self.broche)
            # Si le capteur est déclenché
            if currentstate == 1 and previousstate == 0:
                GPIO.output(18, GPIO.HIGH)
                GPIO.output(22, GPIO.HIGH)
                GPIO.output(18, GPIO.LOW)
                GPIO.output(22, GPIO.LOW)
                # print("Mouvement détecté !")
                # En enregistrer l'état
                previousstate = 1
            # Si le capteur est s'est stabilisé
            elif currentstate == 0 and previousstate == 1:
                # print("Prêt")

                previousstate = 0
            # On attends 10ms
