#!/usr/bin/env python3
"""
module that manage the interaction with source files
"""

import numpy as np
import soundfile as sf
from PIL import Image as pil

from sound import Sound
from image import Image

def read_sound(filename: str):
    """
    open a sound as numpy array
    """
    sound, samplerate = sf.read(filename)
    return Sound(sound, samplerate)


def write_sound(filename: str, sound, samplerate):
    """
    write sound to file
    """
    #TODO: add rename of filename if already existing
    sf.write(filename, sound, samplerate)


def read_music(filename: str, blocksize):
    """
    open music as list of sounds
    """
    music = np.array(sf.blocks(filename, blocksize))
    return music

def read_image(filename: str, sweeping_func):
    """
    open an image parsed by the sweeping_func
    """
    image = pil.open(filename)
    return Image(image, sweeping_func)


def write_image(filename: str, image):
    """
    save image to file
    """
    image.save(filename)
