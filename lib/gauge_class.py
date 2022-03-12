""""
Gauge Class

   A gauge that can be placed anywhere on a TFT screen
"""

import utime
import math
import st7789
import vga1_8x16 as fonts
import vga1_bold_16x16 as fontl
import vga1_bold_16x32 as fontxl


class gauge:

    def __init__(self, display, xpos, ypos, box, color_hint, units="Units", low=0, high=100, bg=st7789.WHITE, fg=st7789.BLACK):
        print("Gauge Init")
        self.value = None
        self.low = low
        self.high = high
        self.range = high - low
        self.factor = 270/self.range # this is a 270 gauge
        self.prev_value = None
        self.display = display
        self.xpos = xpos
        self.ypos = ypos
        self.box = box
        self.fg = fg
        self.bg = bg
        self.center_x = int(box/2)+xpos
        self.center_y = int(box/2)+ypos
        self.center_text_y_offset = int(0.7 * box)
        self.center_value_y_offset = int(0.86 * box)
        self.hub = 4 # this is the centre hub
        if box > 200:
            self.font = fontl
        elif box > 220:
            self.font = fontxl
        else:
            self.font = fonts
        bg = "../jpg/g{}{}.jpg".format(box,color_hint)
        display.jpg(bg,xpos,ypos,st7789.SLOW)
        pointer_len = int(box * 0.60 / 2)
        self.pointer_poly = self.hand_polygon(pointer_len, 1)
        display.bounding(True)
        self.pointer_bound = display.bounding(True)
        self.show_units(units)

    def hand_polygon(self, length, radius):
        return [
            (0, 0),
            (-radius, radius),
            (-radius, int(length * 0.3)),
            (-1, length),
            (1, length),
            (radius, int(length * 0.3)),
            (radius, radius),
            (0,0)
        ]

    def center(self, text):
        length = len(text)
        self.display.text(
            self.font,
            text,
            self.xpos + self.box // 2 - length // 2 * self.font.WIDTH,
            self.ypos + self.center_text_y_offset,
            self.fg,
            self.bg)

    def show_units(self, text):
        length = len(text)
        self.display.text(
            self.font,
            text,
            self.xpos + self.box // 2 - length // 2 * self.font.WIDTH,
            self.ypos + self.center_value_y_offset,
            self.fg,
            self.bg)

    def update(self,value):
        # don't do anything unless we have to!
        if value == self.prev_value:
            return
        self.value = value
        # calculate the angle of pointer in radians
        displace = self.factor * value
        pointer_ang = math.radians(displace+45)  # 270 range gauge
        # print("Pointer Angle: {} iteration: {}".format(pointer_ang, value))  # only for debug
        self.center(" {} ".format(value))

        # erase the bounding area of the last drawn pointer
        x1, y1, x2, y2 = self.pointer_bound
        self.display.fill_rect(x1, y1, x2, y2, self.bg)

        # draw the hub after erasing the bounding areas to reduce flickering
        self.display.fill_circle(self.center_x, self.center_y, self.hub, self.fg)
        self.display.bounding(True)      # clear bounding rectangle

        # draw and fill the pointer
        self.display.fill_polygon(self.pointer_poly, self.center_x, self.center_y, st7789.RED, pointer_ang)

        # get the bounding rectangle of the pointer_polygon as drawn and
        # reset the bounding box for the next polygon
        self.pointer_bound = self.display.bounding(True, True)

        # draw the hub again to cover up the second hand
        self.display.fill_circle(self.center_x, self.center_y, self.hub, self.fg)
        self.prev_value = value # for next time round

