from machine import Pin, I2C
import sh1106

i2c = I2C(scl=Pin(16), sda=Pin(17), freq=400000)
display = sh1106.SH1106_I2C(128, 64, i2c, Pin(16), 0x3c)
display.sleep(False)
display.fill(0)
display.text('Testing 1', 0, 0, 1)
display.show()