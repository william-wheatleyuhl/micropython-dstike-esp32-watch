from machine import Pin

##CONSTANTS
WHEEL_UP = Pin(19, Pin.IN, Pin.PULL_UP)
WHEEL_CENTER = Pin(18, Pin.IN, Pin.PULL_UP)
WHEEL_DOWN = Pin(5, Pin.IN, Pin.PULL_UP)
SIDE_A = Pin(22, Pin.IN, Pin.PULL_UP)
SIDE_B = Pin(23, Pin.IN, Pin.PULL_UP)

class ButtonListener():
    def __init__(self):
        print("butts are ready")

    def checkPinState(self):
        if WHEEL_UP.value() == 0:
            return 'up'
        elif WHEEL_CENTER.value() == 0:
            return 'center'
        elif WHEEL_DOWN.value() == 0:
            return 'down'
        elif SIDE_A.value() == 0:
            return 'side_a'
        elif SIDE_B.value() == 0:
            return 'side_b'
        else:
            return 'none'
