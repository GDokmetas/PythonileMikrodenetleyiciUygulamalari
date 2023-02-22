from machine import *
import time
i2c = I2C(1, scl=Pin(13), sda=Pin(12), freq=400000)

data = bytearray(1) # Tek baytlık tampon oluştur.

print(i2c.scan())  #i2c aygıtları listele (adresleri desimal gösterilir)
time.sleep(5)
    
while True:
    # 0x68 adresli aygıtın 0x00 adresinden 1 bayt oku
    i2c.writeto(0x68, b'\x00')
    data = i2c.readfrom(0x68, 1)
    #bytes verisini int'e çevir
    i = int.from_bytes(data, "big")
    #int verisini ikilik formatta yazdır
    print("{:08b}".format(i))
    time.sleep_ms(100)
    