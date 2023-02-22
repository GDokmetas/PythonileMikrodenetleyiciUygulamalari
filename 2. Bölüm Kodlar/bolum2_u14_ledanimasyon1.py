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
gecikme_ms = 200
animasyon_no = 0
max_animasyon = 4
simdiki_ms = 0 # sonradan ticks'den dönen değer yüklenecek
onceki_ms = time.ticks_ms() # değerin sıfır olmamasına dikkat edin hata verebilir.
#ticks_us okumak gecikmeye sebep oluyor, ms okumak daha hızlı!
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
        #Düğme basılınca işletilecek kodlar/fonksiyon buraya yazılacak
        gecikme_ms += 25 
        print("Gecikme : ", gecikme_ms)
        while(dugme_1.value() != 1):
            continue
        
    if(dugme_2.value() != 1):
        pin_deger = dugme_2.value()
        sayac = 0
        while sayac < 20:
            if(dugme_2.value() != pin_deger):
                sayac += 1
            else:
               sayac = 0
            time.sleep_ms(1)
        #Düğme basılınca işletilecek kodlar/fonksiyon buraya yazılacak
        gecikme_ms -= 25
        if gecikme_ms < 0:
            gecikme_ms = 0
        print("Gecikme : ", gecikme_ms)
        while(dugme_2.value() != 1):
            continue
        
    simdiki_ms = time.ticks_ms()
    if(time.ticks_diff(simdiki_ms, onceki_ms) > (gecikme_ms)):
        onceki_ms = simdiki_ms
        
        animasyon_no += 1
        
        if animasyon_no > max_animasyon:
            animasyon_no = 1
        print(animasyon_no)    
        if(animasyon_no == 1):
            kirmizi_led.on()
            sari_led.off()
            yesil_led.off()
        elif(animasyon_no == 2):
            kirmizi_led.off()
            sari_led.on()
            yesil_led.off()
        elif(animasyon_no == 3):
            kirmizi_led.off()
            sari_led.off()
            yesil_led.on()
        elif(animasyon_no == 4):
            kirmizi_led.off()
            sari_led.on()
            yesil_led.off()
        else:
            kirmizi_led.off()
            sari_led.off()
            yesil_led.off()

    