import drivers
from time import sleep
from datetime import  datetime

display = drivers.Lcd()



try:
    print("Skriver til LCD skaermen")
    display.lcd_display_string("Dato: ", 1)
    while True:
        now = datetime.now().time()
        display.lcd_display_string("   Klokken er:", 1)
        now = datetime.now().time()
        display.lcd_display_string(f'    {now.replace(microsecond=0)}',2)
        sleep(1)
        now = datetime.now().time()
        sleep(1)
        now = datetime.now().time()
        sleep(1)
        now = datetime.now().time()
        sleep(1)
        now = datetime.now().time()
        sleep(1)
        now = datetime.now().time()
        sleep(1)
        now = datetime.now().time()
        display.lcd_display_string("Det regner i dag", 1)   # Refresh the first line of display with a different message
        now = datetime.now().time()
        sleep(1)                                           # Give time for the message to be read
        now = datetime.now().time()
        sleep(1)                                           # Give time for the message to be read
        now = datetime.now().time()
        sleep(1)   
        now = datetime.now().time()
        sleep(1)                                           # Give time for the message to be read
        display.lcd_clear()                                # Clear the display of any data
        sleep(1)                                           # Give time for the message to be read
    
except KeyboardInterrupt:
    print("Slukker for uret")
    display.lcd_clear()