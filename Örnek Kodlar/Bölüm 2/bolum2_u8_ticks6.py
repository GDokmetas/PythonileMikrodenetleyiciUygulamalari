import time
from machine import *
freq(240000000)
kirmizi_led = Pin(5, Pin.OUT)

sonlandirma_5s = time.ticks_add(time.ticks_ms(), 5000)
sayma_degeri = 0

while time.ticks_diff(sonlandirma_5s, time.ticks_ms()) > 0:
    kirmizi_led.on()
    kirmizi_led.off()
    kirmizi_led.on()
    kirmizi_led.off()
    kirmizi_led.on()
    kirmizi_led.off()
    kirmizi_led.on()
    kirmizi_led.off()
    kirmizi_led.on()
    kirmizi_led.off()
    kirmizi_led.on()
    kirmizi_led.off()
    sayma_degeri += 1

print("5 saniye icinde {0} kere kodumuz calisti".format(sayma_degeri))
