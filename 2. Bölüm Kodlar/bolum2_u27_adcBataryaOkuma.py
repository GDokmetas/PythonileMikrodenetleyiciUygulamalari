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
    gerilim_mV = pot_value * (3300.0 / 4095.0)
    #Ölçülen ham ADC değerini milivolta çevir
    #3300 referans gerilimi (3.3v) 4095 azami değer
    bat_gerilim = map(gerilim_mV, 0, 3300, 0, 14000)
    # Gerilim bölücü direnç 0-14000mV arası değeri 0-3300mv arasına düşürüyor.
    
    
    
    bar_deger = 0
    bar_deger = int(map(int(bat_gerilim), 9000, 12000, 0, 8))
    # Batarya 9V altındaysa boş, 12V ve üstündeyse tam dolu
    #hesaplanan değerleri yazdır
    print("Gerilim: ", gerilim_mV)
    print("Bat Gerilim:", bat_gerilim)
    print("Bar Deger:", bar_deger)

    #karaşimşek devresinde bar olarak göster
    for x in led: 
        if bar_deger > 0:  # bar değeri kadar ledleri yak
            x.value(1)
            bar_deger -= 1
        else:
            x.value(0) # geri kalan ledleri sıfırla
    time.sleep_ms(100)