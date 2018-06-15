#!/usr/bin/env python3
"""
Test on color picking with angle and amplitude of a complex number
"""

import numpy as np

#pylint:disable=invalid-name
def rgb2hsl(rgb):
    """
    convert array of rgb values into array of hsl
    """
    # getting components independentely
    red, green, blue = rgb.T
    # basic algorithm to calculate hsl values from rgb numpy compatible
    mins, maxes = np.min(rgb, axis=1), np.max(rgb, axis=1)

    diff = maxes - mins
    add = maxes + mins
    light = add / 2

    lightmask = light <= 0.5

    zero = diff == 0.

    sat = np.where(zero,
                   0.,
                   np.where(lightmask, diff / add, diff / (2. - add)))

    masks = [color == maxes for color in rgb.T]
    hue = 60. * np.where(zero, 0,
                         np.where(masks[0], (green - blue) / diff,
                                  np.where(masks[1], (2. + (blue - red) / diff),
                                           (4. + (red - green) / diff))))

    hsl = np.array([hue, sat, light]).T
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
    masks = [(i <= hprime) & (hprime < i + 1) for i in range(6)]

    # calculating each component reffering to wikipedia tables
    R1 = (masks[0] | masks[5]) * chroma + (masks[1] | masks[4]) * X
    G1 = (masks[1] | masks[2]) * chroma + (masks[0] | masks[3]) * X
    B1 = (masks[3] | masks[4]) * chroma + (masks[2] | masks[5]) * X

    m = light - 1./2. * chroma

    rgb = np.array((R1 + m, G1 + m, B1 + m)).T
    rgb = np.where(rgb <= 0., 0., rgb)
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
    return light * sat * np.exp(1j * hue * np.pi / 180.)


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
