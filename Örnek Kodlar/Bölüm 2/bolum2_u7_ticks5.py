import time
from machine import *
freq(240000000)
kirmizi_led = Pin(5, Pin.OUT)

sonlandirma_5s = time.ticks_add(time.ticks_ms(), 5000)
sayma_degeri = 0
onceki_us = 0
simdiki_us = 0
bekleme_araligi = 100000

while time.ticks_diff(sonlandirma_5s, time.ticks_ms()) > 0:
    simdiki_us = time.ticks_us()
    if(time.ticks_diff(simdiki_us, onceki_us) > bekleme_araligi):
        onceki_us = simdiki_us
        if(kirmizi_led.value() == 0):
            kirmizi_led.value(1)
        else:
            kirmizi_led.value(0)
    sayma_degeri += 1

print("5 saniye icinde {0} kere kodumuz calisti".format(sayma_degeri))
