from RPi import GPIO
from domein import lcd
from subprocess import check_output
GPIO.setmode(GPIO.BCM)

lcd = lcd.Lcd()

try:
    ip = check_output(['hostname', '--all-ip-addresses'])
    ips = ip.split()
    print(ips)
    lcd.write_message(str(ips[1])[2:-1])
except Exception as e:
    print(e)
finally:
    GPIO.cleanup()
    print("gestopt")