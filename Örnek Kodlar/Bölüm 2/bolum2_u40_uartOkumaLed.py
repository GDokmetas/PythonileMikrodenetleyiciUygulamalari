from machine import *
import time
uart1 = UART(1, baudrate = 9600, tx = 33, rx = 32, timeout = 100)
#timeout her read fonksiyonunda bekleme süresi (ms)
#timeout verilmezse veri kaçırılabilir.

led_1 = Pin(18, Pin.OUT)
led_2 = Pin(19, Pin.OUT)

led_1.value(0)
led_2.value(0)

while True:
    uart_okuma = uart1.read(1) # 1 baytlık veri oku
    print(uart_okuma)
    #A komutunda yapılacaklar
    if uart_okuma == b'A':
        led_1.value(1)
        uart1.write("Led1 ON \n")
    #a komutunda yapılacaklar
    elif uart_okuma == b'a':
        led_1.value(0)
        uart1.write("Led1 OFF \n")
    #B komutunda yapılacaklar   
    elif uart_okuma == b'B':
        led_2.value(1)
        uart1.write("Led2 ON \n")
    #b komutunda yapılacaklar   
    elif uart_okuma == b'b':
        led_2.value(0)
        uart1.write("Led2 OFF \n")
