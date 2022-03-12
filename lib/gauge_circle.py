""""
Gauge Circle

   A gauge that can be placed anywhere on a TFT screen, uses a circle as a pointer

   Expects to find background JPGs in /jpg
"""

import math
import st7789
import vga1_16x16 as fontl
import vga1_8x16 as font
from posXY100 import posXY

class gauge:

    def __init__(self, display, xpos, ypos, box, color_hint, units='Units', bg=st7789.WHITE, fg=st7789.BLACK):
        print("Gauge Init")
        self.value = None
        self.prev_value = None
        self.display = display
        self.xpos = xpos
        self.ypos = ypos
        self.box = box
        self.fg = fg
        self.bg = bg
        self.hub = 4 # this is the pointer diameter
        bg = "../jpg/g{}{}.jpg".format(box,color_hint)
        display.jpg(bg,xpos,ypos,st7789.SLOW)
        self.show_units(units)

    def center(self, text):
        length = len(text)
        self.display.text(
            fontl,
            text,
            self.xpos + 26,
            self.ypos + 44,
            self.fg,
            self.bg)

    def show_units(self, text):
        length = len(text)
        self.display.text(
            font,
            text,
            self.xpos + self.box // 2 - length // 2 * font.WIDTH,
            self.ypos + 86,
            self.fg,
            self.bg)

    def update(self,value):
        # don't do anything unless we have to!
        if value == self.prev_value:
            return
        self.value = value
        # calculate the position of pointer
        x, y = posXY[int(value)]

        # print("Pointer position X: {} Y: {}".format(pointer_ang, value))  # only for debug
        self.center("{:003d}".format(value))

        # erase the bounding area of the last drawn pointer
        if self.prev_value != None:
            px, py = posXY[int(self.prev_value)]
            self.display.fill_circle(self.xpos+px, self.ypos+py, self.hub, self.bg)
        
        # draw and fill the pointer
        self.display.fill_circle(self.xpos+x, self.ypos+y, self.hub, st7789.RED)

        self.prev_value = value # for next time round

