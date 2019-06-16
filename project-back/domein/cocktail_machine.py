import time
from domein.Deur import Deur
from domein.Ultrasonesensor import ultra_soon
from domein.Infaroodsensor import infra_rood
import time
from RPi import GPIO

class cocktailmachine:

    aan_het_maken = False

    def __init__(self, motor=[26, 19, 13, 6, 5, 21, 20, 16]):
        GPIO.setmode(GPIO.BCM)
        self.motor = motor
        GPIO.setup(motor, GPIO.OUT)
        self.ir = infra_rood()
        self.ultra = ultra_soon()
        self.deur = Deur()

    def maak_cocktail(self, code):
        steps = self.__get_steps(code)
        if self.deur.closed and self.ir.detect:
            for i in range(len(steps)):
                #print("step {0}:".format(i+1))
                for j in range(len(steps[i])):
                    #print("drink {0}:".format(j+1))
                    #print("id: {0}, quantity: {1}".format(steps[i][j][0], steps[i][j][1]))
                    stop = time.time() + float(steps[i][j][1]) *8
                    GPIO.output(self.motor[int(steps[i][j][0])-1], GPIO.HIGH)
                    while stop > time.time():
                        if not self.deur.closed or not self.ir.detect:
                            GPIO.output(self.motor[int(steps[i][j][0]) - 1], GPIO.LOW)
                            pauze = stop - time.time()
                            while not self.deur.closed or not self.ir.detect:
                                pass
                            stop = time.time() + pauze
                            GPIO.output(self.motor[int(steps[i][j][0]) - 1], GPIO.HIGH)
                        elif self.ultra.get_avg_distance() < 12:
                            if self.ultra.get_avg_distance(1) < 12:
                                GPIO.output(self.motor[int(steps[i][j][0]) - 1], GPIO.LOW)
                                return "shaker is te vol"
                    GPIO.output(self.motor[int(steps[i][j][0])-1], GPIO.LOW)
            GPIO.output(self.motor, GPIO.LOW)
            return "cocktail werd succesvol gemaakt"
        elif self.deur.closed and not self.ir.detect:
            GPIO.output(self.motor, GPIO.LOW)
            return "er werd geen shaker gedetecteerd, plaats een shaker en probeer het opnieuw"
        elif not self.deur.closed and self.ir.detect:
            GPIO.output(self.motor, GPIO.LOW)
            return "deur moet gesloten zijn, sluit de deur en probeer het opnieuw"
        else:
            GPIO.output(self.motor, GPIO.LOW)
            return "plaats een shaker en sluit de deur, probeer dan opnieuw"


    def __get_steps(self, code):
        code = str.upper(code)
        steps = []
        for i in range(code.count("X")):
            steps.append(code[:code.find("X")])
            code = code[code.find("X") + 1:]
        steps.append(code)
        inst = []
        for step in steps:
            drinks = []
            for i in range(step.count("N")):
                drinks.append(step[:step.find("N")])
                step = step[step.find("N") + 1:]
            drinks.append(step)
            inst.append(drinks)
        out = []
        for i in inst:
            y = []
            for q in i:
                x = []
                x.append(q[:q.find("Q")])
                q = q[q.find("Q") + 1:]
                x.append(q)
                y.append(x)
            out.append(y)
        return out