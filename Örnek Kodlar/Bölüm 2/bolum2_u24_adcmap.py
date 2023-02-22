from machine import *
import time
def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)
while True:
    pot_value = pot.read()
    print("Okuma : ", pot_value)
    print("Map:", int(map(pot_value, 0, 4095, 0, 10)))
    # 0-4095 arası değeri 0-10 arası değere dönüştür
    time.sleep_ms(500)