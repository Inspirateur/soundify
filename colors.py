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

    hue = np.array(
        masks[0] * 60. * (
            masks[1] * (((green - blue) / delta) % 6.)
            + masks[2] * ((blue - red) / delta + 2.)
            + masks[3] * ((red - green)/ delta + 4.)
        )
    )

    sat = masks[0] * delta / (1. - np.abs(2. * light - 1.))
    return np.array((hue, sat, light)).T


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
    R1 = np.array((masks[0] | masks[5]) * chroma
                  + (masks[1] | masks[4]) * X)
    G1 = np.array((masks[1] | masks[2]) * chroma
                  + (masks[0] | masks[3]) * X)
    B1 = np.array((masks[3] | masks[4]) * chroma
                  + (masks[2] | masks[5]) * X)
    m = light - 1./2. * chroma

    rgb = np.array((R1 + m, G1 + m, B1 + m)).T
    rgb = np.where(rgb <= 0., 0, rgb)
    return rgb


def color2number(colors):
    """
    take a color (triplet of float in [0, 1]), and return the complex
    number in the unit disk associated to it
    """
    # colors are floats in [0, 1]
    assert ((colors >= 0.) & (colors <= 1.)).all()
    # grey scale
    hue, sat, light = rgb2hsl(colors).T
    return light * np.exp(1j*(hue * np.pi / 180.))


def number2color(numbers):
    """
    take a complex vector with module between 0 and 1 and return the color
    associated to it
    """
    #  we don't want any amplitude greater to 1
    assert (np.abs(numbers) <= 1.).all()

    # generating hsl values for each complex numbers
    hsl = np.array((
        (np.angle(numbers) * 180./np.pi) % 360.,    # angle in [0, 360[
        np.ones(np.shape(numbers)),                 # saturation (always 1)
        np.abs(numbers),                            # lightness
    )).T
    return hsl2rgb(hsl)
