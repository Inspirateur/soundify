#!/usr/bin/env python3
"""
module soundify to transform your pictures into sounds
"""

from PIL import Image
from math import log
from hilbert import hilbert

IMG = Image.open('image.jpg')
n = int(log(IMG.size[0], 2))

values = bytearray(IMG.size[0]*IMG.size[1])


for i, (x, y) in enumerate(hilbert(n)):
    val = IMG.getpixel((x,y))
    values[i] = val

print(255 in values)
