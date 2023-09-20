import drivers
from time import sleep
from datetime import  datetime

display = drivers.Lcd()

try:
    print("Skriver til LCD skaermen")
    display.lcd_display_string("Dato: ", 1)
    while True:
        display.lcd_display_string("   Klokken er:", 1)
        display.lcd_display_string(str(datetime.datetime.now().isoformat(sep=" ", timespec="seconds")),2)
        sleep(6)
        display.lcd_display_string("Det regner i dag", 1)   # Refresh the first line of display with a different message
        sleep(6)                                           # Give time for the message to be read
        display.lcd_clear()                                # Clear the display of any data
        sleep(1)   
    
except KeyboardInterrupt:
    print("Slukker for uret")
    display.lcd_clear()