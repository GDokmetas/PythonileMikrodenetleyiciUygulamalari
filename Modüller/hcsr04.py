from machine import *
import time
class hcsr04:
    def __init__(self, trg, ech, timeout = 11600):
        self.timeout = timeout
        self.trig = Pin(trg, mode = Pin.OUT)
        self.echo = Pin(ech, mode=Pin.IN, pull=None)
        self.trig.value(0)

    def mesafe(self):
        self.trig.value(0)
        time.sleep_us(5)
        self.trig.value(1)
        time.sleep_us(10)
        self.trig.value(0)
        #10 mikrosaniyelik sinyal gönderildi.

        try:
            pals_suresi = time_pulse_us(self.echo, 1, self.timeout)
        except:
            print("zaman asimi!")
            return 0
        # 1 milimetrede 2.91 mikrosaniye gider.
        # sesin gidip gelmesi mesafeyi iki katına çıkarır
        # bu yüzden pals_suresi / 2 / 2.91 olarak hesaplanmalı
        mesafe_cm = (pals_suresi / 2) / 29.1
        return mesafe_cm
