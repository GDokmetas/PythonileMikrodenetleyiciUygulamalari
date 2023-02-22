from machine import *
import time

kirmizi_led = Pin(5, Pin.OUT)
sari_led = Pin(18, Pin.OUT)
yesil_led = Pin(19, Pin.OUT)

kirmizi_led.value(0)
sari_led.value(0)
yesil_led.value(0)

while True:
    # kirmizi
    kirmizi_led.value(1)
    sari_led.value(0)
    yesil_led.value(0)
    time.sleep_ms(4000)
    #sari
    sari_led.value(1)
    time.sleep_ms(1000)
    #yesil
    kirmizi_led.value(0)
    sari_led.value(0)
    yesil_led.value(1)
    time.sleep_ms(4000)
    #yesil-sari
    sari_led.value(1)
    time.sleep_ms(1000)
    
    