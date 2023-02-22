from machine import *
import time
led_no = [23, 22, 21, 19, 18, 5, 17, 16]
led = [] # boş liste oluştur
for i in led_no:
    led.append(Pin(i, Pin.OUT))

index = -1 # dizinin indisini gösteren değer
yon = 0 # soldan sağa mı, sağdan sola mı?
def karasimsek(t):
    global index
    global yon # değişkenleri global olarak al (kalıcı olması gerek)
    if yon == 0: #soldan saga ise
        index += 1 #indisi bir artır
        led[index].value(1) #indise denk gelen ledi yak
        if index != 0: # Eğer kenarda bulunmuyorsa kendinden onceki ledi sondur
            led[index-1].value(0)
        if index == 7: # sona geldiğinde yönü değiştir
            yon = 1
    if yon == 1: # sağdan sola ise
        led[index].value(1) #indise denk gelen ledi yak
        if index != 7: 
            led[index+1].value(0) # eğer kenarda değilse kendinden oncekini sondur
        if index == 0: # sona geldiğinde yon değiştir
            yon = 0
        if index > 0: # 0 olana kadar birer birer azalt
            index -= 1
    print(index)
tim0 = Timer(0)
tim0.init(period = 100, mode = Timer.PERIODIC, callback = karasimsek)
#100ms periyotta zamanlayıcıyı çalıştır

while True:
    pass

