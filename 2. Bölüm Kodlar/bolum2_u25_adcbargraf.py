from machine import *
import time
led_no = [23, 22, 21, 19, 18, 5, 17, 16]
led = [] # boş liste oluştur
for i in led_no:
    led.append(Pin(i, Pin.OUT))

def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)

while True:
    pot_value = pot.read()
    bar_deger = int(map(pot_value, 0, 4095, 0, 8))
    # 0-4095 arası değeri 0-8 arası değere dönüştür
    for x in led: 
        if bar_deger > 0:  # bar değeri kadar ledleri yak
            x.value(1)
            bar_deger -= 1
        else:
            x.value(0) # geri kalan ledleri sıfırla
            