import time
baslangic = time.ticks_ms()

while True:
    if time.ticks_diff(time.ticks_ms(), baslangic) > 1000:
        print("1 saniye geçti")
        baslangic = time.ticks_ms()
        