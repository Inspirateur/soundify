#!/usr/bin/env python3
"""
Soundify main file
"""

import numpy as np
from numpy.fft import rfft, rfftfreq, irfft
import matplotlib.pyplot as plt
from hilbert import hilbert
from colors import color_to_number, number_to_color


def image_to_music(image):
    """
    convert an image (numpy array of pixel (rgb(a?))) into a numpy array representing sound
    """
    # converting image into frequency spectrum
    spectrum = color_to_number(image)
    sound = irfft(len(spectrum) / 2 * spectrum)
    return sound


def music_to_image(music):
    """
    convert an music (array of amplitude) into a numpy array of color
    """
    image = number_to_color(2 / len(music) * rfft(music))
    return image


def main():
    """
    main function here
    """
    pass

if __name__ == "__main__":
    main()
