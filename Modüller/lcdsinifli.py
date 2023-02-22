from machine import *
import time

class LCD(object):

    def __init__(self, rs_pin, en_pin, d4, d5, d6, d7): # yapıcı metod (constructor)
        self.data_pinleri = list() # nesneye ait data pinleri listesi oluştur
        data_pinleri_num = list()
        data_pinleri_num.append(d4)
        data_pinleri_num.append(d5)
        data_pinleri_num.append(d6)
        data_pinleri_num.append(d7) # data pinleri listesine ekle

        self.rs = Pin(rs_pin, Pin.OUT) # nesneye ait rs pinini oluştur
        self.en = Pin(en_pin, Pin.OUT) # nesneye ait en pinini oluştur
        for i in data_pinleri_num:
            self.data_pinleri.append(Pin(i, Pin.OUT))  
        
        for x in self.data_pinleri:
            x.value(0)

        self.rs.off()
        self.en.off()
        #nesneye ait fonksiyonlarda self kullanılmalı
        self.yaz(0x28, 0)  # 4 bit mod, 2 satır , 5x7 font
        self.yaz(0x0C, 0)  # imleç yok, yanıp sönme yok
        self.yaz(0x06, 0)  # otomatik artırma, ekran kayması yok
        self.yaz(0x80, 0)   # DDRAM 0 ofsetle 0x80'de
        self.yaz(0x01, 0) # ekranı temizle,

    def paralel_yaz_msb(self, deger, pin_list):
        for index in range((len(pin_list) - 1), -1, -1):
            pin_value = (deger >> index) & 0x01
            pin_list[index].value(pin_value)

    def yaz(self, data, komut):
        
        if komut == 1:
            self.rs.on()
        else:
            self.rs.off()
        
        high_nibble = (data >> 4) & 0x0F
        low_nibble = data & 0x0F
        
        self.paralel_yaz_msb(high_nibble, self.data_pinleri)
        time.sleep_ms(1)
        self.en.on()
        time.sleep_ms(1)
        self.en.off()
        time.sleep_ms(1)
        
        self.paralel_yaz_msb(low_nibble, self.data_pinleri)
        time.sleep_ms(1)
        self.en.on()
        time.sleep_ms(1)
        self.en.off()
        time.sleep_ms(1)
 
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
        self.yaz(0x02, 0) # imleci basa al
        if y == 0:
            self.yaz(0x02, 0)
        if y == 1:
            self.yaz(0xC0, 0)
        for i in range(0, x):
            self.yaz(0x10 | 0x04, 0)

    def home(self):
        self.yaz(0x02, 0)

    def satir2(self):
        self.yaz(0xC0, 0)

    def clear(self):
        self.yaz(0x01, 0)
        

