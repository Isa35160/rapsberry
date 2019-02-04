import RPi.GPIO as GPIO
import time

class Leds:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(24, GPIO.OUT)

    def led_on(self, number):
        if number == '1':
            GPIO.output(18, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(18, GPIO.LOW)
            time.sleep(1)

        elif number == '2':
            GPIO.output(24, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(24, GPIO.LOW)
            time.sleep(1)

    def led_of(self, number):
        if number == '1':
            GPIO.output(18, GPIO.LOW)
        elif number == '2':
            GPIO.output(24, GPIO.LOW)

    def blink(self):
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(18, GPIO.LOW)
        GPIO.output(18, GPIO.HIGH)
