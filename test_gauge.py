""""
Gauge test -- Expects class elements in lib subfolder
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
    tft.text(
    fontl,
    "Test Gauges",
    10,
    112,
    st7789.BLACK,
    st7789.WHITE)

    utime.sleep_ms(1000)

    g1 = gauge_class.gauge(tft,4,0,100,'orange',units='Flux')
    #g2 = gauge_circle.gauge(tft,110,0,100,'b',units='mJ',bg=st7789.WHITE,fg=st7789.BLUE)

    m1 = meter.Meter(tft,110,4,100,30,legend='kWhr')
    m2 = meter.Meter(tft,110,36,100,30,legend='Jobs', bezel='../jpg/MeterBezelAlt2.jpg')
    m3 = meter.Meter(tft,110,70,100,30,legend='Doings')
    l1 = ScreenLED.LED(tft,200,90,30, legend='Test')

    g1.update(randint(20,100))
    utime.sleep_ms(100)
    #g2.update(randint(30,100))
    m1.update(random()*1500)
    m2.update(randint(30,100))
    m3.update(randint(30,100))
    utime.sleep_ms(100)
    l1.update(randint(0,1))

    while True:

        v1 = randint(0,100)
        v2 = random()*1100
        v3 = randint(0,100)
        v4 = randint(0,100)
        s1 = randint(0,1)

        for i in range(20):
            g1.update(move_to(v1,g1.value))
            #g2.update(move_to(v2,g2.value))
            m1.update(move_to(v2,m1.value))
            m2.update(move_to(v3,m2.value))
            m3.update(move_to(v4,m3.value))
            l1.update(s1)

            utime.sleep_ms(100)

main()
