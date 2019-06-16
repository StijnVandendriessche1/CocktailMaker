from domein import cocktail_machine
from RPi import GPIO
GPIO.setmode(GPIO.BCM)
import time
from domein import cocktail_machine

machine = cocktail_machine.cocktailmachine()
#motor=[26, 19, 13, 6, 5, 21, 20, 16]
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(motor, GPIO.OUT)

try:
    #GPIO.output(motor, GPIO.HIGH)
    #time.sleep(60)
    #GPIO.output(motor, GPIO.LOW)
    time.sleep(2)
    m = machine.maak_cocktail("2Q0.5N1Q1")
    print(m)
except Exception as e:
    print(e)
finally:
    #GPIO.output(motor, GPIO.LOW)
    print("klaar")
    GPIO.cleanup()