import machine
import time
led = machine.Pin(2, machine.Pin.OUT)
print("Led yakma programi basladi!!! \n")
print("Ben ESP32'yim!!")
while True:
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)
