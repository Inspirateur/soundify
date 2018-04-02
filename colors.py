#!/usr/bin/env python3
"""
Test on color picking with angle and amplitude of a complex number
"""

import numpy as np

#pylint:disable=invalid-name
def colorWheel(colors):
    """
    return the angle associated with a particular color
    """
    return 2 * np.pi / 3 * np.sum(colors, axis=1) % (2 * np.pi)

def hls2rgb(hls):
    """
    convert array of hls values into array of rgb values
    """
    # used for indexing
    H, L, S = 0, 1, 2
    # same notation as wikipedia
    C = (1 - np.abs(2*hls.T[L] - 1))*hls.T[S]
    rgb = hls
    return rgb

def color2number(colors):
    """
    take a color (triplet of float between 0 and 1), and return the complex
    number in the unit sphere associated to it
    """
    modules = 1/3 * np.sum(colors, axis=1)
    angles = colorWheel(colors)
    return modules * np.exp(1j*angles)

def number2color(numbers):
    """
    take a complex number with module between 0 and 1 and return the color
    associated to it
    """
    #  we don't want any amplitude greater to 1
    assert (np.abs(numbers) <= 1).all()
    modules, angles = np.abs(numbers), np.angle(numbers)
    # generating hls values for each complex numbers
    hls = np.array(angles*180/np.pi + 180,
                   (1 - modules),
                   np.ones(np.shape(numbers))).T
    colors = hls2rgb(hls)
    return colors
