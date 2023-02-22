from machine import *
import time
led_no = [17, 5, 18, 19, 21, 22, 23]
#23 a, 22b, 21c, 19d, 18e, 5f, 17g)
rakamlar = [0x7E, 0x30, 0x6D, 0x79, 0x33, 0x5B, 0x5F, 0x70, 0x7F, 0x7B]
led = [] # boş liste oluştur
for i in led_no:
    led.append(Pin(i, Pin.OUT))

def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)

while True:
    pot_value = 0
    for i in range(0, 100):
        pot_value += pot.read()
    #toplam 100 ölçüm yap ve bunları topla
    pot_value /= 100
    #ölçümleri 100'e bölüp ortalamasını al
    bar_deger = int(map(pot_value, 0, 4095, 0, 10))
    # 0-4095 arası değeri 0-8 arası değere dönüştür
    rakam = rakamlar[bar_deger]
    for x in range(6, -1, -1): 
        bit = (rakam >> x) & 0x01
        led[x].value(bit)
        