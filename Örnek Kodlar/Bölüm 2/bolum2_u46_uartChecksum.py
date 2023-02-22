
from machine import *
import time
uart1 = UART(1, baudrate = 9600, tx = 33, rx = 32, timeout = 100)

deger1 = 100
deger2 = 200
deger3 = 300

def checksum(data):
    checksum = 0
    for char in data:
        checksum ^= ord(char) # ord fonksiyonuyla baytın tam sayı değerini al
        # XOR işlemine tabi tut
    return checksum

while True:
    buf = ""
    buf += '\x02' # start of text
    data = "{:d},{:d},{:d},".format(deger1, deger2, deger3)
    charlist = []
    #Karakter dizisini tek tek karakterlere ayır, bunları baytlara çevir
    for char in data:
        charlist.append(bytes(char, 'utf-8'))
           
    check_sum = checksum(charlist)
    
    buf += data
    buf += "{:2x}".format(check_sum)
    #checksum verisini 2'li hex şeklinde diziye ekle
    buf += '\x03' #end of text
    print(buf)
    uart1.write(buf)
    time.sleep_ms(200)


    