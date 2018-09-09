#!/usr/bin/env python3
"""
Test file for dialogue with system
"""
import soundify_io as io
import numpy as np
from hilbert import hilbert


def test_sound():
    # testing homogeneity
    sound = io.read_sound("saw.wav")
    io.write_sound("export.wav", sound.data, sound.frate)


def test_image():
    # testing homogeneity
    image = io.read_image("chess_board.png", hilbert)
    print(image.format, image.size, image.mode)
    io.write_image("export.png", image)



def main():
    test_sound()
    test_image()
    

if __name__ == "__main__":
    main()