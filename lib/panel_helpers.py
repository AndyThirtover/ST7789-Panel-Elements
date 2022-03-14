"""
Panel elements helper functions.
"""

def chunked_bitmap ( display, bitmapref, xpos, ypos):
    # display a bitmap in chunks, useful for memory allocation errors when dealing with larger bitmaps
    # chunks are assumed to be equally divided in hieght
    if hasattr(bitmapref,'BITMAPS'):
        # chunks available, deal with them
        for i in range(bitmapref.BITMAPS):
            display.bitmap(bitmapref,xpos,(i*bitmapref.HEIGHT)+ypos,i)
    else:
        display.bitmap(bitmapref,xpos,ypos)  # no chunks just display

