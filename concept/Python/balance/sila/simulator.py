from threading import Thread
import time
import random
from pint import UnitRegistry
ureg = UnitRegistry()
Q_ = ureg.Quantity

class Simulator(Thread):

    def __init__(self, value):
        Thread.__init__(self)
        self.__target = value
        self.start()

    def run(self):
        while(True):
            # Sleep
            slp = random.randint(0,10)
            time.sleep(slp)

            # Generate new random value
            new_value = random.random()*2000
            #print(new_value)
            self.__target.weight = Q_(new_value, 'g')
