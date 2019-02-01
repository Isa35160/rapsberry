import RPi.GPIO as GPIO

class Leds:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT)

    def led_on(self, number):
        if number == '1':
            GPIO.output(18, GPIO.HIGH)
        elif number == '2':
            GPIO.output(23, GPIO.HIGH)

    def led_of(self, number):
        if number == '1':
            GPIO.output(18, GPIO.LOW)
        elif number == '2':
            GPIO.output(23, GPIO.LOW)
