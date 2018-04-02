#!/usr/bin/env python3
"""
Test on color picking with angle and amplitude of a complex number
"""

import numpy as np

#pylint:disable=invalid-name
def rgb2hsl(rgb):
    """
    convert array of rgb values into array of hsl values
    """
    mins, maxes = np.min(rgb, axis=1), np.max(rgb, axis=1)

    hsl = rgb
    return hsl


def hsl2rgb(hsl):
    """
    convert array of hsl values into array of rgb values
    """
    # getting each component independently
    hue, sat, light = hsl.T
    # same notation as wikipedia
    chroma = (1. - np.abs(2.*light - 1.))*sat
    hprime = hue / 60.
    X = chroma * (1. - np.abs(hprime % 2. - 1.))

    # creating masks for computing rgb
    masks = np.array([None for _ in range(6)])
    for i in range(6):
        masks[i] = (i <= hprime) & (hprime < i + 1)

    # calculating each component reffering to wikipedia tables
    R1 = np.array(C * (masks[0] | masks[5])
                  + X * (masks[1] | masks[4]))
    G1 = np.array(C * (masks[1] | masks[2])
                  + X * (masks[0] | masks[3]))
    B1 = np.array(C * (masks[3] | masks[4])
                  + X * (masks[2] | masks[5]))
    m = light - 1./2. * chroma

    rgb = np.array((R1 + m, G1 + m, B1 + m)).T
    return rgb


def color2number(colors):
    """
    take a color (triplet of float between 0 and 1), and return the complex
    number in the unit disk associated to it
    """
    # colors are floats in [0, 1]
    assert ((0 <= colors) & (colors <= 1)).all()
    # grey scale
    hsl = rgb2hsl(colors)
    modules = 1/3 * np.sum(colors, axis=1)
    angles = colorWheel(colors)
    return modules * np.exp(1j*angles)


def number2color(numbers):
    """
    take a complex vector with module between 0 and 1 and return the color
    associated to it
    """
    #  we don't want any amplitude greater to 1
    assert (np.abs(numbers) <= 1).all()

    # generating hsl values for each complex numbers
    hsl = np.array((
        (np.angle(numbers) * 180./np.pi) % 360.,    # angle in [0, 360[
        np.ones(np.shape(numbers)),                 # saturation (always 1)
        np.abs(numbers),                            # lightness
    )).T
    colors = hsl2rgb(hsl)
    return colors
