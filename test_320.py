""""
Gauge test for 320x240 screens
    -- Expects class elements in lib subfolder
    -- Expects bitmap.py files in bitmap subfolder
"""

import utime
import math
from random import randint
from random import random
import st7789
import tft_config
import lib.simple_gauge as gauge_class
#import lib.gauge_circle as gauge_circle
#import lib.meter as meter
from lib.panel_helpers import chunked_bitmap
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
    Draw 1 gauges and update it
    '''
    # enable display
    tft.init()
    tft.rotation(0)
    tft.inversion_mode(False)
    tft.fill(st7789.BLACK)

    g1 = gauge_class.gauge(tft,0,0,240,bezel='bitmap.240Bar')
    gc.collect()
    g1.update(randint(20,100))

    autostate = 'bitmap.AutoState'
    bm = __import__(autostate)              # import the bitmap .py file
    ref = autostate.replace('bitmap.','')   # reference to the object in the .py file, replace is a better option
    chunked_bitmap(tft, getattr(bm,ref),0,240)
    del bm
    del ref
    gc.collect()

    utime.sleep_ms(100)

    while True:
        v1 = randint(0,100)
        v2 = int(gc.mem_free()/1024)

        for i in range(20):
            gc.collect()
            g1.update(move_to(v1,g1.value))
            print("Gauge 1: {}  Free Memory: {}".format(g1.value,v2))
            utime.sleep_ms(100)

main()
