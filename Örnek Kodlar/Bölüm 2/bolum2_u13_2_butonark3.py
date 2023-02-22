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

dugme_sayac = 0
while True:
    if(dugme_1.value() != 1):
        pin_deger = dugme_1.value()
        sayac = 0
        while sayac < 20:
            if(dugme_1.value() != pin_deger):
                sayac += 1
            else:
               sayac = 0
            time.sleep_ms(1)
        dugme_sayac += 1
        #Düğme basılınca işletilecek kodlar/fonksiyon buraya yazılacak
            
        while(dugme_1.value() != 1):
            continue
        
    if(dugme_2.value() != 1):
        #Bunda filtrelemeye gerek yoktur.
        break

print("Dugmeye {0} kere basildi.".format(dugme_sayac))
    