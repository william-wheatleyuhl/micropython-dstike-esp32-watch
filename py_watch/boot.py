# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#import sh1106
#esp.osdebug(None)
#import webrepl
#webrepl.start()        

def button():
        import time
        from beeps import Beeper
        from machine import Pin
        from button_listener import ButtonListener
        from menu_gui import Menu
        from menus import MenuOptions

        menu = Menu()
        mo = MenuOptions()
        bl = ButtonListener()
        beeper = Beeper()
        row = 0
        y_values = [1,11,21,31,41,51]

        led = Pin(27, Pin.OUT, Pin.PULL_DOWN)
        led.value(1)

        
        menu.setMenuList(mo.getMenuOpts(mo.mainMenu))
        currentMenu = menu.menu_options
        # previousMenu = currentMenu
        # menu.initMenuOptions(currentMenu)
        menu.drawSelect(y_values[row], 1)
        menu.renderOptions(row, currentMenu)
        menu.refresh()

        while True:
                led_status = led.value()
                active_butt = bl.checkPinState()
                # if active_butt != 'none' and moved == False:
                #         menu.drawSelect(y_values[row], 1)
                #         menu.renderOptions(row, currentMenu)
                #         menu.refresh()
                #         moved = True
                #         time.sleep(.15)


                if row < len(menu.menu_options)-1 and (active_butt == 'down'):
                        row += 1
                        beeper.playDownTone()
                        menu.drawSelect(y_values[row], 1)
                        menu.renderOptions(row, currentMenu)
                        menu.refresh()
                        time.sleep(.15)
                        print(row)

                if row > 0 and (active_butt == 'up'):
                        row -= 1
                        beeper.playUpTone()
                        menu.drawSelect(y_values[row], 1)
                        menu.renderOptions(row, currentMenu)
                        menu.refresh()
                        time.sleep(.15)
                        print(row)

                if active_butt == 'center':
                        if menu.menu_options[row].get('action') != 'goBack':
                                menu.setMenuList(mo.getMenuOpts(menu.menu_options[row].get('action')))
                        else:
                                menu.setMenuList(mo.getMenuOpts(mo.mainMenu))
                        currentMenu = menu.menu_options
                        # menu.initMenuOptions(currentMenu)
                        row = 0
                        menu.drawSelect(y_values[row], 1)
                        menu.renderOptions(row, currentMenu)
                        beeper.playSelectTone()
                        moved = False
                        menu.refresh()
                        time.sleep(.5)

                if active_butt == 'side_b' and led_status == 1:
                        led.value(0)
                        time.sleep(.25)
                elif active_butt == 'side_b' and led_status == 0:
                        led.value(1)
                        time.sleep(.25)
                        
