import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.OUT)

try:
    while True:
        GPIO.output(3, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(3, GPIO.LOW)
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
