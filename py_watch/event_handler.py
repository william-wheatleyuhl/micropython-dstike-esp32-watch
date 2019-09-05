from menus import MenuOptions

class EventHandler():
    def __init__(self):
        self.mo = MenuOptions()
    def getMainMenu(self):
        return self.mo.mainMenu
    def getMenuList(self, menu):
        return self.mo.getMenuOpts(menu)
    def getMainMenuList(self):
        return self.mo.getMenuOpts(self.mo.mainMenu)
    def getEvent(self, event):
        print("Passed Event: {}".format(event))
        if isinstance(event, dict):
            return self.mo.getMenuOpts(event)
        else:
            return self.mo.getMenuOpts(self.mo.mainMenu)
