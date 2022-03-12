""""
Gauge test -- just to see ...
"""

import utime
import math
from random import randint
import st7789
import tft_config
import vga1_bold_16x16 as fontl
import gauge_class
import gauge_circle
import ScreenLED

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
    g2 = gauge_circle.gauge(tft,110,0,100,'b',units='mJ',bg=st7789.WHITE,fg=st7789.BLUE)
    l1 = ScreenLED.LED(tft,200,90,30, legend='Test')

    g1.update(randint(20,100))
    utime.sleep_ms(100)
    g2.update(randint(30,100))
    utime.sleep_ms(100)
    l1.update(randint(0,1))

    while True:

        v1 = randint(0,100)
        v2 = randint(0,100)
        s1 = randint(0,1)

        for i in range(20):
            g1.update(move_to(v1,g1.value))
            g2.update(move_to(v2,g2.value))
            l1.update(s1)

            utime.sleep_ms(100)

main()
