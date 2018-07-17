#!/usr/bin/env python3
"""
module that manage the interaction with source files
"""

import numpy as np
import soundfile as sf

def read_sound(filename : str):
    sound, samplerate = sf.read(filename)
    return np.fft.rfft(sound), samplerate

def write_sound(filename : str, sound, samplerate):
    sf.write(filename, sound, samplerate)
    #TODO : add rename of filename if already existing