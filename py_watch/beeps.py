from machine import Pin, PWM
import time

class Beeper():
    def __init__(self):
        self.beeper = PWM(Pin(32), freq=0, duty=0)
        self.soundOn = True
        # self.beeper.deinit()

    def soundOn(self):
        return self.soundOn

    def deinit(self):
        self.beeper.deinit()

    def reinit(self, f, d):
        self.beeper = PWM(Pin(32), freq=f, duty=d)

    def playUpTone(self):
        # self.reinit(262, 512)
        self.beeper.freq(262)
        self.beeper.duty(512)
        time.sleep(.1)
        self.beeper.freq(523)
        self.beeper.duty(512)
        time.sleep(.1)
        # self.deinit()
        self.beeper.freq(0)
        self.beeper.duty(0)

    def playDownTone(self):
        # self.reinit(523, 512)
        self.beeper.freq(523)
        self.beeper.duty(512)
        time.sleep(.1)
        self.beeper.freq(262)
        self.beeper.duty(512)
        time.sleep(.1)
        # self.deinit()
        self.beeper.freq(0)
        self.beeper.duty(0)

    def playSelectTone(self):
        # self.reinit(523, 512)
        self.beeper.freq(523)
        self.beeper.duty(512)
        time.sleep(.1)
        self.beeper.freq(0)
        self.beeper.duty(0)
        # self.deinit()