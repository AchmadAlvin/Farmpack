import RPi.GPIO as GPIO
import time

Buzzer = 26
PIR = 19

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN)
GPIO.setup(Buzzer,GPIO.OUT)

try:
    time.sleep(1)
    while True:
        if GPIO.input(PIR) == 1:
            GPIO.output(Buzzer,GPIO.HIGH)
            print("Gerakan terdeteksi")
        else:
            print("...")
            GPIO.output(Buzzer,GPIO.LOW)

            
except KeyboardInterrupt:
    GPIO.cleanup()