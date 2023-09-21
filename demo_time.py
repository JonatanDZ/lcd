import drivers
from time import sleep
from datetime import  datetime
from multiprocessing import Process

display = drivers.Lcd()

def updateTime():
    while True:
        now = datetime.now().time()
        display.lcd_display_string(f'    {now.replace(microsecond=0)}',2)
        sleep(1)

p = Process(target=updateTime)

try:
    print("Skriver til LCD skaermen")
    
    p.start()

    while True:
        display.lcd_clear()
        display.lcd_display_string("   Klokken er:", 1)
        sleep(6)
        display.lcd_display_string("Det regner i dag", 1)
        sleep(6)

except KeyboardInterrupt:
    print("Slukker for uret")
    display.lcd_clear()

