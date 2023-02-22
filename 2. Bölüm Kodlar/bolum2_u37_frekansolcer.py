from machine import *
import time

led = PWM(Pin(14), 60000)
freq_in = Pin(18, Pin.IN)


while True:
    
    time_pulse_us(freq_in, 1, 100000)
    pozitif = time_pulse_us(freq_in, 1, 100000)
    time_pulse_us(freq_in, 0, 100000)
    negatif = time_pulse_us(freq_in, 0, 100000)
    period = pozitif + negatif
    frekans = 1000000 / period
    print("Frekans: ", frekans)
    time.sleep_ms(100)
    