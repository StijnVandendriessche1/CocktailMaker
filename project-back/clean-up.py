from RPi import GPIO
GPIO.setmode(GPIO.BCM)
import time
motor=[26, 19, 13, 6, 5, 21, 20, 16]
GPIO.setup(motor, GPIO.OUT)
GPIO.output(motor, GPIO.HIGH)
time.sleep(10)
GPIO.output(motor, GPIO.LOW)