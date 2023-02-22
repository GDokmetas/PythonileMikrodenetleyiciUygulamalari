from machine import *
import time

dac1 = DAC(Pin(25))
dac2 = DAC(Pin(26))

def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

dac1_gerilim_mV = 1000
dac2_gerilim_mV = 1500

dac1_deger = int(map(dac1_gerilim_mV, 0, 3300, 0, 255))
dac2_deger = int(map(dac2_gerilim_mV, 0, 3300, 0, 255))

dac1.write(dac1_deger)
dac2.write(dac2_deger)

while True:
    continue
