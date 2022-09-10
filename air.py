import RPi.GPIO as GPIO
import time
import sys

sensorPin = 5
relayPin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensorPin, GPIO.IN)
GPIO.setup(relayPin, GPIO.OUT)

try:
    while True:
        kondisiSensor = GPIO.input(sensorPin)
        print(GPIO.input(sensorPin))
        print('- kondisi sensor ',("basah" if kondisiSensor == 0 else "kering"))
        if kondisiSensor == 1:
            print('masuk kondisi kering')
            status = GPIO.output(relayPin, GPIO.HIGH)
            print(status)
        else:
            print('masuk kondisi basah')
            status = GPIO.output(relayPin, GPIO.LOW)
            print(status)
        time.sleep(2)
finally:
    GPIO.cleanup()