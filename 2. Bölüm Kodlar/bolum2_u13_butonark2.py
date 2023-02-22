from machine import *
import time

kirmizi_led = Pin(5, Pin.OUT)
sari_led = Pin(18, Pin.OUT)
yesil_led = Pin(19, Pin.OUT)
dugme_1 = Pin(17, Pin.IN, Pin.PULL_UP)
dugme_2 = Pin(16, Pin.IN, Pin.PULL_UP)

kirmizi_led.value(0)
sari_led.value(0)
yesil_led.value(0)

sayac = 0
while True:
    if(dugme_1.value() != 1):
        time.sleep_ms(100)
        sayac += 1
        while(dugme_1.value() != 1):
            continue
        time.sleep_ms(100)
        
    if(dugme_2.value() != 1):
        #Bunda filtrelemeye gerek yoktur.
        break

print("Dugmeye {0} kere basildi.".format(sayac))
    