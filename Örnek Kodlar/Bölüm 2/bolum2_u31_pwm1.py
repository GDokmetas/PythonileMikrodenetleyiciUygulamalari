from machine import *
import time

led = PWM(Pin(14), 1000)
print("Duty : ", led.duty())