import time
from domein.Deur import Deur
from domein.Ultrasonesensor import ultra_soon
from domein.Infaroodsensor import infra_rood
from RPi import GPIO
GPIO.setmode(GPIO.BCM)

motor = [26, 19, 13, 6, 5, 21, 20, 16]
infra = infra_rood()
ultra = ultra_soon()
deur = Deur()

GPIO.setup(motor, GPIO.OUT)

def deur_changed(a):
    print("deur = " + str(deur.closed))

def infra_changed(a):
    print("object detected = " + str(infra.detect))

try:
    deur.on_change(deur_changed)
    infra.on_change(infra_changed)
    while True:
        print(ultra.get_avg_distance())
        time.sleep(1)
except Exception as e:
    print(e)
finally:
    GPIO.cleanup()
    print('gestopt')