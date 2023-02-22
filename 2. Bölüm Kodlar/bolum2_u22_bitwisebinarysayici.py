from machine import *
import time
led_no = [23, 22, 21, 19, 18, 5, 17, 16]
led = [] # boş liste oluştur
for i in led_no:
    led.append(Pin(i, Pin.OUT))

deger = 0 # sayaç değeri
while True:
    for index in range(0, 8):
        pin_value = (deger >> index) & 0x01
        led[index].value(pin_value)
        
    deger += 1 # gösterim bittikten sonra sayacı bir artır
    if deger > 255: # taşmayı engelle
        deger = 0
    time.sleep_ms(500)
