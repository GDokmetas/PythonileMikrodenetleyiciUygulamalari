from machine import *
import time
led_no = [23, 22, 21, 19, 18, 5, 17, 16]
led = [] # boş liste oluştur
for i in led_no:
    led.append(Pin(i, Pin.OUT))

while True:
    for x in range(1, 8):
        print(x)
        led[x].on()
        led[x-1].off()
        time.sleep_ms(100)
        
    for x in range(7, 0, -1):
        print(x)
        led[x].off()
        led[x-1].on()
        time.sleep_ms(100)