#!/usr/bin/env python3
"""
internal image class
"""

import numpy as np

class Image:
    def __init__(self, image, sweeping_func):
        self.size = image.size
        self.mode = image.mode
        self.format = image.format
        self.sweep = sweeping_func
        self.data = Image._generate_data(image, sweeping_func)


    @staticmethod
    def _generate_data(image, sweeping_func):
        data = np.zeros((np.prod(image.size), 3))
        for i, point in enumerate(sweeping_func(image.size)):
            data[i] = image.getpixel(point)
        return data