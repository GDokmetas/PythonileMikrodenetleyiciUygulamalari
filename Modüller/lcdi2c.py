from machine import *
import time

MASK_RS = 0x01       
MASK_E  = 0x04       
SHIFT_ISIK = 3  
SHIFT_VERI = 4
# bit işlemlerinde kullanılan sabitler
class LCD(object):
    LCD_SATIR = (0x00, 0x40) # LCD satır offsetleri
    def __init__(self, addr, sda, scl): # yapıcı metod (constructor)
        self.address = addr
        self.i2c = I2C(1, scl=Pin(scl), sda=Pin(sda), freq=400000)
        self.backlight = 1

        time.sleep_ms(100)  # LCD'nin güçlenmesi için bekle
        
        #nesneye ait fonksiyonlarda self kullanılmalı
        self.init_yaz(0x30)  # 
        time.sleep_ms(10)
        self.init_yaz(0x30)  # 
        time.sleep_ms(10)
        self.init_yaz(0x30)  # 
        time.sleep_ms(10)
        self.init_yaz(0x20 | 0x08 | 0x02) # 4 bit mod, 2 satır, 5x8 font
        time.sleep_ms(5)
        self.yaz(0x01, 0) # ekranı temizle,
        self.home()

    def init_yaz(self, data):
        veri = (data >> 4) & 0x0F << SHIFT_VERI
        self.i2c.writeto(self.address, bytes([veri | MASK_E]))
        self.i2c.writeto(self.address, bytes([veri]))

    def yaz(self, data, komut):
        high_data = (data >> 4) & 0x0F # son dört bitlik veriyi 4 bit olarak ayır
        low_data = data & 0x0F # son dört bitlik veriyi 4 bit olarak ayır
        i2c_data = 0
        # 0 nolu bit RS, 1 nolu bit RW, 2 nolu bit E, 3 nolu bit backlight
        # baştaki dört bit data ayakları (d4-d7)
        if komut == 0: # komut ise
            i2c_data = (self.backlight << SHIFT_ISIK) | (high_data << SHIFT_VERI)

            self.i2c.writeto(self.address, bytes([i2c_data | MASK_E])) 
            #Enable bitini 1 yap ve veriyi yaz
            self.i2c.writeto(self.address, bytes([i2c_data & ~MASK_E])) 
            #Enable bitini 0 yapmak için bir daha gönder
            i2c_data = (self.backlight << SHIFT_ISIK) | (low_data << SHIFT_VERI) 
            # veriyi 4 bit kaydır 
            self.i2c.writeto(self.address, bytes([i2c_data | MASK_E])) 
            #Enable bitini 1 yap ve veriyi yaz
            self.i2c.writeto(self.address, bytes([i2c_data & ~MASK_E])) 
            #Enable bitini 0 yapmak için bir daha gönder
        else: # veri ise
            i2c_data = (self.backlight << SHIFT_ISIK) | (high_data << SHIFT_VERI) | MASK_RS 
            # RS bitini de 1 yap
            self.i2c.writeto(self.address, bytes([i2c_data | MASK_E])) 
            #Enable bitini 1 yap ve veriyi yaz
            self.i2c.writeto(self.address, bytes([i2c_data & ~MASK_E])) 
            #Enable bitini 0 yapmak için bir daha gönder
            i2c_data = (self.backlight << SHIFT_ISIK) | (low_data << SHIFT_VERI) | MASK_RS 
            # veriyi 4 bit kaydır
            self.i2c.writeto(self.address, bytes([i2c_data | MASK_E])) 
            #Enable bitini 1 yap ve veriyi yaz
            self.i2c.writeto(self.address, bytes([i2c_data & ~MASK_E])) 
            #Enable bitini 0 yapmak için bir daha gönder
        time.sleep_ms(4) #komutlar arası 1 ms bekle

    def puts(self, yazi):
        for x in yazi:
            self.yaz(ord(x), 1)

    def disp_control(self, display = True, cursor = False, blink = False):
        disp_control = 0x08
        if display == True:
            disp_control = disp_control | 0x04
        if cursor == True:
            disp_control = disp_control | 0x02
        if blink == True:
            disp_control |= disp_control | 0x01
        self.yaz(disp_control, 0)

    def xy(self, x, y):
        if y > len(self.LCD_SATIR):
            y = len(self.LCD_SATIR) - 1
        self.yaz(0x80 | self.LCD_SATIR[y] | x, 0)   # bellek adresi + satır offseti + sütun

    def home(self):
        self.yaz(0x02, 0)

    def satir2(self):
        self.yaz(0xC0, 0)

    def clear(self):
        self.yaz(0x01, 0)
        
    def backlight(self, on = True):
        if on == True: # arka ışığı aç
            self.backlight = 1
        else: # arka ışığı kapat
            self.backlight = 0



