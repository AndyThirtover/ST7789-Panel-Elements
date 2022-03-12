""""
Meter

   A Meter that can be placed anywhere on a TFT screen
"""

import utime
import math
import st7789
import vga1_8x8 as fonts
import vga1_bold_16x16 as fontl
import vga1_bold_16x32 as fontxl

class Meter:

    def __init__(self, display, xpos, ypos, xbox, ybox, legend="Legend", bg=st7789.WHITE, lc=st7789.RED, fg=st7789.BLACK):
        print("Screen Meter Init at {},{}".format(xpos,ypos))
        self.value = None
        self.prev_value = None
        self.display = display
        self.xpos = xpos
        self.ypos = ypos
        self.xbox = xbox
        self.ybox = ybox
        self.fg = fg
        self.lc = lc
        self.bg = bg
        self.center_x = int(xbox/2)+xpos
        self.center_y = int(ybox/2)+ypos
        self.center_x = int(xbox/2)+xpos
        self.center_y = int(ybox/2)+ypos
        self.center_legend_y_offset = int(0.7 * ybox)
        self.center_value_y_offset = int(0.1 * ybox)
        self.font_value = fontl
        if xbox > 200:
            self.font = fontl
        elif xbox > 220:
            self.font = fontxl
        else:
            self.font = fonts
        bg =  '../jpg/MeterBezel.jpg'             #  calculation hint "../jpg/g{}{}.jpg".format(box,color_hint)
        display.jpg(bg,xpos,ypos,st7789.SLOW)

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
        self.show_value(" {} ".format(value))
        self.prev_value = value # for next time round
