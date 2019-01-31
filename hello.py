from flask import Flask
app = Flask(__name__)

from flask import render_template

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)


@app.route('/')
def hello_world():
    return render_template('base.html')


@app.route('/hello/<status>')
def hello(status):
    return 'Hello %s' % status


@app.route('/led/<number>/<status>')
def swicthOne(number, status):
    if status == 'on' and number == '1':
        GPIO.output(14, GPIO.HIGH)
    elif status == 'on' and number == '2':
        GPIO.output(15, GPIO.HIGH)
    elif status == 'off' and number == '1':
        GPIO.output(14, GPIO.LOW)
    elif status == 'off' and number == '2':
        GPIO.output(15, GPIO.LOW)

    return render_template('base.html', status=status, number=number)



@app.route('/leds/<status>')
def switchAll(status):
    if status == 'on':
        GPIO.output(14, GPIO.HIGH)
        GPIO.output(15, GPIO.HIGH)
        print("Led ON")
    elif status == 'off':
        GPIO.output(14, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)
        print("Led OFF")

    return render_template('base.html', status=status)