from machine import *
import time
uart1 = UART(1, baudrate = 9600, tx = 33, rx = 32)

while True:
    uart1.write("Merhaba")
    time.sleep_ms(100)
