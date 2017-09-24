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
sound = .5 * np.sin(2 * np.pi * 440 * time)


plt.figure(0)
plt.plot(time, sound, marker='+')

fsound = np.fft.rfft(sound, len(sound))
spectrum = np.absolute(fsound)

freq = np.linspace(44100 / len(values), 44100, num=len(spectrum))
plt.figure(1)
plt.semilogx(freq, spectrum, marker="+")

sample = np.fft.irfft(spectrum, len(fsound))

time = np.linspace(0, len(sample) / 44100, num=len(sample))
plt.figure(2)
plt.plot(time, sample, marker='+')


spectrum = np.absolute(np.fft.rfft(sound, len(sound)))
freq = np.linspace(44100 / len(values), 44100, num=len(spectrum))
plt.figure()
plt.semilogx(freq, spectrum, marker="+")

plt.show()

