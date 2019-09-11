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
        from event_handler import EventHandler

        menu = Menu()
        eh = EventHandler()
        bl = ButtonListener()

        row = 0
        y_values = [1,11,21,31,41,51]

        led = Pin(27, Pin.OUT, Pin.PULL_DOWN)
        led.value(1)

        menu.setMenuList(eh.getMainMenuList())
        currentMenu = menu.menu_options
        menu.drawSelect(y_values[row], 1)
        menu.renderOptions(row, currentMenu)
        menu.refresh()

        while True:
                led_status = led.value()
                active_butt = bl.checkPinState()

                if row < len(menu.menu_options)-1 and (active_butt == 'down'):
                        row += 1
                        eh.parseEvent(active_butt)
                        menu.moveSelection(row, currentMenu)
                        time.sleep(.15)

                if row > 0 and (active_butt == 'up'):
                        row -= 1
                        eh.parseEvent(active_butt)
                        menu.moveSelection(row, currentMenu)
                        time.sleep(.15)

                if active_butt == 'center':
                        eh.parseEvent(active_butt)
                        if isinstance(menu.menu_options[row].get('action'), dict):
                                menu.setMenuList(eh.parseEvent(menu.menu_options[row].get('action')))
                                currentMenu = menu.menu_options
                                row = 0
                                menu.moveSelection(row, currentMenu)
                                time.sleep(.5)
                        else:
                                menu.setMenuList(eh.getEvent(menu.menu_options[row].get('action')))
                                currentMenu = menu.menu_options
                                row = 0
                                menu.moveSelection(row, currentMenu)
                                time.sleep(.5)

                if active_butt == 'side_b' and led_status == 1:
                        led.value(0)
                        time.sleep(.25)
                elif active_butt == 'side_b' and led_status == 0:
                        led.value(1)
                        time.sleep(.25)
                        

