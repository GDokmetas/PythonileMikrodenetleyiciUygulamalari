import time
from machine import *

kirmizi_led = Pin(5, Pin.OUT)
sari_led = Pin(18, Pin.OUT)
yesil_led = Pin(19, Pin.OUT)

kirmizi_led_yanma_zamani = time.ticks_add(time.ticks_ms(), 5000)
sari_led_yanma_zamani = time.ticks_add(time.ticks_ms(), 6000)
yesil_led_yanma_zamani = time.ticks_add(time.ticks_ms(), 7000)

while True:
    if time.ticks_diff(kirmizi_led_yanma_zamani, time.ticks_ms()) < 0:
        kirmizi_led.value(1)
    if time.ticks_diff(sari_led_yanma_zamani, time.ticks_ms()) < 0:
        sari_led.value(1)
    if time.ticks_diff(yesil_led_yanma_zamani, time.ticks_ms()) < 0:
        yesil_led.value(1)
    
    if kirmizi_led.value() == 1 and sari_led.value() == 1 and yesil_led.value() == 1:
        print("Butun LED'ler yandi!!")
        break
    