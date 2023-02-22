from machine import *
import time
import math
led = PWM(Pin(14), 1000)

r = (100 * math.log10(2)) / (math.log10(1023))
while True:
    led.duty(0)
    for i in range(0, 100):
        duty = math.pow(2, (i / r)) - 1
        led.duty(int(duty))
        time.sleep_ms(10)
    for i in range(100, -1, -1):
        duty = math.pow(2, (i / r)) - 1
        led.duty(int(duty))
        time.sleep_ms(10)
