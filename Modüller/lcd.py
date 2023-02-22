from machine import *
import time

data_pinleri = list() # boş liste oluştur
rs = 0
en = 0
def paralel_yaz_msb(deger, pin_list):
    for index in range((len(pin_list) - 1), -1, -1):
        pin_value = (deger >> index) & 0x01
        pin_list[index].value(pin_value)

def yaz(data, komut):
    global rs, en, data_pinleri
    
    if komut == 1:
        rs.on()
    else:
        rs.off()
    
    high_nibble = (data >> 4) & 0x0F
    low_nibble = data & 0x0F
    
    paralel_yaz_msb(high_nibble, data_pinleri)
    time.sleep_ms(1)
    en.on()
    time.sleep_ms(1)
    en.off()
    time.sleep_ms(1)
    
    paralel_yaz_msb(low_nibble, data_pinleri)
    time.sleep_ms(1)
    en.on()
    time.sleep_ms(1)
    en.off()
    time.sleep_ms(1)

def init(rs_pin, en_pin, d4, d5, d6, d7):
    global data_pinleri
    global en
    global rs
    data_pinleri_num = list()
    data_pinleri_num.append(d4)
    data_pinleri_num.append(d5)
    data_pinleri_num.append(d6)
    data_pinleri_num.append(d7)

    rs = Pin(rs_pin, Pin.OUT)
    en = Pin(en_pin, Pin.OUT)
    for i in data_pinleri_num:
        data_pinleri.append(Pin(i, Pin.OUT))
    
    for x in data_pinleri:
        x.value(0)

    rs.off()
    en.off()

    yaz(0x28, 0)  # 4 bit mod, 2 satır , 5x7 font
    yaz(0x0C, 0)  # imleç yok, yanıp sönme yok
    yaz(0x06, 0)  # otomatik artırma, ekran kayması yok
    yaz(0x80, 0)   # DDRAM 0 ofsetle 0x80'de
    yaz(0x01, 0) # ekranı temizle
    
def puts(yazi):
    for x in yazi:
        yaz(ord(x), 1)

def disp_control(display = True, cursor = False, blink = False):
    disp_control = 0x08
    if display == True:
        disp_control = disp_control | 0x04
    if cursor == True:
        disp_control = disp_control | 0x02
    if blink == True:
        disp_control |= disp_control | 0x01
    yaz(disp_control, 0)

def xy(x, y):
    yaz(0x02, 0) # imleci basa al
    if y == 0:
        yaz(0x02, 0)
    if y == 1:
        yaz(0xC0, 0)
    for i in range(0, x):
        yaz(0x10 | 0x04, 0)

def home():
    yaz(0x02, 0)

def satir2():
    yaz(0xC0, 0)

def clear():
    yaz(0x01, 0)
    

