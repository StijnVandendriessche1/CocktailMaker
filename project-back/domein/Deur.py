from RPi import GPIO
GPIO.setmode(GPIO.BCM)


class Deur:
    def __init__(self, pin=24, bouncetime=200):
        self.pin = pin
        self.bouncetime = bouncetime

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    @property
    def closed(self):
        ingedrukt = GPIO.input(self.pin)
        return not ingedrukt

    def on_change(self, call_method):
        GPIO.add_event_detect(self.pin, GPIO.BOTH, call_method, bouncetime=self.bouncetime)

    def on_release(self, call_method):
        GPIO.add_event_detect(self.pin, GPIO.RISING, call_method, bouncetime=self.bouncetime)