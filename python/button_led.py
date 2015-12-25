import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(3, GPIO.IN)
GPIO.setup(17, GPIO.OUT)

try:
    while True:
        if GPIO.input(3) == GPIO.LOW:
            # blink several times
            for x in range(0,10):
                GPIO.output(17, GPIO.LOW)
                time.sleep(0.1)
                GPIO.output(17, GPIO.HIGH)
                time.sleep(0.3)
            
except KeyboardInterrupt:
    GPIO.cleanup()
