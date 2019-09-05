from menus import MenuOptions
from beeps import Beeper

class EventHandler():
    def __init__(self):
        self.mo = MenuOptions()
        self.beeper = Beeper()

    def getMainMenu(self):
        return self.mo.mainMenu

    def getMenuList(self, menu):
        return self.mo.getMenuOpts(menu)

    def getMainMenuList(self):
        return self.mo.getMenuOpts(self.mo.mainMenu)

    def parseEvent(self, event):
        # print("Parsing {}".format(event))
        if isinstance(event, dict):
            return self.getMenu(event)
        else:
            return self.getEvent(event)

    def getEvent(self, event):
        if event == 'goBack':
            menuList = self.mo.getMenuOpts(self.mo.mainMenu)
            return menuList
        if event == 'up':
            if self.beeper.soundOn == True:
                self.beeper.playUpTone()
        if event == 'down':
            if self.beeper.soundOn == True:
                self.beeper.playDownTone()
        if event == 'center':
            if self.beeper.soundOn == True:
                self.beeper.playSelectTone()
        if event == 'soundOff' and self.beeper.soundOn == True:
            self.beeper.deinit()
            self.beeper.soundOn = False
            self.mo.soundMenu.get('soundOn')['name'] = '[ ] Sound On'
            self.mo.soundMenu.get('soundOff')['name'] = '[X] Sound Off'
            menuList = self.mo.getMenuOpts(self.mo.soundMenu)
            return menuList
        if event == 'soundOn' and self.beeper.soundOn == False:
            self.beeper.reinit(0, 0)
            self.beeper.soundOn = True
            # on = '[X] Sound On'
            self.mo.soundMenu.get('soundOn')['name'] = '[X] Sound On'
            self.mo.soundMenu.get('soundOff')['name'] = '[ ] Sound Off'
            self.beeper.playSelectTone()
            menuList = self.mo.getMenuOpts(self.mo.soundMenu)
            return menuList

    def getMenu(self, event):
        menuList = self.mo.getMenuOpts(event)
        return menuList
