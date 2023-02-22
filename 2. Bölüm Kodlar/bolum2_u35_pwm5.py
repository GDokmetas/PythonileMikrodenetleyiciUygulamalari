from machine import *
import time
import math
led = PWM(Pin(14), 50000)
buf = bytearray(100) #100 elemanlık bayt dizisi oluştur
for i in range(len(buf)):
    buf[i] = 128 + int(127 * math.sin(2 * math.pi * i / len(buf)))


while True:
    for i in range(len(buf)):
        led.duty(buf[i]*4) # 10 bit olması için 0-255'i 4 e çarp 
