from machine import Pin, PWM
import time

class Beeper():
    def __init__(self):
        self.beeper = PWM(Pin(32), freq=0, duty=0)

    def playUpTone(self):
        self.beeper.freq(262)
        self.beeper.duty(512)
        time.sleep(.1)
        self.beeper.freq(523)
        self.beeper.duty(512)
        time.sleep(.1)
        self.beeper.freq(0)
        self.beeper.duty(0)

    def playDownTone(self):
        self.beeper.freq(523)
        self.beeper.duty(512)
        time.sleep(.1)
        self.beeper.freq(262)
        self.beeper.duty(512)
        time.sleep(.1)
        self.beeper.freq(0)
        self.beeper.duty(0)

    def playSelectTone(self):
        self.beeper.freq(523)
        self.beeper.duty(512)
        time.sleep(.1)
        # self.beeper.freq(262)
        # self.beeper.duty(512)
        # time.sleep(.1)
        self.beeper.freq(0)
        self.beeper.duty(0)