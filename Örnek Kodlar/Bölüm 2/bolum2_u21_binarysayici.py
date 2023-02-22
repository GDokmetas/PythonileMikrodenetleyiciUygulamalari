from machine import *
import time
led_no = [23, 22, 21, 19, 18, 5, 17, 16]
led = [] # boş liste oluştur
for i in led_no:
    led.append(Pin(i, Pin.OUT))

deger = 0 # sayaç değeri
while True:
    binary_string = "{:08b}".format(deger)
    #sayaç değerini binary biçimde (10101010 gibi) formatla
    print(binary_string)
    
    index = 0 # led listesi için indis
    for bin_char in binary_string: # binary_stringdeki her karakteri sirasiyla al
        led[index].value(int(bin_char))
        #bin_char'ı integer'e dönüştür ve led'in değerini belirle
        index += 1 # bir sonraki karakter için bir sonraki lede geç
        
    deger += 1 # gösterim bittikten sonra sayacı bir artır
    if deger > 255: # taşmayı engelle
        deger = 0
    time.sleep_ms(500)
