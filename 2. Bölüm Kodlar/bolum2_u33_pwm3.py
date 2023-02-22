from machine import *
import time

def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


hoparlor = PWM(Pin(14), 60)
pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)
while True:
   adc_deger = pot.read()
   frekans_deger = ((adc_deger + 1) * 4) # ADC değerini duyma aralığına dönüştür
   print(frekans_deger) 
   hoparlor.freq(frekans_deger)
   time.sleep_ms(10)