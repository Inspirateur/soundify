"""
Implementation that works for this way of convertion
"""

import numpy as np

#pylint:disable=invalid-name
def rgb2hsl(rgb):
    """
    convert array of rgb values into array of hsl values
    """
    # getting components independentely
    red, green, blue = rgb.T
    # basic algorithm to calculate hsl values from rgb numpy compatible
    mins, maxes = np.min(rgb, axis=1), np.max(rgb, axis=1)
    light = (mins + maxes) / 2.
    delta = maxes - mins

    masks = np.array([None for _ in range(4)])
    masks[0] = (delta != 0.)
    for i in range(1, 4):
        masks[i] = (rgb.T[i-1] == maxes)

    hue = np.where(
        masks[0],
        60. * (
            masks[1] * (((green - blue) / delta) % 6.)
            + masks[2] * ((blue - red) / delta + 2.)
            + masks[3] * ((red - green)/ delta + 4.)
        ),
        0
    )

    sat = np.where(
        masks[0],
        delta / (1. - np.abs(2. * light - 1.)),
        0
    )
    return np.array((hue, sat, light)).T

def color2number(colors):
    """
    take a color (triplet of float in [0, 1]), and return the complex
    number in the unit disk associated to it
    """
    # colors are floats in [0, 1]
    assert ((colors >= 0.) & (colors <= 1.)).all()
    # grey scale
    hue, sat, light = rgb2hsl(colors).T
    return light * sat * np.exp(1j*(hue * np.pi / 180.))
