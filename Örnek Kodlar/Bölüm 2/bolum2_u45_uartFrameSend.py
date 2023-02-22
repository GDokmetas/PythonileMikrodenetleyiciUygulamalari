from machine import *
import time
uart1 = UART(1, baudrate = 9600, tx = 33, rx = 32, timeout = 100)

deger1 = 300
deger2 = 400
deger3 = 500

while True:
    
    buf = ""
    buf += '\x02' # start of text
    buf += "{:d},{:d},{:d}".format(deger1, deger2, deger3)
    buf += '\x03' #end of text
    uart1.write(buf)
    time.sleep_ms(2000)