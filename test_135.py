""""
Test the 135 gauge
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
    Draw 135 gauge and an LED and update them
    '''
    # enable display
    tft.init()
    tft.inversion_mode(True)
    tft.fill(st7789.WHITE)

    g1 = gauge_class.gauge(tft,0,0,135,units='Flux')
    l1 = ScreenLED.LED(tft,200,90,30, legend='Test')

    g1.update(randint(20,100))
    l1.update(randint(0,1))

    while True:

        v1 = randint(0,100)
        s1 = randint(0,1)

        for i in range(20):
            g1.update(move_to(v1,g1.value))
            l1.update(s1)
            utime.sleep_ms(100)

main()
