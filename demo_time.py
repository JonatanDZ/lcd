import drivers
from time import sleep
from datetime import  datetime

display = drivers.Lcd()

try:
    print("Skriver til LCD skaermen")
    display.lcd_display_string("Klokken er:", 1)
    while True:
        display.lcd_display_string(str(datetime.now().time()),2)
    
except KeyboardInterrupt:
    print("Slukker for uret")
    display.lcd_clear()