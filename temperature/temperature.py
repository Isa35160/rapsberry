from flask import Flask

app = Flask(__name__)
app.debug = True

# Imports
from flask import render_template
import os
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

# Intialisation des broches
os.system('modprobe w1-gpio')  # Allume le module 1wire
os.system('modprobe w1-therm')  # Allume le module Temperature

# Chemin du fichier contenant la température (remplacer par votre valeur trouvée précédemment)
device_file = '/sys/bus/w1/devices/28-01131a446afe/w1_slave'


# @app.route('/')
class TemperatureSensor:

    def read_temp_raw(self):
        f = open(device_file, 'r')  # Ouvre le dichier
        lines = f.readlines()  # Returns the text
        f.close()
        return lines

    # Lis la temperature
    def Convert(self):
        choice = str(input('Choose your degrees Celsius or Fahrenheit (1 or 2) : \n'))
        lines = self.read_temp_raw()  # Lit le fichier de température
        # Tant que la première ligne ne vaut pas 'YES', on attend 0,2s
        # On relis ensuite le fichier
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.read_temp_raw()
        # On cherche le '=' dans la seconde ligne du fichier
        equals_pos = lines[1].find('t=')
        # Si le '=' est trouvé, on converti ce qu'il y a après le '=' en degrées celcius
        if equals_pos != -1 and choice == '1':
            temp_string = lines[1][equals_pos + 2:]
            temp_c = float(temp_string) / 1000.0
            print(temp_c, 'degrés celscius')
            # si choix fahreinheit
        elif equals_pos != -1 and choice == '2':
            temp_string = lines[1][equals_pos + 2:]
            temp_f = float(temp_string) / 1000.0 * 9 / 5 + 32
            print(temp_f, 'degrés fahrenheit')

    def WarningTemperature(self):
        lines = self.read_temp_raw()  # Lit le fichier de température
        # Tant que la première ligne ne vaut pas 'YES', on attend 0,2s
        # On relis ensuite le fichier
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.read_temp_raw()
        # On cherche le '=' dans la seconde ligne du fichier
        equals_pos = lines[1].find('t=')
        # Si le '=' est trouvé, on converti ce qu'il y a après le '=' en degrées celcius
        if equals_pos != -1:
            temp_string = lines[1][equals_pos + 2:]
            temp_c = float(temp_string) / 1000.0

            return temp_c


tep = TemperatureSensor()


# tep.read_temp_raw()
# tep.WarningTemperature()


class Leds:

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


led1 = Leds()
led2 = Leds()


@app.route('/')
def read_temp():
    temp_c = tep.WarningTemperature()
    if temp_c < 18:
        message = 'froid'
        led1.led_on('2')
        led2.led_of('1')
    elif 18 <= temp_c < 20:
        message = 'bon'
        led2.led_of('1')
        led2.led_of('2')
    else:
        message = 'chaud'
        led1.led_on('1')
        led2.led_of('2')
    return render_template('temperature.html', message=message, temp_c=temp_c)
