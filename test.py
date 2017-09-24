#!/usr/bin/env python3
"""
module soundify to transform your pictures into sounds
"""
# std import
from math import log
import numpy as np
import matplotlib.pyplot as plt
# custom import
from PIL import Image
from hilbert import hilbert

IMG = Image.open('aubergine.jpg')
n = int(log(IMG.size[0], 2))

red, green, blue = IMG.split()

values = bytearray(IMG.size[0]*IMG.size[1])

for i, (x, y) in enumerate(hilbert(n)):
    # values[i] = int((red.getpixel((x, y)) + green.getpixel((x, y)) + blue.getpixel((x, y)))/3)
    break

time = np.linspace(0, len(values) / 44100, num=len(values))
sound = np.sin(440 / 2 * np.pi * time)


plt.figure(0)
plt.plot(time, sound)

spectrum = np.fft.rfft(sound)
for e in spectrum:
    if np.absolute(e) > 100. :
        print(e)
# freq = np.linspace(44100 / len(values), 2*44100, num=len(spectrum))
# plt.figure(1)
# plt.semilogx(freq, spectrum, marker="+")
# plt.show()
