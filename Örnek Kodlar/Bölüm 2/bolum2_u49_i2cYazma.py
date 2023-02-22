from machine import *
i2c = I2C(1, scl=Pin(13), sda=Pin(12), freq=400000)


while True:
    i2c.writeto(0x68, b'1')