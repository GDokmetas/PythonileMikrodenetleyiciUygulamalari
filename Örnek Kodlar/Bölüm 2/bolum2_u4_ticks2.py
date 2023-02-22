import time
baslangic = time.ticks_ms()

while True:
    for i in range(200000):
        time.time()
    if time.ticks_diff(time.ticks_ms(), baslangic) > 1000:
        artan_kisim = time.ticks_diff(time.ticks_ms(), baslangic) - 1000
        print("1 saniye geçti")
        baslangic = time.ticks_ms() + artan_kisim