from machine import *
import time
uart1 = UART(1, baudrate = 9600, tx = 33, rx = 32, timeout = 100)

buf = b''

while True:
    # Tampon bellekte hiç veri kalmayana kadar okumayı gerçekleştir.

    buf = b''
    while uart1.any():
        buf += uart1.read(1)
        # okunan baytları birer birer ekle
        #okuma bitince stringe çevir
    buf = buf.decode('utf-8')
     
    #veri başlangıcının indisini bul
    start_index = buf.find('\x02')
    veri = ""
    
    i = start_index + 1
    #Eğer 0x02 bulunuyorsa
    if start_index != -1:
        while(buf[start_index + i] != '\x03'): #0x03 bulunana kadar okumaya devam et
            veri += buf[i]
            print(veri.encode('hex'))
            i += 1
        #veriyi yazdır
        print("Veri: ", veri.encode('hex'))
        veri_split = veri.split(',') # okunan stringi virgülleri gözeterek ayir
        ayrilmis_veriler = dict() # yeni bir sozluk oluştur
        
        veri_adlari = ['x', 'y', 'z'] # sozlukteki anahtları belirle
        # Verilerin sıralanması burada çok önemli
        
        # veri_splitteki nesne sayısı kadar tekrarla
        for veri_no, deger in enumerate(veri_split):
            ayrilmis_veriler[veri_adlari[veri_no]] = deger
        # istersek sadece veri_no diyerek  anahtarlari 0, 1, 2 diye oluşturabiliriz.
        print(str(ayrilmis_veriler))
    
    time.sleep_ms(2000)