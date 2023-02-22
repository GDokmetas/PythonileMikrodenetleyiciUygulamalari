from machine import *
import time

pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)
while True:
    print("Okuma : ", pot.read())
    print("16-bit aralikta :", pot.read_u16())
    print("Gerilim okuma (uV):", pot.read_uv())
    time.sleep_ms(500)
