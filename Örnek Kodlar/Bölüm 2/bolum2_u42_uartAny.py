from machine import *
import time
uart1 = UART(1, baudrate = 9600, tx = 33, rx = 32, timeout = 100)

buf = b''
while True:
    # Tampon bellekte hiç veri kalmayana kadar okumayı gerçekleştir. 
    while uart1.any():
        buf += uart1.read(1)
        # okunan baytları birer birer ekle
    print(buf.decode('utf-8'))   
    time.sleep_ms(2000)