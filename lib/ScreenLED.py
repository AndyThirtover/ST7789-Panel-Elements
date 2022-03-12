""""
Gauge Screen LED

   A LED that can be placed anywhere on a TFT screen
"""

import utime
import math
import st7789
import vga1_8x8 as fonts
import vga1_bold_16x16 as fontl
import vga1_bold_16x32 as fontxl

class LED:

    def __init__(self, display, xpos, ypos, box, legend="Legend", diameter=5, bg=st7789.WHITE, lc=st7789.RED, fg=st7789.BLACK):
        print("Screen LED Init at {},{}".format(xpos,ypos))
        self.state = None
        self.prev_state = None
        self.display = display
        self.xpos = xpos
        self.ypos = ypos
        self.box = box
        self.diameter = diameter
        self.fg = fg
        self.lc = lc
        self.bg = bg
        self.center_x = int(box/2)+xpos
        self.center_y = int(box/2)+ypos
        self.center_x = int(box/2)+xpos
        self.center_y = int(box/2)+ypos
        self.center_legend_y_offset = int(0.86 * box)
        if box > 200:
            self.font = fontl
        elif box > 220:
            self.font = fontxl
        else:
            self.font = fonts
        self.show_legend(legend)
        # Create an outline, 1px larger than LED diameter
        self.display.fill_circle(self.center_x, self.center_y, self.diameter+2, self.fg)

    def show_legend(self, text):
        length = len(text)
        self.display.text(
            self.font,
            text,
            self.xpos + self.box // 2 - length // 2 * self.font.WIDTH,
            self.ypos + self.center_legend_y_offset,
            self.fg,
            self.bg)

    def update(self,state):
         # don't do anything unless we have to!
         if state == self.prev_state:
            return
         self.state = state

         # draw the LED
         if state:
            colour = self.lc
         else:
            colour = self.bg

         self.display.fill_circle(self.center_x, self.center_y, self.diameter, colour)
         self.prev_state = state # for next time round
