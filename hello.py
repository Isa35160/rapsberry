from flask import Flask
app = Flask(__name__)

from led import led.py
import RPi.GPIO as GPIO

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello/<name>')
def hello(name):
    return 'Hello %s' % name

@app.route('/on')
def on():
    led = pyb.LED()
    while True:
        led.toggle()
        pyb.delay(1000)
