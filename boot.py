# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#import sh1106
#esp.osdebug(None)
#import webrepl
#webrepl.start()        

def button():
        import time
        from machine import Pin
        from button_listener import ButtonListener
        from menu_gui import Menu
        from menus import MenuOptions

        menu = Menu()
        mo = MenuOptions()
        bl = ButtonListener()
        moved = False
        row = 0
        y_values = [1,11,21,31,41,51]

        led = Pin(27, Pin.OUT, Pin.PULL_DOWN)
        led.value(1)

        
        # menu.drawBorder()
        menu.setMenuList(mo.mainMenu)
        currentMenu = menu.menu_options
        menu.initMenuOptions(currentMenu)
        menu.refresh()

        while True:
                led_status = led.value()
                active_butt = bl.checkPinState()
                if active_butt != 'none' and moved == False:
                        menu.drawSelect(y_values[row], 1)
                        menu.renderOptions(row, currentMenu)
                        menu.refresh()
                        moved = True

                if row < len(menu.menu_options)-1 and (active_butt == 'down' and moved == True):
                        row += 1
                        menu.drawSelect(y_values[row], 1)
                        menu.renderOptions(row, currentMenu)
                        menu.refresh()
                        print(row)

                if row > 0 and (active_butt == 'up' and moved == True):
                        row -= 1
                        menu.drawSelect(y_values[row], 1)
                        menu.renderOptions(row, currentMenu)
                        menu.refresh()
                        print(row)

                if active_butt == 'center':
                        print(menu.menu_options[row].get('action'))
                        menu.setMenuList(menu.menu_options[row].get('action'))
                        currentMenu = menu.menu_options
                        menu.initMenuOptions(currentMenu)
                        row = 0
                        moved = False
                        menu.refresh()
                        time.sleep(.5)

                if active_butt == 'side_b' and led_status == 1:
                        led.value(0)
                        time.sleep(.25)
                elif active_butt == 'side_b' and led_status == 0:
                        led.value(1)
                        time.sleep(.25)
                        
                time.sleep(.1)

