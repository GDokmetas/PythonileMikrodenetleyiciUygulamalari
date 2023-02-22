from machine import *
from micropython import const
import time

pin2 = Pin(2, Pin.OUT)

GPIO_OUT_REG = const(0x3FF44004)

while True:
    mem32[GPIO_OUT_REG] |= (1<<2)
    time.sleep_ms(200)
    mem32[GPIO_OUT_REG] &= ~(1<<2)
    time.sleep_ms(200)
