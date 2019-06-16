from RPi import GPIO
import time

class ultra_soon:

    def __init__(self, trigger = 18, echo = 23):
        GPIO.setmode(GPIO.BCM)
        self.trigger = trigger
        self.echo = echo
        GPIO.setup(trigger, GPIO.OUT)
        GPIO.setup(echo, GPIO.IN)

    def get_distance(self):
        GPIO.output(self.trigger, True)

        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.trigger, False)

        StartTime = time.time()
        StopTime = time.time()

        # save StartTime
        while GPIO.input(self.echo) == 0:
            StartTime = time.time()

        # save time of arrival
        while GPIO.input(self.echo) == 1:
            StopTime = time.time()

        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
        return distance

    def get_avg_distance(self, count=5):
        avg = 0
        for i in range(count):
            avg += self.get_distance()
        return avg / count