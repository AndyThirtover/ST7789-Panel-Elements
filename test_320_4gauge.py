""""
Gauge test for 320x240 screens
    -- Expects class elements in lib subfolder
    -- Expects bitmap.py files in bitmap subfolder

This uses 4 x 120 gauges

"""

import utime
import math
from random import randint
from random import random
import st7789
import tft_config
import vga1_bold_16x16 as fontl
import lib.gauge_class as gauge_class
import lib.gauge_circle as gauge_circle
import lib.ScreenLED as ScreenLED
import lib.meter as meter
import gc

tft = tft_config.config(1)


def move_to (curr, prev):
    if curr > prev:
        return prev + 1
    if curr < prev:
        return prev - 1
    return curr

def main():
    '''
    Draw 4 gauges and update them
    '''
    # enable display
    tft.init()
    tft.inversion_mode(True)
    tft.fill(st7789.WHITE)
    tft.text(fontl,"Test Gauges",10,112,st7789.BLACK,st7789.WHITE)

    g1 = gauge_class.gauge(tft,0,0,120,bezel='bitmap.g120plain',units='Flux')
    g2 = gauge_class.gauge(tft,120,0,120,bezel='bitmap.g120plain',units='Amps')
    g3 = gauge_class.gauge(tft,0,120,120,bezel='bitmap.g120plain',units='Volts')
    g4 = gauge_class.gauge(tft,120,120,120,bezel='bitmap.g120plain',units='MGs')

    m1 = meter.Meter(tft,230,4,80,30,legend='F Mem', bezel='bitmap.MeterBezelSimple', max=8000)
    m2 = meter.Meter(tft,230,40,80,30,legend='Jobs', bezel='bitmap.MeterBezelSimple')
    m3 = meter.Meter(tft,230,200,80,30,legend='Doings', bezel='bitmap.MeterBezelSimple',lc=st7789.GREEN, fg=st7789.BLUE)
    l1 = ScreenLED.LED(tft,260,80,30, legend='Test', lc=st7789.GREEN)
    l2 = ScreenLED.LED(tft,260,110,30, legend='Alarm')
    l3 = ScreenLED.LED(tft,260,140,30, legend='Russes', lc=st7789.BLUE)

    g1.update(randint(20,100))
    g2.update(randint(30,100))
    g3.update(randint(40,100))
    g4.update(randint(50,100))

    m1.update(random()*1500)
    m2.update(randint(30,100))
    m3.update(randint(30,100))

    l1.update(randint(0,1))
    l2.update(randint(0,1))
    l3.update(randint(0,1))

    while True:


        v1 = randint(0,100)
        v2 = randint(0,100)
        v3 = random()*1100
        v4 = randint(0,100)
        v5 = randint(0,100)
        v6 = randint(0,100)
        v7 = randint(0,100)

        s1 = randint(0,1)
        s2 = randint(0,1)
        s3 = randint(0,1)

        for i in range(20):
            g1.update(move_to(v1,g1.value))
            g2.update(move_to(v2,g2.value))
            g3.update(move_to(v3,g3.value))
            g4.update(move_to(v4,g4.value))

            m1.update(int(gc.mem_free()/1024))
            m2.update(move_to(v3,m2.value))
            m3.update(move_to(v5,m3.value))

            l1.update(s1)
            l2.update(s2)
            l3.update(s3)
            utime.sleep_ms(50)

main()
