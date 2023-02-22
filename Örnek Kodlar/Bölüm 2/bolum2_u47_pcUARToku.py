import serial

ser = serial.Serial('COM3', 9600, timeout=1)
#com3 9600 baud oranında seri port nesnesi oluşturuldu

def checksum(data): #checksum hesaplama fonksiyonu
    cs = 0
    for c in data:
        cs = cs ^ c
    return cs

def seri_oku():
    buf = b''
    buf += ser.read(16) # 16 byte oku
    start_index = buf.find(b'\x02') #başlangıç karakteri bul

    veri = ""
    if start_index != -1: #başlangıç karakteri varsa
        buf = buf[start_index:] #başlangıç karakterinden itibaren oku
        end_index = buf.find(b'\x03') #bitiş karakteri bul
        if end_index != -1: #bitiş karakteri varsa
            veri = buf[1:end_index] #başlangıç ve bitiş karakterlerini çıkar
    return veri

while True:
    veri = b''
    if(ser.inWaiting()>0):
        veri = seri_oku()
        charlist = []
        for char in veri: #veriyi karakter karakter oku
            charlist.append(char) #listeye ekle
    
        print(charlist)
        sum = int(chr(charlist[-2]) + chr(charlist[-1]), 16)
        print("Sum:", sum)
        charlist.pop() #son elemanı çıkar (cheksum ilk nibble)
        charlist.pop() #son elemanı çıkar (checksum son nibble)
        cs = checksum(charlist)
        print("checksum: ", cs)
        if cs == sum:
            print("checksum doğru")
        else:
            raise Exception("checksum hatalı")

        veri = veri.decode('utf-8')
        veri = veri.split(',')
        veri.pop() #son elemanı çıkar (checksum)
        print(veri)
