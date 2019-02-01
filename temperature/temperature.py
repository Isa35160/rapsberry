from flask import Flask
app = Flask(__name__)
app.debug = True

from leds import Leds
from tempsensor import TemperatureSensor
from flask import render_template


tep = TemperatureSensor()
led1 = Leds()
led2 = Leds()


@app.route('/')
def read_temp():
    temp_c = tep.WarningTemperature()
    if temp_c < 22:
        message = 'froid'
        led1.led_on('2')
        led2.led_of('1')
    elif 22 <= temp_c < 23:
        message = 'bon'
        led2.led_of('1')
        led2.led_of('2')
    else:
        message = 'chaud'
        led1.led_on('1')
        led2.led_of('2')
    return render_template('temperature.html', message=message, temp_c=temp_c)
