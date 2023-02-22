from machine import *
import time
class max7219(object):
    def __init__(self, mosi, miso, sck, cs, baudrate = 1000000):
        #SPI ayak tanımları ve SPI tanımı
        self.mosi = Pin(mosi)
        self.cs = Pin(cs, Pin.OUT)
        self.miso = Pin(miso)
        self.sck = Pin(sck)
        self.spi = SPI(1, baudrate=baudrate, polarity=0, phase=0, sck=self.sck, mosi=self.mosi, miso=self.miso)
        self.cs.value(1) # CS başlangıçta HIGH
        # MAX7219 başlangıç ayarları
        self.__yaz(0x09, 0xFF) # Decode modu tüm karakterler için açık
        self.parlaklik(0x07) # Parlaklik değeri
        self.__yaz(0x0B, 0x07) # Scan limit değeri
        self.__yaz(0x0C, 0x01) # Normal çalışma modu

    def __yaz(self, reg, data): # özel metot olarak belirle.
        self.cs.value(0) # CS LOW
        self.spi.write(bytes([reg, data])) # SPI ile veri gönder (reg ve data)
        self.cs.value(1) # CS HIGH
    
    def parlaklik(self, data):
        self.__yaz(0x0A, data)
    #parlaklık yazmacı 0x0A degeri 0-15 arası 

    def test(self, data):
        self.__yaz(0x0F, data)
    # 1 = test modu 0 = normal mod
    
    def digit(self, digit, data):
        self.__yaz(digit, data)
    # bağımsız olarak digit yazdırmak için

    def temizle(self):
        for i in range(1, 9):
            self.digit(i, 0x00)
    
    def int_yaz(self, n):
        if n > 99999999:
            n = 99999999
        elif n < -9999999:
            n = -9999999
        if n < 0:
            n = -n
            negatif = True
        else:
            negatif = False
        for i in range(8):
            self.digit(i+1, n % 10)
            n //= 10
        if negatif:
            self.digit(8, 0x0A)

    