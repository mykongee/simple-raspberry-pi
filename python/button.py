import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN)
pull_up_down = GPIO.PUD_UP

try:
    while True:
        if GPIO.input(3) == GPIO.LOW:
            print("Switch pressed.")
            break
            GPIO.cleanup()

except KeyboardInterrupt:
    GPIO.cleanup()
    
