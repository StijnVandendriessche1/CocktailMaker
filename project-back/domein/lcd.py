#datapins invoeren van D7 naar D0
from RPi import GPIO
import time
from smbus import SMBus

i2c = SMBus()
i2c.open(1)
GPIO.setmode(GPIO.BCM)

inst = {"function_set": 0b00111000, "display_on": 0b00001111, "clear_display_&_cursor_home": 0b00000001, "new_line": 0b11000000}


class Lcd:

    def __init__(self, E = 27, RS = 17):
        self.E = E
        self.RS = RS
        GPIO.setup([self.E, self.RS], GPIO.OUT)
        GPIO.output(self.E, GPIO.HIGH)
        self.send_instruction(inst["function_set"])
        self.send_instruction(inst["display_on"])
        self.send_instruction(inst["clear_display_&_cursor_home"])

    def send_instruction(self, value):
        GPIO.output(self.RS, GPIO.LOW)
        GPIO.output(self.E, GPIO.HIGH)
        self.set_data_bits(value)
        GPIO.output(self.E, GPIO.LOW)
        time.sleep(0.01)
        GPIO.output(self.E, GPIO.HIGH)

    def send_character(self, value):
        GPIO.output(self.RS, GPIO.HIGH)
        GPIO.output(self.E, GPIO.HIGH)
        self.set_data_bits(value)
        GPIO.output(self.E, GPIO.HIGH)
        GPIO.output(self.E, GPIO.LOW)

    def set_data_bits(self, byte):
        i2c.write_byte(0x38, byte)

    def write_message(self, value):
        for i in value:
            self.send_character(ord(i))

    def new_line(self):
        self.send_instruction(inst["new_line"])

    def write_scroll(self, head, boodschap):
        self.send_instruction(0b00000001)
        if len(boodschap) > 16:
            b = boodschap
            lijst = []
            for i in b:
                lijst.append(i)
            for i in range(40 - lijst.__len__()):
                lijst.append(" ")
            for i in range(50):
                self.send_instruction(inst["clear_display_&_cursor_home"])
                self.write_message(head)
                self.new_line()
                for j in range(i, i + 16):
                    self.send_character(ord(lijst[j]))
                time.sleep(0.2)
        else:
            self.write_message(head)
            self.new_line()
            self.write_message(boodschap)