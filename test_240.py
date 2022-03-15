""""
Gauge test for 240x240 screens
    -- Expects class elements in lib subfolder
    -- Expects bitmap.py files in bitmap subfolder
"""

import utime
import math
from random import randint
from random import random
import st7789
import tft_config
import vga1_bold_16x16 as fontl
import lib.gauge_class as gauge_class
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
    Draw gauge and update
    '''
    # enable display
    tft.init()
    tft.inversion_mode(True)
    tft.fill(st7789.WHITE)
    tft.text(fontl,"Test Gauges",10,112,st7789.BLACK,st7789.WHITE)

    g1 = gauge_class.gauge(tft,0,0,240,bezel='bitmap.g240plainRedline',units='Flux')

    """
    m1 = meter.Meter(tft,230,4,80,30,legend='kWhr', bezel='bitmap.MeterBezelSimple')
    m2 = meter.Meter(tft,230,40,80,30,legend='Jobs', bezel='bitmap.MeterBezelSimple')
    m3 = meter.Meter(tft,230,200,80,30,legend='Doings', bezel='bitmap.MeterBezelSimple',lc=st7789.GREEN, fg=st7789.BLUE)
    l1 = ScreenLED.LED(tft,260,80,30, legend='Test', lc=st7789.GREEN)
    l2 = ScreenLED.LED(tft,260,110,30, legend='Alarm')
    l3 = ScreenLED.LED(tft,260,140,30, legend='Russes', lc=st7789.BLUE)
    """

    g1.update(randint(20,100))

    while True:

        v1 = randint(0,100)

        for i in range(20):
            g1.update(move_to(v1,g1.value))
            utime.sleep_ms(50)

main()
