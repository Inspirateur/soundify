#!/usr/bin/env python3
"""
Soundify main file
"""
import sys, os
import numpy as np
from numpy.fft import rfft, rfftfreq, irfft
import matplotlib.pyplot as plt
from hilbert import hilbert
from colors import color_to_number, number_to_color
import soundify_io as sdfio 

SOUND_EXT = ['wav']
IMAGE_EXT = ['png', 'jpg']

def image_to_sound(image):
    """
    convert an image (numpy array of pixel (rgb(a?))) into a numpy array representing sound
    """
    # converting image into frequency spectrum
    spectrum = color_to_number(image)
    sound = irfft(len(spectrum) / 2 * spectrum)
    return sound


def sound_to_image(sound):
    """
    convert an music (array of amplitude) into a numpy array of color
    """
    image = number_to_color(2 / len(sound) * rfft(sound))
    return image


def main():
    """
    main function here
    """
    input_file = input("input file : ")
    output_file = input("output file : ")

    input_ext = input_file.split('.')[-1]
    output_ext = output_file.split('.')[-1]

    if input_ext in SOUND_EXT:
        sound = sdfio.read_sound(input_file)
        image = sound_to_image(sound.data)
        print(np.shape(image))
        if output_ext in SOUND_EXT:
            result = image_to_sound(image)
            print(np.shape(result))
            sdfio.write_sound(output_file , result, sound.frate)




if __name__ == "__main__":
    main()
