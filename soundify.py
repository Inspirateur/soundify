#!/usr/bin/env python3
"""
Soundify main file
"""

import numpy as np
from numpy.fft import rfft, rfftfreq, irfft
from hilbert import hilbert
from colors import color2number, number2color


def dispay_sound(sound):
    """
    display the sound
    """
    nbsamples = len(sound)
    # sampling frequency
    frate = 44100.
    # time and frequency array
    time = np.linspace(0., nbsamples / frate, nbsamples)
    freq = rfftfreq(nbsamples, 1 / frate)




def image2music(image):
    """
    convert an image (numpy array of pixel (rgb(a?))) into a numpy array
    """
    # converting image into frequency spectrum
    spectrum = color2number(image)
    sound = irfft(spectrum)
    # used for debugging
    dispay_sound(sound)
    return sound

def music2image(music):
    """
    convert an music (array of amplitude) into a numpy array of color
    """
    spectrum = rfft(music)
    image = number2color(spectrum)
    return image


def main():
    """
    main function here
    """

    pass

if __name__ == "__main__":
    main()
