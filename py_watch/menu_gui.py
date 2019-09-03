import sh1106
from machine import Pin, I2C

class Menu():
    def __init__(self):
        self.i2c = I2C(scl=Pin(16), sda=Pin(17), freq=400000)
        self.display = sh1106.SH1106_I2C(128, 64, self.i2c, Pin(16), 0x3c)
        self.display.sleep(False)
        self.display.rotate(True,update=True)
        self.refresh()
        self.y_values = [1,11,21,31,41,51]
        self.menu_options = list()
        
    def setMenuList(self, menuList):
        self.menu_options = menuList

    def drawBorder(self):
        self.display.rect(0 , 0, 128, 64, 1)

    def refresh(self):
        self.drawBorder()
        self.display.hline
        self.display.show()
        self.display.fill(0)

    def drawSelect(self, y_pos, color):
        self.display.fill_rect(2, y_pos, 123, 11, color)

    def renderText(self, text, y_pos, color):
        self.display.text(text, 2, y_pos, color)

    def initMenuOptions(self, menuName):
        for option in menuName:
            self.renderText(option.get('name'), self.y_values[menuName.index(option)]+2, 1)

    def renderOptions(self, row, options):
        for option in options:
            if options.index(option) == row:
                self.renderText(option.get('name'), self.y_values[options.index(option)]+2, 0)
            else:
                self.renderText(option.get('name'), self.y_values[options.index(option)]+2, 1)