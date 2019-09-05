class MenuOptions():
    def __init__(self):
        self.backOption = {
            'name' : 'Back...',
            'action' : 'goBack',
            'order' : 99
        }
        self.scanMenu = {
            'name' : 'The Scan Menu',
            'order' : 1
        }
        self.scanSub = {
            'scanMenu' : self.scanMenu,
            'back' : self.backOption
        }
        self.scanOption = {
            'name' : 'Scan',
            'description' : 'Scan for Wifi Networks',
            'order' : 2,
            'action' : self.scanSub
        }
        self.connectMenu = {
            'name' : 'The Connection Menu',
            'order' : 1
        }
        self.connSub = {
            'connSub' : self.connectMenu,
            'back' : self.backOption
        }
        self.connectOption = {
            'name' : 'Connect',
            'description' : 'Connect to Wifi Network',
            'order' : 1,
            'action' : self.connSub
        }
        self.subButt1 = {
            'name' : 'sub butt 1',
            'order' : 1
        }
        self.subButt2 = {
            'name' : 'sub butt 2',
            'order' : 2
        }
        self.subButts = {
            'subButt1' : self.subButt1,
            'subButt2' : self.subButt2,
            'back' : self.backOption
        }
        self.buttMenu = {
            'name': 'buttMenu',
            'order' : 4,
            'action' : self.subButts
        }
        self.soundMenu = {
            'soundOn' : {'name' : '[ ] Sound On', 'order' : 1} ,
            'soundOff' : {'name' : '[ ] Sound Off', 'order' : 2},
            'back' : self.backOption 
        }
        self.soundOption = {
            'name' : 'Sounds...',
            'order' : 3,
            'action' : self.soundMenu
        }
        self.mainMenu = {
            'buttOption' : self.buttMenu,
            'scanOption' : self.scanOption,
            'connectOption' : self.connectOption,
            'soundOption' : self.soundOption
        }

    def getMenuOpts(self, menu):
        menuOpts = self.sortMenu(menu)
        sortedMenus = list()
        for d in menuOpts:
            sortedMenus.append(d.get('dict'))
        return sortedMenus

    def sortMenu(self, menu):
        dictList = list()
        for opt in menu:
            optOrder = {'dict' : menu.get(opt), 'order' : menu.get(opt).get('order')}
            dictList.append(optOrder)
        newlist = sorted(dictList, key = lambda k: k['order'])
        return newlist