#!/usr/bin/env python3
"""
module that manage the interaction with source files
"""

import numpy as np
import soundfile as sf
from PIL import Image as pil

from sound import Sound
from image import Image

def read_sound(filename : str):
    sound, samplerate = sf.read(filename)
    return Sound(sound, samplerate)


def write_sound(filename : str, sound, samplerate):
    sf.write(filename, sound, samplerate)
    #TODO : add rename of filename if already existing

def read_music(filename : str, blocksize):
    music = np.array(sf.blocks(filename, blocksize))
    return music

def read_image(filename : str, sweeping_func):
    image = pil.open(filename).convert('RGB')
    return Image(image, sweeping_func)


def write_image(filename : str, image):
    image.save(filename)

