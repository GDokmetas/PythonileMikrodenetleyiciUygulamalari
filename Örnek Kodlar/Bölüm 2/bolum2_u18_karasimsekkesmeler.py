from machine import *
import time
led_no = [23, 22, 21, 19, 18, 5, 17, 16]
led = [] # boş liste oluştur
for i in led_no:
    led.append(Pin(i, Pin.OUT))

bekleme = 200  # varsayilan bekleme süresi
kademe = 20 # artırıp azaltma miktari

def isr_dugme1(dugme1):
    global bekleme
    global kademe # fonksiyonlarda global degiskenleri kullanmak icin
    bekleme += kademe
    print(bekleme)
    while(dugme_1.value() == 0):
        continue
    time.sleep_ms(100) # buton arki onleme
    
def isr_dugme2(dugme2):
    global bekleme
    global kademe
    bekleme -= kademe
    if bekleme < 0 :
        bekleme = 0
    print(bekleme)
    while(dugme_2.value() == 0):
        continue
    time.sleep_ms(100)

#GPIO 32 ve 33 düğmeler, pull-up
dugme_1 = Pin(32, Pin.IN, Pin.PULL_UP)
dugme_2 = Pin(33, Pin.IN, Pin.PULL_UP)
# giris olarak belirle


dugme_1.irq(handler = isr_dugme1, trigger = Pin.IRQ_FALLING)
dugme_2.irq(handler = isr_dugme2, trigger = Pin.IRQ_FALLING)
#dugmelerin kesmelerini etkinlestir handler = kesme fonksiyonu trigger = tetikleyici


while True:
    for x in range(1, 8):
        led[x].on()
        led[x-1].off()
        time.sleep_ms(bekleme)
        
    for x in range(7, 0, -1):
        led[x].off()
        led[x-1].on()
        time.sleep_ms(bekleme)
