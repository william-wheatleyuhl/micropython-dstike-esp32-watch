# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#import sh1106
#esp.osdebug(None)
#import webrepl
#webrepl.start()        

# def get_button_state():
#         import button_listener
#         active_pin = button_listener.checkPinState()
#         # print(active_pin)
#         return active_pin


def button():
        import time
        from machine import Pin
        from button_listener import ButtonListener
        from menu_gui import Menu

        menu = Menu()
        bl = ButtonListener()
        moved = False
        row = 0
        y_values = [1,11,21,31,41,51]
        # menu_options = ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5', 'Option 6']
        

        menu.drawBorder()
        led = Pin(27, Pin.OUT, Pin.PULL_DOWN)
        led.value(1)
        menu.refresh()


        while True:
                led_status = led.value()
                active_butt = bl.checkPinState()
                # menu.display.rect(0 , 0, 128, 64, 1)
                if active_butt != 'none' and moved == False:
                        # menu.display.rect(0 , 0, 128, 64, 1)
                        menu.drawSelect(y_values[row], 1)
                        menu.renderOptions(row)
                        menu.refresh()
                        moved = True

                if row < 5 and (active_butt == 'down' and moved == True):
                        row += 1
                        # menu.display.rect(0 , 0, 128, 64, 1)
                        menu.drawSelect(y_values[row], 1)
                        menu.renderOptions(row)
                        menu.refresh()

                if row > 0 and (active_butt == 'up' and moved == True):
                        row -= 1
                        # menu.display.rect(0 , 0, 128, 64, 1)
                        menu.drawSelect(y_values[row], 1)
                        menu.renderOptions(row)
                        menu.refresh()

                if active_butt == 'side_b' and led_status == 1:
                        led.value(0)
                        time.sleep(.25)
                elif active_butt == 'side_b' and led_status == 0:
                        led.value(1)
                        time.sleep(.25)
                        
                # display.text('{}'.format(active_butt), 2, 2, 1)
                time.sleep(.1)

