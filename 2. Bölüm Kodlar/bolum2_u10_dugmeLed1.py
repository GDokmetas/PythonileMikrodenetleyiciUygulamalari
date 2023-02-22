from machine import *
import time

kirmizi_led = Pin(5, Pin.OUT)
sari_led = Pin(18, Pin.OUT)
yesil_led = Pin(19, Pin.OUT)
dugme_1 = Pin(17, Pin.IN)
dugme_2 = Pin(16, Pin.IN)

kirmizi_led.value(0)
sari_led.value(0)
yesil_led.value(0)

while True:
    if(dugme_1.value() != 1):
        kirmizi_led.on()
    else:
        kirmizi_led.off()
    
    if(dugme_2.value() != 1):
        sari_led.on()
    else:
        sari_led.off()
    