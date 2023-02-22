import time
from machine import *

kirmizi_led = Pin(5, Pin.OUT)

sonlandirma_5s = time.ticks_add(time.ticks_ms(), 5000)
sayma_degeri = 0
while time.ticks_diff(sonlandirma_5s, time.ticks_ms()) > 0:
    kirmizi_led.value(1)
    time.sleep_ms(100)
    kirmizi_led.value(0)
    time.sleep_ms(100)
    sayma_degeri += 1

print("5 saniye icinde {0} kere kodumuz calisti".format(sayma_degeri))
