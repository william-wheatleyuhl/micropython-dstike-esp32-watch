import sh1106
from machine import Pin, I2C
from menus import MenuOptions

class Menu():
    def __init__(self):
        self.mo = MenuOptions()
        self.i2c = I2C(scl=Pin(16), sda=Pin(17), freq=400000)
        self.display = sh1106.SH1106_I2C(128, 64, self.i2c, Pin(16), 0x3c)
        self.display.sleep(False)
        self.display.rotate(True,update=True)
        self.refresh()
        self.y_values = [1,11,21,31,41,51]
        # self.menu_options = self.mo.getMenuOpts(self.mo.mainMenu)
        self.menu_options = list()
        # for option in self.menu_options:
        #     self.renderText(option.get('name'), self.y_values[self.menu_options.index(option)]+2, 1)

    def setMenuList(self, menuName):
        self.menu_options = self.mo.getMenuOpts(menuName)

    def getMenuList(self, menuName):
        return self.mo.getMenuOpts(menuName)

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