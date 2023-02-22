from machine import *
import time

led = PWM(Pin(14), 5)

while True:
    for i in range(0, 1023):
        led.duty(i)
        time.sleep_ms(10)
       
    for i in range(1023, 0, -1):
        led.duty(i)
        time.sleep_ms(10)