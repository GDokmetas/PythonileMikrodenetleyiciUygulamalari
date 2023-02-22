from machine import *
import time
uart1 = UART(1, baudrate = 9600, tx = 33, rx = 32, timeout = 100)

buf = b''
while True:
    buf = b''
    while uart1.any():
        buf += uart1.read(1)
        # okunan baytları birer birer ekle
        #okuma bitince stringe çevir
    buf = buf.decode('utf-8')
     
    #veri başlangıcının indisini bul
    start_index = buf.find('\x02')
    veri = ""
    
    i = start_index + 1
    #Eğer 0x02 bulunuyorsa
    if start_index != -1:
        while(buf[start_index + i] != '\x03'): #0x03 bulunana kadar okumaya devam et
            veri += buf[i]
            i += 1
        #veriyi yazdır
        print("Veri: ", veri)
        print("Verix:", veri.encode('hex'))
    
    time.sleep_ms(2000)