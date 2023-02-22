import math
from machine import *


buf = bytearray(100) #100 elemanlık bayt dizisi oluştur
for i in range(len(buf)):
    buf[i] = 128 + int(127 * math.sin(2 * math.pi * i / len(buf)))
#sinüs değerini hesapla ve diziye yazdır

dac = DAC(Pin(25))

while True:
    for i in range(len(buf)):
        dac.write(buf[i])
        #dizideki elemanları sırasıyla yaz