class MenuOptions():
    def __init__(self):
        # self.buttMenu = dict()
        self.scanMenu = {
            'name' : 'The Scan Menu'
        }
        self.scanSub ={
            'scanMenu' : self.scanMenu
        }
        self.scanOption = {
            'name' : 'Scan',
            'description' : 'Scan for Wifi Networks',
            'action' : self.scanSub
        }
        self.connectMenu = {
            'name' : 'The Connection Menu'
        }
        self.connSub = {
            'connSub' : self.connectMenu
        }
        self.connectOption = {
            'name' : 'Connect',
            'description' : 'Connect to Wifi Network',
            'action' : self.connSub
        }
        self.subButt1 = {
            'name' : 'sub butt 1'
        }
        self.subButt2 = {
            'name' : 'sub butt 2'
        }
        self.subButts = {
            'subButt1' : self.subButt1,
            'subButt2' : self.subButt2,
            # 'back' : self.backOption
        }
        self.buttMenu = {
            'name': 'buttMenu',
            'action' : self.subButts
        }
        self.mainMenu = {
            'buttOption' : self.buttMenu,
            'scanOption' : self.scanOption,
            'connectOption' : self.connectOption
        }
        # self.backOption = {
        #     'name' : 'Back...',
        #     'action' : self.mainMenu
        # }
    def getMenuOpts(self, menu):
        menuOpts = list()
        for opt in menu:
            print(opt)
            menuOpts.append(menu.get(opt))
            print(menu.get(opt).get('name'))
        return menuOpts