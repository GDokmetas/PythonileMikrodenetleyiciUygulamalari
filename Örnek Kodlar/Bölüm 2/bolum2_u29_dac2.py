from machine import *
import time

dac1 = DAC(Pin(25))

dac_deger = 1
while True:
    for x in range(0, 255):
        dac1.write(x)
    
    for x in range(255, 0, -1):
        dac1.write(x)

