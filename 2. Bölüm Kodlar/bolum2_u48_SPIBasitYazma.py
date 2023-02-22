from machine import *
import time
spi = SPI(1, 1000000, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
cs = Pin(27, Pin.OUT, value = 1)
while True:
    cs(0)
    spi.write(b'12345')
    cs(1)
    time.sleep_ms(10)