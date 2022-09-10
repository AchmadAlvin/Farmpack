import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

#relay pupuk
relay = 24
GPIO.cleanup()
GPIO.setup (relay, GPIO.OUT)

def set_relay (state) :
    if state ==  "high" :
        GPIO.output (17, GPIO.HIGH)
    if state == "low" :
        GPIO.output (17, GPIO. LOW)
        
if __name__ == "__main__" :
        while True:
            print("nyala" )
            GPIO.output("high")
            time.sleep(1)
            print("mati")
            GPIO.output("low")
            time.sleep(1)