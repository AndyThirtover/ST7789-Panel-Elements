""""
Meter

   A Meter that can be placed anywhere on a TFT screen

   note:  b = __import__('MeterBezelAlt2')   <-- this works
"""

import utime
import math
import st7789
import vga1_8x8 as fonts
import vga1_8x16 as fontl
import vga1_bold_16x32 as fontxl
from lib.panel_helpers import chunked_bitmap
import gc

class Meter:

    def __init__(self, display, xpos, ypos, xbox, ybox, legend="Legend", bezel="bitmap.MeterBezel", max=1000, bg=st7789.WHITE, lc=st7789.RED, fg=st7789.BLACK):
        print("Screen Meter Init at {},{}".format(xpos,ypos))
        self.value = None
        self.prev_value = None
        self.display = display
        self.xpos = xpos
        self.ypos = ypos
        self.xbox = xbox
        self.ybox = ybox
        self.max = max
        self.fg = fg
        self.lc = lc
        self.bg = bg
        self.center_x = int(xbox/2)+xpos
        self.center_y = int(ybox/2)+ypos
        self.center_x = int(xbox/2)+xpos
        self.center_y = int(ybox/2)+ypos
        self.center_legend_y_offset = int(0.75 * ybox)
        self.center_value_y_offset = int(0.1 * ybox)
        self.font_value = fontl
        if xbox > 200:
            self.font = fontl
        elif xbox > 220:
            self.font = fontxl
        else:
            self.font = fonts
        # display Bezel
        meterBez = __import__(bezel)  # import the bitmap .py file - careful with this!
        ref = bezel.replace('bitmap.','')  # reference to the object in the .py file
        print("Ref: {} from {}".format(ref,bezel))
        chunked_bitmap(display,getattr(meterBez,ref),xpos,ypos)
        gc.collect()
        self.show_legend(legend)

    def show_legend(self, text):
        length = len(text)
        self.display.text(
            self.font,
            text,
            self.xpos + self.xbox // 2 - length // 2 * self.font.WIDTH,
            self.ypos + self.center_legend_y_offset,
            self.fg,
            self.bg)


    def show_value(self, text):
        length = len(text)
        self.display.text(
            self.font_value,
            text,
            self.xpos + self.xbox // 2 - length // 2 * self.font_value.WIDTH,
            self.ypos + self.center_value_y_offset,
            self.lc,
            self.bg)


    def update(self,value):
        # don't do anything unless we have to!
        if value == self.prev_value:
            return
        self.value = value # so that we can be queried about our current value
        if value > self.max:
            self.show_value(" #### ")
        else:
            if isinstance(value, int):
                self.show_value(" {} ".format(value))
            else:
                self.show_value(" {:.1f} ".format(value))
        self.prev_value = value # for next time round

