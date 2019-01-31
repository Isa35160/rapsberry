from flask import Flask
app = Flask(__name__)

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello/<name>')
def hello(name):
    return 'Hello %s' % name

@app.route('/led/<name>')
def switch(name):
    if name == 'on':
        GPIO.output(14, GPIO.HIGH)
        GPIO.output(15, GPIO.HIGH)
    elif name == 'off' :
        GPIO.output(14, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)
    return 'Name %' % name



@app.route('/on')
def on():
    GPIO.output(14, GPIO.HIGH)
    GPIO.output(15, GPIO.HIGH)
    print("Led ON")

@app.route('/off')
def off():
    GPIO.output(14, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
    print("Led OFF")
